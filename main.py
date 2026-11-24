#!/usr/bin/env python3
"""The Long Roast entry.

Writes one satirical sentence to /output/entry.txt (1-320 characters,
UTF-8, a single sentence). Standard library only, no network, no input.

The line is built from two fragments: a setup (the lawmakers' authority
— a year spent writing the rules for artificial intelligence) and a
punch (the undercut — their own bill still circulates as a Word file
named FINAL_v12 because nobody in the room can turn it into a PDF).
``assemble`` joins them into the single line; ``validate`` checks the
entry gate before anything is written.
"""

from pathlib import Path

SETUP = (
    "The lawmakers who spent a year writing the rules for artificial "
    "intelligence still circulate their bill as a Word file named FINAL_v12"
)
PUNCH = "because nobody in the room can turn it into a PDF."

OUTPUT_PATH = Path("/output/entry.txt")


def assemble(setup: str, punch: str) -> str:
    """Join the setup and punch fragments into one satirical line."""
    return f"{setup} {punch}"


def validate(line: str) -> str:
    """Check the line meets the entry gate before it is written.

    Must be 1-320 characters, UTF-8-encodable, a single line, and
    more than whitespace. Raises ValueError otherwise.
    """
    if not 1 <= len(line) <= 320:
        raise ValueError(f"line must be 1-320 characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line (no newline characters)")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    line.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return line


def main() -> None:
    line = validate(assemble(SETUP, PUNCH))
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
