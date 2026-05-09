# Ćwiczenia: Titanic i Tips

## Titanic 1 — odds ratio

Policz ręcznie:

$$
odds_{female}=\frac{survived_{female}}{died_{female}}
$$

$$
odds_{male}=\frac{survived_{male}}{died_{male}}
$$

$$
OR=\frac{odds_{female}}{odds_{male}}
$$

Następnie policz $\log(OR)$ i porównaj z współczynnikiem modelu logistycznego `survived ~ female`.

## Titanic 2 — threshold

Dla progów $0.3$, $0.5$, $0.7$ policz:

- TP,
- FP,
- TN,
- FN,
- recall,
- precision.

Który próg wybierasz, jeśli false negative jest drogie?

## Titanic 3 — leakage

Dodaj kolumnę `alive_yes_LEAK`.

Odpowiedz:

1. Dlaczego AUC wzrosło?
2. Dlaczego to nie jest uczciwy model?
3. Jak rozpoznać podobny błąd w realnych danych?

## Tips 1 — regresja liniowa

Dopasuj:

$$
\widehat{tip}=\beta_0+\beta_1 total\_bill
$$

Policz $R^2$ i RMSE.

## Tips 2 — klasyfikacja

Zdefiniuj:

$$
large\_tip=1 \quad \text{gdy} \quad tip \ge 3.00
$$

Dopasuj model bez `tip`.

Następnie dodaj `tip` i sprawdź leakage.

## Tips 3 — dyskusja

Czy przewidywanie napiwków jest neutralnym problemem? Jakie zmienne mogą być problematyczne etycznie lub interpretacyjnie?
