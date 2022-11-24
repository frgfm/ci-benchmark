import pytest

from dummy_lib.core import (TemperatureScale, convert_temperature_sequences,
                            greet_contributor)


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
    "input_temperatures, input_scale, output_scale, error_type, expected_output",
    [
        [[], None, None, None, []],
        # Fahrenheit to Celsius
        [[50, 14.0, 32], None, None, None, [10, -10.0, 0]],
        [
            [50, 14.0, 32],
            TemperatureScale.FAHRENHEIT,
            TemperatureScale.CELSIUS,
            None,
            [10, -10.0, 0],
        ],
        # Celsius to Fahrenheit
        [
            [10, -10.0, 0],
            TemperatureScale.CELSIUS,
            TemperatureScale.FAHRENHEIT,
            None,
            [50, 14.0, 32],
        ],
        # Same scale
        [
            [10, -10.0, 0],
            TemperatureScale.CELSIUS,
            TemperatureScale.CELSIUS,
            None,
            [10, -10.0, 0],
        ],
        # Error
        [[10, -10.0, 0], TemperatureScale.CELSIUS, "kelvin", NotImplementedError, None],
    ],
)
def test_convert_temperature_sequences(
    input_temperatures, input_scale, output_scale, error_type, expected_output
):
    kwargs = {}
    if input_scale is not None:
        kwargs["input_scale"] = input_scale
    if output_scale is not None:
        kwargs["output_scale"] = output_scale

    if error_type is None:
        assert (
            convert_temperature_sequences(input_temperatures, **kwargs)
            == expected_output
        )
    else:
        with pytest.raises(error_type):
            convert_temperature_sequences(input_temperatures, **kwargs)
