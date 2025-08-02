from arraylist import ArrayList
import pytest


@pytest.fixture
def arraylist():
    """Creates a fresh instance of the arraylist for each test case."""
    return ArrayList()


@pytest.mark.parametrize("items, expected", [([6, 2, 3, 7, 8], [6, 2, 3, 7, 8])])
def test_append(arraylist: ArrayList, items, expected):
    for item in items:
        arraylist.append(item)
    assert arraylist.items == expected


@pytest.mark.parametrize("items, expected", [([6, 2, 3, 7, 8], [2, 3, 6, 7, 8])])
def test_insert_sorted(arraylist: ArrayList, items, expected):
    for item in items:
        arraylist.insert_sorted(item)
    assert arraylist.items == expected


@pytest.mark.parametrize("items, expected", [([1, 2], 1)])
def test_pop(arraylist: ArrayList, items, expected):
    for item in items:
        arraylist.append(item)
    assert arraylist.pop(0) == expected, "item was not removed properly."


def test_pop_throws_indexerror(arraylist: ArrayList):
    with pytest.raises(IndexError, match="Cannot remove from empty list."):
        arraylist.pop()


@pytest.mark.parametrize("items, index", [([1, 2, 3], 3), ([4, 5], 2)])
def test_pop_throws_valueerror(arraylist: ArrayList, items, index):
    for item in items:
        arraylist.append(item)
    with pytest.raises(ValueError, match="Input index provided is out of bounds."):
        arraylist.pop(index)


@pytest.mark.parametrize("items, expected", [([6, 2, 3, 7, 8], [2, 3, 6, 7, 8])])
def test_sort(arraylist: ArrayList, items, expected):
    for item in items:
        arraylist.append(item)
    arraylist.sort()
    assert arraylist.items == expected


@pytest.mark.parametrize("items, target, expected", [([2, 3, 6, 7, 8], 7, 3)])
def test_search(arraylist: ArrayList, items, target, expected):
    for item in items:
        arraylist.append(item)
    arraylist.sort()
    assert arraylist.search(target) == expected
