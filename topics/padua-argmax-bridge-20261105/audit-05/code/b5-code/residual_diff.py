#!/usr/bin/env python3
"""Audit-05: show residual differences of numbered blocks vs baseline AFTER the
literal rename map (same block/rename semantics as audit-03 notation_scan.py,
reimplemented here).  Read-only; uses `git show` on REPO.

Usage: residual_diff.py REPO BASELINE MAP SIDE(paper|companion)
"""
import difflib
import json
import re
import subprocess
import sys
from pathlib import Path

REPO, BASE, MAP, SIDE = sys.argv[1:5]
TOPIC = 'topics/padua-argmax-bridge-20261105'
CLAIMS = r'theorem|lemma|proposition|corollary|definition|remark'
DISPLAYS = r'equation|align|gather|multline|flalign|alignat|eqnarray'
renames = json.loads(Path(MAP).read_text())


def blocks(text, names):
    return [m.group() for m in re.finditer(r'\\begin\{(' + names + r')\}.*?\\end\{\1\}', text, re.S)]


def apply(text, fname):
    for r in renames:
        if r.get('files') and fname not in r['files']:
            continue
        text = re.sub(r['from'], r['to'], text) if r.get('regex') else text.replace(r['from'], r['to'])
    return text


def toks(s):
    return re.findall(r'\\[A-Za-z]+|\\.|[A-Za-z]+|\d+|\S', s)


total = 0
for f in sorted((Path(REPO) / TOPIC / SIDE / 'sections').glob('*.tex')):
    rel = f'{TOPIC}/paper/sections/{f.name}'
    old = subprocess.check_output(['git', 'show', f'{BASE}:{rel}'], cwd=REPO, text=True)
    cur = f.read_text()
    for names, kind in ((CLAIMS, 'statement'), (DISPLAYS, 'display')):
        exp = [apply(x, f.name) for x in blocks(old, names)]
        got = blocks(cur, names)
        if len(exp) != len(got):
            print(f'!! {f.name} {kind}: count {len(exp)} vs {len(got)}')
        for i, (a, b) in enumerate(zip(exp, got)):
            if a == b:
                continue
            total += 1
            lab = (re.findall(r'\\label\{([^}]+)\}', a) or [f'#{i}'])[0]
            ta, tb = toks(a), toks(b)
            sm = difflib.SequenceMatcher(None, ta, tb, autojunk=False)
            print(f'\n### {f.name} {kind} {lab}  (tokens {len(ta)} -> {len(tb)}, ratio {sm.ratio():.3f})')
            for op, i1, i2, j1, j2 in sm.get_opcodes():
                if op == 'equal':
                    continue
                l = ' '.join(ta[max(0, i1 - 4):i1])
                print(f'  {op:7} ...{l} | -[{" ".join(ta[i1:i2])[:220]}] +[{" ".join(tb[j1:j2])[:220]}]')
print(f'\nTOTAL residual blocks ({SIDE}): {total}')
