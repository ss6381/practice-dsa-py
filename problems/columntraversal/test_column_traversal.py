from column_traversal import vertical_traversal
import pytest

"""
TreeNode(
    val=3,
    left=TreeNode(
        val=9,
        left=TreeNode(val=4),
        right=TreeNode(val=0, right=TreeNode(val=2)),
    ),
    right=TreeNode(
        val=8,
        left=TreeNode(val=1, left=TreeNode(val=5)),
        right=TreeNode(val=7),
    ),
),
"""


@pytest.mark.parametrize(
    "input, expected",
    [
        (
            [3, 9, 8, 4, 0, 1, 7, None, None, None, 2, 5],
            [[4], [9, 5], [3, 0, 1], [8, 2], [7]],
        ),
    ],
)
def test_vertical_traversal(input, expected):
    assert vertical_traversal(input) == expected
