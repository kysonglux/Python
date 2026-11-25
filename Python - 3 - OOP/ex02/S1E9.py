from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract base class for a character."""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """Initialize a character with a name and health state."""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self) -> None:
        """Set the character's health state to dead."""
        self.is_alive = False


class Stark(Character):
    """Represent a character from House Stark."""

    def die(self) -> None:
        """Set this Stark character's health state to dead."""
        super().die()
