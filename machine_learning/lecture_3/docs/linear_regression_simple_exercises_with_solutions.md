# Regresja liniowa — proste ćwiczenia do tablicy i pracy własnej

Ten plik jest pomyślany jako karta pracy na krótkie wejścia w trakcie wykładu. Każde zadanie można zrobić w 3–8 minut. Najlepiej nie zaczynać od kodu: najpierw studenci liczą na kartce, potem sprawdzamy w Pythonie albo GeoGebrze.

---

## Część A — zadania dla studentów

### 1. Predykcja z prostej

Model ma postać:

$$\hat y = 2 + 3x$$

Policz predykcje dla:

| x | y | $\hat y$ | reszta $e=y-\hat y$ |
|---:|---:|---:|---:|
| 0 | 1 |  |  |
| 1 | 5 |  |  |
| 2 | 7 |  |  |

Pytanie: czy model systematycznie zawyża, zaniża, czy popełnia różne błędy?

---

### 2. SSE dla dwóch prostych

Dane:

| x | y |
|---:|---:|
| 1 | 2 |
| 2 | 3 |
| 3 | 5 |

Porównaj dwie proste:

$$\hat y = x + 1$$

oraz:

$$\hat y = 1.5x + 0.2$$

Dla każdej policz:

1. predykcje,
2. reszty,
3. kwadraty reszt,
4. SSE.

Która prosta jest lepsza według SSE?

---

### 3. Baseline średniej i $R^2$

Dane są prawdziwe wartości i predykcje modelu:

| obserwacja | y | $\hat y$ |
|---:|---:|---:|
| 1 | 10 | 9 |
| 2 | 12 | 13 |
| 3 | 13 | 12 |
| 4 | 15 | 16 |

Policz:

1. średnią $\bar y$,
2. $TSS=\sum(y_i-\bar y)^2$,
3. $SSE=\sum(y_i-\hat y_i)^2$,
4. $R^2=1-SSE/TSS$.

Pytanie: jak powiedzieć wynik $R^2$ zwykłym językiem?

---

### 4. Ujemne $R^2$ na danych testowych

Dane testowe:

| y | $\hat y$ |
|---:|---:|
| 3 | 10 |
| 4 | 10 |
| 5 | 10 |
| 6 | 10 |

Policz $R^2$.

Pytania:

1. Dlaczego wynik jest ujemny?
2. Czy ujemne $R^2$ musi oznaczać błąd w kodzie?
3. Co jest baseline’em w tym zadaniu?

---

### 5. Tabela ANOVA i statystyka $F$

Dla regresji z jedną cechą mamy:

- $n=12$,
- $p=1$,
- $TSS=240$,
- $SSE=90$.

Policz:

1. $SSR=TSS-SSE$,
2. $R^2$,
3. $df_{model}$, $df_{error}$, $df_{total}$,
4. $MSR$ i $MSE$,
5. statystykę $F$.

Sprawdź też wzorem:

$$F=\frac{R^2/p}{(1-R^2)/(n-p-1)}$$

---

### 6. Adjusted $R^2$: czy dodatkowe cechy naprawdę pomagają?

Dwa modele były ocenione na tym samym zbiorze treningowym, gdzie $n=50$.

| model | liczba cech $p$ | treningowe $R^2$ |
|---|---:|---:|
| A | 1 | 0.60 |
| B | 10 | 0.64 |

Policz adjusted $R^2$:

$$\bar R^2=1-(1-R^2)\frac{n-1}{n-p-1}$$

Pytanie: czy model B na pewno jest lepszy tylko dlatego, że ma większe zwykłe $R^2$?

---

### 7. Fit, underfitting, overfitting

Porównaj modele:

| model | train $R^2$ | test $R^2$ |
|---|---:|---:|
| A | 0.96 | 0.38 |
| B | 0.82 | 0.79 |
| C | 0.42 | 0.39 |

Dla każdego modelu zdecyduj: underfitting, sensowny fit czy overfitting.

Który model wybrałbyś do predykcji i dlaczego?

---

### 8. Reszty tworzą literę U

Po dopasowaniu prostej widzisz wykres reszt, na którym punkty układają się w kształt litery U.

Odpowiedz:

1. Co to sugeruje o zależności między $x$ i $y$?
2. Jaką dodatkową cechę można rozważyć?
3. Czy samo wysokie treningowe $R^2$ wystarczy, żeby zignorować wykres reszt?

---

### 9. Statystyczna istotność kontra siła predykcji

Model ma:

- p-value z testu $F$: 0.0001,
- testowe $R^2$: 0.08.

Odpowiedz:

1. Czy model może być statystycznie istotny?
2. Czy jest silny predykcyjnie?
3. Jak wytłumaczyć studentom tę różnicę jednym zdaniem?

---

## Część B — klucz odpowiedzi

### 1. Predykcja z prostej

Dla $\hat y=2+3x$:

| x | y | $\hat y$ | $e=y-\hat y$ |
|---:|---:|---:|---:|
| 0 | 1 | 2 | -1 |
| 1 | 5 | 5 | 0 |
| 2 | 7 | 8 | -1 |

Model dwa razy zawyża o 1 i raz trafia dokładnie.

### 2. SSE dla dwóch prostych

Prosta $\hat y=x+1$:

| x | y | $\hat y$ | e | $e^2$ |
|---:|---:|---:|---:|---:|
| 1 | 2 | 2 | 0 | 0 |
| 2 | 3 | 3 | 0 | 0 |
| 3 | 5 | 4 | 1 | 1 |

$SSE=1$.

Prosta $\hat y=1.5x+0.2$:

| x | y | $\hat y$ | e | $e^2$ |
|---:|---:|---:|---:|---:|
| 1 | 2 | 1.7 | 0.3 | 0.09 |
| 2 | 3 | 3.2 | -0.2 | 0.04 |
| 3 | 5 | 4.7 | 0.3 | 0.09 |

$SSE=0.22$. Według SSE druga prosta jest lepsza.

### 3. $R^2$

$\bar y=(10+12+13+15)/4=12.5$.

$$TSS=(10-12.5)^2+(12-12.5)^2+(13-12.5)^2+(15-12.5)^2=13$$

$$SSE=(10-9)^2+(12-13)^2+(13-12)^2+(15-16)^2=4$$

$$R^2=1-4/13\approx 0.692$$

Interpretacja: model usuwa około 69.2% błędu baseline’u średniej.

### 4. Ujemne $R^2$

$\bar y=4.5$.

$$TSS=(3-4.5)^2+(4-4.5)^2+(5-4.5)^2+(6-4.5)^2=5$$

$$SSE=(3-10)^2+(4-10)^2+(5-10)^2+(6-10)^2=126$$

$$R^2=1-126/5=-24.2$$

Wynik jest ujemny, bo model jest dużo gorszy od baseline’u średniej. To może się zdarzyć na danych testowych i nie musi oznaczać błędu w kodzie.

### 5. $F$

$$SSR=240-90=150$$

$$R^2=1-90/240=0.625$$

Stopnie swobody:

- $df_{model}=p=1$,
- $df_{error}=n-p-1=10$,
- $df_{total}=n-1=11$.

$$MSR=150/1=150$$

$$MSE=90/10=9$$

$$F=150/9\approx 16.67$$

Sprawdzenie:

$$F=\frac{0.625/1}{(1-0.625)/10}=\frac{0.625}{0.0375}\approx 16.67$$

### 6. Adjusted $R^2$

Model A:

$$\bar R_A^2=1-(1-0.60)\frac{49}{48}\approx 0.592$$

Model B:

$$\bar R_B^2=1-(1-0.64)\frac{49}{39}\approx 0.548$$

Model B ma większe zwykłe $R^2$, ale mniejsze adjusted $R^2$. Dodatkowe cechy poprawiły dopasowanie zbyt słabo względem wzrostu złożoności.

### 7. Fit/underfit/overfit

- Model A: overfitting — świetny train, dużo gorszy test.
- Model B: sensowny fit — train i test są podobne i dość dobre.
- Model C: underfitting — oba wyniki słabe.

Do predykcji najrozsądniejszy jest model B.

### 8. Reszty w kształcie U

To sugeruje zależność nieliniową. Można rozważyć cechę $x^2$, regresję wielomianową albo inny model nieliniowy. Wykresu reszt nie warto ignorować, bo pokazuje strukturę, której model nie wyjaśnił.

### 9. Istotność kontra predykcja

Tak, model może być statystycznie istotny, zwłaszcza przy dużej liczbie obserwacji. Jednocześnie testowe $R^2=0.08$ oznacza słabą siłę predykcyjną. Jednozdaniowo:

> Test $F$ mówi, że sygnał prawdopodobnie nie jest zerowy, a testowe $R^2$ mówi, że sygnał jest mały dla praktycznej predykcji.
