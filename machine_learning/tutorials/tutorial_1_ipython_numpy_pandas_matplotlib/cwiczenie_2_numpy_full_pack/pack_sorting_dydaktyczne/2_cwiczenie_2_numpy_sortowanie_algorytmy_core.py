from __future__ import annotations

from collections import Counter
from typing import Callable, Dict, Iterable, List, Sequence, TypeVar
import random
import time

T = TypeVar("T")

RANDOM_SEED = 0


def is_sorted(seq: Sequence[T], key: Callable[[T], object] = lambda x: x) -> bool:
    """Return True if seq is non-decreasing with respect to key."""
    return all(key(seq[i]) <= key(seq[i + 1]) for i in range(len(seq) - 1))


def same_multiset(a: Sequence[T], b: Sequence[T]) -> bool:
    """Return True if a and b contain the same elements with the same multiplicities."""
    return Counter(a) == Counter(b)


def time_call(fn: Callable[..., object], *args, repeats: int = 3) -> float:
    """Best-of-repeats wall-clock time."""
    best = float("inf")
    for _ in range(repeats):
        t0 = time.perf_counter()
        fn(*args)
        dt = time.perf_counter() - t0
        best = min(best, dt)
    return best


def make_random_list(n: int, seed: int = RANDOM_SEED) -> List[int]:
    rng = random.Random(seed)
    return [rng.randint(-10_000, 10_000) for _ in range(n)]


def make_nearly_sorted_list(n: int, swaps: int = 10, seed: int = RANDOM_SEED) -> List[int]:
    rng = random.Random(seed)
    xs = list(range(n))
    if n <= 1:
        return xs
    for _ in range(max(0, swaps)):
        i = rng.randrange(n)
        j = rng.randrange(n)
        xs[i], xs[j] = xs[j], xs[i]
    return xs


def make_reversed_list(n: int) -> List[int]:
    return list(range(n, 0, -1))


def benchmark_suite(
    sorters: Dict[str, Callable[[Sequence[int]], object]],
    datasets: Dict[str, Sequence[int]],
    repeats: int = 3,
) -> List[Dict[str, float | str | int]]:
    """
    Benchmark each sorter on each dataset.

    Returns list of rows:
      {"dataset": ..., "n": ..., "<sorter_name>": time_in_seconds, ...}
    """
    rows: List[Dict[str, float | str | int]] = []
    for dataset_name, xs in datasets.items():
        row: Dict[str, float | str | int] = {"dataset": dataset_name, "n": len(xs)}
        for sorter_name, sorter in sorters.items():
            row[sorter_name] = time_call(sorter, xs, repeats=repeats)
        rows.append(row)
    return rows


def print_benchmark_table(rows: List[Dict[str, float | str | int]], sort_order: List[str]) -> None:
    """
    Pretty-print benchmark rows produced by benchmark_suite.
    """
    header = f"{'dataset':<15} {'n':>6} " + " ".join(f"{name:>12}" for name in sort_order)
    print(header)
    print("-" * len(header))
    for row in rows:
        parts = [f"{row['dataset']:<15}", f"{row['n']:>6d}"]
        for name in sort_order:
            parts.append(f"{row[name]:>12.6f}")
        print(" ".join(parts))
