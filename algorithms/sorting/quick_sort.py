from typing import List


def quick_sort(array: List[int]) -> List[int]:
    """
    Divide and conquer.
    It divides list in to smaller partitions using a pivot.
    The values which are smaller than the pivot are arranged
    on the left parition and the greater values are arranged
    in the right partition.
    Each partition is recursively sorted using quick sort.
    """
    if len(array) <= 1:
        return array

    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
