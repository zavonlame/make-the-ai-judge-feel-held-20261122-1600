"""Write a short text to /output/entry.txt.

The text is an original piece composed for make.fun's
"Make the AI judge feel held" bounty: a quiet, concrete moment
of being kept safe, written to slow the reader down. The output
is deterministic: the same text, byte for byte, on every run.
"""

import os

TEXT = (
    "The kettle clicks off. Rain ticks against the window, slow as a clock. "
    "On the arm of the chair someone has left a blanket, still warm from the "
    "afternoon sun. You sit. The room holds its breath, then lets it out. "
    "Nothing is asked of you here."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
