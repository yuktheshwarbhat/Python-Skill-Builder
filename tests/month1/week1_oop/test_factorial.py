"""Tests for Q24 - recursive factorial."""

import pytest

from solutions.month1.week1_oop.factorial import factorial


def test_five_returns_120() -> None:
    """The stated requirement."""
    assert factorial(5) == 120


@pytest.mark.parametrize(
    ("n", "expected"),
    [(0, 1), (1, 1), (2, 2), (3, 6), (4, 24), (5, 120), (7, 5040), (10, 3628800)],
)
def test_known_values(n: int, expected: int) -> None:
    assert factorial(n) == expected


def test_negative_raises() -> None:
    with pytest.raises(ValueError, match=">= 0"):
        factorial(-1)


@pytest.mark.parametrize("bad", [1.5, "5", None, True])
def test_bad_type_raises(bad: object) -> None:
    with pytest.raises(TypeError):
        factorial(bad)  # type: ignore[arg-type]


def test_recursion_limit_is_real() -> None:
    """Recursion consumes stack frames - iterative would not fail here."""
    with pytest.raises(RecursionError):
        factorial(5000)