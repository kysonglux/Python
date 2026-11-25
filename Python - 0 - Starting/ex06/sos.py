import sys


NESTED_MORSE = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "": "/"
}


def encode_morse(text: str) -> str:
    """
    Convert a string into Morse code.
    """
    return " ".join(NESTED_MORSE[char] for char in text.upper())


def validate_text(text: str) -> None:
    """
    Check that the text contains only alphanumeric
    characters and spaces.
    """
    if not all(char.isalnum() or char.isspace() for char in text):
        raise AssertionError("the arguments are bad")


def main() -> None:
    """
    Main function.
    """
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")

        text = sys.argv[1]

        validate_text(text)

        print(encode_morse(text))

    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()