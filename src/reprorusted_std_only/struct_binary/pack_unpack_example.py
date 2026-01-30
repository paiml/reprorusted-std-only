r"""Struct pack and unpack using the struct module.

Demonstrates ``struct.pack`` / ``struct.unpack`` and their Rust equivalents
using ``byteorder`` or ``bincode``.

Rust equivalent:
    use byteorder::{BigEndian, WriteBytesExt, ReadBytesExt};
    use std::io::Cursor;

    fn pack_two_u16(a: u16, b: u16) -> Vec<u8> {
        let mut buf = Vec::new();
        buf.write_u16::<BigEndian>(a).unwrap();
        buf.write_u16::<BigEndian>(b).unwrap();
        buf
    }

    fn unpack_two_u16(data: &[u8]) -> (u16, u16) {
        let mut cursor = Cursor::new(data);
        let a = cursor.read_u16::<BigEndian>().unwrap();
        let b = cursor.read_u16::<BigEndian>().unwrap();
        (a, b)
    }

Examples:
    >>> from reprorusted_std_only.struct_binary.pack_unpack_example import pack_two_u16
    >>> pack_two_u16(1, 2)
    b'\\x00\\x01\\x00\\x02'
"""

from __future__ import annotations

import struct
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass


def pack_two_u16(a: int, b: int) -> bytes:
    r"""Pack two unsigned 16-bit integers into big-endian bytes.

    Args:
        a: First unsigned 16-bit integer (0-65535).
        b: Second unsigned 16-bit integer (0-65535).

    Returns:
        A 4-byte big-endian representation.

    Raises:
        struct.error: When values are out of range for unsigned 16-bit.

    Examples:
        >>> pack_two_u16(256, 512)
        b'\\x01\\x00\\x02\\x00'

        >>> pack_two_u16(0, 0)
        b'\\x00\\x00\\x00\\x00'

        >>> pack_two_u16(70000, 0)  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        struct.error: ...
    """
    return struct.pack(">HH", a, b)


def unpack_two_u16(data: bytes) -> tuple[int, int]:
    r"""Unpack two unsigned 16-bit integers from big-endian bytes.

    Args:
        data: Exactly 4 bytes of big-endian data.

    Returns:
        A tuple of two integers.

    Raises:
        struct.error: When ``data`` is not exactly 4 bytes.

    Examples:
        >>> unpack_two_u16(b'\\x00\\x01\\x00\\x02')
        (1, 2)

        >>> unpack_two_u16(b'\\x00\\x00\\x00\\x00')
        (0, 0)

        >>> unpack_two_u16(b'\\x00')  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        struct.error: ...
    """
    return struct.unpack(">HH", data)
