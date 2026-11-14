#!/usr/bin/env python3
"""B4 diagnostic of the helper's artifact stage WITHOUT the original PDFs.

The documented artifact mode requires the preserved 48/162-page PDFs, which are
absent here. This diagnostic imports the committed helper from a git-archive
copy tree, replaces ONLY preserved_pdf() by a recorder (so the historical-PDF
identity check is explicitly NOT performed), and runs artifacts() on
(a) the fresh audit builds, (b) a copy of the fresh companion aux with one label
number altered, (c) a companion output whose aux lacks one label.
Also re-runs prose-only control S11b. Usage: artifact_diag.py TREE BUILD WORK
"""
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

TREE, BUILD, WORK = (Path(a).resolve() for a in sys.argv[1:4])
TOPIC = 'topics/padua-argmax-bridge-20261105'
sys.path.insert(0, str(TREE / TOPIC / 'companion-paper'))
os.environ['GIT_DIR'] = '/home/user/padua_research/.git'
os.environ['GIT_OPTIONAL_LOCKS'] = '0'
os.chdir(TREE)
import check_correspondence as c  # noqa: E402

calls = []
c.preserved_pdf = lambda path, kind: calls.append((str(path), kind))
labels, claims, displays = c.compare_pair(c.current_sources(c.ORIGINAL), c.current_sources(c.HERE))
dummy_p, dummy_c = WORK / 'orig-paper.pdf', WORK / 'orig-companion.pdf'


def attempt(tag, paper_out, comp_out):
    try:
        c.artifacts(paper_out, comp_out, labels, False, dummy_p, dummy_c)
        print(tag, '-> PASS (preserved_pdf NOT verified; recorded calls:', len(calls), ')')
    except ValueError as e:
        print(tag, '-> FAIL:', e)


attempt('(a) fresh builds', BUILD / 'paper', BUILD / 'companion')
for tag, edit in [('(b) one label number altered', lambda t: t.replace(
        '\\newlabel{ul:far192}{{5.2}', '\\newlabel{ul:far192}{{5.3}', 1)),
                  ('(c) one label missing', lambda t: re.sub(r'\\newlabel\{ul:far192\}[^\n]*\n', '', t, 1))]:
    d = WORK / ('comp-' + tag[1])
    if d.exists():
        shutil.rmtree(d)
    d.mkdir(parents=True)
    shutil.copy(BUILD / 'companion' / 'main.pdf', d / 'main.pdf')
    (d / 'main.aux').write_text(edit((BUILD / 'companion' / 'main.aux').read_text()))
    attempt(tag, BUILD / 'paper', d)
attempt('(d) same output dir for both', BUILD / 'paper', BUILD / 'paper')

# S11b: companion-only prose change outside statements/displays/headings
work_tree = WORK / 'S11b-tree'
if work_tree.exists():
    shutil.rmtree(work_tree)
shutil.copytree(TREE, work_tree)
f = work_tree / TOPIC / 'companion-paper' / 'sections' / 'corner-unified.tex'
t = f.read_text()
i = t.index('\\begin{proof}')
f.write_text(t[:i] + 'AUDIT PROSE MUTATION. ' + t[i:])
p = subprocess.run([sys.executable, '-I', '-B', f'{TOPIC}/companion-paper/check_correspondence.py'],
                   cwd=work_tree, capture_output=True, text=True)
print('S11b companion-only prose before first proof: checker exit', p.returncode, (p.stdout + p.stderr).strip().splitlines()[-1])
q = subprocess.run([sys.executable, '-I', '-B', '-c',
                    'import sys; sys.path.insert(0, sys.argv[1]); import check_correspondence as c; '
                    'l, a, b = c.compare_pair(c.current_sources(c.ORIGINAL), c.current_sources(c.HERE)); '
                    'print("PAIRWISE PASS", a, b, len(l))', str(work_tree / TOPIC / 'companion-paper')],
                   cwd=work_tree, capture_output=True, text=True)
print('S11b pairwise:', q.returncode, (q.stdout + q.stderr).strip().splitlines()[-1])
