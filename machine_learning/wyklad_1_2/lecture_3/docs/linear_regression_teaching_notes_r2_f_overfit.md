# Notatki prowadzącego — regresja liniowa, R², F-test i overfitting

## Główna narracja wykładu

Ten wykład warto prowadzić w czterech warstwach:

1. **Model jako prosta**: student widzi punkty i prostą.
2. **Model jako minimalizacja błędu**: prosta jest dobra, jeśli ma małe pionowe błędy.
3. **Model jako poprawa baseline’u**: $R^2$ porównuje regresję ze średnią.
4. **Model jako obiekt ML**: dobry fit na train nie wystarcza; liczy się test/CV.

StatQuest dobrze sprawdza się jako inspiracja dydaktyczna, bo pokazuje kolejność: least squares → residuals/SSE → $R^2$ → p-value przez $F$. W tym materiale ta kolejność jest rozszerzona o train/test, overfitting i zadania ręczne.

---

## 1. Najważniejsze wzory

Dla jednej cechy:

$$
\hat y_i = b_0 + b_1x_i
$$

Reszta:

$$
e_i = y_i - \hat y_i
$$

Suma kwadratów błędów:

$$
SSE = \sum_i (y_i - \hat y_i)^2
$$

Parametry OLS dla jednej cechy:

$$
b_1 = \frac{\sum_i (x_i-\bar x)(y_i-\bar y)}{\sum_i (x_i-\bar x)^2}
$$

$$
b_0 = \bar y - b_1\bar x
$$

---

## 2. R² jako poprawa względem średniej

Baseline średniej:

$$
\hat y_i = \bar y
$$

Total sum of squares:

$$
TSS = \sum_i(y_i-\bar y)^2
$$

Error/residual sum of squares:

$$
SSE = \sum_i(y_i-\hat y_i)^2
$$

Explained sum of squares:

$$
SSR = TSS - SSE
$$

Współczynnik determinacji:

$$
R^2 = \frac{SSR}{TSS} = 1 - \frac{SSE}{TSS}
$$

### Jak tłumaczyć studentom

- $R^2=0$: model nie poprawia średniej.
- $R^2=0.7$: model usunął 70% błędu baseline’u średniej.
- $R^2=1$: idealne dopasowanie na ocenianych danych.
- $R^2<0$: model jest gorszy od baseline’u średniej; często zdarza się na test set.

### Pułapka

Treningowe $R^2$ przy dodawaniu cech zwykle nie maleje. Dlatego nie wystarczy chwalić modelu za wysokie $R^2$ na danych treningowych.

---

## 3. Adjusted R²

$$
R^2_{adj}=1-(1-R^2)\frac{n-1}{n-p-1}
$$

gdzie:

- $n$ — liczba obserwacji,
- $p$ — liczba cech/predyktorów.

Adjusted $R^2$ karze model za dodawanie cech. Jest przydatne w klasycznej regresji i porównywaniu modeli na tych samych danych, ale w kursie ML trzeba podkreślić:

> Adjusted $R^2$ nie zastępuje walidacji na nowych danych.

---

## 4. Tabela ANOVA i test F

Dla modelu z $p$ cechami:

| Źródło | SS | df | MS |
|---|---:|---:|---:|
| Model | $SSR$ | $p$ | $MSR=SSR/p$ |
| Residual/Error | $SSE$ | $n-p-1$ | $MSE=SSE/(n-p-1)$ |
| Total | $TSS$ | $n-1$ | |

Statystyka:

$$
F = \frac{MSR}{MSE}
= \frac{SSR/p}{SSE/(n-p-1)}
$$

albo bezpośrednio z $R^2$:

$$
F = \frac{R^2/p}{(1-R^2)/(n-p-1)}
$$

Hipotezy:

$$
H_0: \beta_1=\beta_2=\dots=\beta_p=0
$$

$$
H_A: \text{co najmniej jeden predyktor pomaga}
$$

p-value:

$$
p = P(F_{df_1, df_2} \ge F_{obs})
$$

W Pythonie:

```python
from scipy.stats import f
p_value = f.sf(F_obs, df1, df2)
```

### Ważna interpretacja

Test $F$ mówi, czy model poprawia baseline średniej na danych, na których go liczymy. Nie mówi automatycznie, że model dobrze przewidzi przyszłe dane. To jest miejsce na mocne połączenie ze splitami train/test.

---

## 5. Fitting, underfitting, overfitting

**Fitting**: dopasowanie parametrów modelu do danych treningowych.

**Underfitting**: model zbyt prosty. Objaw: słaby wynik na train i test.

**Dobry fit**: model łapie strukturę, a wyniki train/test są podobne.

**Overfitting**: model zbyt elastyczny. Objaw: bardzo dobry train, wyraźnie słabszy test.

Dobra formuła do powiedzenia na wykładzie:

> Wysokie treningowe $R^2$ mówi, że model dobrze opisał dane, które już widział. Nie mówi, czy zrozumiał regułę generującą nowe dane.

---

## 6. Proponowane pytania do studentów

1. Czy prosta o najmniejszym SSE musi przechodzić przez najwięcej punktów?
2. Dlaczego błędy kwadratowe mocno reagują na outliery?
3. Co oznacza $R^2=0$?
4. Czy $R^2$ na teście może być ujemne?
5. Dlaczego dodawanie losowych cech może poprawić train $R^2$?
6. Czy p-value z testu $F$ jest metryką jakości predykcyjnej?
7. Co widzimy, gdy reszty tworzą literę U?
8. Dlaczego regularizacja będzie naturalnym kolejnym tematem?

---

## 7. Proponowany przebieg 60–90 minut

1. 10 min — dane, scatterplot, baseline średniej.
2. 15 min — model liniowy, reszty, SSE, ręczne porównanie kilku prostych.
3. 15 min — fit w sklearn i ręczna formuła $b_0$, $b_1$.
4. 15 min — $R^2$, TSS/SSE/SSR, zadanie ręczne.
5. 10 min — ANOVA i test $F$ jako rozszerzenie statystyczne.
6. 15 min — train/test, CV, underfitting/overfitting.
7. 10 min — GeoGebra lub dyskusja z resztami/outlierem.

---

## Źródła/inspiracje

- StatQuest: Linear Regression, Clearly Explained!!!
- StatQuest GitHub: linear_regression_demo.R
- Penn State STAT 462: sumy kwadratów, $R^2$, ANOVA i test $F$
- statsmodels documentation: `OLSResults.fvalue`, `f_pvalue`, `mse_model`, `mse_resid`
