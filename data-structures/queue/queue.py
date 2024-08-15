import collections

class Queue:
	def __init__(self):
		self.items = collections.deque()
		self.size = 0
	
	def enqueue(self, val):
		self.items.append(val)
		self.size += 1
	
	def dequeue(self):
		if self.items:
			item = self.items.popleft()
			self.size -= 1
			return item
		raise Exception('Error: Cannot dequeue from an empty queue.')
	
	def empty(self):
		return self.size == 0
    
if __name__ == '__main__':
	q = Queue()
    
	q.enqueue(1)
	q.enqueue(2)
	print(q.dequeue())
	q.enqueue(3)
	print(q.dequeue())
	print(q.dequeue())
	try:
		print(q.dequeue())
	except Exception:
		print('exception.')