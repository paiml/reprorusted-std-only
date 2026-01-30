r"""StringIO operations using the io module.

Demonstrates ``io.StringIO`` and its Rust equivalent using
``std::io::Cursor<String>``.

Rust equivalent:
    use std::io::{Cursor, Write, Read};

    fn write_and_read(lines: &[&str]) -> String {
        let mut buf = Cursor::new(Vec::new());
        for line in lines {
            writeln!(buf, "{}", line).unwrap();
        }
        let data = buf.into_inner();
        String::from_utf8(data).unwrap()
    }

Examples:
    >>> from reprorusted_std_only.io_files.stringio_example import write_and_read
    >>> write_and_read(["hello", "world"])
    'hello\\nworld\\n'
"""

from __future__ import annotations

import io
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Sequence


def write_and_read(lines: Sequence[str]) -> str:
    r"""Write lines to an in-memory StringIO buffer and read them back.

    Each line is written followed by a newline character.

    Args:
        lines: Sequence of strings to write.

    Returns:
        The full contents of the buffer as a single string.

    Raises:
        TypeError: When ``lines`` contains a non-string element.

    Examples:
        >>> write_and_read(["alpha", "beta", "gamma"])
        'alpha\\nbeta\\ngamma\\n'

        >>> write_and_read([])
        ''

        >>> write_and_read([1, 2])  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        TypeError: ...
    """
    buf = io.StringIO()
    for line in lines:
        if not isinstance(line, str):
            msg = f"expected str elements, got {type(line).__name__}"
            raise TypeError(msg)
        buf.write(line)
        buf.write("\n")
    return buf.getvalue()
