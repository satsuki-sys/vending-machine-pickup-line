#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes a single pickup line, spoken by a vending machine to a passing
human, to /output/entry.txt (UTF-8, 1-200 chars).

Revision pass 2 (full rewrite): the first draft opened with a generic
"Hey" any stranger could say, and "hostage" leaned menacing rather than
warm. This version opens in the machine's own voice ("I run on exact
change"), keeps one specific machine detail (the coil dropping the bar
crooked), and lands the turn in the last few words.
"""

from pathlib import Path

ENTRY = (
    "I run on exact change, but my coil keeps dropping your bar crooked. "
    "I think it's flirting with you on my behalf."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars"
    out.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
