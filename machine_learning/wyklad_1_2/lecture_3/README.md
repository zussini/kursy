# Universal ML Teaching Pack

Spójny pakiet analityczno-dydaktyczny do nauki:

- KNN
- drzew decyzyjnych
- PCA
- SVM
- Random Forest / Gradient Boosting
- XGBoost jako moduł opcjonalny
- manifold learning jako most do embeddingów i latent space

Pakiet jest zbudowany tak, aby **te same zbiory danych i te same funkcje** były używane w kolejnych lekcjach. Dzięki temu student nie uczy się ciągle nowego środowiska, tylko widzi, jak zmienia się sposób patrzenia modelu na te same dane.

---

## Instalacja

```bash
cd ml_universal_teaching_pack
pip install -r requirements.txt
```

Opcjonalnie:

```bash
pip install xgboost umap-learn
```

XGBoost i UMAP są celowo opcjonalne, bo są za złożone na początek. W podstawowym kursie wystarczą `scikit-learn`, `numpy`, `pandas`, `matplotlib`.

---

## Główna idea kursu

```text
KNN
→ lokalna geometria: odległość i sąsiedztwo

Decision Tree
→ reguły if/else, interpretowalność, overfitting

PCA
→ reprezentacja danych, projekcja, redukcja wymiaru

SVM
→ globalna geometria: hiperplan, margines, support vectors

Random Forest / Gradient Boosting
→ ensemble learning, stabilizacja, model praktyczny dla tabel

XGBoost optional
→ przemysłowy boosting drzew, już po bazowej intuicji

Manifold Learning
→ nieliniowa geometria, lokalne sąsiedztwa, embeddingi
```

---

## Dlaczego taka kolejność?

KNN, PCA i SVM tworzą wspólną narrację geometryczną:

```text
KNN:  jaki punkt jest blisko?
PCA:  w jakiej przestrzeni dane wyglądają prościej?
SVM:  jaka granica w tej przestrzeni ma największy margines?
```

Drzewa i boosting tworzą równoległą narrację regułową:

```text
Decision Tree: pojedynczy zestaw reguł
Random Forest: wiele losowych drzew stabilizujących wynik
Gradient Boosting / XGBoost: drzewa uczone sekwencyjnie na błędach
```

Manifold learning jest późnym tematem, bo wymaga intuicji z KNN/PCA:

```text
PCA: dane leżą blisko liniowej podprzestrzeni
Manifold learning: dane leżą blisko zakrzywionej niskowymiarowej powierzchni
```

---

## Zbiory danych

| Dataset | Do czego służy |
|---|---|
| `blobs_margin` | KNN, linear SVM, margines, separowalność |
| `moons` | nieliniowe granice, KNN, drzewa, RBF SVM |
| `circles` | kernel trick, jawna transformacja cech `r²` |
| `iris` | mały realny dataset, pierwszy pełny pipeline |
| `breast_cancer` | realny tabular, metryki, walidacja, ensemble |
| `high_dim_redundant` | PCA, redundantne cechy, regularizacja |
| `swiss_roll` | manifold learning, PCA vs Isomap/t-SNE/UMAP |

---

## Minimalny przykład

```python
from ml_teaching_pack import make_dataset, model_library, run_basic_experiment

ds = make_dataset("moons", n_samples=500, random_state=42)
models = model_library("geometry")
results = run_basic_experiment(ds, models, scale=True)
print(results)
```

---

## Struktura pakietu

```text
ml_universal_teaching_pack/
├── ml_teaching_pack/
│   ├── datasets.py        # generowanie i ładowanie danych
│   ├── preprocessing.py   # split, scaling, PCA, proste feature maps
│   ├── models.py          # fabryki modeli
│   ├── evaluation.py      # metryki, porównania, cross-validation
│   ├── visualization.py   # wykresy 2D, PCA, granice decyzyjne
│   ├── manifold.py        # PCA/Isomap/LLE/t-SNE/UMAP optional
│   └── curriculum.py      # mapa kursu
├── notebooks/
│   ├── 00_setup_and_curriculum.ipynb
│   ├── 01_knn_geometry.ipynb
│   ├── 02_decision_trees_rules.ipynb
│   ├── 03_pca_representation.ipynb
│   ├── 04_svm_margin_kernels.ipynb
│   ├── 05_ensembles_xgboost_optional.ipynb
│   ├── 06_manifold_learning.ipynb
│   └── 07_full_comparison_pipeline.ipynb
├── scripts/
│   └── run_comparison.py
├── docs/
│   └── teaching_sequence.md
└── requirements.txt
```

---

## Jak używać dydaktycznie

1. Zawsze zaczynaj lekcję od tego samego pytania: **„jak ten model widzi dane?”**
2. Używaj najpierw danych 2D, bo granice decyzyjne są widoczne.
3. Dopiero potem przechodź na `iris`, `breast_cancer`, `high_dim_redundant`.
4. XGBoost pokazuj jako praktyczny benchmark, nie jako pierwszy model teoretyczny.
5. Manifold learning pokazuj dopiero po PCA i KNN, bo jego intuicja opiera się na sąsiedztwach i reprezentacji.

## Dodany moduł: 08 — Regresja liniowa, $R^2$, test $F$ i overfitting

Nowy materiał znajduje się w:

- `notebooks/08_linear_regression_lecture.ipynb` — główny notebook wykładowy,
- `notebooks/08_linear_regression_lecture_executed.ipynb` — wersja z wykonanymi komórkami i wykresami,
- `docs/linear_regression_teaching_notes_r2_f_overfit.md` — notatki prowadzącego,
- `docs/r2_f_overfit_cheatsheet.md` — krótka ściąga ze wzorami,
- `docs/linear_regression_simple_exercises_with_solutions.md` — proste ćwiczenia z kluczem odpowiedzi,
- `docs/linear_regression_lesson_plan_r2_f_overfit.md` — plan zajęć 45/90 minut,
- `docs/geogebra_linear_regression_r2_overfitting_task.md` — zadanie GeoGebra,
- `docs/geogebra_linear_regression_commands.txt` — komendy do wklejenia w GeoGebrze.

Materiał jest zrobiony w kolejności dydaktycznej: baseline średniej → reszty/SSE → `fit()` → $R^2$ → adjusted $R^2$ → test $F$ → train/test → underfitting/overfitting → diagnostyka reszt.


## Dodany moduł: 09 — GLM w stylu StatQuest, ekspresja genu i design matrix

Nowy materiał pokazuje, jak t-test i ANOVA wynikają z tej samej logiki co regresja liniowa:

- model zerowy = jedna średnia,
- model dopasowany = średnie grupowe albo regresja z cechami,
- porównanie modeli = `SSE_mean`, `SSE_fit`, test `F`, p-value,
- design matrix = sposób kodowania grup i zmiennych w jednym równaniu.

Pliki:

- `notebooks/09_statquest_glm_gene_expression_design_matrix.ipynb` — główny notebook,
- `notebooks/09_statquest_glm_gene_expression_design_matrix_executed.ipynb` — wersja wykonana,
- `docs/statquest_glm_gene_expression_notes.md` — notatki prowadzącego,
- `docs/statquest_glm_gene_expression_exercises_with_solutions.md` — proste ćwiczenia z odpowiedziami,
- `docs/geogebra_gene_expression_glm_commands.txt` — komendy do GeoGebry,
- `data/statquest_style_gene_expression_ttest.csv`,
- `data/statquest_style_gene_expression_anova.csv`,
- `data/statquest_style_gene_expression_weight.csv`.
## v5 dodatki: design matrix, GLM, odds i testy ręczne

Nowe materiały:

- `notebooks/09_glm_design_matrix_ttest_anova_v5.ipynb` — design matrix jako wspólny język regresji, t-testu i ANOVA.
- `notebooks/10_odds_log_odds_or_fisher_chisquare_wald_v5.ipynb` — odds, log-odds, odds ratio oraz ręczne testy Fishera, chi-square i Walda.
- `docs/glm_design_matrix_ttest_anova_notes_v5.md` — notatki prowadzącego do części o GLM/design matrix.
- `docs/odds_log_odds_tests_notes_v5.md` — notatki prowadzącego do części odds/testy.
- `docs/glm_odds_simple_exercises_with_solutions_v5.md` — proste ćwiczenia z odpowiedziami.
- `docs/glm_odds_cheatsheet_v5.md` — krótka ściąga wzorów.
- `docs/geogebra_glm_odds_demo_commands_v5.txt` — proste komendy do GeoGebry.

Nowe dane:

- `data/statquest_style_glm_ttest.csv`
- `data/statquest_style_glm_anova_5_groups.csv`
- `data/statquest_style_glm_weight_genotype.csv`
- `data/statquest_style_gene_cancer_2x2_counts.csv`


## v6 update — linear models to PCA block, PCA excluded

Added statsmodels-free teaching notebooks:

- `09_glm_design_matrix_ttest_anova_v6_statsmodels_free.ipynb`
- `10_odds_log_odds_or_fisher_chisquare_wald_v6_statsmodels_free.ipynb`
- `11_logistic_regression_likelihood_v6.ipynb`
- `12_logistic_regression_deviance_model_tests_v6.ipynb`
- `13_roc_auc_thresholds_v6.ipynb`
- `14_regularization_ridge_lasso_elasticnet_v6.ipynb`

The v6 notebooks avoid `statsmodels` to prevent the `numpy.MachAr` compatibility error in older environments.


## Addendum v6.1 — most aplikacyjny i GeoGebra

Dodano:

- `notebooks/15_applied_bridge_grades_marathon_v6_1.ipynb` — zastosowania na `grades.csv` i danych maratończyków,
- `data/previous_lecture_grades.csv`,
- `data/previous_lecture_marathon_processed_sample.csv`,
- `data/previous_lecture_marathon_processed_full.csv`,
- `docs/v6_1_review_and_teaching_gaps.md`,
- `docs/dataset_bridge_and_project_ideas_v6_1.md`,
- rozbudowane skrypty GeoGebry `GG01`–`GG06`.

Wersja v6.1 nie usuwa małych przykładów tablicowych. Dodaje warstwę ćwiczeniowo-projektową, żeby studenci widzieli, jak linear/logistic/ROC/regularization działają na danych z poprzednich zajęć.

## v6.2 add-on

Dodano notebook `notebooks/16_applied_bridge_titanic_tips_v6_2.ipynb` oraz lokalne CSV `data/seaborn_titanic.csv` i `data/seaborn_tips.csv`. Ten blok służy jako opcjonalny most od małych przykładów tablicowych do ćwiczeń/projektu.
