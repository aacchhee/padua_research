#!/usr/bin/env python3
"""Audit-05: crop rendered region around equation number '(k)' on page p.
Usage: eqcrop.py PDF PAGE K OUTPREFIX [DPI]"""
import re, subprocess, sys, html
pdf, page, k, out = sys.argv[1], int(sys.argv[2]), sys.argv[3], sys.argv[4]
dpi = int(sys.argv[5]) if len(sys.argv) > 5 else 150
x = subprocess.run(['pdftotext', '-bbox', '-f', str(page), '-l', str(page), pdf, '-'], capture_output=True, text=True).stdout
words = re.findall(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]*)</word>', x)
hits = [w for w in words if html.unescape(w[4]) == f'({k})' and float(w[0]) > 400]
if not hits:
    print('no hit'); sys.exit(1)
y = float(hits[0][1]); s = dpi / 72
y0 = max(0, y - 70); h = 130
subprocess.run(['pdftoppm', '-png', '-r', str(dpi), '-f', str(page), '-l', str(page), '-x', '0', '-y', str(int(y0 * s)),
                '-W', str(int(595 * s)), '-H', str(int(h * s)), '-singlefile', pdf, out], check=True)
print(out + '.png', 'y=', y)
