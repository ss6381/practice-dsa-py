from course_schedule import course_schedule
import pytest


@pytest.mark.parametrize(
    "prerequisites, expected",
    [
        ([(1, 0)], True),
        ([(1, 0), (0, 1)], False),
        ([(2, 1), (3, 2), (4, 2), (5, 3), (5, 4), (6, 5)], True),
        ([(2, 1), (3, 2), (4, 2), (5, 3), (5, 4), (6, 5), (1, 6)], False),
    ],
)
def test_course_schedule(prerequisites, expected):
    assert course_schedule(prerequisites) == expected
