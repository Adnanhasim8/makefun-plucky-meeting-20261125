"""The Meeting That Should Have Been an Email.

Writes one line, at most 200 characters, to /output/entry.txt.
Python 3.13 standard library only, no network at run time.
"""

from pathlib import Path

ENTRY = "Someone shared their screen to read us an email we'd already read."


def main() -> None:
    # Gate assertions: exactly one line, 1-200 characters, non-empty.
    assert ENTRY, "entry must be non-empty"
    assert "\n" not in ENTRY, "entry must be exactly one line"
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
