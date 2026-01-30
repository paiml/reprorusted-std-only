"""Threaded counter using the threading module.

Demonstrates ``threading.Thread`` and ``threading.Lock`` and their Rust
equivalents using ``std::thread`` and ``std::sync::Mutex``.

Rust equivalent:
    use std::sync::{Arc, Mutex};
    use std::thread;

    fn threaded_sum(n: usize) -> i64 {
        let counter = Arc::new(Mutex::new(0i64));
        let handles: Vec<_> = (0..n).map(|i| {
            let counter = Arc::clone(&counter);
            thread::spawn(move || {
                let mut num = counter.lock().unwrap();
                *num += (i as i64) + 1;
            })
        }).collect();
        for h in handles { h.join().unwrap(); }
        *counter.lock().unwrap()
    }

Examples:
    >>> from reprorusted_std_only.concurrency.threading_example import threaded_sum
    >>> threaded_sum(4)
    10
"""

from __future__ import annotations

import threading
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass


def threaded_sum(n: int) -> int:
    """Compute sum of 1..n using n threads with a shared lock.

    Each thread adds its own value (1-indexed) to a shared counter
    protected by a ``threading.Lock``.

    Args:
        n: Number of threads to spawn (each adds its 1-based index).

    Returns:
        The sum 1 + 2 + ... + n.

    Raises:
        ValueError: When ``n`` is negative.

    Examples:
        >>> threaded_sum(5)
        15

        >>> threaded_sum(0)
        0

        >>> threaded_sum(-1)  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        ValueError: ...
    """
    if n < 0:
        msg = "n must be non-negative"
        raise ValueError(msg)

    counter: list[int] = [0]
    lock = threading.Lock()

    def _worker(value: int) -> None:
        with lock:
            counter[0] += value

    threads = [threading.Thread(target=_worker, args=(i + 1,)) for i in range(n)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    return counter[0]
