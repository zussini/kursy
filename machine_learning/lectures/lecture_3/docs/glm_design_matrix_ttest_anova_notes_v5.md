# GLM / design matrix: połączenie regresji, t-testu i ANOVA — notatki prowadzącego

## Główna teza wykładu

Regresja liniowa, t-test i ANOVA to nie są trzy zupełnie osobne światy. Wszystkie można zapisać jako:

\[
y = X\beta + \varepsilon
\]

Różnica polega na tym, co wpiszemy do macierzy projektu `X`.

## 1. Regresja liniowa

Dane: masa myszy i ekspresja genu.

\[
expression_i = \beta_0 + \beta_1 weight_i + \varepsilon_i
\]

Design matrix:

\[
X =
\begin{bmatrix}
1 & weight_1 \\
1 & weight_2 \\
\vdots & \vdots \\
1 & weight_n
\end{bmatrix}
\]

Interpretacja:

- `β0`: intercept,
- `β1`: zmiana ekspresji na 1 gram masy.

## 2. t-test dwóch grup jako regresja

Dane: `Control` i `Mutant`.

Kodowanie bez interceptu:

\[
expression_i = \beta_{Control} I(Control_i) + \beta_{Mutant} I(Mutant_i) + \varepsilon_i
\]

Wtedy:

- `βControl` = średnia grupy Control,
- `βMutant` = średnia grupy Mutant.

Kodowanie z interceptem:

\[
expression_i = \beta_0 + \beta_1 I(Mutant_i) + \varepsilon_i
\]

Wtedy:

- `β0` = średnia Control,
- `β1` = różnica Mutant − Control.

W przykładzie:

- Control mean = 2.2,
- Mutant mean = 3.6,
- różnica = 1.4.

## 3. F-test i t-test

Model zerowy:

\[
\hat y_i = \bar y
\]

Model pełny:

\[
\hat y_i = \bar y_{group(i)}
\]

Liczymy:

\[
SSE_{null}=\sum_i(y_i-\hat y_{null,i})^2
\]

\[
SSE_{full}=\sum_i(y_i-\hat y_{full,i})^2
\]

\[
F=\frac{(SSE_{null}-SSE_{full})/(p_{full}-p_{null})}{SSE_{full}/(n-p_{full})}
\]

Dla dwóch grup:

\[
F=t^2
\]

To jest najlepszy punkt wykładowy do pokazania, że t-test jest szczególnym przypadkiem ANOVA/regresji.

## 4. ANOVA jako regresja

Dla `k` grup:

\[
expression_i = \mu_1 I(group_i=1)+\mu_2 I(group_i=2)+...+\mu_k I(group_i=k)+\varepsilon_i
\]

Design matrix to one-hot encoding.

ANOVA porównuje:

- model z jedną średnią,
- model z k średnimi grupowymi.

\[
F=\frac{SS_{between}/(k-1)}{SS_{within}/(n-k)}
\]

## 5. Połączenie regresji i ANOVA

Model:

\[
expression_i = \beta_0 + \beta_1 weight_i + \beta_2 I(Mutant_i)+\varepsilon_i
\]

Interpretacja:

- `β1`: wpływ masy,
- `β2`: różnica Mutant vs Control po uwzględnieniu masy.

Wersja z interakcją:

\[
expression_i = \beta_0 + \beta_1 weight_i + \beta_2 I(Mutant_i)+\beta_3 weight_i I(Mutant_i)+\varepsilon_i
\]

Interpretacja:

- `β3`: różnica nachyleń między grupami.

## Proste ćwiczenie na 10 minut

Dane:

Control: 1.5, 1.8, 2.2, 2.4, 3.1  
Mutant: 2.9, 3.3, 3.6, 3.9, 4.3

Zadania:

1. Policz średnie grup.
2. Zbuduj ręcznie design matrix bez interceptu.
3. Pokaż, że współczynniki modelu to średnie grup.
4. Zbuduj design matrix z interceptem i zmienną `Mutant`.
5. Pokaż, że współczynnik `Mutant` to różnica średnich.
6. Policz `SSE_null` i `SSE_full`.
7. Policz `F` i porównaj z `t²`.