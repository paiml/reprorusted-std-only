"""Enum definition using the enum module.

Demonstrates ``enum.Enum`` and its Rust equivalent.

Rust equivalent:
    #[derive(Debug, Clone, Copy, PartialEq)]
    enum Color {
        Red,
        Green,
        Blue,
    }

    impl Color {
        fn hex(&self) -> &str {
            match self {
                Color::Red => "#FF0000",
                Color::Green => "#00FF00",
                Color::Blue => "#0000FF",
            }
        }
    }

Examples:
    >>> from reprorusted_std_only.enum.basic_example import Color
    >>> Color.RED.hex()
    '#FF0000'
"""

from __future__ import annotations

import enum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass


class Color(enum.Enum):
    """RGB color enumeration.

    Each variant maps to a hex color code string.
    """

    RED = "red"
    GREEN = "green"
    BLUE = "blue"

    def hex(self) -> str:
        """Return the hex color code for this color.

        Returns:
            A hex color code string (e.g. ``#FF0000``).

        Examples:
            >>> Color.GREEN.hex()
            '#00FF00'

            >>> Color.BLUE.hex()
            '#0000FF'

            >>> Color.RED.hex()
            '#FF0000'
        """
        mapping: dict[Color, str] = {
            Color.RED: "#FF0000",
            Color.GREEN: "#00FF00",
            Color.BLUE: "#0000FF",
        }
        return mapping[self]
