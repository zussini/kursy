# v6.2 — Titanic i Tips jako most do ćwiczeń

## Wniosek dydaktyczny

Materiał v6.1 jest wystarczający na wykład 3-godzinny, jeżeli celem jest zrozumienie:

- design matrix,
- odds, log-odds, odds ratio,
- regresji logistycznej przez likelihood,
- ROC/AUC i progów,
- regularyzacji.

Nie warto dokładać całego dużego case study do głównego wykładu, bo wtedy łatwo zgubić główną nić. Lepiej użyć danych jako krótkiego mostu lub jako ćwiczeń.

## Proponowane użycie danych

### Wykład

Na wykładzie używamy małych przykładów tablicowych oraz 1–2 krótkich demonstracji:

1. Titanic: odds ratio przeżycia kobiet względem mężczyzn.
2. Titanic: ROC/AUC i leakage przez kolumnę `alive`.

### Ćwiczenia

Na ćwiczeniach/laboratorium używamy notebooka:

`16_applied_bridge_titanic_tips_v6_2.ipynb`

Studenci przechodzą przez:

- regresję logistyczną na Titanicu,
- threshold tuning,
- leakage,
- regresję liniową na Tips,
- klasyfikację `large_tip`,
- L1 regularization z cechami szumowymi.

### Projekt

Najlepszy mini-projekt nadal może być na maratończykach, bo ładnie łączy regresję liniową, klasyfikację, leakage i ROC/AUC. Titanic jest bardzo dobry jako projekt krótszy albo ćwiczenie domowe.

## Czy Titanic/Tips są lepsze niż grades/marathon?

Nie zastępują ich. Dają inny efekt dydaktyczny:

- `grades.csv` jest najlepsze na pierwsze wejście, bo jest bardzo proste.
- `marathon-data.csv` jest najlepsze na projekt, bo ma naturalną historię predykcyjną.
- `Titanic` jest najlepszy na odds/logistic/ROC/leakage.
- `Tips` jest najlepszy na pokazanie, że jeden dataset może być regresyjny lub klasyfikacyjny po zdefiniowaniu targetu.
