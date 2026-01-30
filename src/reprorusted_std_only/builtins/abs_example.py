"""Absolute value computation using Python builtins.

Demonstrates the built-in ``abs()`` function and its Rust equivalent.

Rust equivalent:
    fn absolute_value(n: i64) -> i64 {
        n.abs()
    }

Examples:
    >>> from reprorusted_std_only.builtins.abs_example import absolute_value
    >>> absolute_value(-5)
    5
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass


def absolute_value(n: int) -> int:
    """Return the absolute value of an integer.

    Args:
        n: The integer whose absolute value is computed.

    Returns:
        The non-negative absolute value of ``n``.

    Raises:
        TypeError: When ``n`` is not an integer.

    Examples:
        >>> absolute_value(-42)
        42

        >>> absolute_value(0)
        0

        >>> absolute_value("x")  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        TypeError: ...
    """
    if not isinstance(n, int):
        msg = f"expected int, got {type(n).__name__}"
        raise TypeError(msg)
    return abs(n)
