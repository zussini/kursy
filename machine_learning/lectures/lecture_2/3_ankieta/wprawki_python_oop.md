
# Wstępne wprawki z Pythona / OOP wynikające z ankiety

## Po co je robić
Ankieta sugeruje, że grupa:
- jest dość pewna w typach danych, stringach i podstawowym Pythonie,
- jest mniej pewna w Jupyterze/Colabie, OOP oraz w przejściu od pętli do podejścia wektorowego,
- ma dużą lukę w pracy na danych (`shape`, filtrowanie, `groupby`, `merge`, braki danych).

Dlatego wprawki z „czystego Pythona” powinny być **krótkie i celowane**, a nie pełnym kursem Pythona od zera.

## Krótkie wprawki (15–25 min każda)

### 1. Jupyter / Colab entry
- otwórz notebook,
- uruchom 3 komórki,
- popraw jedną literówkę,
- dopisz `print()`,
- zapisz wynik.

### 2. Typy + stringi
- `split`, `join`, `replace`, `count`,
- wyciągnięcie liczby / słowa ze stringa,
- zbudowanie listy ze stringa,
- mały parser prostego napisu typu `"Anna,24,Kraków"`.

### 3. Listy / słowniki
- z listy imion policz liczbę liter,
- ze słownika `miasto -> liczba` wybierz maksimum,
- odwróć mapowanie w prostym przykładzie.

### 4. Pętla vs podejście „wektorowe”
- policz kwadraty liczb pętlą,
- policz to samo na tablicy NumPy,
- porównaj czytelność i wynik.

### 5. OOP mini
- klasa `Student(name, points)`,
- metoda `add_points`,
- metoda `passed(threshold)`.

To wystarczy jako wstęp przed wejściem w dane.

## Co z załączników „lekcje.zip” może się przydać
W załączniku są zrzuty ekranu z PixBlocks dla:
- operacji na łańcuchach znaków,
- list,
- zbiorów,
- słowników,
- sortowania,
- generatorów,
- obiektowości.

Najbardziej użyteczne pod ten kurs:
1. **łańcuchy znaków** – bo grupa wysoko ocenia `split`, ale warto to szybko ujednolicić,
2. **słowniki** – bo dobrze przygotowują do myślenia o mapowaniach i agregacjach,
3. **obiektowość** – ale tylko jako krótki dodatek, nie główny blok.

## Co z załączników „gry.zip” może się przydać
Widać inspiracje typu:
- platformówka,
- malowanie myszką,
- labirynt,
- memory,
- tic-tac-toe,
- proste gry zręcznościowe.

To może zadziałać jako **luźniejsza przerwa 30–45 min**, jeśli chcesz zrobić blok obiektowo-zabawowy.

Najlepsze opcje dydaktycznie:
- **malowanie myszką**: event loop, obiekty, stan,
- **prosta platformówka**: grawitacja, sterowanie, kolizje,
- **zbieranie punktów**: klasy `Player`, `Coin`, `Obstacle`.

## Moja rekomendacja
Jeśli ten blok ma służyć kursowi ML/data, to:
- **rdzeń**: Jupyter + stringi + słowniki + mini OOP,
- **bonus**: jedna bardzo prosta gra 2D jako luźniejsza przerwa,
- ale nie robiłbym pełnej platformówki kosztem NumPy/pandas.

Najbezpieczniejsza wersja:
1. 20 min: Jupyter + debug,
2. 20 min: stringi + listy + słowniki,
3. 15 min: mini OOP,
4. 30 min: mała zabawa typu malowanie myszką / zbieranie punktów.

To da „oddech”, ale nie rozwali osi wykładu.
