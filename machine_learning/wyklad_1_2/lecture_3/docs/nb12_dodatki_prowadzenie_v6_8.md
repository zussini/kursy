# Notebook 12 — co dorobiłem, żeby łatwiej prowadzić zajęcia

Najbardziej sensowne dodatki do notebooka 12 to nie nowe duże obliczenia, tylko małe „prowadnice” dydaktyczne.

## 1. Mapa notebooka na początku

Dodałem krótkie wyjaśnienie, że notebook 12 jest statystycznym domknięciem regresji logistycznej:

- log-likelihood,
- deviance,
- AIC,
- McFadden pseudo-$R^2$,
- likelihood-ratio test,
- Wald test,
- deviance residuals,
- separacja i regularizacja.

## 2. Mini-przypomnienie: czym to się różni od ROC/AUC

ROC/AUC ocenia ranking score'ów i progi.

Notebook 12 pyta o coś innego:

$$
\ell_{full} > \ell_{reduced}
$$

czyli: czy model pełniejszy ma istotnie większy log-likelihood.

## 3. Tabela postępu modeli

Po tabeli modeli dodałem tabelę:

- różnica deviance względem poprzedniego modelu,
- różnica AIC względem poprzedniego modelu.

To pomaga mówić:

> Dodaliśmy zmienną. Czy model naprawdę się poprawił?

## 4. LRT vs AIC vs Wald

Dodałem krótkie rozróżnienie:

- LRT — porównuje dwa modele zagnieżdżone,
- AIC — szybkie kryterium modelu z karą za złożoność,
- Wald — testuje pojedynczy współczynnik.

## 5. Interpretacja `exp(coef)`

Dodałem przypomnienie:

$$
e^\beta
$$

to mnożnik odds, nie zmiana prawdopodobieństwa.

## 6. Deviance residuals jako „zaskakujące obserwacje”

Dodałem wykres deviance residuals i krótkie wyjaśnienie:

- duże dodatnie reszty: model dał niskie $p$, a było $y=1$,
- duże ujemne reszty: model dał wysokie $p$, a było $y=0$.

## 7. Skrypt prowadzenia

Dodałem sekcję z gotową kolejnością mówienia na zajęciach.

Najważniejsze zdanie:

> W regresji logistycznej porównujemy modele nie przez $SSE$, tylko przez log-likelihood i deviance.
