#!/usr/bin/env python3
"""Audit-05: content-aligned (not index-aligned) comparison of numbered blocks vs
baseline after the literal rename map.  Read-only.  Usage: block_align.py REPO BASE MAP SIDE"""
import difflib, json, re, subprocess, sys
from pathlib import Path
REPO, BASE, MAP, SIDE = sys.argv[1:5]
TOPIC = 'topics/padua-argmax-bridge-20261105'
CL = r'theorem|lemma|proposition|corollary|definition|remark'
DI = r'equation|align|gather|multline|flalign|alignat|eqnarray'
R = json.loads(Path(MAP).read_text())
def blocks(t, n): return [m.group() for m in re.finditer(r'\\begin\{(' + n + r')\}.*?\\end\{\1\}', t, re.S)]
def ap(t, f):
    for r in R:
        if r.get('files') and f not in r['files']: continue
        t = re.sub(r['from'], r['to'], t) if r.get('regex') else t.replace(r['from'], r['to'])
    return t
lab = lambda b: (re.findall(r'\\label\{([^}]+)\}', b) or ['(nolabel)'])[0]
for f in sorted((Path(REPO) / TOPIC / SIDE / 'sections').glob('*.tex')):
    old = subprocess.check_output(['git', 'show', f'{BASE}:{TOPIC}/paper/sections/{f.name}'], cwd=REPO, text=True)
    cur = f.read_text()
    for n, k in ((CL, 'statement'), (DI, 'display')):
        e = [ap(x, f.name) for x in blocks(old, n)]; g = blocks(cur, n)
        sm = difflib.SequenceMatcher(None, e, g, autojunk=False)
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op != 'equal':
                print(f'{f.name} {k}: {op} baseline[{i1}:{i2}] {[lab(x) for x in e[i1:i2]]} -> current[{j1}:{j2}] {[lab(x) for x in g[j1:j2]]}')
        moved = [lab(x) for x in e if x in g and e.index(x) != g.index(x)]
        if moved: print(f'  {f.name} {k}: blocks byte-equal (after map) but at different index: {len(moved)}')
