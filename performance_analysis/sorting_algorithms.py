"""
Sorting Algorithm Implementations
==================================
This module contains pure Python implementations of various sorting algorithms
for performance analysis and time complexity evaluation.
"""

import random
from typing import List


def bubble_sort(arr: List[int]) -> List[int]:
    """
    Bubble Sort - O(n²) time complexity
    Repeatedly swaps adjacent elements if they are in wrong order.
    """
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def selection_sort(arr: List[int]) -> List[int]:
    """
    Selection Sort - O(n²) time complexity
    Repeatedly selects the minimum element from unsorted portion.
    """
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def insertion_sort(arr: List[int]) -> List[int]:
    """
    Insertion Sort - O(n²) average, O(n) best case
    Builds sorted array one element at a time.
    """
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(arr: List[int]) -> List[int]:
    """
    Merge Sort - O(n log n) time complexity
    Divide and conquer algorithm using recursive merging.
    """
    if len(arr) <= 1:
        return arr.copy()
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return _merge(left, right)


def _merge(left: List[int], right: List[int]) -> List[int]:
    """Helper function to merge two sorted arrays."""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(arr: List[int]) -> List[int]:
    """
    Quick Sort - O(n log n) average, O(n²) worst case
    Divide and conquer using pivot partitioning.
    """
    if len(arr) <= 1:
        return arr.copy()
    
    arr = arr.copy()
    _quick_sort_helper(arr, 0, len(arr) - 1)
    return arr


def _quick_sort_helper(arr: List[int], low: int, high: int) -> None:
    """Helper function for quick sort."""
    if low < high:
        pi = _partition(arr, low, high)
        _quick_sort_helper(arr, low, pi - 1)
        _quick_sort_helper(arr, pi + 1, high)


def _partition(arr: List[int], low: int, high: int) -> int:
    """Partition function for quick sort."""
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def heap_sort(arr: List[int]) -> List[int]:
    """
    Heap Sort - O(n log n) time complexity
    Uses binary heap data structure for sorting.
    """
    arr = arr.copy()
    n = len(arr)
    
    for i in range(n // 2 - 1, -1, -1):
        _heapify(arr, n, i)
    
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        _heapify(arr, i, 0)
    
    return arr


def _heapify(arr: List[int], n: int, i: int) -> None:
    """Helper function to maintain heap property."""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        _heapify(arr, n, largest)


def shell_sort(arr: List[int]) -> List[int]:
    """
    Shell Sort - O(n log n) to O(n²) depending on gap sequence
    Generalized insertion sort with gap sequence.
    """
    arr = arr.copy()
    n = len(arr)
    gap = n // 2
    
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    
    return arr


def counting_sort(arr: List[int]) -> List[int]:
    """
    Counting Sort - O(n + k) time complexity
    Non-comparison based sorting for integers in a known range.
    """
    if not arr:
        return []
    
    arr = arr.copy()
    max_val = max(arr)
    min_val = min(arr)
    range_size = max_val - min_val + 1
    
    count = [0] * range_size
    output = [0] * len(arr)
    
    for num in arr:
        count[num - min_val] += 1
    
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    for num in reversed(arr):
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1
    
    return output


def radix_sort(arr: List[int]) -> List[int]:
    """
    Radix Sort - O(d * (n + k)) time complexity
    Sorts integers by processing individual digits.
    """
    if not arr:
        return []
    
    arr = arr.copy()
    max_val = max(arr)
    exp = 1
    
    while max_val // exp > 0:
        _counting_sort_by_digit(arr, exp)
        exp *= 10
    
    return arr


def _counting_sort_by_digit(arr: List[int], exp: int) -> None:
    """Helper function for radix sort."""
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    for num in arr:
        index = (num // exp) % 10
        count[index] += 1
    
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
    
    for i in range(n):
        arr[i] = output[i]


def tim_sort(arr: List[int]) -> List[int]:
    """
    Tim Sort - O(n log n) time complexity
    Hybrid sorting algorithm (used by Python's built-in sort).
    """
    return sorted(arr)


ALGORITHMS = {
    'Bubble Sort': bubble_sort,
    'Selection Sort': selection_sort,
    'Insertion Sort': insertion_sort,
    'Merge Sort': merge_sort,
    'Quick Sort': quick_sort,
    'Heap Sort': heap_sort,
    'Shell Sort': shell_sort,
    'Counting Sort': counting_sort,
    'Radix Sort': radix_sort,
    'Tim Sort': tim_sort,
}
