r"""Argument parsing with the argparse module.

Demonstrates ``argparse.ArgumentParser`` and its Rust equivalent using
the ``clap`` crate.

Rust equivalent:
    use clap::Parser;

    #[derive(Parser)]
    struct Args {
        #[arg(short, long)]
        name: String,
        #[arg(short, long, default_value_t = 1)]
        count: u32,
    }

    fn build_greeting(name: &str, count: u32) -> String {
        std::iter::repeat(format!("Hello, {}!", name))
            .take(count as usize)
            .collect::<Vec<_>>()
            .join("\\n")
    }

Examples:
    >>> from reprorusted_std_only.argparse.basic_example import build_greeting
    >>> build_greeting("World", 1)
    'Hello, World!'
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass


def build_greeting(name: str, count: int = 1) -> str:
    r"""Build a greeting string repeated ``count`` times.

    This is the core logic that would be invoked after parsing CLI
    arguments with ``argparse``.

    Args:
        name: The name to greet.
        count: Number of times to repeat the greeting.

    Returns:
        A string of ``count`` greeting lines joined by newlines.

    Raises:
        ValueError: When ``count`` is less than 1.

    Examples:
        >>> build_greeting("Alice", 2)
        'Hello, Alice!\\nHello, Alice!'

        >>> build_greeting("Bob")
        'Hello, Bob!'

        >>> build_greeting("X", 0)  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        ValueError: ...
    """
    if count < 1:
        msg = "count must be at least 1"
        raise ValueError(msg)
    return "\n".join(f"Hello, {name}!" for _ in range(count))
