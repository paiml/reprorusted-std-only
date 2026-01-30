"""Tests for dataclasses.basic_example module."""

from __future__ import annotations

import pytest

from reprorusted_std_only.dataclasses.basic_example import Point


class TestPoint:
    """Test suite for Point dataclass."""

    def test_creation(self) -> None:
        """Point can be created with x and y."""
        p = Point(3.0, 4.0)
        assert p.x == 3.0
        assert p.y == 4.0

    def test_frozen(self) -> None:
        """Point is frozen (immutable)."""
        p = Point(1.0, 2.0)
        with pytest.raises(AttributeError):
            p.x = 5.0  # type: ignore[misc]

    def test_distance_basic(self) -> None:
        """Distance from origin to (3, 4) is 5."""
        p1 = Point(0.0, 0.0)
        p2 = Point(3.0, 4.0)
        assert p1.distance(p2) == 5.0

    def test_distance_same_point(self) -> None:
        """Distance between same point is zero."""
        p = Point(1.0, 1.0)
        assert p.distance(p) == 0.0

    def test_distance_symmetry(self) -> None:
        """Distance is symmetric."""
        p1 = Point(1.0, 2.0)
        p2 = Point(4.0, 6.0)
        assert p1.distance(p2) == p2.distance(p1)

    def test_distance_type_error(self) -> None:
        """Non-Point argument raises TypeError."""
        p = Point(0.0, 0.0)
        with pytest.raises(TypeError, match="expected Point"):
            p.distance("not a point")  # type: ignore[arg-type]

    def test_equality(self) -> None:
        """Two Points with same coords are equal."""
        assert Point(1.0, 2.0) == Point(1.0, 2.0)

    def test_inequality(self) -> None:
        """Two Points with different coords are not equal."""
        assert Point(1.0, 2.0) != Point(3.0, 4.0)
