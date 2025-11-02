"""Implementing Randomized Quicksort involves selecting a random pivot from the subarray and placing it at the end for easier partitioning.
Rearranging elements around the pivot ensures that smaller elements move to the left while larger elements shift to the right.
Recursively sorting the left and right subarrays continues until the entire array is ordered. Handling edge cases such as empty arrays,
already sorted arrays, and repeated elements ensures the algorithm’s robustness.
"""

import random


# Partitioning the array around the pivot
def partition(arr, low, high):
    # Selecting a random pivot and swapping it with the last element
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

    pivot = arr[high]
    i = low - 1

    # Moving elements smaller than pivot to the left
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Placing the pivot at its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


# Sorting the array with randomized quicksort
def randomized_quicksort(arr, low, high):
    if low < high:
        # Partitioning the array and getting the pivot index
        pi = partition(arr, low, high)

        # Sorting the left subarray
        randomized_quicksort(arr, low, pi - 1)

        # Sorting the right subarray
        randomized_quicksort(arr, pi + 1, high)


# Wrapping the function to call quicksort
def quicksort(arr):
    randomized_quicksort(arr, 0, len(arr) - 1)
    return arr


# Running test cases to check the behavior with different inputs
test_cases = [
    [3, 2, 1, 5, 4],
    [1, 2, 3, 4, 5],
    [5, 5, 5, 5],
    [],
    [3, 1, 2, 3, 4, 1]
]

# Testing each case
for test_case in test_cases:
    print(f"Original: {test_case}")
    sorted_arr = quicksort(test_case)
    print(f"Sorted: {sorted_arr}")
    print('-' * 50)
