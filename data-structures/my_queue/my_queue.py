from collections import deque


class MyQueue:
    """
    Python has a built-in queue implementation in the collections module.
    However, we can implement our own queue using a deque.
    """

    def __init__(self):
        self.items = deque()
        self.size = 0

    def enqueue(self, val):
        self.items.append(val)
        self.size += 1

    def dequeue(self):
        if self.items:
            item = self.items.popleft()
            self.size -= 1
            return item
        raise IndexError("Cannot dequeue from an empty queue.")

    def empty(self):
        return self.size == 0
