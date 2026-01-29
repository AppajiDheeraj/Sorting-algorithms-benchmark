#include <stdio.h>
#include <stdlib.h>

int getMax(int arr[], int n) {
    int max = arr[0];
    int i;
    for (i = 1; i < n; i++)
        if (arr[i] > max)
            max = arr[i];
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
    int arr[] = {170, 45, 75, 90, 802, 24, 2, 66};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    printf("Original array: ");
    printArray(arr, n);
    
    radixSort(arr, n);
    
    printf("Sorted array: ");
    printArray(arr, n);
    
    return 0;
}
