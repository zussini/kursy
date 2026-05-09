# Ściąga wykładowa: GLM + odds/testy

## Design matrix

\[
y=X\beta+\varepsilon
\]

| Temat | Formula | Kolumny w X | Główna interpretacja |
|---|---|---|---|
| Regresja | `y ~ x` | `1`, `x` | nachylenie |
| t-test | `y ~ group` | `1`, `I(group=B)` | różnica średnich |
| ANOVA | `y ~ group` | `1`, k−1 dummy | czy grupy się różnią globalnie |
| ANCOVA | `y ~ x + group` | `1`, `x`, dummy | grupa po kontroli x |
| Interakcja | `y ~ x * group` | `1`, `x`, dummy, `x*dummy` | różne nachylenia |

## F-test dla modeli zagnieżdżonych

\[
F=\frac{(SSE_{null}-SSE_{full})/(p_{full}-p_{null})}{SSE_{full}/(n-p_{full})}
\]

Dla dwóch grup:

\[
F=t^2
\]

## Odds

\[
odds=\frac{p}{1-p}
\]

\[
logit(p)=\log\left(\frac{p}{1-p}\right)
\]

## Odds ratio

Dla tabeli:

\[
\begin{array}{c|cc}
 & Yes & No \\
\hline
Exposed & a & b \\
Not\ exposed & c & d
\end{array}
\]

\[
OR=\frac{ad}{bc}
\]

\[
\log(OR)=\log\left(\frac{ad}{bc}\right)
\]

## Wald dla log(OR)

\[
SE=\sqrt{\frac{1}{a}+\frac{1}{b}+\frac{1}{c}+\frac{1}{d}}
\]

\[
z=\frac{\log(OR)}{SE}
\]

## Chi-square

\[
E_{ij}=\frac{row_i\ total\cdot col_j\ total}{N}
\]

\[
\chi^2=\sum\frac{(O-E)^2}{E}
\]

## Fisher

\[
P(A=k)=\frac{\binom{K}{k}\binom{N-K}{n-k}}{\binom{N}{n}}
\]