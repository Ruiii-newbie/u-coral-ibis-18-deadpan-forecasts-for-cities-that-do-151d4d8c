#!/usr/bin/env python3
"""Deadpan forecast for the city of Varn Hollow, which does not exist.

Writes the single forecast line to /output/entry.txt and nothing else.
"""
import os

ENTRY = (
    "In Varn Hollow, expect 14 centimetres of sideways rain by noon, "
    "with 90-kilometre-an-hour gusts relocating the post office twice before tea."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
