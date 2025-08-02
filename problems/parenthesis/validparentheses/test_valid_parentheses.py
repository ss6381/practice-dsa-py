from valid_parentheses import is_valid_parenthesis
import pytest


@pytest.mark.parametrize(
    "s, expected",
    [
        ("()", True),
        ("{}", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("[[(]])", False),
        ("{}}", False),
        ("{({[{}({})]})}", True),
    ],
)
def test_is_valid_parenthesis(s: str, expected: bool):
    assert is_valid_parenthesis(s) == expected
