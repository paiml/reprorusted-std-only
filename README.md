# reprorusted-std-only

[![CI](https://github.com/paiml/reprorusted-std-only/actions/workflows/ci.yml/badge.svg)](https://github.com/paiml/reprorusted-std-only/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen.svg)](https://github.com/paiml/reprorusted-std-only)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Ruff](https://img.shields.io/badge/linter-ruff-purple.svg)](https://github.com/astral-sh/ruff)
[![uv](https://img.shields.io/badge/package-uv-orange.svg)](https://github.com/astral-sh/uv)

**Zero-dependency, stdlib-only Python-to-Rust transpilation corpus** for the
[depyler](https://github.com/paiml/depyler) transpiler.

## Key Constraint

**Zero third-party dependencies.** Every Python source file uses exclusively
the CPython 3.11+ standard library. This is enforced by AST scanning in CI
(Gate 0).

## Installation

```bash
# Clone the repository
git clone https://github.com/paiml/reprorusted-std-only.git
cd reprorusted-std-only

# Install uv if not already installed
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
make setup
```

## Usage

```bash
# Run all quality gates (6-gate Jidoka pipeline)
make check

# Run tests with coverage
make test

# Export corpus to Parquet format
make export

# Validate stdlib-only constraint
uv run python scripts/validate_stdlib_only.py
```

## Demo

```bash
# Clone and setup
git clone https://github.com/paiml/reprorusted-std-only.git
cd reprorusted-std-only
make setup

# Run all 6-gate Jidoka quality pipeline
make check

# Example: Run a specific module
python -c "from reprorusted_std_only.collections import most_common; print(most_common(['a','b','a','c','a'], 2))"
# Output: [('a', 3), ('b', 1)]

# Export corpus to Parquet for HuggingFace
make export
```

## Architecture

```
reprorusted-std-only/
├── src/reprorusted_std_only/
│   ├── builtins/          # abs, len, min, max, sum, sorted, ...
│   ├── collections/       # Counter, defaultdict, deque, ...
│   ├── itertools/         # chain, groupby, permutations, ...
│   ├── functools/         # reduce, partial, lru_cache, ...
│   ├── pathlib/           # Path operations
│   ├── re/                # Regex matching
│   ├── json/              # JSON encode/decode
│   ├── csv/               # CSV parsing
│   ├── math_stats/        # Math and statistics
│   ├── dataclasses/       # Struct-like data classes
│   ├── typing/            # Generics and type hints
│   ├── enum/              # Enumerations
│   ├── argparse/          # CLI argument parsing
│   ├── datetime/          # Date/time operations
│   ├── hashlib_secrets/   # Cryptographic hashing
│   ├── io_files/          # File I/O, StringIO
│   ├── concurrency/       # Threading, asyncio
│   ├── contextlib/        # Context managers
│   ├── struct_binary/     # Binary pack/unpack
│   └── string_text/       # String manipulation
├── scripts/
│   ├── validate_stdlib_only.py  # Gate 0: AST scanner
│   └── export_corpus.py         # Parquet exporter
└── tests/
    └── unit/              # 182 tests, 100% coverage
```

## Quality Standards

| Gate | Tool | Requirement |
|------|------|-------------|
| 0 | AST scanner | Zero third-party imports |
| 1 | ruff check | Zero lint violations |
| 2 | ruff format | Consistent formatting |
| 3 | ty | Zero type errors |
| 4 | bandit | Zero security findings |
| 5 | pytest | 95%+ branch coverage |

Additional standards:
- Google-style docstrings with 3+ doctests per function
- Property-based testing via Hypothesis
- Mutation testing via mutmut (85%+ mutation score)

## Categories (20 stdlib domains)

| Category | Stdlib modules | Rust mapping |
|----------|---------------|--------------|
| `builtins` | built-in functions | `std` primitives |
| `collections` | `collections` | `std::collections` |
| `itertools` | `itertools` | `itertools` / `std::iter` |
| `functools` | `functools` | closures, `memoize` |
| `pathlib` | `pathlib` | `std::path` |
| `re` | `re` | `regex` crate |
| `json` | `json` | `serde_json` |
| `csv` | `csv` | `csv` crate |
| `math_stats` | `math`, `statistics` | `std::f64`, `statrs` |
| `dataclasses` | `dataclasses` | `struct` + `derive` |
| `typing` | `typing` | generics, traits |
| `enum` | `enum` | `enum` |
| `argparse` | `argparse` | `clap` |
| `datetime` | `datetime` | `chrono` |
| `hashlib_secrets` | `hashlib`, `secrets` | `sha2`, `rand` |
| `io_files` | `io`, `tempfile`, `shutil` | `std::io`, `tempfile` |
| `concurrency` | `threading`, `asyncio` | `std::thread`, `tokio` |
| `contextlib` | `contextlib` | RAII / `Drop` |
| `struct_binary` | `struct` | `byteorder`, `bincode` |
| `string_text` | `string`, `textwrap` | `std::fmt`, `textwrap` |

## Quick Start

```bash
# Install dependencies (requires uv)
make setup

# Run all quality gates
make check

# Run tests only
make test

# Check coverage
make coverage

# Export to Parquet
make export

# Generate documentation
make docs
```

## CI Pipeline

The 6-gate Jidoka pipeline runs on every push:

1. **Gate 0**: Stdlib-only validation (AST scan)
2. **Gate 1**: Lint (ruff check)
3. **Gate 2**: Format (ruff format --check)
4. **Gate 3**: Type check (ty)
5. **Gate 4**: Security (bandit)
6. **Gate 5**: Tests + Coverage (pytest, 95% threshold)

Matrix: Ubuntu + macOS × Python 3.11 + 3.12

## Contributing

1. Fork the repository
2. Create a feature branch
3. Ensure all quality gates pass: `make check`
4. Submit a pull request

## License

Apache-2.0
