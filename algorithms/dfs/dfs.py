from dataclasses import dataclass
from typing import Optional, List


@dataclass
class TreeNode:
    val: int
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


def dfs(node: Optional[TreeNode], result: List[int]):
    if not node:
        return result
    result.append(node.val)
    result = dfs(node.left, result)
    result = dfs(node.right, result)
    return result


def dfs_iterative(node: TreeNode) -> list[int]:
    result = []
    stack = [node]
    while stack:
        node: TreeNode = stack.pop()
        result.append(node.val)
        # Push right child first so left child is processed next (LIFO)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result
