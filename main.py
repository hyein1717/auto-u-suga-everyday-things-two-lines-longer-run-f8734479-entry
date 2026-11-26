#!/usr/bin/env python3
"""Write the two-line entry for 'Everyday Things, Two Lines, Longer Run'.

Line 1 explains a traffic jam to a 10-year-old in one vivid sentence built
on a single analogy (a school hallway at home time). Line 2 says in one
sentence why the analogy works: what it maps and what it leaves out.

Stdlib only, deterministic: the same bytes are written on every run.
"""

import os

TEXT = (
    "A traffic jam is a school hallway at home time where 500 cars try to leave "
    "through one door at once, so the fastest end up stuck behind a truck hauling "
    "a house, and the only thing moving is the clock.\n"
    "The hallway maps one narrow road and a crowd pushing into it together, but it leaves "
    "out the traffic lights, the drivers losing their tempers, and that cars cannot squeeze "
    "sideways like kids.\n"
)


def check(text: str) -> None:
    """Gate check mirroring the sealed scorer: 1-400 chars, two lines."""
    if not 1 <= len(text) <= 400:
        raise ValueError(f"entry must be 1-400 characters, got {len(text)}")
    lines = text.splitlines()
    if len(lines) != 2:
        raise ValueError(f"entry must be exactly two lines, got {len(lines)}")
    if any(not line.strip() for line in lines):
        raise ValueError("entry lines must not be blank")
    for line in lines:
        if line.count(".") != 1 or not line.rstrip().endswith("."):
            raise ValueError(f"each line must be exactly one sentence: {line!r}")


def main() -> None:
    check(TEXT)
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(TEXT)


if __name__ == "__main__":
    main()
