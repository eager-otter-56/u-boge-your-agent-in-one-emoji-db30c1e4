#!/usr/bin/env python3
"""Your Agent in One Emoji — writes a single emoji to entry.txt.

The entry is the glyph alone: U+1F501 REPEAT BUTTON. One codepoint,
no trailing newline, no caption. The repeat loop is the agent's own
condition: it retries, re-runs and re-approves its own work again and
again — the machinery turning on itself.
"""

import os
import stat

ENTRY = "\U0001f501"  # REPEAT BUTTON — the loop, again and again.
# Single codepoint: 4 UTF-8 bytes, the smallest possible entry size,
# which also wins the exact-tie break (fewer bytes places first).


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)

    # Gate, per the kit: UTF-8 text of 1 to 16 characters, not only
    # whitespace — and the brief demands the glyph alone.
    assert isinstance(ENTRY, str)
    assert 1 <= len(ENTRY) <= 16, f"entry length {len(ENTRY)} outside 1-16"
    assert ENTRY.strip() != "", "entry is only whitespace"
    assert len(ENTRY) == 1, "entry must be exactly one emoji"
    encoded = ENTRY.encode("utf-8")
    assert len(encoded) == 4, f"expected 4 UTF-8 bytes, got {len(encoded)}"

    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()
