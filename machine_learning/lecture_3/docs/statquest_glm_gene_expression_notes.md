# StatQuest-style GLM: ekspresja genu, design matrix, t-test i ANOVA

## Co dodaje ten moduł

Ten moduł jest pomostem między wykładem o regresji liniowej a przyszłymi tematami: regresją logistyczną, LDA/QDA i modelami probabilistycznymi. Pokazuje, że t-test i ANOVA można przedstawić jako szczególne przypadki modelu liniowego.

Główna intuicja:

> W regresji liniowej dopasowujemy prostą. W t-teście dopasowujemy dwie średnie. W ANOVA dopasowujemy wiele średnich. W każdym przypadku minimalizujemy sumę kwadratów reszt i możemy porównać model prostszy z modelem pełniejszym przez test F.

## Mini-przykład: Control vs Mutant

Dane dydaktyczne:

| grupa | ekspresja |
|---|---:|
| Control | 1.7 |
| Control | 2.1 |
| Control | 2.3 |
| Control | 2.7 |
| Mutant | 3.1 |
| Mutant | 3.4 |
| Mutant | 3.7 |
| Mutant | 4.2 |

Średnie:

- Control: 2.2,
- Mutant: 3.6,
- ogólna: 2.9.

## Model zerowy

Model zerowy przewiduje jedną średnią dla wszystkich myszy:

\[
\hat y_i = \bar y
\]

Liczba parametrów:

\[
p_{mean}=1
\]

Suma kwadratów reszt:

\[
SSE_{mean}=\sum_i(y_i-\bar y)^2
\]

Dla danych powyżej:

\[
SSE_{mean}=5.10
\]

## Model dopasowany: dwie średnie

Model dopasowany przewiduje osobną średnią dla każdej grupy:

\[
\hat y_i = I(Control)\mu_C + I(Mutant)\mu_M
\]

Macierz projektu:

\[
X=\begin{bmatrix}
1&0\\
1&0\\
1&0\\
1&0\\
0&1\\
0&1\\
0&1\\
0&1
\end{bmatrix}
\]

Parametry:

\[
\mu_C=2.2, \quad \mu_M=3.6
\]

Liczba parametrów:

\[
p_{fit}=2
\]

Suma kwadratów reszt:

\[
SSE_{fit}=1.18
\]

## Test F

Porównanie modelu prostego i pełniejszego:

\[
F=\frac{(SSE_{simple}-SSE_{full})/(p_{full}-p_{simple})}{SSE_{full}/(n-p_{full})}
\]

W przykładzie:

\[
F=\frac{(5.10-1.18)/(2-1)}{1.18/(8-2)}\approx 19.93
\]

p-value liczymy z rozkładu F o stopniach swobody:

\[
df_1=p_{fit}-p_{mean}=1
\]

\[
df_2=n-p_{fit}=6
\]

## Ważny fakt: przy dwóch grupach F = t²

Dla dwóch grup jednoczynnikowa ANOVA i t-test z założeniem równej wariancji są równoważne:

\[
F=t^2
\]

To bardzo dobry moment dydaktyczny: studenci widzą, że wiele „oddzielnych” testów statystycznych można opowiedzieć jednym językiem modeli liniowych.

## Standardowy zapis z interceptem

Model z dwiema kolumnami `Control`, `Mutant` jest czytelny dydaktycznie, ale w praktyce częściej spotyka się zapis:

\[
\hat y = \beta_0 + \beta_1 I(Mutant)
\]

Wtedy:

- \(\beta_0\) = średnia grupy Control,
- \(\beta_1\) = różnica `Mutant - Control`.

Dla danych:

\[
\beta_0=2.2
\]

\[
\beta_1=1.4
\]

Predykcje są identyczne jak w modelu z dwiema kolumnami. Różni się tylko interpretacja współczynników.

## ANOVA jako model z wieloma średnimi

Dla pięciu grup model ma pięć parametrów — po jednej średniej na grupę:

\[
\hat y_i = I(g_1)\mu_1 + I(g_2)\mu_2 + I(g_3)\mu_3 + I(g_4)\mu_4 + I(g_5)\mu_5
\]

Test F odpowiada na pytanie:

> Czy model z pięcioma średnimi jest istotnie lepszy niż model z jedną średnią ogólną?

## Rozszerzenie: ekspresja genu i masa myszy

Praktyczny model:

\[
\widehat{expression}=\beta_0+\beta_1 weight+\beta_2 I(Mutant)
\]

Interpretacja:

- \(\beta_1\): o ile średnio zmienia się ekspresja przy wzroście masy o 1 jednostkę, przy stałym genotypie,
- \(\beta_2\): o ile średnio różni się ekspresja u Mutant względem Control, przy tej samej masie.

To chroni przed prostą pułapką: jeśli mutanty są cięższe, a ekspresja zależy od masy, samo porównanie średnich może mieszać efekt genotypu z efektem masy.

## Prosty skrypt słowny na wykład

1. „Najpierw udajemy, że grup nie ma — przewidujemy jedną średnią.”
2. „Potem pozwalamy modelowi mieć osobną średnią dla każdej grupy.”
3. „Jeśli druga wersja znacznie zmniejsza sumę kwadratów reszt, grupa coś wyjaśnia.”
4. „Design matrix to tylko sposób, żeby komputer wiedział, który parametr włączyć dla której obserwacji.”
5. „Regresja, t-test i ANOVA mają ten sam mechanizm: model prostszy kontra model pełniejszy.”

## Pliki w pakiecie

- `notebooks/09_statquest_glm_gene_expression_design_matrix.ipynb`
- `data/statquest_style_gene_expression_ttest.csv`
- `data/statquest_style_gene_expression_anova.csv`
- `data/statquest_style_gene_expression_weight.csv`
- `docs/statquest_glm_gene_expression_exercises_with_solutions.md`
- `docs/geogebra_gene_expression_glm_commands.txt`
