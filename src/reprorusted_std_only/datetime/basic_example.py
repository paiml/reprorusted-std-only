"""Date operations using the datetime module.

Demonstrates ``datetime.date`` and its Rust equivalent using the ``chrono``
crate.

Rust equivalent:
    use chrono::NaiveDate;

    fn days_between(date1: &str, date2: &str) -> i64 {
        let d1 = NaiveDate::parse_from_str(date1, "%Y-%m-%d").unwrap();
        let d2 = NaiveDate::parse_from_str(date2, "%Y-%m-%d").unwrap();
        (d2 - d1).num_days().abs()
    }

Examples:
    >>> from reprorusted_std_only.datetime.basic_example import days_between
    >>> days_between("2024-01-01", "2024-01-31")
    30
"""

from __future__ import annotations

import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass


def days_between(date1: str, date2: str) -> int:
    """Compute the absolute number of days between two ISO-format dates.

    Args:
        date1: First date in ``YYYY-MM-DD`` format.
        date2: Second date in ``YYYY-MM-DD`` format.

    Returns:
        The absolute number of days between the two dates.

    Raises:
        ValueError: When a date string is not in valid ISO format.

    Examples:
        >>> days_between("2024-03-01", "2024-03-15")
        14

        >>> days_between("2024-01-01", "2024-01-01")
        0

        >>> days_between(  # doctest: +IGNORE_EXCEPTION_DETAIL
        ...     "not-a-date", "2024-01-01"
        ... )
        Traceback (most recent call last):
        ValueError: ...
    """
    d1 = datetime.date.fromisoformat(date1)
    d2 = datetime.date.fromisoformat(date2)
    return abs((d2 - d1).days)
