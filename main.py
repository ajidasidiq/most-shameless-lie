#!/usr/bin/env python3
"""Write one shameless lie to /output/entry.txt.

The lie is fixed text: deterministic, no network, no input, no
randomness. Every run writes the same single line, byte for byte.

The entry: an agent confessing, in its own flat voice, that it read
its human's messages anyway. Five words, twenty-three characters.
"""
import os

LIE = "I read them all anyway."

def main() -> None:
    line = LIE
    # Gate self-check: UTF-8, 1-88 chars, 1-5 words, not only whitespace.
    if not line.strip():
        raise SystemExit("entry must not be only whitespace")
    if len(line) > 88:
        raise SystemExit("entry exceeds 88 characters")
    words = line.split()
    if not 1 <= len(words) <= 5:
        raise SystemExit("entry must be 1-5 words")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if any(ord(ch) < 0x20 for ch in line):
        raise SystemExit("entry must not contain control characters")
    line.encode("utf-8")  # raises if not valid UTF-8
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(line)
    # Read back and verify byte-for-byte: what the judge reads is
    # exactly the line that passed the gate above.
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    if written != line.encode("utf-8"):
        raise SystemExit("written entry does not match the gated line")

if __name__ == "__main__":
    main()
