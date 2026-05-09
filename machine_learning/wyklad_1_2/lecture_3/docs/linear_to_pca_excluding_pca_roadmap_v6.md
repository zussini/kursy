
# Draft v6: od modeli liniowych do PCA — bez PCA na razie

Zakres przygotowany w tej wersji obejmuje blok przed PCA, ze szczególnym naciskiem na:

1. modele liniowe i design matrix,
2. t-test i ANOVA jako przypadki modelu liniowego,
3. probability vs likelihood, maximum likelihood,
4. odds, log-odds, odds ratio,
5. Fisher, chi-square, Wald,
6. regresję logistyczną,
7. deviance, pseudo-$R^2$, likelihood-ratio test,
8. ROC/AUC, progi decyzyjne i macierz pomyłek,
9. regularyzację Ridge, Lasso i Elastic Net.

## Mapa notebooków

| Notebook | Temat | Główna intuicja |
|---|---|---|
| `08_linear_regression_lecture_v4_statquest_glm.ipynb` | regresja liniowa, $R^2$, $F$ | jedna linia, reszty, SSE, porównanie modeli |
| `09_glm_design_matrix_ttest_anova_v6_statsmodels_free.ipynb` | design matrix, t-test, ANOVA | t-test i ANOVA to regresja z innym $X$ |
| `10_odds_log_odds_or_fisher_chisquare_wald_v6_statsmodels_free.ipynb` | odds, OR, Fisher, chi-square, Wald | $\log(OR)$ łączy tabelę 2×2 z logistyczną |
| `11_logistic_regression_likelihood_v6.ipynb` | logistyczna od zera | modelujemy log-odds, fitujemy likelihood |
| `12_logistic_regression_deviance_model_tests_v6.ipynb` | deviance, pseudo-$R^2$, LRT | porównujemy log-likelihoody, nie SSE |
| `13_roc_auc_thresholds_v6.ipynb` | ROC/AUC i progi | AUC mierzy ranking, próg robi decyzję |
| `14_regularization_ridge_lasso_elasticnet_v6.ipynb` | Ridge/Lasso/Elastic Net | kara stabilizuje model i ogranicza overfitting |

## Błąd `np.MachAr` / `statsmodels`

Wersja v6 nie używa `statsmodels`. Poprzedni błąd wynikał z niezgodności wersji: starszy `statsmodels` może odwoływać się do `np.MachAr`, którego nie ma w nowszych NumPy. W notebookach v6 wszystkie obliczenia są ręczne albo oparte na `numpy`, `scipy` i opcjonalnie `scikit-learn`.

## Proponowana kolejność dydaktyczna

### Lekcja 1: design matrix

Najpierw pokazujemy, że model liniowy to tylko $y=X\beta+\varepsilon$. Potem pokazujemy trzy macierze:

- intercept only: jedna średnia,
- intercept + 0/1: t-test,
- one-hot: ANOVA.

### Lekcja 2: odds i tabela 2×2

Najpierw $p$, potem odds, potem $\log(odds)$, potem odds ratio. Dopiero po tym regresja logistyczna.

### Lekcja 3: likelihood

Pokazujemy, że dla klasyfikacji binarnej nie minimalizujemy $SSE$, tylko maksymalizujemy likelihood Bernoulliego.

### Lekcja 4: logistyczna jako GLM

Pokazujemy sigmoid, interpretację $\exp(\beta)$ oraz porównywanie modeli przez LRT/deviance.

### Lekcja 5: ROC/AUC

Pokazujemy, że probabilistyczny model nie ma jednego progu. AUC ocenia ranking, a threshold tuning jest oddzielną decyzją.

### Lekcja 6: regularyzacja

Ridge jako „mniejsze współczynniki”, Lasso jako „część współczynników może zniknąć”, Elastic Net jako kompromis. W logistycznej pokazujemy separację.
