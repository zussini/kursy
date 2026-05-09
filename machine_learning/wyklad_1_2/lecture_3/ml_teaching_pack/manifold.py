"""Manifold learning helpers."""

from __future__ import annotations

from typing import Literal

import numpy as np
from sklearn.decomposition import PCA
from sklearn.manifold import Isomap, LocallyLinearEmbedding, TSNE


Method = Literal["pca", "isomap", "lle", "tsne", "umap_optional"]


def embed(X, method: Method = "isomap", n_components: int = 2, random_state: int = 42, **kwargs):
    """Return a 2D/low-dimensional embedding.

    `umap_optional` requires `pip install umap-learn`. The rest are sklearn methods.
    """
    X_arr = np.asarray(X)
    method = method.lower()

    if method == "pca":
        model = PCA(n_components=n_components, random_state=random_state, **kwargs)
        return model.fit_transform(X_arr), model

    if method == "isomap":
        model = Isomap(n_components=n_components, n_neighbors=kwargs.pop("n_neighbors", 12), **kwargs)
        return model.fit_transform(X_arr), model

    if method == "lle":
        model = LocallyLinearEmbedding(
            n_components=n_components,
            n_neighbors=kwargs.pop("n_neighbors", 12),
            random_state=random_state,
            **kwargs,
        )
        return model.fit_transform(X_arr), model

    if method == "tsne":
        model = TSNE(
            n_components=n_components,
            perplexity=kwargs.pop("perplexity", 30),
            init=kwargs.pop("init", "pca"),
            learning_rate=kwargs.pop("learning_rate", "auto"),
            random_state=random_state,
            **kwargs,
        )
        return model.fit_transform(X_arr), model

    if method == "umap_optional":
        try:
            import umap  # type: ignore
        except Exception as exc:  # pragma: no cover - optional dependency
            raise ImportError("Install UMAP with `pip install umap-learn`, or use isomap/lle/tsne first.") from exc
        model = umap.UMAP(n_components=n_components, random_state=random_state, **kwargs)
        return model.fit_transform(X_arr), model

    raise ValueError(f"Unknown method: {method}")
