"""Generic type usage with the typing module.

Demonstrates generic container functions and their Rust equivalents
using generics and trait bounds.

Rust equivalent:
    fn first_or_default<T: Default + Clone>(items: &[T]) -> T {
        items.first().cloned().unwrap_or_default()
    }

Examples:
    >>> from reprorusted_std_only.typing.generics_example import first_or_default
    >>> first_or_default([10, 20, 30])
    10
"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

if TYPE_CHECKING:
    from collections.abc import Sequence

T = TypeVar("T")


def first_or_default(items: Sequence[T], default: T) -> T:
    """Return the first element of a sequence, or a default value.

    Args:
        items: The sequence to inspect.
        default: Value returned when the sequence is empty.

    Returns:
        The first element if the sequence is non-empty, otherwise ``default``.

    Examples:
        >>> first_or_default([1, 2, 3], 0)
        1

        >>> first_or_default([], 42)
        42

        >>> first_or_default(["a", "b"], "z")
        'a'
    """
    if len(items) == 0:
        return default
    return items[0]
