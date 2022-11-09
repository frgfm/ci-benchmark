import pytest

from dummy_lib.core import greet_contributor, feature_a


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
        [[50, 14, 32], [10, -10, 0]],
    ],
)
def test_feature_a(input_temperatures, expected_output):
    assert feature_a(input_temperatures) == expected_output
