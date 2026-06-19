"""Datasets for a coherent ML teaching sequence.

The goal is not to maximize benchmark performance. The goal is to reuse a small
family of datasets so each new algorithm answers a new question:

- KNN: what does locality/distance mean?
- Trees: how do rule-based splits differ from geometry?
- PCA: what changes when we rotate/compress the feature space?
- SVM: what does a global margin mean?
- Ensembles/XGBoost: how do many weak trees become a strong tabular model?
- Manifold learning: what if the data live on a curved low-dimensional surface?
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

import numpy as np
import pandas as pd
from sklearn.datasets import (
    load_breast_cancer,
    load_iris,
    make_blobs,
    make_circles,
    make_classification,
    make_moons,
    make_swiss_roll,
)


@dataclass
class DatasetBundle:
    """A consistent container used across notebooks and scripts."""

    name: str
    X: pd.DataFrame
    y: pd.Series
    feature_names: List[str]
    target_names: Optional[List[str]] = None
    description: str = ""
    kind: str = "classification"
    metadata: Dict[str, Any] = field(default_factory=dict)

    def as_xy(self):
        """Return X, y as pandas objects."""
        return self.X, self.y

    def frame(self) -> pd.DataFrame:
        """Return one DataFrame with features and target."""
        out = self.X.copy()
        out["target"] = self.y.values
        return out


DATASET_GUIDE = {
    "blobs_margin": "Linear-ish binary dataset. Best for KNN intuition, linear SVM, margin.",
    "moons": "Nonlinear two-class dataset. Best for KNN, tree boundaries, RBF SVM.",
    "circles": "Nonlinear concentric classes. Best for kernel trick and feature maps.",
    "iris": "Small real multiclass dataset. Best for first full pipeline.",
    "breast_cancer": "Real tabular binary dataset. Best for evaluation metrics and practical comparison.",
    "high_dim_redundant": "Many correlated/redundant features. Best for PCA and regularization.",
    "swiss_roll": "3D curved manifold. Best for PCA vs manifold learning.",
}


def list_datasets() -> pd.DataFrame:
    """Return a compact guide to available datasets."""
    rows = [{"dataset": k, "use": v} for k, v in DATASET_GUIDE.items()]
    return pd.DataFrame(rows)


def _frame(X: np.ndarray, prefix: str = "x") -> pd.DataFrame:
    return pd.DataFrame(X, columns=[f"{prefix}{i+1}" for i in range(X.shape[1])])


def make_dataset(
    name: str,
    n_samples: int = 500,
    random_state: int = 42,
    noise: Optional[float] = None,
) -> DatasetBundle:
    """Create or load one dataset by name.

    Parameters
    ----------
    name:
        One of: blobs_margin, moons, circles, iris, breast_cancer,
        high_dim_redundant, swiss_roll.
    n_samples:
        Used for synthetic datasets.
    random_state:
        Controls reproducibility.
    noise:
        Optional override for synthetic dataset noise.
    """
    name = name.lower().strip()

    if name == "blobs_margin":
        X, y = make_blobs(
            n_samples=n_samples,
            centers=[(-2.0, -1.2), (2.0, 1.2)],
            cluster_std=noise if noise is not None else 1.15,
            random_state=random_state,
        )
        df = _frame(X)
        return DatasetBundle(
            name=name,
            X=df,
            y=pd.Series(y, name="target"),
            feature_names=list(df.columns),
            target_names=["class_0", "class_1"],
            description="Nearly linearly separable blobs for distance, boundary, and margin intuition.",
        )

    if name == "moons":
        X, y = make_moons(
            n_samples=n_samples,
            noise=noise if noise is not None else 0.22,
            random_state=random_state,
        )
        df = _frame(X)
        return DatasetBundle(
            name=name,
            X=df,
            y=pd.Series(y, name="target"),
            feature_names=list(df.columns),
            target_names=["moon_0", "moon_1"],
            description="Two interleaving moons: a compact example where nonlinear boundaries matter.",
        )

    if name == "circles":
        X, y = make_circles(
            n_samples=n_samples,
            factor=0.45,
            noise=noise if noise is not None else 0.08,
            random_state=random_state,
        )
        df = _frame(X)
        return DatasetBundle(
            name=name,
            X=df,
            y=pd.Series(y, name="target"),
            feature_names=list(df.columns),
            target_names=["outer", "inner"],
            description="Concentric circles: ideal for showing why linear models fail and kernels help.",
        )

    if name == "iris":
        data = load_iris(as_frame=True)
        X = data.data.copy()
        y = data.target.copy()
        return DatasetBundle(
            name=name,
            X=X,
            y=pd.Series(y, name="target"),
            feature_names=list(X.columns),
            target_names=list(data.target_names),
            description="Classic small real dataset with three flower species and four numeric features.",
        )

    if name == "breast_cancer":
        data = load_breast_cancer(as_frame=True)
        X = data.data.copy()
        y = data.target.copy()
        return DatasetBundle(
            name=name,
            X=X,
            y=pd.Series(y, name="target"),
            feature_names=list(X.columns),
            target_names=list(data.target_names),
            description="Real medical tabular dataset; useful for metrics, scaling, and robust validation.",
        )

    if name == "high_dim_redundant":
        X, y = make_classification(
            n_samples=n_samples,
            n_features=24,
            n_informative=4,
            n_redundant=10,
            n_repeated=0,
            n_classes=2,
            class_sep=1.0,
            flip_y=0.04,
            random_state=random_state,
        )
        df = _frame(X)
        return DatasetBundle(
            name=name,
            X=df,
            y=pd.Series(y, name="target"),
            feature_names=list(df.columns),
            target_names=["class_0", "class_1"],
            description="High-dimensional redundant data for PCA, regularization, and scaling lessons.",
        )

    if name == "swiss_roll":
        X, t = make_swiss_roll(
            n_samples=n_samples,
            noise=noise if noise is not None else 0.18,
            random_state=random_state,
        )
        df = pd.DataFrame(X, columns=["x", "height", "z"])
        # Binned classes are only for visualization/classification demos.
        y = pd.Series(pd.qcut(t, q=3, labels=False), name="target").astype(int)
        return DatasetBundle(
            name=name,
            X=df,
            y=y,
            feature_names=list(df.columns),
            target_names=["low_t", "mid_t", "high_t"],
            description="A 3D curved surface. PCA compresses linearly; manifold methods try to unfold locally.",
            kind="manifold",
            metadata={"t": t},
        )

    valid = ", ".join(DATASET_GUIDE)
    raise ValueError(f"Unknown dataset '{name}'. Valid options: {valid}")
