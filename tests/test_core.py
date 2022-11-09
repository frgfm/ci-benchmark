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
    """
    Test greet contributor.

    Args:
        name: write your description
        expected_output: write your description
    """
    assert greet_contributor(name) == expected_output
