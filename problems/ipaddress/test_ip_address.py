from ip_address import access
import pytest


@pytest.mark.parametrize(
    "rules, ip_address, expected",
    [
        (
            [
                ("ALLOW", "1.2.3.4/31"),
                ("ALLOW", "255.124.53.64/9"),
                ("DENY", "8.8.8.8/0"),
            ],
            "0.0.0.0",
            "DENY",
        ),
        (
            [
                ("ALLOW", "1.2.3.4/31"),
                ("ALLOW", "255.124.53.64/9"),
                ("DENY", "8.8.8.8/0"),
            ],
            "1.2.3.4",
            "ALLOW",
        ),
        (
            [
                ("ALLOW", "1.2.3.4/31"),
                ("ALLOW", "255.124.53.64/9"),
                ("DENY", "8.8.8.8/0"),
            ],
            "8.8.8.8",
            "DENY",
        ),
    ],
)
def test_access(rules, ip_address, expected):
    assert access(rules, ip_address) == expected
