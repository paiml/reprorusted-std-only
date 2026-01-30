"""Reducing a sequence with functools.reduce.

Demonstrates ``functools.reduce`` and its Rust equivalent using
``Iterator::fold``.

Rust equivalent:
    fn product(values: &[i64]) -> i64 {
        values.iter().fold(1, |acc, &x| acc * x)
    }

Examples:
    >>> from reprorusted_std_only.functools.reduce_example import product
    >>> product([2, 3, 4])
    24
"""

from __future__ import annotations

import functools
import operator
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Sequence


def product(values: Sequence[int]) -> int:
    """Compute the product of a sequence of integers.

    Uses ``functools.reduce`` with ``operator.mul`` to multiply
    all elements together.

    Args:
        values: Sequence of integers to multiply.

    Returns:
        The product of all elements. Returns 1 for an empty sequence.

    Raises:
        TypeError: When ``values`` contains non-integer elements.

    Examples:
        >>> product([1, 2, 3, 4, 5])
        120

        >>> product([])
        1

        >>> product([7])
        7
    """
    return functools.reduce(operator.mul, values, 1)
