"""Tests for builtins.abs_example module."""

from __future__ import annotations

import pytest

from reprorusted_std_only.builtins.abs_example import absolute_value


class TestAbsoluteValue:
    """Test suite for absolute_value function."""

    def test_negative_integer(self) -> None:
        """Negative integer returns positive."""
        assert absolute_value(-42) == 42

    def test_positive_integer(self) -> None:
        """Positive integer returns itself."""
        assert absolute_value(7) == 7

    def test_zero(self) -> None:
        """Zero returns zero."""
        assert absolute_value(0) == 0

    def test_large_negative(self) -> None:
        """Large negative number works correctly."""
        assert absolute_value(-1_000_000) == 1_000_000

    def test_type_error_string(self) -> None:
        """Non-integer input raises TypeError."""
        with pytest.raises(TypeError, match="expected int"):
            absolute_value("x")  # type: ignore[arg-type]

    def test_type_error_float(self) -> None:
        """Float input raises TypeError."""
        with pytest.raises(TypeError, match="expected int"):
            absolute_value(3.14)  # type: ignore[arg-type]

    def test_type_error_none(self) -> None:
        """None input raises TypeError."""
        with pytest.raises(TypeError, match="expected int"):
            absolute_value(None)  # type: ignore[arg-type]

    def test_minus_one(self) -> None:
        """Minus one returns one."""
        assert absolute_value(-1) == 1
