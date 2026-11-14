#!/usr/bin/env python3
"""For each paper display block not found verbatim-in-order in the companion,
report: (a) exact occurrence anywhere (out of order), (b) best fuzzy companion
match with a token diff after removing layout-only tokens. Read-only.

Usage: unnumbered_match.py PAPER_SECTIONS COMPANION_SECTIONS
"""
import difflib
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from block_diff_a3 import strip_comments, norm, displays  # noqa: E402

LAYOUT = re.compile(r'\\(?:qquad|quad|,|;|!|:|\s)|\\\\|&|\\begin\{(?:aligned|gathered|split|multlined)\}(?:\[[a-z]\])?|\\end\{(?:aligned|gathered|split|multlined)\}|\\(?:\[|\])|\\(?:begin|end)\{(?:align|gather|multline|equation)\*\}|\\(?:left|right|big|Big|bigl|bigr|Bigl|Bigr)\b|\\(?:displaystyle|nonumber|notag)|[{}.,;\s]')


def core(block):
    return LAYOUT.sub('', block)


def tokens(s):
    return re.findall(r'\\[A-Za-z]+|\d+|[A-Za-z]|[^\sA-Za-z\d]', s)


def main():
    pdir, cdir = Path(sys.argv[1]), Path(sys.argv[2])
    for pf in sorted(pdir.glob('*.tex')):
        p = strip_comments(pf.read_text())
        c = strip_comments((cdir / pf.name).read_text())
        dp = [norm(b) for _, b in displays(p)]
        dc = [norm(b) for _, b in displays(c)]
        i = 0
        for blk in dp:
            j = i
            while j < len(dc) and dc[j] != blk:
                j += 1
            if j < len(dc):
                i = j + 1
                continue
            anywhere = blk in dc
            # core-equality anywhere
            cores = [core(x) for x in dc]
            cb = core(blk)
            core_hit = [k for k, x in enumerate(cores) if x == cb]
            # substring of concatenated companion displays (block split into several)
            concat = ''.join(cores)
            in_concat = cb in concat
            best = max(range(len(dc)), key=lambda k: difflib.SequenceMatcher(None, cb, cores[k]).ratio())
            ratio = difflib.SequenceMatcher(None, cb, cores[best]).ratio()
            print(f'=== {pf.name}: paper block (exact elsewhere={anywhere}, core-equal idx={core_hit}, core-substring-of-concat={in_concat}, best ratio={ratio:.3f})')
            print('PAPER    :', blk[:400])
            print('COMPANION:', dc[best][:400])
            if not core_hit and not in_concat:
                a, b = tokens(cb), tokens(cores[best])
                diff = [d for d in difflib.ndiff(a, b) if d[0] in '+-']
                print('TOKEN DIFF (core):', ' '.join(diff)[:600])
            print()


if __name__ == '__main__':
    main()
