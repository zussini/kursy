"""Reusable preprocessing utilities for the teaching pack."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Tuple

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


@dataclass
class SplitData:
    X_train: np.ndarray
    X_test: np.ndarray
    y_train: np.ndarray
    y_test: np.ndarray
    scaler: Optional[StandardScaler]
    feature_names: list[str]


def split_scale(
    X: pd.DataFrame | np.ndarray,
    y: pd.Series | np.ndarray,
    test_size: float = 0.25,
    random_state: int = 42,
    scale: bool = True,
    stratify: bool = True,
) -> SplitData:
    """Train/test split with optional StandardScaler.

    Scale KNN, PCA, SVM, logistic regression. Usually do not need scaling for trees.
    """
    feature_names = list(X.columns) if hasattr(X, "columns") else [f"x{i+1}" for i in range(np.asarray(X).shape[1])]
    X_arr = np.asarray(X)
    y_arr = np.asarray(y)
    stratify_y = y_arr if stratify and len(np.unique(y_arr)) > 1 else None

    X_train, X_test, y_train, y_test = train_test_split(
        X_arr,
        y_arr,
        test_size=test_size,
        random_state=random_state,
        stratify=stratify_y,
    )

    scaler = None
    if scale:
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)

    return SplitData(X_train, X_test, y_train, y_test, scaler, feature_names)


def pca_project(
    X_train: np.ndarray,
    X_test: Optional[np.ndarray] = None,
    n_components: int = 2,
    random_state: int = 42,
) -> Tuple[PCA, np.ndarray, Optional[np.ndarray]]:
    """Fit PCA on train data and transform train/test."""
    pca = PCA(n_components=n_components, random_state=random_state)
    Z_train = pca.fit_transform(X_train)
    Z_test = pca.transform(X_test) if X_test is not None else None
    return pca, Z_train, Z_test


def add_radial_feature(X: pd.DataFrame | np.ndarray) -> pd.DataFrame:
    """Explicit feature map for circles: add r^2 = x1^2 + x2^2.

    This is a simple pre-kernel trick demo: sometimes nonlinear separability appears
    after a manually designed feature transformation.
    """
    if isinstance(X, pd.DataFrame):
        X_arr = X.values
        out = X.copy()
        names = list(X.columns)
    else:
        X_arr = np.asarray(X)
        names = [f"x{i+1}" for i in range(X_arr.shape[1])]
        out = pd.DataFrame(X_arr, columns=names)

    if X_arr.shape[1] < 2:
        raise ValueError("add_radial_feature needs at least two columns")
    out["r2"] = X_arr[:, 0] ** 2 + X_arr[:, 1] ** 2
    return out
