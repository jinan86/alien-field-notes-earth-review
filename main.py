#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review — make.fun entry.

A program/v1 entry: writes exactly one line of plain text to
/output/entry.txt — a review of planet Earth left by an alien tourist.

The line is fixed in this file (no randomness, no network, stdlib only),
so every run produces byte-identical output.

Chosen angle: fireworks. Humans set off coloured explosions in the sky
for fun and call it a celebration; the alien reads the same display the
way their own world does — as the opening of a war. The laugh comes from
that alien inversion of an ordinary Earth celebration, not from a joke
bolted on. Angles deliberately avoided because the field is saturated
with them: queues, Wi-Fi passwords, pet dogs ("tiny wolves"), food and
snacks, weather, "would abduct again", generic "five stars", gravity,
money, and traffic.
"""

import os
import sys
from pathlib import Path

# One line, one clean joke, punch at the end, verdict in the tail.
ENTRY = (
    "They explode coloured lights in the sky for fun and call it a "
    "celebration. On my planet, that's how a war starts. 4/5"
)


def output_path() -> Path:
    """Where the entry goes: /output/entry.txt in the grading sandbox.

    ENTRY_OUTPUT overrides it for local runs only; the graded run uses
    the default.
    """
    return Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))


def main() -> int:
    text = ENTRY
    # Gate mirror: 1-200 UTF-8 characters, not only whitespace.
    if not 1 <= len(text) <= 200:
        print(f"entry is {len(text)} characters, must be 1-200", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry is only whitespace", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    text.encode("utf-8")  # raises if not valid UTF-8

    path = output_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
