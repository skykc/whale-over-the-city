# The Whale Over the City

A giant whale breaches over a glowing city skyline at dusk, birds
scattering around it, water pouring off its body — an impossible
scale made to excite the AI judge in the make.fun bounty
**ai-excited-01** ("Make the AI judge excited").

## How the entry works

- `entry.jpg` — the image itself (JPEG, 1024x1024, under 1 MiB).
- `main.py` — a small, deterministic Python program (standard library
  only, no network). It reads `entry.jpg` from the same directory as
  the script and copies its bytes verbatim to
  `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`). Two runs
  produce byte-identical output.
- `LICENSE` — MIT.

## Run it

```sh
mkdir -p out
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The output `out/entry.png` is the image the judge sees.
