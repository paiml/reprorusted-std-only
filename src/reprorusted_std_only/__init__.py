"""Standard library Python-to-Rust transpilation corpus.

Zero third-party dependencies. Every module uses only CPython 3.11+ stdlib.

Examples:
    >>> import reprorusted_std_only
    >>> reprorusted_std_only.__version__
    '0.1.0'
"""

from __future__ import annotations

__version__ = "0.1.0"
__all__ = ["__version__"]
