class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:

	def inorder_iterative(self, node):
		pass

	def inorder_recursive(self, node):
		if node:
			self.inorder_recursive(node.left)
			print(node.val)
			self.inorder_recursive(node.right)

if __name__ == "__main__":
	s = Solution()
	node = TreeNode(1)
	node.left = TreeNode(2)
	node.left.left = TreeNode(4)
	node.left.right = TreeNode(5)
	node.right = TreeNode(3)
	node.right.left = TreeNode(6)
	node.right.right = TreeNode(7)

	print(s.inorder_recursive(node))