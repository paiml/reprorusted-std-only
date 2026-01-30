"""Context manager using contextlib.

Demonstrates ``contextlib.contextmanager`` and its Rust equivalent
using RAII / ``Drop`` semantics.

Rust equivalent:
    struct TimedSection {
        label: String,
        start: std::time::Instant,
    }

    impl TimedSection {
        fn new(label: &str) -> Self {
            Self { label: label.to_string(), start: std::time::Instant::now() }
        }
    }

    impl Drop for TimedSection {
        fn drop(&mut self) {
            let elapsed = self.start.elapsed();
            println!("{}: {:.3}s", self.label, elapsed.as_secs_f64());
        }
    }

Examples:
    >>> from reprorusted_std_only.contextlib.contextmanager_example import collect_items
    >>> with collect_items() as items:
    ...     items.append("a")
    ...     items.append("b")
    >>> items
    ['a', 'b']
"""

from __future__ import annotations

import contextlib
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Generator


@contextlib.contextmanager
def collect_items() -> Generator[list[str], None, None]:
    """Context manager that provides a shared list for collecting items.

    The list is yielded to the ``with`` block and can be appended to.
    On exit, the list is available with all items collected.

    Yields:
        A mutable list of strings.

    Examples:
        >>> with collect_items() as items:
        ...     items.append("x")
        >>> items
        ['x']

        >>> with collect_items() as items:
        ...     pass
        >>> items
        []

        >>> with collect_items() as items:
        ...     items.extend(["one", "two", "three"])
        >>> len(items)
        3
    """
    items: list[str] = []
    yield items
