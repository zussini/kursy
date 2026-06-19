# Walidacja V4

Sprawdzono sekwencyjne wykonanie komórek rozwiązaniowych notebooków:

- `prowadzacy/02_MDS_tSNE_UMAP_ROZWIAZANIA.ipynb`,
- `prowadzacy/03_PROJEKT_miejscowosci_polaczenia_ROZWIAZANIA.ipynb`.

Obowiązkowe ścieżki zakończyły się bez błędów.

## Wyniki kontrolne

### Wysokowymiarowe księżyce

Na danych 12-wymiarowych metody lokalne wyraźnie lepiej zachowują sąsiedztwa obu łuków niż PCA/MDS. W środowisku walidacyjnym, przy pominięciu opcjonalnego bibliotecznego UMAP, najlepsze wyniki lokalnej separacji uzyskiwały t-SNE, Laplacian Eigenmaps i Isomap.

### Graf miast

- największa składowa przekracza 50% około `17.5 km`,
- przekracza 90% około `22 km`,
- przekracza 99% około `27 km`,
- pełna spójność pojawia się około `46.5 km`,
- największy skok największej składowej występuje około `17 km`.

### Drzewa A/B

- drzewo surrogate korzystające ze składników `need_score`: ROC AUC około `0.983`,
- drzewo kontekstowe bez bezpośrednich składników score: ROC AUC około `0.882`.

Różnica jest celowym elementem dydaktycznym: pierwsze drzewo streszcza definicję wskaźnika, drugie sprawdza generalizację z szerszego kontekstu przestrzennego.

## Elementy interaktywne

Animacje Plotly i gotowa implementacja `umap-learn` są opcjonalne i wymagają środowiska Jupyter z zależnościami z `requirements.txt`. Ręczne konstrukcje macierzy P/Q oraz funkcji strat nie zależą od `umap-learn`.
