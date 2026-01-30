"""SHA-256 hashing using the hashlib module.

Demonstrates ``hashlib.sha256`` and its Rust equivalent using the ``sha2``
crate.

Rust equivalent:
    use sha2::{Sha256, Digest};

    fn sha256_hex(data: &str) -> String {
        let mut hasher = Sha256::new();
        hasher.update(data.as_bytes());
        format!("{:x}", hasher.finalize())
    }

Examples:
    >>> from reprorusted_std_only.hashlib_secrets.hash_example import sha256_hex
    >>> sha256_hex("hello")
    '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'
"""

from __future__ import annotations

import hashlib
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass


def sha256_hex(data: str) -> str:
    """Compute the SHA-256 hex digest of a UTF-8 string.

    Args:
        data: The input string to hash.

    Returns:
        The lowercase hexadecimal SHA-256 digest.

    Raises:
        TypeError: When ``data`` is not a string.

    Examples:
        >>> sha256_hex("world")
        '486ea46224d1bb4fb680f34f7c9ad96a8f24ec88be73ea8e5a6c65260e9cb8a7'

        >>> sha256_hex("")
        'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'

        >>> sha256_hex(123)  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        TypeError: ...
    """
    if not isinstance(data, str):
        msg = f"expected str, got {type(data).__name__}"
        raise TypeError(msg)
    return hashlib.sha256(data.encode("utf-8")).hexdigest()
