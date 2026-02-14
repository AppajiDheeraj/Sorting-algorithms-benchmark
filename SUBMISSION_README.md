# Sorting Algorithms Benchmarking - Submission Guide

This package contains the source code and benchmarking tools used for the CS-253 Practical Assignment.

## Project Structure
- `sorting_algorithms/`: C implementations of all 7 sorting algorithms and Quick Sort variants.
- `benchmark.py`: The main Python script that automates compilation, execution, and data analysis.
- `generate_test_data.py`: Script used to generate the random, sorted, and reverse-sorted datasets.
- `test_data/`: Directory containing the pre-generated input files.
- `graphs/`: (Generated after running) Contains the CSV results and visualization plots.

## Prerequisites
- **C Compiler**: `gcc` (MinGW for Windows or standard GCC for Linux/macOS).
- **Python 3.x**: With the following libraries installed:
  ```bash
  pip install matplotlib pandas numpy scipy
  ```

## How to Run the Benchmarks
1. **Navigate to the project directory**:
   ```bash
   cd Sorting-algorithms-benchmark
   ```
2. **Generate Test Data** (Optional, if not already present):
   ```bash
   python generate_test_data.py
   ```
3. **Run the Benchmark**:
   ```bash
   python benchmark.py
   ```
   *Note: The script will automatically compile the C files into an `executables/` folder and run them against the data in `test_data/`.*

4. **View Results**:
   - Numerical data will be saved in `graphs/csv_data/`.
   - Visualization plots will be available in `graphs/7_sorting_algo_comparisons/` and `graphs/quick_sort_analysis/`.

## Authors
- Appaji Nagaraja Dheeraj (241CS110)
- Adarsh Malipatil (241CS102)

---

### Terminal Output

```
PS C:\Users\Appaji Dheeraj\OneDrive\Desktop\OS_Labs\Sorting-algorithms-benchmark> python .\benchmark.py
Compiling sorting_algorithms\bubble_sort.c...
Successfully compiled sorting_algorithms\bubble_sort.c to executables\bubble_sort
Compiling sorting_algorithms\heap_sort.c...
Successfully compiled sorting_algorithms\heap_sort.c to executables\heap_sort
Compiling sorting_algorithms\insertion_sort.c...
Successfully compiled sorting_algorithms\insertion_sort.c to executables\insertion_sort
Compiling sorting_algorithms\merge_sort.c...
Successfully compiled sorting_algorithms\merge_sort.c to executables\merge_sort
Compiling sorting_algorithms\quick_sort_median_of_three_pivot.c...
Successfully compiled sorting_algorithms\quick_sort_median_of_three_pivot.c to executables\quick_sort_median_of_three_pivot
Compiling sorting_algorithms\radix_sort.c...
Successfully compiled sorting_algorithms\radix_sort.c to executables\radix_sort
Compiling sorting_algorithms\selection_sort.c...
Successfully compiled sorting_algorithms\selection_sort.c to executables\selection_sort
Compiling sorting_algorithms\quick_sort_first_pivot.c...
Successfully compiled sorting_algorithms\quick_sort_first_pivot.c to executables\quick_sort_first_pivot
Compiling sorting_algorithms\quick_sort_median_of_three_pivot.c...
Successfully compiled sorting_algorithms\quick_sort_median_of_three_pivot.c to executables\quick_sort_median_of_three_pivot
Compiling sorting_algorithms\quick_sort_random_pivot.c...
Successfully compiled sorting_algorithms\quick_sort_random_pivot.c to executables\quick_sort_random_pivot

Starting benchmarking...
Benchmarking N=100, Type=random...
  bubble_sort: Time = 0.000018 s, Comparisons = 4929
  heap_sort: Time = 0.000007 s, Comparisons = 1026
  insertion_sort: Time = 0.000005 s, Comparisons = 2619
  merge_sort: Time = 0.000016 s, Comparisons = 540
  quick_sort_median_of_three_pivot: Time = 0.000005 s, Comparisons = 716
  radix_sort: Time = 0.000004 s, Comparisons = 99
  selection_sort: Time = 0.000010 s, Comparisons = 4950
  quick_sort_first_pivot: Time = 0.000005 s, Comparisons = 587
  quick_sort_median_of_three_pivot: Time = 0.000005 s, Comparisons = 716
  quick_sort_random_pivot: Time = 0.000007 s, Comparisons = 677
Benchmarking N=100, Type=reverse_sorted...
  bubble_sort: Time = 0.000020 s, Comparisons = 4950
  heap_sort: Time = 0.000006 s, Comparisons = 944
  insertion_sort: Time = 0.000011 s, Comparisons = 4950
  merge_sort: Time = 0.000014 s, Comparisons = 316
  quick_sort_median_of_three_pivot: Time = 0.000004 s, Comparisons = 868
  radix_sort: Time = 0.000004 s, Comparisons = 99
  selection_sort: Time = 0.000009 s, Comparisons = 4950
  quick_sort_first_pivot: Time = 0.000011 s, Comparisons = 4950
  quick_sort_median_of_three_pivot: Time = 0.000004 s, Comparisons = 868
  quick_sort_random_pivot: Time = 0.000006 s, Comparisons = 668
Benchmarking N=100, Type=sorted...
  bubble_sort: Time = 0.000000 s, Comparisons = 99
  heap_sort: Time = 0.000007 s, Comparisons = 1081
  insertion_sort: Time = 0.000000 s, Comparisons = 99
  merge_sort: Time = 0.000013 s, Comparisons = 356
  quick_sort_median_of_three_pivot: Time = 0.000002 s, Comparisons = 669
  radix_sort: Time = 0.000003 s, Comparisons = 99
  selection_sort: Time = 0.000009 s, Comparisons = 4950
  quick_sort_first_pivot: Time = 0.000009 s, Comparisons = 4950
  quick_sort_median_of_three_pivot: Time = 0.000002 s, Comparisons = 669
  quick_sort_random_pivot: Time = 0.000005 s, Comparisons = 856
Benchmarking N=500, Type=random...
  bubble_sort: Time = 0.000322 s, Comparisons = 124672
  heap_sort: Time = 0.000052 s, Comparisons = 7405
  insertion_sort: Time = 0.000127 s, Comparisons = 63376
  merge_sort: Time = 0.000072 s, Comparisons = 3840
  quick_sort_median_of_three_pivot: Time = 0.000031 s, Comparisons = 5137
  radix_sort: Time = 0.000017 s, Comparisons = 499
  selection_sort: Time = 0.000220 s, Comparisons = 124750
  quick_sort_first_pivot: Time = 0.000030 s, Comparisons = 4588
  quick_sort_median_of_three_pivot: Time = 0.000032 s, Comparisons = 5137
  quick_sort_random_pivot: Time = 0.000037 s, Comparisons = 4840
Benchmarking N=500, Type=reverse_sorted...
  bubble_sort: Time = 0.000315 s, Comparisons = 124750
  heap_sort: Time = 0.000042 s, Comparisons = 7010
  insertion_sort: Time = 0.000285 s, Comparisons = 124750
  merge_sort: Time = 0.000051 s, Comparisons = 2216
  quick_sort_median_of_three_pivot: Time = 0.000019 s, Comparisons = 6790
  radix_sort: Time = 0.000013 s, Comparisons = 499
  selection_sort: Time = 0.000223 s, Comparisons = 124750
  quick_sort_first_pivot: Time = 0.000317 s, Comparisons = 124750
  quick_sort_median_of_three_pivot: Time = 0.000019 s, Comparisons = 6790
  quick_sort_random_pivot: Time = 0.000026 s, Comparisons = 4727
Benchmarking N=500, Type=sorted...
  bubble_sort: Time = 0.000001 s, Comparisons = 499
  heap_sort: Time = 0.000044 s, Comparisons = 7756
  insertion_sort: Time = 0.000001 s, Comparisons = 499
  merge_sort: Time = 0.000051 s, Comparisons = 2272
  quick_sort_median_of_three_pivot: Time = 0.000011 s, Comparisons = 4263
  radix_sort: Time = 0.000014 s, Comparisons = 499
  selection_sort: Time = 0.000227 s, Comparisons = 124750
  quick_sort_first_pivot: Time = 0.000231 s, Comparisons = 124750
  quick_sort_median_of_three_pivot: Time = 0.000011 s, Comparisons = 4263
  quick_sort_random_pivot: Time = 0.000022 s, Comparisons = 4433
Benchmarking N=1000, Type=random...
  bubble_sort: Time = 0.001382 s, Comparisons = 498680
  heap_sort: Time = 0.000113 s, Comparisons = 16878
  insertion_sort: Time = 0.000501 s, Comparisons = 251240
  merge_sort: Time = 0.000145 s, Comparisons = 8704
  quick_sort_median_of_three_pivot: Time = 0.000062 s, Comparisons = 11473
  radix_sort: Time = 0.000036 s, Comparisons = 999
  selection_sort: Time = 0.000899 s, Comparisons = 499500
  quick_sort_first_pivot: Time = 0.000063 s, Comparisons = 11133
  quick_sort_median_of_three_pivot: Time = 0.000064 s, Comparisons = 11473
  quick_sort_random_pivot: Time = 0.000072 s, Comparisons = 10462
Benchmarking N=1000, Type=reverse_sorted...
  bubble_sort: Time = 0.001234 s, Comparisons = 499500
  heap_sort: Time = 0.000098 s, Comparisons = 15965
  insertion_sort: Time = 0.001009 s, Comparisons = 499500
  merge_sort: Time = 0.000100 s, Comparisons = 4932
  quick_sort_median_of_three_pivot: Time = 0.000039 s, Comparisons = 15849
  radix_sort: Time = 0.000028 s, Comparisons = 999
  selection_sort: Time = 0.000901 s, Comparisons = 499500
  quick_sort_first_pivot: Time = 0.001090 s, Comparisons = 499500
  quick_sort_median_of_three_pivot: Time = 0.000043 s, Comparisons = 15849
  quick_sort_random_pivot: Time = 0.000053 s, Comparisons = 10492
Benchmarking N=1000, Type=sorted...
  bubble_sort: Time = 0.000002 s, Comparisons = 999
  heap_sort: Time = 0.000107 s, Comparisons = 17583
  insertion_sort: Time = 0.000002 s, Comparisons = 999
  merge_sort: Time = 0.000097 s, Comparisons = 5044
  quick_sort_median_of_three_pivot: Time = 0.000021 s, Comparisons = 9520
  radix_sort: Time = 0.000028 s, Comparisons = 999
  selection_sort: Time = 0.000925 s, Comparisons = 499500
  quick_sort_first_pivot: Time = 0.000913 s, Comparisons = 499500
  quick_sort_median_of_three_pivot: Time = 0.000020 s, Comparisons = 9520
  quick_sort_random_pivot: Time = 0.000044 s, Comparisons = 10732
Benchmarking N=5000, Type=random...
  bubble_sort: Time = 0.027815 s, Comparisons = 12493672
  heap_sort: Time = 0.000717 s, Comparisons = 107585
  insertion_sort: Time = 0.012253 s, Comparisons = 6179345
  merge_sort: Time = 0.000755 s, Comparisons = 55262
  quick_sort_median_of_three_pivot: Time = 0.000386 s, Comparisons = 69100
  radix_sort: Time = 0.000220 s, Comparisons = 4999
  selection_sort: Time = 0.021407 s, Comparisons = 12497500
  quick_sort_first_pivot: Time = 0.000344 s, Comparisons = 69969
  quick_sort_median_of_three_pivot: Time = 0.000367 s, Comparisons = 69100
  quick_sort_random_pivot: Time = 0.000429 s, Comparisons = 73235
Benchmarking N=5000, Type=reverse_sorted...
  bubble_sort: Time = 0.028985 s, Comparisons = 12497500
  heap_sort: Time = 0.000530 s, Comparisons = 103227
  insertion_sort: Time = 0.023443 s, Comparisons = 12497500
  merge_sort: Time = 0.000489 s, Comparisons = 29804
  quick_sort_median_of_three_pivot: Time = 0.000261 s, Comparisons = 106182
  radix_sort: Time = 0.000165 s, Comparisons = 4999
  selection_sort: Time = 0.020846 s, Comparisons = 12497500
  quick_sort_first_pivot: Time = 0.024646 s, Comparisons = 12497500
  quick_sort_median_of_three_pivot: Time = 0.000247 s, Comparisons = 106182
  quick_sort_random_pivot: Time = 0.000281 s, Comparisons = 70092
Benchmarking N=5000, Type=sorted...
  bubble_sort: Time = 0.000010 s, Comparisons = 4999
  heap_sort: Time = 0.000614 s, Comparisons = 112126
  insertion_sort: Time = 0.000009 s, Comparisons = 4999
  merge_sort: Time = 0.000497 s, Comparisons = 32004
  quick_sort_median_of_three_pivot: Time = 0.000138 s, Comparisons = 60678
  radix_sort: Time = 0.000162 s, Comparisons = 4999
  selection_sort: Time = 0.021105 s, Comparisons = 12497500
  quick_sort_first_pivot: Time = 0.020358 s, Comparisons = 12497500
  quick_sort_median_of_three_pivot: Time = 0.000131 s, Comparisons = 60678
  quick_sort_random_pivot: Time = 0.000232 s, Comparisons = 71401
Benchmarking N=10000, Type=random...
  bubble_sort: Time = 0.113006 s, Comparisons = 49988672
  heap_sort: Time = 0.001479 s, Comparisons = 235490
  insertion_sort: Time = 0.047454 s, Comparisons = 24806136
  merge_sort: Time = 0.001842 s, Comparisons = 120399
  quick_sort_median_of_three_pivot: Time = 0.000808 s, Comparisons = 153146
  radix_sort: Time = 0.000396 s, Comparisons = 9999
  selection_sort: Time = 0.083987 s, Comparisons = 49995000
  quick_sort_first_pivot: Time = 0.000747 s, Comparisons = 156301
  quick_sort_median_of_three_pivot: Time = 0.000746 s, Comparisons = 153146
  quick_sort_random_pivot: Time = 0.000942 s, Comparisons = 157820
Benchmarking N=10000, Type=reverse_sorted...
  bubble_sort: Time = 0.117618 s, Comparisons = 49995000
  heap_sort: Time = 0.001246 s, Comparisons = 226682
  insertion_sort: Time = 0.092417 s, Comparisons = 49995000
  merge_sort: Time = 0.000997 s, Comparisons = 64608
  quick_sort_median_of_three_pivot: Time = 0.000535 s, Comparisons = 234923
  radix_sort: Time = 0.000329 s, Comparisons = 9999
  selection_sort: Time = 0.084492 s, Comparisons = 49995000
  quick_sort_first_pivot: Time = 0.097727 s, Comparisons = 49995000
  quick_sort_median_of_three_pivot: Time = 0.000572 s, Comparisons = 234923
  quick_sort_random_pivot: Time = 0.000558 s, Comparisons = 165532
Benchmarking N=10000, Type=sorted...
  bubble_sort: Time = 0.000019 s, Comparisons = 9999
  heap_sort: Time = 0.001125 s, Comparisons = 244460
  insertion_sort: Time = 0.000017 s, Comparisons = 9999
  merge_sort: Time = 0.000962 s, Comparisons = 69008
  quick_sort_median_of_three_pivot: Time = 0.000278 s, Comparisons = 131343
  radix_sort: Time = 0.000383 s, Comparisons = 9999
  selection_sort: Time = 0.086273 s, Comparisons = 49995000
  quick_sort_first_pivot: Time = 0.084633 s, Comparisons = 49995000
  quick_sort_median_of_three_pivot: Time = 0.000288 s, Comparisons = 131343
  quick_sort_random_pivot: Time = 0.000472 s, Comparisons = 153346
Benchmarking N=25000, Type=random...
  bubble_sort: Time = 1.020484 s, Comparisons = 312440529
  heap_sort: Time = 0.003945 s, Comparisons = 654836
  insertion_sort: Time = 0.290027 s, Comparisons = 156474911
  merge_sort: Time = 0.004164 s, Comparisons = 334086
  quick_sort_median_of_three_pivot: Time = 0.002249 s, Comparisons = 412865
  radix_sort: Time = 0.000955 s, Comparisons = 24999
  selection_sort: Time = 0.547672 s, Comparisons = 312487500
  quick_sort_first_pivot: Time = 0.002088 s, Comparisons = 437160
  quick_sort_median_of_three_pivot: Time = 0.002155 s, Comparisons = 412865
  quick_sort_random_pivot: Time = 0.002384 s, Comparisons = 446895
Benchmarking N=25000, Type=reverse_sorted...
  bubble_sort: Time = 0.704165 s, Comparisons = 312487500
  heap_sort: Time = 0.003413 s, Comparisons = 633719
  insertion_sort: Time = 0.566661 s, Comparisons = 312487500
  merge_sort: Time = 0.002608 s, Comparisons = 178756
  quick_sort_median_of_three_pivot: Time = 0.001456 s, Comparisons = 660758
  radix_sort: Time = 0.000972 s, Comparisons = 24999
  selection_sort: Time = 0.545617 s, Comparisons = 312487500
  quick_sort_first_pivot: Time = 0.625080 s, Comparisons = 312487500
  quick_sort_median_of_three_pivot: Time = 0.001507 s, Comparisons = 660758
  quick_sort_random_pivot: Time = 0.001412 s, Comparisons = 441969
Benchmarking N=25000, Type=sorted...
  bubble_sort: Time = 0.000048 s, Comparisons = 24999
  heap_sort: Time = 0.002993 s, Comparisons = 677688
  insertion_sort: Time = 0.000041 s, Comparisons = 24999
  merge_sort: Time = 0.002588 s, Comparisons = 188476
  quick_sort_median_of_three_pivot: Time = 0.000799 s, Comparisons = 366397
  radix_sort: Time = 0.000967 s, Comparisons = 24999
  selection_sort: Time = 0.553209 s, Comparisons = 312487500
  quick_sort_first_pivot: Time = 0.537556 s, Comparisons = 312487500
  quick_sort_median_of_three_pivot: Time = 0.000770 s, Comparisons = 366397
  quick_sort_random_pivot: Time = 0.001548 s, Comparisons = 600104
Benchmarking N=50000, Type=random...
  bubble_sort: Time = 4.497194 s, Comparisons = 1249886169
  heap_sort: Time = 0.009122 s, Comparisons = 1409620
  insertion_sort: Time = 1.136402 s, Comparisons = 624641029
  merge_sort: Time = 0.008813 s, Comparisons = 718247
  quick_sort_median_of_three_pivot: Time = 0.004768 s, Comparisons = 875720
  radix_sort: Time = 0.002332 s, Comparisons = 49999
  selection_sort: Time = 2.189686 s, Comparisons = 1249975000
  quick_sort_first_pivot: Time = 0.004375 s, Comparisons = 923491
  quick_sort_median_of_three_pivot: Time = 0.004756 s, Comparisons = 875720
  quick_sort_random_pivot: Time = 0.005043 s, Comparisons = 931636
Benchmarking N=50000, Type=reverse_sorted...
  bubble_sort: Time = 2.770762 s, Comparisons = 1249975000
  heap_sort: Time = 0.006886 s, Comparisons = 1366047
  insertion_sort: Time = 2.256765 s, Comparisons = 1249975000
  merge_sort: Time = 0.005370 s, Comparisons = 382512
  quick_sort_median_of_three_pivot: Time = 0.003257 s, Comparisons = 1433133
  radix_sort: Time = 0.002049 s, Comparisons = 49999
  selection_sort: Time = 2.173029 s, Comparisons = 1249975000
  quick_sort_first_pivot: Time = 2.470309 s, Comparisons = 1249975000
  quick_sort_median_of_three_pivot: Time = 0.003234 s, Comparisons = 1433133
  quick_sort_random_pivot: Time = 0.002977 s, Comparisons = 943754
Benchmarking N=50000, Type=sorted...
  bubble_sort: Time = 0.000094 s, Comparisons = 49999
  heap_sort: Time = 0.007051 s, Comparisons = 1455438
  insertion_sort: Time = 0.000093 s, Comparisons = 49999
  merge_sort: Time = 0.005632 s, Comparisons = 401952
  quick_sort_median_of_three_pivot: Time = 0.001697 s, Comparisons = 782782
  radix_sort: Time = 0.001888 s, Comparisons = 49999
  selection_sort: Time = 2.203945 s, Comparisons = 1249975000
  quick_sort_first_pivot: Time = 2.154354 s, Comparisons = 1249975000
  quick_sort_median_of_three_pivot: Time = 0.001818 s, Comparisons = 782782
  quick_sort_random_pivot: Time = 0.003305 s, Comparisons = 1261677
Benchmarking N=75000, Type=random...
  bubble_sort: Time = 10.661124 s, Comparisons = 2812377422
  heap_sort: Time = 0.013260 s, Comparisons = 2200165
  insertion_sort: Time = 2.652428 s, Comparisons = 1406654900
  merge_sort: Time = 0.013320 s, Comparisons = 1121211
  quick_sort_median_of_three_pivot: Time = 0.006921 s, Comparisons = 1380517
  radix_sort: Time = 0.003686 s, Comparisons = 74999
  selection_sort: Time = 5.102751 s, Comparisons = 2812462500
  quick_sort_first_pivot: Time = 0.006966 s, Comparisons = 1401422
  quick_sort_median_of_three_pivot: Time = 0.007225 s, Comparisons = 1380517
  quick_sort_random_pivot: Time = 0.007776 s, Comparisons = 1401884
Benchmarking N=75000, Type=reverse_sorted...
  bubble_sort: Time = 6.307536 s, Comparisons = 2812462500
  heap_sort: Time = 0.009603 s, Comparisons = 2138650
  insertion_sort: Time = 5.106620 s, Comparisons = 2812462500
  merge_sort: Time = 0.007943 s, Comparisons = 594612
  quick_sort_median_of_three_pivot: Time = 0.005171 s, Comparisons = 2272487
  radix_sort: Time = 0.003217 s, Comparisons = 74999
  selection_sort: Time = 4.916955 s, Comparisons = 2812462500
  quick_sort_first_pivot: Time = 5.603166 s, Comparisons = 2812462500
  quick_sort_median_of_three_pivot: Time = 0.005262 s, Comparisons = 2272487
  quick_sort_random_pivot: Time = 0.004735 s, Comparisons = 1452608
Benchmarking N=75000, Type=sorted...
  bubble_sort: Time = 0.000142 s, Comparisons = 74999
  heap_sort: Time = 0.010050 s, Comparisons = 2268087
  insertion_sort: Time = 0.000123 s, Comparisons = 74999
  merge_sort: Time = 0.008164 s, Comparisons = 624316
  quick_sort_median_of_three_pivot: Time = 0.002556 s, Comparisons = 1195642
  radix_sort: Time = 0.002999 s, Comparisons = 74999
  selection_sort: Time = 5.400607 s, Comparisons = 2812462500
  quick_sort_first_pivot: Time = 5.325701 s, Comparisons = 2812462500
  quick_sort_median_of_three_pivot: Time = 0.002466 s, Comparisons = 1195642
  quick_sort_random_pivot: Time = 0.005357 s, Comparisons = 2142049
Benchmarking N=100000, Type=random...
  bubble_sort: Time = 18.934788 s, Comparisons = 4999861169
  heap_sort: Time = 0.018448 s, Comparisons = 3019305
  insertion_sort: Time = 4.546540 s, Comparisons = 2494946890
  merge_sort: Time = 0.018090 s, Comparisons = 1536607
  quick_sort_median_of_three_pivot: Time = 0.009721 s, Comparisons = 1889643
  radix_sort: Time = 0.004706 s, Comparisons = 99999
  selection_sort: Time = 8.877578 s, Comparisons = 4999950000
  quick_sort_first_pivot: Time = 0.009497 s, Comparisons = 2007941
  quick_sort_median_of_three_pivot: Time = 0.009709 s, Comparisons = 1889643
  quick_sort_random_pivot: Time = 0.010930 s, Comparisons = 1971608
Benchmarking N=100000, Type=reverse_sorted...
  bubble_sort: Time = 11.150289 s, Comparisons = 4999950000
  heap_sort: Time = 0.013819 s, Comparisons = 2926640
  insertion_sort: Time = 9.111691 s, Comparisons = 4999950000
  merge_sort: Time = 0.010854 s, Comparisons = 815024
  quick_sort_median_of_three_pivot: Time = 0.006941 s, Comparisons = 3107283
  radix_sort: Time = 0.003925 s, Comparisons = 99999
  selection_sort: Time = 8.739415 s, Comparisons = 4999950000
  quick_sort_first_pivot: Time = 9.993032 s, Comparisons = 4999950000
  quick_sort_median_of_three_pivot: Time = 0.006874 s, Comparisons = 3107283
  quick_sort_random_pivot: Time = 0.006447 s, Comparisons = 2101616
Benchmarking N=100000, Type=sorted...
  bubble_sort: Time = 0.000214 s, Comparisons = 99999
  heap_sort: Time = 0.013519 s, Comparisons = 3112517
  insertion_sort: Time = 0.000164 s, Comparisons = 99999
  merge_sort: Time = 0.011038 s, Comparisons = 853904
  quick_sort_median_of_three_pivot: Time = 0.003801 s, Comparisons = 1665551
  radix_sort: Time = 0.003955 s, Comparisons = 99999
  selection_sort: Time = 8.879359 s, Comparisons = 4999950000
  quick_sort_first_pivot: Time = 8.709523 s, Comparisons = 4999950000
  quick_sort_median_of_three_pivot: Time = 0.003598 s, Comparisons = 1665551
  quick_sort_random_pivot: Time = 0.007291 s, Comparisons = 2879163

Benchmarking complete. Generating plots...
Generated plot: graphs\7_sorting_algo_comparisons\sorting_algorithms_average_case_(random_input)_case_time.png
Generated plot: graphs\7_sorting_algo_comparisons\sorting_algorithms_average_case_(random_input)_case_time_log_scale.png
Generated plot: graphs\7_sorting_algo_comparisons\sorting_algorithms_worst_case_(reverse_sorted_input)_case_time.png
Generated plot: graphs\7_sorting_algo_comparisons\sorting_algorithms_worst_case_(reverse_sorted_input)_case_time_log_scale.png
Generated plot: graphs\7_sorting_algo_comparisons\sorting_algorithms_best_case_(sorted_input)_case_time.png
Generated plot: graphs\7_sorting_algo_comparisons\sorting_algorithms_best_case_(sorted_input)_case_time_log_scale.png
Generated plot: graphs\7_sorting_algo_comparisons\sorting_algorithms_average_case_(random_input)_case_comparisons.png
Generated plot: graphs\7_sorting_algo_comparisons\sorting_algorithms_average_case_(random_input)_case_comparisons_log_scale.png
Generated plot: graphs\7_sorting_algo_comparisons\sorting_algorithms_worst_case_(reverse_sorted_input)_case_comparisons.png
Generated plot: graphs\7_sorting_algo_comparisons\sorting_algorithms_worst_case_(reverse_sorted_input)_case_comparisons_log_scale.png
Generated plot: graphs\7_sorting_algo_comparisons\sorting_algorithms_best_case_(sorted_input)_case_comparisons.png
Generated plot: graphs\7_sorting_algo_comparisons\sorting_algorithms_best_case_(sorted_input)_case_comparisons_log_scale.png
Generated correlation plot: graphs\7_sorting_algo_comparisons\time_vs_comparisons_correlation.png

Generating QuickSort variant plots...
Generated plot: graphs\quick_sort_analysis\sorting_algorithms_average_case_(random_input)_case_time.png
Generated plot: graphs\quick_sort_analysis\sorting_algorithms_average_case_(random_input)_case_time_log_scale.png
Generated plot: graphs\quick_sort_analysis\sorting_algorithms_worst_case_(reverse_sorted_input)_case_time.png
Generated plot: graphs\quick_sort_analysis\sorting_algorithms_worst_case_(reverse_sorted_input)_case_time_log_scale.png
Generated plot: graphs\quick_sort_analysis\sorting_algorithms_best_case_(sorted_input)_case_time.png
Generated plot: graphs\quick_sort_analysis\sorting_algorithms_best_case_(sorted_input)_case_time_log_scale.png
Generated plot: graphs\quick_sort_analysis\sorting_algorithms_average_case_(random_input)_case_comparisons.png
Generated plot: graphs\quick_sort_analysis\sorting_algorithms_average_case_(random_input)_case_comparisons_log_scale.png
Generated plot: graphs\quick_sort_analysis\sorting_algorithms_worst_case_(reverse_sorted_input)_case_comparisons.png
Generated plot: graphs\quick_sort_analysis\sorting_algorithms_worst_case_(reverse_sorted_input)_case_comparisons_log_scale.png
Generated plot: graphs\quick_sort_analysis\sorting_algorithms_best_case_(sorted_input)_case_comparisons.png
Generated plot: graphs\quick_sort_analysis\sorting_algorithms_best_case_(sorted_input)_case_comparisons_log_scale.png
Generated correlation plot: graphs\quick_sort_analysis\time_vs_comparisons_correlation.png

All plots generated successfully.
Results are in the 'graphs' directory.
  - 7 sorting algorithm comparisons: 'graphs\7_sorting_algo_comparisons'
  - Quick sort analysis: 'graphs\quick_sort_analysis'
  - CSV data: 'graphs\csv_data'

--- Benchmarking Methodology ---
Each experiment was repeated 7 times, and the average execution time is reported.
Timing mechanism: Python's `time.perf_counter()` for high-resolution timing.
Comparison counting: Instrumented C code tracks all element comparisons.
Input selection: Pre-generated test data from the 'test_data/' directory was used.
Same inputs were used for all sorting algorithms to ensure a fair comparison.

Note on Best/Worst Case Definitions:
  - Average Case: Represented by 'random' input data.
  - Worst Case: Represented by 'reverse_sorted' input data.
  - Best Case: Represented by 'sorted' input data.

Correlation Analysis:
  The correlation plots show the relationship between the number of comparisons
  and execution time. A high correlation (close to 1.0) indicates that comparisons
  are a strong predictor of execution time for that algorithm.

--- Benchmarking Results Table ---
                   Algorithm     Input Type  Input Size (N) Average Time (s) Average Comparisons
                 Bubble Sort         Random             100         0.000018                4929       
                   Heap Sort         Random             100         0.000007                1026       
              Insertion Sort         Random             100         0.000005                2619       
                  Merge Sort         Random             100         0.000016                 540       
Quick Sort (Median of Three)         Random             100         0.000005                 716       
                  Radix Sort         Random             100         0.000004                  99       
              Selection Sort         Random             100         0.000010                4950       
                 Bubble Sort Reverse Sorted             100         0.000020                4950       
                   Heap Sort Reverse Sorted             100         0.000006                 944       
              Insertion Sort Reverse Sorted             100         0.000011                4950       
                  Merge Sort Reverse Sorted             100         0.000014                 316       
Quick Sort (Median of Three) Reverse Sorted             100         0.000004                 868       
                  Radix Sort Reverse Sorted             100         0.000004                  99       
              Selection Sort Reverse Sorted             100         0.000009                4950       
                 Bubble Sort         Sorted             100         0.000000                  99       
                   Heap Sort         Sorted             100         0.000007                1081       
              Insertion Sort         Sorted             100         0.000000                  99       
                  Merge Sort         Sorted             100         0.000013                 356       
Quick Sort (Median of Three)         Sorted             100         0.000002                 669       
                  Radix Sort         Sorted             100         0.000003                  99       
              Selection Sort         Sorted             100         0.000009                4950       
                 Bubble Sort         Random             500         0.000322              124672       
                   Heap Sort         Random             500         0.000052                7405       
              Insertion Sort         Random             500         0.000127               63376       
                  Merge Sort         Random             500         0.000072                3840       
Quick Sort (Median of Three)         Random             500         0.000031                5137       
                  Radix Sort         Random             500         0.000017                 499       
              Selection Sort         Random             500         0.000220              124750       
                 Bubble Sort Reverse Sorted             500         0.000315              124750       
                   Heap Sort Reverse Sorted             500         0.000042                7010       
              Insertion Sort Reverse Sorted             500         0.000285              124750       
                  Merge Sort Reverse Sorted             500         0.000051                2216       
Quick Sort (Median of Three) Reverse Sorted             500         0.000019                6790       
                  Radix Sort Reverse Sorted             500         0.000013                 499       
              Selection Sort Reverse Sorted             500         0.000223              124750       
                 Bubble Sort         Sorted             500         0.000001                 499       
                   Heap Sort         Sorted             500         0.000044                7756       
              Insertion Sort         Sorted             500         0.000001                 499       
                  Merge Sort         Sorted             500         0.000051                2272       
Quick Sort (Median of Three)         Sorted             500         0.000011                4263       
                  Radix Sort         Sorted             500         0.000014                 499       
              Selection Sort         Sorted             500         0.000227              124750       
                 Bubble Sort         Random            1000         0.001382              498680       
                   Heap Sort         Random            1000         0.000113               16878       
              Insertion Sort         Random            1000         0.000501              251240       
                  Merge Sort         Random            1000         0.000145                8704       
Quick Sort (Median of Three)         Random            1000         0.000062               11473       
                  Radix Sort         Random            1000         0.000036                 999       
              Selection Sort         Random            1000         0.000899              499500       
                 Bubble Sort Reverse Sorted            1000         0.001234              499500       
                   Heap Sort Reverse Sorted            1000         0.000098               15965       
              Insertion Sort Reverse Sorted            1000         0.001009              499500       
                  Merge Sort Reverse Sorted            1000         0.000100                4932       
Quick Sort (Median of Three) Reverse Sorted            1000         0.000039               15849       
                  Radix Sort Reverse Sorted            1000         0.000028                 999       
              Selection Sort Reverse Sorted            1000         0.000901              499500       
                 Bubble Sort         Sorted            1000         0.000002                 999       
                   Heap Sort         Sorted            1000         0.000107               17583       
              Insertion Sort         Sorted            1000         0.000002                 999       
                  Merge Sort         Sorted            1000         0.000097                5044       
Quick Sort (Median of Three)         Sorted            1000         0.000021                9520       
                  Radix Sort         Sorted            1000         0.000028                 999       
              Selection Sort         Sorted            1000         0.000925              499500       
                 Bubble Sort         Random            5000         0.027815            12493672       
                   Heap Sort         Random            5000         0.000717              107585       
              Insertion Sort         Random            5000         0.012253             6179345       
                  Merge Sort         Random            5000         0.000755               55262       
Quick Sort (Median of Three)         Random            5000         0.000386               69100       
                  Radix Sort         Random            5000         0.000220                4999       
              Selection Sort         Random            5000         0.021407            12497500       
                 Bubble Sort Reverse Sorted            5000         0.028985            12497500       
                   Heap Sort Reverse Sorted            5000         0.000530              103227       
              Insertion Sort Reverse Sorted            5000         0.023443            12497500       
                  Merge Sort Reverse Sorted            5000         0.000489               29804       
Quick Sort (Median of Three) Reverse Sorted            5000         0.000261              106182       
                  Radix Sort Reverse Sorted            5000         0.000165                4999       
              Selection Sort Reverse Sorted            5000         0.020846            12497500       
                 Bubble Sort         Sorted            5000         0.000010                4999       
                   Heap Sort         Sorted            5000         0.000614              112126       
              Insertion Sort         Sorted            5000         0.000009                4999       
                  Merge Sort         Sorted            5000         0.000497               32004       
Quick Sort (Median of Three)         Sorted            5000         0.000138               60678       
                  Radix Sort         Sorted            5000         0.000162                4999       
              Selection Sort         Sorted            5000         0.021105            12497500       
                 Bubble Sort         Random           10000         0.113006            49988672       
                   Heap Sort         Random           10000         0.001479              235490       
              Insertion Sort         Random           10000         0.047454            24806136       
                  Merge Sort         Random           10000         0.001842              120399       
Quick Sort (Median of Three)         Random           10000         0.000808              153146       
                  Radix Sort         Random           10000         0.000396                9999       
              Selection Sort         Random           10000         0.083987            49995000       
                 Bubble Sort Reverse Sorted           10000         0.117618            49995000       
                   Heap Sort Reverse Sorted           10000         0.001246              226682       
              Insertion Sort Reverse Sorted           10000         0.092417            49995000       
                  Merge Sort Reverse Sorted           10000         0.000997               64608       
Quick Sort (Median of Three) Reverse Sorted           10000         0.000535              234923       
                  Radix Sort Reverse Sorted           10000         0.000329                9999       
              Selection Sort Reverse Sorted           10000         0.084492            49995000       
                 Bubble Sort         Sorted           10000         0.000019                9999       
                   Heap Sort         Sorted           10000         0.001125              244460       
              Insertion Sort         Sorted           10000         0.000017                9999       
                  Merge Sort         Sorted           10000         0.000962               69008       
Quick Sort (Median of Three)         Sorted           10000         0.000278              131343       
                  Radix Sort         Sorted           10000         0.000383                9999       
              Selection Sort         Sorted           10000         0.086273            49995000       
                 Bubble Sort         Random           25000         1.020484           312440529       
                   Heap Sort         Random           25000         0.003945              654836       
              Insertion Sort         Random           25000         0.290027           156474911       
                  Merge Sort         Random           25000         0.004164              334086       
Quick Sort (Median of Three)         Random           25000         0.002249              412865       
                  Radix Sort         Random           25000         0.000955               24999       
              Selection Sort         Random           25000         0.547672           312487500       
                 Bubble Sort Reverse Sorted           25000         0.704165           312487500       
                   Heap Sort Reverse Sorted           25000         0.003413              633719       
              Insertion Sort Reverse Sorted           25000         0.566661           312487500       
                  Merge Sort Reverse Sorted           25000         0.002608              178756       
Quick Sort (Median of Three) Reverse Sorted           25000         0.001456              660758       
                  Radix Sort Reverse Sorted           25000         0.000972               24999       
              Selection Sort Reverse Sorted           25000         0.545617           312487500       
                 Bubble Sort         Sorted           25000         0.000048               24999       
                   Heap Sort         Sorted           25000         0.002993              677688       
              Insertion Sort         Sorted           25000         0.000041               24999       
                  Merge Sort         Sorted           25000         0.002588              188476       
Quick Sort (Median of Three)         Sorted           25000         0.000799              366397       
                  Radix Sort         Sorted           25000         0.000967               24999       
              Selection Sort         Sorted           25000         0.553209           312487500       
                 Bubble Sort         Random           50000         4.497194          1249886169       
                   Heap Sort         Random           50000         0.009122             1409620       
              Insertion Sort         Random           50000         1.136402           624641029       
                  Merge Sort         Random           50000         0.008813              718247       
Quick Sort (Median of Three)         Random           50000         0.004768              875720       
                  Radix Sort         Random           50000         0.002332               49999       
              Selection Sort         Random           50000         2.189686          1249975000       
                 Bubble Sort Reverse Sorted           50000         2.770762          1249975000       
                   Heap Sort Reverse Sorted           50000         0.006886             1366047       
              Insertion Sort Reverse Sorted           50000         2.256765          1249975000       
                  Merge Sort Reverse Sorted           50000         0.005370              382512       
Quick Sort (Median of Three) Reverse Sorted           50000         0.003257             1433133       
                  Radix Sort Reverse Sorted           50000         0.002049               49999       
              Selection Sort Reverse Sorted           50000         2.173029          1249975000       
                 Bubble Sort         Sorted           50000         0.000094               49999       
                   Heap Sort         Sorted           50000         0.007051             1455438       
              Insertion Sort         Sorted           50000         0.000093               49999       
                  Merge Sort         Sorted           50000         0.005632              401952       
Quick Sort (Median of Three)         Sorted           50000         0.001697              782782       
                  Radix Sort         Sorted           50000         0.001888               49999       
              Selection Sort         Sorted           50000         2.203945          1249975000       
                 Bubble Sort         Random           75000        10.661124          2812377422       
                   Heap Sort         Random           75000         0.013260             2200165       
              Insertion Sort         Random           75000         2.652428          1406654900       
                  Merge Sort         Random           75000         0.013320             1121211       
Quick Sort (Median of Three)         Random           75000         0.006921             1380517       
                  Radix Sort         Random           75000         0.003686               74999       
              Selection Sort         Random           75000         5.102751          2812462500       
                 Bubble Sort Reverse Sorted           75000         6.307536          2812462500       
                   Heap Sort Reverse Sorted           75000         0.009603             2138650       
              Insertion Sort Reverse Sorted           75000         5.106620          2812462500       
                  Merge Sort Reverse Sorted           75000         0.007943              594612       
Quick Sort (Median of Three) Reverse Sorted           75000         0.005171             2272487       
                  Radix Sort Reverse Sorted           75000         0.003217               74999       
              Selection Sort Reverse Sorted           75000         4.916955          2812462500       
                 Bubble Sort         Sorted           75000         0.000142               74999       
                   Heap Sort         Sorted           75000         0.010050             2268087       
              Insertion Sort         Sorted           75000         0.000123               74999       
                  Merge Sort         Sorted           75000         0.008164              624316       
Quick Sort (Median of Three)         Sorted           75000         0.002556             1195642       
                  Radix Sort         Sorted           75000         0.002999               74999       
              Selection Sort         Sorted           75000         5.400607          2812462500       
                 Bubble Sort         Random          100000        18.934788          4999861169       
                   Heap Sort         Random          100000         0.018448             3019305       
              Insertion Sort         Random          100000         4.546540          2494946890       
                  Merge Sort         Random          100000         0.018090             1536607       
Quick Sort (Median of Three)         Random          100000         0.009721             1889643       
                  Radix Sort         Random          100000         0.004706               99999       
              Selection Sort         Random          100000         8.877578          4999950000       
                 Bubble Sort Reverse Sorted          100000        11.150289          4999950000       
                   Heap Sort Reverse Sorted          100000         0.013819             2926640       
              Insertion Sort Reverse Sorted          100000         9.111691          4999950000       
                  Merge Sort Reverse Sorted          100000         0.010854              815024       
Quick Sort (Median of Three) Reverse Sorted          100000         0.006941             3107283       
                  Radix Sort Reverse Sorted          100000         0.003925               99999       
              Selection Sort Reverse Sorted          100000         8.739415          4999950000       
                 Bubble Sort         Sorted          100000         0.000214               99999       
                   Heap Sort         Sorted          100000         0.013519             3112517       
              Insertion Sort         Sorted          100000         0.000164               99999       
                  Merge Sort         Sorted          100000         0.011038              853904       
Quick Sort (Median of Three)         Sorted          100000         0.003801             1665551       
                  Radix Sort         Sorted          100000         0.003955               99999       
              Selection Sort         Sorted          100000         8.879359          4999950000       

Full results table saved to graphs\csv_data\all_sorting_benchmark_results.csv

--- Correlation Analysis Summary ---
Algorithm                           | Correlation (r) | P-value
----------------------------------------------------------------------
Bubble Sort                         |          0.9615 | 1.5303e-15
Heap Sort                           |          0.9816 | 1.6861e-19
Insertion Sort                      |          1.0000 | 2.9430e-53
Merge Sort                          |          0.9976 | 1.4220e-30
Quick Sort (Median of Three)        |          0.8789 | 1.6330e-09
Radix Sort                          |          0.9933 | 6.4550e-25
Selection Sort                      |          0.9996 | 8.7698e-40

Interpretation:
  r close to 1.0: Strong positive correlation (more comparisons → more time)
  r close to 0.0: Weak/no correlation
  p-value < 0.05: Statistically significant correlation

================================================================================
IMPORTANT NOTES ON RESULTS
================================================================================

⚠️  TIMING MEASUREMENT:
  - Timing is measured INSIDE C code using clock_gettime(CLOCK_MONOTONIC)
  - This eliminates Python subprocess overhead from the measurements
  - Results are now accurate for actual algorithm performance

⚠️  RADIX SORT 'COMPARISONS' NOTE:
  - Radix sort is a NON-COMPARATIVE sorting algorithm
  - It does NOT use element comparisons (like other algorithms)
  - The 'comparisons' count represents operations in getMax() function
  - This value (~n) is NOT comparable to other algorithms' comparisons
  - Use TIME metric, not COMPARISONS, to evaluate radix sort performance

✓ EXPECTED BEHAVIOR:
  - O(n²) algorithms: Bubble, Insertion, Selection Sort
  - O(n log n) algorithms: Heap, Merge, Quick Sort
  - O(n+k) algorithm: Radix Sort (where k is key range)
  - Best case optimized: Bubble & Insertion sort show O(n) for sorted input
================================================================================
```