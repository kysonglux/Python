from typing import Callable


def square(x: int | float) -> int | float:
    """Return the square of a number."""
    return x * x


def pow(x: int | float) -> int | float:
    """Return a number raised to its own power."""
    return x ** x


def outer(
    x: int | float, function: Callable[[int | float], int | float]
) -> Callable[[], int | float]:
    """Return a closure that repeatedly applies a function to its result."""
    value = x

    def inner() -> int | float:
        """Apply the function to the current value and store the result."""
        nonlocal value
        value = function(value)
        return value

    return inner


def main() -> None:
    """Run closure demonstrations."""
    counter = outer(3, square)
    print(counter())
    print(counter())
    print(counter())
    print("---")
    another_counter = outer(1.5, pow)
    print(another_counter())
    print(another_counter())
    print(another_counter())


if __name__ == "__main__":
    main()
