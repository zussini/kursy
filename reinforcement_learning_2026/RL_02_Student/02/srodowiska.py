"""Dyskretne środowiska do ćwiczeń. Numery akcji: lewo, dół, prawo, góra."""

from collections import Counter


class FrozenLake:
    """Jedna plansza 4×4 dla programowania dynamicznego i uczenia z próbek."""

    tiles = ("SFFF", "FHFH", "FFFH", "HFFG")
    rows, cols = 4, 4
    n_states = rows * cols
    start = 0
    actions = (0, 1, 2, 3)
    action_names = ("lewo", "dół", "prawo", "góra")
    motion = ((0, -1), (1, 0), (0, 1), (-1, 0))

    def __init__(self, slippery=False):
        self.slippery = slippery

    def terminal(self, state):
        row, col = divmod(state, self.cols)
        return self.tiles[row][col] in "HG"

    def _move(self, state, action):
        row, col = divmod(state, self.cols)
        dr, dc = self.motion[action]
        row = min(max(row + dr, 0), self.rows - 1)
        col = min(max(col + dc, 0), self.cols - 1)
        nxt = row * self.cols + col
        return nxt, int(self.tiles[row][col] == "G"), self.terminal(nxt)

    def outcomes(self, state, action):
        """Zwróć gałęzie (prawdopodobieństwo, następny stan, nagroda, koniec)."""
        if self.terminal(state):
            return ((1.0, state, 0, True),)
        directions = (
            ((action - 1) % 4, action, (action + 1) % 4)
            if self.slippery
            else (action,)
        )
        counts = Counter(self._move(state, direction) for direction in directions)
        return tuple(
            (count / len(directions), nxt, reward, done)
            for (nxt, reward, done), count in counts.items()
        )

    def sample(self, state, action, rng):
        """Zwróć jedną próbkę (następny stan, nagroda, koniec)."""
        branches = self.outcomes(state, action)
        if len(branches) == 1:
            return branches[0][1:]
        selected, = rng.choices(branches, weights=[branch[0] for branch in branches])
        return selected[1:]


class CliffWalking:
    """Plansza 4×12. Upadek zwraca do startu z nagrodą −100 w tym samym epizodzie."""

    rows, cols = 4, 12
    n_states = rows * cols
    start, goal = 36, 47
    actions = FrozenLake.actions
    action_names = FrozenLake.action_names
    motion = FrozenLake.motion

    def terminal(self, state):
        return state == self.goal

    def sample(self, state, action, rng):
        if self.terminal(state):
            return state, 0, True
        row, col = divmod(state, self.cols)
        dr, dc = self.motion[action]
        row = min(max(row + dr, 0), self.rows - 1)
        col = min(max(col + dc, 0), self.cols - 1)
        nxt = row * self.cols + col
        if self.start < nxt < self.goal:
            return self.start, -100, False
        return nxt, -1, self.terminal(nxt)

    def outcomes(self, state, action):
        return ((1.0, *self.sample(state, action, None)),)
