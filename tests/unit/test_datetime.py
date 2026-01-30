"""Tests for datetime.basic_example module."""

from __future__ import annotations

import pytest

from reprorusted_std_only.datetime.basic_example import days_between


class TestDaysBetween:
    """Test suite for days_between function."""

    def test_basic_difference(self) -> None:
        """30-day difference computed correctly."""
        assert days_between("2024-01-01", "2024-01-31") == 30

    def test_same_date(self) -> None:
        """Same date returns zero."""
        assert days_between("2024-06-15", "2024-06-15") == 0

    def test_reversed_order(self) -> None:
        """Absolute difference regardless of order."""
        assert days_between("2024-03-15", "2024-03-01") == 14

    def test_across_months(self) -> None:
        """Difference across month boundaries."""
        assert days_between("2024-01-15", "2024-03-15") == 60

    def test_leap_year(self) -> None:
        """Feb 28 to Mar 1 in leap year is 2 days."""
        assert days_between("2024-02-28", "2024-03-01") == 2

    def test_invalid_date_raises(self) -> None:
        """Invalid date string raises ValueError."""
        with pytest.raises(ValueError):
            days_between("not-a-date", "2024-01-01")

    def test_invalid_second_date_raises(self) -> None:
        """Invalid second date string raises ValueError."""
        with pytest.raises(ValueError):
            days_between("2024-01-01", "invalid")

    def test_year_difference(self) -> None:
        """Difference across years."""
        result = days_between("2023-01-01", "2024-01-01")
        assert result == 365
