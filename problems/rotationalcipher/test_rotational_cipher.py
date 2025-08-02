import pytest
from rotational_cipher import rotational_cipher


@pytest.mark.parametrize(
    "input_str, rotation_factor, expected",
    [
        ("All-convoYs-9-be:Alert1.", 4, "Epp-gsrzsCw-3-fi:Epivx5."),
        ("abcdZXYzxy-999.@", 200, "stuvRPQrpq-999.@"),
        (
            "abcdefghijklmNOPQRSTUVWXYZ0123456789",
            39,
            "nopqrstuvwxyzABCDEFGHIJKLM9012345678",
        ),
    ],
)
def test_rotational_cipher(input_str, rotation_factor, expected):
    assert rotational_cipher(input_str, rotation_factor) == expected
