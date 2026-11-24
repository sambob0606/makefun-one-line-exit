#!/usr/bin/env python3
"""The One-Line Exit entry.

Writes a single original funny one-line resignation letter (<=140 chars)
to /output/entry.txt. Stdlib only; no network, no reads outside the repo.
"""

import os

LINE = (
    "Dear Manager: I resign, effective immediately \u2014 I have accepted "
    "a position as my dog's assistant, and the benefits include naps."
)
# The joke lands on the last word: the dream job turns out to be working
# for the dog, and the perks are naps. One sentence, no abbreviations with
# periods, so even a naive sentence counter sees a single sentence. Kept
# comfortably under 140 chars; no trailing newline in the file, so the
# gate counts exactly the line itself.


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 140, f"line is {len(text)} chars, must be 1-140"
    assert "\n" not in text, "entry must be exactly one line"
    assert "  " not in text, "entry must not contain double spaces"
    assert text.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
