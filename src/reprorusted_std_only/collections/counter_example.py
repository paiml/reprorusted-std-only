"""Word counting with collections.Counter.

Demonstrates ``collections.Counter`` and its Rust equivalent using
``std::collections::HashMap``.

Rust equivalent:
    fn count_words(text: &str) -> HashMap<String, usize> {
        let mut counts = HashMap::new();
        for word in text.split_whitespace() {
            *counts.entry(word.to_string()).or_insert(0) += 1;
        }
        counts
    }

Examples:
    >>> from reprorusted_std_only.collections.counter_example import count_words
    >>> count_words("hello world hello")
    {'hello': 2, 'world': 1}
"""

from __future__ import annotations

import collections
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass


def count_words(text: str) -> dict[str, int]:
    """Count word frequencies in a text string.

    Splits on whitespace and returns a dictionary mapping each word
    to its occurrence count.

    Args:
        text: Input text to count words from.

    Returns:
        Dictionary mapping words to their frequency counts.

    Raises:
        TypeError: When ``text`` is not a string.

    Examples:
        >>> count_words("the cat sat on the mat")
        {'the': 2, 'cat': 1, 'sat': 1, 'on': 1, 'mat': 1}

        >>> count_words("")
        {}

        >>> count_words(42)  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        TypeError: ...
    """
    if not isinstance(text, str):
        msg = f"expected str, got {type(text).__name__}"
        raise TypeError(msg)
    return dict(collections.Counter(text.split()))
