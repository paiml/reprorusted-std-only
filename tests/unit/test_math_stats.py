"""Tests for math_stats.math_example module."""

from __future__ import annotations

import pytest

from reprorusted_std_only.math_stats.math_example import greatest_common_divisor


class TestGreatestCommonDivisor:
    """Test suite for greatest_common_divisor function."""

    def test_basic_gcd(self) -> None:
        """GCD of 12 and 8 is 4."""
        assert greatest_common_divisor(12, 8) == 4

    def test_coprime(self) -> None:
        """GCD of coprime numbers is 1."""
        assert greatest_common_divisor(7, 13) == 1

    def test_same_number(self) -> None:
        """GCD of same number is that number."""
        assert greatest_common_divisor(5, 5) == 5

    def test_zero_first(self) -> None:
        """GCD with zero first is the other number."""
        assert greatest_common_divisor(0, 5) == 5

    def test_zero_second(self) -> None:
        """GCD with zero second is the other number."""
        assert greatest_common_divisor(5, 0) == 5

    def test_both_zero(self) -> None:
        """GCD of both zero is zero."""
        assert greatest_common_divisor(0, 0) == 0

    def test_large_numbers(self) -> None:
        """GCD of larger numbers."""
        assert greatest_common_divisor(54, 24) == 6

    def test_negative_raises(self) -> None:
        """Negative first argument raises ValueError."""
        with pytest.raises(ValueError, match="non-negative"):
            greatest_common_divisor(-1, 5)

    def test_negative_second_raises(self) -> None:
        """Negative second argument raises ValueError."""
        with pytest.raises(ValueError, match="non-negative"):
            greatest_common_divisor(5, -1)
