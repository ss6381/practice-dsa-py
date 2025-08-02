class ArrayList:
    def __init__(self, items=None, size=0):
        self.items = items if items is not None else []
        self.size = size

    def append(self, value: int):
        """O(1)"""
        self.items.append(value)
        self.size += 1

    def insert_sorted(self, value: int):
        """Insert value in sorted order. O(n)"""
        insert_index = 0
        for i in range(len(self.items)):
            if self.items[i] > value:
                insert_index = i
                break
            insert_index = i + 1
        self.insert(insert_index, value)

    def insert(self, index: int, value: int):
        """Insert value at index. O(n)"""
        self.items = self.items[:index] + [value] + self.items[index:]
        self.size += 1

    def pop(self, index: int = 0) -> int:
        if self.size == 0:
            raise IndexError("Cannot remove from empty list.")
        if index >= self.size:
            raise ValueError("Input index provided is out of bounds.")
        removed = self.items[index]
        self.items = self.items[:index] + self.items[index + 1 :]
        self.size -= 1
        return removed

    def remove(self, value: int) -> bool:
        for i, item in enumerate(self.items):
            if item == value:
                self.items = self.items[:i] + self.items[i + 1 :]
                self.size -= 1
                return True
        return False

    def sort(self):
        """Tim sort: O(nlogn)"""
        self.items = sorted(self.items)

    def search(self, value: int) -> int:
        """Binary search: O(logn) - only works if the items list is already sorted.
        Arg:
            value: the target value being searched for.

        Return:
            index: the index of the target value in the array, -1 if not found.
        """
        left, right = 0, len(self.items) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.items[mid] == value:
                return mid
            if self.items[mid] > value:
                right = mid - 1
            else:
                left = mid + 1
        return -1
