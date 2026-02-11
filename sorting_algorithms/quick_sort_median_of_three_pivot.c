#include <stdio.h>
#include <stdlib.h>

void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// Function to find the median of three elements
int medianOfThree(int arr[], int low, int high) {
    int mid = low + (high - low) / 2;
    
    // Sort arr[low], arr[mid], arr[high] to find the median
    if (arr[low] > arr[mid]) swap(&arr[low], &arr[mid]);
    if (arr[low] > arr[high]) swap(&arr[low], &arr[high]);
    if (arr[mid] > arr[high]) swap(&arr[mid], &arr[high]);
    
    return mid; // arr[mid] is now the median
}

// Partition function (pivot is the last element)
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

// Quick Sort with median-of-three pivot
void quickSortMedianOfThreePivot(int arr[], int low, int high) {
    if (low < high) {
        // Find the median of arr[low], arr[mid], arr[high]
        int median_index = medianOfThree(arr, low, high);
        
        // Swap the median element with the last element to use the existing partition logic
        swap(&arr[median_index], &arr[high]);
        
        int pi = partition(arr, low, high);
        
        quickSortMedianOfThreePivot(arr, low, pi - 1);
        quickSortMedianOfThreePivot(arr, pi + 1, high);
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
    
    quickSortMedianOfThreePivot(arr, 0, n - 1);
    
    // Optionally print the sorted array, but for benchmarking, we might skip this
    // for (int i = 0; i < n; i++) {
    //     printf("%d ", arr[i]);
    // }
    // printf("\n");
    
    free(arr); // Free dynamically allocated memory
    return 0;
}