# Problem source: https://leetcode.com/problems/binary-tree-vertical-order-traversal/
# Meta - 1st round
# *Input:* [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5)
"""
def vertical_traversal(input: List[int]) -> List[List[int]]:
    result: Dict[int, List[int]] = defaultdict(list)
    min_column, max_column = float("inf"), float("-inf")
    
    queue = deque([(0, 0)])
    while queue:
        column, curr_index = queue.popleft()
        result[column].append(input[curr_index])

        min_column, max_column = min(min_column, column), max(max_column, column)

        left_index, right_index = (curr_index * 2) + 1, (curr_index * 2) + 2
        if left_index < len(input) and input[left_index] is not None:
            queue.append((column - 1, left_index))
        if right_index < len(input) and input[right_index] is not None:
            queue.append((column + 1, right_index))

    return [result[level] for level in range(min_column, max_column + 1)]

"""


#      3
#     /\\
#    /  \\
#    9   8
#   /\  /\\
#  /  \/  \\
#  4  01   7
#     /\\
#    /  \\
#    5   2

# *Output:*

# [
#   [4],
#   [9,5],
#   [3,0,1],
#   [8,2],
#   [7]
# ]
from typing import List, Dict
from collections import defaultdict, deque


def vertical_traversal(input: List[int]) -> List[List[int]]:
    """
    Tradeoffs:
    - Preorder vs. Postorder vs. Inorder vs. Level-order
    - Track column_level using len(results) vs. maintaining min_col_level & max_col_level.
    - Iterative vs. recursive approach.
    Approach:
    - Track min / max column level.
    - Recursive approach using level order
    """
    # results: List[List[int]]= []
    # left_index = (index * 2) + 1
    # right_index = (index * 2) + 2
    pass
