"""Main module for the helloworld package."""

from core import greeter


def main() -> None:
    """Run the main routine."""
    greeter.greet()


if __name__ == "__main__":
    main()
