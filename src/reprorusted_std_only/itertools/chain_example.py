"""Chaining multiple iterables with itertools.chain.

Demonstrates ``itertools.chain`` and its Rust equivalent using
``Iterator::chain``.

Rust equivalent:
    fn chain_lists(a: Vec<i64>, b: Vec<i64>) -> Vec<i64> {
        a.into_iter().chain(b.into_iter()).collect()
    }

Examples:
    >>> from reprorusted_std_only.itertools.chain_example import chain_lists
    >>> chain_lists([1, 2], [3, 4])
    [1, 2, 3, 4]
"""

from __future__ import annotations

import itertools
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass


def chain_lists(a: list[int], b: list[int]) -> list[int]:
    """Chain two integer lists into a single list.

    Concatenates elements of ``a`` followed by elements of ``b``
    using ``itertools.chain``.

    Args:
        a: First list of integers.
        b: Second list of integers.

    Returns:
        A new list containing all elements from ``a`` then ``b``.

    Raises:
        TypeError: When either argument is not a list.

    Examples:
        >>> chain_lists([10, 20], [30])
        [10, 20, 30]

        >>> chain_lists([], [])
        []

        >>> chain_lists("ab", [1])  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        TypeError: ...
    """
    if not isinstance(a, list) or not isinstance(b, list):
        msg = "both arguments must be lists"
        raise TypeError(msg)
    return list(itertools.chain(a, b))
