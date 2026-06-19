# Plan prowadzenia ćwiczeń po wykładzie 4

## Aktualna sekwencja notebooków

Główna sekwencja materiału:

```text
1. cwiczenia_wyklad_4_01_reczne_gini_drzewo_student_doprecyzowane.ipynb
2. cwiczenia_wyklad_4_02_progi_liczbowe_drzewo_regresyjne_student_doprecyzowane.ipynb
3. cwiczenia_wyklad_4_03_random_forest_churn_student_podniesione.ipynb
4. cwiczenia_wyklad_4_04_gradient_boosting_xgboost_churn_student_boosting_zamkniete_lr_iteracje.ipynb
5. cwiczenia_wyklad_4_05_auto_xgboost_podsumowanie_student_neutral_appendix.ipynb
```

Notebook 4.5 jest krótkim zwieńczeniem: mniej ręcznego liczenia, więcej automatycznego workflow i porównania modeli.

## Co było na wykładzie

W pliku `wyklad_4_17_05_2026.ipynb` zrealizowany został głównie przykład `kup_lody`:

- dane binarne 0/1,
- nieczystość Giniego,
- ręczne liczenie splitu,
- porównanie `cieplo`, `weekend`, `krotka_kolejka`,
- drugi split dla gałęzi `cieplo = 1`,
- porównanie z `DecisionTreeClassifier`.

## Akcenty pojęciowe do pilnowania

### Notebook 4.1 — Gini i pierwsze drzewo

Ważny akcent: cechy są binarne, więc pytania są gotowe. `sklearn` zapisuje je jako `<= 0.5`, ale to nadal odpowiada podziałowi `0/1`.

### Notebook 4.2 — progi liczbowe i regresja

Przejście od:

```text
cieplo == 1?
```

do:

```text
projekt_pkt <= 59.5?
```

Najważniejszy wniosek: mechanizm drzewa jest ten sam, ale dla cech liczbowych trzeba znaleźć próg.

Drugi ważny wniosek:

```text
klasyfikacja: liść zwraca klasę, split minimalizuje Gini
regresja:     liść zwraca średnią/liczbę, split minimalizuje MSE/MAE
```

Progowanie nie oznacza regresji.

### Notebook 4.3 — Random Forest

Najważniejsze elementy do omówienia:

1. bootstrap wierszy,
2. OOB — obserwacje niewykorzystane przez dane drzewo,
3. losowanie cech przy splitach,
4. głosowanie drzew,
5. różnica między udziałem twardych głosów a `predict_proba`,
6. próg decyzyjny dla churn.

Random Forest nie zmienia pojedynczego splitu. Split dalej jest oceniany przez Gini/MSE. Nowe jest wiele drzew i agregacja.

### Notebook 4.4 — Gradient Boosting i XGBoost

Najlepiej tłumaczyć partiami algorytmu:

1. model startowy,
2. residual / gradient,
3. małe drzewo-poprawka,
4. `learning_rate`,
5. aktualizacja score,
6. kilka kolejnych stumpów,
7. predykcja nowego klienta przez sumę wszystkich drzew,
8. mały `learning_rate` i większa liczba iteracji,
9. XGBoost: gradient, Hessian, regularizacja, gain.

Ważny kontrast:

```text
Random Forest: drzewa niezależne, wynik to głosowanie/średnia.
Gradient Boosting: drzewa sekwencyjne, wynik to suma poprawek.
```

### Notebook 4.5 — szybki workflow automatyczny

Ten notebook ma pokazać praktyczne zastosowanie wcześniejszej wiedzy:

```text
dane -> preprocessing -> porównanie modeli -> próg decyzyjny -> ranking obserwacji
```

To nie jest notebook do długiego ręcznego rachunku. Ma pokazać, jak szybko użyć metod z 4.1–4.4 na bardziej złożonych danych.

## Trzy najważniejsze zdania do powtarzania

1. **Progowanie rozwiązuje problem cech liczbowych, ale nie jest definicją regresji.**
2. **Random Forest to wiele niezależnych drzew, a boosting to sekwencja drzew-poprawek.**
3. **XGBoost nie jest magicznym osobnym modelem; to regularizowany, praktyczny boosting drzewiasty.**
