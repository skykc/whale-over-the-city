#!/usr/bin/env python3
"""Copy the bundled entry image to the output path, byte for byte.

No network, no randomness: the output is a deterministic copy of
entry.jpg, so two runs always produce identical bytes.
"""

import os
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.jpg")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    with open(source, "rb") as src:
        data = src.read()
    with open(target, "wb") as dst:
        dst.write(data)
    return 0


if __name__ == "__main__":
    sys.exit(main())
