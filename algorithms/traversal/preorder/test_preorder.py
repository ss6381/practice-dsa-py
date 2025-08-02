from preorder import preorder, TreeNode
import pytest

#        1
#      /   \
#     2     3
#    / \   / \
#   4   5 6   7


@pytest.mark.parametrize(
    "root, expected",
    [
        (
            TreeNode(
                val=1,
                left=TreeNode(val=2, left=TreeNode(val=4), right=TreeNode(val=5)),
                right=TreeNode(val=3, left=TreeNode(val=6), right=TreeNode(val=7)),
            ),
            [1, 2, 4, 5, 3, 6, 7],
        )
    ],
)
def test_preorder(root, expected):
    assert preorder(root) == expected
