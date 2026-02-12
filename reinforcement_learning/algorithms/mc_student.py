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

        # TODO: policz zwroty G_t dla każdego kroku (użyj helpera returns_from_trajectory z utils)
        Gs = ...  # Gs[t] ma być zwrotem od kroku t (czyli suma zdyskontowanych nagród od t do końca epizodu)

        visited = ...  # TODO: stwórz zbiór visited do first-visit (żeby aktualizować stan tylko raz na epizod)

        for (t, (s, a, r)) in enumerate(traj):
            # TODO: first-visit MC: jeśli stan s już był w tym epizodzie, pomiń aktualizację
            if ...:
                continue  # first-visit (aktualizujemy tylko przy pierwszym wystąpieniu stanu w epizodzie)

            visited.add(...)  # TODO: dodaj bieżący stan s do visited (oznaczamy, że już był)

            G = ...  # TODO: wybierz zwrot dla kroku t (to jest target do aktualizacji V[s])

            N[s] += ...  # TODO: zwiększ licznik wizyt stanu s (potrzebny do średniej inkrementalnej)

            # TODO: aktualizacja średniej inkrementalnej V[s] zgodnie ze wzorem: V <- V + (G - V)/N
            V[s] += ...  # aktualizujemy estymatę wartości stanu s na podstawie zwrotu G

    return V, N

def mc_control_epsilon_greedy(env, nS: int, nA: int, gamma: float = 0.99, episodes: int = 50_000, epsilon: float = 0.1, seed: int = 0, max_steps: int = 10_000):
    rng = np.random.default_rng(seed)
    Q = np.zeros((nS, nA), dtype=np.float64)
    N = np.zeros((nS, nA), dtype=np.int64)

    def policy(s: int) -> int:
        return ...  # TODO: wybierz akcję ε-greedy na podstawie Q[s] (użyj helpera epsilon_greedy z utils)

    for _ in range(episodes):
        traj = rollout_episode(env, policy, max_steps=max_steps)

        # TODO: policz zwroty G_t dla każdego kroku t (użyj returns_from_trajectory z utils)
        Gs = ...  # Gs[t] ma być zwrotem od kroku t (target do aktualizacji Q)

        visited = ...  # TODO: zbiór visited dla first-visit par (s,a) w tym epizodzie

        for (t, (s, a, r)) in enumerate(traj):
            key = ...  # TODO: zdefiniuj klucz pary (s,a), np. (s, a)

            # TODO: first-visit MC control: jeśli (s,a) już było w epizodzie, pomiń
            if ...:
                continue  # first-visit (aktualizujemy tylko pierwsze wystąpienie pary (s,a))

            visited.add(...)  # TODO: dodaj key do visited (oznaczamy, że para (s,a) już była)

            G = ...  # TODO: wybierz zwrot dla kroku t: G = Gs[t] (to jest target dla Q[s,a])

            N[s, a] += ...  # TODO: zwiększ licznik wizyt pary (s,a) (potrzebny do średniej inkrementalnej)

            # TODO: aktualizacja średniej inkrementalnej Q[s,a] zgodnie ze wzorem: Q <- Q + (G - Q)/N
            Q[s, a] += ...  # aktualizujemy wartość akcji a w stanie s na podstawie zwrotu G

    pi_greedy = np.argmax(Q, axis=1)  # gotowa polityka do ewaluacji: wybieramy argmax_a Q(s,a)
    return Q, pi_greedy, N
