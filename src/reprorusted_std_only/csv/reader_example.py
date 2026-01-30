r"""CSV parsing with the csv module.

Demonstrates ``csv.reader`` and its Rust equivalent using the ``csv`` crate.

Rust equivalent:
    fn parse_csv(input: &str) -> Vec<Vec<String>> {
        let mut rdr = csv::ReaderBuilder::new()
            .has_headers(false)
            .from_reader(input.as_bytes());
        rdr.records()
            .map(|r| r.unwrap().iter().map(String::from).collect())
            .collect()
    }

Examples:
    >>> from reprorusted_std_only.csv.reader_example import parse_csv
    >>> parse_csv("a,b\\n1,2")
    [['a', 'b'], ['1', '2']]
"""

from __future__ import annotations

import csv
import io
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass


def parse_csv(text: str) -> list[list[str]]:
    r"""Parse a CSV-formatted string into a list of rows.

    Each row is a list of string fields. Uses the default CSV dialect.

    Args:
        text: A CSV-formatted string.

    Returns:
        List of rows, where each row is a list of field strings.

    Raises:
        TypeError: When ``text`` is not a string.

    Examples:
        >>> parse_csv("name,age\\nAlice,30\\nBob,25")
        [['name', 'age'], ['Alice', '30'], ['Bob', '25']]

        >>> parse_csv("")
        []

        >>> parse_csv(999)  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        TypeError: ...
    """
    if not isinstance(text, str):
        msg = f"expected str, got {type(text).__name__}"
        raise TypeError(msg)
    reader = csv.reader(io.StringIO(text))
    return list(reader)
