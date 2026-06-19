
# Wykład 1 — iteracja 2  
## Analiza ankiety, plan zajęć i oś pracy z notebookami

Ten notebook ma być **główną osią wykładu** i punktem wejścia do dalszych mini-notebooków.

## Najważniejsza decyzja dydaktyczna

Na tym etapie **nie zaczynamy od bardziej zaawansowanych metod ML**.  
Najpierw skupiamy się na **praktycznym zastosowaniu podstaw**:

- Jupyter / Colab,
- Python jako narzędzie pracy,
- NumPy: `shape`, tablice, indeksowanie, maski,
- pandas: filtrowanie, braki danych, `groupby`, `merge`, `pivot_table`,
- matplotlib: proste wykresy.

Dopiero później, na bazie tej samej ankiety lub zbioru maratońskiego, można wejść w:
- bardziej systematyczne porównywanie rozkładów,
- korelacje i podobieństwa pytań,
- PCA / clustering / prostą analizę ML-ową.

To podejście lepiej pasuje do wyników ankiety: grupa ma już podstawy Python/SQL, ale największa luka jest w **praktycznej analizie danych**.

## Co jest w tym folderze

- `00_analiza_ankiety_i_plan_wykladu.ipynb` — ten notebook,
- `01_jupyter_python_wprawki.ipynb` — krótkie wprawki z Jupytera i czystego Pythona,
- `02_numpy_wprawki.ipynb` — NumPy pod potrzeby ankiety,
- `03_pandas_wprawki.ipynb` — pandas pod potrzeby ankiety,
- `04_matplotlib_wprawki.ipynb` — matplotlib pod potrzeby ankiety,
- zewnetrzne linki do upstreamowych notebookow Jake'a VanderPlasa zamiast lokalnej kopii,
- `../data/Ankieta_ML.csv` — dane wejściowe,
- `plots/` i `tables/` — wykresy i tabele generowane przez ten notebook.

## Proponowana oś wykładu

1. **Ręczna analiza ankiety**: co widać „na oko” i jakie mamy hipotezy.
2. **Deskryptywna analiza w pandas**: średnie, rozrzut, kontrasty pytań.
3. **Ćwiczenie narzędziowe**: Jupyter + Python + NumPy + pandas + matplotlib.
4. **Powrót do ankiety**: zastosowanie poznanych narzędzi do własnych danych grupy.
5. **Maratończycy** dopiero w drugiej części lub na kolejnym spotkaniu, jako płynniejszy case do `groupby`, `pivot_table` i wizualizacji.

## Lista notebooków VanderPlasa, które warto włączyć

### IPython / Jupyter
- [01.01 Help and Documentation](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks_v1/01.01-Help-And-Documentation.ipynb)
- [01.06 Errors and Debugging](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks_v1/01.06-Errors-and-Debugging.ipynb)

### NumPy
- [02.01 Understanding Data Types](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks_v1/02.01-Understanding-Data-Types.ipynb)
- [02.02 The Basics of NumPy Arrays](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks_v1/02.02-The-Basics-Of-NumPy-Arrays.ipynb)
- [02.04 Computation on arrays: aggregates](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks_v1/02.04-Computation-on-arrays-aggregates.ipynb)
- [02.06 Boolean Arrays and Masks](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks_v1/02.06-Boolean-Arrays-and-Masks.ipynb)

### pandas
- [03.02 Data Indexing and Selection](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks_v1/03.02-Data-Indexing-and-Selection.ipynb)
- [03.04 Missing Values](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks_v1/03.04-Missing-Values.ipynb)
- [03.07 Merge and Join](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks_v1/03.07-Merge-and-Join.ipynb)
- [03.08 Aggregation and Grouping](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks_v1/03.08-Aggregation-and-Grouping.ipynb)
- [03.09 Pivot Tables](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks_v1/03.09-Pivot-Tables.ipynb)
- [03.10 Working With Strings](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks_v1/03.10-Working-With-Strings.ipynb)

### matplotlib
- [04.01 Simple Line Plots](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks_v1/04.01-Simple-Line-Plots.ipynb)
- [04.02 Simple Scatter Plots](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks_v1/04.02-Simple-Scatter-Plots.ipynb)
- [04.05 Histograms and Binnings](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks_v1/04.05-Histograms-and-Binnings.ipynb)

### Jak to scalać
Najlepszy tryb to nie liniowe „czytanie” całych notebooków, tylko:
1. pokazujesz **wybrany fragment** VanderPlasa,
2. od razu przechodzicie do **lokalnej wprawki** z tego samego tematu,
3. wracacie do **analizy ankiety** i stosujecie narzędzie na realnych danych grupy.



## Szybkie podsumowanie tego, co już widać

### Najmocniejsze domeny
- SQL / relacyjne bazy,
- ogólny Python,
- matematyka i statystyka na poziomie podstawowym,
- organizacja pracy i czytanie dokumentacji.

### Najsłabsza domena
- NumPy / pandas / wizualizacja.

### Najbardziej praktyczny wniosek
To nie jest grupa, której trzeba robić pełny kurs „Python od zera”.  
To jest grupa, której trzeba pomóc **przejść od składni do pracy na danych**.



## Ręczna analiza ankiety — wersja dopracowana

Ta część przepisuje i porządkuje ręczne uwagi do ankiety.  
Założenie jest takie:

- najpierw patrzymy na **poziom średni**,
- potem na **rozrzut odpowiedzi**,
- potem na **kontrasty pytań pokrewnych**,
- a na końcu zamieniamy to w **decyzje dydaktyczne**.

To znaczy: sama średnia nie wystarczy.  
Pytanie może mieć średnią „średnią”, ale bardzo duży rozrzut, a to oznacza, że grupa jest **nierówna** i trzeba przygotować zadania warstwowe.

### Jak czytać tę ankietę
- **średnia wysoka + mały rozrzut**: temat raczej bezpieczny, wystarczy krótkie przypomnienie,
- **średnia wysoka + duży rozrzut**: część grupy umie, część nie, warto dać warianty zadań,
- **średnia niska + mały rozrzut**: temat ogólnie słaby, trzeba go ćwiczyć od podstaw,
- **średnia niska + duży rozrzut**: temat jest słaby i nierówny, trzeba ćwiczyć + dać ścieżkę support i opcję advanced.

---

## 1. Python / programowanie (Q1–Q8)

**Q1. Jupyter / Colab**  
Wynik jest niższy niż w zwykłych podstawach Pythona i ma duży rozrzut. To jest sygnał, że warto zacząć od krótkiego wspólnego wejścia do środowiska.  
**Wniosek dydaktyczny:** zrobić prosty wspólny start w Colabie lub lokalnym Jupyterze. Nie polecam jednego wspólnego użytkownika na jednej maszynie, bo to zbyt łatwo wysypać.

**Q2. Typy danych w Pythonie**  
To wygląda dobrze.  
**Wniosek:** nie robić z tego dużego wykładu, tylko krótką rozgrzewkę.

**Q3. Stringi / `split`**  
Też wygląda dobrze.  
**Wniosek:** dobra rzecz na szybkie wejście i oswojenie notebooka.

**Q4. OOP**  
Średnio jest nieźle, ale rozrzut jest zauważalny.  
**Wniosek:** krótka wprawka z klasami ma sens, ale nie jako główna oś dnia.

**Q5. Funkcje**  
Wysoko i dość stabilnie.  
**Wniosek:** przypomnieć tylko przy okazji ćwiczeń.

**Q6. Debugowanie**  
Dość dobrze, ale nie idealnie.  
**Wniosek:** 5 minut na czytanie błędów i proste debugowanie bardzo się opłaci.

**Q7. Korzystanie z dokumentacji**  
Bardzo dobry sygnał.  
**Wniosek:** można bez stresu odsyłać studentów do helpa i dokumentacji.

**Q8. Różnica między pętlą a podejściem wektorowym / kolekcjami**  
Tu widać większą niepewność niż w czystych podstawach Pythona.  
**Wniosek:** koniecznie pokazać bardzo prosty kontrast:
- pętla po liście,
- to samo przez tablicę NumPy / maskę / agregację.

---

## 2. NumPy / pandas / wizualizacja (Q9–Q15)

To jest najsłabszy blok całej ankiety i najważniejszy praktycznie.

**Q9. Podstawowe operacje na tablicy NumPy**  
Nie jest tragicznie, ale dużo słabiej niż podstawy Pythona.  
**Wniosek:** NumPy trzeba robić od podstaw, ale krótko i konkretnie.

**Q10. `shape`, indeksowanie i slicing w NumPy**  
To jest jeden z pierwszych bardzo wyraźnie słabych punktów.  
**Wniosek:** obowiązkowo ćwiczenia z wymiarowości danych, `shape`, 1D vs 2D, slicing i maskami.

**Q11. Filtrowanie i wybieranie danych w pandas**  
Widać wyraźny zjazd względem Pythona.  
**Wniosek:** filtrowanie w DataFrame musi być jednym z głównych ćwiczeń.

**Q12. `groupby` w pandas**  
To jest bardzo słaby punkt.  
**Wniosek:** potraktować `groupby` jako jeden z filarów tego wykładu.

**Q13. `merge` / `join` w pandas**  
Jeszcze słabiej niż `groupby`.  
**Wniosek:** bardzo mocno ćwiczyć `merge` i łączyć to z przypomnieniem kluczy / granularności.

**Q14. Braki danych**  
Raczej równomiernie słabo.  
**Wniosek:** studenci mogą nie mieć automatyzmu w `NaN`, `isna`, `fillna`, `dropna`; trzeba to przećwiczyć.

**Q15. Prosty wykres**  
To nie jest pełna katastrofa, ale rozrzut jest bardzo duży. Część studentów umie, część nie.  
**Wniosek:** nie zakładać, że „wszyscy umieją zrobić wykres”, tylko pokazać 3–4 najprostsze przypadki od zera.

**Najmocniejszy wniosek z bloku Q9–Q15**  
To nie jest problem „Python od zera”. To jest problem **przejścia do analizy danych**.  
Właśnie dlatego ten wykład powinien być oparty na:
`shape -> filtrowanie -> braki danych -> groupby -> merge -> wykres`.

---

## 3. SQL / relacyjne bazy (Q16–Q19)

**Q16. SELECT / WHERE / ORDER BY**  
Bardzo wysoko.

**Q17. SQL GROUP BY**  
Bardzo wysoko.

**Q18. SQL JOIN**  
Wysoko.

**Q19. Klucze, klucze obce i granularność**  
Trochę niżej niż czysty SQL operacyjny.

**Wniosek zbiorczy:**  
Studenci deklarują znajomość SQL, ale możliwe, że bardziej „operacyjnie” niż modelowo.  
Najlepszy ruch dydaktyczny to nie robić wielkiej powtórki z SQL, tylko użyć SQL jako pomostu do pandas:

- `SELECT` -> wybór kolumn,
- `WHERE` -> maska,
- `GROUP BY` -> `groupby`,
- `JOIN` -> `merge`,
- klucz / granularność -> warunki poprawnego łączenia tabel.

To jest jeden z najcenniejszych kontrastów całej ankiety:  
**Q12 vs Q17** i **Q13 vs Q18**.

---

## 4. Matematyka i statystyka (Q20–Q31)

Tutaj wynik jest bardziej zniuansowany niż „umieją / nie umieją”.

**Q20. Średnia, mediana, odchylenie, wariancja**  
Wysoko. To jest bezpieczny obszar.

**Q21. Percentyl / kwartyl / rozkład**  
Wyraźnie gorzej niż Q20.  
**Wniosek:** trzeba przypomnieć rozkład i kwantyle, najlepiej wizualnie.

**Q22. Korelacja i brak przyczynowości**  
Dość wysoko.

**Q23. Kowariancja**  
Wyraźnie słabiej niż korelacja.  
**Wniosek:** można to pokazać krótko jako kontrast pojęciowy, ale nie robić z tego długiego bloku.

**Q24. Prawdopodobieństwo warunkowe**  
Średnio.  
**Wniosek:** raczej krótka intuicja niż formalny rachunek.

**Q25. Próbkowanie i błąd estymacji**  
Niżej i mniej pewnie.  
**Wniosek:** temat warto pokazać intuicyjnie na przykładzie, nie przez definicje.

**Q26. Intuicja funkcji liniowej i nachylenia**  
Nieźle, ale słabiej niż „policzyć pochodną”.  
**Wniosek:** Twoja intuicja jest dobra — część studentów prawdopodobnie umie liczyć ze wzorów, ale słabiej rozumie geometrię.

**Q27. Różnica między funkcją liniową a kwadratową**  
Bardzo dobrze.

**Q28. Różnica między liniową / kwadratową a wielomianami wyższych stopni**  
Też dobrze.

**Q29. Liczenie prostych pochodnych**  
Bardzo wysoko.

**Q30. Pochodna jako miara zmiany**  
Niżej niż Q29.  
**Wniosek:** bardzo dobry materiał do GeoGebry: liczenie jest, intuicja geometryczna jest słabsza.

**Q31. Wektory i macierze**  
Dość dobrze, ale nie perfekcyjnie.  
**Wniosek:** warto dać 5–10 minut wizualnego przypomnienia.

**Najmocniejszy wniosek z matematyki/statystyki**  
Nie widać tu katastrofy, ale widać różnicę między:
- **rachunkiem / rozpoznaniem wzoru**, a
- **intuicją geometryczną i statystyczną**.

To bardzo dobrze pasuje do Twojego pomysłu na krótkie wprawki w GeoGebrze.

---

## 5. ML podstawy + sprawność algorytmiczna (Q32–Q42)

Tu widać dokładnie to, czego można było się spodziewać:  
grupa **coś kojarzy**, ale rozkłady są nierówne i część pojęć jest naprawdę słaba.

**Q32. Funkcja straty**  
Słabo i z dużym rozrzutem.  
**Wniosek:** trzeba wytłumaczyć od zera, intuicyjnie.

**Q33. Nadzorowane / nienadzorowane**  
Średnio, z dużym rozrzutem.  
**Wniosek:** część studentów zna, część nie — nadaje się na pierwszy prosty kontrast.

**Q34. Feature / target / etykieta**  
Słabiej niż można by chcieć.  
**Wniosek:** po wyjaśnieniu powinno pójść szybko, ale nie wolno zakładać, że to oczywiste.

**Q35. Train / validation / test**  
Średnio.

**Q36. Overfitting / underfitting**  
Średnio, ale z bardzo dużym rozrzutem.  
**Wniosek:** jest grupa, która to zna, i grupa, która prawie nie zna.

**Q37. Data leakage**  
Jeden z najgorszych wyników w całej części ML.  
**Wniosek:** koniecznie wytłumaczyć na przykładzie.

**Q38. Regresja vs klasyfikacja**  
Rozrzut bardzo duży.  
**Wniosek:** temat trzeba wyłożyć prosto i wizualnie.

**Q39. Dobór metryki zależy od problemu**  
Średnio, ale tu część studentów może zgadywać intuicyjnie.

**Q40. Intuicja modeli drzewiastych**  
Raczej słabo i nierówno.  
**Wniosek:** to będzie temat dopiero później.

**Q41. BFS / DFS**  
Średnio.  
**Wniosek:** nie robiłbym z tego teraz dużego tematu; jeśli wróci, to jako krótki bonus lub support.

**Q42. merge-/quicksort**  
Dość dobrze, ale to nie jest teraz krytyczna oś wykładu.

**Najmocniejszy wniosek z ML**  
Na tym etapie nie ma sensu zaczynać od „bardziej zaawansowanej analizy ML ankiety”.  
Najpierw trzeba zbudować warsztat danych i dopiero potem wrócić do PCA / clusteringu / szerszej eksploracji.

---

## 6. Praca, preferencje i feedback po pierwszych zajęciach (Q43–Q64)

**Q43. Praca z niedookreślonym problemem**  
Dość dobrze, ale bez przesadnej pewności.

**Q44. Planowanie pracy na kilka dni / tygodni**  
Wysoko.

**Q45. Czytanie dokumentacji angielskiej**  
Bardzo wysoko. To świetny sygnał.

**Q46. Prezentowanie wyniku swojej pracy**  
Nieźle, ale z rozrzutem.

**Q47. Współpraca z innymi**  
Wysoko.

**Q48 vs Q49. Nauka materiału vs sprawne zaliczenie**  
Oba wyniki są wysokie. To nie jest sprzeczność; oznacza raczej, że grupa chce się nauczyć, ale też nie chce utrudnionej organizacji kursu.

**Q50 vs Q51. Pisemne vs projekty**  
To jest bardzo mocny i łatwy do pokazania kontrast: projekty zdecydowanie wygrywają z formą pisemną.

**Q52 vs Q53. Więcej teorii vs więcej praktyki**  
Praktyka wygrywa.

**Q54 vs Q56. Forma wczoraj vs forma dziś**  
Wczorajsza forma została oceniona wyżej.

**Q55 vs Q57. Zrozumienie wczoraj vs zrozumienie dziś**  
Różnica jest mniejsza niż w samym „podobało się / nie podobało się”.  
**Wniosek:** dzisiejsza forma mogła być trochę mniej komfortowa, ale niekoniecznie mniej skuteczna.

**Q58. Slajdy vs aktywny udział**  
Nie widać mocnego poparcia dla czysto slajdowego formatu.  
**Wniosek:** warto utrzymać wykład z małymi przerwami na działanie.

**Q59. Ścieżka wyrównawcza**  
Studenci deklaratywnie raczej jej nie chcą.  
**Ale:** wyniki z pandas/NumPy sugerują, że zadania support i tak są potrzebne. Lepiej więc nie nazywać tego „ścieżką wyrównawczą”, tylko po prostu dać poziom podstawowy / standard / rozszerzenie.

**Q60. Ścieżka advanced**  
Jest pewna grupa zainteresowanych, ale nie większość.

**Q61. Regularne checkpointy / konsultacje**  
Raczej umiarkowane zainteresowanie.

**Q62. Stres matematyką / statystyką**  
Raczej niski.

**Q63 vs Q64. Indywidualnie vs w parze / grupie**  
Silniejsza jest preferencja pracy indywidualnej.  
**Wniosek:** główny tryb zajęć może być indywidualny, a opcjonalny projekt grupowy najlepiej zostawić na koniec lub dla chętnych.

---

## 7. Najważniejsze kontrasty, które warto pokazać studentom na wykładzie

Jeśli chcesz zrobić analizę „z ręki”, a potem uzasadnić ją prostymi statystykami i wykresami, to najciekawsze są te pary:

1. **Q12 vs Q17** — pandas `groupby` kontra SQL `GROUP BY`  
2. **Q13 vs Q18** — pandas `merge` kontra SQL `JOIN`  
3. **Q26 vs Q29 vs Q30** — nachylenie funkcji, liczenie pochodnych, intuicja pochodnej  
4. **Q20 vs Q21** — statystyki opisowe kontra kwartyle / rozkład  
5. **Q22 vs Q23** — korelacja kontra kowariancja  
6. **Q50 vs Q51** — pisemne kontra projekty  
7. **Q52 vs Q53** — teoria kontra praktyka  
8. **Q54 vs Q56** — odbiór dwóch form zajęć  
9. **Q55 vs Q57** — zrozumienie dwóch form zajęć  
10. **Q63 vs Q64** — praca indywidualna kontra praca w parze / grupie  

To są miejsca, w których sama średnia nie wystarcza — warto porównywać także **rozklady odpowiedzi**.

---

## 8. Decyzje dydaktyczne wynikające z ankiety

### Co ćwiczyć na pewno
- Jupyter / Colab,
- `shape`, indeksowanie i slicing w NumPy,
- filtrowanie w pandas,
- `groupby`,
- `merge`,
- braki danych,
- prosty matplotlib,
- różnica między liczeniem pochodnej a intuicją pochodnej.

### Co tylko krótko przypomnieć
- typy danych,
- stringi,
- funkcje,
- dokumentacja,
- SQL operacyjny.

### Co zostawić na później
- głębsze wchodzenie w BFS/DFS,
- sortowania,
- drzewa decyzyjne jako model,
- bardziej zaawansowane metody ML,
- pełny blok gier w pygame.

### Co można zostawić jako lekki przerywnik
- krótka wprawka OOP z klasą i metodami,
- ewentualnie bardzo prosty bonus obiektowy / growy, ale tylko jeśli zostanie czas.



## Plan zajęć — iteracja 2

Poniżej wersja planu, która scala:
- analizę ankiety,
- wybrane notebooki VanderPlasa,
- lokalne mini-wprawki,
- Twoje luźne propozycje z wcześniejszych notatek.

### Rdzeń decyzji
Na tym spotkaniu **stawiamy na praktyczne użycie podstaw**.  
Zaawansowaną analizę ML-ową ankiety zostawiamy jako końcówkę albo osobny kolejny krok.

---

### Blok A. Otwarcie i cel wykładu (10–15 min)
- po co analizujemy ankietę,
- jak czytać rozkład odpowiedzi,
- czym różni się średnia od rozrzutu,
- jakie pytania chcemy sobie zadać o tej grupie.

---

### Blok B. Ankieta — analiza ręczna i deskryptywna (60–90 min)
1. najpierw komentarz „na oko”,
2. potem proste statystyki w pandas,
3. potem kontrasty pytań pokrewnych.

**Cel dydaktyczny:**  
pokazać, że analiza danych zaczyna się od hipotez, a dopiero potem wchodzą narzędzia.

**Najważniejsze kontrasty do pokazania:**
- pandas `groupby` vs SQL `GROUP BY`,
- pandas `merge` vs SQL `JOIN`,
- liczenie pochodnych vs intuicja pochodnej,
- projekty vs zaliczenie pisemne,
- teoria vs praktyka,
- forma zajęć wczoraj vs dziś.

---

### Blok C. Wybrane cegły z VanderPlasa + lokalne wprawki (około 2.5–3 h łącznie)

#### C1. Jupyter / IPython (20–30 min)
Najpierw krótko:
- [01.01 Help and Documentation](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks_v1/01.01-Help-And-Documentation.ipynb)
- [01.06 Errors and Debugging](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks_v1/01.06-Errors-and-Debugging.ipynb)

Potem lokalnie:
- [01_jupyter_python_wprawki.ipynb](01_jupyter_python_wprawki.ipynb)

**Po co:**  
bo Jupyter ma niższy wynik i większy rozrzut niż zwykłe podstawy Pythona.

#### C2. NumPy (35–45 min)
Najpierw krótko:
- [02.01 Understanding Data Types](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks_v1/02.01-Understanding-Data-Types.ipynb)
- [02.02 The Basics of NumPy Arrays](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks_v1/02.02-The-Basics-Of-NumPy-Arrays.ipynb)
- [02.04 Computation on arrays: aggregates](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks_v1/02.04-Computation-on-arrays-aggregates.ipynb)
- [02.06 Boolean Arrays and Masks](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks_v1/02.06-Boolean-Arrays-and-Masks.ipynb)

Potem lokalnie:
- [02_numpy_wprawki.ipynb](02_numpy_wprawki.ipynb)

**Po co:**  
bo `shape`, slicing, maski i wektorowość są jednym z głównych braków.

#### C3. pandas (60–75 min)
Najpierw krótko:
- [03.02 Data Indexing and Selection](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks_v1/03.02-Data-Indexing-and-Selection.ipynb)
- [03.04 Missing Values](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks_v1/03.04-Missing-Values.ipynb)
- [03.07 Merge and Join](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks_v1/03.07-Merge-and-Join.ipynb)
- [03.08 Aggregation and Grouping](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks_v1/03.08-Aggregation-and-Grouping.ipynb)
- [03.09 Pivot Tables](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks_v1/03.09-Pivot-Tables.ipynb)
- [03.10 Working With Strings](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks_v1/03.10-Working-With-Strings.ipynb)

Potem lokalnie:
- [03_pandas_wprawki.ipynb](03_pandas_wprawki.ipynb)

**Po co:**  
to jest najważniejszy blok całego spotkania.

#### C4. matplotlib (25–35 min)
Najpierw krótko:
- [04.01 Simple Line Plots](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks_v1/04.01-Simple-Line-Plots.ipynb)
- [04.02 Simple Scatter Plots](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks_v1/04.02-Simple-Scatter-Plots.ipynb)
- [04.05 Histograms and Binnings](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks_v1/04.05-Histograms-and-Binnings.ipynb)

Potem lokalnie:
- [04_matplotlib_wprawki.ipynb](04_matplotlib_wprawki.ipynb)

**Po co:**  
bo wykresy trzeba przećwiczyć od zera, a nie zakładać, że wszyscy je umieją.

---

### Blok D. Powrót do ankiety (30–45 min)
Po poznaniu narzędzi wracacie do ankiety i próbujecie:
- policzyć średnie,
- zrobić `groupby` po blokach,
- porównać pokrewne pytania,
- narysować 1–2 wykresy.

To dobrze domyka zajęcia: narzędzie -> wprawka -> zastosowanie na własnych danych.

---

### Blok E. GeoGebra i intuicja matematyczna (krótkie wstawki, nie osobny długi blok)
Najlepiej jako 5–10 minutowe przerywniki przy temacie:
- nachylenie i funkcja liniowa,
- pochodna jako zmiana,
- overfit / underfit,
- PCA jako obrót układu,
- gradient descent.

---

### Blok F. Co zostawić jako opcję / bonus
- Pygame / prosta gra 2D,
- większy blok OOP,
- bardziej zaawansowane metody ML na ankiecie.

To może być bardzo dobry przerywnik lub ciekawostka, ale **nie powinno zjeść osi wykładu**.

---

## Krótka rekomendacja końcowa

Jeśli trzeba coś uciąć, to:
1. **nie ucinaj** ankiety,
2. **nie ucinaj** pandas `groupby` / `merge`,
3. **nie ucinaj** prostych wykresów,
4. **ucinaj najpierw** bonusy typu gry / większy blok OOP / bardziej zaawansowane ML.
