import sys
sys.path.append('../iterative_sorting')
from iterative_sorting import *


def linear_search(arr, target):
    # Your code here

    # Loop through the length of index
    for i in range(len(arr)):
        # Check if the indexed element equals the target
        if arr[i] == target:
            # Return the index if found
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    low = 0
    high = len(arr) - 1

    while low <= high:
        middle = (low + high) // 2
        guess = arr[middle]

        if guess == target:
            return middle
        if guess > target:
            high = middle - 1
        else:
            low = middle + 1

    return -1  # not found
