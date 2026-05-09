
# GeoGebra v6 — instrukcje dydaktyczne

Poniżej są cztery krótkie demonstracje. Każdą można prowadzić jako 5–10 minutową wstawkę na wykładzie.

## 1. Design matrix / t-test / ANOVA

Cel: pokazać, że model z jedną średnią ma większe reszty niż model z dwiema średnimi.

Przebieg:

1. Wstaw punkty dla grup `Control` i `Mutant`.
2. Narysuj jedną średnią globalną.
3. Narysuj dwie średnie grupowe.
4. Porównaj długości pionowych reszt.
5. Powiedz: „dodanie kolumny w design matrix pozwoliło mieć osobny poziom dla Mutant”.

## 2. Odds/logit/logistic

Cel: suwakiem zmieniać $\beta_0$ i $\beta_1$ w funkcji:

$$
p(x)=\frac{1}{1+e^{-(\beta_0+\beta_1x)}}
$$

Pokazać, że liniowy jest logit, nie prawdopodobieństwo.

## 3. ROC/AUC

Cel: przesuwać próg i obserwować, jak zmieniają się $TPR$ i $FPR$.

Najprostsza wersja: punkty ROC są wpisane ręcznie jako lista, a studenci widzą schodkową krzywą.

## 4. Regularyzacja

Cel: porównać geometrię L2 i L1:

- L2: okrąg — gładki brzeg,
- L1: romb — ostre rogi, łatwiej trafić w oś i wyzerować współczynnik.
