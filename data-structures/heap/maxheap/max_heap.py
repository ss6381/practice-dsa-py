class MaxHeap:
    """
    Python has a built-in min heap implementation in the heapq module:
    arr = [], heapq.heapify(arr), heapq.heappush(arr, 1), heapq.heappop(arr), max_val = arr[0]
    We can use the heapq module to implement a max heap by storing negative values.
    This is a manual implementation of a max heap.
    """

    def __init__(self):
        self.array = []
        self.size = 0

    def insert(self, k: int):
        self.array.append(k)
        self.size += 1
        self.max_heapify_up(len(self.array) - 1)

    def extract(self) -> int:
        if len(self.array) <= 0:
            return -1
        self.swap(0, len(self.array) - 1)
        removed = self.array.pop()
        self.size -= 1
        self.max_heapify_down(0)
        return removed

    def get_max(self) -> int:
        if self.size == 0:
            return -1
        return self.array[0]

    def max_heapify_up(self, index: int):
        """O(logn)"""
        if index == 0:
            return
        if self.array[index] > self.array[self.parent(index)]:
            self.swap(index, self.parent(index))
            self.max_heapify_up(self.parent(index))

    def max_heapify_down(self, index: int):
        """O(logn)"""
        if index >= len(self.array):
            return

        left, right = self.left(index), self.right(index)

        # Find the largest child
        largest = index
        if left < len(self.array) and self.array[left] > self.array[largest]:
            largest = left
        if right < len(self.array) and self.array[right] > self.array[largest]:
            largest = right

        # If largest is not the current node, swap and continue
        if largest != index:
            self.swap(largest, index)
            self.max_heapify_down(largest)

    def swap(self, index1: int, index2: int):
        """Swaps two nodes in the heap."""
        self.array[index1], self.array[index2] = self.array[index2], self.array[index1]

    def parent(self, index: int) -> int:
        """The index of the parent node."""
        return (index - 1) // 2  # truncated integer division

    def left(self, index: int) -> int:
        """The index of the left node."""
        return (index * 2) + 1

    def right(self, index: int) -> int:
        """The index of the right node."""
        return (index * 2) + 2
