"""Curriculum map for the teaching pack."""

from __future__ import annotations

import pandas as pd

CURRICULUM = [
    {
        "stage": 1,
        "topic": "KNN",
        "question": "Czy bliskość oznacza podobieństwo?",
        "dataset": "blobs_margin, moons, iris",
        "core_concepts": "distance, scaling, local decision boundary, k",
    },
    {
        "stage": 2,
        "topic": "Decision Tree",
        "question": "Czy da się klasyfikować prostymi regułami if/else?",
        "dataset": "moons, iris, breast_cancer",
        "core_concepts": "Gini/entropy, splits, depth, overfitting, interpretability",
    },
    {
        "stage": 3,
        "topic": "PCA",
        "question": "Czy zmiana układu współrzędnych odsłania strukturę danych?",
        "dataset": "iris, high_dim_redundant, breast_cancer",
        "core_concepts": "variance, projection, components, compression, denoising",
    },
    {
        "stage": 4,
        "topic": "SVM",
        "question": "Jaka granica decyzyjna jest najbardziej stabilna?",
        "dataset": "blobs_margin, circles, moons, high_dim_redundant",
        "core_concepts": "hyperplane, margin, support vectors, C, kernel, gamma",
    },
    {
        "stage": 5,
        "topic": "Random Forest / Boosting",
        "question": "Co daje wiele słabszych drzew zamiast jednego?",
        "dataset": "breast_cancer, high_dim_redundant",
        "core_concepts": "ensembles, bagging, boosting, residual errors, regularization",
    },
    {
        "stage": 6,
        "topic": "XGBoost optional",
        "question": "Dlaczego boosting drzew jest tak mocny dla danych tablicowych?",
        "dataset": "breast_cancer, high_dim_redundant",
        "core_concepts": "gradient boosting, learning rate, depth, early stopping, validation",
    },
    {
        "stage": 7,
        "topic": "Manifold Learning",
        "question": "Co jeśli dane leżą na zakrzywionej powierzchni?",
        "dataset": "swiss_roll, moons",
        "core_concepts": "local neighborhoods, nonlinear embedding, Isomap, t-SNE, UMAP",
    },
]


def curriculum_table() -> pd.DataFrame:
    return pd.DataFrame(CURRICULUM)


def print_curriculum() -> None:
    df = curriculum_table()
    for _, row in df.iterrows():
        print(f"{row.stage}. {row.topic}: {row.question}")
        print(f"   dataset: {row.dataset}")
        print(f"   concepts: {row.core_concepts}\n")
