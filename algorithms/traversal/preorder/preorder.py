from dataclasses import dataclass
from typing import Optional, List


@dataclass
class TreeNode:
    val: int
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


def preorder(node: Optional[TreeNode], result: List[int] = []) -> List[int]:
    if not node:
        return result
    result.append(node.val)
    preorder(node.left, result)
    preorder(node.right, result)
    return result
