from dataclasses import dataclass
from typing import Optional, List


@dataclass
class Node:
    data: int
    next: Optional["Node"] = None
    prev: Optional["Node"] = None


class DoublyLinkedList:
    """
    Doubly-linked list (DLL) implementation.
    Python does not have a built-in doubly-linked list,
    so we implement it ourselves.
    """

    def __init__(self):
        self.head = Node(data=-1)
        self.tail = Node(data=-1, prev=self.head)
        self.head.next = self.tail
        self.size = 0

    def insert(self, data: int, index: int = 0):
        """
        We use the insert function to add items to doubly linked list.
        We compare the index against the size so in practice, we only need
        to travel for size / 2 nodes in DLL.

        Args:
            data: The data value being inserted into the linked list.
            index: The specific index where the data should be inserted, defaults to index=0.
        """
        # transform index=-1 into the last index in the list.
        if index == -1:
            self.append(data)
            return
        # base case: index is valid.
        if index not in range(0, self.size + 1):
            raise ValueError("Index value provided was out-of-bounds.")
        # base case: self.size == 0.
        if self.size == 0 or index == 0:
            self.__insert_after(self.head, data)
        # check if index is greater or less than or equal to self.size // 2.
        elif index <= self.size // 2:
            # if less than or equal to: traverse forward starting from head.
            curr = self.head.next
            i = 0
            while curr != self.tail:
                if i == index - 1:
                    self.__insert_after(curr, data)
                    return
                curr = curr.next
                i += 1
        else:
            # if greater than: traverse backwards starting from tail.
            curr = self.tail.prev
            i = self.size
            while curr != self.head:
                if i == index:
                    self.__insert_after(curr, data)
                    return
                curr = curr.prev
                i -= 1

    def append(self, data: int):
        self.__insert_after(self.tail.prev, data)

    def __insert_after(self, node: Node, data: int):
        """
        Adds a new node with data=data after the node field
        that is passed in.

        Args:
            node: the node that the new node is inserted after.
            data: data for the new node that will be inserted.
        """
        node_to_insert = Node(data=data)
        # manipulating the pointers of the curr and next nodes:
        # connecting the nodes forwards...
        next = node.next
        node.next = node_to_insert
        node_to_insert.next = next
        # and backwards...
        next.prev = node_to_insert
        node_to_insert.prev = node

        # increment the size of the linked list by 1.
        self.size += 1

    def pop(self, index: int = -1) -> Node:
        if self.size <= 0:
            raise ValueError("Cannot remove from an empty linked list.")
        if index == -1:
            return self.__remove(self.tail.prev)
        if index not in range(0, self.size):
            raise ValueError("Index value provided was out-of-bounds.")

        curr = self.head.next
        i = 0
        while curr != self.tail:
            if i == index:
                return self.__remove(curr)
            curr = curr.next
            i += 1
        return None

    def remove(self, data: int) -> Optional[Node]:
        """
        Remove the item at the end of the linked list.
        """
        curr = self.head.next
        while curr != self.tail:
            if curr.data == data:
                return self.__remove(curr)
            curr = curr.next
        return None

    def __remove(self, node_to_remove: Node) -> Node:
        prev = node_to_remove.prev
        next = node_to_remove.next
        prev.next = next
        next.prev = prev
        self.size -= 1
        return node_to_remove

    def to_list(self) -> List[int]:
        result = []
        curr = self.head.next
        while curr != self.tail:
            result.append(curr.data)
            curr = curr.next
        print(result)
        return result
