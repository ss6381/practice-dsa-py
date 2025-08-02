from function_time import calculate_function_time
import pytest


@pytest.mark.parametrize("logs, expected, explanation", [
    (
        ["0:start:0", "0:start:2", "0:end:5", "1:start:7",
            "0:start:8", "0:end:9", "1:end:10", "0:end:12"],
        [9, 3],
        "Function 0 runs for 9 time units [0, 1, 2, 3, 4, 5, 6, 8, 9, 12], recursively calling itself. Function 1 runs for 3 time units [7, 10, 11]."
    ),
    (
        ["0:start:0", "1:start:2", "1:end:5", "2:start:7", "2:end:8", "0:end:9"],
        [4, 4, 2],
        "Function 0 runs for 4 time units [0, 1, 6, 9], function 1 runs for 4 time units [2, 3, 4, 5], and function 2 runs for 2 time units [7, 8]."
    ),
    (
        ["0:start:0", "1:start:2", "1:end:5", "0:end:6"],
        [3, 4],
        "Function 0 runs for 3 time units [0, 1, 6], and function 1 runs for 4 time units [2, 3, 4, 5]."
    ),
])
def test_calculate_function_time(logs, expected, explanation):
    assert calculate_function_time(logs) == expected, explanation
