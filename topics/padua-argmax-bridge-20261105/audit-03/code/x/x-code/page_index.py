#!/usr/bin/env python3
"""Page index and label comparison from two fresh .aux files (audit X, read-only).

Usage: page_index.py PAPER_AUX COMPANION_AUX
Prints a markdown table: label, kind, number, paper page, companion page,
and a summary of number mismatches.
"""
import re
import sys
from pathlib import Path

LABEL = re.compile(r'^\\newlabel\{([^}]*)\}\{\{([^}]*)\}\{([^}]*)\}\{(.*)\}\{([^}]*)\}\{\}\}\s*$')
TOC = re.compile(r'^\\@writefile\{toc\}\{\\contentsline \{(section|subsection|subsubsection)\}\{\\numberline \{([^}]*)\}(.*)\}\{(\d+)\}\{([^}]*)\}')


def parse(path):
    labels = {}
    toc = []
    for line in Path(path).read_text(errors='replace').splitlines():
        m = LABEL.match(line)
        if m:
            key, num, page, title, anchor = m.groups()
            labels[key] = (num, int(page) if page.isdigit() else page, anchor, title)
            continue
        m = TOC.match(line)
        if m:
            kind, num, title, page, anchor = m.groups()
            toc.append((kind, num, title.strip(), int(page)))
    return labels, toc


def kind(anchor):
    return anchor.split('.')[0] if anchor else '?'


def main():
    pl, pt = parse(sys.argv[1])
    cl, ct = parse(sys.argv[2])
    print('## Sections and subsections (number, title, paper page, companion page)\n')
    print('| Kind | No. | Title | Paper p. | Companion p. |')
    print('|---|---|---|---|---|')
    cmap = {(k, n): p for k, n, _, p in ct}
    for k, n, t, p in pt:
        print(f'| {k} | {n} | {t[:70]} | {p} | {cmap.get((k, n), "MISSING")} |')
    missing_c = [(k, n) for k, n, _, _ in ct if (k, n) not in {(a, b) for a, b, _, _ in pt}]
    print(f'\nCompanion-only toc entries: {missing_c}\n')
    print('## Labels (key, kind, paper no./page, companion no./page)\n')
    print('| Label | Kind | Paper no. | Paper p. | Comp. no. | Comp. p. |')
    print('|---|---|---|---|---|---|')
    mism = []
    for key, (num, page, anchor, _) in pl.items():
        c = cl.get(key)
        if c is None:
            mism.append((key, 'missing in companion'))
            cn, cp = 'MISSING', ''
        else:
            cn, cp = c[0], c[1]
            if cn != num:
                mism.append((key, f'paper {num} companion {cn}'))
        print(f'| {key} | {kind(anchor)} | {num} | {page} | {cn} | {cp} |')
    extra = sorted(set(cl) - set(pl))
    kinds = {}
    for key, (num, page, anchor, _) in pl.items():
        kinds[kind(anchor)] = kinds.get(kind(anchor), 0) + 1
    print(f'\nPaper labels: {len(pl)}; companion labels: {len(cl)}; kinds (paper): {kinds}')
    print(f'Number mismatches: {mism}')
    print(f'Companion-only labels: {extra}')


if __name__ == '__main__':
    main()
