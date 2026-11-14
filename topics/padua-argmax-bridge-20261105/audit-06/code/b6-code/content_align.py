#!/usr/bin/env python3
"""Audit-06 content-aligned residual analysis of numbered blocks vs a baseline after a literal rename map.

Own reimplementation (same block regex and rename semantics as audit-03 notation_scan.py); read-only.
Usage: content_align.py SRC_ROOT BASE_REV MAP|- SIDE(paper|companion-paper)   [env GIT_DIR for git show]

For each section file and kind (statement / numbered display):
  * blocks are aligned by CONTENT (difflib on the block lists), not by index;
  * 'equal' runs at different indices are reported as index shifts (unchanged content);
  * each replaced/inserted/deleted block is classified:
      FORMAT  - identical after removing whitespace, &, \\\\, \\notag/\\nonumber, split/aligned wrappers,
                \\quad/\\qquad/\\, spacing and \\left/\\right sizing (layout only);
      CONTENT - anything else (token diff printed);
      NEW / DELETED.
"""
import difflib
import json
import re
import subprocess
import sys
from pathlib import Path

SRC, BASE, MAP, SIDE = sys.argv[1:5]
TOPIC = 'topics/padua-argmax-bridge-20261105'
CL = r'theorem|lemma|proposition|corollary|definition|remark'
DI = r'equation|align|gather|multline|flalign|alignat|eqnarray'
R = json.loads(Path(MAP).read_text()) if MAP != '-' else []


def blocks(t, n):
    return [m.group() for m in re.finditer(r'\\begin\{(' + n + r')\}.*?\\end\{\1\}', t, re.S)]


def ap(t, f):
    for r in R:
        if r.get('files') and f not in r['files']:
            continue
        t = re.sub(r['from'], r['to'], t) if r.get('regex') else t.replace(r['from'], r['to'])
    return t


def lab(b):
    return (re.findall(r'\\label\{([^}]+)\}', b) or ['(nolabel)'])[0]


def layout_norm(b):
    b = re.sub(r'\\begin\{(equation|align|split|aligned|gathered|multline)\*?\}(\[[^\]]*\])?', '', b)
    b = re.sub(r'\\end\{(equation|align|split|aligned|gathered|multline)\*?\}', '', b)
    b = re.sub(r'\\(notag|nonumber|quad|qquad|left|right|big|Big|bigg|Bigg)\b', '', b)
    b = re.sub(r'\\[,;:! ]', '', b)
    b = re.sub(r'\\\\(\[[^\]]*\])?', '', b)
    b = b.replace('&', '')
    return re.sub(r'\s+', '', b)


def toks(s):
    return re.findall(r'\\[A-Za-z]+|\\.|[A-Za-z]+|\d+|\S', s)


def tokdiff(a, b):
    ta, tb = toks(a), toks(b)
    sm = difflib.SequenceMatcher(None, ta, tb, autojunk=False)
    out = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op != 'equal':
            out.append(f'      {op}: ...{" ".join(ta[max(0, i1 - 5):i1])} | -[{" ".join(ta[i1:i2])[:300]}] +[{" ".join(tb[j1:j2])[:300]}]')
    return out


counts = {'shift': 0, 'format': 0, 'content': 0, 'new': 0, 'deleted': 0, 'same_index_equal': 0}
for f in sorted((Path(SRC) / TOPIC / SIDE / 'sections').glob('*.tex')):
    old = subprocess.check_output(['git', 'show', f'{BASE}:{TOPIC}/paper/sections/{f.name}'], text=True)
    cur = f.read_text()
    for n, k in ((CL, 'statement'), (DI, 'display')):
        e = [ap(x, f.name) for x in blocks(old, n)]
        g = blocks(cur, n)
        sm = difflib.SequenceMatcher(None, e, g, autojunk=False)
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op == 'equal':
                for a, b in zip(range(i1, i2), range(j1, j2)):
                    if a == b:
                        counts['same_index_equal'] += 1
                    else:
                        counts['shift'] += 1
                        print(f'{f.name} {k}: SHIFT (content equal) {lab(e[a])} baseline#{a} -> current#{b}')
                continue
            pairs = list(zip(range(i1, i2), range(j1, j2)))
            for a, b in pairs:
                if layout_norm(e[a]) == layout_norm(g[b]):
                    counts['format'] += 1
                    print(f'{f.name} {k}: FORMAT-ONLY {lab(e[a])} -> {lab(g[b])} (#{a}->#{b})')
                else:
                    counts['content'] += 1
                    print(f'{f.name} {k}: CONTENT {lab(e[a])} -> {lab(g[b])} (#{a}->#{b})')
                    print('\n'.join(tokdiff(e[a], g[b])))
            for a in range(i1 + len(pairs), i2):
                counts['deleted'] += 1
                print(f'{f.name} {k}: DELETED {lab(e[a])} #{a}')
            for b in range(j1 + len(pairs), j2):
                counts['new'] += 1
                print(f'{f.name} {k}: NEW {lab(g[b])} #{b}: {g[b][:400]!r}')
print('COUNTS', SIDE, BASE[:8], 'map entries', len(R), counts)
