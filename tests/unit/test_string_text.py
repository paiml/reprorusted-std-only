"""Tests for string_text.string_methods_example module."""

from __future__ import annotations

import pytest

from reprorusted_std_only.string_text.string_methods_example import title_case


class TestTitleCase:
    """Test suite for title_case function."""

    def test_basic_title_case(self) -> None:
        """Basic string is title-cased."""
        assert title_case("hello world") == "Hello World"

    def test_already_title_case(self) -> None:
        """Already title-cased string unchanged."""
        assert title_case("Hello World") == "Hello World"

    def test_all_uppercase(self) -> None:
        """All uppercase becomes title case."""
        assert title_case("HELLO WORLD") == "Hello World"

    def test_empty_string(self) -> None:
        """Empty string returns empty."""
        assert title_case("") == ""

    def test_single_word(self) -> None:
        """Single word is capitalized."""
        assert title_case("python") == "Python"

    def test_mixed_case(self) -> None:
        """Mixed case words are title-cased."""
        assert title_case("hELLO wORLD") == "Hello World"

    def test_type_error_int(self) -> None:
        """Integer input raises TypeError."""
        with pytest.raises(TypeError, match="expected str"):
            title_case(42)  # type: ignore[arg-type]

    def test_type_error_list(self) -> None:
        """List input raises TypeError."""
        with pytest.raises(TypeError, match="expected str"):
            title_case(["hello"])  # type: ignore[arg-type]
