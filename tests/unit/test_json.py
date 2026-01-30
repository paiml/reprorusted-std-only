"""Tests for json.loads_dumps_example module."""

from __future__ import annotations

import json

import pytest

from reprorusted_std_only.json.loads_dumps_example import json_roundtrip


class TestJsonRoundtrip:
    """Test suite for json_roundtrip function."""

    def test_basic_object(self) -> None:
        """Simple object roundtrips correctly."""
        result = json_roundtrip('{"key": "value"}')
        assert result == '{"key": "value"}'

    def test_sorted_keys(self) -> None:
        """Keys are sorted in output."""
        result = json_roundtrip('{"b": 2, "a": 1}')
        assert result == '{"a": 1, "b": 2}'

    def test_empty_array(self) -> None:
        """Empty array roundtrips correctly."""
        assert json_roundtrip("[]") == "[]"

    def test_empty_object(self) -> None:
        """Empty object roundtrips correctly."""
        assert json_roundtrip("{}") == "{}"

    def test_nested_object(self) -> None:
        """Nested object roundtrips correctly."""
        result = json_roundtrip('{"a": {"b": 1}}')
        parsed = json.loads(result)
        assert parsed == {"a": {"b": 1}}

    def test_number_value(self) -> None:
        """Number values preserved."""
        result = json_roundtrip('{"x": 42}')
        assert result == '{"x": 42}'

    def test_invalid_json_raises(self) -> None:
        """Invalid JSON raises JSONDecodeError."""
        with pytest.raises(json.JSONDecodeError):
            json_roundtrip("not json")

    def test_array_of_values(self) -> None:
        """Array of values roundtrips."""
        result = json_roundtrip("[1, 2, 3]")
        assert result == "[1, 2, 3]"
