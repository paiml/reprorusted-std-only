#!/usr/bin/env python3
"""Export stdlib corpus to Apache Parquet format.

Usage:
    python -m reprorusted_std_only.export_corpus
    python scripts/export_corpus.py --output data/corpus.parquet
"""

from __future__ import annotations

import ast
import sys
from pathlib import Path

# Note: pyarrow is a dev dependency, not in the corpus source
import pyarrow as pa
import pyarrow.parquet as pq


def extract_functions(source: str) -> list[dict[str, str | int]]:
    """Extract function metadata from Python source.

    Args:
        source: Python source code.

    Returns:
        List of function metadata dicts.
    """
    tree = ast.parse(source)
    functions: list[dict[str, str | int]] = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            sig = ast.get_source_segment(source, node) or ""
            first_line = sig.split("\n")[0] if sig else ""
            functions.append(
                {
                    "name": node.name,
                    "signature": first_line,
                    "docstring": ast.get_docstring(node) or "",
                    "line_number": node.lineno,
                }
            )
    return functions


def build_corpus(src_dir: Path) -> list[dict]:
    """Build corpus from source directory.

    Args:
        src_dir: Path to source package.

    Returns:
        List of module records.
    """
    records: list[dict] = []

    for py_file in sorted(src_dir.rglob("*.py")):
        if py_file.name == "__init__.py":
            continue

        rel_path = py_file.relative_to(src_dir)
        category = rel_path.parts[0] if len(rel_path.parts) > 1 else "root"
        content = py_file.read_text()
        functions = extract_functions(content)

        records.append(
            {
                "module": str(rel_path),
                "category": category,
                "content": content,
                "function_count": len(functions),
                "line_count": len(content.splitlines()),
            }
        )

    return records


def main() -> int:
    """Export corpus to Parquet."""
    src_dir = Path(__file__).parent.parent / "src" / "reprorusted_std_only"
    output_dir = Path(__file__).parent.parent / "data"
    output_dir.mkdir(exist_ok=True)
    output_path = output_dir / "corpus.parquet"

    records = build_corpus(src_dir)
    if not records:
        print("No source files found", file=sys.stderr)
        return 1

    table = pa.Table.from_pylist(records)
    pq.write_table(table, output_path, compression="zstd")

    print(f"Exported {len(records)} modules to {output_path}")
    print(f"Categories: {len({r['category'] for r in records})}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
