"""Jednoblokowy model przyczynowy i jego backprop w NumPy."""

import numpy as np

TOKENS = ("<START>", "LEWY", "PRAWY", "0", "1", "a", "b", "c", "d", "<KONIEC>")
TOKEN_ID = {token: index for index, token in enumerate(TOKENS)}
ANSWER_POS = 5


def make_splits():
    """Rozłączne pary szumu, wszystkie pojedyncze symbole w każdym podziale."""
    vocab_noise = "abcd"
    groups = {"train": [], "val": [], "test": []}
    for i, left in enumerate(vocab_noise):
        for j, right in enumerate(vocab_noise):
            split = ("train", "train", "val", "test")[(j - i) % 4]
            for first in ("0", "1"):
                for second in ("0", "1"):
                    for command, answer in (("LEWY", first), ("PRAWY", second)):
                        row = ("<START>", first, second, left, right, command, answer, "<KONIEC>")
                        groups[split].append([TOKEN_ID[token] for token in row])
    return {name: (np.array(rows)[:, :-1], np.array(rows)[:, 1:]) for name, rows in groups.items()}


def decode(ids):
    return " ".join(TOKENS[i] for i in ids)


def softmax(x):
    exp_x = np.exp(x - x.max(axis=-1, keepdims=True))
    return exp_x / exp_x.sum(axis=-1, keepdims=True)


def log_softmax(x):
    shifted = x - x.max(axis=-1, keepdims=True)
    return shifted - np.log(np.exp(shifted).sum(axis=-1, keepdims=True))


def normalize(x):
    centered = x - x.mean(axis=-1, keepdims=True)
    inv_std = 1 / np.sqrt((centered**2).mean(axis=-1, keepdims=True) + 1e-5)
    return centered * inv_std, inv_std


def normalize_backward(gradient, normalized, inv_std):
    mean = gradient.mean(axis=-1, keepdims=True)
    projection = (gradient * normalized).mean(axis=-1, keepdims=True)
    return inv_std * (gradient - mean - normalized * projection)


def weight_gradient(inputs, delta):
    """Suma wkładów z osi batcha i pozycji."""
    return np.einsum("bti,bto->io", inputs, delta)


class MiniTransformer:
    """Pre-norm, jedna głowa attention, dwa residuale i FFN z ReLU."""

    def __init__(self, width=16, ff_width=32, seed=2026):
        rng = np.random.default_rng(seed)
        vocab = len(TOKENS)
        self.params = {
            "E": rng.normal(0, 0.2, size=(vocab, width)),
            "P": rng.normal(0, 0.2, size=(7, width)),
        }
        sizes = {
            "Q": (width, width),
            "K": (width, width),
            "V": (width, width),
            "O": (width, width),
            "F1": (width, ff_width),
            "F2": (ff_width, width),
            "U": (width, vocab),
        }
        for name, (fan_in, fan_out) in sizes.items():
            self.params[name] = rng.normal(0, 1 / np.sqrt(fan_in), size=(fan_in, fan_out))
        self.scale = np.sqrt(width)

    def forward(self, tokens):
        p = self.params
        length = tokens.shape[1]
        x = p["E"][tokens] + p["P"][:length]

        z, inv_z = normalize(x)
        q, k, v = z @ p["Q"], z @ p["K"], z @ p["V"]
        scores = q @ k.swapaxes(-1, -2) / self.scale
        future = np.triu(np.ones((length, length), dtype=bool), k=1)
        attention = softmax(np.where(future, -np.inf, scores))
        context = attention @ v
        h = x + context @ p["O"]

        u, inv_u = normalize(h)
        activation = np.maximum(0, u @ p["F1"])
        out = h + activation @ p["F2"]
        logits = out @ p["U"]
        cache = (z, inv_z, q, k, v, context, u, inv_u, activation, out)
        return logits, attention, cache

    def loss_and_gradients(self, tokens, targets):
        p = self.params
        logits, attention, cache = self.forward(tokens)
        z, inv_z, q, k, v, context, u, inv_u, activation, out = cache
        labels = targets[:, ANSWER_POS:]
        log_probs = log_softmax(logits[:, ANSWER_POS:])
        rows, positions = np.indices(labels.shape)
        loss = -log_probs[rows, positions, labels].mean()
        delta = np.exp(log_probs)
        delta[rows, positions, labels] -= 1
        d_logits = np.zeros_like(logits)
        d_logits[:, ANSWER_POS:] = delta / labels.size

        # Głowa słownikowa i FFN, wraz ze ścieżką resztową.
        grads = {"U": weight_gradient(out, d_logits)}
        d_out = d_logits @ p["U"].T
        grads["F2"] = weight_gradient(activation, d_out)
        d_ff = (d_out @ p["F2"].T) * (activation > 0)
        grads["F1"] = weight_gradient(u, d_ff)
        d_h = d_out + normalize_backward(d_ff @ p["F1"].T, u, inv_u)

        # Attention. W zamaskowanych miejscach waga i jej gradient wynoszą zero.
        grads["O"] = weight_gradient(context, d_h)
        d_context = d_h @ p["O"].T
        d_attention = d_context @ v.swapaxes(-1, -2)
        d_v = attention.swapaxes(-1, -2) @ d_context
        d_scores = attention * (d_attention - (d_attention * attention).sum(axis=-1, keepdims=True))
        d_q = d_scores @ k / self.scale
        d_k = d_scores.swapaxes(-1, -2) @ q / self.scale
        grads["Q"] = weight_gradient(z, d_q)
        grads["K"] = weight_gradient(z, d_k)
        grads["V"] = weight_gradient(z, d_v)
        d_z = d_q @ p["Q"].T + d_k @ p["K"].T + d_v @ p["V"].T
        d_x = d_h + normalize_backward(d_z, z, inv_z)

        # Ten sam embedding może wystąpić w wielu pozycjach i próbkach.
        grads["E"] = np.zeros_like(p["E"])
        np.add.at(grads["E"], tokens, d_x)
        grads["P"] = np.zeros_like(p["P"])
        grads["P"][:tokens.shape[1]] = d_x.sum(axis=0)
        return float(loss), grads

    def generate(self, prefix, max_new=2):
        result = list(prefix)
        for _ in range(max_new):
            logits, _, _ = self.forward(np.array([result]))
            result.append(int(logits[0, -1].argmax()))
            if result[-1] == TOKEN_ID["<KONIEC>"]:
                break
        return result


class Adam:
    def __init__(self, params, lr=0.005):
        self.params = params
        self.lr = lr
        self.t = 0
        self.m = {name: np.zeros_like(weight) for name, weight in params.items()}
        self.v = {name: np.zeros_like(weight) for name, weight in params.items()}

    def step(self, grads):
        self.t += 1
        for name, grad in grads.items():
            self.m[name] = 0.9 * self.m[name] + 0.1 * grad
            self.v[name] = 0.999 * self.v[name] + 0.001 * grad**2
            m_hat = self.m[name] / (1 - 0.9**self.t)
            v_hat = self.v[name] / (1 - 0.999**self.t)
            self.params[name] -= self.lr * m_hat / (np.sqrt(v_hat) + 1e-8)


def measure(model, tokens, targets):
    logits, _, _ = model.forward(tokens)
    labels = targets[:, ANSWER_POS:]
    response_logits = logits[:, ANSWER_POS:]
    loss = -np.take_along_axis(log_softmax(response_logits), labels[..., None], axis=-1).mean()
    correct = logits[:, ANSWER_POS].argmax(axis=-1) == targets[:, ANSWER_POS]
    return float(loss), float(correct.mean())


def train_bigram(tokens, targets):
    """Najczęstszy następnik w treningu dla każdego bieżącego tokenu."""
    counts = np.zeros((len(TOKENS), len(TOKENS)), dtype=int)
    np.add.at(counts, (tokens, targets), 1)
    return counts.argmax(axis=-1)
