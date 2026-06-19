# Odds, log-odds, odds ratio, Fisher, chi-square, Wald — notatki prowadzącego

## 1. Probability vs odds

Prawdopodobieństwo:

\[
p = \frac{sukcesy}{sukcesy+porażki}
\]

Odds:

\[
odds = \frac{sukcesy}{porażki}=\frac{p}{1-p}
\]

Powrót z odds do probability:

\[
p = \frac{odds}{1+odds}
\]

Log-odds:

\[
logit(p)=\log\left(\frac{p}{1-p}\right)
\]

Warto pokazać studentom:

- `p=0.5` daje odds `1` i log-odds `0`,
- `p=0.8` daje odds `4` i log-odds `1.386`,
- `p=0.2` daje odds `0.25` i log-odds `-1.386`.

## 2. Odds ratio

Tabela:

|                    | Cancer Yes | Cancer No |
|--------------------|-----------:|----------:|
| Mutated Yes        | a          | b         |
| Mutated No         | c          | d         |

\[
OR=\frac{a/b}{c/d}=\frac{ad}{bc}
\]

\[
\log(OR)=\log\left(\frac{ad}{bc}\right)
\]

Dla przykładu:

|                    | Cancer Yes | Cancer No |
|--------------------|-----------:|----------:|
| Mutated Yes        | 23         | 117       |
| Mutated No         | 6          | 210       |

\[
OR=\frac{23/117}{6/210}=6.88
\]

\[
\log(OR)=1.93
\]

Interpretacja: odds zachorowania w grupie z mutacją są około 6.88 razy większe niż w grupie bez mutacji.

## 3. Fisher exact test ręcznie

Przy ustalonych marginesach:

\[
P(A=k)=\frac{\binom{K}{k}\binom{N-K}{n-k}}{\binom{N}{n}}
\]

Gdzie:

- `N = a+b+c+d`,
- `K = a+c`, liczba przypadków pozytywnych,
- `n = a+b`, liczba osób w pierwszym wierszu,
- `A` = liczba pozytywnych w pierwszym wierszu.

Wersja dwustronna: sumujemy prawdopodobieństwa tabel co najmniej tak ekstremalnych jak obserwowana. Warto zaznaczyć, że istnieją różne definicje dwustronnego p-value w Fisherze.

## 4. Chi-square ręcznie

Liczebności oczekiwane:

\[
E_{ij}=\frac{row_i\ total \cdot column_j\ total}{N}
\]

Statystyka:

\[
\chi^2=\sum_{i,j}\frac{(O_{ij}-E_{ij})^2}{E_{ij}}
\]

Dla 2×2:

\[
df=1
\]

## 5. Wald dla log(OR)

Przybliżenie:

\[
\log(OR) \sim Normal
\]

Standard error:

\[
SE(\log(OR))=\sqrt{\frac{1}{a}+\frac{1}{b}+\frac{1}{c}+\frac{1}{d}}
\]

Statystyka:

\[
z=\frac{\log(OR)}{SE(\log(OR))}
\]

Przedział ufności dla log(OR):

\[
\log(OR) \pm 1.96SE
\]

Przedział ufności dla OR:

\[
\left(e^{low}, e^{high}\right)
\]

## 6. Połączenie z regresją logistyczną

Model:

\[
\log\left(\frac{p}{1-p}\right)=\beta_0+\beta_1 I(Mutated)
\]

Wtedy:

\[
\beta_1 = \log(OR)
\]

oraz:

\[
e^{\beta_1}=OR
\]

To jest najlepsze przejście do regresji logistycznej: nie modelujemy prawdopodobieństwa bezpośrednio linią, tylko modelujemy log-odds.

## Minimum ćwiczeniowe

1. Policz odds dla `p=0.75`.
2. Policz `p`, gdy odds = `3`.
3. Dla tabeli `[[12,18],[5,35]]` policz OR i log(OR).
4. Policz oczekiwane liczebności chi-square.
5. Policz `SE(log(OR))` i test Walda.