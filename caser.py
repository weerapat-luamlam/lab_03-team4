"""Word-capitalization helpers."""


def capitalize_words(text):
    """Capitalize the first letter of every word in text."""
    return " ".join(word.capitalize() for word in text.split())
