# Sekwencja dydaktyczna

## Moduł 0 — mapa kursu

Cel: student rozumie, że modele ML nie są tylko listą algorytmów, ale różnymi sposobami patrzenia na dane.

Główna oś:

```text
geometria lokalna → reguły → reprezentacja → margines → ensemble → manifold
```

---

## Moduł 1 — KNN: lokalna geometria

Pytanie lekcji:

> Czy punkty blisko siebie są podobne?

Dane:

- `blobs_margin`
- `moons`
- `iris`

Pojęcia:

- odległość
- sąsiedztwo
- `k`
- skalowanie
- curse of dimensionality jako zapowiedź PCA

Ćwiczenia:

1. Porównaj KNN dla `k=1`, `k=7`, `k=31`.
2. Uruchom KNN bez skalowania i ze skalowaniem.
3. Zobacz granicę decyzyjną na `moons`.

---

## Moduł 2 — drzewa decyzyjne: reguły zamiast geometrii

Pytanie lekcji:

> Czy da się klasyfikować przez serię pytań if/else?

Dane:

- `moons`
- `iris`
- `breast_cancer`

Pojęcia:

- split
- impurity: Gini/entropy
- depth
- interpretowalność
- overfitting

Ćwiczenia:

1. Porównaj drzewo płytkie i głębokie.
2. Zobacz, że drzewo nie potrzebuje skalowania.
3. Porównaj granicę drzewa z granicą KNN.

---

## Moduł 3 — PCA: reprezentacja danych

Pytanie lekcji:

> Czy dane można opisać prostszym układem współrzędnych?

Dane:

- `iris`
- `high_dim_redundant`
- `breast_cancer`

Pojęcia:

- wariancja
- komponenty główne
- projekcja
- redukcja wymiaru
- utrata informacji

Ćwiczenia:

1. Narysuj `explained_variance_ratio_`.
2. Porównaj KNN/SVM przed i po PCA.
3. Pokaż, że PCA jest transformacją liniową, a nie klasyfikatorem.

---

## Moduł 4 — SVM: margines i separacja

Pytanie lekcji:

> Która granica decyzyjna jest najbardziej stabilna?

Dane:

- `blobs_margin`
- `moons`
- `circles`
- `high_dim_redundant`

Pojęcia:

- hiperplan
- margines
- support vectors
- soft margin
- `C`
- kernel RBF
- `gamma`

Ćwiczenia:

1. Linear SVM na `blobs_margin`.
2. Linear SVM vs RBF SVM na `moons`.
3. `circles`: dodaj ręcznie `r²`, a potem użyj RBF kernel.

---

## Moduł 5 — ensemble: Random Forest i Gradient Boosting

Pytanie lekcji:

> Co daje wiele drzew zamiast jednego?

Dane:

- `breast_cancer`
- `high_dim_redundant`

Pojęcia:

- bagging
- variance reduction
- boosting
- model sekwencyjny
- learning rate
- walidacja

Ćwiczenia:

1. Decision Tree vs Random Forest.
2. Random Forest vs Gradient Boosting.
3. Porównaj wynik z SVM i KNN na danych tablicowych.

---

## Moduł 6 — XGBoost jako opcja późniejsza

Pytanie lekcji:

> Dlaczego boosting drzew jest tak mocny praktycznie?

XGBoost nie jest dobrym pierwszym modelem, ale jest świetnym końcowym benchmarkiem dla danych tablicowych.

Minimalne wymagania przed XGBoost:

- drzewo decyzyjne
- funkcja straty
- validation split
- overfitting
- regularizacja
- ensemble learning

---

## Moduł 7 — manifold learning

Pytanie lekcji:

> Co jeśli dane leżą na zakrzywionej powierzchni?

Dane:

- `swiss_roll`
- `moons`

Pojęcia:

- lokalne sąsiedztwa
- zakrzywiona struktura
- Isomap
- LLE
- t-SNE
- UMAP jako opcja
- embeddingi jako most do deep learningu

Najważniejsza intuicja:

```text
PCA zakłada liniową podprzestrzeń.
Manifold learning zakłada nieliniową, ale lokalnie prostą strukturę.
```

## Uzupełnienie: wykład 08 — regresja liniowa

Proponowana najprostsza kolejność:

1. Dane i scatterplot: `weight -> size`.
2. Baseline: zawsze przewiduj średnią.
3. Kilka ręcznych prostych i porównanie SSE.
4. `LinearRegression().fit(X, y)` jako minimalizacja SSE.
5. Metryki: MAE, MSE, RMSE, $R^2$.
6. Dokładne liczenie $R^2$: TSS, SSE, SSR.
7. Adjusted $R^2$ i pułapka dodawania cech.
8. Test $F$ jako pytanie: czy model jest lepszy od średniej?
9. Train/test, CV, underfitting i overfitting.
10. GeoGebra: suwaki prostej, `FitLine`, $R^2$, porównanie wielomianów.


## Uzupełnienie do bloku Linear models: GLM, t-test i ANOVA

Po notebooku `08_linear_regression_lecture.ipynb` można zrobić 20–30 minutowy moduł:

1. `09_statquest_glm_gene_expression_design_matrix.ipynb`
2. Control vs Mutant jako dwie średnie.
3. Design matrix z kolumnami `Control`, `Mutant`.
4. Ręczne liczenie `SSE_mean`, `SSE_fit`, `F`.
5. Rozszerzenie do ANOVA: pięć grup.
6. Rozszerzenie praktyczne: `gene_expression ~ mouse_weight + genotype`.

Cel: pokazać, że regresja liniowa, t-test i ANOVA mają wspólny mechanizm porównywania modeli.
