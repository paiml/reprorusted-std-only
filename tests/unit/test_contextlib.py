"""Tests for contextlib.contextmanager_example module."""

from __future__ import annotations

from reprorusted_std_only.contextlib.contextmanager_example import collect_items


class TestCollectItems:
    """Test suite for collect_items context manager."""

    def test_basic_collection(self) -> None:
        """Items appended in context are available after."""
        with collect_items() as items:
            items.append("a")
            items.append("b")
        assert items == ["a", "b"]

    def test_empty_context(self) -> None:
        """No items appended yields empty list."""
        with collect_items() as items:
            pass
        assert items == []

    def test_extend(self) -> None:
        """Extending items works in context."""
        with collect_items() as items:
            items.extend(["x", "y", "z"])
        assert items == ["x", "y", "z"]

    def test_single_item(self) -> None:
        """Single item collection."""
        with collect_items() as items:
            items.append("only")
        assert items == ["only"]

    def test_len_after_context(self) -> None:
        """Length is correct after context exit."""
        with collect_items() as items:
            items.extend(["1", "2", "3"])
        assert len(items) == 3

    def test_separate_contexts_independent(self) -> None:
        """Each context creates a new list."""
        with collect_items() as items1:
            items1.append("first")
        with collect_items() as items2:
            items2.append("second")
        assert items1 == ["first"]
        assert items2 == ["second"]
