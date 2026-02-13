import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_performance():
    # Load data
    try:
        df = pd.read_csv('benchmark_results.csv')
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return

    # Set style
    plt.style.use('bmh') # Using a built-in style

    # Get unique algorithms
    algorithms = df['Algorithm'].unique()

    # 1. Linear Scale Plot
    plt.figure(figsize=(12, 8))
    for algo in algorithms:
        subset = df[df['Algorithm'] == algo]
        plt.plot(subset['Size'], subset['Time'], marker='o', label=algo, linewidth=2)

    plt.title('Sorting Algorithm Performance (Linear Scale)', fontsize=16)
    plt.xlabel('Input Size (n)', fontsize=12)
    plt.ylabel('Execution Time (seconds)', fontsize=12)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, which="both", ls="-", alpha=0.5)
    plt.tight_layout()
    plt.savefig('sorting_performance_linear.png', dpi=300)
    print("Saved sorting_performance_linear.png")

    # 2. Log-Log Scale Plot
    plt.figure(figsize=(12, 8))
    for algo in algorithms:
        subset = df[df['Algorithm'] == algo]
        plt.loglog(subset['Size'], subset['Time'], marker='o', label=algo, linewidth=2)

    plt.title('Sorting Algorithm Performance (Log-Log Scale)', fontsize=16)
    plt.xlabel('Input Size (n)', fontsize=12)
    plt.ylabel('Execution Time (seconds)', fontsize=12)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, which="both", ls="-", alpha=0.5)
    plt.tight_layout()
    plt.savefig('sorting_performance_loglog.png', dpi=300)
    print("Saved sorting_performance_loglog.png")

    # 3. Zoomed in Linear Scale (for efficient algorithms)
    plt.figure(figsize=(12, 8))
    efficient_algos = ["Merge Sort", "Quick Sort", "Randomized Quick Sort", "Heap Sort", "Shell Sort", "Counting Sort", "Radix Sort"]
    for algo in efficient_algos:
        if algo in algorithms:
            subset = df[df['Algorithm'] == algo]
            plt.plot(subset['Size'], subset['Time'], marker='o', label=algo, linewidth=2)

    plt.title('Efficient Sorting Algorithms Performance (Linear Scale)', fontsize=16)
    plt.xlabel('Input Size (n)', fontsize=12)
    plt.ylabel('Execution Time (seconds)', fontsize=12)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, which="both", ls="-", alpha=0.5)
    plt.tight_layout()
    plt.savefig('sorting_performance_efficient.png', dpi=300)
    print("Saved sorting_performance_efficient.png")

if __name__ == "__main__":
    plot_performance()
