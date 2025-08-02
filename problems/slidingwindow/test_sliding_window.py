from sliding_window import sliding_window
import pytest
from typing import List, Tuple


# find all contiguous permutations of b in s
@pytest.mark.parametrize(
    "cipher, input, expected",
    [
        ("abc", "abcbdacbabce", [(0, 2), (5, 7), (6, 8), (8, 10)]),
        ("ccaaa", "acccaa", []),
        ("ccaaa", "acccaaa", [(2, 6)]),
        ("ccaaa", "ac", []),
    ],
)
def test_sliding_window(cipher: str, input: str, expected: List[Tuple[int, int]]):
    assert sliding_window(cipher, input) == expected
