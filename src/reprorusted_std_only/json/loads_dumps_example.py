"""JSON roundtrip with the json module.

Demonstrates ``json.loads`` and ``json.dumps`` and their Rust equivalents
using ``serde_json``.

Rust equivalent:
    fn json_roundtrip(input: &str) -> String {
        let value: serde_json::Value = serde_json::from_str(input).unwrap();
        serde_json::to_string(&value).unwrap()
    }

Examples:
    >>> from reprorusted_std_only.json.loads_dumps_example import json_roundtrip
    >>> json_roundtrip('{"key": "value"}')
    '{"key": "value"}'
"""

from __future__ import annotations

import json
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass


def json_roundtrip(input_str: str) -> str:
    """Parse a JSON string and re-serialize it.

    Performs a load-then-dump roundtrip to normalize the JSON output
    (sorted keys, no extra whitespace).

    Args:
        input_str: A valid JSON string.

    Returns:
        The re-serialized JSON string with sorted keys.

    Raises:
        json.JSONDecodeError: When ``input_str`` is not valid JSON.

    Examples:
        >>> json_roundtrip('{"b": 2, "a": 1}')
        '{"a": 1, "b": 2}'

        >>> json_roundtrip('[]')
        '[]'

        >>> json_roundtrip('not json')  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        json.decoder.JSONDecodeError: ...
    """
    parsed = json.loads(input_str)
    return json.dumps(parsed, sort_keys=True)
