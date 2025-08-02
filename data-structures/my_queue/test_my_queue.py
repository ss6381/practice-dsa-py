from my_queue import MyQueue
import pytest


@pytest.fixture
def queue():
    return MyQueue()


@pytest.mark.parametrize(
    "insert, pop_count, expected",
    [
        ([2, 6, 1, 5, 3, 1, 7], 0, [2, 6, 1, 5, 3, 1, 7]),
        ([2, 6, 1, 5, 3, 1, 7], 2, [1, 5, 3, 1, 7]),
    ],
)
def test_queue_success(queue, insert, pop_count, expected):
    for item in insert:
        queue.enqueue(item)
    for _ in range(pop_count):
        queue.dequeue()
    assert list(queue.items) == expected


@pytest.mark.parametrize(
    "insert, pop_count, error_msg",
    [
        ([], 1, "Cannot dequeue from an empty queue."),
        ([2, 6], 3, "Cannot dequeue from an empty queue."),
    ],
)
def test_queue_error(queue, insert, pop_count, error_msg):
    with pytest.raises(IndexError, match=error_msg):
        for item in insert:
            queue.enqueue(item)
        for _ in range(pop_count):
            queue.dequeue()
