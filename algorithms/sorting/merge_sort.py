# average and worst case: 0(nlogn).
# memory: Depends, but space complexity of merge sort is 0(n) due to the auxiliary space used to merge parts of the array.

from typing import List


def merge_sort(array: List[int]) -> List[int]:
    """
    Divide and conquer approach.
    It keeps dividing the list intosmaller sub-lists
    until all sub-lists are only 1 element big.
    Then it merges them in a sorted way until all sub-lists are consumed.

    It has a run-time complexity of O(n log n) and
    it needs O(n) auxiliary space.
    """
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left_half, right_half = array[:mid], array[mid:]
    left, right = merge_sort(left_half), merge_sort(right_half)
    return merge(left, right)


def merge(left: List[int], right: List[int]) -> List[int]:
    """
    This is the standard algorithm to merge two sorted lists,
    used in the merge sort algorithm to rejoin two independently sorted lists.
    """
    result: List[int] = []
    l, r = 0, 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result.extend(left[l:])  # pick up any left over values in left
    result.extend(right[r:])  # pick up any left over values in right
    return result
