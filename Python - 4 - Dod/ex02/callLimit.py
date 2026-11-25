from typing import Any, Callable


def callLimit(limit: int) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Return a decorator that limits calls to a function."""
    count = 0

    def callLimiter(function: Callable[..., Any]) -> Callable[..., Any]:
        """Wrap a function with a shared call counter."""
        def limit_function(*args: Any, **kwds: Any) -> Any:
            """Call the function until the configured limit is reached."""
            nonlocal count
            if count >= limit:
                print(f"Error: {function} called too many times")
                return None
            count += 1
            return function(*args, **kwds)

        return limit_function

    return callLimiter


def main() -> None:
    """Run call-limit demonstrations."""
    @callLimit(3)
    def f() -> None:
        """Print the name of the first test function."""
        print("f()")

    @callLimit(1)
    def g() -> None:
        """Print the name of the second test function."""
        print("g()")

    for _ in range(3):
        f()
        g()


if __name__ == "__main__":
    main()
