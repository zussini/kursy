# RL Pack: Monte Carlo → Temporal Difference → Most do metod ciągłych
# Od  zajęć MC,TD itd. tworzymy sobie bibliotekę 
Ten zestaw plików jest przygotowany tak, żeby:
1) na **GridWorld / FrozenLake** przejść porównawczo przez **DP vs Monte Carlo vs TD**,  
2) zrobić **TD(λ)** jako płynne przejście MC↔TD,  
3) domknąć **most do środowisk ciągłych** (funkcja aproksymacji + dlaczego policy-based),  
4) zostawić przygotowany „start” pod kolejny blok: **Policy Gradient / Actor-Critic / PPO** (bez pełnej implementacji na tym etapie).

> Cel dydaktyczny: po bloku 1 studenci rozumieją *kompromisy* (bias/variance, bootstrapping, on/off-policy) i *dlaczego* w środowiskach ciągłych sensownie przejść do policy gradient.

---

## Sugerowany rozkład zajęć (2 bloki × 4h)

### Blok 1 (4h): MC, TD, TD(λ) + most do ciągłych
**0:00–0:20** Setup + przypomnienie DP jako „złoty standard”  
**0:20–1:30** Monte Carlo: prediction + kontrola (ε-greedy)  
**1:30–2:40** TD(0): prediction + SARSA/Q-learning (krótko jako preview)  
**2:40–3:30** TD(λ): eligibility traces, eksperymenty dla różnych λ  
**3:30–4:00** Most do ciągłych: ograniczenia tablic (V/Q tables), wstęp do aproksymacji i policy-based

### Blok 2 (4h): Policy gradient / Actor-Critic / PPO + szkic projektu MuJoCo
W tym repo jest notebook **stub** (szkielet). Docelowo w bloku 2:
**0:00–1:00** REINFORCE / policy gradient (intuicja, baseline)  
**1:00–2:00** Actor-Critic (TD jako krytyk)  
**2:00–3:00** PPO (intuicja klipu + praktyka)  
**3:00–4:00** Projekt MuJoCo: wybór tasku, metryki, logowanie, sanity-checki

---

## Struktura folderów

- `notebooks/`
  - `00_setup_and_envs.ipynb` – szybki start, wizualizacje stanów, API środowisk
  - `01_dp_baseline_frozenlake.ipynb` – DP jako punkt odniesienia (FrozenLake z jawnym modelem `P[s][a]` (budowany w czystym Pythonie))
  - `02_mc_on_gridworld_frozenlake.ipynb` – Monte Carlo prediction + control
  - `03_td0_on_gridworld_frozenlake.ipynb` – TD(0) prediction + (preview) SARSA/Q-learning
  - `04_td_lambda_bridge.ipynb` – TD(λ) i porównania λ
  - `05_bridge_to_continuous_function_approx.ipynb` – most do ciągłych: aproksymacja wartości/polityki (bez PPO/AC)
  - `06_block2_stub_policy_based.ipynb` – szkielet pod blok 2 (bez pełnych implementacji)

- `envs/`
  - `gridworld.py` – mały deterministyczny GridWorld (przydatny do debugowania i „klików”)
  - `wrappers.py` – funkcje ujednolicające API + pomocnicze konwersje

- `algorithms/`
  - `dp.py` – policy evaluation / value iteration dla dyskretnych modeli (`env.P`)
  - `mc.py` – MC prediction i MC control (ε-greedy)
  - `td.py` – TD(0) prediction, SARSA, Q-learning (krótko)
  - `td_lambda.py` – TD(λ) z eligibility traces
  - `utils.py` – seedy, rollout, logowanie, wykresy + heatmapy wartości

- `requirements.txt` – minimalne zależności.

---

## Jak uruchomić

1) Zainstaluj zależności:
```bash
pip install -r requirements.txt
```

2) Uruchom Jupytera:
```bash
jupyter lab
```

3) Odpal notebooki po kolei z `notebooks/`.

> Jeśli macie własne implementacje GridWorld/FrozenLake: wystarczy podmienić środowisko w notebookach (sekcja „Wybór env”) – algorytmy zakładają standardowy interfejs `reset()/step()` oraz dyskretny indeks stanu.

---

## Notatka o FrozenLake

Notebooki wspierają FrozenLake przez `gymnasium`. Dla DP wykorzystujemy `env.unwrapped.P` (model przejść).
Dla wersji „slippery” wartości będą probabilistyczne, co jest super do pokazania różnicy DP vs sample-based.

Powodzenia i miłego prowadzenia 👌


---

## Wymagania / instalacja

- FrozenLake w tym pakiecie **nie wymaga Gym** (budujemy `P[s][a]` sami).
- Notebook 05 (CartPole) wymaga `gymnasium` lub `gym`.

```
pip install -r requirements.txt
jupyter lab
```
