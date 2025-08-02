from dataclasses import dataclass
from typing import Optional, List


@dataclass
class TreeNode:
    val: int
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    return __level_order(root, 0, [])


def __level_order(
    node: Optional[TreeNode], level: int, result: List[List[int]]
) -> List[List[int]]:
    if node is None:
        return result
    if len(result) <= level:
        result.append([])

    result[level].append(node.val)
    result = __level_order(node.left, level + 1, result)
    result = __level_order(node.right, level + 1, result)
    return result
