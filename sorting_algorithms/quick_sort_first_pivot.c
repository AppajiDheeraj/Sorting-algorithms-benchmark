#include <stdio.h>
#include <stdlib.h>

void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// Partition function for Quick Sort (pivot is the last element)
int partition(int arr[], int low, int high) {
    int pivot = arr[high]; // Pivot is now the element that was moved to high
    int i = (low - 1);
    int j;
    
    for (j = low; j <= high - 1; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return (i + 1);
}

// Quick Sort with first element as pivot
void quickSortFirstPivot(int arr[], int low, int high) {
    if (low < high) {
        // Move the first element to the end to use the existing partition logic
        swap(&arr[low], &arr[high]);
        int pi = partition(arr, low, high);
        
        quickSortFirstPivot(arr, low, pi - 1);
        quickSortFirstPivot(arr, pi + 1, high);
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
    
    quickSortFirstPivot(arr, 0, n - 1);
    
    // Optionally print the sorted array, but for benchmarking, we might skip this
    // for (int i = 0; i < n; i++) {
    //     printf("%d ", arr[i]);
    // }
    // printf("\n");
    
    free(arr); // Free dynamically allocated memory
    return 0;
}
