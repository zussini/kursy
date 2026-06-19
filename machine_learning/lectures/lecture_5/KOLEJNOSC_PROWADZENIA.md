# Kolejność prowadzenia — v4 optimal

## Minimalna ścieżka do UMAP / DBSCAN

```text
0_0 → 0_1 → 2_4 → 2_3 → 1_1 → 3_1 → 3_2
```

## Pełna ścieżka

1. `0_0` — mapa metod i główna historia: punkty → odległości → sąsiedztwo → graf.
2. `0_1` — fundament: macierz odległości, $\varepsilon$-sąsiedztwo, kNN, graf, `union` vs `mutual`.
3. `2_4`, `2_3`, `1_1` — podobieństwa i UMAP.
4. `2_2`, `1_2` — t-SNE jako dopasowanie macierzy $P$ i $Q$.
5. `2_1`, `1_3` — PCA jako liniowy kontrast.
6. `3_1`, `3_2`, `3_3`, `3_4` — KNN, DBSCAN, k-means i porównanie.
7. `4_1`, `4_2`, `4_3`, `4_4` — LDA, QDA, SVC/SVM i kernel SVM.

## Gdzie pokazać panele interaktywne?

- `0_1`: po wyjaśnieniu `union` / `mutual`, bo wtedy suwak $k$ ma sens.
- `1_3`: po ręcznym PCA, jako kontrast „obracamy oś i patrzymy na wariancję”.
- `3_2`: po core/border/noise, bo suwak $\varepsilon$ pokazuje, że DBSCAN jest definicją gęstości.
- `3_3`: po pierwszych iteracjach k-means, żeby nie pokazywać wielu osobnych statycznych wykresów.
- `3_4`: po trzech metodach, żeby zobaczyć wpływ $k$ w KNN.
- `4_1`: po projekcji LDA, żeby zobaczyć różnicę między kierunkiem PCA i LDA.
- `4_3`: po soft margin, gdy wiadomo już, co oznacza $C$.
