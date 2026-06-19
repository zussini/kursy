# Ćwiczenia po wykładzie 4: drzewa, lasy, boosting i XGBoost

Ta paczka zawiera uporządkowaną ścieżkę ćwiczeń po wykładzie 4. Aktualnie główna sekwencja ma pięć notebooków:

```text
4.1  pojedyncze drzewo klasyfikacyjne na cechach binarnych
4.2  progi liczbowe, klasyfikacja i drzewo regresyjne
4.3  Random Forest: bootstrap, losowanie cech, głosowanie
4.4  Gradient Boosting i XGBoost: sekwencyjne poprawianie błędów
4.5  szybka analiza automatyczna: porównanie metod i praktyczny workflow
```

## Najważniejsze pliki

### Wersje dla studentów

- `cwiczenia_wyklad_4_01_reczne_gini_drzewo_student_doprecyzowane.ipynb`
- `cwiczenia_wyklad_4_02_progi_liczbowe_drzewo_regresyjne_student_doprecyzowane.ipynb`
- `cwiczenia_wyklad_4_03_random_forest_churn_student_podniesione.ipynb`
- `cwiczenia_wyklad_4_04_gradient_boosting_xgboost_churn_student_boosting_zamkniete_lr_iteracje.ipynb`
- `cwiczenia_wyklad_4_05_auto_xgboost_podsumowanie_student_neutral_appendix.ipynb`

### Wersje z rozwiązaniami

- `cwiczenia_wyklad_4_01_reczne_gini_drzewo_rozwiazania_doprecyzowane.ipynb`
- `cwiczenia_wyklad_4_02_progi_liczbowe_drzewo_regresyjne_rozwiazania_doprecyzowane.ipynb`
- `cwiczenia_wyklad_4_03_random_forest_churn_rozwiazania_podniesione.ipynb`
- `cwiczenia_wyklad_4_04_gradient_boosting_xgboost_churn_rozwiazania_boosting_zamkniete_lr_iteracje.ipynb`
- `cwiczenia_wyklad_4_05_auto_xgboost_podsumowanie_rozwiazania_neutral_appendix.ipynb`

### Wersje wykonane / kontrolne

- `cwiczenia_wyklad_4_01_reczne_gini_drzewo_rozwiazania_executed_doprecyzowane.ipynb`
- `cwiczenia_wyklad_4_02_progi_liczbowe_drzewo_regresyjne_rozwiazania_executed_doprecyzowane.ipynb`
- `cwiczenia_wyklad_4_03_random_forest_churn_rozwiazania_executed_podniesione.ipynb`
- `cwiczenia_wyklad_4_04_gradient_boosting_xgboost_churn_rozwiazania_executed_boosting_zamkniete_lr_iteracje.ipynb`
- `cwiczenia_wyklad_4_05_auto_xgboost_podsumowanie_rozwiazania_executed_neutral_appendix.ipynb`

## Pliki dodatkowe

- `wyklad_4_17_05_2026.ipynb` — notebook wykładowy.
- `prowadzenie_cwiczen_wyklad_4.md` — notatka organizacyjna do prowadzenia ćwiczeń.
- `MAPA_SPOJNOSCI.md` — mapa narracji i lista doprecyzowań.
- `analiza_wykladu_4_i_plan_cwiczen.md` — analiza materiału i ryzyk nieporozumień.
- `README_wyklad_4_05_auto_xgboost_podsumowanie_neutral_appendix.md` — osobny README do notebooka 4.5.

## Główna narracja dydaktyczna

```text
Notebook 4.1
cechy binarne -> gotowe pytania TAK/NIE -> Gini -> klasa

Notebook 4.2A
cechy liczbowe -> szukanie progów -> Gini -> klasa

Notebook 4.2B
cechy liczbowe -> szukanie progów -> MSE/MAE -> liczba

Notebook 4.3
wiele niezależnych drzew -> bootstrap + losowanie cech -> głosowanie/średnia

Notebook 4.4
wiele małych drzew sekwencyjnie -> residuale/gradienty -> learning_rate -> regularizacja

Notebook 4.5
praktyczny workflow -> preprocessing -> porównanie modeli -> próg -> ranking obserwacji
```

Najważniejsze rozróżnienia utrwalane w notebookach:

1. `sklearn` pokazuje `<= 0.5` dla cech 0/1, ale to nadal jest zwykły podział binarny.
2. Progowanie cech liczbowych nie oznacza regresji — regresja zaczyna się wtedy, gdy przewidujemy liczbę.
3. Random Forest nie zmienia pojedynczego splitu; zmienia sposób budowania i agregacji wielu drzew.
4. Gradient Boosting nie jest kolejnym lasem; drzewa są budowane po kolei i dodają poprawki.
5. XGBoost to regularizowana, wydajna wersja boostingu, która używa gradientów, Hessianów i kar za złożoność.
6. Notebook 4.5 nie jest kolejnym ręcznym rachunkiem, tylko krótkim zastosowaniem całej ścieżki w praktyce.

## Wymagane biblioteki

Podstawowe:

```bash
pip install numpy pandas matplotlib scikit-learn
```

Opcjonalne:

```bash
pip install xgboost
```

`xgboost` jest opcjonalny. Notebooki 4.4 i 4.5 sprawdzają, czy pakiet jest dostępny. Jeśli nie jest dostępny, część XGBoost zostanie pominięta, a porównanie nadal działa dla modeli ze scikit-learn.

## Ostatnie doprecyzowania

- W 4.3 dodano appendix do ćwiczenia z progiem decyzyjnym i przypomnienie metryk klasyfikacji.
- W 4.4 dodano mapę pracy z notebookiem, ręczne przejście przez kilka stumpów, predykcję nowego klienta oraz pokazanie wpływu `learning_rate` i liczby iteracji.
- W 4.5 dodano `customer_id` i `customer_name` jako pola opisowe niewykorzystywane w modelu oraz appendiksy z metrykami, parametrami i interpretacją `feature_importances_`.
