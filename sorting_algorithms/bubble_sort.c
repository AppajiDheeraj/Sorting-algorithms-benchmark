#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdint.h>

long long comparison_count = 0;
struct timespec start_time, end_time;

double get_elapsed_time(struct timespec start, struct timespec end) {
    return (end.tv_sec - start.tv_sec) + (end.tv_nsec - start.tv_nsec) / 1e9;
}

void bubbleSort(int arr[], int n) {
    int i, j, temp;
    int swapped;
    
    for (i = 0; i < n - 1; i++) {
        swapped = 0;
        for (j = 0; j < n - i - 1; j++) {
            comparison_count++;
            if (arr[j] > arr[j + 1]) {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                swapped = 1;
            }
        }
        if (swapped == 0)
            break;
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
    bubbleSort(arr, n);
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
