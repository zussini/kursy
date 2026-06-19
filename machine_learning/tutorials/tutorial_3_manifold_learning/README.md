# AI-CS-ML — finalny zestaw 6h, wersja V3

## Zawartość

- `student/` — notebooki z krótkimi TODO, pseudokodem bliskim Pythonowi i autotestami,
- `prowadzacy/` — pełne rozwiązania,
- realne dane PRNG,
- agregaty przestrzenne gmin,
- instrukcja rozszerzenia o BDL/TERYT/CKE.

## Główne ulepszenia V2

- wszystkie wzory w komórkach Markdown korzystają z delimiterów `$...$` oraz `$$...$$`,
- każdy obowiązkowy TODO ma opis słowny i pseudokod bliski składni Python/NumPy,
- dwa księżyce porównują k-means, DBSCAN i Spectral Clustering,
- powierzchnia S jest pokazana z kilku rzutów i interaktywnie w Plotly,
- MDS, Isomap, t-SNE i UMAP pracują na danych ukrytych w 10 wymiarach,
- t-SNE i UMAP mają animację `P -> Q(Y)` podczas optymalizacji,
- projekt pokazuje skoki największej składowej, przyrost krawędzi, epsilon vs kNN, huby i DBSCAN,
- dodano automatyczne szkice wniosków i opcjonalną analizę wielowymiarową gmin.


## Dodatek V3: LDA, QDA i SVM/SVC

Dodano notebook `02B` w dwóch wersjach:

- student: krótkie TODO, pseudokod bliski NumPy/Pythonowi i autotesty,
- prowadzący: pełne rozwiązania.

Materiał obejmuje ręczne LDA, funkcję dyskryminacyjną QDA, margines i support vectors SVM, wpływ parametru `C`, macierz podobieństwa RBF oraz `SVC(kernel="precomputed")`. Projekt PRNG pozostaje ostatnim notebookiem głównej ścieżki.

## Aktualizacja V4 — dodatkowe analizy

Do notebooków dodano:

- wysokowymiarowe dwa księżyce porównujące PCA, MDS, Isomap, Laplacian Eigenmaps, t-SNE i UMAP,
- jawny panel skoku największej składowej grafu miast,
- histogram i dystrybuantę długości krawędzi dla grafu epsilon i kNN,
- cztery zoomy Śląska dla `eps = 15, 20, 25, 30 km`,
- Isomap miast Polski jako wizualizację odległości po grafie,
- porównanie drzewa surrogate ze „świadomym targetu” i drzewa kontekstowego bez bezpośrednich składników `need_score`.

Części te są oznaczone jako dodatkowe; prowadzący może je uruchomić po części obowiązkowej albo zadać do samodzielnej analizy.
