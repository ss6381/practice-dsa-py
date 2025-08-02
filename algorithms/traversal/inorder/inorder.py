from dataclasses import dataclass
from typing import Optional, List


@dataclass
class TreeNode:
    val: int
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


def inorder(node: Optional[TreeNode], result: List[int] = []):
    if not node:
        return result

    inorder(node.left)
    result.append(node.val)
    inorder(node.right)

    return result


def inorder_iterative(node):
    pass
