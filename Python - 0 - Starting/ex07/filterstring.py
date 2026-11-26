import sys


def filter_words(text: str, length: int) -> list:
    """
    Return words whose length is greater than length.
    """

    longer_than = lambda word: len(word) > length
    return [word for word in text.split() if longer_than(word)] 


def main() -> None:
    """
    Main function.
    """
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")

        text = sys.argv[1]

        try:
            length = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")

        print(filter_words(text, length))

    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()

