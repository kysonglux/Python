from typing import Iterable, Any


def count_in_list(values: Iterable[Any], target: Any) -> int:
    """Return the number of occurrences of target in values."""
    return sum(1 for value in values if value == target)


__all__ = ["count_in_list"]
