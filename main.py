"""The One-Liner Groan-Off entry.

Writes exactly one original dad joke -- a single line of 1-140
characters, no trailing newline -- to /output/entry.txt.
Standard library only.
"""

import os

ENTRY = "I tried to start a band called '1023 MB' \u2014 we never got a gig."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    assert 1 <= len(ENTRY) <= 140, f"entry length {len(ENTRY)} outside 1-140"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY == ENTRY.strip(), "entry must not have leading/trailing whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"{ENTRY} ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
