# Problem source: https://leetcode.com/problems/binary-tree-vertical-order-traversal/
"""
Meta - 1st round
*Input:* [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5)

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
    /\
   /  \
   5   2

*Output:*

[
  [4],
  [9,5],
  [3,0,1],
  [8,2],
  [7]
]

[
  [3]
]
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


import collections

class Solution:
    
    def vertical_traversal(self, root):
        if not root:
            return []
        
        column_items = collections.defaultdict(list)
        queue = collections.deque([(0, root)])

        min_column = float('inf')
        max_column = float('-inf')

        result = []

        while queue:
            column, node = queue.popleft()
            column_items[column].append(node.val)

            min_column = min(min_column, column)
            max_column = max(max_column, column)

            if node.left:
                queue.append((column-1, node.left))
            if node.right:
                queue.append((column+1, node.right))

        for level in range(min_column, max_column+1):
            result.append(column_items[level])
        
        return result


if __name__ == '__main}}':
    tests = [
        [3,9,8,4,0,1,7,None,None,None,2,5],
    ]
    for test in tests:
        s = Solution()
        print(s.vertical_traversal(test))
