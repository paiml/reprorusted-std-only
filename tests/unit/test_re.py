"""Tests for re.match_example module."""

from __future__ import annotations

import pytest

from reprorusted_std_only.re.match_example import is_valid_email


class TestIsValidEmail:
    """Test suite for is_valid_email function."""

    def test_valid_email(self) -> None:
        """Standard email is valid."""
        assert is_valid_email("user@example.com") is True

    def test_valid_with_dots(self) -> None:
        """Email with dots in local part is valid."""
        assert is_valid_email("first.last@example.com") is True

    def test_valid_with_plus(self) -> None:
        """Email with plus sign is valid."""
        assert is_valid_email("user+tag@example.com") is True

    def test_invalid_no_at(self) -> None:
        """String without @ is invalid."""
        assert is_valid_email("not-an-email") is False

    def test_invalid_no_domain(self) -> None:
        """String with @ but no domain is invalid."""
        assert is_valid_email("user@") is False

    def test_invalid_no_local(self) -> None:
        """String with @ but no local part is invalid."""
        assert is_valid_email("@example.com") is False

    def test_empty_string(self) -> None:
        """Empty string is invalid."""
        assert is_valid_email("") is False

    def test_type_error_int(self) -> None:
        """Integer input raises TypeError."""
        with pytest.raises(TypeError, match="expected str"):
            is_valid_email(42)  # type: ignore[arg-type]

    def test_type_error_none(self) -> None:
        """None input raises TypeError."""
        with pytest.raises(TypeError, match="expected str"):
            is_valid_email(None)  # type: ignore[arg-type]
