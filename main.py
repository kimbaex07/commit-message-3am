"""Write the 3 AM commit message entry to the make.fun output directory.

Reads entry.txt next to this script, validates it (1-200 characters, one
line, not only whitespace), and writes it plus one trailing newline to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.txt")
    with open(src, "r", encoding="utf-8") as f:
        text = f.read()
    # Strip at most one trailing newline.
    if text.endswith("\n"):
        text = text[:-1]
    if not text or not text.strip():
        print("error: entry is empty", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if len(text) > 200:
        print("error: entry is %d characters, over the 200 limit" % len(text),
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, "entry.txt")
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    os.chmod(out, 0o644)
    print("entry.txt: %d characters" % len(text))
    return 0


if __name__ == "__main__":
    sys.exit(main())
