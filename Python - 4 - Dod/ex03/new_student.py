import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generate a random fifteen-character lowercase identifier."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Represent a student with generated login and identifier fields."""

    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self) -> None:
        """Create the login from the student's name and surname."""
        self.login = (self.name[0] + self.surname).capitalize()


def main() -> None:
    """Run the student dataclass demonstration."""
    student = Student(name="Edward", surname="agle")
    print(student)


if __name__ == "__main__":
    main()
