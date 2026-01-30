"""String methods using built-in str operations.

Demonstrates common ``str`` methods and their Rust equivalents using
``std::string::String`` and ``std::fmt``.

Rust equivalent:
    fn title_case(s: &str) -> String {
        s.split_whitespace()
            .map(|w| {
                let mut c = w.chars();
                match c.next() {
                    None => String::new(),
                    Some(f) => f.to_uppercase().to_string()
                        + &c.as_str().to_lowercase(),
                }
            })
            .collect::<Vec<_>>()
            .join(" ")
    }

Examples:
    >>> from reprorusted_std_only.string_text.string_methods_example import title_case
    >>> title_case("hello world")
    'Hello World'
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass


def title_case(text: str) -> str:
    """Convert a string to title case.

    Each word's first character is capitalized and the rest lowered.
    Uses ``str.title()`` from the Python stdlib.

    Args:
        text: Input string to convert.

    Returns:
        The title-cased version of the input.

    Raises:
        TypeError: When ``text`` is not a string.

    Examples:
        >>> title_case("the quick brown fox")
        'The Quick Brown Fox'

        >>> title_case("")
        ''

        >>> title_case(42)  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        TypeError: ...
    """
    if not isinstance(text, str):
        msg = f"expected str, got {type(text).__name__}"
        raise TypeError(msg)
    return text.title()
