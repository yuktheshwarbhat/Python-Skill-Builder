from __future__ import annotations


def is_palindrome(text: str) -> bool:
    """Return True if text reads the same backwards, ignoring case/punctuation."""
    cleaned = "".join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]
