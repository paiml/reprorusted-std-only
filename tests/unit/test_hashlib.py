"""Tests for hashlib_secrets.hash_example module."""

from __future__ import annotations

import pytest

from reprorusted_std_only.hashlib_secrets.hash_example import sha256_hex


class TestSha256Hex:
    """Test suite for sha256_hex function."""

    def test_hello(self) -> None:
        """SHA-256 of 'hello' matches known hash."""
        expected = "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
        assert sha256_hex("hello") == expected

    def test_empty_string(self) -> None:
        """SHA-256 of empty string matches known hash."""
        expected = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
        assert sha256_hex("") == expected

    def test_world(self) -> None:
        """SHA-256 of 'world' matches known hash."""
        expected = "486ea46224d1bb4fb680f34f7c9ad96a8f24ec88be73ea8e5a6c65260e9cb8a7"
        assert sha256_hex("world") == expected

    def test_deterministic(self) -> None:
        """Same input always produces same output."""
        assert sha256_hex("test") == sha256_hex("test")

    def test_different_inputs(self) -> None:
        """Different inputs produce different hashes."""
        assert sha256_hex("a") != sha256_hex("b")

    def test_length(self) -> None:
        """SHA-256 hex digest is always 64 characters."""
        assert len(sha256_hex("anything")) == 64

    def test_type_error_int(self) -> None:
        """Integer input raises TypeError."""
        with pytest.raises(TypeError, match="expected str"):
            sha256_hex(123)  # type: ignore[arg-type]

    def test_type_error_bytes(self) -> None:
        """Bytes input raises TypeError."""
        with pytest.raises(TypeError, match="expected str"):
            sha256_hex(b"hello")  # type: ignore[arg-type]
