"""Tests for enum.basic_example module."""

from __future__ import annotations

from reprorusted_std_only.enum.basic_example import Color


class TestColor:
    """Test suite for Color enum."""

    def test_red_hex(self) -> None:
        """RED hex is #FF0000."""
        assert Color.RED.hex() == "#FF0000"

    def test_green_hex(self) -> None:
        """GREEN hex is #00FF00."""
        assert Color.GREEN.hex() == "#00FF00"

    def test_blue_hex(self) -> None:
        """BLUE hex is #0000FF."""
        assert Color.BLUE.hex() == "#0000FF"

    def test_values(self) -> None:
        """Enum values are lowercase strings."""
        assert Color.RED.value == "red"
        assert Color.GREEN.value == "green"
        assert Color.BLUE.value == "blue"

    def test_member_count(self) -> None:
        """There are exactly 3 colors."""
        assert len(Color) == 3

    def test_by_value(self) -> None:
        """Can look up color by value."""
        assert Color("red") is Color.RED

    def test_identity(self) -> None:
        """Enum members are singletons."""
        assert Color.RED is Color.RED
