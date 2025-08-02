from typing import List


def insertion_sort(array: List[int]) -> List[int]:
    """
    Divides the list into two sublists, sorted and unsorted.
    It takes one element at a time and finds its appropriate
    location in the sorted sublist and inserts it there.
    The output after insertion is a sorted sublist.

    Insertion sort works on the current element and places it
    in the sorted array at the appropriate location.
    """
    if len(array) <= 1:
        return array

    for index in range(1, len(array)):
        current_value = array[index]
        sorted_index = index - 1
        # Goes backwards through the sorted part of the array
        while sorted_index >= 0 and current_value < array[sorted_index]:
            # Moves all the elements up by one.
            array[sorted_index + 1] = array[sorted_index]
            sorted_index -= 1
        # Inserts the value in the exact right position.
        array[sorted_index + 1] = current_value
    return array
