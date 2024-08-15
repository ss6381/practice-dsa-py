class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
    
	def dfs(self, node, result):
		if not node:
			return result
		result.append(node.val)
		result = self.dfs(node.left, result)
		result = self.dfs(node.right, result)
		return result

	def dfs_iterative(self, node):
		stack = []
		stack.append(node)
		while stack:
			node = stack.pop()
			print(node.val)
			if node.right:
				stack.append(node.right)
			if node.left:
				stack.append(node.left)
	
if __name__ == '__main__':
	node = TreeNode(1)
	node.left = TreeNode(2)
	node.left.left = TreeNode(4)
	node.left.right = TreeNode(5)
	node.right = TreeNode(3)
	node.right.left = TreeNode(6)
	node.right.right = TreeNode(7)
	s = Solution()
	print(s.dfs(node, []))
	s.dfs_iterative(node)
