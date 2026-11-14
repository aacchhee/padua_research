#!/usr/bin/env python3
"""Audit-06: crop the rendered region around equation tag '(k)' on page p and report geometry.

Usage: eqcrop6.py PDF PAGE K OUTPREFIX [DPI]
Prints the tag bbox and the bboxes of words on the same baseline band, plus the nearest
non-tag words above/below, so a tag set on its own line (no formula text in its band)
is detectable; the PNG is for visual inspection.
"""
import html
import re
import subprocess
import sys

pdf, page, k, out = sys.argv[1], int(sys.argv[2]), sys.argv[3], sys.argv[4]
dpi = int(sys.argv[5]) if len(sys.argv) > 5 else 200
x = subprocess.run(['pdftotext', '-bbox', '-f', str(page), '-l', str(page), pdf, '-'],
                   capture_output=True, text=True).stdout
words = [(float(a), float(b), float(c), float(d), html.unescape(w)) for a, b, c, d, w in
         re.findall(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]*)</word>', x)]
hits = [w for w in words if w[4] == f'({k})' and w[0] > 400]
if not hits:
    print('no hit')
    sys.exit(1)
tx0, ty0, tx1, ty1, _ = hits[0]
yc = (ty0 + ty1) / 2
band = [w for w in words if w is not hits[0] and w[1] < yc < w[3]]
print(f'tag ({k}) page {page}: x {tx0:.1f}-{tx1:.1f}, y {ty0:.1f}-{ty1:.1f}; '
      f'{len(band)} other words on the tag band: {" ".join(w[4] for w in band)[:120]!r}')
s = dpi / 72
y0 = max(0, ty0 - 75)
h = 140
subprocess.run(['pdftoppm', '-png', '-r', str(dpi), '-f', str(page), '-l', str(page), '-x', '0',
                '-y', str(int(y0 * s)), '-W', str(int(595 * s)), '-H', str(int(h * s)),
                '-singlefile', pdf, out], check=True)
print(out + '.png')
