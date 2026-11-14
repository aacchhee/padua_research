#!/usr/bin/env python3
"""M5B: list sentences ADDED to the paper between two source trees that are not
contained (whitespace-normalized) in the companion at the new tree.

usage: python3 -I containment.py OLD_PAPER_DIR NEW_PAPER_DIR NEW_COMPANION_DIR file...
Read-only; prints misses."""
import re
import sys


def norm(s):
    s = re.sub(r'%.*', '', s)
    s = re.sub(r'\s+', ' ', s)
    return s.strip()


def sentences(text):
    text = norm(text)
    parts = re.split(r'(?<=[.;:])\s+(?=[A-Z\\$(])', text)
    return [p.strip() for p in parts if len(p.strip()) > 25]


def main():
    old_p, new_p, new_c = sys.argv[1:4]
    total = 0
    for f in sys.argv[4:]:
        old = open(f'{old_p}/{f}').read()
        new = open(f'{new_p}/{f}').read()
        comp = norm(open(f'{new_c}/{f}').read())
        old_n = norm(old)
        for s in sentences(new):
            if s in old_n:
                continue  # unchanged paper sentence
            if s in comp:
                continue
            # fuzzy: try the core without leading connective
            core = s[:60]
            if core in comp:
                continue
            total += 1
            print(f'[{f}] NOT IN COMPANION: {s[:300]}')
    print('misses', total)


if __name__ == '__main__':
    main()
