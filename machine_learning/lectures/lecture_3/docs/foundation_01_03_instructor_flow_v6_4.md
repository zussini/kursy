# Skrypt prowadzenia brakujących 01–03

## 01. Pipeline

Najważniejsze zdanie:

> Model oceniamy tak, jakby miał działać na przyszłych danych.

Na tablicy:

$$
Dane \rightarrow Train/Test \rightarrow Fit \rightarrow Predict \rightarrow Metric
$$

Baseline regresyjny:

$$
\hat y_i = \bar y_{train}
$$

Pytanie kontrolne przy leakage:

> Czy ta cecha byłaby dostępna w momencie predykcji?

## 02. Metryki

Na tablicy policzyć mały przykład:

$$
MAE=\frac{1}{n}\sum_i |y_i-\hat y_i|
$$

$$
RMSE=\sqrt{\frac{1}{n}\sum_i (y_i-\hat y_i)^2}
$$

$$
R^2=1-\frac{SSE}{TSS}
$$

Dla klasyfikacji narysować confusion matrix:

| | Pred 1 | Pred 0 |
|---|---:|---:|
| True 1 | TP | FN |
| True 0 | FP | TN |

Potem próg:

$$
score_i \ge t \Rightarrow \hat y_i=1
$$

ROC jako efekt przesuwania progu:

$$
TPR=\frac{TP}{TP+FN}, \quad FPR=\frac{FP}{FP+TN}
$$

## 03. Geometria

Na tablicy:

$$
\|[3,4]\|_2=5
$$

$$
d(a,b)=\sqrt{\sum_j(a_j-b_j)^2}
$$

Problem skali:

- wiek: 20–80,
- dochód: 2000–20000,
- dochód dominuje odległość.

Most do modeli liniowych:

$$
\hat y=\beta_0+x^T\beta
$$

Most do regularizacji:

$$
L2: \sum_j \beta_j^2, \quad L1: \sum_j |\beta_j|
$$
