# Rozpiska przygotowania i prowadzenia wykładu z analizy danych w Pythonie

## Cel główny

Nie prowadzisz tych zajęć jako przeglądu `14.zip`, tylko jako **jeden workflow powtórzony na trzech coraz bardziej realnych case'ach**:

1. **Student data** — mały, kontrolowany case do rozgrzewki.
2. **Maratończycy** — case do `groupby`, `pivot_table`, filtrów, agregacji i wykresów.
3. **Ankieta studentów** — case najbardziej realny i motywujący, spięty z Twoim kursem.

Oś całego wykładu:

**pytanie → dane → czyszczenie → wybór/filtr → agregacja → wizualizacja → interpretacja**

To ma być centralny model, do którego wracasz cały czas.

---

## Co ma być gotowe na koniec przygotowań

Na koniec półtora dnia masz mieć tylko trzy rzeczy:

1. **`master.ipynb`** dla prowadzącego.
2. **jedną kartkę planu mówienia** z hasłami do każdego bloku.
3. **notebook ćwiczeniowy / miejsca na zadania** dla studentów albo sekcje TODO w `master.ipynb`.

Nie przygotowujesz pełnego „wszystkiego”, tylko stabilny szkielet.

---

## Materiały źródłowe, które faktycznie wykorzystujesz

### Główne źródła
- `wyklad_2/analiza1/wyklad_analiza_1_vscode_tut.ipynb`
- `wyklad_2/analiza_maratonczycy/maratonczycy_groupby_pivot_demo.ipynb`
- `wyklad_2/wyklad_2_iteracja2/00_analiza_ankiety_i_plan_wykladu.ipynb`

### Wsparcie / wprawki
- `wyklad_2/wyklad_2_iteracja2/01_jupyter_python_wprawki.ipynb`
- `wyklad_2/wyklad_2_iteracja2/02_numpy_wprawki.ipynb`
- `wyklad_2/wyklad_2_iteracja2/03_pandas_wprawki.ipynb`
- `wyklad_2/wyklad_2_iteracja2/04_matplotlib_wprawki.ipynb`

### Z `14.zip` bierz tylko wybrane rzeczy
- help i dokumentacja
- debugging
- NumPy: typy, tablice, agregacje, maski
- pandas: selection, missing values, merge, grouping, pivot tables, strings
- matplotlib: line, scatter, histogram, bar

Nie robisz teraz:
- time series
- hierarchical indexing
- zaawansowanego matplotlib
- performance `eval/query`
- rzeczy pobocznych, które nie wspierają głównego workflow

---

## Dwie poprawki techniczne, które zrób od razu

### 1. Bug w `wyklad_analiza_1_vscode_tut.ipynb`
Masz tam niespójność `passes` vs `passed`.

Powinno być spójnie, np.:

```python
passed = pd.Series(df_students["Grade"] >= 60, name="Pass")
df_students = pd.concat([df_students, passed], axis=1)
```

### 2. Stara składnia wyboru wielu kolumn po `groupby`
Zamiast:

```python
df_students.groupby(df_students.Passed)['StudyHours','Grade'].mean()
```

daj:

```python
df_students.groupby("Passed")[["StudyHours", "Grade"]].mean()
```

### 3. Nie używaj `wget` na żywo, jeśli nie musisz
Dane trzymaj lokalnie w `data/` albo generuj z list bez pobierania z internetu.

---

## Rozpiska przygotowań na półtora dnia

## Dzień 1, blok 1 — 60 do 90 minut
### Ustal oś wykładu

Na jednej kartce wypisz:

- 3 case'y
- 8 kroków workflow
- 6 obowiązkowych narzędzi:
  - `read_csv`
  - filtrowanie maską
  - `isna` / `fillna` / `dropna`
  - `groupby`
  - `pivot_table`
  - prosty wykres
- 4 pułapki:
  - `NaN`
  - zła granularność przy `merge`
  - `groupby` vs `pivot_table`
  - stringi i parsowanie
- 3 rzeczy do wycięcia, jeśli zabraknie czasu

**Efekt tego bloku:** jedna kartka sterująca całym przygotowaniem.

---

## Dzień 1, blok 2 — 90 do 120 minut
### Sklej `master.ipynb`

Łączysz wszystko w jeden notebook prowadzącego w tej kolejności:

1. Intro: po co analiza danych i co mówi ankieta.
2. Case 1: student data.
3. Krótka wprawka / mini-zadanie.
4. Case 2: maratończycy.
5. Krótka wprawka / mini-zadanie.
6. Case 3: ankieta studentów.
7. Pułapki i ciekawostki z `14.zip`.
8. Zadanie końcowe i podsumowanie.

**Zasada:** jeden notebook, zero skakania między pięcioma plikami podczas prowadzenia.

---

## Dzień 1, blok 3 — 60 do 90 minut
### Oczyść i skróć materiał

Usuń albo schowaj:
- puste komórki
- duplikaty
- martwy kod
- rzeczy, których nie pokażesz na pewno
- pobieranie plików z internetu
- dygresje, które nie wzmacniają osi wykładu

Zostaw tylko komórki, które:
- coś obliczają,
- pokazują ważny wzorzec,
- prowadzą do interpretacji.

**Efekt:** notebook jest krótki i prowadzi po jednej osi.

---

## Dzień 1, blok 4 — 60 minut
### Pierwsze przejście na głos

Przejdź od początku do końca:
- intro
- case 1
- case 2
- case 3

Nie poprawiaj jeszcze wszystkiego po drodze. Zaznacz tylko:
- gdzie się plączesz,
- gdzie brakuje mostu pośredniego,
- gdzie wchodzisz za głęboko,
- gdzie tempo siada.

**Efekt:** wiesz, co Cię poznawczo blokuje.

---

## Dzień 2, blok 1 — 60 do 90 minut
### Stabilizacja techniczna

Popraw:
- importy
- ścieżki do plików
- wykresy
- stare składnie pandas
- błędy w kodzie
- nazwy kolumn
- brakujące `show()`

Zrób lokalną strukturę:

```text
master.ipynb
data/
    Ankieta_ML.csv
    marathon-data.csv   # albo Twój właściwy plik
plots/
    01_domain_summary.png
    02_top_dispersion.png
    03_key_contrasts.png
    04_feedback_counts.png
```

**Efekt:** notebook odpala się bez improwizacji.

---

## Dzień 2, blok 2 — 45 do 60 minut
### Plan mówienia

Do każdego większego bloku dopisz tylko trzy linie:

- **Wniosek:** co chcę, żeby zapamiętali.
- **Mechanizm:** jakiej operacji użyję.
- **Przykład:** na jakich danych to pokażę.

To bardzo ważne dla Twojego stylu, bo chroni Cię przed wrzucaniem całego stanu wewnętrznego naraz.

---

## Dzień 2, blok 3 — 30 do 45 minut
### Plan awaryjny

Zapisz od razu, co tniesz, jeśli czasu zabraknie.

### Tnij w tej kolejności
1. pełny live coding ankiety
2. dygresje statystyczne z case 1
3. ozdobniejsze wykresy
4. bonusy z `14.zip`

### Nie tnij
- pierwszego pełnego workflow
- `groupby`
- `pivot_table`
- jednego wykresu robionego od zera
- końcowego mini-zadania

---

## Proponowany rozkład 6 godzin wykładu

## Blok 1 — 20 do 25 min
### Motywacja: po co nam dziś Python do analizy danych

Pokazujesz 3–4 gotowe wykresy z ankiety i mówisz:
- co już widać,
- po co nam analiza danych,
- jaka będzie oś wykładu.

Nie kodujesz jeszcze.

---

## Blok 2 — 75 do 90 min
### Case 1: student data

Cel:
- wejście w styl pracy na danych
- przejście przez `numpy` → `pandas`
- filtrowanie, braki danych, `groupby`, prosty wykres

Muszą zapamiętać:
- dane nie są „listą funkcji”, tylko obiektem do zadawania pytań
- każde narzędzie ma odpowiadać na konkretne pytanie

---

## Blok 3 — 60 do 70 min
### Case 2: maratończycy

Cel:
- `groupby`
- `pivot_table`
- prosta interpretacja wyników
- połączenie z intuicją SQL

Tu możesz powiedzieć:
- `WHERE` ≈ maska
- `GROUP BY` ≈ `groupby`
- `JOIN` ≈ `merge`

---

## Blok 4 — 60 do 75 min
### Case 3: ankieta studentów

Cel:
- zastosować ten sam workflow do realnych danych grupy
- nie robić pełnej analizy wszystkiego
- pokazać 1–2 operacje live i kilka gotowych wyników

Na żywo:
- wczytanie,
- konwersja na liczby,
- proste agregaty,
- jeden wykres,
- jedna interpretacja.

---

## Blok 5 — 35 do 45 min
### Pułapki i szczególne przypadki

Wybierz tylko 4:
- `None` vs `NaN`
- zła granularność przy `merge`
- `groupby` vs `pivot_table`
- stringi / parsowanie

To ma być blok „na co uważać”, a nie nowy wykład.

---

## Blok 6 — 30 do 40 min
### Mini-zadanie studentów

Trzy poziomy:
- podstawowy: filtr + średnia + wykres
- standardowy: `groupby` albo `pivot_table`
- rozszerzony: `merge` albo porównanie dwóch grup

Oddają:
- jedną komórkę kodu,
- jedno zdanie interpretacji.

---

## Jak prowadzić zgodnie z Twoim stylem, ale czytelnie dla nich

Trzymaj stały porządek:

**co chcemy wiedzieć → jakie mamy dane → jakiej operacji użyjemy → co z tego wynika**

Nie mów:
> „teraz pokażę `groupby`”.

Mów:
> „chcemy wiedzieć, która grupa ma średnio lepszy wynik, więc musimy pogrupować dane i policzyć agregat”.

To jest w pełni w Twoim stylu, ale linearyzuje go dla studentów.

---

## Ostatnia checklista przed wejściem na salę

- notebook uruchamia się od góry do dołu
- wszystkie ścieżki są lokalne
- nie ma `wget`
- masz zapisany plan awaryjny cięć
- masz 3–4 gotowe wykresy na start
- wiesz, gdzie robisz przerwę
- masz zaznaczone komórki:
  - live
  - opcjonalne
  - do pokazania jako gotowe

---

## Najkrótsza wersja strategii

Nie uczysz dziś „całego Pythona do danych”.  
Uczysz **jednego sposobu pracy na danych**, który studenci zobaczą trzy razy:

1. na małym case'ie,
2. na bardziej realnym case'ie,
3. na własnych danych.

To będzie dużo lepsze dydaktycznie i dużo bardziej zgodne z Twoim stylem niż przechodzenie liniowo przez `14.zip`.
