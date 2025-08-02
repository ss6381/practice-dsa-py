from collections import deque
from dataclasses import dataclass
from typing import Optional, List


@dataclass
class TreeNode:
    val: int
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


def bfs(root: TreeNode) -> List[int]:
    """
    Breadth-first search can be implemented iteratively using a queue.
    We can do BFS over a binary tree, graph, adjacency list, and matrix.
    """
    result = []
    q = deque([root])
    while q:
        curr: TreeNode = q.popleft()
        result.append(curr.val)
        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)
    return result


def bfs_recursive(root: Optional[TreeNode]) -> List[int]:
    """
    Breadth-first search implemented recursively.
    Note: True BFS is inherently iterative, but we can simulate it recursively
    by processing nodes level by level.
    """
    if not root:
        return []

    result = []
    level = [root]

    def bfs_level(nodes: List[TreeNode]) -> None:
        if not nodes:
            return

        next_level = []
        for node in nodes:
            result.append(node.val)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)

        bfs_level(next_level)

    bfs_level(level)
    return result
