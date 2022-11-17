from typing import List

__all__ = ["greet_contributor", "feature_a"]


def greet_contributor(name: str) -> str:
	"""Creates a string message to greet the contributor.

	Args:
		name: name of the person to greet

	Returns:
		the greeting message
	"""
	return f"Hello {name}! Nice to meet you."


def feature_a(input_temperatures: List[float]) -> List[float]:
	"""Converts temperatures from Fahrenheit to Celsius.

	Args:
		input_temperatures: the list of temperatures in Fahrenheit

	Returns:
		the temperatures converted to Celsius
	"""

	return [
		(fahrenheit_temp - 32) * 5 / 9 for fahrenheit_temp in input_temperatures
	]
