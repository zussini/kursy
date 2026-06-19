# Ćwiczenie 4.5 — szybka analiza automatyczna z metodami drzewiastymi i XGBoost

Krótki notebook końcowy do pakietu 4.1–4.4.

Cel: pokazać praktyczny workflow po zrozumieniu drzew, Random Forest, Gradient Boosting i XGBoost:

```text
dane -> preprocessing -> porównanie modeli -> dobór progu -> feature importance -> ranking obserwacji
```

## Pliki

- `cwiczenia_wyklad_4_05_auto_xgboost_podsumowanie_student_neutral_appendix.ipynb` — wersja z krótkimi TODO.
- `cwiczenia_wyklad_4_05_auto_xgboost_podsumowanie_rozwiazania_neutral_appendix.ipynb` — wersja rozwiązaniowa.
- `cwiczenia_wyklad_4_05_auto_xgboost_podsumowanie_rozwiazania_executed_neutral_appendix.ipynb` — wersja wykonana.

## Co zostało dopracowane

1. Dodano pola opisowe `customer_id` i `customer_name`.
2. Identyfikator i nazwa są zostawione w tabelach oraz w rankingu, ale są wykluczone z treningu modelu.
3. W rankingu klientów wynik modelu i cechy ryzyka są pokazane najpierw, a `customer_id` i `customer_name` na końcu tabeli.
4. Dodano appendiksy z przypomnieniem metryk, parametrów modeli i `feature_importances_`.
5. Język notebooka został ujednolicony i zapisany neutralniej, jako materiał do pracy z notebookiem.

## Dlaczego dane syntetyczne?

Notebook generuje lokalnie syntetyczny churn klientów, więc działa bez internetu i bez zewnętrznych plików.
Dane mają nieliniowe zależności oraz interakcje, np.:

- dużo reklamacji + umowa miesięczna,
- mało logowań + oferta konkurencji,
- długi staż + rabat.

Dzięki temu metody drzewiaste mają okazję pokazać przewagę nad pojedynczym drzewem i baseline.

## Appendixy w notebooku

Na końcu notebooka są krótkie przypomnienia:

- jak podmienić dane i ustawić `TARGET`, `ID_COL`, `NAME_COLS`,
- czym są `accuracy`, `precision_tak`, `recall_tak`, `f1_tak`, `roc_auc`, `log_loss`,
- jak działa próg decyzyjny,
- co oznaczają najważniejsze parametry modeli,
- czym jest `feature_importances_` i czego z niej nie należy wyciągać automatycznie.

## Sugerowany sposób użycia

Notebook jest przewidziany jako krótkie zwieńczenie zajęć. Nie trzeba go omawiać tak szczegółowo jak 4.1–4.4.
Najważniejsze jest przejście przez cały workflow:

1. przygotowanie danych,
2. porównanie kilku modeli,
3. wybór progu decyzyjnego,
4. interpretacja metryk,
5. sprawdzenie ważności cech,
6. przygotowanie rankingu obserwacji do działania.
