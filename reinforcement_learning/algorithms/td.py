"""
Temporal Difference (TD):
- TD(0) prediction: V(s)
- SARSA: on-policy control
- Q-learning: off-policy control
"""

from __future__ import annotations
from typing import Callable, Tuple, Optional
import numpy as np
from .utils import epsilon_greedy


def td0_prediction(env, policy: Callable[[int], int], nS: int, gamma: float = 0.99, alpha: float = 0.1, episodes: int = 10_000, max_steps: int = 10_000):
    V = np.zeros(nS, dtype=np.float64)

    for _ in range(episodes):
        s, _ = env.reset()
        for _ in range(max_steps):
            a = int(policy(int(s)))
            sp, r, terminated, truncated, _ = env.step(a)
            sp = int(sp)
            # TODO: TD(0) target: r + gamma*V(s') (0 jeśli terminal)
            target = r + (0.0 if (terminated or truncated) else gamma * V[sp])
            # TODO: TD update: V(s) <- V(s) + alpha*(target - V(s))
            V[int(s)] += alpha * (target - V[int(s)])
            s = sp
            if terminated or truncated:
                break
    return V


def sarsa(env, nS: int, nA: int, gamma: float = 0.99, alpha: float = 0.1, epsilon: float = 0.1, episodes: int = 20_000, seed: int = 0, max_steps: int = 10_000):
    rng = np.random.default_rng(seed)
    Q = np.zeros((nS, nA), dtype=np.float64)

    for _ in range(episodes):
        s, _ = env.reset()
        s = int(s)
        a = epsilon_greedy(Q[s], epsilon=epsilon, rng=rng)
        for _ in range(max_steps):
            sp, r, terminated, truncated, _ = env.step(a)
            sp = int(sp)
            if terminated or truncated:
                target = r
                Q[s, a] += alpha * (target - Q[s, a])
                break
            # TODO: SARSA: wybieramy a' zgodnie z tą samą polityką (on-policy)
            ap = epsilon_greedy(Q[sp], epsilon=epsilon, rng=rng)
            # TODO: TD(0) target: r + gamma*V(s') (0 jeśli terminal)
            target = r + gamma * Q[sp, ap]
            Q[s, a] += alpha * (target - Q[s, a])
            s, a = sp, ap

    pi_greedy = np.argmax(Q, axis=1)
    return Q, pi_greedy


def q_learning(env, nS: int, nA: int, gamma: float = 0.99, alpha: float = 0.1, epsilon: float = 0.1, episodes: int = 20_000, seed: int = 0, max_steps: int = 10_000):
    rng = np.random.default_rng(seed)
    Q = np.zeros((nS, nA), dtype=np.float64)

    for _ in range(episodes):
        s, _ = env.reset()
        s = int(s)
        for _ in range(max_steps):
            a = epsilon_greedy(Q[s], epsilon=epsilon, rng=rng)
            sp, r, terminated, truncated, _ = env.step(a)
            sp = int(sp)
            if terminated or truncated:
                target = r
                Q[s, a] += alpha * (target - Q[s, a])
                break
            # TODO (student): TD(0) target: r + gamma*V(s') (0 jeśli terminal)
            target = r + gamma * np.max(Q[sp])
            Q[s, a] += alpha * (target - Q[s, a])
            s = sp

    pi_greedy = np.argmax(Q, axis=1)
    return Q, pi_greedy
