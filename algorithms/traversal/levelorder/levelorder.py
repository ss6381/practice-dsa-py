class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:

	def levelorder(self, node):
		h = self.height(node)
		for level in range(h):
			self.currlevel(node, level+1)
			print()

	def height(self, node):
		if not node:
			return 0
		left = self.height(node.left)
		right = self.height(node.right)
		return max(left, right) + 1
	
	def currlevel(self, node, level):
		if level == 1:
			print(node.val)
		elif level > 1:
			if node.left:
				self.currlevel(node.left, level - 1)
			if node.right:
				self.currlevel(node.right, level - 1)


if __name__ == '__main__':
	s = Solution()
	node = TreeNode(1)
	node.left = TreeNode(2)
	node.left.left = TreeNode(4)
	node.left.right = TreeNode(5)
	node.right = TreeNode(3)
	node.right.left = TreeNode(6)
	node.right.right = TreeNode(7)

	print(s.levelorder(node))