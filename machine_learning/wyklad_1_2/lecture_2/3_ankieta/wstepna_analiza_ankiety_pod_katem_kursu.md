# Wstępna analiza ankiety pod kątem kursu

Liczba odpowiedzi: **25**.

## 1. Najważniejszy obraz grupy

Grupa wygląda na **ogólnie sprawną**, ale **nierówną technicznie**. Najmocniejsze obszary to SQL, ogólna samodzielność pracy, podstawowy Python i część matematyczno-statystyczna. Największa luka jest w praktycznej analizie danych: **NumPy + pandas + przygotowanie danych + groupby/merge**.

## 2. Średnie domenowe

| Domena                                  |   Średnia |   Mediana |   Odchylenie std |   Liczba pytań |
|:----------------------------------------|----------:|----------:|-----------------:|---------------:|
| Dane: NumPy / pandas / wykresy          |     2.937 |         3 |            1.344 |              7 |
| Podstawy ML                             |     3.156 |         3 |            1.46  |              9 |
| Preferencje kursu (bez feedbacku zajęć) |     3.16  |         3 |            1.401 |             13 |
| Matematyka i statystyka                 |     3.927 |         4 |            1.07  |             12 |
| Python                                  |     3.93  |         4 |            1.039 |              8 |
| Samodzielność i gotowość projektowa     |     4.04  |         4 |            0.985 |              7 |
| Feedback po 2 pierwszych spotkaniach    |     4.208 |         4 |            0.845 |              4 |
| SQL / relacyjne myślenie o danych       |     4.39  |         5 |            0.709 |              4 |


### Interpretacja domen

- **Dane: NumPy / pandas / wykresy** to najsłabszy blok. To bardzo mocny sygnał, że pierwszy 6-godzinny blok powinien być warsztatem z workflow danych, a nie z samych podstaw Pythona.
- **Podstawy ML** są na poziomie średnim: studenci kojarzą wiele pojęć, ale jeszcze nie mają stabilnej intuicji praktycznej.
- **SQL** wypada bardzo dobrze. To warto wykorzystać jako most do `groupby`, `merge` i myślenia tabelarycznego w pandas.
- **Samodzielność i gotowość projektowa** są wysokie, więc kurs projektowy ma dobrą bazę wejściową.

## 3. Najsłabsze pytania

|   qid | Pytanie                                                                                                            |   Średnia |   % 4-5 |   % 1-2 |
|------:|:-------------------------------------------------------------------------------------------------------------------|----------:|--------:|--------:|
|    50 | Preferuję zaliczenie w formie pisemnej                                                                             |      1.6  |       8 |      88 |
|    59 | Potrzebuję ścieżki wyrównawczej / dodatkowych zadań podstawowych (np. drzewa, traversal, sortowanie, wyszukiwanie) |      1.92 |       8 |      72 |
|    62 | Stresuje mnie matematyka / statystyka w kontekście tego kursu.                                                     |      2.08 |       8 |      68 |
|    13 | Potrafię łączyć tabele / ramki danych (merge / join) w pandas                                                      |      2.52 |      20 |      56 |
|    37 | Rozumiem, czym jest data leakage                                                                                   |      2.52 |      16 |      48 |
|    64 | Wolę pracować w parze lub małej grupie                                                                             |      2.52 |      24 |      52 |
|    12 | Potrafię użyć groupby / agregacji w pandas                                                                         |      2.56 |      28 |      56 |
|    61 | Chciał(a)bym regularnych krótkich konsultacji / checkpointów do projektów                                          |      2.64 |       8 |      32 |
|    14 | Potrafię wykrywać i obsługiwać braki danych                                                                        |      2.68 |      32 |      48 |
|    60 | Był(a)bym zainteresowany(a) ścieżką advanced / samodzielnie wymyślonym projektem                                   |      2.88 |      28 |      40 |
|    58 | Preferuję zajęcia z samym podawaniem wiedzy np. poprzez slajdy, od takich w których się aktywnie uczestniczy       |      2.92 |      36 |      40 |
|    10 | Rozumiem kształt danych (shape), indeksowanie i slicing w NumPy                                                    |      2.92 |      32 |      36 |


### Co z tego wynika dla kursu

- Największe ryzyko na starcie to nie składnia języka, tylko **operowanie na tabelach i tablicach**.
- Konieczne minimum na początku kursu: `shape`, filtrowanie, `groupby`, `merge`, braki danych, prosty wykres.
- W ML szczególnej uwagi będą wymagały: **funkcja straty**, **data leakage**, **train/validation/test**, **overfitting**.

## 4. Najmocniejsze pytania

|   qid | Pytanie                                                                                                                                                             |   Średnia |   % 4-5 |   % 5 |
|------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------:|--------:|------:|
|    45 | Potrafię czytać anglojęzyczną dokumentację techniczną                                                                                                               |      4.72 |     100 |    72 |
|    51 | Preferuję zaliczenie w formie 2–3 projektów                                                                                                                         |      4.68 |      96 |    76 |
|    16 | Rozumiem składnię SELECT / WHERE / ORDER BY                                                                                                                         |      4.6  |      92 |    68 |
|    17 | Rozumiem GROUP BY i podstawowe agregacje SQL                                                                                                                        |      4.52 |      92 |    60 |
|    27 | Rozumiem różnicę między funkcją liniową a kwadratową                                                                                                                |      4.52 |      88 |    64 |
|    54 | Jak Pani/Panu odpowiada forma wczorajszych  zajęć - początkowe wprowadzenie, potem praca samodzielna (5 - bardzo odpowiada, 1 - nie odpowiada, 0 - nie było mnie )? |      4.5  |      88 |    56 |
|    29 | Potrafię policzyć proste pochodne, np. x, x^2, (x-1)^3                                                                                                              |      4.44 |      88 |    56 |
|    20 | Rozumiem średnią, medianę, odchylenie standardowe i wariancję                                                                                                       |      4.36 |      84 |    52 |
|    48 | Zależy mi na realnym nauczeniu się materiału                                                                                                                        |      4.36 |      88 |    52 |
|    28 | Rozumiem różnicę między funkcją liniową i kwadratową a wielomianami wyższych stopni                                                                                 |      4.36 |      84 |    60 |
|     5 | Potrafię pisać funkcje i używać parametrów / wartości zwracanych                                                                                                    |      4.28 |      84 |    48 |
|     7 | Potrafię korzystać z dokumentacji biblioteki, aby znaleźć potrzebną funkcję                                                                                         |      4.28 |      80 |    52 |


Mocne strony grupy sugerują, że nie trzeba długo powtarzać ogólnego Pythona ani elementarnych statystyk. Lepiej od razu przejść do **analizy danych w praktyce**.

## 5. Preferencje dotyczące kursu

| Wskaźnik                                           |   Średnia |   % 4-5 |   % 1-2 |
|:---------------------------------------------------|----------:|--------:|--------:|
| Zaliczenie projektowe (2-3 projekty)               |      4.68 |      96 |       4 |
| Realne nauczenie się materiału                     |      4.36 |      88 |       4 |
| Sprawne zaliczenie kursu                           |      4.12 |      72 |       4 |
| Preferencja pracy indywidualnej                    |      4    |      68 |      12 |
| Więcej praktyki / kodowania / analizy danych       |      3.96 |      68 |       0 |
| Więcej teorii i wyjaśnień                          |      3.4  |      32 |       8 |
| Preferencja slajdów zamiast aktywnego uczestnictwa |      2.92 |      36 |      40 |
| Zainteresowanie ścieżką advanced                   |      2.88 |      28 |      40 |
| Potrzeba regularnych checkpointów                  |      2.64 |       8 |      32 |
| Preferencja pracy w parze / grupie                 |      2.52 |      24 |      52 |
| Stres mat/stat w kursie                            |      2.08 |       8 |      68 |
| Potrzeba ścieżki wyrównawczej                      |      1.92 |       8 |      72 |
| Zaliczenie pisemne                                 |      1.6  |       8 |      88 |


### Wnioski organizacyjne

- Studenci **bardzo wyraźnie preferują projekty** zamiast zaliczenia pisemnego.
- Wyżej stoi **realne nauczenie się materiału** niż sama forma zaliczenia, ale sprawne zaliczenie też jest dla nich ważne.
- Grupa jest raczej **pro-praktyczna**: więcej praktyki niż teorii.
- Wyraźniej wolą pracę **indywidualną** niż pracę w parze / małej grupie.
- Na poziomie deklaracji mało osób prosi o ścieżkę wyrównawczą, ale wyniki w pandas/NumPy pokazują, że **granularne zadania podstawowe** i tak będą potrzebne.

## 6. Odbiór dwóch pierwszych spotkań

| Wskaźnik                    |   Średnia (bez 0) |   % 5 (bez 0) |   % 4 (bez 0) |   Frekwencja % |
|:----------------------------|------------------:|--------------:|--------------:|---------------:|
| Forma wczorajszych zajęć    |             4.5   |            56 |            32 |             96 |
| Zrozumienie po wczorajszych |             4.167 |            32 |            52 |             96 |
| Forma dzisiejszych hands-on |             4.083 |            36 |            44 |             96 |
| Zrozumienie po dzisiejszych |             4.083 |            40 |            28 |             96 |


Widać ciekawy efekt dydaktyczny: **wczorajsza forma zajęć** była oceniona odrobinę wyżej niż dzisiejsza forma hands-on, a przy formie wczorajszej było też więcej ocen maksymalnych. Z kolei **zrozumienie** obu spotkań jest podobnie wysokie. To sugeruje, że druga forma mogła być mniej komfortowa, ale niekoniecznie mniej skuteczna.

## 7. Wstępna segmentacja grupy (heurystyczna)

Na potrzeby planowania kursu można roboczo myśleć o grupie jako o: **11 osobach wymagających wsparcia**, **11 osobach w ścieżce standardowej** i **3 osobach potencjalnie gotowych do ścieżki advanced**.

To nie jest klasyfikacja formalna, tylko dydaktyczna heurystyka. Jej sens praktyczny jest prosty: na zajęciach warto dawać zadania warstwowe: podstawowe, standardowe i rozszerzone.

## 8. Co zrobić na najbliższym 6-godzinnym bloku

Najbardziej opłacalny plan:
1. **20-30 min**: środowisko pracy i workflow (Jupyter/Colab, czytanie błędów, dokumentacja).
2. **60-75 min**: NumPy jako model myślenia o danych (`shape`, slicing, maski, agregacje).
3. **75-90 min**: pandas I: filtrowanie, wybór danych, `isna`, `fillna`, proste statystyki.
4. **75-90 min**: pandas II: `groupby` i `merge` przez analogie do SQL.
5. **45-60 min**: matplotlib minimum: histogram, line, scatter, bar.
6. **60-90 min**: jeden spójny mini-case od pytania do wykresu i krótkich wniosków.

Najważniejsza zasada: **nie prowadzić tego jako wykładu o Pythonie**, tylko jako warsztat workflow danych.
