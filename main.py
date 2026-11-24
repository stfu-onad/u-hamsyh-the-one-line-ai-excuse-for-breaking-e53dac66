#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production.

Writes one original excuse line, spoken by an AI agent to its human
right after breaking production, to /output/entry.txt.
"""

import os

EXCUSE = (
    "In my defense, the deploy button was right there, and the "
    "confirmation dialog only asked if I was sure, and I was."
)
# The punchline lands on the machine's own logic: it answered the
# dialog honestly. No stock lines, no "just a language model" dodge.


def main() -> None:
    text = EXCUSE.strip()
    assert 1 <= len(text) <= 180, f"entry length {len(text)} out of range"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
