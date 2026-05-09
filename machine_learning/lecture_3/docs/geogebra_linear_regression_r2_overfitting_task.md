# GeoGebra — regresja liniowa, $R^2$ i overfitting

## Cel aktywności

Studenci mają zobaczyć trzy rzeczy:

1. regresja liniowa minimalizuje SSE,
2. $R^2$ porównuje model z baseline’em średniej,
3. mniejszy błąd treningowy nie zawsze oznacza lepszy model predykcyjny.

## Krok 1 — punkty

Wpisz w GeoGebrze:

```text
L = {(0.9,1.4), (1.8,2.6), (2.4,1.0), (3.5,3.7), (3.9,5.5), (4.4,3.2), (5.1,3.0), (5.6,4.9), (6.3,6.3)}
```

## Krok 2 — ręczna prosta

Dodaj suwaki `a` i `b`.

```text
f(x) = a*x + b
SSE_manual = SumSquaredErrors(L, f)
```

Zadanie: poruszaj suwakami, aż `SSE_manual` będzie możliwie małe.

## Krok 3 — automatyczna regresja

```text
g(x) = FitLine(L)
SSE_fit = SumSquaredErrors(L, g)
```

Pytania:

1. Czy Twoja ręczna prosta ma podobny błąd jak `g(x)`?
2. Czy prosta regresji musi przechodzić przez wiele punktów?
3. Dlaczego liczymy pionowe odległości od prostej?

## Krok 4 — baseline średniej i $R^2$

```text
ybar = Mean({1.4,2.6,1.0,3.7,5.5,3.2,3.0,4.9,6.3})
m(x) = ybar
SSE_mean = SumSquaredErrors(L, m)
R2 = 1 - SSE_fit / SSE_mean
```

Pytania:

1. Co oznacza `SSE_mean`?
2. Co oznacza `SSE_fit`?
3. Dlaczego $R^2 = 1 - SSE_fit / SSE_mean$?
4. Co oznaczałoby $R^2 = 0$?
5. Co oznaczałoby $R^2 = 1$?

## Krok 5 — overfitting przez wielomiany

```text
p1(x) = FitPoly(L, 1)
p2(x) = FitPoly(L, 2)
p5(x) = FitPoly(L, 5)
SSE_p1 = SumSquaredErrors(L, p1)
SSE_p2 = SumSquaredErrors(L, p2)
SSE_p5 = SumSquaredErrors(L, p5)
```

Pytania:

1. Który wielomian ma najmniejszy SSE na danych treningowych?
2. Czy krzywa stopnia 5 wygląda stabilnie?
3. Czy taki model może źle przewidywać nowe punkty?
4. Jak zasymulować test set? Ukryj 2–3 punkty, dopasuj model do reszty, a potem sprawdź błędy na ukrytych punktach.

## Puenta

Najmniejsze SSE na danych, które widzieliśmy, nie gwarantuje najlepszego modelu. Dlatego w ML potrzebujemy walidacji, cross-validation i regularizacji.
