# GeoGebra manifest v6.1

Pliki `.ggbscript.txt` są głównym, pewnym formatem pracy: są czytelne, edytowalne i można je wkleić do GeoGebry. Pliki `.ggb` są prototypami startowymi z obiektami i suwakami. Zrobiłem je w bardziej standardowej paczce `.ggb`, z `geogebra.xml`, `geogebra_defaults2d.xml`, `geogebra_defaults3d.xml` i `geogebra_javascript.js`.

## Kolejność użycia

1. `GG01_probability_odds_logit_v6_1` — probability, odds, log-odds.
2. `GG02_odds_ratio_2x2` — OR, logOR, SE i Wald na tabeli 2×2.
3. `GG03_logistic_curve_threshold` — sigmoid, beta0, beta1, próg.
4. `GG04_logistic_likelihood_points` — log-likelihood dla kilku punktów.
5. `GG05_ROC_threshold_sweep` — próg, TPR, FPR, punkt ROC.
6. `GG06_regularization_l1_l2_geometry` — geometria Ridge/Lasso.

## Uwagi techniczne

GeoGebra różnie zachowuje się między wersjami przy imporcie gotowych `.ggb`, dlatego w razie problemu użyj odpowiadającego pliku `.ggbscript.txt`. To jest najbardziej kontrolowalna forma dla zajęć.
