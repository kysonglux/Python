import string
import sys


def analyze_text(text: str) -> None:
    """
    Analyze and display character statistics for a text.
    """
    upper = sum(1 for char in text if char.isupper())
    lower = sum(1 for char in text if char.islower())
    punctuation = sum(1 for char in text if char in string.punctuation)
    spaces = sum(1 for char in text if char.isspace())
    digits = sum(1 for char in text if char.isdigit())

    print(f"The text contains {len(text)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main() -> None:
    """
    Entry point of the program.
    """
    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")

        if len(sys.argv) == 2:
            text = sys.argv[1]
        else:
            text = input("What is the text to count?\n")

        analyze_text(text)

    except AssertionError as error:
        print(f"AssertionError: {error}")
    except Exception as error:
        print(error)


if __name__ == "__main__":
    main()