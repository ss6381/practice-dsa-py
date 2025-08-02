from kth_largest_number import kth_largest
import pytest
from typing import List


@pytest.mark.parametrize(
    "array, k, expected",
    [
        ([1, 6, 2, 5, 3, 7, 4], 3, 5),
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
    ],
)
def test_kth_largest(array: List[int], k: int, expected: int):
    assert kth_largest(array, k) == expected
