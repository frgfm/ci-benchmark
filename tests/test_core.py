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
    assert greet_contributor(name) == expected_output


@pytest.mark.parametrize(
    "input_temperatures, expected_output",
    [
        [[], []],
        [[50, 14.0, 32], [10, -10.0, 0]],
    ],
)
def test_convert_fahrenheit_to_celsius(input_temperatures, expected_output):
    assert convert_fahrenheit_to_celsius(input_temperatures) == expected_output
