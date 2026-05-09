
# Wykład 3 — spójna kompilacja zakresu 01–16

Ta paczka jest poprawioną kompilacją **bez tematów `17_*`**. Nie ma tutaj KNN, drzew decyzyjnych, SVM, ensemble ani manifold learning — to zostaje na później.

## Notebooki

1. `wyklad3_01_geometria_pipeline_regresja.ipynb`
   - dane jako punkty i wektory,
   - normy, odległości, scaling, cosine similarity,
   - $\bar y$ vs $\hat y$,
   - baseline, regresja liniowa, reszty,
   - MAE/RMSE/$R^2$,
   - design matrix,
   - train/test, CV, pipeline,
   - tips regression i krótka regularyzacja.

2. `wyklad3_02_odds_logistic_roc.ipynb`
   - probability, odds, log-odds,
   - odds ratio i $\log(OR)$,
   - Fisher/chi-square/Wald,
   - regresja logistyczna,
   - likelihood, deviance, pseudo-$R^2$,
   - threshold, confusion matrix,
   - ROC/AUC,
   - leakage na Titanicu,
   - tips jako krótka klasyfikacja.

## Dane

Folder `data/` zawiera:

- `previous_lecture_grades.csv`,
- `seaborn_tips.csv`,
- `seaborn_titanic.csv`.

## GeoGebra

Folder `geogebra/` zawiera dostarczony plik:

- `Dopasowanie_prostej_odleglosci_normy_pogladowo.ggb`.

Najlepiej użyć go do części pierwszej: punkty, prosta, reszty, średnia $\bar y$, predykcje $\hat y$, TSS/RSS/$R^2$ oraz intuicja odległości.
