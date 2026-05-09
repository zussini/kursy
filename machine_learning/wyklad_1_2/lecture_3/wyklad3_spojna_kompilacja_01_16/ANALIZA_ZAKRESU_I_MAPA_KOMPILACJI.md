
# Analiza zakresu i mapa kompilacji

## Co zostało uwzględnione

Zakres: notebooki i tematy od `01` do `15/16`, plus bieżące `wyklad_3.ipynb`, `notatki_wyklad_3_9_05_26.ipynb` oraz plik GeoGebra.

Uwzględnione bloki tematyczne:

| Źródło | Co trafiło do kompilacji |
|---|---|
| `01_ml_pipeline...` | train/test, baseline, CV, leakage, pipeline |
| `02_metrics...` | MAE, RMSE, $R^2$, confusion matrix, threshold, ROC/AUC |
| `03_geometry...` | wektory, normy, odległości, scaling, cosine similarity |
| `08_linear_regression...` | regresja liniowa, $\bar y$ vs $\hat y$, reszty, TSS/RSS/$R^2$, design matrix, GeoGebra |
| `09 GLM/design matrix` | idea design matrix i GLM jako wspólna rama modeli |
| `10 odds/log-odds...` | probability, odds, log-odds, odds ratio, Fisher/chi-square/Wald |
| `11 logistic likelihood` | sigmoid, logit, likelihood, interpretacja współczynników |
| `12 deviance/model tests` | deviance, model null/full, pseudo-$R^2$, Wald/LRT jako intuicja |
| `13 ROC/AUC` | threshold sweep, confusion matrix, ROC, AUC |
| `14 regularization` | krótka kapsuła Ridge/Lasso bez wchodzenia w przyszłe algorytmy |
| `15 applied bridge` | grades jako regresja i klasyfikacja, leakage, log-odds |
| `16 Titanic/Tips` | Titanic logistic/ROC/leakage, Tips regression/classification |
| `wyklad_3.ipynb` | aktualna ścieżka wykładu: grades, OR/logOR, normy, scaling, cosine, log-odds |
| `notatki_wyklad_3...` | poprawka dydaktyczna: wyraźnie odróżnić $\bar y$ od $\hat y$ |

## Co zostało świadomie wykluczone

Wykluczone:

- `17_05_01_knn_geometry.ipynb`,
- `17_05_02_decision_trees_rules.ipynb`,
- `17_05_04_svm_margin_kernels.ipynb`,
- `17_05_05_ensembles_xgboost_optional.ipynb`,
- `17_05_06_manifold_learning.ipynb`.

Powód: to są tematy przyszłych wykładów, a nie zakres aktualnej kompilacji.

## Dlaczego tylko 2 notebooki?

Materiał 01–16 da się logicznie podzielić na dwa bloki:

1. regresja i geometria,
2. klasyfikacja i logistyka.

Dzięki temu historia jest spójna i nie rozprasza się na przyszłe algorytmy.
