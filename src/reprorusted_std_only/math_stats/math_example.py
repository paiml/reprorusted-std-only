"""Math operations using the math module.

Demonstrates ``math.gcd`` and its Rust equivalent.

Rust equivalent:
    fn gcd(a: u64, b: u64) -> u64 {
        if b == 0 { a } else { gcd(b, a % b) }
    }

Examples:
    >>> from reprorusted_std_only.math_stats.math_example import greatest_common_divisor
    >>> greatest_common_divisor(12, 8)
    4
"""

from __future__ import annotations

import math
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass


def greatest_common_divisor(a: int, b: int) -> int:
    """Compute the greatest common divisor of two non-negative integers.

    Uses ``math.gcd`` which implements the Euclidean algorithm.

    Args:
        a: First non-negative integer.
        b: Second non-negative integer.

    Returns:
        The greatest common divisor of ``a`` and ``b``.

    Raises:
        ValueError: When either argument is negative.

    Examples:
        >>> greatest_common_divisor(54, 24)
        6

        >>> greatest_common_divisor(0, 5)
        5

        >>> greatest_common_divisor(-1, 5)  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        ValueError: ...
    """
    if a < 0 or b < 0:
        msg = "arguments must be non-negative"
        raise ValueError(msg)
    return math.gcd(a, b)
