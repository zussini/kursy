# Notatki prowadzącego — fundamenty 01–03

## 01. ML pipeline

Najważniejsza fraza do powtarzania:

> Test set ma udawać przyszłość.

Minimalna opowieść:

1. Mamy dane, cechy $X$ i target $y$.
2. Dzielimy dane na train/test.
3. Uczymy model tylko na train.
4. Oceniamy na test.
5. Porównujemy z baseline'em.
6. Sprawdzamy, czy nie ma leakage.

Wzór do tablicy:

$$
\text{fit tylko na train} \quad \rightarrow \quad \text{ocena na test}
$$

Pytanie kontrolne:

> Czy ta cecha byłaby znana w momencie predykcji?

Jeżeli nie, to prawdopodobnie leakage.

## 02. Metryki

Regresja:

$$
MAE=\frac{1}{n}\sum_i |y_i-\hat y_i|
$$

$$
RMSE=\sqrt{\frac{1}{n}\sum_i (y_i-\hat y_i)^2}
$$

$$
R^2=1-\frac{SSE_{model}}{SSE_{baseline}}
$$

Klasyfikacja:

$$
precision=\frac{TP}{TP+FP}
$$

$$
recall=\frac{TP}{TP+FN}
$$

$$
specificity=\frac{TN}{TN+FP}
$$

Najważniejsza intuicja:

> Model daje score, a próg zamienia score na decyzję.

To przygotowuje do logistic regression, threshold tuning i ROC/AUC.

## 03. Geometria

Główna fraza:

> Algorytm widzi tabelę jako punkty w przestrzeni.

Odległość euklidesowa:

$$
d(a,b)=\sqrt{\sum_j(a_j-b_j)^2}
$$

StandardScaler:

$$
z=\frac{x-\mu}{\sigma}
$$

Cosine similarity:

$$
\cos(x,y)=\frac{x\cdot y}{\|x\|\|y\|}
$$

W tym miejscu nie trzeba jeszcze uczyć KNN. Wystarczy powiedzieć, że za tydzień wrócimy do pytania: „co znaczy najbliższy sąsiad?”.