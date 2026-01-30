r"""Regex matching with the re module.

Demonstrates ``re.match`` and its Rust equivalent using the ``regex`` crate.

Rust equivalent:
    fn is_valid_email(email: &str) -> bool {
        let pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$";
        let re = Regex::new(pattern).unwrap();
        re.is_match(email)
    }

Examples:
    >>> from reprorusted_std_only.re.match_example import is_valid_email
    >>> is_valid_email("user@example.com")
    True
"""

from __future__ import annotations

import re
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass

_EMAIL_PATTERN: re.Pattern[str] = re.compile(
    r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
)


def is_valid_email(email: str) -> bool:
    """Check whether a string is a valid email address.

    Uses a simple regex pattern to validate the email format.
    This is not RFC 5322 compliant but covers common cases.

    Args:
        email: The string to validate.

    Returns:
        ``True`` if the string matches the email pattern, ``False`` otherwise.

    Raises:
        TypeError: When ``email`` is not a string.

    Examples:
        >>> is_valid_email("alice@example.com")
        True

        >>> is_valid_email("not-an-email")
        False

        >>> is_valid_email(42)  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        TypeError: ...
    """
    if not isinstance(email, str):
        msg = f"expected str, got {type(email).__name__}"
        raise TypeError(msg)
    return _EMAIL_PATTERN.match(email) is not None
