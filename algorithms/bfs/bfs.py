import collections

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:

	def bfs_recursive(self, queue):
		if not queue:
			return
		curr = queue.popleft()
		print(curr.val)
		if curr.left:
			queue.append(curr.left)
		if curr.right:
			queue.append(curr.right)
		self.bfs_recursive(queue)

	def bfs(self, node):
		if not node:
			return
		q = collections.deque()
		q.append(node)
		self.bfs_recursive(q)
		
	def bfs_iterative(self, node):
		q = collections.deque()
		q.append(node)
		while q:
			curr = q.popleft()
			print(curr.val)
			if curr.left:
				q.append(curr.left)
			if curr.right:
				q.append(curr.right)
		return -1

if __name__ == '__main__':
	node = TreeNode(1)
	node.left = TreeNode(2)
	node.left.left = TreeNode(4)
	node.left.right = TreeNode(5)
	node.right = TreeNode(3)
	node.right.left = TreeNode(6)
	node.right.right = TreeNode(7)
	s = Solution()
	s.bfs(node)
	s.bfs_iterative(node)