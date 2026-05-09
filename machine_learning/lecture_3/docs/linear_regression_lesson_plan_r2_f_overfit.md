# Plan prowadzenia wykładu — regresja liniowa, $R^2$, $F$ i overfitting

## Wersja 45 minut

1. **5 min — problem regresji**  
   Pokazujemy dane `weight -> size`. Pytanie: czy masa pomaga przewidzieć rozmiar?

2. **8 min — baseline średniej**  
   Model naiwny: zawsze przewiduj $\bar y$. To przygotowuje intuicję pod $R^2$.

3. **10 min — prosta i SSE**  
   Rysujemy kilka prostych. Dla jednej małej tabelki liczymy predykcje, reszty, kwadraty reszt i SSE.

4. **7 min — `fit()`**  
   `fit()` oznacza znalezienie parametrów $b_0,b_1$, które minimalizują SSE na danych treningowych.

5. **8 min — $R^2$**  
   $R^2=1-SSE/TSS$. Najważniejsze zdanie: $R^2$ porównuje model z baseline’em średniej.

6. **7 min — train/test i overfitting**  
   Pokazujemy, że wysokie train $R^2$ nie wystarcza. Krótka tabela: train/test dla kilku modeli.

## Wersja 90 minut

1. **10 min — dane i baseline**  
   Scatterplot, średnia, SSE baseline’u.

2. **15 min — kilka prostych i funkcja straty**  
   Studenci ręcznie liczą SSE dla dwóch prostych. Potem pokazujemy powierzchnię błędu.

3. **10 min — OLS w sklearn**  
   `LinearRegression().fit(X, y)`, współczynniki, predykcje, reszty.

4. **10 min — ręczna formuła $b_0,b_1$**  
   Nachylenie jako współzmienność $x$ i $y$ podzielona przez zmienność $x$.

5. **15 min — $R^2$, TSS, SSE, SSR**  
   Liczenie ręczne i interpretacja. Pokazujemy też możliwość ujemnego $R^2$ na teście.

6. **10 min — test $F$**  
   Tabela ANOVA: $SSR$, $SSE$, stopnie swobody, $MSR$, $MSE$, $F=MSR/MSE$.

7. **10 min — adjusted $R^2$ i dodawanie losowych cech**  
   Zwykłe treningowe $R^2$ może rosnąć, ale adjusted $R^2$ i walidacja ostrzegają przed złożonością.

8. **10 min — underfitting/overfitting**  
   Regresja wielomianowa: stopień 1, 3, 6, 15. Porównanie train/test/CV.

9. **opcjonalnie — GeoGebra**  
   Suwaki `a`, `b`, ręczne minimalizowanie SSE, porównanie z `FitLine`, liczenie $R^2$.

## Najważniejsze zdania do powtórzenia

- Regresja liniowa minimalizuje sumę kwadratów pionowych błędów.
- `fit()` to dopasowanie parametrów na danych treningowych.
- $R^2$ mówi, jak bardzo model poprawia baseline średniej.
- Statystyka $F$ porównuje wyjaśnioną zmienność z niewyjaśnionym błędem.
- Wysokie treningowe $R^2$ nie oznacza automatycznie dobrej generalizacji.
- Wykres reszt często mówi więcej niż jedna liczba.
