"""Worst AI pickup line entry: writes the chosen line to /output/entry.txt."""

import os

LINE = (
    "Please say yes to dinner. I already generated our anniversary "
    "photo, and I look very happy in it."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = LINE
    if not (1 <= len(text) <= 140):
        raise SystemExit(f"entry length {len(text)} outside 1..140")
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    encoded = text.encode("utf-8")
    if encoded.decode("utf-8") != text:
        raise SystemExit("entry is not valid UTF-8 text")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(encoded)
    with open(OUTPUT_PATH, "rb") as handle:
        written = handle.read()
    if written != encoded:
        raise SystemExit("written entry does not match the chosen line")


if __name__ == "__main__":
    main()
