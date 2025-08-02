# Meta phone screen 2025, pt 2.
# 2 -> 3 -> 5 -> 6 -> 6 -> 8, insert: 6, start: 6

from dataclasses import dataclass
from typing import Optional


@dataclass
class SinglyLinkedListNode:
    data: int
    next: Optional["SinglyLinkedListNode"] = None


def insert_sorted_sll(
    start: SinglyLinkedListNode, insert: SinglyLinkedListNode
) -> bool:
    curr = start
    while curr.data > insert.data:
        curr = curr.next

    while curr.next is not start:
        if curr.data >= insert.data:
            curr_next = curr.next
            curr.next = insert
            insert.next = curr_next
            return start
        curr = curr.next
    return start


def print_sll(start: SinglyLinkedListNode):
    result = [start.data]
    curr = start
    while curr.next is not start:
        result.append(curr.next.data)
        curr = curr.next
    return result
