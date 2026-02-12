"""
TD(λ) prediction z eligibility traces (wersja dla V(s)).
To jest most MC ↔ TD:
- λ=0 → TD(0)
- λ→1 → podejście bliskie Monte Carlo (przy epizodach)
"""

from __future__ import annotations
from typing import Callable
import numpy as np


def td_lambda_prediction(env, policy: Callable[[int], int], nS: int, gamma: float = 0.99, alpha: float = 0.1, lam: float = 0.9, episodes: int = 10_000, max_steps: int = 10_000):
    V = np.zeros(nS, dtype=np.float64)

    for _ in range(episodes):
        e = np.zeros(nS, dtype=np.float64)  # eligibility trace
        # TODO: zrozum e jako 'pamięć' ostatnio odwiedzanych stanów (eligibility traces)
        s, _ = env.reset()
        s = int(s)
        for _ in range(max_steps):
            a = int(policy(s))
            sp, r, terminated, truncated, _ = env.step(a)
            sp = int(sp)

            # TD error
            bootstrap = 0.0 if (terminated or truncated) else gamma * V[sp]
            # TODO: TD error δ = r + γV(s') - V(s) (z poprawką terminal)
            delta = r + bootstrap - V[s]

            # update traces i wartości
            # TODO: ślad zanika: e <- γλ e
            e *= gamma * lam
            # TODO: accumulating traces: e[s] += 1 (wariant replacing: e[s]=1)
            e[s] += 1.0
            # TODO: aktualizacja wszystkich stanów proporcjonalnie do e
            V += alpha * delta * e

            s = sp
            if terminated or truncated:
                break

    return V
