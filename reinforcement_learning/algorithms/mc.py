"""
Monte Carlo (model-free) dla środowisk dyskretnych.
- prediction: V(s) z pełnych epizodów
- control: first-visit MC control (ε-greedy)
"""

from __future__ import annotations
from typing import Callable, Tuple, Optional
import numpy as np
from .utils import rollout_episode, returns_from_trajectory, epsilon_greedy


def mc_prediction(env, policy: Callable[[int], int], nS: int, gamma: float = 0.99, episodes: int = 10_000, max_steps: int = 10_000):
    V = np.zeros(nS, dtype=np.float64)
    N = np.zeros(nS, dtype=np.int64)

    for _ in range(episodes):
        traj = rollout_episode(env, policy, max_steps=max_steps)
        # TODO: policz zwroty G_t dla każdego kroku (tu: helper w utils returns_from_trajectory)
        Gs = returns_from_trajectory(traj, gamma) # stworzyć zmienna Gs - zwrot z danej trajektorii
        visited = set() # stworzyć zbiór visited
        for (t, (s, a, r)) in enumerate(traj):
            # TODO: first-visit MC: aktualizuj stan tylko przy pierwszym wystąpieniu w epizodzie
            if s in visited:
                continue  # first-visit
            visited.add(s) # aktualizacja listy visited
            G = Gs[t] # 
            N[s] += 1
            # TODO: aktualizacja średniej inkrementalnej V[s] - zgodnie ze wzorem
            V[s] += (G - V[s]) / N[s]
    return V, N

def mc_control_epsilon_greedy(
    env,
    nS: int,
    nA: int,
    gamma: float = 0.99,
    episodes: int = 50_000,
    epsilon: float = 0.1,
    seed: int = 0,
    max_steps: int = 10_000
):
    rng = np.random.default_rng(seed)                              # RNG: powtarzalność eksperymentów
    Q = np.zeros((nS, nA), dtype=np.float64)                       # Q(s,a): estymata wartości akcji
    N = np.zeros((nS, nA), dtype=np.int64)                         # N(s,a): licznik wizyt (do średniej inkrementalnej)

    def policy(s: int) -> int:
        return epsilon_greedy(Q[s], epsilon=epsilon, rng=rng)       # π_ε: zachowanie (behavior) = ε-greedy wprost z Q (on-policy)

    for _ in range(episodes):
        traj = rollout_episode(env, policy, max_steps=max_steps)    # traj = [(s,a,r), ...] z próbkowania środowiska (model-free)
        Gs = returns_from_trajectory(traj, gamma)                   # Gs[t] = G_t = r_t + γ r_{t+1} + ... (zwrot od kroku t)
        visited = set()                                             # visited: pilnuje FIRST-visit dla par (s,a) w tym epizodzie

        for t, (s, a, r) in enumerate(traj):
            key = (s, a)                                            # identyfikator pary stan–akcja
            if key in visited:
                continue                                            # first-visit: pomijamy kolejne wystąpienia (s,a) w epizodzie
            visited.add(key)                                        # zapamiętaj, że (s,a) już było “pierwszy raz”
            G = Gs[t]                                               # zwrot od tej pierwszej wizyty (definicja first-visit MC)

            N[s, a] += 1                                            # inkrementuj licznik wizyt (s,a)
            Q[s, a] += (G - Q[s, a]) / N[s, a]                      # średnia inkrementalna: Q <- Q + (G-Q)/N

        # (opcjonalnie) GLIE: epsilon maleje -> polityka staje się coraz bardziej zachłanna
        # epsilon = max(0.01, epsilon * 0.9999)                      # przykładowy decay (do demonstracji na zajęciach)

    pi_greedy = np.argmax(Q, axis=1)                                # do ewaluacji/wizualizacji: deterministyczna greedy z Q
    return Q, pi_greedy, N                                          # zwracamy też N do diagnostyki pokrycia (coverage)

"""
def mc_control_epsilon_greedy(env, nS: int, nA: int, gamma: float = 0.99, episodes: int = 50_000, epsilon: float = 0.1, seed: int = 0, max_steps: int = 10_000):
    rng = np.random.default_rng(seed)
    Q = np.zeros((nS, nA), dtype=np.float64)
    N = np.zeros((nS, nA), dtype=np.int64)

    def policy(s: int) -> int:
        return epsilon_greedy(Q[s], epsilon=epsilon, rng=rng)

    for _ in range(episodes):
        traj = rollout_episode(env, policy, max_steps=max_steps)
        # TODO: policz zwroty G_t dla każdego kroku (tu: helper returns_from_trajectory)
        # Dla Q potrzebujemy G_t od momentu t do końca
        # G_t obliczamy na bazie nagród trajektorii.
        G = 0.0
        visited = set()
        # TODO: dla MC control liczymy zwrot od końca epizodu (reverse pass)
        for (s, a, r) in reversed(traj):
            G = r + gamma * G # zwroty dla trajektori dla kolejnych krokow
            key = (s, a)  # wektor stanu i akcji
            if key in visited:
                continue  # first-visit dla pary (s,a)
            visited.add(key)
            N[s, a] += 1
            # TODO: analogiczna aktualizacja średniej dla Q(s,a)
            Q[s, a] += (G - Q[s, a]) / N[s, a]

    # deterministyczna polityka zachłanna - po treningu/optymalizacji
    pi_greedy = np.argmax(Q, axis=1)
    return Q, pi_greedy, N
"""
