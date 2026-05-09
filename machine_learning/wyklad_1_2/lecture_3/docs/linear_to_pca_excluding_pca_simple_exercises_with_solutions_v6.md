
# Ćwiczenia z odpowiedziami v6: design matrix, odds, logistyczna, ROC, regularyzacja

## 1. Design matrix

Dane: `Control = [2, 4]`, `Mutant = [5, 7]`.

### Zadanie

Zapisz model z interceptem i kolumną `Mutant`.

### Odpowiedź

$$
X=\begin{bmatrix}
1&0\\
1&0\\
1&1\\
1&1
\end{bmatrix}
$$

$$
y=\begin{bmatrix}2\\4\\5\\7\end{bmatrix}
$$

Średnia `Control` to $3$, średnia `Mutant` to $6$, więc:

$$
\hat\beta_0=3
$$

$$
\hat\beta_1=6-3=3
$$

## 2. t-test i F

Jeśli dla porównania dwóch grup dostajesz $t=2.5$, to dla równoważnego testu F:

$$
F=t^2=6.25
$$

## 3. Odds

Jeśli $p=0.75$, to:

$$
odds=\frac{0.75}{0.25}=3
$$

$$
log(odds)=\log(3)\approx 1.099
$$

## 4. Odds ratio

Tabela:

$$
\begin{array}{c|cc}
 & Yes & No\\
\hline
A & 8 & 2\\
B & 4 & 6
\end{array}
$$

$$
OR=\frac{8\cdot6}{2\cdot4}=6
$$

$$
\log(OR)=\log(6)\approx 1.792
$$

## 5. Wald dla log(OR)

Dla tabeli z zadania 4:

$$
SE=\sqrt{\frac18+\frac12+\frac14+\frac16}\approx 0.918
$$

$$
z=\frac{1.792}{0.918}\approx 1.952
$$

## 6. Logistyczna — predykcja

Model:

$$
logit(p)=-3+1.2x
$$

Dla $x=2$:

$$
z=-3+1.2\cdot2=-0.6
$$

$$
p=\frac{1}{1+e^{0.6}}\approx 0.354
$$

## 7. Log-likelihood jednej obserwacji

Jeśli $y=1$ i model daje $p=0.9$, wkład do log-likelihoodu:

$$
\log(0.9)\approx -0.105
$$

Jeśli $y=0$ i model daje $p=0.9$:

$$
\log(0.1)\approx -2.303
$$

## 8. ROC

Jeśli $TP=8$, $FN=2$, $FP=3$, $TN=7$:

$$
TPR=\frac{8}{10}=0.8
$$

$$
FPR=\frac{3}{10}=0.3
$$

## 9. AUC pairwise

Mamy positive scores `[0.9, 0.7]` i negative scores `[0.8, 0.4]`.

Pary:

- $0.9>0.8$ — wygrana,
- $0.9>0.4$ — wygrana,
- $0.7<0.8$ — przegrana,
- $0.7>0.4$ — wygrana.

$$
AUC=\frac{3}{4}=0.75
$$

## 10. Ridge

Jeśli kara to $\lambda\beta^2$, $\lambda=0.5$, $\beta=4$:

$$
0.5\cdot 4^2=8
$$

## 11. Lasso soft-thresholding

$$
S(0.3,0.5)=0
$$

$$
S(1.2,0.5)=0.7
$$

$$
S(-1.2,0.5)=-0.7
$$
