"""Pytest configuration and shared fixtures."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from pathlib import Path


@pytest.fixture
def tmp_text_file(tmp_path: Path) -> Path:
    """Create a temporary text file for testing."""
    p = tmp_path / "test.txt"
    p.write_text("hello world\n")
    return p


@pytest.fixture
def sample_csv(tmp_path: Path) -> Path:
    """Create a temporary CSV file for testing."""
    p = tmp_path / "test.csv"
    p.write_text("name,age\nAlice,30\nBob,25\n")
    return p


@pytest.fixture
def sample_json(tmp_path: Path) -> str:
    """Return a sample JSON string."""
    return '{"name": "Alice", "age": 30}'
