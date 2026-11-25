class calculator:
    """Perform arithmetic operations on two vectors."""

    @staticmethod
    def dotproduct(v1: list[float], v2: list[float]) -> None:
        """Print the dot product of two vectors."""
        print(f"Dot product is: {sum(a * b for a, b in zip(v1, v2))}")

    @staticmethod
    def add_vec(v1: list[float], v2: list[float]) -> None:
        """Print the element-wise sum of two vectors."""
        print(f"Add Vector is: {[float(a + b) for a, b in zip(v1, v2)]}")

    @staticmethod
    def sous_vec(v1: list[float], v2: list[float]) -> None:
        """Print the element-wise difference of two vectors."""
        print(f"Sous Vector is: {[float(a - b) for a, b in zip(v1, v2)]}")


def main() -> None:
    """Run vector calculator demonstrations."""
    a = [5, 10, 2]
    b = [2, 4, 3]
    calculator.dotproduct(a, b)
    calculator.add_vec(a, b)
    calculator.sous_vec(a, b)


if __name__ == "__main__":
    main()
