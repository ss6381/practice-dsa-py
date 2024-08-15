class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def preorder_recursive(self, node):
		if node:
			print(node.val)
			self.preorder_recursive(node.left)
			self.preorder_recursive(node.right)

if __name__ == '__main__':
	s = Solution()

    #        1
    #      /   \
    #     2     3
    #    / \   / \
    #   4   5 6   7

	node = TreeNode(1)
	node.left = TreeNode(2)
	node.left.left = TreeNode(4)
	node.left.right = TreeNode(5)
	node.right = TreeNode(3)
	node.right.left = TreeNode(6)
	node.right.right = TreeNode(7)

	print(s.preorder_recursive(node))