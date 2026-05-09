# R², adjusted R², F-test i overfitting — ściąga do wykładu

## Oznaczenia

Dane:

$$
(x_i,y_i), \quad i=1,\dots,n
$$

Predykcja modelu:

$$
\hat y_i
$$

Średnia wartości prawdziwych:

$$
\bar y = \frac{1}{n}\sum_i y_i
$$

## Sumy kwadratów

Całkowita zmienność względem średniej:

$$
\mathrm{TSS}=\sum_i(y_i-\bar y)^2
$$

Błąd modelu:

$$
\mathrm{SSE}=\sum_i(y_i-\hat y_i)^2
$$

Zmienność usunięta przez model:

$$
\mathrm{SSR}=\mathrm{TSS}-\mathrm{SSE}
$$

## R²

$$
R^2=1-\frac{\mathrm{SSE}}{\mathrm{TSS}}
$$

albo:

$$
R^2=\frac{\mathrm{SSR}}{\mathrm{TSS}}
$$

Interpretacja:

> R² mówi, jaką część błędu baseline’u średniej model usunął.

## Adjusted R²

$$
R^2_{adj}=1-(1-R^2)\frac{n-1}{n-p-1}
$$

Stosujemy, gdy porównujemy modele z różną liczbą cech. Karze za dodatkowe parametry.

## F-test całego modelu

Dla modelu z $p$ cechami:

$$
\mathrm{MSR}=\frac{\mathrm{SSR}}{p}
$$

$$
\mathrm{MSE}=\frac{\mathrm{SSE}}{n-p-1}
$$

$$
F=\frac{\mathrm{MSR}}{\mathrm{MSE}}
$$

Równoważnie z R²:

$$
F=\frac{R^2/p}{(1-R^2)/(n-p-1)}
$$

Hipoteza zerowa:

$$
H_0: \beta_1=\beta_2=\dots=\beta_p=0
$$

p-value:

$$
P(F_{p,n-p-1}\ge F_{obs})
$$

## Train/test R²

| Wzorzec | Train R² | Test R² | Diagnoza |
|---|---:|---:|---|
| niskie/niskie | niskie | niskie | underfitting |
| podobne i dobre | średnie/wysokie | podobne | sensowne dopasowanie |
| wysokie/niskie | wysokie | dużo niższe | overfitting |

## Ważne zdania do powtarzania studentom

- R² nie mierzy przyczynowości.
- R² na treningu nie mierzy generalizacji.
- Wysokie R² nie zastępuje wykresu reszt.
- Ujemne R² na teście oznacza: model jest gorszy niż baseline przewidujący średnią.
- F-test odpowiada na pytanie statystyczne, a train/test odpowiada na pytanie predykcyjne.
