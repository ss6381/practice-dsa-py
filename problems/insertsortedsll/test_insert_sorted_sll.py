from insert_sorted_sll import insert_sorted_sll, print_sll, SinglyLinkedListNode
import pytest


@pytest.mark.parametrize(
    "start, insert, expected",
    [
        ([1, 2, 3, 4, 5, 6, 7], 8, [1, 2, 3, 4, 5, 6, 7, 8]),  # Insert at end
        ([1, 2, 3, 4, 5, 6, 7], 0, [0, 1, 2, 3, 4, 5, 6, 7]),  # Insert at beginning
        ([1, 2, 3, 4, 5, 6, 7], 3, [1, 2, 3, 3, 4, 5, 6, 7]),  # Insert in middle
        ([1, 3, 5, 7], 4, [1, 3, 4, 5, 7]),  # Insert between values
        ([4, 5, 6, 7, 1, 2], 3, [4, 5, 6, 7, 1, 2, 3]),
    ],
)
def test_insert_sorted_sll(start, insert, expected):
    start_node = SinglyLinkedListNode(start[0])
    curr = start_node
    for num in start[1:]:
        curr.next = SinglyLinkedListNode(num)
        curr = curr.next
    curr.next = start_node
    assert (
        print_sll(insert_sorted_sll(start_node, SinglyLinkedListNode(insert)))
        == expected
    )
