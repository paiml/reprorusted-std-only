#!/usr/bin/env python3
"""Validate that no third-party imports exist in the corpus.

Gate 0 in the Jidoka CI pipeline. Scans every .py file under src/
and rejects any import not in the CPython 3.11 stdlib.

Usage:
    python scripts/validate_stdlib_only.py
"""

from __future__ import annotations

import ast
import sys
from pathlib import Path

STDLIB_MODULES: frozenset[str] = frozenset(sys.stdlib_module_names)

# Also allow the package itself
ALLOWED_FIRST_PARTY: frozenset[str] = frozenset({"reprorusted_std_only"})


def _is_allowed_module(module_name: str) -> bool:
    """Check if a module name is in the stdlib or first-party allowlist."""
    top = module_name.split(".")[0]
    return top in STDLIB_MODULES or top in ALLOWED_FIRST_PARTY


def _check_import_node(node: ast.Import, path: Path) -> list[str]:
    """Check an Import node for violations."""
    violations: list[str] = []
    for alias in node.names:
        if not _is_allowed_module(alias.name):
            violations.append(f"{path}:{node.lineno} imports '{alias.name}'")
    return violations


def _check_import_from_node(node: ast.ImportFrom, path: Path) -> list[str]:
    """Check an ImportFrom node for violations."""
    if node.module and not _is_allowed_module(node.module):
        return [f"{path}:{node.lineno} imports '{node.module}'"]
    return []


def check_file(path: Path) -> list[str]:
    """Return list of non-stdlib top-level imports.

    Args:
        path: Path to Python file to check.

    Returns:
        List of violation descriptions.
    """
    tree = ast.parse(path.read_text())
    violations: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            violations.extend(_check_import_node(node, path))
        elif isinstance(node, ast.ImportFrom):
            violations.extend(_check_import_from_node(node, path))
    return violations


def main() -> int:
    """Scan all source files for non-stdlib imports."""
    src_dir = Path(__file__).parent.parent / "src" / "reprorusted_std_only"
    if not src_dir.exists():
        print(f"Error: {src_dir} not found", file=sys.stderr)
        return 1

    all_violations: list[str] = []
    files_checked = 0

    for py_file in sorted(src_dir.rglob("*.py")):
        files_checked += 1
        violations = check_file(py_file)
        all_violations.extend(violations)

    print(f"Checked {files_checked} files")

    if all_violations:
        print(f"\nFAILED: {len(all_violations)} third-party import(s) found:\n")
        for v in all_violations:
            print(f"  {v}")
        return 1

    print("OK: All imports are stdlib-only")
    return 0


if __name__ == "__main__":
    sys.exit(main())
