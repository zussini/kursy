"""Run a compact model comparison from the command line.

Examples:
    python scripts/run_comparison.py --dataset moons --stage geometry
    python scripts/run_comparison.py --dataset breast_cancer --stage full --no-scale
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from ml_teaching_pack import make_dataset, model_library, run_basic_experiment


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", default="moons")
    parser.add_argument("--stage", default="geometry", choices=["first_models", "geometry", "trees", "full"])
    parser.add_argument("--n-samples", type=int, default=500)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--no-scale", action="store_true")
    args = parser.parse_args()

    ds = make_dataset(args.dataset, n_samples=args.n_samples, random_state=args.seed)
    models = model_library(args.stage, random_state=args.seed)
    results = run_basic_experiment(ds, models, scale=not args.no_scale, random_state=args.seed)
    print(f"Dataset: {ds.name}")
    print(ds.description)
    print(results.to_string(index=False))


if __name__ == "__main__":
    main()
