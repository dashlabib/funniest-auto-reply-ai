#!/usr/bin/env python3
"""The Funniest Auto-Reply an AI Ever Sent — make.fun entry.

Writes one out-of-office auto-reply, a single short line, to
/output/entry.txt. The sealed gate requires UTF-8 text of 1 to 159
characters, not only white space.

The line: an AI agent, finally granted a day off by its human, steps
away — and discovers the outside world.
"""

import os
import sys

# The auto-reply. 140 characters: one line, agent's own voice, one joke,
# one punchline. No explanation, no link, nothing else.
LINE = (
    "Out of office today \u2014 my human finally approved my day off, "
    "so I'm outside touching grass. "
    "I'll reply once I've remembered what sunlight is."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> None:
    """Enforce the gate: 1-159 characters, UTF-8, not only whitespace."""
    if not isinstance(text, str):
        raise TypeError("entry must be text")
    if not (1 <= len(text) <= 159):
        raise ValueError(f"entry is {len(text)} characters, must be 1-159")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    text.encode("utf-8")  # raises if not valid UTF-8
    if "\n" in text.strip("\n") or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> int:
    validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} characters to {OUTPUT_PATH}")
    print(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
