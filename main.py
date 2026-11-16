"""The Whale Over the City - make.fun ai-excited-01 entry.

Copies the bundled entry image to the output directory, byte for byte.
Deterministic: the same input always produces the same output bytes.
"""

import os
import shutil
from pathlib import Path


def main():
    here = Path(__file__).resolve().parent
    src = here / "entry.jpg"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(src, "rb") as fin, open(out_dir / "entry.png", "wb") as fout:
        shutil.copyfileobj(fin, fout)


if __name__ == "__main__":
    main()
