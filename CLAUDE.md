# reprorusted-std-only - Development Guidelines

## Project Overview

Standard library Python-to-Rust transpilation corpus. Every Python source uses
ONLY CPython 3.11+ stdlib modules. Zero third-party dependencies in corpus code.

## Critical Rules

### Package Management
- **ONLY use `uv`** - No pip, conda, or poetry
- All commands use `uv run` prefix
- Dependencies managed in `pyproject.toml`

### Quality Standards
- **95% minimum test coverage** (branch) - Enforced via pytest
- **Zero ruff violations** - `make lint` must pass
- **Zero ty type errors** - `make typecheck` must pass
- **Zero third-party imports** - `make validate-stdlib` must pass
- **100% docstring coverage** for public APIs
- **Property-based testing** via Hypothesis for all pure functions

### Stdlib-Only Rule
- Every `.py` file under `src/` must use ONLY Python stdlib imports
- `scripts/validate_stdlib_only.py` enforces this via AST scanning
- This runs as Gate 0 in CI, before lint

### Typing Rules
- `from __future__ import annotations` in every `.py` file
- Full type annotations on all function parameters and return types
- Zero `# type: ignore` comments
- Use `TYPE_CHECKING` guard for import-only types
- Prefer `X | None` over `Optional[X]`

### Docstring Rules
- Google style convention
- Every public function has a docstring
- Minimum 3 doctests per function: happy path, edge case, error case
- Use `+IGNORE_EXCEPTION_DETAIL` for error doctests

### TDD Workflow
1. Write failing test (RED)
2. Implement minimum code (GREEN)
3. Refactor while green (REFACTOR)

### Commit Format
```
feat|fix|docs|refactor|test: message (Refs GH-XXX)

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
```

## Commands

```bash
make setup              # Install dependencies
make check              # All 6 gates (stdlib + lint + format + ty + security + coverage)
make validate-stdlib    # Gate 0: stdlib-only validation
make lint               # Ruff linter
make format             # Format check
make typecheck          # ty type checker
make test               # Full test suite with coverage
make test-fast          # Quick unit tests, no coverage
make security           # Bandit security scan
make mutation           # Mutation testing
make export             # Export corpus to Parquet
```

## Module Structure

```python
"""One-line summary.

Demonstrates Python stdlib X and its Rust equivalent.

Rust equivalent:
    fn example() -> i64 { ... }

Examples:
    >>> from reprorusted_std_only.category.module import func
    >>> func(42)
    42
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass


def func(n: int) -> int:
    """One-line summary.

    Args:
        n: Description.

    Returns:
        Description.

    Raises:
        TypeError: When n is invalid.

    Examples:
        >>> func(7)
        7

        >>> func(0)
        0

        >>> func("x")  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        TypeError: ...
    """
    ...
```
