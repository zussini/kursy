# Plan 3-godzinnego wykładu: linear/logistic/ROC/regularization

## Wariant rekomendowany

### 0:00–0:20 — przypomnienie modeli liniowych

Cel:

$$
y \approx X\beta
$$

Pokazać:

- czym jest design matrix,
- jak t-test i ANOVA są regresją z inną macierzą $X$,
- dlaczego regresja liniowa jest intuicyjnym punktem startu.

### 0:20–0:50 — probability, odds, log-odds

Małe liczby na tablicy:

$$
odds=\frac{p}{1-p}
$$

$$
logit(p)=\log\left(\frac{p}{1-p}\right)
$$

Pokazać przykład 2x2, odds ratio i log odds ratio.

### 0:50–1:20 — regresja logistyczna jako model liniowy na skali log-odds

Główna oś:

$$
logit(p)=X\beta
$$

$$
p=\sigma(X\beta)=\frac{1}{1+e^{-X\beta}}
$$

Podkreślić różnicę względem regresji liniowej:

- inny target,
- inna skala predykcji,
- inna funkcja celu,
- inna interpretacja współczynników.

### 1:20–1:35 — przerwa lub GeoGebra

Najlepsza demonstracja: suwak `beta0`, `beta1`, krzywa sigmoid i próg.

### 1:35–2:00 — likelihood, deviance, Wald/LRT

Nie robić zbyt długo. Pokazać intuicję:

$$
L(\beta)=\prod_i p_i^{y_i}(1-p_i)^{1-y_i}
$$

$$
\ell(\beta)=\sum_i y_i\log(p_i)+(1-y_i)\log(1-p_i)
$$

Następnie:

$$
G^2=2(\ell_{full}-\ell_{reduced})
$$

### 2:00–2:30 — ROC/AUC i threshold tuning

Oddzielić:

- score/probability,
- próg,
- klasy,
- confusion matrix,
- ROC/AUC.

Krótka demonstracja na Titanicu może wejść tutaj.

### 2:30–2:50 — regularizacja

Pokazać:

$$
L2: \lambda\sum_j \beta_j^2
$$

$$
L1: \lambda\sum_j |\beta_j|
$$

Wytłumaczyć geometrycznie: okrąg vs romb, L1 zeruje współczynniki.

### 2:50–3:00 — zamknięcie i zadanie

Dać studentom notebook aplikacyjny:

- `15_applied_bridge_grades_marathon_v6_1.ipynb`, albo
- `16_applied_bridge_titanic_tips_v6_2.ipynb`.

## Czy materiału wystarczy?

Tak, materiału jest nawet więcej niż na 3h. Trzeba pilnować, aby główny wykład nie zamienił się w laboratorium. Datasets najlepiej traktować jako 10-minutowy most lub jako ćwiczenia.
