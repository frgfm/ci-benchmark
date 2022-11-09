import pytest

from dummy_lib.core import greet_contributor


@pytest.mark.parametrize(
    "name, expected_output",
    [
        ["there", "Hello there! Nice to meet you."],
        ["Linus", "Hello Linus! Nice to meet you."],
    ],
)
def test_greet_contributor(name, expected_output):
    assert greet_contributor(name) == expected_output
