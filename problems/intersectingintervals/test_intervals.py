from intervals import merge_k_interval_lists, min_meeting_rooms, merge
import pytest


@pytest.mark.parametrize(
    "input, expected",
    [
        ([(0, 30), (5, 10), (15, 20)], 2),
        ([(7, 10), (2, 4)], 1),
        ([(0, 5), (5, 30), (4, 8)], 2),
    ],
)
def test_min_meeting_rooms(input, expected):
    assert min_meeting_rooms(input) == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        ([[2, 4], [8, 10], [6, 7], [3, 5]], [[2, 5], [6, 7], [8, 10]]),
        ([[2, 4], [8, 10], [6, 8], [3, 5]], [[2, 5], [6, 10]]),
        ([], []),
    ],
)
def test_merge(input, expected):
    assert merge(input) == expected


@pytest.mark.parametrize(
    "input, expected", [([[(2, 4), (6, 8)], [(8, 10), (3, 5)]], [(2, 5), (6, 10)])]
)
def test_merge_k_intervals(input, expected):
    assert merge_k_interval_lists(input) == expected
