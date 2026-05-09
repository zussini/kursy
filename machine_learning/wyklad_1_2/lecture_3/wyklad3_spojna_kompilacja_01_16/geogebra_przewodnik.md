
# GeoGebra — przewodnik do wykładu 3

Plik:

```text
geogebra/Dopasowanie_prostej_odleglosci_normy_pogladowo.ggb
```

## Część 1: regresja liniowa

Użyj GeoGebry do pokazania:

1. punktów jako obserwacji,
2. prostej jako modelu,
3. pionowych reszt:

$$
e_i = y_i - \hat y_i
$$

4. średniej jako baseline'u:

$$
\bar y
$$

5. różnicy między:

$$
y_i - \bar y
$$

a:

$$
y_i - \hat y_i
$$

6. intuicji:

$$
R^2 = 1 - \frac{RSS}{TSS}
$$

## Część 2: logistyka

Dla logistyki najlepiej zrobić osobny szkic w GeoGebrze:

1. linia log-odds:

$$
\eta = b_0+b_1x
$$

2. sigmoid:

$$
p = \frac{1}{1+e^{-\eta}}
$$

3. próg decyzyjny $t$,
4. pokazanie, że zmiana progu zmienia confusion matrix.

## Najważniejsze zdanie dla studentów

Regresja liniowa modeluje bezpośrednio liczbę:

$$
\hat y = b_0+b_1x
$$

Regresja logistyczna modeluje liniowo log-odds:

$$
\log\left(\frac{p}{1-p}\right)=b_0+b_1x
$$
