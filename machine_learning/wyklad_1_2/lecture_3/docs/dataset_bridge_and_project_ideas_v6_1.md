# Most danych do bloku linear/logistic/ROC/regularization — v6.1

Ten plik odpowiada na pytanie: **czy dodawać zbiory danych już teraz?**

Tak, ale nie jako główny ciężar wykładu. Dane warto dodać jako warstwę ćwiczeniową i projektową.

## Zasada prowadzenia

Na wykładzie:

- małe liczby,
- ręczne obliczenia,
- jeden wykres,
- jedna intuicja.

Na ćwiczeniach:

- `grades.csv`,
- `marathon-data.csv`,
- train/test,
- ROC/AUC,
- threshold tuning,
- leakage,
- regularizacja.

Na projekcie:

- pełny pipeline,
- raport metryk,
- interpretacja współczynników,
- decyzja biznesowa/statystyczna.

## Dataset 1: oceny i godziny nauki

Plik: `data/previous_lecture_grades.csv`.

### Zadanie A: regresja liniowa

Cel:

$$
Grade \sim StudyHours
$$

Pytania:

1. Czy więcej godzin nauki zwiększa ocenę?
2. Ile punktów oceny daje jedna dodatkowa godzina według modelu?
3. Jak wygląda $R^2$?
4. Czy model ma sens dla `StudyHours = 0`?

### Zadanie B: regresja logistyczna

Tworzymy:

$$
Pass = \mathbb{1}(Grade \ge 60)
$$

Model:

$$
\log\left(\frac{p}{1-p}\right)=\beta_0+\beta_1 StudyHours
$$

Pytania:

1. Co oznacza $p$?
2. Co oznacza $\beta_1$?
3. Co oznacza $e^{\beta_1}$?
4. Przy ilu godzinach model daje $p \approx 0.5$?

## Dataset 2: maratończycy

Pliki:

- `data/previous_lecture_marathon_processed_sample.csv`,
- `data/previous_lecture_marathon_processed_full.csv`.

Kolumny po przetworzeniu:

- `age`,
- `gender`,
- `split_hours`,
- `final_hours`,
- `second_half_hours`,
- `slowdown_minutes`,
- `female`,
- `under_4h`,
- `under_3h30`,
- `negative_split`.

### Zadanie C: regresja liniowa

Cel:

$$
final\_hours \sim split\_hours + age + female
$$

Pytania:

1. Która cecha jest najsilniejsza?
2. Czy wiek pomaga po uwzględnieniu czasu połówki?
3. Co oznacza współczynnik przy `female`?
4. Jakie są MAE, RMSE i $R^2$ na train/test?

### Zadanie D: regresja logistyczna

Cel:

$$
under\_4h \sim split\_hours + age + female
$$

Pytania:

1. Czy model przewiduje prawdopodobieństwo, czy klasę?
2. Jak dobrać próg, jeśli zależy nam na wysokiej czułości?
3. Jak dobrać próg, jeśli zależy nam na wysokiej precyzji?
4. Jakie jest ROC/AUC?

### Zadanie E: leakage

Zły model:

$$
under\_4h \sim split\_hours + age + female + final\_hours
$$

Ponieważ `under_4h` jest zdefiniowane z `final_hours`, użycie `final_hours` jako cechy jest wyciekiem informacji.

Pytania:

1. Dlaczego metryka robi się podejrzanie dobra?
2. Co wiedziałby model w chwili predykcji?
3. Jakie cechy są dozwolone „na półmetku” maratonu?

### Zadanie F: regularyzacja

Dodajemy cechy wielomianowe i interakcje:

$$
split\_hours, age, female, split\_hours^2, age^2, split\_hours \cdot age, \ldots
$$

Porównujemy:

- brak silnej regularyzacji,
- L2/Ridge,
- L1/Lasso.

Pytania:

1. Czy AUC bardzo się zmienia?
2. Co dzieje się ze współczynnikami?
3. Czy L1 zeruje część cech?
4. Kiedy interpretowalność jest ważniejsza niż minimalna poprawa metryki?

## Propozycja mini-projektu

Temat: **Czy na półmetku maratonu można przewidzieć ukończenie poniżej 4 godzin?**

Minimalne wymagania:

1. Stwórz cechy dostępne na półmetku: `split_hours`, `age`, `gender`.
2. Stwórz target `under_4h`.
3. Podziel dane na train/test.
4. Wytrenuj regresję logistyczną.
5. Policz ROC/AUC.
6. Wybierz próg dla konkretnego celu:
   - wariant A: chcesz złapać większość osób, które realnie złamią 4h,
   - wariant B: chcesz mieć pewność, że wskazane osoby naprawdę złamią 4h.
7. Opisz, które cechy wolno użyć, a które powodują leakage.
8. Porównaj model z i bez regularyzacji.

Rozszerzenie:

- kalibracja probability,
- porównanie z drzewem decyzyjnym,
- interpretacja odds ratio,
- analiza oddzielnie dla kobiet i mężczyzn.
