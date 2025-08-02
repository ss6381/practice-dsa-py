class Stack:
    def __init__(self):
        self.items = []
        self.max = []
        self.size = 0

    def push(self, val: int):
        if not self.items or val >= self.max[-1]:
            self.max.append(val)
        else:
            self.max.append(self.max[-1])
        self.items.append(val)
        self.size += 1

    def pop(self) -> int:
        if not self.items:
            raise IndexError("Cannot pop when stack is empty.")
        item = self.items.pop()
        self.max.pop()
        self.size -= 1
        return item

    def get_max(self) -> int:
        if not self.max:
            raise IndexError("Cannot get max when stack is empty.")
        return self.max[-1]
