class Stack:
    
	def __init__(self):
		self.items = []
		self.size = 0

	def push(self, val):
		self.items.append(val)
		self.size += 1

	def pop(self):
		if self.items:
			item = self.items.pop()
			self.size -= 1
			return item
		raise Exception('Error: Cannot pop from an empty stack.')
	
	def size(self):
		return self.size
	
	def empty(self):
		return self.size == 0
	
if __name__ == '__main__':
	stack = Stack()

	stack.push(1)
	stack.push(3)
	print(stack.pop())
	stack.push(4)
	print(stack.pop())
	print(stack.pop())
	try:
		print(stack.pop())
	except Exception:
		print('exception.')
