"""Tests for pathlib.path_ops_example module."""

from __future__ import annotations

import pytest

from reprorusted_std_only.pathlib.path_ops_example import file_extension


class TestFileExtension:
    """Test suite for file_extension function."""

    def test_txt_extension(self) -> None:
        """Extracts .txt extension."""
        assert file_extension("/home/user/doc.txt") == "txt"

    def test_tar_gz(self) -> None:
        """For .tar.gz returns gz (last suffix)."""
        assert file_extension("archive.tar.gz") == "gz"

    def test_no_extension(self) -> None:
        """No extension returns None."""
        assert file_extension("no_extension") is None

    def test_dotfile(self) -> None:
        """Dotfile with no extension returns None."""
        assert file_extension(".hidden") is None

    def test_py_extension(self) -> None:
        """Extracts .py extension."""
        assert file_extension("script.py") == "py"

    def test_full_path(self) -> None:
        """Works with full path."""
        assert file_extension("/usr/local/bin/app.sh") == "sh"

    def test_type_error_int(self) -> None:
        """Non-string input raises TypeError."""
        with pytest.raises(TypeError, match="expected str"):
            file_extension(123)  # type: ignore[arg-type]

    def test_type_error_none(self) -> None:
        """None input raises TypeError."""
        with pytest.raises(TypeError, match="expected str"):
            file_extension(None)  # type: ignore[arg-type]

    def test_empty_string(self) -> None:
        """Empty string returns None."""
        assert file_extension("") is None
