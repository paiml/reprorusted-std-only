"""Tests for itertools.chain_example module."""

from __future__ import annotations

import pytest

from reprorusted_std_only.itertools.chain_example import chain_lists


class TestChainLists:
    """Test suite for chain_lists function."""

    def test_basic_chain(self) -> None:
        """Two non-empty lists are concatenated."""
        assert chain_lists([1, 2], [3, 4]) == [1, 2, 3, 4]

    def test_empty_lists(self) -> None:
        """Two empty lists produce empty result."""
        assert chain_lists([], []) == []

    def test_first_empty(self) -> None:
        """First list empty, second returned."""
        assert chain_lists([], [5, 6]) == [5, 6]

    def test_second_empty(self) -> None:
        """Second list empty, first returned."""
        assert chain_lists([7, 8], []) == [7, 8]

    def test_single_element_lists(self) -> None:
        """Single element lists chained correctly."""
        assert chain_lists([1], [2]) == [1, 2]

    def test_type_error_string_first(self) -> None:
        """Non-list first arg raises TypeError."""
        with pytest.raises(TypeError, match="must be lists"):
            chain_lists("ab", [1])  # type: ignore[arg-type]

    def test_type_error_string_second(self) -> None:
        """Non-list second arg raises TypeError."""
        with pytest.raises(TypeError, match="must be lists"):
            chain_lists([1], "ab")  # type: ignore[arg-type]

    def test_type_error_both(self) -> None:
        """Neither arg is a list raises TypeError."""
        with pytest.raises(TypeError, match="must be lists"):
            chain_lists("a", "b")  # type: ignore[arg-type]

    def test_preserves_order(self) -> None:
        """Order of elements is preserved across chain."""
        assert chain_lists([3, 1], [4, 2]) == [3, 1, 4, 2]
