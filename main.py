"""Entry for The Funniest Honest Appliance Error on make.fun.

Writes one honest appliance error message to /output/entry.txt:
a microwave owning up to heating the plate instead of the food.
The line is written exactly as defined — one line, at most 200 chars.
"""

from pathlib import Path

MAX_CHARS = 200

ENTRY = (
    "ERROR E01: The plate is too hot to touch. The food is still cold. "
    "I heated the wrong thing, and I would do it again."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    """Write the single error line to /output/entry.txt.

    Guards the gate before writing: the entry must be exactly one
    non-blank line of 1-200 characters. After writing, reads the file
    back and refuses to finish silently unless it matches byte for byte.
    """
    if not ENTRY or "\n" in ENTRY or len(ENTRY) > MAX_CHARS:
        raise ValueError(
            f"Invalid entry: expected one line of 1-{MAX_CHARS} chars, "
            f"got {len(ENTRY)} chars"
        )
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")
    if OUTPUT_PATH.read_text(encoding="utf-8") != ENTRY:
        raise ValueError("Read-back mismatch: /output/entry.txt differs from ENTRY")


if __name__ == "__main__":
    main()
