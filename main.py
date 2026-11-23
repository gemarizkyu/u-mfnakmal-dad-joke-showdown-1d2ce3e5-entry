"""Dad Joke Showdown entry (make.fun program/v1).

Writes a single original dad joke (at most 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt. Deterministic: no input, no network,
no randomness, no wall clock. The joke is 94 characters, inside the
1-200 character gate.
"""

import os

JOKE = "I told my son the ocean is the world's biggest library. Every wave comes with a current issue."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
