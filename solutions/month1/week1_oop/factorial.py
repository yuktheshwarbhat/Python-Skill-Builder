"""Factorial of a number using recursion."""

from __future__ import annotations


def factorial(n: int) -> int:
    """Return n! computed recursively.

    >>> factorial(5)
    120
    >>> factorial(0)
    1
    """
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError("n must be an int")
    if n < 0:
        raise ValueError("n must be >= 0")

    if n <= 1:                      # base case - stops the recursion
        return 1
    return n * factorial(n - 1)     # recursive case - n shrinks toward 1