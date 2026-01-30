"""Tests for typing.generics_example module."""

from __future__ import annotations

from reprorusted_std_only.typing.generics_example import first_or_default


class TestFirstOrDefault:
    """Test suite for first_or_default function."""

    def test_non_empty_list(self) -> None:
        """Returns first element of non-empty list."""
        assert first_or_default([10, 20, 30], 0) == 10

    def test_empty_list_default(self) -> None:
        """Returns default for empty list."""
        assert first_or_default([], 42) == 42

    def test_string_list(self) -> None:
        """Works with string lists."""
        assert first_or_default(["a", "b"], "z") == "a"

    def test_empty_string_default(self) -> None:
        """Returns string default for empty list."""
        assert first_or_default([], "default") == "default"

    def test_single_element(self) -> None:
        """Single element list returns that element."""
        assert first_or_default([99], 0) == 99

    def test_tuple_input(self) -> None:
        """Tuple input also works (Sequence)."""
        assert first_or_default((5, 6), 0) == 5

    def test_empty_tuple_default(self) -> None:
        """Empty tuple returns default."""
        assert first_or_default((), -1) == -1

    def test_none_default(self) -> None:
        """None can be used as default."""
        assert first_or_default([], None) is None
