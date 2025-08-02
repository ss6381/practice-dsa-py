from dataclasses import dataclass
from typing import Optional


@dataclass
class BucketNode:
    key: str = None
    next: Optional["BucketNode"] = None


class Bucket:
    def __init__(self):
        self.head: BucketNode = BucketNode()
        self.size = 0

    def print(self):
        result = []
        curr = self.head.next
        while curr is not None:
            if curr.key is not None:
                result.append(curr.key)
            else:
                result.append("None")
            curr = curr.next
        return " ".join(result)

    def insert(self, key: str):
        # if bucket already contains key, do not insert
        curr = self.head.next
        while curr is not None:
            if curr.key is not None and curr.key == key:
                return
            curr = curr.next
        next = self.head.next
        node = BucketNode(key=key, next=next)
        self.head.next = node
        self.size += 1

    def search(self, key: str) -> BucketNode:
        curr = self.head.next
        while curr is not None:
            if curr.key is not None and curr.key == key:
                return curr
            curr = curr.next
        return None

    def delete(self, key: str) -> bool:
        curr = self.head
        while curr.next is not None:
            if curr.next.key is not None and curr.next.key == key:
                curr.next = curr.next.next
                self.size -= 1
                return True
            curr = curr.next
        return False


class HashTable:
    """
    Python has an in-built hash table implementation called dict.
    This is a manual implementation of a hash table.
    """

    def __init__(self, array_size=5):
        self.array = [Bucket() for _ in range(array_size)]
        self.array_size = array_size
        self.size = 0

    def __repr__(self):
        result = []
        for i, item in enumerate(self.array):
            result.append(f"index {i}: " + item.print())
        return "\n".join(result)

    def insert(self, key: str):
        bucket: Bucket = self.array[self.hash(key)]
        bucket.insert(key=key)
        self.size += 1

    def search(self, key: str) -> int:
        index = self.hash(key)
        if self.array[index].search(key) is not None:
            return index
        return -1

    def delete(self, key: str) -> bool:
        if self.array[self.hash(key)].delete(key):
            self.size -= 1
            return True
        return False

    def hash(self, key: str) -> int:
        sum = 0
        for char in key:
            sum += ord(char)
        return sum % self.array_size


t = HashTable()
t.insert("hello")
print(t)
