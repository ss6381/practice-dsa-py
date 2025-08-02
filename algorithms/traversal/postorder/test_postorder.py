from postorder import postorder, TreeNode
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
            [4, 5, 2, 6, 7, 3, 1],
        )
    ],
)
def test_postorder(root, expected):
    assert postorder(root) == expected
