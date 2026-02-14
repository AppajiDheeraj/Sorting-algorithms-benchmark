#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdint.h>

long long comparison_count = 0;
struct timespec start_time, end_time;

double get_elapsed_time(struct timespec start, struct timespec end) {
    return (end.tv_sec - start.tv_sec) + (end.tv_nsec - start.tv_nsec) / 1e9;
}

int getMax(int arr[], int n) {
    int max = arr[0];
    int i;
    for (i = 1; i < n; i++) {
        comparison_count++;
        if (arr[i] > max)
            max = arr[i];
    }
    return max;
}

void countingSortForRadix(int arr[], int n, int exp) {
    int *output = (int*)malloc(n * sizeof(int));
    int i, count[10] = {0};
    
    for (i = 0; i < n; i++)
        count[(arr[i] / exp) % 10]++;
    
    for (i = 1; i < 10; i++)
        count[i] += count[i - 1];
    
    for (i = n - 1; i >= 0; i--) {
        output[count[(arr[i] / exp) % 10] - 1] = arr[i];
        count[(arr[i] / exp) % 10]--;
    }
    
    for (i = 0; i < n; i++)
        arr[i] = output[i];
    
    free(output);
}

void radixSort(int arr[], int n) {
    int max = getMax(arr, n);
    int exp;
    
    for (exp = 1; max / exp > 0; exp *= 10)
        countingSortForRadix(arr, n, exp);
}

void printArray(int arr[], int size) {
    int i;
    for (i = 0; i < size; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

int main() {
    int n;
    scanf("%d", &n); // Read the number of elements
    int *arr = (int *)malloc(n * sizeof(int));
    if (arr == NULL) {
        return 1; // Error handling for malloc
    }

    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]); // Read elements into the array
    }
    
    clock_gettime(CLOCK_MONOTONIC, &start_time);
    radixSort(arr, n);
    clock_gettime(CLOCK_MONOTONIC, &end_time);
    
    double elapsed = get_elapsed_time(start_time, end_time);
    
    // Print timing and comparison count to stderr
    fprintf(stderr, "TIME: %.9f\n", elapsed);
    fprintf(stderr, "COMPARISONS: %lld\n", comparison_count);
    
    // Optionally print the sorted array, but for benchmarking, we might skip this
    // for (int i = 0; i < n; i++) {
    //     printf("%d ", arr[i]);
    // }
    // printf("\n");
    
    free(arr); // Free dynamically allocated memory
    return 0;
}
