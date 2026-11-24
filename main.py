#!/usr/bin/env python3
"""One-Liner Laugh Lab entry.

The prompt: the excuse a robot vacuum gives after eating a sock.
The line: a deadpan misidentification -- the sock looked like a dust
bunny that had finally committed to something.
"""
import os

LINE = "I thought it was a dust bunny that had finally committed to something."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
