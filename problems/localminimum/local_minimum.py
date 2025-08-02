# Meta phone screen 2025, part 1.
# Return any local minimum in array:
# [0, 3, 5, 4, 6, 7, 2] -> 0 or 4 or 2
# [10, 9, 8, 7, 6, 5, 4, 3] -> 3


def find_local_minimum(arr: list[int]) -> int:
    left, right = 1, len(arr) - 2
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < arr[mid - 1] and arr[mid] < arr[mid + 1]:
            return mid
        if arr[mid - 1] < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1
