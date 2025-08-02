from typing import List


def selection_sort(array: List[int]) -> List[int]:
    """
    An in-place sorting technique.
    It divides the data set into two sublists: sorted and unsorted.
    Then it selects the minimum element from unsorted sublist and
    places it into the sorted list. This iterates unless all the
    elements from unsorted sublist are consumed.

    Selection sort searches the minimum from the unsorted sub-list
    and replaces it with the current element in hand.
    """
    if len(array) <= 1:
        return array

    for index in range(len(array)):
        j = index + 1
        # Finds the index of the minimum value in the array.
        min_index = index
        while j < len(array):
            if array[j] < array[min_index]:
                min_index = j
            j += 1
        # Swaps the current index with the index of the minimum value.
        array[index], array[min_index] = array[min_index], array[index]
    return array
