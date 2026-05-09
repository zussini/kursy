"""Universal ML teaching pack: geometry, trees, margins, ensembles, manifolds."""

from .datasets import DatasetBundle, list_datasets, make_dataset
from .models import get_model, model_library
from .evaluation import compare_models, crossval_compare, evaluate_classifier, run_basic_experiment
from .preprocessing import split_scale, pca_project, add_radial_feature
from .curriculum import curriculum_table, print_curriculum

__all__ = [
    "DatasetBundle",
    "list_datasets",
    "make_dataset",
    "get_model",
    "model_library",
    "compare_models",
    "crossval_compare",
    "evaluate_classifier",
    "run_basic_experiment",
    "split_scale",
    "pca_project",
    "add_radial_feature",
    "curriculum_table",
    "print_curriculum",
]
