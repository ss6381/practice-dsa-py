from match_parentheses import remove_invalid_parenthesis
import pytest


@pytest.mark.parametrize(
    "s, expected",
    [("()", "()"), ("((a)", "(a)"), ("(a))()", "(a)()"), ("(a)(()", "(a)()")],
)
def test_remove_invalid_parenthesis(s: str, expected: str):
    assert remove_invalid_parenthesis(s) == expected
