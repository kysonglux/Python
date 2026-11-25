from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Represent the combined Baratheon and Lannister king."""

    def set_eyes(self, eyes: str) -> None:
        """Set the king's eye color."""
        self.eyes = eyes

    def set_hairs(self, hairs: str) -> None:
        """Set the king's hair color."""
        self.hairs = hairs

    def get_eyes(self) -> str:
        """Return the king's eye color."""
        return self.eyes

    def get_hairs(self) -> str:
        """Return the king's hair color."""
        return self.hairs


def main() -> None:
    """Run a King characteristic demonstration."""
    joffrey = King("Joffrey")
    joffrey.set_eyes("blue")
    joffrey.set_hairs("light")
    print(joffrey.get_eyes())
    print(joffrey.get_hairs())


if __name__ == "__main__":
    main()
