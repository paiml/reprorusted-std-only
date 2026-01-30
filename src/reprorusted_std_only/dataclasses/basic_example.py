"""Dataclass definition using the dataclasses module.

Demonstrates ``@dataclass`` and its Rust equivalent using a ``struct``
with ``#[derive]``.

Rust equivalent:
    #[derive(Debug, Clone, PartialEq)]
    struct Point {
        x: f64,
        y: f64,
    }

    impl Point {
        fn distance(&self, other: &Point) -> f64 {
            ((self.x - other.x).powi(2) + (self.y - other.y).powi(2)).sqrt()
        }
    }

Examples:
    >>> from reprorusted_std_only.dataclasses.basic_example import Point
    >>> p = Point(3.0, 4.0)
    >>> p.x
    3.0
"""

from __future__ import annotations

import dataclasses
import math
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass


@dataclasses.dataclass(frozen=True)
class Point:
    """An immutable 2D point.

    Attributes:
        x: The x-coordinate.
        y: The y-coordinate.
    """

    x: float
    y: float

    def distance(self, other: Point) -> float:
        """Compute Euclidean distance to another point.

        Args:
            other: The other point.

        Returns:
            The Euclidean distance between this point and ``other``.

        Raises:
            TypeError: When ``other`` is not a Point.

        Examples:
            >>> Point(0.0, 0.0).distance(Point(3.0, 4.0))
            5.0

            >>> Point(1.0, 1.0).distance(Point(1.0, 1.0))
            0.0

            >>> p = Point(0.0, 0.0)
            >>> p.distance("not a point")  # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            TypeError: ...
        """
        if not isinstance(other, Point):
            msg = f"expected Point, got {type(other).__name__}"
            raise TypeError(msg)
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
