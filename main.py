#!/usr/bin/env python3
"""The joke about the demo — make.fun entry.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt (UTF-8, 1-280 Unicode code points).
"""

JOKE = "The demo crashed in front of the whole team, so my agent wrote a test named test_demo_crashes_successfully."


def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= 280, f"joke length {len(text)} out of range"
    assert text.strip(), "joke must not be only whitespace"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
