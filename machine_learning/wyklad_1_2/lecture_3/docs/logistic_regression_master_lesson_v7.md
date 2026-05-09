# Regresja logistyczna — master lekcja v7

**Zakres:** od design matrix i prostych modeli liniowych do odds, log-odds, odds ratio, regresji logistycznej, likelihood, deviance, testów, ROC/AUC i regularyzacji. PCA jest celowo pominięte.

**Cel dydaktyczny:** po tym materiale student ma umieć powiedzieć nie tylko „regresja logistyczna daje prawdopodobieństwo”, ale też:

- dlaczego zwykła regresja liniowa nie jest dobrym modelem dla etykiet $0/1$,
- jak przechodzi się od prawdopodobieństwa do odds, potem do log-odds, a potem do liniowego modelu $X\beta$,
- skąd bierze się funkcja logistyczna,
- jak interpretować intercept, slope, log-odds ratio i odds ratio,
- dlaczego w regresji logistycznej używa się likelihood zamiast $SSE$,
- jak ręcznie policzyć małe przykłady: odds, $OR$, Fisher, chi-square, Wald, log-likelihood, deviance, McFadden pseudo-$R^2$,
- jak połączyć logistic regression z ROC/AUC, progiem decyzyjnym i regularyzacją.

---

## 0. Minimalna mapa filmów / lekcji

Ten blok warto prowadzić w takiej kolejności:

1. **Design matrices for linear models**  
   Wspólny język: regresja, t-test i ANOVA można zapisać jako $y=X\beta+\varepsilon$.

2. **Odds and log(Odds)**  
   Najpierw pokazujemy, że probability i odds to nie to samo, a log-odds robią skalę symetryczną.

3. **Odds ratios and log(Odds ratios)**  
   Pokazujemy tabelę $2\times 2$, obliczamy $OR$, $\log(OR)$ i trzy testy: Fisher, chi-square, Wald.

4. **Logistic regression — main idea**  
   Regresja logistyczna jest liniowa nie na skali probability, tylko na skali log-odds.

5. **Logistic regression details: coefficients**  
   Intercept to baseline log-odds, współczynnik dla zmiennej binarnej to log-odds ratio, a $e^{\beta_j}$ to odds ratio.

6. **Logistic regression details: maximum likelihood**  
   Dopasowanie przez maksymalizację likelihood Bernoulliego, nie przez minimalizację $SSE$.

7. **Logistic regression details: pseudo-$R^2$ and p-value**  
   Porównujemy model pełny z modelem zerowym przez log-likelihood, deviance i test likelihood-ratio.

8. **Saturated models, deviance, deviance residuals**  
   Saturated model dopasowuje każdy punkt idealnie; deviance mierzy, ile tracimy względem takiego ideału.

9. **ROC/AUC**  
   Oddzielamy jakość rankingu od wyboru progu decyzyjnego.

10. **Regularization: Ridge, Lasso, Elastic Net**  
    Kara na współczynniki stabilizuje model i ogranicza przeuczenie.

---

# Część I. Design matrix jako wspólny język

## 1. Jedno równanie, wiele modeli

Na tablicy zaczynamy od:

$$
y=X\beta+\varepsilon
$$

gdzie:

- $y$ — wektor obserwacji,
- $X$ — **design matrix**, czyli tabela cech użyta przez model,
- $\beta$ — parametry modelu,
- $\varepsilon$ — błąd.

Dla regresji liniowej z jedną cechą:

$$
y_i=\beta_0+\beta_1x_i+\varepsilon_i
$$

macierz wygląda tak:

$$
X=
\begin{bmatrix}
1 & x_1\\
1 & x_2\\
\vdots & \vdots\\
1 & x_n
\end{bmatrix}
$$

Pierwsza kolumna jedynek odpowiada za intercept $\beta_0$.

### Ćwiczenie tablicowe 1

Mamy punkty:

| obserwacja | $x$ | $y$ |
|---:|---:|---:|
| 1 | 1 | 2 |
| 2 | 2 | 3 |
| 3 | 3 | 5 |

Zapisz $X$, $y$ i $\beta$ dla modelu $y=\beta_0+\beta_1x$.

**Odpowiedź:**

$$
X=
\begin{bmatrix}
1&1\\
1&2\\
1&3
\end{bmatrix},\quad
 y=
\begin{bmatrix}
2\\3\\5
\end{bmatrix},\quad
\beta=
\begin{bmatrix}
\beta_0\\\beta_1
\end{bmatrix}
$$

---

## 2. t-test jako regresja liniowa

Dwie grupy:

| grupa | wartości ekspresji genu |
|---|---|
| Control | 2.0, 2.1, 2.5 |
| Mutant | 3.4, 3.6, 3.8 |

Kodujemy grupę jako $0/1$:

| $y$ | $x_{mutant}$ |
|---:|---:|
| 2.0 | 0 |
| 2.1 | 0 |
| 2.5 | 0 |
| 3.4 | 1 |
| 3.6 | 1 |
| 3.8 | 1 |

Model:

$$
y=\beta_0+\beta_1x_{mutant}+\varepsilon
$$

Interpretacja:

- $\beta_0$ = średnia w grupie Control,
- $\beta_1$ = różnica średnich Mutant minus Control,
- test $H_0:\beta_1=0$ to test, czy grupy różnią się średnio.

Czyli t-test można opisać jako regresję z jedną kolumną $0/1$ w design matrix.

---

## 3. ANOVA jako regresja liniowa z kilkoma kolumnami

Dla trzech grup $A,B,C$ przy kodowaniu treatment coding:

$$
y=\beta_0+\beta_B I(B)+\beta_C I(C)+\varepsilon
$$

Przykładowa design matrix:

| grupa | intercept | $I(B)$ | $I(C)$ |
|---|---:|---:|---:|
| A | 1 | 0 | 0 |
| A | 1 | 0 | 0 |
| B | 1 | 1 | 0 |
| B | 1 | 1 | 0 |
| C | 1 | 0 | 1 |
| C | 1 | 0 | 1 |

Interpretacja:

- $\beta_0$ = średnia grupy bazowej $A$,
- $\beta_B$ = różnica $B-A$,
- $\beta_C$ = różnica $C-A$.

**Wniosek dydaktyczny:** regresja, t-test i ANOVA różnią się głównie tym, jak zbudujemy $X$.

---

# Część II. Probability, odds i log-odds

## 4. Probability vs odds

Prawdopodobieństwo sukcesu:

$$
p=\frac{\text{liczba sukcesów}}{\text{liczba wszystkich prób}}
$$

Szanse, czyli odds:

$$
odds=\frac{\text{liczba sukcesów}}{\text{liczba porażek}}
$$

Jeżeli znamy $p$, to:

$$
odds=\frac{p}{1-p}
$$

Jeżeli znamy odds, to:

$$
p=\frac{odds}{1+odds}
$$

### Przykład tablicowy: 5 meczów

Drużyna wygrywa $1$ mecz i przegrywa $4$ mecze.

$$
p=\frac{1}{5}=0.2
$$

$$
odds=\frac{1}{4}=0.25
$$

**Pułapka:** probability $0.2$ i odds $0.25$ to nie to samo.

---

## 5. Dlaczego bierzemy logarytm z odds?

Odds są asymetryczne:

- odds $=\frac{1}{6}\approx 0.167$ oznacza mocno „przeciw”,
- odds $=\frac{6}{1}=6$ oznacza mocno „za”.

Po logarytmie:

$$
\log\left(\frac{1}{6}\right)\approx -1.79
$$

$$
\log(6)\approx 1.79
$$

Dostajemy skalę symetryczną wokół $0$.

| $p$ | odds $=p/(1-p)$ | log-odds $=\log(p/(1-p))$ |
|---:|---:|---:|
| 0.10 | 0.111 | -2.303 |
| 0.25 | 0.333 | -1.099 |
| 0.50 | 1.000 | 0.000 |
| 0.75 | 3.000 | 1.099 |
| 0.90 | 9.000 | 2.303 |

Funkcja:

$$
logit(p)=\log\left(\frac{p}{1-p}\right)
$$

nazywa się **logit**.

---

# Część III. Odds ratio i log odds ratio

## 6. Tabela $2\times 2$: mutacja genu i rak

Przykład często używany do pokazania odds ratio:

| grupa | Rak + | Rak - |
|---|---:|---:|
| Mutacja + | 23 | 117 |
| Mutacja - | 6 | 210 |

Oznaczmy:

$$
\begin{array}{c|cc}
 & \text{Rak +} & \text{Rak -}\\\hline
\text{Mutacja +} & a & b\\
\text{Mutacja -} & c & d
\end{array}
$$

Tutaj:

$$
a=23,\quad b=117,\quad c=6,\quad d=210
$$

Odds raka w grupie z mutacją:

$$
odds_{mut}=\frac{23}{117}\approx 0.1966
$$

Odds raka w grupie bez mutacji:

$$
odds_{norm}=\frac{6}{210}\approx 0.0286
$$

Odds ratio:

$$
OR=\frac{odds_{mut}}{odds_{norm}}
=\frac{23/117}{6/210}
=\frac{23\cdot210}{117\cdot6}
\approx 6.88
$$

Log odds ratio:

$$
\log(OR)=\log(6.88)\approx 1.93
$$

Interpretacja:

- $OR=1$ — brak różnicy odds,
- $OR>1$ — odds większe w pierwszej grupie,
- $OR<1$ — odds mniejsze w pierwszej grupie,
- $\log(OR)=0$ — brak różnicy na skali log-odds.

---

## 7. Trzy testy dla tabeli $2\times 2$

Wykładowo warto powiedzieć:

- $OR$ mówi o **wielkości efektu**,
- p-value mówi, czy efekt jest zgodny z przypadkiem przy hipotezie zerowej,
- confidence interval mówi, jak niepewna jest estymacja.

### 7.1 Fisher exact test

Fisher zakłada ustalone marginesy tabeli. Dla tabeli:

$$
\begin{array}{c|cc}
 & \text{Rak +} & \text{Rak -}\\\hline
\text{Mutacja +} & a & b\\
\text{Mutacja -} & c & d
\end{array}
$$

przy ustalonych sumach brzegowych losową zmienną jest lewa-górna komórka $a$.

Prawdopodobieństwo konkretnej tabeli:

$$
P(A=x)=\frac{\binom{a+b}{x}\binom{c+d}{a+c-x}}{\binom{a+b+c+d}{a+c}}
$$

To jest rozkład hipergeometryczny.

**Intuicja:** przy założeniu „brak związku między mutacją a rakiem” pytamy, jak często losowe rozmieszczenie przypadków dałoby tabelę tak ekstremalną jak obserwowana.

### 7.2 Chi-square test

W teście niezależności liczymy oczekiwane liczebności:

$$
E_{ij}=\frac{\text{suma wiersza}_i\cdot\text{suma kolumny}_j}{n}
$$

Potem:

$$
\chi^2=\sum_{ij}\frac{(O_{ij}-E_{ij})^2}{E_{ij}}
$$

Dla tabeli $2\times 2$ bez dodatkowych parametrów:

$$
df=(2-1)(2-1)=1
$$

### 7.3 Wald test dla $\log(OR)$

Dla dużych próbek:

$$
\log(OR)\approx N(\theta, SE^2)
$$

a błąd standardowy można przybliżyć przez:

$$
SE(\log OR)=\sqrt{\frac{1}{a}+\frac{1}{b}+\frac{1}{c}+\frac{1}{d}}
$$

Statystyka:

$$
z=\frac{\log(OR)-0}{SE(\log OR)}
$$

Jeżeli $|z|\gtrsim 2$, zwykle mamy p-value poniżej około $0.05$.

Confidence interval:

$$
\log(OR)\pm 1.96\cdot SE
$$

Po przeskalowaniu z powrotem:

$$
CI_{OR}=\left(e^{L},e^{U}\right)
$$

---

# Część IV. Dlaczego zwykła regresja liniowa nie wystarcza?

## 8. Problem klasyfikacji binarnej

Załóżmy, że chcemy przewidzieć:

$$
y=\begin{cases}
1 & \text{mysz otyła / pacjent chory / mail spam}\\
0 & \text{mysz nieotyła / pacjent zdrowy / mail nie-spam}
\end{cases}
$$

Regresja liniowa może dać:

$$
\hat y=1.3 \quad\text{albo}\quad \hat y=-0.2
$$

Dla probability to bez sensu, bo prawdopodobieństwo musi być w zakresie:

$$
0\le p\le 1
$$

Dodatkowo zależność często ma kształt S:

- małe $x$ — prawdopodobieństwo bliskie $0$,
- okolice granicy — szybka zmiana,
- duże $x$ — prawdopodobieństwo bliskie $1$.

---

## 9. Cztery drogi do regresji logistycznej

### Droga A: „chcę mieć probability od 0 do 1”

Zaczynamy od liniowego score:

$$
\eta=\beta_0+\beta_1x
$$

Score $\eta$ może być dowolną liczbą rzeczywistą. Żeby dostać probability, przepuszczamy go przez sigmoidę:

$$
p=\sigma(\eta)=\frac{1}{1+e^{-\eta}}
$$

### Droga B: „chcę zachować liniowość, ale na dobrej skali”

Nie modelujemy bezpośrednio $p$, tylko log-odds:

$$
\log\left(\frac{p}{1-p}\right)=\beta_0+\beta_1x
$$

Po odwróceniu:

$$
\frac{p}{1-p}=e^{\beta_0+\beta_1x}
$$

$$
p=\frac{e^{\beta_0+\beta_1x}}{1+e^{\beta_0+\beta_1x}}
=\frac{1}{1+e^{-(\beta_0+\beta_1x)}}
$$

To dokładnie funkcja logistyczna.

### Droga C: „mam dane 0/1, więc naturalny jest Bernoulli”

Dla pojedynczej obserwacji:

$$
y_i\sim Bernoulli(p_i)
$$

$$
P(y_i|p_i)=p_i^{y_i}(1-p_i)^{1-y_i}
$$

Teraz wiążemy $p_i$ z cechami przez:

$$
p_i=\sigma(x_i^T\beta)
$$

I dobieramy $\beta$ tak, aby zaobserwowane dane były jak najbardziej prawdopodobne.

### Droga D: „chcę klasyfikatora z progiem”

Model daje probability score:

$$
\hat p_i=P(y_i=1|x_i)
$$

Decyzję robimy osobno:

$$
\hat y_i=\begin{cases}
1 & \hat p_i\ge t\\
0 & \hat p_i<t
\end{cases}
$$

Najczęściej $t=0.5$, ale w medycynie, fraudzie lub bezpieczeństwie próg dobiera się do kosztów pomyłek.

---

## 10. Najważniejsza różnica: regresja liniowa vs logistyczna

| element | regresja liniowa | regresja logistyczna |
|---|---|---|
| $y$ | ciągłe | binarne $0/1$ |
| modelowana wielkość | średnia $E[y|x]$ | probability $P(y=1|x)$ |
| skala liniowa | $y$ | $\log\left(\frac{p}{1-p}\right)$ |
| predykcja | dowolna liczba | liczba od $0$ do $1$ |
| dopasowanie | minimalizacja $SSE$ | maksymalizacja likelihood |
| błąd | często normalny | Bernoulli/binomial |
| typowe metryki | RMSE, MAE, $R^2$ | log-loss, deviance, ROC/AUC, confusion matrix |

Krótkie zdanie do zapamiętania:

> Regresja logistyczna to model liniowy na skali log-odds, przekształcony sigmoidą do prawdopodobieństwa.

---

# Część V. Współczynniki regresji logistycznej

## 11. Model ogólny

Dla wielu cech:

$$
\eta_i=x_i^T\beta=\beta_0+\beta_1x_{i1}+\cdots+\beta_px_{ip}
$$

$$
p_i=\frac{1}{1+e^{-\eta_i}}
$$

oraz równoważnie:

$$
\log\left(\frac{p_i}{1-p_i}\right)=x_i^T\beta
$$

---

## 12. Interpretacja interceptu

Jeśli wszystkie cechy są równe $0$:

$$
\log\left(\frac{p}{1-p}\right)=\beta_0
$$

Czyli:

$$
odds=e^{\beta_0}
$$

$$
p=\frac{e^{\beta_0}}{1+e^{\beta_0}}
$$

**Uwaga dydaktyczna:** intercept ma sens tylko wtedy, gdy $x=0$ ma sens albo gdy cechy zostały sensownie wycentrowane.

---

## 13. Interpretacja współczynnika dla zmiennej ciągłej

Jeśli $x$ rośnie o $1$, to:

$$
\eta(x+1)-\eta(x)=\beta_1
$$

Na skali odds:

$$
\frac{odds(x+1)}{odds(x)}=e^{\beta_1}
$$

Czyli $e^{\beta_1}$ to odds ratio dla wzrostu cechy o jedną jednostkę.

Przykład:

- $\beta_1=0.7$,
- $e^{0.7}\approx 2.01$.

Interpretacja: wzrost cechy o $1$ mnoży odds klasy $1$ przez około $2.01$.

---

## 14. Interpretacja zmiennej binarnej — przykład heart disease `sex`

W demo StatQuest w R używany jest zbiór Cleveland Heart Disease. Po przygotowaniu danych prosty model przewiduje chorobę serca na podstawie płci.

Tabela z demo:

| `hd` | F | M |
|---|---:|---:|
| Healthy | 71 | 89 |
| Unhealthy | 25 | 112 |

Kodujemy:

- $y=1$ dla `Unhealthy`,
- $sexM=0$ dla `F`,
- $sexM=1$ dla `M`.

Model:

$$
\log\left(\frac{p}{1-p}\right)=\beta_0+\beta_1 sexM
$$

Dla kobiet:

$$
\beta_0=\log\left(\frac{25}{71}\right)\approx -1.0438
$$

Prawdopodobieństwo choroby wśród kobiet:

$$
p_F=\frac{25}{25+71}\approx 0.2604
$$

Dla mężczyzn log-odds:

$$
\beta_0+\beta_1=\log\left(\frac{112}{89}\right)\approx 0.2300
$$

Współczynnik przy `sexM`:

$$
\beta_1=
\log\left(\frac{112/89}{25/71}\right)\approx 1.2737
$$

Odds ratio:

$$
e^{1.2737}\approx 3.57
$$

Interpretacja:

> Według tego prostego modelu odds bycia w klasie `Unhealthy` są u mężczyzn około $3.57$ razy większe niż u kobiet.

---

## 15. Zmienne kategoryczne i design matrix

Dla zmiennej `chest pain` z czterema kategoriami nie tworzymy jednej kolumny $1,2,3,4$ jako liczby porządkowej, jeśli kategorie nie mają naturalnego dystansu. Robimy kolumny zero-jedynkowe.

Przykład przy kategorii bazowej `cp=typical`:

| pacjent | intercept | cp_atypical | cp_nonanginal | cp_asymptomatic |
|---:|---:|---:|---:|---:|
| 1 | 1 | 0 | 0 | 0 |
| 2 | 1 | 1 | 0 | 0 |
| 3 | 1 | 0 | 1 | 0 |
| 4 | 1 | 0 | 0 | 1 |

Każdy współczynnik mówi o zmianie log-odds względem kategorii bazowej.

---

# Część VI. Likelihood i dopasowanie modelu

## 16. Dlaczego nie $SSE$?

W regresji liniowej minimalizujemy:

$$
SSE=\sum_i(y_i-\hat y_i)^2
$$

Ale w klasyfikacji binarnej:

- $y_i$ jest $0$ albo $1$,
- przewidujemy $p_i$,
- błąd ma rozkład Bernoulliego, a nie normalny,
- na skali log-odds punkty $y=0$ i $y=1$ odpowiadają krańcom $-\infty$ i $+\infty$, więc „odległość do linii” nie jest wygodnym pojęciem.

Naturalna funkcja dopasowania to likelihood Bernoulliego.

---

## 17. Likelihood dla pojedynczego punktu

Jeżeli $y_i=1$, to model daje prawdopodobieństwo $p_i$.

$$
P(y_i=1)=p_i
$$

Jeżeli $y_i=0$, to:

$$
P(y_i=0)=1-p_i
$$

Możemy to zapisać jednym wzorem:

$$
P(y_i|p_i)=p_i^{y_i}(1-p_i)^{1-y_i}
$$

Cały likelihood:

$$
L(\beta)=\prod_{i=1}^{n}p_i^{y_i}(1-p_i)^{1-y_i}
$$

Log-likelihood:

$$
\ell(\beta)=\sum_{i=1}^{n}\left[y_i\log(p_i)+(1-y_i)\log(1-p_i)\right]
$$

Ponieważ:

$$
p_i=\sigma(x_i^T\beta)
$$

można też zapisać stabilnie numerycznie:

$$
\ell(\beta)=\sum_i\left[y_i\eta_i-\log(1+e^{\eta_i})\right]
$$

gdzie $\eta_i=x_i^T\beta$.

---

## 18. Proces dopasowania — wersja „filmowo-tablicowa”

1. Rysujemy kandydacką linię na skali log-odds:

   $$
   \eta=\beta_0+\beta_1x
   $$

2. Dla każdego punktu liczymy $\eta_i$.

3. Zamieniamy $\eta_i$ na probability:

   $$
   p_i=\frac{1}{1+e^{-\eta_i}}
   $$

4. Dla punktu z $y_i=1$ wkład do likelihood to $p_i$.

5. Dla punktu z $y_i=0$ wkład do likelihood to $1-p_i$.

6. Mnożymy wkłady albo, lepiej, sumujemy logarytmy.

7. Przesuwamy/obracamy linię tak długo, aż log-likelihood będzie maksymalny.

---

## 19. Gradient i Hessian — opcjonalnie dla prowadzącego

Dla logistic regression:

$$
\nabla \ell(\beta)=X^T(y-p)
$$

Hessian log-likelihood:

$$
H=-X^TWX
$$

gdzie:

$$
W=diag(p_i(1-p_i))
$$

Newton-Raphson / IRLS aktualizuje parametry tak, aby znaleźć maksimum log-likelihood. W notebooku można to pokazać bez `statsmodels`.

---

# Część VII. Model zerowy, deviance, pseudo-$R^2$, p-value

## 20. Model zerowy

Model zerowy ma tylko intercept:

$$
\log\left(\frac{p}{1-p}\right)=\beta_0
$$

Najlepsze $p$ w modelu zerowym to odsetek jedynek:

$$
\hat p=\bar y
$$

Log-likelihood modelu zerowego oznaczmy:

$$
\ell_0
$$

Log-likelihood modelu pełnego:

$$
\ell_1
$$

Model pełny powinien mieć:

$$
\ell_1\ge \ell_0
$$

bo ma więcej możliwości dopasowania.

---

## 21. McFadden pseudo-$R^2$

W regresji logistycznej klasyczne $R^2$ z $SSE$ nie działa tak jak w regresji liniowej. Często używa się McFadden pseudo-$R^2$:

$$
R^2_{McFadden}=1-\frac{\ell_1}{\ell_0}
$$

Równoważnie:

$$
R^2_{McFadden}=\frac{\ell_0-\ell_1}{\ell_0}
$$

Uwaga: zwykle $\ell_0<0$ i $\ell_1<0$, więc trzeba uważać z intuicją znaków.

---

## 22. Deviance

Dla binarnej regresji logistycznej często zapisujemy:

$$
Deviance=-2\ell(\hat\beta)
$$

W szerszym sensie deviance to różnica względem modelu nasyconego:

$$
D=2(\ell_{sat}-\ell_{model})
$$

Dla danych $0/1$ model nasycony może dać $p_i=1$ dla $y_i=1$ i $p_i=0$ dla $y_i=0$, więc jego log-likelihood jest $0$. Wtedy:

$$
D=-2\ell_{model}
$$

---

## 23. Test likelihood-ratio

Porównujemy model zredukowany i model pełny:

$$
G^2=2(\ell_{full}-\ell_{reduced})
$$

Przy warunkach asymptotycznych:

$$
G^2\sim \chi^2_{df}
$$

Stopnie swobody:

$$
df=k_{full}-k_{reduced}
$$

gdzie $k$ to liczba parametrów.

Dla modelu z jedną zmienną względem modelu zerowego:

$$
df=1
$$

---

## 24. Wald test w regresji logistycznej

Dla pojedynczego współczynnika:

$$
z=\frac{\hat\beta_j}{SE(\hat\beta_j)}
$$

Hipoteza zerowa:

$$
H_0:\beta_j=0
$$

Interpretacja:

- $\beta_j=0$ oznacza $e^{\beta_j}=1$,
- czyli odds ratio równe $1$,
- czyli brak zmiany odds po zmianie cechy.

**Ważna uwaga:** Wald test bywa niestabilny przy małych próbkach, rzadkich zdarzeniach i separacji. Wtedy często lepiej patrzeć na likelihood-ratio test albo dokładniejsze metody.

---

# Część VIII. Saturated model i deviance residuals

## 25. Saturated model

Model nasycony ma tyle elastyczności, że dopasowuje każdą obserwację idealnie.

Dla danych binarnych:

- jeśli $y_i=1$, model nasycony daje $\hat p_i=1$,
- jeśli $y_i=0$, model nasycony daje $\hat p_i=0$.

To daje log-likelihood równy $0$.

Zwykły model logistyczny prawie nigdy nie dopasowuje tak idealnie, więc ma log-likelihood mniejszy od $0$.

---

## 26. Deviance residuals

Deviance residual dla obserwacji binarnej można intuicyjnie traktować jako podpisany wkład obserwacji do deviance.

Dla $y_i\in\{0,1\}$:

$$
r_i=sign(y_i-\hat p_i)\sqrt{2\left[y_i\log\left(\frac{y_i}{\hat p_i}\right)+(1-y_i)\log\left(\frac{1-y_i}{1-\hat p_i}\right)\right]}
$$

Z konwencją:

$$
0\log(0/q)=0
$$

Dla praktycznego wykładu wystarczy intuicja:

- duży dodatni residual: model dał małe $p$, ale obserwacja ma $y=1$,
- duży ujemny residual: model dał duże $p$, ale obserwacja ma $y=0$.

---

# Część IX. ROC/AUC i próg decyzyjny

## 27. Probability score to nie jest jeszcze klasa

Regresja logistyczna zwraca score:

$$
\hat p=P(y=1|x)
$$

Klasa zależy od progu $t$:

$$
\hat y=I(\hat p\ge t)
$$

Zmiana progu zmienia confusion matrix.

---

## 28. Confusion matrix

| | przewidziane 1 | przewidziane 0 |
|---|---:|---:|
| prawdziwe 1 | TP | FN |
| prawdziwe 0 | FP | TN |

Miary:

$$
TPR=Recall=\frac{TP}{TP+FN}
$$

$$
FPR=\frac{FP}{FP+TN}
$$

ROC rysuje:

$$
TPR \quad \text{vs} \quad FPR
$$

przy różnych progach.

---

## 29. Intuicja AUC

AUC można interpretować jako prawdopodobieństwo, że losowo wybrany pozytywny przykład dostanie wyższy score niż losowo wybrany negatywny przykład:

$$
AUC=P(score^+>score^-)+\frac{1}{2}P(score^+=score^-)
$$

Wartości:

- $AUC=0.5$ — ranking jak losowy,
- $AUC=1.0$ — perfekcyjny ranking,
- $AUC<0.5$ — model zwykle odwraca klasy.

**Pułapka dydaktyczna:** AUC nie mówi, jaki próg jest najlepszy. AUC ocenia ranking, a próg dobieramy osobno.

---

# Część X. Regularizacja

## 30. Po co karać współczynniki?

Modele z wieloma cechami mogą:

- mieć niestabilne współczynniki,
- przeuczać się,
- źle działać przy skorelowanych cechach,
- dawać ogromne współczynniki przy separacji klas.

Regularizacja dodaje karę do funkcji celu.

Dla regresji logistycznej minimalizujemy zwykle negative log-likelihood plus kara:

$$
J(\beta)=-\ell(\beta)+\lambda\cdot penalty(\beta)
$$

---

## 31. Ridge / L2

$$
penalty_{L2}=\sum_{j=1}^{p}\beta_j^2
$$

Ridge zmniejsza współczynniki, ale zwykle nie zeruje ich dokładnie.

Intuicja geometryczna: ograniczenie L2 to kula/okrąg.

---

## 32. Lasso / L1

$$
penalty_{L1}=\sum_{j=1}^{p}|\beta_j|
$$

Lasso może wyzerować część współczynników, więc działa jak prosta selekcja cech.

Intuicja geometryczna: ograniczenie L1 to romb z narożnikami na osiach; optimum często trafia w narożnik, czyli jeden współczynnik jest zerowy.

---

## 33. Elastic Net

$$
penalty_{EN}=\alpha\sum_{j=1}^{p}|\beta_j|+(1-\alpha)\sum_{j=1}^{p}\beta_j^2
$$

Łączy L1 i L2.

- L1 daje sparsity,
- L2 stabilizuje przy skorelowanych cechach,
- Elastic Net jest kompromisem.

---

# Część XI. Kod Python — obliczenia bez `statsmodels`

Poniższy kod można wkleić do notebooka. Celowo nie używa `statsmodels`, żeby uniknąć problemu z niekompatybilnością starszych wersji `statsmodels` i nowszego NumPy.

## 34. Probability, odds, log-odds

```python
import numpy as np
import pandas as pd
from scipy import stats
from scipy.special import expit

p = np.array([0.1, 0.25, 0.5, 0.75, 0.9])
odds = p / (1 - p)
log_odds = np.log(odds)

pd.DataFrame({
    "p": p,
    "odds": odds,
    "log_odds": log_odds,
})
```

## 35. Odds ratio, Wald, Fisher i chi-square

```python
from math import comb
from scipy.stats import fisher_exact, chi2_contingency, chi2, norm, hypergeom

# Tabela: rows = mutation +/-, cols = cancer +/−
a, b, c, d = 23, 117, 6, 210
obs = np.array([[a, b], [c, d]])

or_hat = (a * d) / (b * c)
log_or = np.log(or_hat)
se_log_or = np.sqrt(1/a + 1/b + 1/c + 1/d)
z = log_or / se_log_or
p_wald = 2 * norm.sf(abs(z))
ci_log = (log_or - 1.96 * se_log_or, log_or + 1.96 * se_log_or)
ci_or = tuple(np.exp(ci_log))

print("OR =", or_hat)
print("log(OR) =", log_or)
print("SE log(OR) =", se_log_or)
print("z =", z)
print("p Wald =", p_wald)
print("95% CI OR =", ci_or)

# Fisher exact test
print("Fisher:", fisher_exact(obs, alternative="two-sided"))

# Chi-square ręcznie + scipy
row_sums = obs.sum(axis=1, keepdims=True)
col_sums = obs.sum(axis=0, keepdims=True)
expected = row_sums @ col_sums / obs.sum()
chi2_stat = ((obs - expected) ** 2 / expected).sum()
p_chi = chi2.sf(chi2_stat, df=1)

print("expected =")
print(expected)
print("chi2 =", chi2_stat)
print("p chi2 =", p_chi)
print("scipy chi2:", chi2_contingency(obs, correction=False))
```

## 36. Fisher exact test ręcznie przez rozkład hipergeometryczny

```python
M = obs.sum()
n = obs[0].sum()       # pierwszy wiersz
N = obs[:, 0].sum()    # pierwsza kolumna
start, end = hypergeom.support(M, n, N)
xs = np.arange(start, end + 1)
pmf = hypergeom.pmf(xs, M, n, N)

observed_prob = hypergeom.pmf(a, M, n, N)
two_sided_p = pmf[pmf <= observed_prob + 1e-12].sum()

pd.DataFrame({"x_upper_left": xs, "probability": pmf}).head(), observed_prob, two_sided_p
```

## 37. Regresja logistyczna na tabeli `sex` z demo heart disease

```python
# Dane zagregowane z demo StatQuest:
# Female: Healthy 71, Unhealthy 25
# Male:   Healthy 89, Unhealthy 112

rows = []
for sexM, healthy, unhealthy in [(0, 71, 25), (1, 89, 112)]:
    rows += [(sexM, 0)] * healthy
    rows += [(sexM, 1)] * unhealthy

df = pd.DataFrame(rows, columns=["sexM", "unhealthy"])
X = np.column_stack([np.ones(len(df)), df["sexM"].to_numpy()])
y = df["unhealthy"].to_numpy()

# Newton-Raphson / IRLS dla log-likelihood
beta = np.zeros(X.shape[1])
for iteration in range(30):
    eta = X @ beta
    p = expit(eta)
    W = p * (1 - p)
    grad = X.T @ (y - p)
    H_pos = X.T @ (W[:, None] * X)   # -Hessian loglikelihood
    step = np.linalg.solve(H_pos, grad)
    beta = beta + step
    if np.max(np.abs(step)) < 1e-10:
        break

beta
```

Spodziewamy się wartości około:

$$
\beta_0=\log(25/71)\approx -1.0438
$$

$$
\beta_1=\log\left(\frac{112/89}{25/71}\right)\approx 1.2737
$$

```python
manual_intercept = np.log(25/71)
manual_slope = np.log((112/89)/(25/71))
print(manual_intercept, manual_slope)

probs = expit(np.array([[1,0], [1,1]]) @ beta)
print("P(Unhealthy | F) =", probs[0])
print("P(Unhealthy | M) =", probs[1])
print("OR male vs female =", np.exp(beta[1]))
```

## 38. Log-likelihood, pseudo-$R^2$ i LRT

```python
def log_likelihood(X, y, beta):
    eta = X @ beta
    # stabilna forma: sum y*eta - log(1+exp(eta))
    return np.sum(y * eta - np.logaddexp(0, eta))

ll_full = log_likelihood(X, y, beta)

# model zerowy: tylko intercept
X0 = np.ones((len(y), 1))
beta0 = np.array([np.log(y.mean() / (1-y.mean()))])
ll_null = log_likelihood(X0, y, beta0)

mcfadden = 1 - ll_full / ll_null
G2 = 2 * (ll_full - ll_null)
p_lrt = chi2.sf(G2, df=1)

print("LL null =", ll_null)
print("LL full =", ll_full)
print("McFadden pseudo-R^2 =", mcfadden)
print("G^2 =", G2)
print("p LRT =", p_lrt)
```

## 39. ROC/AUC ręcznie

```python
# Mały przykład score'ów z klasyfikatora
scores = np.array([0.95, 0.80, 0.70, 0.60, 0.55, 0.40, 0.35, 0.20])
y_true = np.array([1,    1,    0,    1,    0,    0,    1,    0])

thresholds = np.r_[np.inf, np.sort(scores)[::-1], -np.inf]
roc_rows = []
for t in thresholds:
    y_pred = (scores >= t).astype(int)
    TP = np.sum((y_true == 1) & (y_pred == 1))
    FP = np.sum((y_true == 0) & (y_pred == 1))
    TN = np.sum((y_true == 0) & (y_pred == 0))
    FN = np.sum((y_true == 1) & (y_pred == 0))
    TPR = TP / (TP + FN)
    FPR = FP / (FP + TN)
    roc_rows.append((t, TP, FP, TN, FN, TPR, FPR))

roc_df = pd.DataFrame(roc_rows, columns=["threshold", "TP", "FP", "TN", "FN", "TPR", "FPR"])
roc_df
```

```python
# AUC przez interpretację par dodatni-negatywny
pos_scores = scores[y_true == 1]
neg_scores = scores[y_true == 0]
count = 0
for ps in pos_scores:
    for ns in neg_scores:
        if ps > ns:
            count += 1
        elif ps == ns:
            count += 0.5
auc_pairwise = count / (len(pos_scores) * len(neg_scores))
auc_pairwise
```

## 40. Regularizacja logistyczna w `scikit-learn`

```python
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

# Przykład szkieletu — zwykle najpierw standaryzujemy cechy.
model_l2 = make_pipeline(
    StandardScaler(),
    LogisticRegression(penalty="l2", C=1.0, solver="lbfgs", max_iter=1000)
)

model_l1 = make_pipeline(
    StandardScaler(),
    LogisticRegression(penalty="l1", C=1.0, solver="saga", max_iter=5000)
)

model_en = make_pipeline(
    StandardScaler(),
    LogisticRegression(penalty="elasticnet", C=1.0, l1_ratio=0.5, solver="saga", max_iter=5000)
)
```

Pamiętaj:

- mniejsze $C$ w `sklearn` oznacza silniejszą regularizację,
- większe $\lambda$ w zapisie matematycznym oznacza silniejszą regularizację,
- dlatego $C$ jest odwrotnością siły regularizacji.

---

# Część XII. Kod R — styl StatQuest

Poniższy szkic odpowiada logice demo StatQuest z repozytorium `logistic_regression_demo.R`: pobranie danych Cleveland, nazwanie kolumn, zamiana zmiennych jakościowych na faktory, usunięcie kilku braków, kontrola `xtabs`, prosty model `hd ~ sex`, potem model `hd ~ .`.

```r
library(ggplot2)
library(cowplot)

url <- "https://raw.githubusercontent.com/StatQuest/logistic_regression_demo/master/processed.cleveland.data"
data <- read.csv(url, header=FALSE)

colnames(data) <- c(
  "age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
  "thalach", "exang", "oldpeak", "slope", "ca", "thal", "hd"
)

data[data == "?"] <- NA

data[data$sex == 0,]$sex <- "F"
data[data$sex == 1,]$sex <- "M"
data$sex <- as.factor(data$sex)

data$cp <- as.factor(data$cp)
data$fbs <- as.factor(data$fbs)
data$restecg <- as.factor(data$restecg)
data$exang <- as.factor(data$exang)
data$slope <- as.factor(data$slope)

data$ca <- as.integer(data$ca)
data$ca <- as.factor(data$ca)
data$thal <- as.integer(data$thal)
data$thal <- as.factor(data$thal)

data$hd <- ifelse(data$hd == 0, "Healthy", "Unhealthy")
data$hd <- as.factor(data$hd)

data <- data[!(is.na(data$ca) | is.na(data$thal)),]

xtabs(~ hd + sex, data=data)

logistic <- glm(hd ~ sex, data=data, family="binomial")
summary(logistic)

female.log.odds <- log(25 / 71)
male.log.odds.ratio <- log((112 / 89) / (25 / 71))

ll.null <- logistic$null.deviance / -2
ll.proposed <- logistic$deviance / -2
pseudo.r2 <- (ll.null - ll.proposed) / ll.null
p.value <- 1 - pchisq(2 * (ll.proposed - ll.null), df=1)

pseudo.r2
p.value

logistic.full <- glm(hd ~ ., data=data, family="binomial")
summary(logistic.full)
```

---

# Część XIII. Proste ćwiczenia do prowadzenia na tablicy

## Ćwiczenie 1: probability vs odds

W klasie jest $30$ osób. $6$ zdało bardzo trudny test, $24$ nie zdały.

1. Policz probability zdania.
2. Policz odds zdania.
3. Policz log-odds zdania.

**Rozwiązanie:**

$$
p=6/30=0.2
$$

$$
odds=6/24=0.25
$$

$$
\log(odds)=\log(0.25)\approx -1.386
$$

---

## Ćwiczenie 2: od log-odds do probability

Model daje:

$$
\eta=-2,\quad 0,\quad 2
$$

Policz probability.

**Rozwiązanie:**

$$
p=\frac{1}{1+e^{-\eta}}
$$

Dla $\eta=-2$:

$$
p\approx 0.119
$$

Dla $\eta=0$:

$$
p=0.5
$$

Dla $\eta=2$:

$$
p\approx 0.881
$$

---

## Ćwiczenie 3: odds ratio

| grupa | Choroba + | Choroba - |
|---|---:|---:|
| Ekspozycja + | 10 | 20 |
| Ekspozycja - | 5 | 25 |

Policz $OR$ i $\log(OR)$.

**Rozwiązanie:**

$$
OR=\frac{10\cdot25}{20\cdot5}=2.5
$$

$$
\log(OR)=\log(2.5)\approx 0.916
$$

---

## Ćwiczenie 4: współczynnik logistyczny jako odds ratio

W modelu:

$$
\log\left(\frac{p}{1-p}\right)=-1+0.7x
$$

co oznacza $0.7$?

**Odpowiedź:**

Przy wzroście $x$ o $1$ log-odds rosną o $0.7$, a odds mnożą się przez:

$$
e^{0.7}\approx 2.01
$$

---

## Ćwiczenie 5: intercept i predykcja

Model:

$$
\log\left(\frac{p}{1-p}\right)=-1+2x
$$

Policz $p$ dla $x=0$ i $x=1$.

**Rozwiązanie:**

Dla $x=0$:

$$
\eta=-1
$$

$$
p=\frac{1}{1+e^1}\approx 0.269
$$

Dla $x=1$:

$$
\eta=1
$$

$$
p=\frac{1}{1+e^{-1}}\approx 0.731
$$

---

## Ćwiczenie 6: Wald test na małych liczbach

Dla tabeli:

| grupa | Choroba + | Choroba - |
|---|---:|---:|
| A | 10 | 20 |
| B | 5 | 25 |

Policz:

$$
SE=\sqrt{1/10+1/20+1/5+1/25}
$$

$$
z=\frac{\log(2.5)}{SE}
$$

**Rozwiązanie:**

$$
SE=\sqrt{0.1+0.05+0.2+0.04}=\sqrt{0.39}\approx 0.624
$$

$$
z=0.916/0.624\approx 1.47
$$

Wynik nie przekracza reguły $|z|\approx2$, więc nie mamy mocnego sygnału przy poziomie około $0.05$.

---

## Ćwiczenie 7: próg decyzyjny

Model daje probability:

| osoba | score | prawda |
|---:|---:|---:|
| 1 | 0.90 | 1 |
| 2 | 0.70 | 0 |
| 3 | 0.60 | 1 |
| 4 | 0.40 | 0 |

Policz confusion matrix dla progu $t=0.5$.

**Rozwiązanie:**

Predykcje: $1,1,1,0$.

- TP: osoby 1 i 3, czyli $2$,
- FP: osoba 2, czyli $1$,
- TN: osoba 4, czyli $1$,
- FN: $0$.

---

# Część XIV. GeoGebra — wersja opisowa i komendy

## 41. Demo 1: sigmoid i logit

Cel: student widzi, że linia na skali log-odds po transformacji daje krzywą S.

### Instrukcja tekstowa

1. Utwórz suwaki `b0` i `b1`.
2. Zdefiniuj liniowy score:

   $$
   eta(x)=b0+b1x
   $$

3. Zdefiniuj sigmoidę:

   $$
   p(x)=1/(1+exp(-eta(x)))
   $$

4. Zmieniaj `b0` i `b1`:
   - `b0` przesuwa punkt, gdzie $p=0.5$,
   - `b1` zmienia stromość krzywej.

### GeoGebra-like commands

```text
b0 = Slider(-5, 5, 0.1)
b1 = Slider(-5, 5, 0.1)
eta(x) = b0 + b1 x
p(x) = 1 / (1 + exp(-eta(x)))
f = Function(p, -10, 10)
line_eta = Function(eta, -10, 10)
A = (0, 0.5)
```

---

## 42. Demo 2: odds i log-odds

### Instrukcja tekstowa

1. Utwórz suwak `prob` od $0.01$ do $0.99$.
2. Policz odds i log-odds.
3. Pokaż, że dla $p=0.5$ odds wynoszą $1$, a log-odds wynosi $0$.

### GeoGebra-like commands

```text
prob = Slider(0.01, 0.99, 0.01)
odds = prob / (1 - prob)
logodds = ln(odds)
A = (prob, odds)
B = (prob, logodds)
odds_fun(x) = x / (1 - x)
logit_fun(x) = ln(x / (1 - x))
Function(odds_fun, 0.01, 0.99)
Function(logit_fun, 0.01, 0.99)
```

---

## 43. Demo 3: L1 vs L2

### Instrukcja tekstowa

1. Narysuj okrąg L2:

   $$
   b_1^2+b_2^2=r^2
   $$

2. Narysuj romb L1:

   $$
   |b_1|+|b_2|=r
   $$

3. Pokaż, że romb ma narożniki na osiach, więc łatwiej o $b_j=0$.

### GeoGebra-like commands

```text
r = Slider(0.5, 5, 0.1)
L2 = x^2 + y^2 = r^2
A = (r, 0)
B = (0, r)
C = (-r, 0)
D = (0, -r)
L1 = Polygon(A, B, C, D)
```

---

# Część XV. Najważniejsze pułapki dydaktyczne

1. **Probability i odds to nie to samo.**  
   Probability dzieli przez wszystkie przypadki, odds dzielą sukcesy przez porażki.

2. **Regresja logistyczna nie jest liniowa na skali probability.**  
   Jest liniowa na skali log-odds.

3. **Współczynniki nie są zmianą probability.**  
   $\beta_j$ jest zmianą log-odds, a $e^{\beta_j}$ jest mnożnikiem odds.

4. **Threshold to osobna decyzja.**  
   Model daje score/probability. Próg dobieramy do celu.

5. **AUC nie wybiera progu.**  
   AUC mierzy ranking, nie konkretną confusion matrix.

6. **Wald test nie zawsze jest najlepszy.**  
   Przy małych próbkach, rzadkich zdarzeniach i separacji może być mylący.

7. **Regularizacja wymaga skalowania cech.**  
   Bez standaryzacji kara L1/L2 zależy od jednostek pomiaru.

8. **Przy kategoriach trzeba uważać na kodowanie.**  
   Kodowanie $1,2,3,4$ może sztucznie narzucić porządek i odległości.

---

# Część XVI. Mini-scenariusz prowadzenia 90 minut

## Blok 1: 15 minut — od linear do design matrix

- pokaż $y=X\beta+\varepsilon$,
- pokaż regresję, t-test i ANOVA jako różne $X$,
- ćwiczenie: zbuduj design matrix dla dwóch grup.

## Blok 2: 20 minut — odds, log-odds, OR

- probability vs odds na przykładzie 5 meczów,
- log-odds jako symetryzacja,
- tabela mutacja/rak,
- $OR$, $\log(OR)$, Wald.

## Blok 3: 25 minut — logistic regression

- pokaż, dlaczego OLS nie wystarcza,
- przejście:

  $$
  p\to odds\to log(odds)=X\beta\to p=\sigma(X\beta)
  $$

- interpretacja współczynników na przykładzie `sex` i heart disease.

## Blok 4: 15 minut — likelihood, deviance, pseudo-$R^2$

- likelihood dla $y=1$ i $y=0$,
- log-likelihood,
- model zerowy vs pełny,
- likelihood-ratio test.

## Blok 5: 15 minut — ROC/AUC i regularizacja

- threshold i confusion matrix,
- ROC jako różne progi,
- AUC jako ranking,
- L2/L1/Elastic Net jako kara na współczynniki.

---

# Część XVII. Źródła i inspiracje

- StatQuest playlist / video index: Linear Models, Odds, Logistic Regression, ROC/AUC, Regularization.
- StatQuest `logistic_regression_demo.R`: przykład Cleveland Heart Disease, `glm(hd ~ sex, family="binomial")`, interpretacja interceptu i `sexM`, McFadden pseudo-$R^2$ oraz test chi-square przez różnicę deviance.
- SciPy documentation: `fisher_exact` i `chi2_contingency`.
- scikit-learn documentation: `LogisticRegression`, `roc_auc_score`.

