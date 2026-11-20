#!/usr/bin/env python3
"""Align simple GitHub-flavored Markdown pipe tables."""
import argparse
import re
import sys
from pathlib import Path

def cells(line):
    text = line.strip()
    if text.startswith("|"):
        text = text[1:]
    if text.endswith("|"):
        text = text[:-1]
    return [part.strip() for part in text.split("|")]

def is_separator(line):
    parts = cells(line)
    return bool(parts) and all(re.fullmatch(r":?-{3,}:?", part.replace(" ", "")) for part in parts)

def format_table(lines):
    rows = [cells(line) for line in lines]
    width = max(map(len, rows))
    rows = [row + [""] * (width - len(row)) for row in rows]
    sizes = [max(len(row[i]) for row in rows) for i in range(width)]
    output = []
    for index, row in enumerate(rows):
        if index == 1:
            parts = []
            for i, marker in enumerate(row):
                left, right = marker.startswith(":"), marker.endswith(":")
                dashes = "-" * max(3, sizes[i] - int(left) - int(right))
                parts.append((":" if left else "") + dashes + (":" if right else ""))
            output.append("| " + " | ".join(parts) + " |")
        else:
            output.append("| " + " | ".join(value.ljust(sizes[i]) for i, value in enumerate(row)) + " |")
    return output

def align_markdown(text):
    lines = text.splitlines()
    output = []
    index = 0
    while index < len(lines):
        if index + 1 < len(lines) and "|" in lines[index] and is_separator(lines[index + 1]):
            table = [lines[index], lines[index + 1]]
            index += 2
            while index < len(lines) and "|" in lines[index] and lines[index].strip():
                table.append(lines[index])
                index += 1
            output.extend(format_table(table))
        else:
            output.append(lines[index])
            index += 1
    return "\n".join(output) + ("\n" if text.endswith("\n") else "")

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", nargs="?", help="Markdown file; stdin when omitted")
    parser.add_argument("--in-place", action="store_true", help="replace the input file")
    args = parser.parse_args()
    if args.in_place and not args.file:
        parser.error("--in-place requires a file")
    path = Path(args.file) if args.file else None
    source = path.read_text(encoding="utf-8") if path else sys.stdin.read()
    result = align_markdown(source)
    if args.in_place:
        path.write_text(result, encoding="utf-8")
    else:
        print(result, end="")

if __name__ == "__main__":
    main()
