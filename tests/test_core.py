import pytest

from dummy_lib.core import greet_contributor, convert_fahrenheit_to_celsius


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


@pytest.mark.parametrize(
    "input_temperatures, expected_output",
    [
        [[], []],
        [[50, 14., 32], [10, -10., 0]],
    ],
)
def test_convert_fahrenheit_to_celsius(input_temperatures, expected_output):
    """
    Test that the conversion function can be performed on the given fahrenheit temperatures.

    Args:
        input_temperatures: write your description
        expected_output: write your description
    """
    assert convert_fahrenheit_to_celsius(input_temperatures) == expected_output
