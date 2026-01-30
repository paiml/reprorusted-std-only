"""Tests for concurrency.threading_example module."""

from __future__ import annotations

import pytest

from reprorusted_std_only.concurrency.threading_example import threaded_sum


class TestThreadedSum:
    """Test suite for threaded_sum function."""

    def test_basic_sum(self) -> None:
        """Sum of 1..4 is 10."""
        assert threaded_sum(4) == 10

    def test_five_threads(self) -> None:
        """Sum of 1..5 is 15."""
        assert threaded_sum(5) == 15

    def test_zero_threads(self) -> None:
        """Zero threads returns zero."""
        assert threaded_sum(0) == 0

    def test_single_thread(self) -> None:
        """Single thread returns 1."""
        assert threaded_sum(1) == 1

    def test_ten_threads(self) -> None:
        """Sum of 1..10 is 55."""
        assert threaded_sum(10) == 55

    def test_negative_raises(self) -> None:
        """Negative n raises ValueError."""
        with pytest.raises(ValueError, match="non-negative"):
            threaded_sum(-1)

    def test_negative_large_raises(self) -> None:
        """Large negative raises ValueError."""
        with pytest.raises(ValueError, match="non-negative"):
            threaded_sum(-100)

    def test_two_threads(self) -> None:
        """Sum of 1..2 is 3."""
        assert threaded_sum(2) == 3
