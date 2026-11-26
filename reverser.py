"""Word-order utilities."""


def reverse_words(text):
    """Return the words in *text* in reverse order."""
    return " ".join(reversed(text.split()))
