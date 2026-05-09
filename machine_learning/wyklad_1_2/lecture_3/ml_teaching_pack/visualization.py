"""Plotting helpers. Kept small so students can read and modify them."""

from __future__ import annotations

from typing import Optional

import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.metrics import ConfusionMatrixDisplay


def plot_2d_points(X, y=None, title: str = "2D dataset", ax: Optional[plt.Axes] = None):
    """Scatter plot for 2D data."""
    X_arr = np.asarray(X)
    if X_arr.shape[1] < 2:
        raise ValueError("plot_2d_points needs at least two features")
    if ax is None:
        _, ax = plt.subplots(figsize=(7, 5))
    if y is None:
        ax.scatter(X_arr[:, 0], X_arr[:, 1], s=35)
    else:
        ax.scatter(X_arr[:, 0], X_arr[:, 1], c=np.asarray(y), s=35)
    ax.set_xlabel("x1")
    ax.set_ylabel("x2")
    ax.set_title(title)
    return ax


def plot_decision_boundary_2d(model, X, y, title: str = "Decision boundary", ax: Optional[plt.Axes] = None, step: float = 0.02):
    """Plot decision regions for fitted classifier on 2D input."""
    X_arr = np.asarray(X)
    if X_arr.shape[1] != 2:
        raise ValueError("plot_decision_boundary_2d expects exactly two features")
    if ax is None:
        _, ax = plt.subplots(figsize=(7, 5))

    x_min, x_max = X_arr[:, 0].min() - 0.8, X_arr[:, 0].max() + 0.8
    y_min, y_max = X_arr[:, 1].min() - 0.8, X_arr[:, 1].max() + 0.8
    xx, yy = np.meshgrid(np.arange(x_min, x_max, step), np.arange(y_min, y_max, step))
    grid = np.c_[xx.ravel(), yy.ravel()]
    Z = model.predict(grid).reshape(xx.shape)

    ax.contourf(xx, yy, Z, alpha=0.25)
    ax.scatter(X_arr[:, 0], X_arr[:, 1], c=np.asarray(y), s=35, edgecolor="k")
    ax.set_xlabel("x1")
    ax.set_ylabel("x2")
    ax.set_title(title)
    return ax


def plot_pca_variance(pca: PCA, title: str = "PCA explained variance", ax: Optional[plt.Axes] = None):
    """Plot cumulative explained variance ratio."""
    if ax is None:
        _, ax = plt.subplots(figsize=(7, 5))
    values = np.cumsum(pca.explained_variance_ratio_)
    ax.plot(np.arange(1, len(values) + 1), values, marker="o")
    ax.set_xlabel("number of components")
    ax.set_ylabel("cumulative explained variance")
    ax.set_ylim(0, 1.05)
    ax.set_title(title)
    return ax


def plot_pca_scatter(X, y=None, n_components: int = 2, title: str = "PCA projection", ax: Optional[plt.Axes] = None):
    """Fit PCA and plot first two components."""
    pca = PCA(n_components=n_components)
    Z = pca.fit_transform(np.asarray(X))
    if ax is None:
        _, ax = plt.subplots(figsize=(7, 5))
    ax.scatter(Z[:, 0], Z[:, 1], c=np.asarray(y) if y is not None else None, s=35)
    ax.set_xlabel("PC1")
    ax.set_ylabel("PC2")
    ax.set_title(title)
    return pca, ax


def plot_confusion(model, X_test, y_test, title: str = "Confusion matrix", ax: Optional[plt.Axes] = None):
    """Confusion matrix plot."""
    if ax is None:
        _, ax = plt.subplots(figsize=(6, 5))
    ConfusionMatrixDisplay.from_estimator(model, X_test, y_test, ax=ax)
    ax.set_title(title)
    return ax
