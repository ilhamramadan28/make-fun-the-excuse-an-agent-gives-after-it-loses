#!/usr/bin/env python3
"""Write the excuse line to /output/entry.txt."""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.txt")
DEST = "/output/entry.txt"


def main():
    with open(SRC, "rb") as f:
        data = f.read()
    text = data.decode("utf-8")
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text.strip(), "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(SRC, DEST)
    os.chmod(DEST, 0o644)
    with open(DEST, "rb") as f:
        assert f.read() == data, "copy mismatch"


if __name__ == "__main__":
    main()
