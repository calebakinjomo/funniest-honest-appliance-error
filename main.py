"""Entry for The Funniest Honest Appliance Error on make.fun.

Writes one honest appliance error message to /output/entry.txt:
a microwave owning up to heating the plate instead of the food.
"""

from pathlib import Path

ENTRY = (
    "ERROR E01: The plate is too hot to touch. The food is still cold. "
    "I heated the wrong thing, and I would do it again."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    """Write the single error line to /output/entry.txt."""
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
