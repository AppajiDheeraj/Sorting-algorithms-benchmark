"""
Comprehensive Visualization for Sorting Algorithm Performance Analysis
======================================================================

This script generates advanced comparison visualizations:
- Side-by-side subplots for different distributions
- Combined comparison view
- Individual algorithm performance across distributions
- Professional formatting suitable for academic submission
"""

import csv
from pathlib import Path
from typing import Dict, List

import matplotlib.pyplot as plt
import numpy as np


def load_results(results_dir: Path) -> Dict[str, List[dict]]:
    """Load all CSV results grouped by distribution."""
    data = {}
    for csv_file in results_dir.glob("results_*.csv"):
        if csv_file.name == "results_all.csv":
            continue

        distribution = csv_file.stem.replace("results_", "")

        with csv_file.open("r") as f:
            reader = csv.DictReader(f)
            rows = []
            for row in reader:
                row["n"] = int(row["n"])
                row["median_seconds"] = float(row["median_seconds"])
                row["stdev_seconds"] = float(row["stdev_seconds"])
                rows.append(row)

        data[distribution] = rows

    return data


def plot_multi_distribution(data: Dict[str, List[dict]], output_path: Path, dpi: int = 300) -> None:
    """Create a multi-panel figure comparing distributions."""
    distributions = sorted(data.keys())

    if not distributions:
        return

    n_dist = len(distributions)

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    axes_flat = axes.flatten()

    plt.rcParams.update(
        {
            "font.family": "serif",
            "font.size": 10,
            "axes.titlesize": 12,
            "axes.labelsize": 10,
            "legend.fontsize": 8,
        }
    )

    algorithms = sorted({row["algorithm"] for rows in data.values() for row in rows})
    color_map = plt.cm.get_cmap("tab10", len(algorithms))
    color_dict = {algo: color_map(i) for i, algo in enumerate(algorithms)}

    for idx, dist in enumerate(distributions):
        if idx >= len(axes_flat):
            break

        ax = axes_flat[idx]
        rows = data[dist]

        for algo in algorithms:
            algo_rows = [r for r in rows if r["algorithm"] == algo]
            algo_rows.sort(key=lambda r: r["n"])

            if not algo_rows:
                continue

            n_vals = np.array([r["n"] for r in algo_rows], dtype=float)
            t_vals = np.array([r["median_seconds"] for r in algo_rows], dtype=float)
            s_vals = np.array([r["stdev_seconds"] for r in algo_rows], dtype=float)

            ax.plot(
                n_vals,
                t_vals,
                marker="o",
                markersize=2.5,
                linewidth=1.5,
                label=algo,
                color=color_dict[algo],
            )

            ax.fill_between(
                n_vals,
                np.maximum(t_vals - s_vals, 1e-9),
                t_vals + s_vals,
                alpha=0.10,
                color=color_dict[algo],
                linewidth=0,
            )

        ax.set_xscale("log")
        ax.set_yscale("log")
        ax.set_title(f"{dist.replace('_', ' ').title()} Distribution")
        ax.set_xlabel("Input size n (elements)")
        ax.set_ylabel("Runtime (seconds)")
        ax.grid(True, which="both", linestyle="--", linewidth=0.5, alpha=0.5)

        if idx == 0:
            ax.legend(loc="upper left", ncol=2, frameon=True, framealpha=0.9, fontsize=7)

    for idx in range(n_dist, len(axes_flat)):
        axes_flat[idx].axis("off")

    fig.suptitle("Sorting Algorithm Performance Across Different Distributions", fontsize=14, y=0.995)
    fig.tight_layout(rect=[0, 0, 1, 0.99])
    fig.savefig(output_path, dpi=dpi, bbox_inches="tight")
    plt.close(fig)


def plot_algorithm_comparison(data: Dict[str, List[dict]], output_dir: Path, dpi: int = 300) -> None:
    """Create individual plots showing each algorithm across all distributions."""
    algorithms = sorted({row["algorithm"] for rows in data.values() for row in rows})
    distributions = sorted(data.keys())

    color_map = plt.cm.get_cmap("Set2", len(distributions))
    dist_colors = {dist: color_map(i) for i, dist in enumerate(distributions)}

    for algo in algorithms:
        fig, ax = plt.subplots(figsize=(8, 5))

        for dist in distributions:
            rows = data[dist]
            algo_rows = [r for r in rows if r["algorithm"] == algo]
            algo_rows.sort(key=lambda r: r["n"])

            if not algo_rows:
                continue

            n_vals = np.array([r["n"] for r in algo_rows], dtype=float)
            t_vals = np.array([r["median_seconds"] for r in algo_rows], dtype=float)

            ax.plot(
                n_vals,
                t_vals,
                marker="s",
                markersize=3,
                linewidth=1.8,
                label=dist.replace("_", " ").title(),
                color=dist_colors[dist],
            )

        ax.set_xscale("log")
        ax.set_yscale("log")
        ax.set_title(f"{algo} - Performance Across Distributions")
        ax.set_xlabel("Input size n (elements)")
        ax.set_ylabel("Runtime (seconds)")
        ax.grid(True, which="both", linestyle="--", linewidth=0.5, alpha=0.5)
        ax.legend(loc="best", frameon=True, framealpha=0.9)

        fig.tight_layout()
        safe_name = algo.lower().replace(" ", "_")
        fig.savefig(output_dir / f"algo_{safe_name}.png", dpi=dpi, bbox_inches="tight")
        plt.close(fig)


def plot_complexity_classes(data: Dict[str, List[dict]], output_path: Path, dpi: int = 300) -> None:
    """Group algorithms by complexity class for better insight."""
    quadratic = {"Bubble Sort", "Selection Sort", "Insertion Sort"}
    nlogn = {"Merge Sort", "Quick Sort", "Heap Sort", "Shell Sort", "Tim Sort"}
    linear = {"Counting Sort", "Radix Sort"}

    classes = {
        "Quadratic O(n²)": quadratic,
        "Linearithmic O(n log n)": nlogn,
        "Linear/Special O(n+k)": linear,
    }

    dist = list(data.keys())[0]
    rows = data[dist]

    fig, axes = plt.subplots(1, 3, figsize=(15, 4))

    for idx, (class_name, algos) in enumerate(classes.items()):
        ax = axes[idx]

        for algo in sorted(algos):
            algo_rows = [r for r in rows if r["algorithm"] == algo]
            algo_rows.sort(key=lambda r: r["n"])

            if not algo_rows:
                continue

            n_vals = np.array([r["n"] for r in algo_rows], dtype=float)
            t_vals = np.array([r["median_seconds"] for r in algo_rows], dtype=float)

            ax.plot(n_vals, t_vals, marker="o", markersize=3, linewidth=1.5, label=algo)

        ax.set_xscale("log")
        ax.set_yscale("log")
        ax.set_title(class_name)
        ax.set_xlabel("Input size n")
        ax.set_ylabel("Runtime (seconds)")
        ax.grid(True, which="both", linestyle="--", linewidth=0.5, alpha=0.5)
        ax.legend(loc="best", fontsize=8)

    fig.suptitle(f"Algorithms Grouped by Complexity Class ({dist.replace('_', ' ').title()})", fontsize=13)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(output_path, dpi=dpi, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    results_dir = Path("outputs")

    if not results_dir.exists():
        print("No results directory found. Run experiment.py first.")
        return

    data = load_results(results_dir)

    if not data:
        print("No data loaded.")
        return

    print("Generating comprehensive visualizations...")

    plot_multi_distribution(data, results_dir / "comparison_all_distributions.png")
    print("✓ Multi-distribution comparison created")

    plot_algorithm_comparison(data, results_dir)
    print("✓ Individual algorithm comparisons created")

    plot_complexity_classes(data, results_dir / "complexity_classes.png")
    print("✓ Complexity class grouping created")

    print(f"\nAll visualizations saved to {results_dir}/")


if __name__ == "__main__":
    main()
