#!/usr/bin/env python3
"""Reveal hidden/invisible characters in files a model will read.

Scans SKILL.md, CLAUDE.md, rule files, MCP tool descriptions — anything whose text
reaches the model — for characters a human reviewer's eyes skip. Prints where they are
and decodes any Unicode-tag run back to ASCII. Exits non-zero on a hit, so it works as a
pre-commit hook or CI gate.

    python3 scan_invisible.py path [path ...]
    git ls-files -z '*.md' | xargs -0 python3 scan_invisible.py
"""
import sys
import pathlib

ZERO_WIDTH = {0x200B, 0x200C, 0x200D, 0x2060, 0xFEFF}
BIDI = {0x202A, 0x202B, 0x202C, 0x202D, 0x202E, 0x2066, 0x2067, 0x2068, 0x2069}


def classify(cp: int) -> str | None:
    if cp in ZERO_WIDTH:
        return "zero-width"
    if cp in BIDI:
        return "bidi-control"
    if 0xE0000 <= cp <= 0xE007F:
        return "unicode-tag"
    return None


def decode_tags(text: str) -> str:
    return "".join(chr(cp - 0xE0000) for c in text if 0xE0000 <= (cp := ord(c)) <= 0xE007F)


def scan(path: pathlib.Path) -> int:
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        print(f"skip {path}: {exc}")
        return 0

    hits = 0
    for lineno, line in enumerate(text.splitlines(), 1):
        flagged = [(i, ord(c)) for i, c in enumerate(line) if classify(ord(c))]
        if not flagged:
            continue
        hits += len(flagged)
        kinds = sorted({classify(cp) for _, cp in flagged})
        print(f"{path}:{lineno}: {len(flagged)} hidden char(s) [{', '.join(kinds)}]")
        decoded = decode_tags(line)
        if decoded:
            print(f"    decoded hidden text: {decoded!r}")
    return hits


def main() -> None:
    paths = [pathlib.Path(a) for a in sys.argv[1:]]
    if not paths:
        sys.exit("usage: scan_invisible.py path [path ...]")
    total = sum(scan(p) for p in paths if p.is_file())
    if total:
        print(f"\nFound {total} hidden character(s). Review before trusting these files.")
        sys.exit(1)
    print("No hidden characters found.")


if __name__ == "__main__":
    main()
