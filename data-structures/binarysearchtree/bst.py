from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    """
    Dataclass automatically generates the dunder functions for
    __init__, __repr__, __eq__, and __hash__.
    """

    data: int
    left: Optional["Node"] = None
    right: Optional["Node"] = None

    def __eq__(self, node: Optional["Node"]) -> bool:
        """
        Override the dataclass automatic method generation to
        compare for equality only using the data field, rather
        than comparing for all fields. Easier for testing...
        """
        if node == None:
            return False
        return self.data == node.data

    def insert(self, k: int):
        if self.data < k:
            if self.right == None:
                self.right = Node(k)
                return
            self.right.insert(k)
        elif self.data > k:
            if self.left == None:
                self.left = Node(k)
            self.left.insert(k)

    def search(self, k: int) -> Optional["Node"]:
        if self.data == k:
            return self
        if self.data < k:
            if self.right != None:
                return self.right.search(k)
        else:
            if self.left != None:
                return self.left.search(k)
        return None

    def remove(self, k: int) -> bool:
        """
        Remove a node by restructuring the binary search tree.
        """
        pass


class BinarySearchTree:
    """
    Iterative approach to creating, inserting, searching,
    and removing in a binary search tree.
    """

    def __init__(self, root: Node):
        self.root = root

    def insert(self, k: int):
        self.root.insert(k)

    def search(self, k: int) -> Node:
        return self.root.search(k)

    def remove(self, k: int) -> bool:
        return self.root.remove(k)
