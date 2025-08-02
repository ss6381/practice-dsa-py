from dataclasses import dataclass
from typing import Optional, List


@dataclass
class TreeNode:
    val: int
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


def postorder(node: Optional[TreeNode], result: List[int] = []) -> List[int]:
    if not node:
        return result

    postorder(node.left)
    postorder(node.right)
    result.append(node.val)

    return result
