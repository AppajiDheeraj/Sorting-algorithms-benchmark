#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <stdbool.h>

// --- Helper Functions ---

void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

bool is_sorted(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        if (arr[i] > arr[i + 1]) return false;
    }
    return true;
}

double get_time_seconds() {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return ts.tv_sec + ts.tv_nsec / 1e9;
}

// --- Bubble Sort ---
void bubbleSort(int arr[], int n) {
    int i, j, temp;
    int swapped;
    for (i = 0; i < n - 1; i++) {
        swapped = 0;
        for (j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                swapped = 1;
            }
        }
        if (swapped == 0) break;
    }
}

// --- Selection Sort ---
void selectionSort(int arr[], int n) {
    int i, j, min_idx, temp;
    for (i = 0; i < n - 1; i++) {
        min_idx = i;
        for (j = i + 1; j < n; j++) {
            if (arr[j] < arr[min_idx])
                min_idx = j;
        }
        if (min_idx != i) {
            temp = arr[min_idx];
            arr[min_idx] = arr[i];
            arr[i] = temp;
        }
    }
}

// --- Insertion Sort ---
void insertionSort(int arr[], int n) {
    int i, key, j;
    for (i = 1; i < n; i++) {
        key = arr[i];
        j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}

// --- Merge Sort ---
void merge_internal(int arr[], int l, int m, int r) {
    int i, j, k;
    int n1 = m - l + 1;
    int n2 = r - m;
    int *L = (int*)malloc(n1 * sizeof(int));
    int *R = (int*)malloc(n2 * sizeof(int));
    for (i = 0; i < n1; i++) L[i] = arr[l + i];
    for (j = 0; j < n2; j++) R[j] = arr[m + 1 + j];
    i = 0; j = 0; k = l;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) { arr[k] = L[i]; i++; }
        else { arr[k] = R[j]; j++; }
        k++;
    }
    while (i < n1) { arr[k] = L[i]; i++; k++; }
    while (j < n2) { arr[k] = R[j]; j++; k++; }
    free(L); free(R);
}

void mergeSort_internal(int arr[], int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;
        mergeSort_internal(arr, l, m);
        mergeSort_internal(arr, m + 1, r);
        merge_internal(arr, l, m, r);
    }
}

void mergeSort(int arr[], int n) {
    mergeSort_internal(arr, 0, n - 1);
}

// --- Quick Sort ---
int partition_internal(int arr[], int low, int high) {
    int pivot = arr[high];
    int i = (low - 1);
    for (int j = low; j <= high - 1; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return (i + 1);
}

void quickSort_internal(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition_internal(arr, low, high);
        quickSort_internal(arr, low, pi - 1);
        quickSort_internal(arr, pi + 1, high);
    }
}

void quickSort(int arr[], int n) {
    quickSort_internal(arr, 0, n - 1);
}

// --- Randomized Quick Sort ---
int randomPartition_internal(int arr[], int low, int high) {
    int random = low + rand() % (high - low + 1);
    swap(&arr[random], &arr[high]);
    return partition_internal(arr, low, high);
}

void randomizedQuickSort_internal(int arr[], int low, int high) {
    if (low < high) {
        int pi = randomPartition_internal(arr, low, high);
        randomizedQuickSort_internal(arr, low, pi - 1);
        randomizedQuickSort_internal(arr, pi + 1, high);
    }
}

void randomizedQuickSort(int arr[], int n) {
    randomizedQuickSort_internal(arr, 0, n - 1);
}

// --- Heap Sort ---
void heapify_internal(int arr[], int n, int i) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;
    if (left < n && arr[left] > arr[largest]) largest = left;
    if (right < n && arr[right] > arr[largest]) largest = right;
    if (largest != i) {
        swap(&arr[i], &arr[largest]);
        heapify_internal(arr, n, largest);
    }
}

void heapSort(int arr[], int n) {
    for (int i = n / 2 - 1; i >= 0; i--) heapify_internal(arr, n, i);
    for (int i = n - 1; i > 0; i--) {
        swap(&arr[0], &arr[i]);
        heapify_internal(arr, i, 0);
    }
}

// --- Shell Sort ---
void shellSort(int arr[], int n) {
    for (int gap = n / 2; gap > 0; gap /= 2) {
        for (int i = gap; i < n; i++) {
            int temp = arr[i];
            int j;
            for (j = i; j >= gap && arr[j - gap] > temp; j -= gap) {
                arr[j] = arr[j - gap];
            }
            arr[j] = temp;
        }
    }
}

// --- Counting Sort ---
void countingSort(int arr[], int n) {
    if (n <= 0) return;
    int max = arr[0], min = arr[0];
    for (int i = 1; i < n; i++) {
        if (arr[i] > max) max = arr[i];
        if (arr[i] < min) min = arr[i];
    }
    int range = max - min + 1;
    int *count = (int*)calloc(range, sizeof(int));
    int *output = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) count[arr[i] - min]++;
    for (int i = 1; i < range; i++) count[i] += count[i - 1];
    for (int i = n - 1; i >= 0; i--) {
        output[count[arr[i] - min] - 1] = arr[i];
        count[arr[i] - min]--;
    }
    for (int i = 0; i < n; i++) arr[i] = output[i];
    free(count); free(output);
}

// --- Radix Sort ---
void countingSortForRadix_internal(int arr[], int n, int exp) {
    int *output = (int*)malloc(n * sizeof(int));
    int i, count[10] = {0};
    for (i = 0; i < n; i++) count[(arr[i] / exp) % 10]++;
    for (i = 1; i < 10; i++) count[i] += count[i - 1];
    for (i = n - 1; i >= 0; i--) {
        output[count[(arr[i] / exp) % 10] - 1] = arr[i];
        count[(arr[i] / exp) % 10]--;
    }
    for (i = 0; i < n; i++) arr[i] = output[i];
    free(output);
}

void radixSort(int arr[], int n) {
    if (n <= 0) return;
    int max = arr[0];
    for (int i = 1; i < n; i++) if (arr[i] > max) max = arr[i];
    for (int exp = 1; max / exp > 0; exp *= 10)
        countingSortForRadix_internal(arr, n, exp);
}

// --- Benchmarking Logic ---

typedef void (*SortFunc)(int[], int);

typedef struct {
    char name[30];
    SortFunc func;
    bool is_slow; // O(n^2)
} Algorithm;

int main() {
    srand(42); // Deterministic seed for reproducibility

    Algorithm algos[] = {
        {"Bubble Sort", bubbleSort, true},
        {"Selection Sort", selectionSort, true},
        {"Insertion Sort", insertionSort, true},
        {"Merge Sort", mergeSort, false},
        {"Quick Sort", quickSort, false},
        {"Randomized Quick Sort", randomizedQuickSort, false},
        {"Heap Sort", heapSort, false},
        {"Shell Sort", shellSort, false},
        {"Counting Sort", countingSort, false},
        {"Radix Sort", radixSort, false}
    };
    int num_algos = sizeof(algos) / sizeof(algos[0]);

    int sizes[] = {100, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 1000000};
    int num_sizes = sizeof(sizes) / sizeof(sizes[0]);

    FILE *fp = fopen("benchmark_results.csv", "w");
    if (!fp) {
        perror("Failed to open file");
        return 1;
    }
    fprintf(fp, "Algorithm,Size,Time\n");

    for (int i = 0; i < num_algos; i++) {
        printf("Benchmarking %s...\n", algos[i].name);
        for (int j = 0; j < num_sizes; j++) {
            int n = sizes[j];

            // Skip large sizes for O(n^2) algorithms to avoid excessive wait
            if (algos[i].is_slow && n > 100000) continue;

            // Allocate and generate random array
            int *arr = (int*)malloc(n * sizeof(int));
            for (int k = 0; k < n; k++) arr[k] = rand() % 1000000; // Limit range for Counting Sort

            // Validate correctness (once per algorithm at small size)
            if (j == 0) {
                int *temp_arr = (int*)malloc(n * sizeof(int));
                memcpy(temp_arr, arr, n * sizeof(int));
                algos[i].func(temp_arr, n);
                if (!is_sorted(temp_arr, n)) {
                    fprintf(stderr, "Error: %s failed validation!\n", algos[i].name);
                    free(temp_arr);
                    free(arr);
                    continue;
                }
                free(temp_arr);
            }

            double start = get_time_seconds();
            algos[i].func(arr, n);
            double end = get_time_seconds();
            double duration = end - start;

            fprintf(fp, "%s,%d,%f\n", algos[i].name, n, duration);
            fflush(fp);

            free(arr);

            // If it took too long (> 10s), skip remaining sizes for this slow algorithm
            if (algos[i].is_slow && duration > 10.0) {
                printf("  %s took too long (%.2fs), skipping larger sizes.\n", algos[i].name, duration);
                break;
            }
        }
    }

    fclose(fp);
    printf("Benchmarking complete. Results saved to benchmark_results.csv\n");

    return 0;
}
