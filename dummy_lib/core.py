__all__ = ["greet_contributor"]


def greet_contributor(name: str) -> str:
	"""Creates a string message to greet the contributor.

	Args:
		name: name of the person to greet

	Returns:
		the greeting message
	"""
	return f"Hello {name}! Nice to meet you."
