from inmemorydb import InMemoryDB
import pytest
from typing import List, Tuple, Dict


@pytest.fixture
def db():
    """
    Creates a fresh instance of the db for each test case,
    and tears it down afterwards.
    """
    # setup
    db = InMemoryDB()
    # yield the db object
    yield db
    # teardown
    db.clear()


@pytest.mark.parametrize(
    "insert, query, expected",
    [
        (
            [
                ("users", {"id": 1, "name": "Alice", "age": 30}),
                ("users", {"id": 2, "name": "Bob", "age": 25}),
            ],
            ("users", {"age": "> 25"}),
            [{"id": 1, "name": "Alice", "age": 30}],
        )
    ],
)
def test_inmemorydb(
    db: InMemoryDB,
    insert: List[Tuple[str, Dict[str, str]]],
    query: Tuple[str, Dict[str, str]],
    expected: List[Dict[str, any]],
):
    db.create_table("users")
    for table_name, item in insert:
        db.insert(table_name=table_name, record=item)

    # Query with filtering
    assert db.query(query[0], query[1]) == expected
