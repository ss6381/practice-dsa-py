from fill_merchants import split, Merchant
import pytest


@pytest.mark.parametrize(
    "input, amount, expected",
    [
        (
            [
                Merchant(key="a", capacity=20),
                Merchant(key="c", capacity=10),
                Merchant(key="d", capacity=100),
                Merchant(key="b", capacity=100),
            ],
            100,
            [
                ("a", 20),
                ("c", 10),
                ("d", 35),
                ("b", 35),
            ],
        ),
        (
            [
                Merchant(key="a", capacity=20),
                Merchant(key="c", capacity=10),
                Merchant(key="d", capacity=100),
                Merchant(key="b", capacity=100),
            ],
            101,
            [
                ("a", 20),
                ("c", 10),
                ("d", 36),
                ("b", 35),
            ],
        ),
        # (
        #     [
        #         Merchant(key="a", capacity=20),
        #         Merchant(key="c", capacity=10),
        #         Merchant(key="d", capacity=110),
        #         Merchant(key="b", capacity=110),
        #         Merchant(key="e", capacity=100),
        #         Merchant(key="f", capacity=100),
        #     ],
        #     200,
        #     [
        #         ("a", 20),
        #         ("c", 10),
        #         ("d", 42),
        #         ("b", 44),
        #         ("e", 42),
        #         ("f", 42),
        #     ],
        # ),
    ],
)
def test_split(input, amount, expected):
    assert split(input, amount) == expected
