"""Tests for scripts/export_corpus.py."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

# Load the script module directly since scripts/ is not a package
_SCRIPT_PATH = Path(__file__).parent.parent.parent / "scripts" / "export_corpus.py"
_spec = importlib.util.spec_from_file_location("export_corpus", _SCRIPT_PATH)
assert _spec is not None and _spec.loader is not None
_mod = importlib.util.module_from_spec(_spec)
sys.modules["export_corpus"] = _mod
_spec.loader.exec_module(_mod)

extract_functions = _mod.extract_functions  # type: ignore[attr-defined]
build_corpus = _mod.build_corpus  # type: ignore[attr-defined]


class TestExtractFunctions:
    """Test suite for extract_functions."""

    def test_single_function(self) -> None:
        """Extracts a single function definition."""
        source = 'def hello():\n    """Say hello."""\n    return "hi"\n'
        funcs = extract_functions(source)
        assert len(funcs) == 1
        assert funcs[0]["name"] == "hello"

    def test_multiple_functions(self) -> None:
        """Extracts multiple function definitions."""
        source = "def a():\n    pass\n\ndef b():\n    pass\n"
        funcs = extract_functions(source)
        assert len(funcs) == 2
        names = [f["name"] for f in funcs]
        assert "a" in names
        assert "b" in names

    def test_no_functions(self) -> None:
        """Empty source returns empty list."""
        assert extract_functions("x = 1\n") == []

    def test_function_with_docstring(self) -> None:
        """Docstring is extracted."""
        source = 'def greet():\n    """Greet someone."""\n    pass\n'
        funcs = extract_functions(source)
        assert funcs[0]["docstring"] == "Greet someone."

    def test_function_line_number(self) -> None:
        """Line number is captured."""
        source = "# comment\ndef foo():\n    pass\n"
        funcs = extract_functions(source)
        assert funcs[0]["line_number"] == 2

    def test_empty_source(self) -> None:
        """Empty string returns empty list."""
        assert extract_functions("") == []


class TestBuildCorpus:
    """Test suite for build_corpus."""

    def test_build_from_src(self) -> None:
        """Build corpus from actual source directory."""
        src_dir = Path(__file__).parent.parent.parent / "src" / "reprorusted_std_only"
        records = build_corpus(src_dir)
        assert len(records) > 0
        # Each record has expected keys
        for rec in records:
            assert "module" in rec
            assert "category" in rec
            assert "content" in rec
            assert "function_count" in rec
            assert "line_count" in rec

    def test_skips_init_files(self) -> None:
        """Init files are skipped."""
        src_dir = Path(__file__).parent.parent.parent / "src" / "reprorusted_std_only"
        records = build_corpus(src_dir)
        modules = [r["module"] for r in records]
        assert all("__init__" not in m for m in modules)

    def test_empty_dir(self, tmp_path: Path) -> None:
        """Empty directory returns empty list."""
        assert build_corpus(tmp_path) == []

    def test_categories_extracted(self) -> None:
        """Categories are extracted from directory structure."""
        src_dir = Path(__file__).parent.parent.parent / "src" / "reprorusted_std_only"
        records = build_corpus(src_dir)
        categories = {r["category"] for r in records}
        assert "builtins" in categories
        assert "collections" in categories
