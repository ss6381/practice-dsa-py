from hashtable import HashTable
import pytest


@pytest.fixture
def table():
    return HashTable()


def test_hashtable(table: HashTable):
    input = ["item1", "item2", "item3"]
    for item in input:
        table.insert(item)
    print(table)
    assert table.size == 3

    assert table.search("item2") == 1, "item2 should be hashed to index 1."

    table.delete("item2")
    assert table.size == 2

    assert table.search("item2") == -1, "item2 should be removed."
