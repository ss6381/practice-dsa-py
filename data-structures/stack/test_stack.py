from stack import Stack
import pytest


@pytest.fixture
def stack():
    return Stack()


@pytest.mark.parametrize(
    "push, pop_count, expected",
    [
        ([2, 6, 1, 5, 3, 1, 7], 0, [2, 6, 1, 5, 3, 1, 7]),
        ([2, 6, 1, 5, 3, 1, 7], 2, [2, 6, 1, 5, 3]),
    ],
)
def test_stack_success(stack: Stack, push, pop_count, expected):
    for item in push:
        stack.push(item)
    for _ in range(pop_count):
        stack.pop()
    assert stack.items == expected


@pytest.mark.parametrize(
    "push, pop_count, error_msg",
    [
        ([], 1, "Cannot pop from an empty stack."),
        ([2, 6], 3, "Cannot pop from an empty stack."),
    ],
)
def test_stack_error(stack: Stack, push, pop_count, error_msg):
    with pytest.raises(IndexError, match=error_msg):
        for item in push:
            stack.push(item)
        for _ in range(pop_count):
            stack.pop()
