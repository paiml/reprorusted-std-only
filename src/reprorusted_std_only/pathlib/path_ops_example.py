"""Path manipulation with pathlib.

Demonstrates ``pathlib.PurePosixPath`` operations and their Rust equivalents
using ``std::path::Path``.

Rust equivalent:
    fn file_extension(path: &str) -> Option<String> {
        std::path::Path::new(path)
            .extension()
            .map(|e| e.to_string_lossy().to_string())
    }

Examples:
    >>> from reprorusted_std_only.pathlib.path_ops_example import file_extension
    >>> file_extension("/home/user/doc.txt")
    'txt'
"""

from __future__ import annotations

import pathlib
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass


def file_extension(path: str) -> str | None:
    """Extract the file extension from a path string.

    Uses ``pathlib.PurePosixPath.suffix`` to extract the extension
    without the leading dot.

    Args:
        path: A file path string.

    Returns:
        The file extension without the dot, or ``None`` if there is no
        extension.

    Raises:
        TypeError: When ``path`` is not a string.

    Examples:
        >>> file_extension("archive.tar.gz")
        'gz'

        >>> file_extension("no_extension") is None
        True

        >>> file_extension(123)  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        TypeError: ...
    """
    if not isinstance(path, str):
        msg = f"expected str, got {type(path).__name__}"
        raise TypeError(msg)
    suffix = pathlib.PurePosixPath(path).suffix
    if not suffix:
        return None
    return suffix.lstrip(".")
