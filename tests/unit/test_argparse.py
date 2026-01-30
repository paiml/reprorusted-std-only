"""Tests for argparse.basic_example module."""

from __future__ import annotations

import pytest

from reprorusted_std_only.argparse.basic_example import build_greeting


class TestBuildGreeting:
    """Test suite for build_greeting function."""

    def test_single_greeting(self) -> None:
        """Single greeting returns just the greeting."""
        assert build_greeting("World", 1) == "Hello, World!"

    def test_default_count(self) -> None:
        """Default count is 1."""
        assert build_greeting("Alice") == "Hello, Alice!"

    def test_multiple_greetings(self) -> None:
        """Multiple greetings joined by newline."""
        result = build_greeting("Bob", 3)
        assert result == "Hello, Bob!\nHello, Bob!\nHello, Bob!"

    def test_two_greetings(self) -> None:
        """Two greetings."""
        assert build_greeting("Eve", 2) == "Hello, Eve!\nHello, Eve!"

    def test_zero_count_raises(self) -> None:
        """Count of zero raises ValueError."""
        with pytest.raises(ValueError, match="count must be at least 1"):
            build_greeting("X", 0)

    def test_negative_count_raises(self) -> None:
        """Negative count raises ValueError."""
        with pytest.raises(ValueError, match="count must be at least 1"):
            build_greeting("X", -5)

    def test_empty_name(self) -> None:
        """Empty name is allowed."""
        assert build_greeting("", 1) == "Hello, !"

    def test_name_with_spaces(self) -> None:
        """Name with spaces works."""
        assert build_greeting("Big World", 1) == "Hello, Big World!"
