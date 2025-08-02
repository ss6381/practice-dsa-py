from binary_search import binary_search
import pytest


@pytest.mark.parametrize(
    "arr, target, expected",
    [
        ([1, 5, 7, 12, 24, 26, 46, 75, 103, 125, 235], 235, 10),
        ([1, 5, 7, 12, 24, 26, 46, 75, 103, 125, 235], 7, 2),
        ([1, 5, 7, 12, 24, 26, 46, 75, 103, 125, 235], 9, -1),
    ],
)
def test_binary_search(arr, target, expected):
    actual = binary_search(arr, target)
    assert actual == expected
