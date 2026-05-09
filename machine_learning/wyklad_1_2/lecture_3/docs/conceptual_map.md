# Conceptual Map: KNN, PCA, SVM, trees, XGBoost, manifold learning

## Jedno zdanie na temat

| Temat | Jak model „widzi” dane? | Najlepszy moment w kursie |
|---|---|---|
| KNN | punkty i ich lokalne sąsiedztwo | bardzo wcześnie |
| Decision Tree | reguły `if/else` po pojedynczych cechach | wcześnie, jako kontrast do KNN |
| PCA | nowy układ współrzędnych oparty na wariancji | po pierwszych modelach, przed SVM |
| SVM | globalna granica o maksymalnym marginesie | po PCA lub równolegle z PCA |
| Kernel SVM | separacja w niejawnej bogatszej przestrzeni | po linear SVM |
| Random Forest | wiele drzew redukujących wariancję | po drzewach, przed boostingiem |
| Gradient Boosting | sekwencyjne poprawianie błędów | po Random Forest |
| XGBoost | mocny, regularizowany boosting drzew | później, opcjonalnie |
| Manifold Learning | lokalnie płaska, globalnie zakrzywiona struktura | po PCA, KNN i SVM |

---

## Jak PCA i KNN łączą się z SVM?

### KNN → SVM

KNN uczy, że klasyfikacja może wynikać z geometrii danych:

```text
KNN: patrzymy na sąsiadów punktu
SVM: szukamy globalnej granicy między klasami
```

To przejście jest naturalne dydaktycznie:

```text
lokalna decyzja → globalna decyzja
```

### PCA → SVM

PCA uczy, że przestrzeń cech można zmienić:

```text
oryginalne cechy → nowe osie / komponenty
```

SVM korzysta z geometrii tej przestrzeni:

```text
SVM: hiperplan + margines + iloczyny skalarne
```

Dlatego PCA jest dobrym wstępem do SVM, bo student już rozumie, że:

- reprezentacja ma znaczenie,
- skalowanie ma znaczenie,
- odległości i kierunki w przestrzeni mają znaczenie.

### Kernel SVM → Manifold Learning

Kernel SVM mówi:

```text
możemy pracować w bogatszej przestrzeni cech bez jawnego jej konstruowania
```

Manifold learning mówi:

```text
dane mogą mieć nieliniową strukturę, którą próbujemy odkryć przez lokalne sąsiedztwa
```

To są różne odpowiedzi na podobne pytanie:

> Czy oryginalna przestrzeń cech jest właściwym miejscem do uczenia?

---

## Kiedy XGBoost?

XGBoost nie jest dobry jako pierwszy model, bo wymaga zrozumienia:

- drzew decyzyjnych,
- overfittingu,
- ensemble learning,
- funkcji straty,
- walidacji,
- regularizacji,
- hiperparametrów.

Najlepszy moment:

```text
Decision Tree → Random Forest → Gradient Boosting → XGBoost
```

Dydaktycznie XGBoost warto pokazać jako:

```text
praktyczny standard dla danych tablicowych, nie jako pierwszy model teoretyczny
```

---

## Dwie osie kursu

### Oś geometryczna

```text
KNN → PCA → SVM → Kernel SVM → Manifold Learning
```

### Oś drzewiasta

```text
Decision Tree → Random Forest → Gradient Boosting → XGBoost
```

Najlepszy kurs łączy obie osie:

```text
KNN
Decision Tree
PCA
SVM
Random Forest
Gradient Boosting / XGBoost optional
Manifold Learning
```
