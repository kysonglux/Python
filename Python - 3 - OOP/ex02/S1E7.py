from S1E9 import Character


class Baratheon(Character):
    """Represent the Baratheon family."""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """Initialize a Baratheon character."""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self) -> None:
        """Set the character's health state to dead."""
        super().die()

    def __str__(self) -> str:
        """Return the physical characteristics as a string."""
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"

    def __repr__(self) -> str:
        """Return the printable representation of the character."""
        return self.__str__()


class Lannister(Character):
    """Represent the Lannister family."""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """Initialize a Lannister character."""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self) -> None:
        """Set the character's health state to dead."""
        super().die()

    def __str__(self) -> str:
        """Return the physical characteristics as a string."""
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"

    def __repr__(self) -> str:
        """Return the printable representation of the character."""
        return self.__str__()

    @classmethod
    def create_lannister(
        cls, first_name: str, is_alive: bool = True
    ) -> "Lannister":
        """Create a Lannister character through the class."""
        return cls(first_name, is_alive)
