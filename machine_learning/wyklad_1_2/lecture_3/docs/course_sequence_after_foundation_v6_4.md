# Kolejność kursu po dodaniu 01–03 — v6.4

Możesz realnie prowadzić kurs w kolejności:

$$
01 \rightarrow 02 \rightarrow 03 \rightarrow 06 \rightarrow 07 \rightarrow 08 \rightarrow 09 \rightarrow 10 \rightarrow 11 \rightarrow 12 \rightarrow 13 \rightarrow 14 \rightarrow 04 \rightarrow 05 \rightarrow 15 \rightarrow \ldots
$$

To nie łamie logiki. KNN i clustering nie są wymagane do zrozumienia linear/logistic. Są późniejszym zastosowaniem geometrii.

## Tydzień / blok 1: fundamenty + modele liniowo-statystyczne

| Nr | Temat | Rola |
|---:|---|---|
| 01 | ML pipeline: train/test, CV, leakage, baseline | jak uczciwie oceniać modele |
| 02 | Metrics: regression/classification, confusion matrix, mini ROC | język oceny modeli |
| 03 | Geometry basics: scaling, norms, distances, cosine | skala, odległość, współczynniki, regularizacja |
| 06 | Linear regression | pierwszy model parametryczny |
| 07 | Multiple regression + design matrix | wspólny język $X\beta$ |
| 08 | t-test i ANOVA jako modele liniowe | statystyka jako szczególny przypadek modeli liniowych |
| 09 | Probability vs likelihood + MLE intro | przejście do modeli probabilistycznych |
| 10 | Odds, log-odds, odds ratio, Fisher/chi-square/Wald | fundament logistic regression |
| 11 | Logistic regression: sigmoid, logit, coefficients | model liniowy na skali log-odds |
| 12 | Logistic likelihood, deviance, pseudo-$R^2$, tests | dopasowanie i testowanie modelu |
| 13 | ROC/AUC, thresholds, calibration | decyzje po progu i jakość rankingu |
| 14 | Regularization: Ridge, Lasso, Elastic Net | kontrola złożoności i overfittingu |

## Tydzień / blok 2: geometria lokalna i dalsze modele

| Nr | Temat | Rola |
|---:|---|---|
| 04 | KNN | model lokalny oparty na odległości |
| 05 | Clustering I: k-means, hierarchical | geometria bez etykiet |
| 15 | Naive Bayes, LDA, QDA | probabilistyczne klasyfikatory liniowe/kwadratowe |
| 16 | PCA + supervised LDA projection | reprezentacja i rzutowanie |
| 17 | SVM | margines, soft margin, kernels |
| 18+ | Trees, ensembles, boosting, manifold, text, interpretability | dalszy kurs |

## Uwaga organizacyjna

Nie trzeba fizycznie przenumerowywać wszystkich istniejących notebooków natychmiast. Można zachować obecne nazwy i używać tego pliku jako oficjalnej kolejności prowadzenia. Finalną renumerację warto zrobić dopiero po domknięciu pełnej paczki.
