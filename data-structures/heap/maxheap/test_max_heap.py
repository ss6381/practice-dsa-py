from max_heap import MaxHeap
import pytest
import heapq


@pytest.fixture
def heap():
    return MaxHeap()


@pytest.mark.parametrize(
    "insert, expected",
    [
        ([10, 20, 30, 14, 52, 23, 63], [63, 30, 52, 10, 14, 20, 23]),
        ([10, 20, 30, 14, 52, 23], [52, 30, 23, 10, 14, 20]),
    ],
)
def test_max_heap_insert(heap, insert, expected):
    for item in insert:
        heap.insert(item)

    assert heap.array == expected

    py_heap = [-x for x in insert]
    heapq.heapify(py_heap)
    py_heap = [-x for x in py_heap]
    assert heap.get_max() == py_heap[0]

    assert heap.get_max() == max(insert)


@pytest.mark.parametrize(
    "insert, extract, expected",
    [
        ([10, 20, 30, 14, 52, 23, 63], 0, 63),
        ([10, 20, 52, 30, 14, 23], 0, 52),
        ([10, 20, 52, 30, 14, 23], 1, 30),
        ([10, 20, 52], 3, -1),
    ],
)
def test_max_heap_extract(heap, insert, extract, expected):
    for item in insert:
        heap.insert(item)
    for _ in range(extract):
        heap.extract()

    max = -1
    for item in heap.array:
        if item > max:
            max = item

    assert heap.get_max() == max
    assert heap.get_max() == expected


@pytest.mark.parametrize(
    "insert, extract, expected",
    [
        ([10, 20, 30, 14, 52, 23, 63], 0, 63),
        ([10, 20, 52, 30, 14, 23], 0, 52),
        ([10, 20, 52, 30, 14, 23], 1, 30),
    ],
)
def test_max_heap_extract(heap, insert, extract, expected):
    py_heap = [-x for x in insert]
    heapq.heapify(py_heap)
    for item in insert:
        heap.insert(item)
    for _ in range(extract):
        heap.extract()
        heapq.heappop(py_heap)
    py_heap = [-x for x in py_heap]
    assert heap.get_max() == py_heap[0] == expected
