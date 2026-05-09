# Ćwiczenia z odpowiedziami: design matrix, t-test, ANOVA, odds ratio i testy

## Część A. Design matrix, t-test i ANOVA

### Zadanie 1. Średnie grup i design matrix

Dane:

Control: 1.5, 1.8, 2.2, 2.4, 3.1  
Mutant: 2.9, 3.3, 3.6, 3.9, 4.3

1. Policz średnią Control.
2. Policz średnią Mutant.
3. W modelu `expression ~ 0 + genotype` podaj współczynniki.

**Odpowiedź**

Control:

\[
\bar y_C=\frac{1.5+1.8+2.2+2.4+3.1}{5}=2.2
\]

Mutant:

\[
\bar y_M=\frac{2.9+3.3+3.6+3.9+4.3}{5}=3.6
\]

Współczynniki modelu bez interceptu:

\[
\beta_C=2.2, \quad \beta_M=3.6
\]

---

### Zadanie 2. Intercept + dummy

Dla tych samych danych budujemy model:

\[
expression = \beta_0 + \beta_1 I(Mutant)
\]

Podaj `β0` i `β1`.

**Odpowiedź**

\[
\beta_0=\bar y_C=2.2
\]

\[
\beta_1=\bar y_M-\bar y_C=3.6-2.2=1.4
\]

---

### Zadanie 3. F = t²

Dla danych z zadania 1:

- `SSE_null = 7.56`,
- `SSE_full = 2.66`,
- `n=10`,
- model null ma 1 parametr,
- model full ma 2 parametry.

Policz `F`.

**Odpowiedź**

\[
F=\frac{(7.56-2.66)/(2-1)}{2.66/(10-2)}
\]

\[
F=\frac{4.90}{0.3325}=14.7368
\]

Dla klasycznego t-testu dwóch grup z równą wariancją:

\[
t=-3.8389
\]

\[
t^2=14.7368=F
\]

---

## Część B. Odds, log-odds i odds ratio

### Zadanie 4. Probability → odds → log-odds

Policz odds i log-odds dla `p=0.8`.

**Odpowiedź**

\[
odds=\frac{0.8}{1-0.8}=4
\]

\[
log(odds)=\log(4)=1.3863
\]

---

### Zadanie 5. Odds → probability

Jeżeli odds = 4, policz prawdopodobieństwo.

**Odpowiedź**

\[
p=\frac{odds}{1+odds}=\frac{4}{5}=0.8
\]

---

### Zadanie 6. Odds ratio

Tabela:

|          | Choroba Tak | Choroba Nie |
|----------|------------:|------------:|
| Ekspozycja Tak | 12 | 18 |
| Ekspozycja Nie | 5 | 35 |

Policz OR i log(OR).

**Odpowiedź**

\[
OR=\frac{12/18}{5/35}=\frac{12\cdot35}{18\cdot5}=4.6667
\]

\[
\log(OR)=\log(4.6667)=1.5404
\]

---

### Zadanie 7. Chi-square ręcznie

Dla tabeli z zadania 6 policz oczekiwane liczebności.

**Odpowiedź**

Suma całkowita:

\[
N=12+18+5+35=70
\]

Sumy wierszy: `30`, `40`.  
Sumy kolumn: `17`, `53`.

\[
E_{11}=\frac{30\cdot17}{70}=7.2857
\]

\[
E_{12}=\frac{30\cdot53}{70}=22.7143
\]

\[
E_{21}=\frac{40\cdot17}{70}=9.7143
\]

\[
E_{22}=\frac{40\cdot53}{70}=30.2857
\]

---

### Zadanie 8. Wald ręcznie

Dla tabeli z zadania 6 policz `SE(log(OR))`.

**Odpowiedź**

\[
SE=\sqrt{\frac{1}{12}+\frac{1}{18}+\frac{1}{5}+\frac{1}{35}}
\]

\[
SE=0.6108
\]

\[
z=\frac{1.5404}{0.6108}=2.5219
\]

Dwustronne p-value jest około `0.0117`.