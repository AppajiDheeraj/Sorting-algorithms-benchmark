"""
Experimental Evaluation of Sorting Algorithms
============================================

This script performs an experimental time-complexity evaluation of multiple
sorting algorithms. It generates continuous graphs to visualize growth trends.

Key Features
------------
- Input scaling up to 10^6 elements (with adaptive algorithm selection)
- High-resolution plotting with professional formatting
- Log-log scale for time complexity visualization
- Multiple input distributions (random, sorted, reverse, nearly sorted)
- Reproducible experiments via fixed random seed

Outputs
-------
- results.csv: raw measurement data
- sorting_performance_loglog.png: log-log time complexity plot
- sorting_performance_linear.png: linear scale plot (optional)
"""

from __future__ import annotations

import csv
import math
import os
import random
import statistics
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Dict, Iterable, List, Tuple

import matplotlib.pyplot as plt
import numpy as np

from sorting_algorithms import ALGORITHMS


@dataclass(frozen=True)
class ExperimentConfig:
    seed: int = 42
    repeats: int = 5
    warmup_runs: int = 1
    max_n: int = 1_000_000
    min_n: int = 100
    points: int = 24
    output_dir: str = "outputs"
    dpi: int = 300


def generate_input_sizes(min_n: int, max_n: int, points: int) -> List[int]:
    """Generate logarithmically spaced input sizes for continuous curves."""
    sizes = np.unique(
        np.round(np.logspace(math.log10(min_n), math.log10(max_n), points)).astype(int)
    )
    return [int(n) for n in sizes if n >= 2]


def generate_dataset(n: int, distribution: str, rng: random.Random) -> List[int]:
    """Generate integer arrays under different distributions."""
    if distribution == "random":
        return [rng.randint(0, 1_000_000) for _ in range(n)]

    if distribution == "sorted":
        return list(range(n))

    if distribution == "reverse":
        return list(range(n, 0, -1))

    if distribution == "nearly_sorted":
        arr = list(range(n))
        swaps = max(1, n // 100)  # 1% random swaps
        for _ in range(swaps):
            i = rng.randrange(n)
            j = rng.randrange(n)
            arr[i], arr[j] = arr[j], arr[i]
        return arr

    raise ValueError(f"Unknown distribution: {distribution}")


def time_algorithm(
    sort_fn: Callable[[List[int]], List[int]],
    base_data: List[int],
    repeats: int,
    warmup_runs: int,
) -> Tuple[float, float]:
    """Return (median_time, stdev_time) in seconds."""
    times: List[float] = []

    for _ in range(warmup_runs):
        _ = sort_fn(base_data)

    for _ in range(repeats):
        data = base_data.copy()
        t0 = time.perf_counter()
        out = sort_fn(data)
        t1 = time.perf_counter()

        if len(out) != len(base_data) or (len(out) > 1 and out[0] > out[-1]):
            raise RuntimeError("Sorting validation failed")

        times.append(t1 - t0)

    return statistics.median(times), statistics.pstdev(times)


def select_algorithms_for_n(algorithms: Dict[str, Callable], n: int) -> Dict[str, Callable]:
    """
    Ensure feasible runtime scaling up to 10^6.

    Quadratic algorithms become impractical beyond ~50k (often much less), so we
    exclude them for large n while still plotting them on smaller n.
    """
    quadratic = {"Bubble Sort", "Selection Sort", "Insertion Sort"}

    if n <= 20_000:
        return algorithms

    return {name: fn for name, fn in algorithms.items() if name not in quadratic}


def run_experiment(config: ExperimentConfig, distribution: str) -> List[dict]:
    rng = random.Random(config.seed)
    sizes = generate_input_sizes(config.min_n, config.max_n, config.points)

    rows: List[dict] = []

    for n in sizes:
        base_data = generate_dataset(n, distribution, rng)
        active = select_algorithms_for_n(ALGORITHMS, n)

        for name, fn in active.items():
            median_t, stdev_t = time_algorithm(fn, base_data, config.repeats, config.warmup_runs)
            rows.append(
                {
                    "distribution": distribution,
                    "algorithm": name,
                    "n": n,
                    "median_seconds": median_t,
                    "stdev_seconds": stdev_t,
                }
            )

            print(f"{distribution:>13} | {name:<14} | n={n:<8} | {median_t:.6f}s")

    return rows


def save_csv(rows: List[dict], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = ["distribution", "algorithm", "n", "median_seconds", "stdev_seconds"]

    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def plot_results(rows: List[dict], config: ExperimentConfig, distribution: str) -> None:
    outdir = Path(config.output_dir)
    outdir.mkdir(parents=True, exist_ok=True)

    algorithms = sorted({r["algorithm"] for r in rows})

    plt.rcParams.update(
        {
            "font.family": "serif",
            "font.size": 11,
            "axes.titlesize": 14,
            "axes.labelsize": 12,
            "legend.fontsize": 9,
            "xtick.labelsize": 10,
            "ytick.labelsize": 10,
            "figure.titlesize": 16,
        }
    )

    fig, ax = plt.subplots(figsize=(10, 6))

    color_map = plt.cm.get_cmap("tab10", len(algorithms))

    for idx, algo in enumerate(algorithms):
        algo_rows = [r for r in rows if r["algorithm"] == algo]
        algo_rows.sort(key=lambda r: r["n"])

        n_vals = np.array([r["n"] for r in algo_rows], dtype=float)
        t_vals = np.array([r["median_seconds"] for r in algo_rows], dtype=float)
        s_vals = np.array([r["stdev_seconds"] for r in algo_rows], dtype=float)

        ax.plot(
            n_vals,
            t_vals,
            marker="o",
            markersize=3,
            linewidth=1.8,
            label=algo,
            color=color_map(idx),
        )

        ax.fill_between(
            n_vals,
            np.maximum(t_vals - s_vals, 1e-9),
            t_vals + s_vals,
            alpha=0.12,
            color=color_map(idx),
            linewidth=0,
        )

    ax.set_xscale("log")
    ax.set_yscale("log")

    ax.set_title(f"Sorting Algorithm Performance (Log-Log) - {distribution.replace('_', ' ').title()}")
    ax.set_xlabel("Input size n (elements)")
    ax.set_ylabel("Median runtime (seconds)")

    ax.grid(True, which="both", linestyle="--", linewidth=0.6, alpha=0.6)

    ax.legend(
        loc="best",
        ncol=2,
        frameon=True,
        framealpha=0.95,
        borderpad=0.6,
        labelspacing=0.4,
        handlelength=2.0,
    )

    fig.tight_layout()
    fig.savefig(outdir / f"sorting_performance_loglog_{distribution}.png", dpi=config.dpi)
    plt.close(fig)


def compute_loglog_slope(rows: List[dict], algorithm: str) -> float | None:
    """Estimate slope in log-log space: slope ~ exponent in T(n) ~ n^slope."""
    algo_rows = [r for r in rows if r["algorithm"] == algorithm]
    algo_rows.sort(key=lambda r: r["n"])

    if len(algo_rows) < 4:
        return None

    n = np.array([r["n"] for r in algo_rows], dtype=float)
    t = np.array([r["median_seconds"] for r in algo_rows], dtype=float)

    n = n[t > 0]
    t = t[t > 0]

    if len(n) < 4:
        return None

    x = np.log10(n)
    y = np.log10(t)

    slope, _ = np.polyfit(x, y, 1)
    return float(slope)


def write_conclusions(rows: List[dict], config: ExperimentConfig, distribution: str) -> None:
    outdir = Path(config.output_dir)
    outdir.mkdir(parents=True, exist_ok=True)

    algos = sorted({r["algorithm"] for r in rows})
    slopes = {a: compute_loglog_slope(rows, a) for a in algos}

    path = outdir / f"conclusions_{distribution}.txt"

    with path.open("w") as f:
        f.write("Experimental Conclusions (from log-log curves)\n")
        f.write("================================================\n\n")
        f.write(f"Distribution: {distribution}\n")
        f.write(f"Repeats per n: {config.repeats} (median reported), warmup runs: {config.warmup_runs}\n")
        f.write(f"Input sizes: {config.min_n} to {config.max_n}, {config.points} log-spaced points\n\n")

        f.write("Estimated log-log slopes (approximate exponent in T(n) ~ n^k):\n")
        for algo in algos:
            s = slopes[algo]
            if s is None:
                f.write(f"- {algo}: insufficient points\n")
            else:
                f.write(f"- {algo}: k ≈ {s:.2f}\n")

        f.write("\nInterpretation Guide:\n")
        f.write("- k ≈ 2 suggests quadratic behavior (O(n^2))\n")
        f.write("- k ≈ 1 suggests near-linear behavior (often O(n) or O(n log n) over limited ranges)\n")
        f.write("- k between 1 and 2 often indicates O(n log n) or mixed effects\n\n")

        f.write("Key observations (typical expected trends):\n")
        f.write("1) Quadratic sorts (bubble/selection/insertion) rise steeply and become infeasible early.\n")
        f.write("2) Comparison-based O(n log n) sorts (merge/quick/heap/tim) show shallower slopes.\n")
        f.write("3) Non-comparison integer sorts (counting/radix) can appear close to linear if range/digits remain bounded.\n")
        f.write("\n")


def main() -> None:
    config = ExperimentConfig()
    distributions = ["random", "sorted", "reverse", "nearly_sorted"]

    all_rows: List[dict] = []

    for dist in distributions:
        rows = run_experiment(config, dist)
        save_csv(rows, Path(config.output_dir) / f"results_{dist}.csv")
        plot_results(rows, config, dist)
        write_conclusions(rows, config, dist)
        all_rows.extend(rows)

    save_csv(all_rows, Path(config.output_dir) / "results_all.csv")


if __name__ == "__main__":
    main()
