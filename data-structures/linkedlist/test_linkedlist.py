from linkedlist import DoublyLinkedList
import pytest


@pytest.fixture
def linkedlist():
    return DoublyLinkedList()


@pytest.mark.parametrize(
    "insert, expected",
    [
        ([1], [1]),
        ([2, 3], [2, 3]),
    ],
)
def test_linkedlist_append_success(linkedlist: DoublyLinkedList, insert, expected):
    # use arrange-act-assert to write unit tests using best practices.
    for data in insert:
        linkedlist.append(data=data)
    assert linkedlist.to_list() == expected


@pytest.mark.parametrize(
    "insert, expected",
    [
        ([(1, 0)], [1]),
        ([(2, 0), (3, 0)], [3, 2]),
        ([(2, 0), (3, 1)], [2, 3]),
        ([(2, 0), (4, 0), (3, -1)], [4, 2, 3]),
    ],
)
def test_linkedlist_insert_success(linkedlist: DoublyLinkedList, insert, expected):
    # use arrange-act-assert to write unit tests using best practices.
    for data, index in insert:
        linkedlist.insert(data=data, index=index)
    assert linkedlist.to_list() == expected


@pytest.mark.parametrize(
    "insert, error_msg",
    [
        ([(1, 1)], "Index value provided was out-of-bounds."),
        ([(2, 0), (3, -2)], "Index value provided was out-of-bounds."),
        ([(2, 0), (3, 2)], "Index value provided was out-of-bounds."),
    ],
)
def test_linkedlist_insert_error(linkedlist: DoublyLinkedList, insert, error_msg):
    with pytest.raises(
        ValueError,
        match=error_msg,
    ):
        for data, index in insert:
            linkedlist.insert(data=data, index=index)


@pytest.mark.parametrize("insert, remove, expected", [([1, 2, 3], [2], [1, 3])])
def test_linkedlist_remove_success(
    linkedlist: DoublyLinkedList, insert, remove, expected
):
    for data in insert:
        linkedlist.append(data)
    for data in remove:
        linkedlist.remove(data)
    assert linkedlist.to_list() == expected


@pytest.mark.parametrize(
    "insert, pop, expected",
    [
        ([1, 2, 3], [1], [1, 3]),
        ([1, 2, 3], [-1], [1, 2]),
        ([1], [0], []),
    ],
)
def test_linkedlist_pop_success(linkedlist: DoublyLinkedList, insert, pop, expected):
    for data in insert:
        linkedlist.append(data)
    for index in pop:
        linkedlist.pop(index)
    assert linkedlist.to_list() == expected


@pytest.mark.parametrize(
    "insert, pop, error_msg",
    [
        ([], [0], "Cannot remove from an empty linked list."),
        ([1, 2, 3], [-2], "Index value provided was out-of-bounds."),
        ([1, 2, 3], [3], "Index value provided was out-of-bounds."),
    ],
)
def test_linkedlist_pop_error(linkedlist: DoublyLinkedList, insert, pop, error_msg):
    with pytest.raises(ValueError, match=error_msg):
        for data in insert:
            linkedlist.append(data)
        for index in pop:
            linkedlist.pop(index)
