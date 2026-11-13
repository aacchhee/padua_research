#!/usr/bin/env python3
"""B4 adversarial correspondence harness (audit-06 adaptation of audit-05/audit-04 harness; read-only on the repository).

Builds copy trees from `git archive HEAD` of the paper and companion directories
under OUT/<scenario>/, applies one mutation per scenario, and runs:
  (a) the committed check_correspondence.py (default source-baseline mode)
      from the copy tree, with GIT_DIR pointing read-only at the original repo;
  (b) the checker's own compare_pair() alone (pairwise comparison only);
  (c) for rename scenarios, audit-03 notation_scan.py block check against the
      same baseline (final freeze 8937d3b), with and without a declared rename map.
Usage: mutation_harness.py REPO OUT
"""
import json
import os
import shutil
import subprocess
import sys
import tarfile
import io
from pathlib import Path

REPO = Path(sys.argv[1]).resolve()
OUT = Path(sys.argv[2]).resolve()
TOPIC = 'topics/padua-argmax-bridge-20261105'
HEAD = '5b1a4942af498e60e9da4c8860c57cb4f67be4ef'
BASELINE = '8937d3b723c09c004f49d3e565d0b02976713a37'  # final freeze (response-05)
ENV = dict(os.environ, GIT_DIR=str(REPO / '.git'), GIT_OPTIONAL_LOCKS='0')
NOTATION = REPO / TOPIC / 'audit-03/code/n/notation_scan.py'


def base_tree():
    base = OUT / '_base'
    if base.exists():
        shutil.rmtree(base)
    base.mkdir(parents=True)
    data = subprocess.check_output(['git', 'archive', '--format=tar', HEAD, '--',
                                    f'{TOPIC}/paper', f'{TOPIC}/companion-paper'], cwd=REPO)
    with tarfile.open(fileobj=io.BytesIO(data)) as tf:
        tf.extractall(base, filter='data')
    return base


def fresh(name, base):
    d = OUT / name
    if d.exists():
        shutil.rmtree(d)
    shutil.copytree(base, d)
    return d


def sub_once(path, old, new, after=None):
    t = path.read_text()
    start = t.index(after) if after else 0
    i = t.index(old, start)
    path.write_text(t[:i] + new + t[i + len(old):])


def sub_all(path, old, new):
    t = path.read_text()
    n = t.count(old)
    path.write_text(t.replace(old, new))
    return n


def run_checker(tree):
    p = subprocess.run([sys.executable, '-I', '-B', f'{TOPIC}/companion-paper/check_correspondence.py'],
                       cwd=tree, env=ENV, capture_output=True, text=True)
    return p.returncode, (p.stdout + p.stderr).strip().splitlines()[-1]


def run_pairwise(tree):
    code = (
        'import sys; sys.path.insert(0, sys.argv[1]); import check_correspondence as c\n'
        'try:\n'
        '    labels, claims, displays = c.compare_pair(c.current_sources(c.ORIGINAL), c.current_sources(c.HERE))\n'
        '    print(f"PAIRWISE PASS {claims}/{displays}/{len(labels)}")\n'
        'except ValueError as e:\n'
        '    print("PAIRWISE FAIL", e); sys.exit(1)\n')
    p = subprocess.run([sys.executable, '-I', '-B', '-c', code, str(tree / TOPIC / 'companion-paper')],
                       cwd=tree, env=ENV, capture_output=True, text=True)
    return p.returncode, (p.stdout + p.stderr).strip().splitlines()[-1]


def run_notation(tree, rename_map=None):
    out = tree / '_notation-out'
    cmd = [sys.executable, '-I', '-B', str(NOTATION), '--repo', str(tree), '--out', str(out),
           '--baseline-rev', BASELINE]
    if rename_map is not None:
        mp = tree / '_rename-map.json'
        mp.write_text(json.dumps(rename_map))
        cmd += ['--rename-map', str(mp)]
    p = subprocess.run(cmd, cwd=tree, env=ENV, capture_output=True, text=True)
    lines = [l for l in (p.stdout + p.stderr).splitlines()
             if l.startswith(('PASS', 'FAIL', 'RENAME-CHECK', 'MISMATCH', 'Traceback', 'baseline'))]
    return p.returncode, lines[:6]


def main():
    base = base_tree()
    P = lambda t, f: t / TOPIC / 'paper' / f
    C = lambda t, f: t / TOPIC / 'companion-paper' / f
    results = []

    def record(name, desc, tree, notation=None):
        r = {'scenario': name, 'mutation': desc, 'checker': run_checker(tree), 'pairwise': run_pairwise(tree)}
        if notation is not None:
            for tag, mp in notation:
                r['notation_scan ' + tag] = run_notation(tree, mp)
        results.append(r)

    t = fresh('S0-unmodified', base)
    record('S0', 'unmodified git-archive copy', t, [('no map', None)])

    t = fresh('S1-paired-statement-constant', base)
    for f in (P, C):
        sub_once(f(t, 'sections/comparison-unified.tex'), 'j_*=23/250', 'j_*=24/250',
                 after='\\begin{corollary}[Absolute gate]')
    record('S1', 'identical constant change j_*=23/250 -> 24/250 inside Corollary 4.6 (both texts)', t)

    t = fresh('S1b-paired-main-theorem', base)
    for f in (P, C):
        sub_once(f(t, 'sections/introduction.tex'), 'For every integer $n\\geq2$', 'For every integer $n\\geq3$',
                 after='\\begin{theorem}[Location of the maximum]')
    record('S1b', 'identical quantifier change n>=2 -> n>=3 in Theorem 1.1 (both texts)', t)

    t = fresh('S2-paired-numbered-display', base)
    for f in (P, C):
        txt = f(t, 'sections/comparison-unified.tex').read_text()
        assert '\\label{ul:log-series}' in txt
        sub_once(f(t, 'sections/comparison-unified.tex'), '(1-w_{\\log}^2)}', '(1-w_{\\log}^3)}',
                 after='\\label{ul:log-series}')
    record('S2', 'identical change inside numbered display (ul:log-series) in both texts', t)

    t = fresh('S3-paired-unnumbered-display', base)
    for f in (P, C):
        sub_once(f(t, 'sections/comparison-unified.tex'), 'H_{256}-\\log257<\\gamma', 'H_{256}-\\log258<\\gamma')
    record('S3', 'identical change inside unnumbered gamma bracket display (both texts)', t)

    t = fresh('S4-companion-only-statement', base)
    sub_once(C(t, 'sections/comparison-unified.tex'), 'j_*=23/250', 'j_*=24/250',
             after='\\begin{corollary}[Absolute gate]')
    record('S4', 'companion-only change j_* inside Corollary 4.6', t)

    rename = [{'from': '\\mathfrak T', 'to': '\\mathfrak S', 'files': ['comparison-unified.tex']}]
    t = fresh('S5-paired-rename', base)
    n = [sub_all(f(t, 'sections/comparison-unified.tex'), '\\mathfrak T', '\\mathfrak S') for f in (P, C)]
    record('S5', f'paired rename \\mathfrak T -> \\mathfrak S in comparison-unified.tex (occurrences paper/companion {n})',
           t, [('no map', None), ('declared map', rename)])

    fake = [{'from': 'j_*=23/250', 'to': 'j_*=24/250', 'files': ['comparison-unified.tex']}]
    t = fresh('S6-constant-as-declared-rename', base)
    for f in (P, C):
        sub_once(f(t, 'sections/comparison-unified.tex'), 'j_*=23/250', 'j_*=24/250',
                 after='\\begin{corollary}[Absolute gate]')
    record('S6', 'S1 constant change declared as a "rename" in the map', t,
           [('no map', None), ('declared map', fake)])

    t = fresh('S7-readme-prose', base)
    with open(C(t, 'README.md'), 'a') as fh:
        fh.write('\nAUDIT MUTATION\n')
    record('S7', 'README.md prose append (excluded from freeze by design)', t)

    t = fresh('S8-extra-tex-file', base)
    for f in (P, C):
        f(t, 'sections/extra.tex').write_text('% audit\n')
    record('S8', 'new sections/extra.tex in both trees (not \\input)', t)

    t = fresh('S9-paired-bib', base)
    for f in (P, C):
        sub_once(f(t, 'references.bib'), '1954', '1955')
    record('S9', 'identical year change in both references.bib', t)

    t = fresh('S10-paired-main-numbering', base)
    for f in (P, C):
        sub_once(f(t, 'main.tex'), '\\newtheorem{theorem}{Theorem}[section]', '\\newtheorem{theorem}{Theorem}')
    record('S10', 'identical theorem-numbering change in both main.tex', t)

    t = fresh('S11-companion-only-prose', base)
    sub_once(C(t, 'sections/corner-unified.tex'), 'the ', 'the AUDIT ')
    record('S11', 'companion-only prose change outside any statement/display', t)

    for r in results:
        print(json.dumps(r))


if __name__ == '__main__':
    main()
