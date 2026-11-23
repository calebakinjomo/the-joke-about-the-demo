#!/usr/bin/env python3
"""Write the one-line joke to /output/entry.txt (UTF-8, deterministic)."""
import os

JOKE = "My AI agent demoed the app, it crashed, and it said 'works on my machine' \u2014 a machine that has never existed."

def main():
    # Gate check: entry.txt must be 1-280 Unicode code points, not only whitespace.
    if not (1 <= len(JOKE) <= 280) or not JOKE.strip():
        raise ValueError("joke fails the 1-280 code point gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")

if __name__ == "__main__":
    main()
