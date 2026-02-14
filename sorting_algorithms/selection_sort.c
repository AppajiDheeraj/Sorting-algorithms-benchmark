#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdint.h>

long long comparison_count = 0;
struct timespec start_time, end_time;

double get_elapsed_time(struct timespec start, struct timespec end) {
    return (end.tv_sec - start.tv_sec) + (end.tv_nsec - start.tv_nsec) / 1e9;
}

void selectionSort(int arr[], int n) {
    int i, j, min_idx, temp;
    
    for (i = 0; i < n - 1; i++) {
        min_idx = i;
        for (j = i + 1; j < n; j++) {
            comparison_count++;
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
    selectionSort(arr, n);
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
