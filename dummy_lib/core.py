# Copyright (C) 2022, François-Guillaume Fernandez.

# This program is licensed under the Apache License 2.0.
# See LICENSE or go to <https://www.apache.org/licenses/LICENSE-2.0> for full license details.

from typing import List

__all__ = ["greet_contributor", "convert_fahrenheit_to_celsius"]


def greet_contributor(name: str) -> str:
    """Creates a string message to greet the contributor.

    Args:
            name: name of the person to greet

    Returns:
            the greeting message
    """
    return f"Hello {name}! Nice to meet you."


def convert_fahrenheit_to_celsius(input_temperatures: List[float]) -> List[float]:
    """Converts temperatures from Fahrenheit to Celsius.

    Args:
            input_temperatures: the list of temperatures in Fahrenheit

    Returns:
            the temperatures converted to Celsius
    """

    return [(fahrenheit_temp - 32) * 5 / 9 for fahrenheit_temp in input_temperatures]
