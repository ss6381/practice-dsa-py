from typing import List
from track_max_stack import Stack
import pytest


@pytest.fixture
def stack():
    return Stack()


@pytest.mark.parametrize(
    "push, expected_pop, expected_max",
    [
        ([5, 2, 3, 6], [], 6),
        ([5, 2, 3, 6], [6], 5),
        ([5, 2, 3, 6], [6, 3], 5),
        ([5, 2, 3, 6], [6, 3, 2], 5),
    ],
)
def test_stack_success(
    stack: Stack, push: List[int], expected_pop: List[int], expected_max: int
):
    for item in push:
        stack.push(item)
    for pop in expected_pop:
        assert stack.pop() == pop
    assert stack.size == len(push) - len(expected_pop)
    assert stack.get_max() == expected_max


@pytest.mark.parametrize(
    "push, num_pop, err_msg",
    [
        ([], 1, "Cannot pop when stack is empty."),
        ([5, 2, 3, 6], 5, "Cannot pop when stack is empty."),
    ],
)
def test_stack_pop_error(stack: Stack, push: List[int], num_pop: int, err_msg: str):
    with pytest.raises(IndexError, match=err_msg):
        for item in push:
            stack.push(item)
        for _ in range(num_pop):
            stack.pop()


@pytest.mark.parametrize(
    "push, num_pop, err_msg",
    [
        ([], 0, "Cannot get max when stack is empty."),
        ([5, 2, 3, 6], 4, "Cannot get max when stack is empty."),
    ],
)
def test_stack__get_max_error(
    stack: Stack, push: List[int], num_pop: int, err_msg: str
):
    with pytest.raises(IndexError, match=err_msg):
        for item in push:
            stack.push(item)
        for _ in range(num_pop):
            stack.pop()
        stack.get_max()
