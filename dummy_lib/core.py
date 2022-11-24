# Copyright (C) 2022, François-Guillaume Fernandez.

# This program is licensed under the Apache License 2.0.
# See LICENSE or go to <https://www.apache.org/licenses/LICENSE-2.0> for full license details.

from enum import Enum
from typing import List

__all__ = ["greet_contributor", "convert_temperature_sequences", "TemperatureScale"]


class TemperatureScale(Enum):
    """Temparature scale
    Available values are ``celsius``, ``fahrenheit``.
    """

    CELSIUS = "celsius"
    FAHRENHEIT = "fahrenheit"


def greet_contributor(name: str) -> str:
	"""Creates a string message to greet the contributor.

	Args:
		name: name of the person to greet

	Returns:
		the greeting message
	"""
	return f"Hello {name}! Nice to meet you."


def convert_temperature_sequences(
	input_temperatures: List[float],
	input_scale: TemperatureScale = TemperatureScale.FAHRENHEIT,
	output_scale: TemperatureScale = TemperatureScale.CELSIUS,
) -> List[float]:
	"""Converts temperatures from one scale to another.

	Args:
		input_temperatures: the list of temperatures

	Returns:
		the temperatures converted to the expected scale
	"""

	if input_scale == output_scale:
		return input_temperatures

	if input_scale == TemperatureScale.FAHRENHEIT and output_scale == TemperatureScale.CELSIUS:
		return [
			(fahrenheit_temp - 32) * 5 / 9 for fahrenheit_temp in input_temperatures
		]
	elif input_scale == TemperatureScale.CELSIUS and output_scale == TemperatureScale.FAHRENHEIT:
		return [
			celsius_temp * 9 / 5 + 32 for celsius_temp in input_temperatures
		]

	raise NotImplementedError
