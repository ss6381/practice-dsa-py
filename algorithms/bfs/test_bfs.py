from bfs import bfs, bfs_recursive, TreeNode
import pytest


@pytest.mark.parametrize(
    "root, expected",
    [
        (TreeNode(val=42, left=TreeNode(val=12), right=TreeNode(val=46)), [42, 12, 46]),
        (
            TreeNode(
                val=1,
                left=TreeNode(val=2, left=TreeNode(val=4), right=TreeNode(val=5)),
                right=TreeNode(val=3, left=TreeNode(val=6), right=TreeNode(val=7)),
            ),
            [1, 2, 3, 4, 5, 6, 7],
        ),
    ],
)
def test_bfs(root, expected):
    assert bfs(root) == expected
    assert bfs_recursive(root) == expected
