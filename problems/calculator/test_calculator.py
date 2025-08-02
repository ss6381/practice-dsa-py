from calculator import calculate
import pytest


@pytest.mark.parametrize(
    "input, expected",
    [
        ("(14+5)+2+3+(2+5+6)+1", 38),
        ("(1+(4+5+2)-3)+(6+8)", 23),
        ("3+24-5", 22),
        # ("54-2-(6-4)-7-(2-5)", 46),
    ],
)
def test_calculate_success(input, expected):
    assert calculate(input) == expected


@pytest.mark.parametrize(
    "input, err_msg", [("1+?", "Unknown or invalid character found in input: ?")]
)
def test_calculate_error(input, err_msg):
    with pytest.raises(ValueError, match=err_msg):
        calculate(input)
