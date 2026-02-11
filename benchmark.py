import os
import subprocess
import time
import matplotlib.pyplot as plt
import re
import pandas as pd # Import pandas

# --- Configuration ---
C_FILES = [
    "bubble_sort.c",
    "heap_sort.c",
    "insertion_sort.c",
    "merge_sort.c",
    "quick_sort.c", # This is the generic quick sort (last element pivot)
    "radix_sort.c",
    "selection_sort.c",
]
C_FILE_PATHS = [os.path.join("sorting_algorithms", f) for f in C_FILES]
EXECUTABLES_DIR = "executables"
TEST_DATA_DIR = "test_data"
OUTPUT_GRAPHS_DIR = "graphs"
NUM_REPETITIONS = 7  # Number of times to run each experiment for averaging
# The maximum input size to consider for plotting. Adjust if needed.
MAX_PLOT_N = 100000 

# --- Helper Functions ---

def compile_c_code(c_file_path, output_executable_path):
    """Compiles a C source file into an executable."""
    print(f"Compiling {c_file_path}...")
    try:
        subprocess.run(
            ["gcc", c_file_path, "-o", output_executable_path],
            check=True,
            capture_output=True,
            text=True
        )
        print(f"Successfully compiled {c_file_path} to {output_executable_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error compiling {c_file_path}:")
        print(f"Stdout: {e.stdout}")
        print(f"Stderr: {e.stderr}")
        exit(1)

def read_test_data(filepath):
    """Reads integers from a given test data file, one integer per line."""
    with open(filepath, 'r') as f:
        data = [int(line.strip()) for line in f if line.strip()] # Read all non-empty lines as integers
    return data

def run_benchmark(executable_path, data):
    """
    Runs the compiled C program with the given data, measures execution time.
    Input data is passed via stdin. Output is discarded.
    """
    input_str = f"{len(data)}\n" + " ".join(map(str, data))
    
    start_time = time.perf_counter()
    try:
        # Use Popen to send input via stdin and capture/discard stdout/stderr
        process = subprocess.run(
            [executable_path],
            input=input_str,
            capture_output=True, # Capture stdout and stderr
            text=True,
            check=True # Raise an exception for non-zero exit codes
        )
        # We don't care about the sorted output for timing, just that it ran successfully
    except subprocess.CalledProcessError as e:
        print(f"Error running {executable_path} with data size {len(data)}:")
        print(f"Stdout: {e.stdout}")
        print(f"Stderr: {e.stderr}")
        return float('inf') # Return infinity for failed runs
    end_time = time.perf_counter()
    return end_time - start_time

def extract_n_and_type(filename):
    """Extracts N and data type (random, sorted, reverse_sorted) from a filename."""
    match = re.match(r"n_(\d+)_(\w+)\.txt", filename) # Corrected regex: \.txt instead of \\.txt
    if match:
        return int(match.group(1)), match.group(2)
    return None, None

def plot_results(results, plot_type, output_dir):
    """Generates and saves a plot for a specific case (best, worst, average)."""
    plt.figure(figsize=(12, 7))
    
    for algo_name, data_points in results.items():
        # Sort data points by N for correct plotting
        data_points.sort(key=lambda x: x[0])
        ns = [dp[0] for dp in data_points if dp[0] <= MAX_PLOT_N]
        times = [dp[1] for dp in data_points if dp[0] <= MAX_PLOT_N]
        plt.plot(ns, times, marker='o', linestyle='-', label=algo_name)

    plt.xlabel("Input Size (n)")
    plt.ylabel("Average Execution Time (s)")
    plt.title(f"Sorting Algorithm Performance: {plot_type} Case")
    plt.legend()
    plt.grid(True)
    plt.xscale('log') # Use log scale for x-axis if N values span a wide range
    plt.tight_layout()
    
    output_path = os.path.join(output_dir, f"sorting_algorithms_{plot_type.lower().replace(' ', '_')}_case.png")
    plt.savefig(output_path)
    print(f"Generated plot: {output_path}")
    plt.close()

# --- Main Execution ---
if __name__ == "__main__":
    # Create necessary directories
    os.makedirs(EXECUTABLES_DIR, exist_ok=True)
    os.makedirs(OUTPUT_GRAPHS_DIR, exist_ok=True)

    executables = {}
    for c_file in C_FILES:
        base_name = os.path.splitext(c_file)[0]
        executable_path = os.path.join(EXECUTABLES_DIR, base_name)
        compile_c_code(os.path.join("sorting_algorithms", c_file), executable_path)
        executables[base_name] = executable_path

    all_results = {
        "bubble_sort": {"random": [], "sorted": [], "reverse_sorted": []},
        "heap_sort": {"random": [], "sorted": [], "reverse_sorted": []},
        "insertion_sort": {"random": [], "sorted": [], "reverse_sorted": []},
        "merge_sort": {"random": [], "sorted": [], "reverse_sorted": []},
        "quick_sort": {"random": [], "sorted": [], "reverse_sorted": []},
        "radix_sort": {"random": [], "sorted": [], "reverse_sorted": []},
        "selection_sort": {"random": [], "sorted": [], "reverse_sorted": []},
    }

    # Get all test data files
    test_data_files = [f for f in os.listdir(TEST_DATA_DIR) if f.endswith(".txt")]
    test_data_files.sort(key=lambda x: (extract_n_and_type(x)[0], extract_n_and_type(x)[1]))

    print("\nStarting benchmarking...")
    for data_file in test_data_files:
        n, data_type = extract_n_and_type(data_file)
        if n is None:
            continue
        
        data_filepath = os.path.join(TEST_DATA_DIR, data_file)
        original_data = read_test_data(data_filepath)
        
        print(f"Benchmarking N={n}, Type={data_type}...")

        for algo_base_name, executable_path in executables.items():
            total_time = 0
            for _ in range(NUM_REPETITIONS):
                # Pass a copy of the data because C program might modify it
                time_taken = run_benchmark(executable_path, list(original_data))
                total_time += time_taken
            
            avg_time = total_time / NUM_REPETITIONS
            print(f"  {algo_base_name}: Average time = {avg_time:.6f} s")
            
            # Store results
            all_results[algo_base_name][data_type].append((n, avg_time))

    print("\nBenchmarking complete. Generating plots...")

    # --- Plotting ---
    # Define which data types correspond to best, worst, and average cases for plotting
    # This is a simplification and depends on the specific algorithm.
    # For general sorting algorithms:
    #   - Average Case: Random data
    #   - Worst Case: Reverse-sorted data (for many comparison sorts)
    #   - Best Case: Sorted data (for many comparison sorts)

    # Plot Average Case (using random data)
    avg_case_plot_data = {}
    for algo, types in all_results.items():
        avg_case_plot_data[algo.replace('_', ' ').title()] = types["random"]
    plot_results(avg_case_plot_data, "Average Case (Random Input)", OUTPUT_GRAPHS_DIR)

    # Plot Worst Case (using reverse_sorted data)
    worst_case_plot_data = {}
    for algo, types in all_results.items():
        worst_case_plot_data[algo.replace('_', ' ').title()] = types["reverse_sorted"]
    plot_results(worst_case_plot_data, "Worst Case (Reverse Sorted Input)", OUTPUT_GRAPHS_DIR)

    # Plot Best Case (using sorted data)
    best_case_plot_data = {}
    for algo, types in all_results.items():
        best_case_plot_data[algo.replace('_', ' ').title()] = types["sorted"]
    plot_results(best_case_plot_data, "Best Case (Sorted Input)", OUTPUT_GRAPHS_DIR)

    print("\nAll plots generated successfully.")
    print(f"Results are in the '{OUTPUT_GRAPHS_DIR}' directory.")
    print("\n--- Benchmarking Methodology ---")
    print(f"Each experiment was repeated {NUM_REPETITIONS} times, and the average execution time is reported.")
    print("Timing mechanism: Python's `time.perf_counter()` for high-resolution timing.")
    print("Input selection: Pre-generated test data from the 'test_data/' directory was used.")
    print("Same inputs were used for all sorting algorithms to ensure a fair comparison.")
    print("\nNote on Best/Worst Case Definitions:")
    print("  - Average Case: Represented by 'random' input data.")
    print("  - Worst Case: Represented by 'reverse_sorted' input data. For many comparison sorts (e.g., Bubble, Insertion, Selection, Quick Sort with last/first pivot), this is a true worst-case scenario.")
    print("  - Best Case: Represented by 'sorted' input data. For many comparison sorts (e.g., Insertion, Merge, Heap), sorted data often leads to good performance. However, for Quick Sort with a naive pivot (like the 'quick_sort.c' which uses the last element), sorted data can be a WORST-CASE scenario. The plots will reflect this behavior.")

    # --- Generate Table ---
    print("\n--- Benchmarking Results Table ---")
    table_data = []
    for algo_key, types_data in all_results.items():
        algo_name = algo_key.replace('_', ' ').title()
        for data_type, results_list in types_data.items():
            for n, avg_time in results_list:
                table_data.append({
                    "Algorithm": algo_name,
                    "Input Type": data_type.replace('_', ' ').title(),
                    "Input Size (N)": n,
                    "Average Time (s)": f"{avg_time:.6f}" if avg_time != float('inf') else "Crashed/Timeout"
                })
    
    df = pd.DataFrame(table_data)
    df_sorted = df.sort_values(by=["Input Size (N)", "Input Type", "Algorithm"])
    print(df_sorted.to_string(index=False))

    # Optionally save to CSV
    csv_output_path = os.path.join(OUTPUT_GRAPHS_DIR, "all_sorting_benchmark_results.csv")
    df_sorted.to_csv(csv_output_path, index=False)
    print(f"\nFull results table saved to {csv_output_path}")