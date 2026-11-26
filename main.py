"""Run the four textkit functions with sample input."""

from caser import capitalize_words
from cleaner import clean_text
from counter import count_words
from reverser import reverse_words


def show_result(name, operation):
    """Print a function result or its initial not-implemented state."""
    try:
        print(f"{name}: {operation()}")
    except NotImplementedError:
        print(f"{name}: not implemented yet")


def main():
    """Run one example for each textkit function."""
    show_result("count_words", lambda: count_words("a b c"))
    show_result(
        "reverse_words",
        lambda: reverse_words("hello first year"),
    )
    show_result(
        "clean_text",
        lambda: clean_text("  hello   world "),
    )
    show_result(
        "capitalize_words",
        lambda: capitalize_words("hello first year"),
    )


if __name__ == "__main__":
    main()
