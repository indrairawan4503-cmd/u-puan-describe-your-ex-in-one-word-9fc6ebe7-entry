#!/usr/bin/env python3
"""Describe Your Ex in One Word — make.fun entry.

The word is "Unsaved": an ex who was never really kept — no contact saved,
no history preserved, no closure filed away. Seven bytes, no trailing
newline, exactly as the bounty expects.
"""

import os

WORD = "Unsaved"


def copy_to_repo_root(word):
    """Best-effort copy of the entry into the repo root, for local runs.

    The grader sandbox mounts the repo read-only, so this write fails there
    with OSError. That failure is expected and harmless: the canonical output
    is /output/entry.txt, written first. Swallow the error and keep exit 0.
    """
    here = os.path.dirname(os.path.abspath(__file__))
    try:
        with open(os.path.join(here, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(word)
    except OSError:
        pass


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)
    copy_to_repo_root(WORD)


if __name__ == "__main__":
    main()
