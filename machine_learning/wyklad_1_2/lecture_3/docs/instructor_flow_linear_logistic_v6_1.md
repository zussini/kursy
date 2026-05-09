# Skrypt prowadzenia bloku linear/logistic/ROC/regularization — v6.1

Ten skrypt jest do prowadzenia zajęć „po ludzku”: co powiedzieć, co policzyć na tablicy, kiedy odpalić notebook, kiedy użyć GeoGebry.

## 0. Główna oś narracyjna

Cały blok można prowadzić jedną linią:

$$
\text{małe liczby} \rightarrow X\beta \rightarrow \text{skala predykcji} \rightarrow \text{funkcja celu} \rightarrow \text{metryka} \rightarrow \text{decyzja}
$$

Dla regresji liniowej:

$$
y \approx X\beta
$$

Dla regresji logistycznej:

$$
\log\left(\frac{p}{1-p}\right)=X\beta
$$

W obu przypadkach uczymy $\beta$. Różni się skala po lewej stronie oraz funkcja celu.

## 1. Wejście: design matrix

### Co powiedzieć

„Design matrix to sposób zapisania naszych pytań do danych. Każda kolumna to jedna informacja, którą pozwalamy modelowi wykorzystać”.

### Na tablicy

Dane z dwiema grupami:

$$
\begin{array}{c|c}
Group & y \\
\hline
Control & 2.1 \\
Control & 2.3 \\
Mutant & 3.5 \\
Mutant & 3.7
\end{array}
$$

Model jednej średniej:

$$
X=
\begin{bmatrix}
1\\1\\1\\1
\end{bmatrix}
$$

Model dwóch średnich:

$$
X=
\begin{bmatrix}
1&0\\
1&0\\
0&1\\
0&1
\end{bmatrix}
$$

Model z interceptem i wskaźnikiem mutacji:

$$
X=
\begin{bmatrix}
1&0\\
1&0\\
1&1\\
1&1
\end{bmatrix}
$$

### Puenta

To nie są trzy różne światy. To trzy różne sposoby zapisania pytania w macierzy $X$.

## 2. Przejście do odds/logit

### Co powiedzieć

„Jeżeli $y$ jest zerem albo jedynką, prosta na osi probability jest niewygodna, bo może wyjść poniżej 0 albo powyżej 1. Szukamy skali, na której można postawić prostą”.

### Na tablicy

$$
p=0.2
$$

$$
odds=\frac{p}{1-p}=\frac{0.2}{0.8}=0.25
$$

$$
\log(odds)=\log(0.25)\approx -1.386
$$

Dla $p=0.8$:

$$
odds=4
$$

$$
\log(odds)\approx 1.386
$$

### GeoGebra

Użyj `GG01_probability_odds_logit_v6_1`.

Przesuwaj `p` i pokaż, że log-odds jest symetryczne wokół zera.

## 3. Odds ratio jako efekt grupowy

### Co powiedzieć

„Odds ratio to nie jest jeszcze regresja logistyczna, ale to jest ten sam język interpretacji”.

### Na tablicy

$$
\begin{array}{c|cc}
& Cancer+ & Cancer- \\
\hline
Mutation+ & 23 & 117 \\
Mutation- & 6 & 210
\end{array}
$$

$$
odds_{mut}=\frac{23}{117}
$$

$$
odds_{no}=\frac{6}{210}
$$

$$
OR=\frac{23/117}{6/210}=\frac{23\cdot210}{117\cdot6}\approx 6.88
$$

$$
\log(OR)\approx 1.93
$$

### Puenta

W modelu logistycznym ze zmienną 0/1 współczynnik przy tej zmiennej jest właśnie log-odds ratio.

$$
e^{\beta_1}=OR
$$

### GeoGebra

Użyj `GG02_odds_ratio_2x2_v6_1`.

## 4. Regresja logistyczna jako linia na log-odds

### Co powiedzieć

„Nie dopasowujemy S-ki bezpośrednio. Dopasowujemy prostą na skali log-odds, a S-ka pojawia się po przekształceniu z powrotem do probability”.

### Na tablicy

$$
\eta=\beta_0+\beta_1x
$$

$$
p=\sigma(\eta)=\frac{1}{1+e^{-\eta}}
$$

$$
\log\left(\frac{p}{1-p}\right)=\eta
$$

### GeoGebra

Użyj `GG03_logistic_curve_threshold_v6_1`.

Pokaż:

- `beta0`: przesunięcie krzywej,
- `beta1`: stromość krzywej,
- `threshold`: decyzja niezależna od dopasowania modelu.

## 5. Likelihood

### Co powiedzieć

„W regresji liniowej minimalizowaliśmy sumę kwadratów. W logistycznej pytamy: jak prawdopodobne są zaobserwowane zera i jedynki przy tej krzywej?”.

### Na tablicy

Jeśli $y_i=1$, wkład to:

$$
p_i
$$

Jeśli $y_i=0$, wkład to:

$$
1-p_i
$$

Razem:

$$
L=\prod_i p_i^{y_i}(1-p_i)^{1-y_i}
$$

Logarytm:

$$
\ell=\sum_i y_i\log(p_i)+(1-y_i)\log(1-p_i)
$$

### GeoGebra

Użyj `GG04_logistic_likelihood_points_v6_1`.

Zmieniaj `beta0` i `beta1`, obserwuj `logL`.

## 6. ROC/AUC i próg

### Co powiedzieć

„Model daje score. Próg robi z tego decyzję. ROC sprawdza, co się dzieje dla wszystkich progów”.

### Na tablicy

$$
TPR=\frac{TP}{TP+FN}
$$

$$
FPR=\frac{FP}{FP+TN}
$$

ROC to punkty:

$$
(FPR(t),TPR(t))
$$

AUC można interpretować jako prawdopodobieństwo, że losowy pozytywny przypadek dostanie wyższy score niż losowy negatywny przypadek.

### GeoGebra

Użyj `GG05_ROC_threshold_sweep_v6_1`.

Zmieniaj `threshold` i patrz na `TPR`, `FPR`, `ROCpoint`.

## 7. Regularyzacja

### Co powiedzieć

„Regularyzacja to nie tylko trik na overfitting. To sposób powiedzenia modelowi: wolę prostsze, stabilniejsze współczynniki”.

### Na tablicy

Ridge/L2:

$$
Loss(\beta)+\lambda\sum_j\beta_j^2
$$

Lasso/L1:

$$
Loss(\beta)+\lambda\sum_j|\beta_j|
$$

Elastic Net:

$$
Loss(\beta)+\lambda\left(\alpha\sum_j|\beta_j|+(1-\alpha)\sum_j\beta_j^2\right)
$$

### GeoGebra

Użyj `GG06_regularization_l1_l2_geometry_v6_1`.

Pokaż, że L1 ma narożniki na osiach. Dlatego łatwiej dostać $\beta_j=0$.

## 8. Gdzie wpiąć większe dane

### `grades.csv`

Najlepiej po logit/sigmoid.

Pytanie:

> Jak prawdopodobieństwo zaliczenia zależy od liczby godzin nauki?

### `marathon-data.csv`

Najlepiej po ROC/AUC.

Pytanie:

> Czy na półmetku da się przewidzieć ukończenie poniżej 4h?

To pozwala pokazać:

- train/test,
- ROC/AUC,
- threshold tuning,
- leakage,
- regularyzację.

## 9. Najważniejsze zdania do powtarzania

1. „Regresja logistyczna jest liniowa, ale nie na probability — na log-odds”.
2. „Probability to score; klasa pojawia się dopiero po progu”.
3. „AUC ocenia ranking, nie konkretną decyzję”.
4. „Dobry wynik z leakage nie jest dobrym modelem”.
5. „Regularyzacja może nie poprawić spektakularnie AUC, ale poprawia stabilność i interpretowalność”.
