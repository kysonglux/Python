import math
from typing import Any


def _quartile(values: list[float], fraction: float) -> float:
    """Return a quartile using linear interpolation."""
    position = (len(values) - 1) * fraction
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return float(values[lower])
    return float(values[lower] + (values[upper] - values[lower]) * (
        position - lower
    ))


def _calculate(
    values: list[int | float], operation: str
) -> float | int | list[float] | None:
    """Calculate one supported statistic."""
    if operation == "mean":
        return sum(values) / len(values)
    if operation == "median":
        middle = len(values) // 2
        if len(values) % 2:
            return values[middle]
        return (values[middle - 1] + values[middle]) / 2
    if operation == "quartile":
        return [_quartile(values, 0.25), _quartile(values, 0.75)]
    mean = sum(values) / len(values)
    if operation == "var":
        return sum((value - mean) ** 2 for value in values) / len(values)
    if operation == "std":
        return math.sqrt(
            sum((value - mean) ** 2 for value in values) / len(values)
        )
    return None


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """Print requested statistics for a sequence of numeric arguments."""
    try:
        if not args:
            raise ValueError("at least one value is required")
        if any(isinstance(value, bool) or not isinstance(value, (int, float))
               for value in args):
            raise TypeError("all values must be numeric")
        values = sorted(args)
        for operation in kwargs.values():
            if not isinstance(operation, str):
                raise TypeError("statistic names must be strings")
            result = _calculate(values, operation)
            if result is not None:
                print(f"{operation} : {result}")
    except (TypeError, ValueError, ZeroDivisionError):
        for _ in kwargs:
            print("ERROR")


def main() -> None:
    """Run the statistics demonstrations."""
    ft_statistics(1, 42, 360, 11, 64,
                  toto="mean", tutu="median", tata="quartile")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575,
                  hello="std", world="var")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575,
                  ejfhhe="heheh", ejdjdejn="kdekem")
    print("-----")
    ft_statistics(toto="mean", tutu="median", tata="quartile")


if __name__ == "__main__":
    main()
