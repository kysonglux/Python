class calculator:
    """Perform arithmetic operations on a vector and a scalar."""

    def __init__(self, vector: list[float]) -> None:
        """Initialize the calculator with a vector."""
        self.vector = vector

    def __add__(self, object: float) -> None:
        """Add a scalar to every vector element and print the result."""
        self.vector = [value + object for value in self.vector]
        print(self.vector)

    def __mul__(self, object: float) -> None:
        """Multiply every vector element by a scalar and print the result."""
        self.vector = [value * object for value in self.vector]
        print(self.vector)

    def __sub__(self, object: float) -> None:
        """Subtract a scalar from every vector element and print the result."""
        self.vector = [value - object for value in self.vector]
        print(self.vector)

    def __truediv__(self, object: float) -> None:
        """Divide every vector element by a scalar and print the result."""
        if object == 0:
            print("Division by zero is not possible.")
            return
        self.vector = [value / object for value in self.vector]
        print(self.vector)


def main() -> None:
    """Run calculator demonstrations."""
    v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v1 + 5
    v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v2 * 5
    v3 = calculator([10.0, 15.0, 20.0])
    v3 - 5
    v3 / 5


if __name__ == "__main__":
    main()
