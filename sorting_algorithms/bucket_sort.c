#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    float data;
    struct Node* next;
} Node;

void insertionSortList(Node** head) {
    Node* sorted = NULL;
    Node* current = *head;
    
    while (current != NULL) {
        Node* next = current->next;
        
        if (sorted == NULL || sorted->data >= current->data) {
            current->next = sorted;
            sorted = current;
        } else {
            Node* temp = sorted;
            while (temp->next != NULL && temp->next->data < current->data) {
                temp = temp->next;
            }
            current->next = temp->next;
            temp->next = current;
        }
        current = next;
    }
    *head = sorted;
}

void bucketSort(float arr[], int n) {
    int i, j;
    Node** buckets = (Node**)calloc(n, sizeof(Node*));
    
    for (i = 0; i < n; i++) {
        int bi = (int)(n * arr[i]);
        Node* newNode = (Node*)malloc(sizeof(Node));
        newNode->data = arr[i];
        newNode->next = buckets[bi];
        buckets[bi] = newNode;
    }
    
    for (i = 0; i < n; i++) {
        if (buckets[i] != NULL)
            insertionSortList(&buckets[i]);
    }
    
    int index = 0;
    for (i = 0; i < n; i++) {
        Node* node = buckets[i];
        while (node != NULL) {
            arr[index++] = node->data;
            Node* temp = node;
            node = node->next;
            free(temp);
        }
    }
    
    free(buckets);
}

void printArray(float arr[], int size) {
    int i;
    for (i = 0; i < size; i++)
        printf("%.2f ", arr[i]);
    printf("\n");
}

int main() {
    float arr[] = {0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    printf("Original array: ");
    printArray(arr, n);
    
    bucketSort(arr, n);
    
    printf("Sorted array: ");
    printArray(arr, n);
    
    return 0;
}
