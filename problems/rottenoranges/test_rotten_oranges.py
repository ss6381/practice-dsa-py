from rotten_oranges import rotten_oranges, OrangeState
import pytest


@pytest.mark.parametrize(
    "grid, expected",
    [
        ([[2, 1, 1], [1, 1, 0], [0, 1, 1]], 4),
        ([[2, 1, 1], [1, 1, 0], [0, 0, 1]], -1),
    ],
)
def test_rotten_oranges(grid, expected):
    assert rotten_oranges(grid) == expected
