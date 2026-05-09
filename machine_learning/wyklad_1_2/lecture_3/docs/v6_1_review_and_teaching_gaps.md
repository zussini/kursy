# Przegląd pakietu v6 i rekomendacje dydaktyczne — linear models → pre-PCA

## Diagnoza po przeglądzie paczki

Pakiet v6 ma sensowny rdzeń: małe przykłady, ręczne obliczenia, brak `statsmodels`, osobne moduły dla design matrix, odds/logit, likelihood, ROC/AUC i regularyzacji. Największa luka nie jest matematyczna, tylko **dydaktyczna**: student widzi wzory i małe tabelki, ale za rzadko widzi, jak te same obiekty wracają w prawdziwszej analizie danych.

Warto więc prowadzić blok w trzech warstwach:

1. **Warstwa tablicowa** — bardzo małe liczby, 4–10 obserwacji, wszystko liczone ręcznie.
2. **Warstwa notebookowa dydaktyczna** — ten sam pomysł w Pythonie, ale nadal na małym przykładzie.
3. **Warstwa danych z wcześniejszych zajęć** — `grades.csv` i `marathon-data.csv`, czyli ćwiczenia i mini-projekty.

Nie polecam wrzucać dużych danych zbyt wcześnie do głównego wykładu. Na wykładzie lepiej mieć małe liczby i wykresy. Duże dane powinny wejść jako: końcówka demonstracyjna, laboratorium, praca domowa albo projekt.

## Co znalazłem w `wyklad_2`

W paczce są dwa bardzo użyteczne zbiory:

### 1. `grades.csv`

Kolumny: `Name`, `StudyHours`, `Grade`.

Zastosowania:

- regresja liniowa: $Grade \sim StudyHours$,
- regresja logistyczna: $Pass \sim StudyHours$, np. $Pass=1$ gdy $Grade \ge 60$,
- likelihood i krzywa logistyczna na bardzo małej liczbie punktów,
- próg decyzyjny i interpretacja probability.

To jest najlepszy zbiór do przejścia z tablicy do notebooka.

### 2. `marathon-data.csv`

Kolumny: `age`, `gender`, `split`, `final`.

Po przetworzeniu dodałem:

- `split_hours`,
- `final_hours`,
- `second_half_hours`,
- `slowdown_minutes`,
- `female`,
- `under_4h`,
- `under_3h30`,
- `negative_split`.

Zastosowania:

- regresja liniowa: przewidywanie czasu końcowego z czasu połówki, wieku i płci,
- regresja logistyczna: przewidywanie, czy ktoś złamie 4 godziny,
- ROC/AUC: wynik modelu jako ranking prawdopodobieństw,
- threshold tuning: inny próg dla „wysokiej czułości”, inny dla „wysokiej precyzji”,
- leakage: użycie `final_hours` jako cechy przy celu `under_4h` daje nienaturalnie doskonały model,
- regularizacja: wielomiany i interakcje cech + Ridge/Lasso/Elastic Net.

Titanica nie znalazłem w przekazanej paczce `wyklad_2`. Jeżeli chcesz go dołączyć później, to pasuje naturalnie do osobnego laboratorium o `PassengerClass`, `Sex`, `Age`, `Fare`, `Survived`, ale obecnie lepiej wykorzystać dane, które już mamy.

## Główne luki logiczne w aktualnym materiale

### Luka 1: design matrix jest pokazana, ale nie wraca dostatecznie często

Warto powtarzać jedną mantrę:

$$
\text{model liniowy} = \text{wybieram kolumny w } X + \text{uczę } \beta
$$

Dla regresji liniowej:

$$
y = X\beta + \varepsilon
$$

Dla regresji logistycznej:

$$
\log\left(\frac{p}{1-p}\right)=X\beta
$$

To jest dokładnie ta sama idea liniowa, ale inna skala po lewej stronie.

### Luka 2: odds/logit powinny być mostem, nie osobnym tematem

Sekwencja powinna być zawsze taka:

$$
p \rightarrow odds=\frac{p}{1-p} \rightarrow \log(odds) \rightarrow X\beta \rightarrow \sigma(X\beta)
$$

Czyli:

1. Prawdopodobieństwo jest ograniczone do $[0,1]$.
2. Odds przechodzą od $0$ do $\infty$.
3. Log-odds przechodzą od $-\infty$ do $+\infty$.
4. Na tej skali można postawić prostą albo hiperpłaszczyznę.
5. Sigmoidą wracamy do prawdopodobieństwa.

### Luka 3: ROC/AUC jest za bardzo oderwane od modelu

W notebooku ROC/AUC warto najpierw pokazać toy scores, ale potem od razu użyć predykcji z regresji logistycznej na maratończykach:

$$
score_i = \hat p_i
$$

Dopiero potem zmieniamy próg i liczymy confusion matrix.

### Luka 4: regularyzacja potrzebuje dwóch intuicji naraz

Regularyzacja powinna być pokazana jako:

1. **kara w funkcji celu**:

$$
Loss(\beta)+\lambda\sum_j \beta_j^2
$$

albo

$$
Loss(\beta)+\lambda\sum_j |\beta_j|
$$

2. **geometria ograniczeń**:

$$
\sum_j \beta_j^2 \le c
$$

oraz

$$
\sum_j |\beta_j| \le c
$$

GeoGebra nadaje się głównie do drugiej intuicji.

## Rekomendowana kolejność prowadzenia

### Wykład 1: od design matrix do ANOVA

- zacznij od średniej,
- pokaż model z jedną średnią,
- pokaż dwie średnie jako design matrix,
- pokaż, że t-test i ANOVA są modelami liniowymi,
- dopiero na końcu pokaż `grades.csv` jako szybki przykład $Grade \sim StudyHours$.

### Wykład 2: odds, logit, logistic regression

- zacznij od gry: 1 wygrana, 4 porażki,
- probability vs odds,
- log-odds jako symetryczna skala,
- odds ratio na tabeli 2×2,
- logistic regression jako linia na log-odds,
- `grades.csv`: prawdopodobieństwo zaliczenia w funkcji godzin nauki.

### Wykład 3: likelihood, deviance, testy

- dla każdego punktu: jeśli $y=1$, wkład to $p$; jeśli $y=0$, wkład to $1-p$,
- mnożenie likelihood,
- suma log-likelihood,
- model zerowy vs pełny,
- deviance i LRT,
- Wald jako test pojedynczego współczynnika.

### Wykład 4: ROC/AUC + threshold tuning

- score to nie klasa,
- próg zmienia decyzję,
- ROC patrzy na wszystkie progi,
- AUC mierzy ranking,
- maratończycy: przewidywanie `under_4h`.

### Wykład 5: regularizacja

- overfitting przez za dużo cech,
- Ridge stabilizuje,
- Lasso zeruje część współczynników,
- Elastic Net jako kompromis,
- geometria L1/L2 w GeoGebrze.

## Co dodałem w wersji v6.1

1. Nowy notebook aplikacyjny: `15_applied_bridge_grades_marathon_v6_1.ipynb`.
2. Dane z poprzednich zajęć skopiowane do `data/`.
3. Przetworzony zbiór maratończyków: pełny i próbka 5000 rekordów.
4. Osobna karta: `dataset_bridge_and_project_ideas_v6_1.md`.
5. Rozbudowany pakiet GeoGebry:
   - instrukcje naturalne,
   - skrypty do wklejenia,
   - proste prototypy `.ggb` dla najważniejszych intuicji.

## Decyzja dydaktyczna

Najlepszy kompromis: **nie obciążać głównego wykładu dużym datasetem**, ale dodać dane jako „most” i ćwiczenia.

Na wykładzie pokazujesz 5–10 obserwacji. Na laboratorium studenci dostają te same pojęcia na `grades.csv` i `marathon-data.csv`. Na projekt dostają wariant: zbuduj model, uniknij leakage, oceń ROC/AUC, dobierz próg, porównaj regularyzację.
