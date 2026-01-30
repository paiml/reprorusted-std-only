"""Tests for struct_binary.pack_unpack_example module."""

from __future__ import annotations

import struct

import pytest

from reprorusted_std_only.struct_binary.pack_unpack_example import (
    pack_two_u16,
    unpack_two_u16,
)


class TestPackTwoU16:
    """Test suite for pack_two_u16 function."""

    def test_basic_pack(self) -> None:
        """Basic packing produces correct bytes."""
        result = pack_two_u16(1, 2)
        assert result == b"\x00\x01\x00\x02"

    def test_zeros(self) -> None:
        """Zeros pack to all-zero bytes."""
        assert pack_two_u16(0, 0) == b"\x00\x00\x00\x00"

    def test_max_u16(self) -> None:
        """Maximum u16 value packs correctly."""
        result = pack_two_u16(65535, 65535)
        assert result == b"\xff\xff\xff\xff"

    def test_length(self) -> None:
        """Output is always 4 bytes."""
        assert len(pack_two_u16(100, 200)) == 4

    def test_out_of_range_raises(self) -> None:
        """Value exceeding u16 range raises struct.error."""
        with pytest.raises(struct.error):
            pack_two_u16(70000, 0)

    def test_pack_256_512(self) -> None:
        """Pack 256 and 512."""
        result = pack_two_u16(256, 512)
        assert result == b"\x01\x00\x02\x00"


class TestUnpackTwoU16:
    """Test suite for unpack_two_u16 function."""

    def test_basic_unpack(self) -> None:
        """Basic unpacking returns correct tuple."""
        assert unpack_two_u16(b"\x00\x01\x00\x02") == (1, 2)

    def test_zeros(self) -> None:
        """All-zero bytes unpack to (0, 0)."""
        assert unpack_two_u16(b"\x00\x00\x00\x00") == (0, 0)

    def test_max_values(self) -> None:
        """Max value bytes unpack correctly."""
        assert unpack_two_u16(b"\xff\xff\xff\xff") == (65535, 65535)

    def test_wrong_length_raises(self) -> None:
        """Wrong byte length raises struct.error."""
        with pytest.raises(struct.error):
            unpack_two_u16(b"\x00")

    def test_roundtrip(self) -> None:
        """Pack then unpack returns original values."""
        assert unpack_two_u16(pack_two_u16(42, 99)) == (42, 99)
