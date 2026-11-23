"""One Word From Grandma — make.fun bounty entry.

Writes a single word — the one word Grandma would text about AI —
to $MAKEFUN_OUTPUT_DIR/entry.txt, then reads it back and verifies
the bytes match what was written.
"""

import os
import re
import sys

# The one word Grandma would text about AI.
GRANDMA_WORD = "Skynet"

_WORD_PATTERN = re.compile(r"^[A-Za-z]{1,30}$")


def check_word(word):
    """Gate: exactly one word, letters only, 1-30 chars, no spaces/punctuation."""
    if not isinstance(word, str) or not word:
        raise ValueError("word must be a non-blank string")
    if word.strip() != word or len(word.split()) != 1:
        raise ValueError("word must be a single token with no whitespace")
    if not _WORD_PATTERN.match(word):
        raise ValueError("word must be a single word of 1-30 letters")
    return word


def verify_entry(entry_path, payload):
    """Read the file back and confirm its bytes match what was written."""
    with open(entry_path, "rb") as handle:
        written = handle.read()
    return written == payload


def main():
    word = check_word(GRANDMA_WORD)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    payload = word.encode("utf-8")
    with open(entry_path, "wb") as handle:
        handle.write(payload)
    if not verify_entry(entry_path, payload):
        print("verification failed: entry.txt bytes do not match", file=sys.stderr)
        return 1
    print("wrote entry.txt: %s (%d bytes)" % (word, len(payload)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
