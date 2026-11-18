import pytest
from solutions.month1.week1_oop.palindrome import is_palindrome


@pytest.mark.parametrize(
    "text", ["", "a", "aba", "A man, a plan, a canal: Panama", "12321"]
)
def test_valid_palindromes(text: str) -> None:
    assert is_palindrome(text) is True


@pytest.mark.parametrize("text", ["embedded", "abc", "ESP32"])
def test_invalid_palindromes(text: str) -> None:
    assert is_palindrome(text) is False
