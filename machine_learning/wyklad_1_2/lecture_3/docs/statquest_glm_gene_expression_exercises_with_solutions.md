# Proste ćwiczenia: ekspresja genu, t-test, ANOVA i masa myszy

## Ćwiczenie 1 — średnie grupowe

Dane:

| grupa | ekspresja |
|---|---:|
| Control | 1.7 |
| Control | 2.1 |
| Control | 2.3 |
| Control | 2.7 |
| Mutant | 3.1 |
| Mutant | 3.4 |
| Mutant | 3.7 |
| Mutant | 4.2 |

Policz:

1. średnią ogólną,
2. średnią Control,
3. średnią Mutant.

### Odpowiedź

\[
\bar y = 2.9
\]

\[
\bar y_{Control}=2.2
\]

\[
\bar y_{Mutant}=3.6
\]

---

## Ćwiczenie 2 — SSE dla modelu zerowego

Model zerowy przewiduje każdej myszy wartość 2.9.

Policz:

\[
SSE_{mean}=\sum_i(y_i-2.9)^2
\]

### Odpowiedź

\[
SSE_{mean}=5.10
\]

---

## Ćwiczenie 3 — SSE dla modelu grupowego

Model grupowy przewiduje:

- 2.2 dla Control,
- 3.6 dla Mutant.

Policz:

\[
SSE_{fit}=\sum_i(y_i-\hat y_i)^2
\]

### Odpowiedź

Dla Control:

\[
(1.7-2.2)^2+(2.1-2.2)^2+(2.3-2.2)^2+(2.7-2.2)^2=0.52
\]

Dla Mutant:

\[
(3.1-3.6)^2+(3.4-3.6)^2+(3.7-3.6)^2+(4.2-3.6)^2=0.66
\]

Razem:

\[
SSE_{fit}=1.18
\]

---

## Ćwiczenie 4 — test F

Użyj:

- \(SSE_{mean}=5.10\),
- \(SSE_{fit}=1.18\),
- \(n=8\),
- \(p_{mean}=1\),
- \(p_{fit}=2\).

Policz:

\[
F=\frac{(SSE_{mean}-SSE_{fit})/(p_{fit}-p_{mean})}{SSE_{fit}/(n-p_{fit})}
\]

### Odpowiedź

\[
F=\frac{(5.10-1.18)/(2-1)}{1.18/(8-2)}
\]

\[
F=\frac{3.92}{0.1967}\approx 19.93
\]

---

## Ćwiczenie 5 — design matrix

Uzupełnij macierz projektu dla modelu:

\[
\hat y_i=I(Control)\mu_C+I(Mutant)\mu_M
\]

| obserwacja | grupa | Control | Mutant |
|---:|---|---:|---:|
| 1 | Control | ? | ? |
| 2 | Control | ? | ? |
| 3 | Control | ? | ? |
| 4 | Control | ? | ? |
| 5 | Mutant | ? | ? |
| 6 | Mutant | ? | ? |
| 7 | Mutant | ? | ? |
| 8 | Mutant | ? | ? |

### Odpowiedź

| obserwacja | grupa | Control | Mutant |
|---:|---|---:|---:|
| 1 | Control | 1 | 0 |
| 2 | Control | 1 | 0 |
| 3 | Control | 1 | 0 |
| 4 | Control | 1 | 0 |
| 5 | Mutant | 0 | 1 |
| 6 | Mutant | 0 | 1 |
| 7 | Mutant | 0 | 1 |
| 8 | Mutant | 0 | 1 |

---

## Ćwiczenie 6 — standardowy zapis z interceptem

Model:

\[
\hat y=\beta_0+\beta_1 I(Mutant)
\]

Wiadomo, że średnia Control to 2.2, a średnia Mutant to 3.6.

Policz \(\beta_0\) i \(\beta_1\).

### Odpowiedź

\[
\beta_0=2.2
\]

bo dla Control mamy \(I(Mutant)=0\).

\[
\beta_1=3.6-2.2=1.4
\]

bo dla Mutant model daje \(2.2+1.4=3.6\).

---

## Ćwiczenie 7 — związek z t-testem

Dla dwóch grup klasyczny t-test z założeniem równej wariancji daje statystykę \(t\). Jednoczynnikowa ANOVA daje statystykę \(F\).

Jaki jest związek między nimi?

### Odpowiedź

\[
F=t^2
\]

Dla tego przykładu \(F\approx 19.93\), więc \(|t|\approx\sqrt{19.93}\approx 4.46\).

---

## Ćwiczenie 8 — masa myszy jako zmienna zakłócająca

Załóżmy, że mutanty są przeciętnie cięższe niż myszy kontrolne, a ekspresja genu rośnie z masą myszy.

Dlaczego porównanie samych średnich Control vs Mutant może być mylące?

### Odpowiedź

Bo różnica średnich może wynikać częściowo z genotypu, a częściowo z masy. Model:

\[
\widehat{expression}=\beta_0+\beta_1 weight+\beta_2I(Mutant)
\]

pozwala zapytać: czy genotyp nadal ma efekt, gdy porównujemy myszy o tej samej masie?

---

## Ćwiczenie 9 — interpretacja współczynników

Model:

\[
\widehat{expression}=\beta_0+0.18\cdot weight+0.93\cdot I(Mutant)
\]

Zinterpretuj współczynniki 0.18 i 0.93.

### Odpowiedź

- 0.18: przy tym samym genotypie wzrost masy o 1 jednostkę zwiększa przewidywaną ekspresję średnio o 0.18.
- 0.93: przy tej samej masie myszy mutanty mają przewidywaną ekspresję wyższą średnio o 0.93 względem Control.

---

## Ćwiczenie 10 — kiedy dodać interakcję?

Model addytywny:

\[
expression=\beta_0+\beta_1weight+\beta_2I(Mutant)
\]

Model z interakcją:

\[
expression=\beta_0+\beta_1weight+\beta_2I(Mutant)+\beta_3weight\cdot I(Mutant)
\]

Co oznacza interakcja?

### Odpowiedź

Interakcja oznacza, że wpływ masy na ekspresję może być inny w grupie Control i inny w grupie Mutant. Geometrycznie: grupy mogą mieć różne nachylenia prostych.
