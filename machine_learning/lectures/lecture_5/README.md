# ML algorytmy ręcznie — spójna ścieżka v4 optimal

Ta wersja scala najlepsze elementy gałęzi `v2` i `v3`.

Najważniejsze poprawki:

- `0_1` jest zbudowany jako wersja optymalna: bierze metodyczne dopowiedzenia z v2, poprawioną notację LaTeX z v3 i dodaje dwa panele interaktywne: $\varepsilon$ oraz $k$ / `union` / `mutual`.
- Markdown używa konsekwentnie `$...$` dla wzorów inline oraz `$$...$$` dla wzorów blokowych.
- Dodano panele interaktywne do wybranych notebooków: PCA, DBSCAN, k-means, porównanie KNN oraz LDA.
- `4_3_svc_svm_recznie_margines_soft_margin` wyświetla suwak $C$ także w notebooku, nie tylko zapisuje HTML.
- Usunięto z głównej ścieżki duplikaty `0_1_*_v2` / `0_1_*_v3_latex`, żeby student nie widział kilku wersji tego samego materiału.

## Główna kolejność

```text
0_0 mapa kursu
0_1 odległości, macierze sąsiedztwa, graf kNN

2_4 similarity scores UMAP/t-SNE
2_3 UMAP ręcznie
1_1 UMAP interaktywny

2_2 t-SNE ręcznie
1_2 t-SNE interaktywny

2_1 PCA ręcznie
1_3 PCA kontrast liniowy + panel projekcji

3_1 KNN
3_2 DBSCAN + panel eps
3_3 k-means + panel iteracji
3_4 porównanie KNN/DBSCAN/k-means + panel KNN

4_1 LDA + panel kierunku projekcji
4_2 QDA
4_3 SVC/SVM + suwak C
4_4 SVM kernelowy
```

## Uwaga praktyczna

Panele Plotly zapisują dodatkowe pliki HTML do katalogu `html/` po uruchomieniu notebooka. Dzięki temu można potem pokazywać same interaktywne wizualizacje bez uruchamiania Jupytera.
