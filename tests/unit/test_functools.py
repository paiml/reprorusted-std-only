"""Tests for functools.reduce_example module."""

from __future__ import annotations

from reprorusted_std_only.functools.reduce_example import product


class TestProduct:
    """Test suite for product function."""

    def test_basic_product(self) -> None:
        """Product of [2, 3, 4] is 24."""
        assert product([2, 3, 4]) == 24

    def test_factorial_like(self) -> None:
        """Product of [1, 2, 3, 4, 5] is 120."""
        assert product([1, 2, 3, 4, 5]) == 120

    def test_empty_sequence(self) -> None:
        """Empty sequence returns identity 1."""
        assert product([]) == 1

    def test_single_element(self) -> None:
        """Single element returns that element."""
        assert product([7]) == 7

    def test_contains_zero(self) -> None:
        """Product with zero is zero."""
        assert product([5, 0, 3]) == 0

    def test_all_ones(self) -> None:
        """Product of all ones is one."""
        assert product([1, 1, 1]) == 1

    def test_negative_numbers(self) -> None:
        """Product of two negatives is positive."""
        assert product([-2, -3]) == 6

    def test_tuple_input(self) -> None:
        """Tuple input also works (Sequence protocol)."""
        assert product((2, 5)) == 10
