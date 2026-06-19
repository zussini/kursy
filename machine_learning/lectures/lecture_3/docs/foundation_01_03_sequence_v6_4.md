# Fundamenty 01–03 — jak prowadzić, jeśli paczka startowała od modeli

Ta aktualizacja dodaje brakujący blok startowy:

1. `01_ml_pipeline_train_test_cv_leakage_v6_4.ipynb`
2. `02_metrics_regression_classification_roc_auc_v6_4.ipynb`
3. `03_geometry_scaling_norms_distances_cosine_v6_4.ipynb`

## Dlaczego te pliki są potrzebne?

Bez nich kurs zaczyna się zbyt szybko od konkretnych algorytmów. Studenci widzą model, ale nie mają jeszcze wspólnego języka:

- czym jest train/test,
- czym jest baseline,
- czym jest leakage,
- jak działa confusion matrix,
- czym różni się score od klasy po progu,
- dlaczego scaling zmienia geometrię danych.

## Docelowa ścieżka na teraz

Jeżeli chcesz szybko wejść w blok liniowy, prowadź tak:

$$
01 \rightarrow 02 \rightarrow 03 \rightarrow 08 \rightarrow 09 \rightarrow 10 \rightarrow 11 \rightarrow 12 \rightarrow 13 \rightarrow 14
$$

Praktycznie:

- 01 można zrobić krótko, jako wprowadzenie do pipeline'u.
- 02 można zrobić jako metryki, które później wrócą przy logistic regression i ROC/AUC.
- 03 można zrobić jako geometrię potrzebną do scalingu, regularyzacji, KNN, PCA i SVM.

## Uwaga o starych nazwach

W starszej paczce pliki `01_knn_geometry.ipynb` i `02_decision_trees_rules.ipynb` były nazwane historycznie. W docelowej kolejności traktuj je jako późniejsze moduły:

- `01_knn_geometry.ipynb` → docelowo okolice modułu 04 KNN,
- `02_decision_trees_rules.ipynb` → docelowo okolice modułu 18 Drzewa decyzyjne.

Nie trzeba ich usuwać. Wystarczy używać manifestu kolejności.