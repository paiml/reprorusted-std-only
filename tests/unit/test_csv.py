"""Tests for csv.reader_example module."""

from __future__ import annotations

import pytest

from reprorusted_std_only.csv.reader_example import parse_csv


class TestParseCsv:
    """Test suite for parse_csv function."""

    def test_basic_csv(self) -> None:
        """Basic CSV string parsed correctly."""
        result = parse_csv("a,b\n1,2")
        assert result == [["a", "b"], ["1", "2"]]

    def test_three_rows(self) -> None:
        """Three rows parsed correctly."""
        result = parse_csv("name,age\nAlice,30\nBob,25")
        assert result == [["name", "age"], ["Alice", "30"], ["Bob", "25"]]

    def test_empty_string(self) -> None:
        """Empty string produces empty list."""
        assert parse_csv("") == []

    def test_single_value(self) -> None:
        """Single value CSV."""
        assert parse_csv("hello") == [["hello"]]

    def test_single_row(self) -> None:
        """Single row with multiple columns."""
        assert parse_csv("a,b,c") == [["a", "b", "c"]]

    def test_type_error_int(self) -> None:
        """Non-string input raises TypeError."""
        with pytest.raises(TypeError, match="expected str"):
            parse_csv(999)  # type: ignore[arg-type]

    def test_type_error_list(self) -> None:
        """List input raises TypeError."""
        with pytest.raises(TypeError, match="expected str"):
            parse_csv(["a", "b"])  # type: ignore[arg-type]

    def test_quoted_fields(self) -> None:
        """Quoted fields parsed correctly."""
        result = parse_csv('"hello, world",foo')
        assert result == [["hello, world", "foo"]]
