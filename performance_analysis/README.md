# Experimental Evaluation of Sorting Algorithms (Python)

## Objective
This lab evaluates multiple sorting algorithms experimentally and **visualizes time-complexity growth using continuous curves**. The experiment emphasizes:

- Efficient input scaling up to **10⁶** elements (with adaptive exclusion of impractical O(n²) algorithms at large *n*)
- High-resolution plotting (publication-ready **PNG** output)
- **Log–log plots** to reveal growth rates
- Comparison of multiple algorithms under multiple input distributions
- Professional figure formatting and reproducible measurement methodology

---

## Algorithms Compared
The following algorithms are implemented in **pure Python** for fair comparison under the same interpreter/runtime:

### Quadratic (O(n²))
- Bubble Sort
- Selection Sort
- Insertion Sort

### Linearithmic (O(n log n))
- Merge Sort
- Quick Sort
- Heap Sort
- Shell Sort
- Tim Sort (Python built-in `sorted`, included as a high-performance baseline)

### Integer / Non-comparison
- Counting Sort (O(n + k))
- Radix Sort (O(d(n + k)))

---

## Input Scaling Strategy (Up to 10⁶)
Naively running O(n²) algorithms up to 10⁶ is infeasible. This experiment uses a **scientifically valid scaling approach**:

- All algorithms are evaluated for small and medium *n*
- For large *n* (above 20,000), quadratic algorithms are excluded to avoid multi-hour runs
- Logarithmic spacing is used to produce smooth, continuous curves across orders of magnitude

This approach preserves the curve shape and clearly demonstrates when quadratic methods become impractical.

---

## Distributions Tested
Each algorithm is evaluated under the following input distributions:

- `random`: uniformly random integers
- `sorted`: already sorted input (best-case for some algorithms)
- `reverse`: reverse sorted (often worst-case for insertion-like sorts)
- `nearly_sorted`: 1% random swaps applied to a sorted array

---

## How to Run
From the `performance_analysis/` directory:

```bash
python3 experiment.py
```

Optional comprehensive figure generation (after running the main experiment):

```bash
python3 visualize_comprehensive.py
```

---

## Outputs
All output files are written to `performance_analysis/outputs/`:

- `results_<distribution>.csv` – raw results per distribution
- `results_all.csv` – all runs combined
- `sorting_performance_loglog_<distribution>.png` – main log–log plots
- `comparison_all_distributions.png` – multi-panel comparison figure
- `complexity_classes.png` – grouped by expected complexity
- `conclusions_<distribution>.txt` – conclusions inferred from curves and estimated slopes

---

## Professional Graph Formatting (What to Look For)
- **Log–log axes** reveal the approximate exponent *k* in \(T(n) \approx n^k\)
- Confidence bands (±1 standard deviation) show run-to-run variability
- Consistent serif fonts and grid styling match academic report standards

---

## Conclusions (Expected from Curves)
When plotted on a log–log scale:

1. **Quadratic algorithms** exhibit steep slopes (≈2) and become unusable early.
2. **O(n log n) algorithms** form shallower, nearly parallel curves.
3. **Counting/Radix sort** can appear close to linear when the integer range/digits remain bounded.
4. **Tim sort** typically dominates comparison-based approaches in practice.

See the generated `conclusions_<distribution>.txt` files for measured log–log slope estimates and distribution-specific comments.
