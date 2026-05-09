# GeoGebra — wprawki v6.1 do bloku logistic/ROC/regularization

Poprzednie pliki GeoGebry były za krótkie i za mało „prowadzące”. Ten zestaw ma dwie warstwy:

1. **Pliki `.ggbscript.txt`** — najbezpieczniejsze do użycia: otwórz GeoGebrę, wklej komendy linia po linii albo partiami.
2. **Prototypy `.ggb`** — proste pliki startowe. Nie traktuj ich jako finalnych apletów, raczej jako szybki szkic obiektów.

Najlepiej prowadzić GeoGebrę jako krótkie 5–8 minutowe wprawki, nie jako pełny wykład.

## GG01: probability → odds → log-odds

Cel: zobaczyć, dlaczego probability nie jest dobrą skalą dla prostej liniowej, a log-odds jest.

Prowadzenie:

1. Ustaw `p=0.2`.
2. Policz `odds = p/(1-p)`.
3. Policz `logodds = ln(odds)`.
4. Zmień `p` na 0.8.
5. Zauważ, że log-odds zmienia znak symetrycznie.

Komentarz tablicowy:

$$
p=0.2 \Rightarrow odds=0.25 \Rightarrow \log(odds)\approx -1.386
$$

$$
p=0.8 \Rightarrow odds=4 \Rightarrow \log(odds)\approx 1.386
$$

## GG02: odds ratio z tabeli 2×2

Cel: pokazać, że OR to tylko iloraz dwóch odds.

Tabela:

$$
\begin{array}{c|cc}
& Cancer+ & Cancer- \\
\hline
Mutation+ & a & b \\
Mutation- & c & d
\end{array}
$$

$$
OR=\frac{a/b}{c/d}=\frac{ad}{bc}
$$

Prowadzenie:

1. Zacznij od `a=23`, `b=117`, `c=6`, `d=210`.
2. Pokaż `OR` i `logOR`.
3. Zmień `a` i zobacz, jak rośnie OR.
4. Pokaż `SE`, `zWald`, ale nie zaczynaj od p-value.

## GG03: sigmoid i próg decyzyjny

Cel: pokazać, że regresja logistyczna jest liniowa na log-odds, ale krzywa na probability.

Prowadzenie:

1. Zmieniaj `beta0` — krzywa przesuwa się w lewo/prawo.
2. Zmieniaj `beta1` — krzywa robi się bardziej lub mniej stroma.
3. Zmieniaj `threshold` — decyzja klasyfikacyjna przesuwa się niezależnie od modelu.

## GG04: likelihood dla kilku punktów

Cel: odczarować maximum likelihood.

Dla punktu pozytywnego wkład to $p_i$.
Dla punktu negatywnego wkład to $1-p_i$.

Log-likelihood:

$$
\ell=\sum_i y_i\log(p_i)+(1-y_i)\log(1-p_i)
$$

Prowadzenie:

1. Zmień `beta0` i `beta1`.
2. Obserwuj `logL`.
3. Powiedz: algorytm szuka takich parametrów, które maksymalizują `logL`.

## GG05: ROC jako przesuwanie progu

Cel: oddzielić score od decyzji.

Prowadzenie:

1. Ustaw próg wysoko: mało pozytywnych predykcji.
2. Ustaw próg nisko: dużo pozytywnych predykcji.
3. Obserwuj `TPR` i `FPR`.
4. Pokaż punkt `(FPR, TPR)`.

## GG06: geometria L1 i L2

Cel: pokazać, dlaczego Lasso częściej daje zera.

Prowadzenie:

1. Pokaż kontury straty.
2. Pokaż okrąg L2.
3. Pokaż romb L1.
4. Wyjaśnij: romb ma narożniki na osiach, dlatego optimum częściej trafia w $\beta_j=0$.

$$
L2: \beta_1^2+\beta_2^2\le c
$$

$$
L1: |\beta_1|+|\beta_2|\le c
$$
