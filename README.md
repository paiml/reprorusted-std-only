# reprorusted-std-only

Standard library Python-to-Rust transpilation corpus for the
[depyler](https://github.com/paiml/depyler) transpiler.

## Key Constraint

**Zero third-party dependencies.** Every Python source file uses exclusively
the CPython 3.11+ standard library. This is enforced by AST scanning in CI.

## Quality Standards

- 95%+ test coverage (branch)
- Zero `ty` type errors
- Zero `ruff` lint violations
- Zero `bandit` security findings
- Google-style docstrings with 3+ doctests per function
- Property-based testing via Hypothesis
- Mutation testing via mutmut

## Categories (20 stdlib domains)

| Category | Stdlib modules | Rust mapping |
|---|---|---|
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
make setup    # Install dependencies
make check    # Run all quality gates
make export   # Export corpus to Parquet
```

## License

Apache-2.0
