#!/usr/bin/env python3
"""One-Line Robot Wedding Vows.

Writes a one-line robot wedding vow to /output/entry.txt.
"""

import os

ENTRY = "I vow to love you through 214 firmware updates, every dead battery, and every reboot — and to never once call tech support on you."

# One joke only: a wedding vow of loyalty phrased as a customer-service
# non-action — the spouse is buggy enough that tech support is on the
# table, and the vow is never to call it. Concrete number (214 updates),
# machine world (firmware, battery, reboot, tech support), twist in the
# final words: "never once call tech support on you".

assert 1 <= len(ENTRY) <= 160 and "\n" not in ENTRY and ENTRY.strip()


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
