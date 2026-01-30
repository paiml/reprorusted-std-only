"""Tests for io_files.stringio_example module."""

from __future__ import annotations

import pytest

from reprorusted_std_only.io_files.stringio_example import write_and_read


class TestWriteAndRead:
    """Test suite for write_and_read function."""

    def test_basic(self) -> None:
        """Lines are joined with newlines."""
        result = write_and_read(["hello", "world"])
        assert result == "hello\nworld\n"

    def test_empty_list(self) -> None:
        """Empty list returns empty string."""
        assert write_and_read([]) == ""

    def test_single_line(self) -> None:
        """Single line gets trailing newline."""
        assert write_and_read(["only"]) == "only\n"

    def test_three_lines(self) -> None:
        """Three lines correctly joined."""
        result = write_and_read(["alpha", "beta", "gamma"])
        assert result == "alpha\nbeta\ngamma\n"

    def test_empty_string_elements(self) -> None:
        """Empty strings produce just newlines."""
        result = write_and_read(["", ""])
        assert result == "\n\n"

    def test_type_error_int_elements(self) -> None:
        """Non-string elements raise TypeError."""
        with pytest.raises(TypeError, match="expected str"):
            write_and_read([1, 2])  # type: ignore[list-item]

    def test_type_error_mixed(self) -> None:
        """Mixed types raise TypeError on first non-string."""
        with pytest.raises(TypeError, match="expected str"):
            write_and_read(["ok", 42])  # type: ignore[list-item]

    def test_tuple_input(self) -> None:
        """Tuple input also works (Sequence protocol)."""
        result = write_and_read(("a", "b"))
        assert result == "a\nb\n"
