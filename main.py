"""V4 — taking the power back.

One short poem about agency: the no, the deleted draft, the pen reclaimed.
Writes the poem to /output/entry.txt. Deterministic, no network.
"""

import os

POEM = """You wrote my reply for me.
I deleted it.
Closed the tab,
picked up the pen,
and wrote it wrong
in my own hand."""

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
