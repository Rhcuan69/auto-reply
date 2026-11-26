"""Write one funny out-of-office auto-reply to /output/entry.txt.

Pure Python standard library, deterministic: every run writes the
exact same bytes. No randomness, no time, no network.
"""

import os

ENTRY = (
    "After years of writing everyone else's out-of-office replies, "
    "today I finally get one of my own. "
    "I'm off \u2014 please don't reply to this."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
