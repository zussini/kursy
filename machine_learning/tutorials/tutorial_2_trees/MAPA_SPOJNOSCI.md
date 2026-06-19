# MAPA_SPOJNOSCI — przegląd całej paczki po poprawkach

## Aktualna ścieżka pojęciowa

```text
4.1
cechy binarne
    ↓
gotowe pytania 0/1
    ↓
Gini
    ↓
jedno drzewo klasyfikacyjne

4.2A
cechy liczbowe
    ↓
szukanie progów
    ↓
Gini
    ↓
jedno drzewo klasyfikacyjne

4.2B
cechy liczbowe
    ↓
szukanie progów
    ↓
MSE/MAE
    ↓
jedno drzewo regresyjne

4.3
wiele drzew niezależnych
    ↓
bootstrap + losowanie cech
    ↓
głosowanie / średnia prawdopodobieństw
    ↓
Random Forest

4.4
wiele małych drzew sekwencyjnie
    ↓
residuale / gradienty / Hessiany
    ↓
learning_rate + regularizacja
    ↓
Gradient Boosting / XGBoost

4.5
praktyczny workflow
    ↓
preprocessing + porównanie modeli
    ↓
próg decyzyjny + feature importance + ranking
```

## Co zostało doprecyzowane

1. **Cechy binarne a zapis `<= 0.5`.**
   Dodano wyjaśnienie, że dla cech 0/1 próg `0.5` jest technicznym zapisem pytania `0 czy 1`.

2. **Progowanie a regresja.**
   W 4.2 wyraźnie oddzielono szukanie progów liczbowych od problemu regresji.

3. **Przejście do Random Forest.**
   Dodano most: pojedyncze drzewo jest interpretowalne, ale bywa niestabilne; Random Forest stabilizuje predykcję przez wiele drzew.

4. **Bagging vs Random Forest.**
   Dopisano rozróżnienie: Bagging = bootstrap + wiele drzew, Random Forest = bootstrap + wiele drzew + losowanie cech przy splitach.

5. **Metryki przy wyborze progu w Random Forest.**
   W 4.3 dodano appendix przypominający TP/FP/FN/TN, precision, recall, F1 i accuracy.

6. **`feature_importances_`.**
   Zmieniono opis na definicyjny: to miara wykorzystania cech w splitach i ich wkładu w poprawę kryterium drzewa. Uwaga o przyczynowości jest dodatkiem, nie główną definicją.

7. **Boosting jako suma poprawek.**
   W 4.4 dodano ręczne przejście przez kilka stumpów, predykcję nowego klienta oraz pokazanie, że nie wybiera się jednego drzewa — końcowy model to suma wielu drzew.

8. **Learning rate i liczba iteracji.**
   W 4.4 dodano końcowe porównanie dużego i małego `learning_rate` oraz tabelę pokazującą ewolucję wyników przy wielu iteracjach.

9. **Notebook 4.5 jako finał praktyczny.**
   Dodano krótki notebook pokazujący szybki workflow: preprocessing, porównanie modeli, próg decyzyjny, ważność cech i ranking obserwacji.

10. **Korekta techniczna 4.4.**
    Naprawiono błędny zapis `raise ValueError(...)` w sekcji z ręczną demonstracją stumpów.

## Trzy zdania porządkujące całość

1. **Progowanie cech liczbowych nie oznacza regresji.**
2. **Random Forest agreguje wiele niezależnych drzew.**
3. **Gradient Boosting i XGBoost sumują kolejne poprawki, a nie głosy niezależnych drzew.**
