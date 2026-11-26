"""Text-cleaning utilities."""


def clean_text(text):
    """Trim text and collapse repeated whitespace to one space."""
    return " ".join(text.split())
