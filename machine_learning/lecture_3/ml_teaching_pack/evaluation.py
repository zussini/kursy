"""Evaluation functions shared by all lessons."""

from __future__ import annotations

from typing import Dict, Mapping, Optional

import numpy as np
import pandas as pd
from sklearn.base import clone
from sklearn.metrics import accuracy_score, balanced_accuracy_score, f1_score
from sklearn.model_selection import StratifiedKFold, cross_validate

from .preprocessing import split_scale


def evaluate_classifier(model, X_test, y_test) -> Dict[str, float]:
    """Return a compact metric dictionary for classification."""
    pred = model.predict(X_test)
    return {
        "accuracy": float(accuracy_score(y_test, pred)),
        "balanced_accuracy": float(balanced_accuracy_score(y_test, pred)),
        "f1_macro": float(f1_score(y_test, pred, average="macro")),
    }


def compare_models(
    models: Mapping[str, object],
    X_train,
    X_test,
    y_train,
    y_test,
) -> pd.DataFrame:
    """Fit each model once and compare test metrics."""
    rows = []
    for name, model in models.items():
        fitted = clone(model)
        fitted.fit(X_train, y_train)
        metrics = evaluate_classifier(fitted, X_test, y_test)
        rows.append({"model": name, **metrics})
    return pd.DataFrame(rows).sort_values("balanced_accuracy", ascending=False).reset_index(drop=True)


def crossval_compare(
    models: Mapping[str, object],
    X,
    y,
    cv: int = 5,
    random_state: int = 42,
    scoring: Optional[list[str]] = None,
) -> pd.DataFrame:
    """Cross-validated comparison with mean/std metrics."""
    if scoring is None:
        scoring = ["accuracy", "balanced_accuracy", "f1_macro"]

    splitter = StratifiedKFold(n_splits=cv, shuffle=True, random_state=random_state)
    rows = []
    for name, model in models.items():
        scores = cross_validate(clone(model), X, y, cv=splitter, scoring=scoring)
        row = {"model": name}
        for metric in scoring:
            values = scores[f"test_{metric}"]
            row[f"{metric}_mean"] = float(np.mean(values))
            row[f"{metric}_std"] = float(np.std(values))
        rows.append(row)
    return pd.DataFrame(rows).sort_values("balanced_accuracy_mean", ascending=False).reset_index(drop=True)


def run_basic_experiment(
    dataset,
    models: Mapping[str, object],
    scale: bool = True,
    test_size: float = 0.25,
    random_state: int = 42,
) -> pd.DataFrame:
    """One-line experiment for lessons."""
    split = split_scale(
        dataset.X,
        dataset.y,
        test_size=test_size,
        random_state=random_state,
        scale=scale,
    )
    return compare_models(models, split.X_train, split.X_test, split.y_train, split.y_test)
