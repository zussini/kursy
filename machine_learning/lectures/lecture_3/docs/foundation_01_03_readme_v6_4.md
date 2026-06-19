# Brakujące fundamenty 01–03 — v6.4

Ta paczka uzupełnia początek kursu, którego brakowało przed blokiem linear/logistic. Notebooki są celowo krótkie i praktyczne: mają dać język potrzebny do późniejszych tematów, ale nie mają zastępować pełnych wykładów o KNN, clusteringu, SVM czy PCA.

## Kolejność

1. `01_ml_pipeline_train_test_cv_leakage_v6_4.ipynb`
   - train/test,
   - baseline,
   - cross-validation,
   - leakage,
   - pierwszy przykład regresji i klasyfikacji.

2. `02_metrics_regression_classification_roc_auc_v6_4.ipynb`
   - MAE, MSE, RMSE, $R^2$,
   - confusion matrix,
   - accuracy, precision, recall/sensitivity, specificity, F1,
   - threshold sweep,
   - mini-ROC i AUC.

3. `03_geometry_scaling_norms_distances_cosine_v6_4.ipynb`
   - wektory,
   - normy L1/L2,
   - odległość euklidesowa i Manhattan,
   - standaryzacja,
   - cosine similarity,
   - most do modeli liniowych i regularizacji.

## Jak tego używać na zajęciach

Na wykładzie wystarczy przejść skrótem:

$$
train/test \rightarrow baseline \rightarrow leakage \rightarrow metryki \rightarrow skala/odległość
$$

Potem można wejść w blok:

$$
linear\ regression \rightarrow design\ matrix \rightarrow t/ANOVA \rightarrow odds/logit \rightarrow logistic\ regression
$$

## Dlaczego to wystarczy przed 06–14?

Blok 06–14 potrzebuje głównie trzech rzeczy:

- rozumienia, że model oceniamy na danych testowych,
- rozumienia, że metryka zależy od typu problemu,
- rozumienia, że skala cech wpływa na geometrię, współczynniki i regularizację.

KNN i clustering można spokojnie zrobić później jako powrót do geometrii lokalnej i uczenia bez etykiet.
