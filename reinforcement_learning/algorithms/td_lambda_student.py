"""
TD(λ) prediction — wersja STUDENT.

Cel: estymacja V(s) ≈ v_π(s) dla ustalonej polityki π, używając eligibility traces.

To jest „most” między MC a TD:
- λ = 0  -> TD(0)
- λ -> 1 -> zachowanie zbliżone do Monte Carlo (w zadaniach epizodycznych)

Implementujemy backward view (eligibility traces):
- trzymamy wektor e(s)
- w każdym kroku liczymy błąd TD: δ = r + γ V(s') - V(s)
- rozprowadzamy aktualizację po wszystkich stanach proporcjonalnie do e

Wskazówki:
- Dla terminala przyjmujemy V(terminal)=0, czyli bootstrap=0.
- Najprostszy wariant to accumulating traces: e[s] += 1.
  (Alternatywnie replacing traces: e[s] = 1.)
"""

from __future__ import annotations
from typing import Callable
import numpy as np


def td_lambda_prediction(
    env,
    policy: Callable[[int], int],
    nS: int,
    gamma: float = 0.99,
    alpha: float = 0.1,
    lam: float = 0.9,
    episodes: int = 10_000,
    max_steps: int = 10_000,
):
    V = np.zeros(nS, dtype=np.float64)

    for _ in range(episodes):
        # eligibility trace dla aktualnego epizodu
        e = np.zeros(nS, dtype=np.float64)

        s, _ = env.reset()
        s = int(s)

        for _ in range(max_steps):
            # TODO: wybierz akcję zgodnie z polityką π
            a = ...

            sp, r, terminated, truncated, _ = env.step(int(a))
            sp = int(sp)
            done = bool(terminated or truncated)

            # TODO: bootstrap = γ V(sp) jeśli nie terminal, inaczej 0
            bootstrap = ...

            # TODO: błąd TD: δ = r + bootstrap - V[s]
            delta = ...

            # TODO: ślad zanika: e <- γ λ e
            e *= ...

            # TODO: accumulating traces: e[s] += 1 (wariant replacing: e[s] = 1)
            e[s] += ...

            # TODO: aktualizacja wszystkich stanów: V <- V + α δ e
            V += ...

            s = sp
            if done:
                break

    return V
