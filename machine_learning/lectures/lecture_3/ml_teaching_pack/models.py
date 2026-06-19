"""Model factories used across the teaching sequence."""

from __future__ import annotations

from collections import OrderedDict
from typing import Dict

from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC, LinearSVC
from sklearn.tree import DecisionTreeClassifier


def get_model(name: str, random_state: int = 42, **kwargs):
    """Create a sklearn-compatible model by short name.

    Supported names:
    knn, tree, tree_deep, logreg, linear_svm, svm_rbf, random_forest,
    gradient_boosting, xgboost_optional.
    """
    name = name.lower().strip()

    if name == "knn":
        return KNeighborsClassifier(n_neighbors=kwargs.pop("n_neighbors", 7), **kwargs)

    if name == "tree":
        return DecisionTreeClassifier(
            max_depth=kwargs.pop("max_depth", 3),
            random_state=random_state,
            **kwargs,
        )

    if name == "tree_deep":
        return DecisionTreeClassifier(random_state=random_state, **kwargs)

    if name == "logreg":
        return LogisticRegression(max_iter=kwargs.pop("max_iter", 3000), random_state=random_state, **kwargs)

    if name == "linear_svm":
        return LinearSVC(C=kwargs.pop("C", 1.0), max_iter=kwargs.pop("max_iter", 10000), random_state=random_state, **kwargs)

    if name in {"svm_rbf", "rbf_svm"}:
        return SVC(
            kernel="rbf",
            C=kwargs.pop("C", 1.0),
            gamma=kwargs.pop("gamma", "scale"),
            probability=kwargs.pop("probability", False),
            random_state=random_state,
            **kwargs,
        )

    if name == "random_forest":
        return RandomForestClassifier(
            n_estimators=kwargs.pop("n_estimators", 200),
            max_depth=kwargs.pop("max_depth", None),
            random_state=random_state,
            **kwargs,
        )

    if name == "gradient_boosting":
        return GradientBoostingClassifier(random_state=random_state, **kwargs)

    if name == "xgboost_optional":
        try:
            from xgboost import XGBClassifier  # type: ignore
        except Exception as exc:  # pragma: no cover - optional dependency
            raise ImportError(
                "xgboost is optional. Install it with `pip install xgboost`, "
                "or use `gradient_boosting` first."
            ) from exc
        return XGBClassifier(
            n_estimators=kwargs.pop("n_estimators", 200),
            max_depth=kwargs.pop("max_depth", 3),
            learning_rate=kwargs.pop("learning_rate", 0.05),
            subsample=kwargs.pop("subsample", 0.9),
            colsample_bytree=kwargs.pop("colsample_bytree", 0.9),
            eval_metric=kwargs.pop("eval_metric", "logloss"),
            random_state=random_state,
            **kwargs,
        )

    raise ValueError(f"Unknown model name: {name}")


def model_library(stage: str = "core", random_state: int = 42) -> Dict[str, object]:
    """Return an ordered dictionary of models for a lesson stage."""
    stage = stage.lower().strip()

    if stage == "first_models":
        names = ["knn", "tree", "logreg"]
    elif stage == "geometry":
        names = ["knn", "logreg", "linear_svm", "svm_rbf"]
    elif stage == "trees":
        names = ["tree", "tree_deep", "random_forest", "gradient_boosting"]
    elif stage == "full":
        names = ["knn", "tree", "logreg", "linear_svm", "svm_rbf", "random_forest", "gradient_boosting"]
    else:
        names = ["knn", "tree", "linear_svm", "svm_rbf"]

    return OrderedDict((name, get_model(name, random_state=random_state)) for name in names)
