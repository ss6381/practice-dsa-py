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
        raise IndexError("Cannot pop from an empty stack.")

    def size(self):
        return self.size

    def empty(self):
        return self.size == 0
