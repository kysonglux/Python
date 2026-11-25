def _validate_numbers(values: list[int | float], name: str) -> None:
    if not isinstance(values, list):
        raise TypeError(f"{name} must be a list")
    if any(isinstance(value, bool) or not isinstance(value, (int, float))
           for value in values):
        raise TypeError(f"{name} must contain only integers or floats")


def give_bmi(
    height: list[int | float], weight: list[int | float]
) -> list[int | float]:
    _validate_numbers(height, "height")
    _validate_numbers(weight, "weight")

    if len(height) != len(weight):
        raise ValueError("height and weight must have the same size")
    if any(value == 0 for value in height):
        raise ValueError("height values must not be zero")

    return [current_weight / (current_height ** 2)
            for current_height, current_weight in zip(height, weight)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    _validate_numbers(bmi, "bmi")
    if isinstance(limit, bool) or not isinstance(limit, int):
        raise TypeError("limit must be an integer")

    return [current_bmi > limit for current_bmi in bmi]