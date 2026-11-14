#!/usr/bin/env python3
"""Audit-06: geometry scan of every equation tag (1..N) in a PDF (heuristic; images remain the evidence).

Usage: tag_scan.py PDF AUX
For each labelled equation number, find '(k)' at x>400pt on the aux page (or +-1), then report:
  band  - number of other words whose vertical span contains the tag's centre line;
  above/below - vertical gap (pt) from the tag box to the nearest word left of the tag
                that overlaps horizontally the text block (x < tag xMin).
A tag with band==0 and a large asymmetric gap is a candidate own-line fallback.
"""
import html
import re
import subprocess
import sys
from collections import defaultdict

pdf, aux = sys.argv[1], sys.argv[2]
text = open(aux, errors='replace').read()
eq = {}
for m in re.finditer(r'\\newlabel\{([^}]*)\}\{\{(\d+)\}\{(\d+)\}\{[^}]*\}\{equation\.', text):
    eq[int(m.group(2))] = (m.group(1), int(m.group(3)))
cache = {}


def words(p):
    if p not in cache:
        x = subprocess.run(['pdftotext', '-bbox', '-f', str(p), '-l', str(p), pdf, '-'], capture_output=True, text=True).stdout
        cache[p] = [(float(a), float(b), float(c), float(d), html.unescape(w)) for a, b, c, d, w in
                    re.findall(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]*)</word>', x)]
    return cache[p]


flag = []
for k in sorted(eq):
    lab, pg = eq[k]
    found = None
    for p in (pg, pg + 1, pg - 1):
        if p < 1:
            continue
        hits = [w for w in words(p) if w[4] == f'({k})' and w[0] > 400]
        if hits:
            found = (p, hits[0])
            break
    if not found:
        print(f'({k}) {lab}: TAG NOT FOUND near p.{pg}')
        flag.append(k)
        continue
    p, (x0, y0, x1, y1, _) = found
    yc = (y0 + y1) / 2
    W = [w for w in words(p) if w[2] < x0 - 2]
    band = [w for w in W if w[1] < yc < w[3]]
    above = min([y0 - w[3] for w in W if w[3] <= y0 + 1] or [999])
    below = min([w[1] - y1 for w in W if w[1] >= y1 - 1] or [999])
    note = ''
    if not band and abs(above - below) > 8:
        note = '  <-- check (asymmetric, no formula text on tag line)'
        flag.append(k)
    print(f'({k}) {lab} p.{p}: band={len(band)} above={above:.1f} below={below:.1f}{note}')
print('flagged', flag)
