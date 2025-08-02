from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quick_sort import quick_sort
from selection_sort import selection_sort
import pytest


@pytest.mark.parametrize(
    "input, expected", [([4, 7, 2, 5, 8, 2, 1, 9, 4], [1, 2, 2, 4, 4, 5, 7, 8, 9])]
)
def test_insertion_sort(input, expected):
    assert insertion_sort(input) == expected


@pytest.mark.parametrize(
    "input, expected", [([4, 7, 2, 5, 8, 2, 1, 9, 4], [1, 2, 2, 4, 4, 5, 7, 8, 9])]
)
def test_selection_sort(input, expected):
    assert selection_sort(input) == expected


@pytest.mark.parametrize(
    "input, expected", [([4, 7, 2, 5, 8, 2, 1, 9, 4], [1, 2, 2, 4, 4, 5, 7, 8, 9])]
)
def test_merge_sort(input, expected):
    assert merge_sort(input) == expected


@pytest.mark.parametrize(
    "input, expected", [([4, 7, 2, 5, 8, 2, 1, 9, 4], [1, 2, 2, 4, 4, 5, 7, 8, 9])]
)
def test_quick_sort(input, expected):
    assert quick_sort(input) == expected
