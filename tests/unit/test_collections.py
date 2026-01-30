"""Tests for collections.counter_example module."""

from __future__ import annotations

import pytest

from reprorusted_std_only.collections.counter_example import count_words


class TestCountWords:
    """Test suite for count_words function."""

    def test_basic_counting(self) -> None:
        """Basic word counting returns correct frequencies."""
        result = count_words("hello world hello")
        assert result == {"hello": 2, "world": 1}

    def test_single_word(self) -> None:
        """Single word returns count of one."""
        assert count_words("python") == {"python": 1}

    def test_empty_string(self) -> None:
        """Empty string returns empty dict."""
        assert count_words("") == {}

    def test_all_same_words(self) -> None:
        """All same words returns single entry."""
        assert count_words("go go go") == {"go": 3}

    def test_multiple_spaces(self) -> None:
        """Multiple spaces between words handled by split."""
        result = count_words("a  b   c")
        assert result == {"a": 1, "b": 1, "c": 1}

    def test_type_error_int(self) -> None:
        """Integer input raises TypeError."""
        with pytest.raises(TypeError, match="expected str"):
            count_words(42)  # type: ignore[arg-type]

    def test_type_error_list(self) -> None:
        """List input raises TypeError."""
        with pytest.raises(TypeError, match="expected str"):
            count_words(["hello"])  # type: ignore[arg-type]

    def test_whitespace_only(self) -> None:
        """Whitespace-only string returns empty dict."""
        assert count_words("   ") == {}
