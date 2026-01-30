"""Tests for scripts/validate_stdlib_only.py."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from unittest import mock

# Load the script module directly since scripts/ is not a package
_SCRIPT_PATH = (
    Path(__file__).parent.parent.parent / "scripts" / "validate_stdlib_only.py"
)
_spec = importlib.util.spec_from_file_location("validate_stdlib_only", _SCRIPT_PATH)
assert _spec is not None and _spec.loader is not None
_mod = importlib.util.module_from_spec(_spec)
sys.modules["validate_stdlib_only"] = _mod
_spec.loader.exec_module(_mod)

check_file = _mod.check_file  # type: ignore[attr-defined]
main = _mod.main  # type: ignore[attr-defined]


class TestCheckFile:
    """Test suite for check_file function."""

    def test_stdlib_only_no_violations(self, tmp_path: Path) -> None:
        """File with only stdlib imports has no violations."""
        p = tmp_path / "clean.py"
        p.write_text("import os\nimport sys\nfrom pathlib import Path\n")
        assert check_file(p) == []

    def test_third_party_import(self, tmp_path: Path) -> None:
        """Third-party import is flagged."""
        p = tmp_path / "dirty.py"
        p.write_text("import numpy\n")
        violations = check_file(p)
        assert len(violations) == 1
        assert "numpy" in violations[0]

    def test_third_party_from_import(self, tmp_path: Path) -> None:
        """Third-party from-import is flagged."""
        p = tmp_path / "dirty2.py"
        p.write_text("from pandas import DataFrame\n")
        violations = check_file(p)
        assert len(violations) == 1
        assert "pandas" in violations[0]

    def test_first_party_allowed(self, tmp_path: Path) -> None:
        """First-party package import is allowed."""
        p = tmp_path / "first.py"
        p.write_text("from reprorusted_std_only.builtins import abs_example\n")
        assert check_file(p) == []

    def test_empty_file(self, tmp_path: Path) -> None:
        """Empty file has no violations."""
        p = tmp_path / "empty.py"
        p.write_text("")
        assert check_file(p) == []

    def test_multiple_violations(self, tmp_path: Path) -> None:
        """Multiple third-party imports all flagged."""
        p = tmp_path / "multi.py"
        p.write_text("import requests\nimport flask\n")
        violations = check_file(p)
        assert len(violations) == 2


class TestMain:
    """Test suite for main function."""

    def test_main_success(self) -> None:
        """Main returns 0 when all files are clean."""
        result = main()
        assert result == 0

    def test_main_missing_dir(self) -> None:
        """Main returns 1 when src dir is missing."""
        with mock.patch.object(Path, "exists", return_value=False):
            result = main()
            assert result == 1
