#!/usr/bin/env python3
"""B4 page index from fresh .aux files plus pdftotext (audit-05 copy of audit-04 tool, read-only).

Usage: page_index.py PAPER_AUX COMPANION_AUX PAPER_TXT COMPANION_TXT PAPER_SRC COMPANION_SRC

* Sections/subsections/paragraphs: aux toc entries (printed page = \\thepage).
* Figures/tables: aux lof/lot entries.
* Formal statements: every \\begin{theorem|lemma|proposition|corollary|remark|definition}
  in source order (following \\input from main.tex); the compiled number and printed
  page come from the label when one exists, otherwise from the first pdftotext page
  whose text contains '<Kind> <number>' where the number is reconstructed from the
  shared [theorem] counter (reset by \\section).
* Also checks printed page numbers against physical page index (form feeds).
"""
import re
import sys
from pathlib import Path

LABEL = re.compile(r'^\\newlabel\{([^}]*)\}\{\{([^}]*)\}\{([^}]*)\}\{(.*)\}\{([^}]*)\}\{\}\}\s*$')
TOC = re.compile(r'^\\@writefile\{toc\}\{\\contentsline \{(\w+)\}\{(?:\\numberline \{([^}]*)\})?(.*)\}\{(\d+)\}\{([^}]*)\}')
LOFT = re.compile(r'^\\@writefile\{(lof|lot)\}\{\\contentsline \{(figure|table)\}\{\\numberline \{([^}]*)\}\{\\ignorespaces (.*?)\}\}\{(\d+)\}\{([^}]*)\}')
STMT = 'theorem|lemma|proposition|corollary|remark|definition'


def parse_aux(path):
    labels, toc, floats = {}, [], []
    for line in Path(path).read_text(errors='replace').splitlines():
        m = LABEL.match(line)
        if m:
            key, num, page, title, anchor = m.groups()
            labels[key] = (num, page, anchor)
            continue
        m = TOC.match(line)
        if m:
            kind, num, title, page, anchor = m.groups()
            toc.append((kind, num or '', title.strip(), page))
            continue
        m = LOFT.match(line)
        if m:
            _, kind, num, cap, page, anchor = m.groups()
            floats.append((kind, num, cap[:60], page))
    return labels, toc, floats


def strip_comments(text):
    return '\n'.join(re.split(r'(?<!\\)%', l, 1)[0] for l in text.split('\n'))


def expand(srcdir, name):
    text = strip_comments((Path(srcdir) / (name + '.tex')).read_text())
    return re.sub(r'\\input\{([^}]+)\}', lambda m: expand(srcdir, m.group(1)), text)


def statements(srcdir):
    """Source-order statements with reconstructed numbers (shared counter per section)."""
    text = expand(srcdir, 'main')
    text = text.split('\\backmatter')[0]
    sec, cnt, out = 0, 0, []
    tok = re.compile(r'\\section\{|\\begin\{(' + STMT + r')\}(\[[^\]]*\])?\s*(\\label\{([^}]*)\})?')
    for m in tok.finditer(text):
        if m.group(0).startswith('\\section{'):
            sec += 1
            cnt = 0
            continue
        cnt += 1
        out.append((m.group(1), f'{sec}.{cnt}', (m.group(2) or '')[1:-1][:45], m.group(4)))
    return out


def page_of(txt, kind, num):
    pages = Path(txt).read_text(errors='replace').split('\f')
    pat = re.compile(r'\b' + kind.capitalize() + r'\s+' + re.escape(num) + r'\b')
    for i, pg in enumerate(pages, 1):
        if pat.search(pg):
            return str(i)
    return '?'


def printed_vs_physical(txt):
    pages = Path(txt).read_text(errors='replace').split('\f')
    bad = []
    for i, pg in enumerate(pages, 1):
        lines = [l.strip() for l in pg.strip().split('\n') if l.strip()]
        if not lines:
            continue
        cand = [l for l in (lines[0], lines[-1]) if re.fullmatch(r'\d+', l.split()[-1] if l.split() else '')]
        nums = {int(l.split()[-1]) for l in cand} | ({int(lines[0].split()[0])} if lines[0].split()[0].isdigit() else set())
        if nums and i not in nums:
            bad.append((i, sorted(nums)))
    return len(pages), bad


def main():
    paux, caux, ptxt, ctxt, psrc, csrc = sys.argv[1:7]
    pl, pt, pf = parse_aux(paux)
    cl, ct, cf = parse_aux(caux)
    print('# Page index (fresh audit-05 builds)\n')
    print('Printed page numbers from the fresh .aux files (\\thepage); unlabeled statements located by pdftotext.\n')
    print('## Numbered sections and subsections\n')
    print('| Kind | No. | Title | Paper p. | Companion p. |')
    print('|---|---|---|---|---|')
    cmap = {(k, n): p for k, n, _, p in ct if n}
    for k, n, t, p in pt:
        if n:
            print(f'| {k} | {n} | {t[:70]} | {p} | {cmap.get((k, n), "MISSING")} |')
    pnum = [(k, n) for k, n, _, _ in pt if n]
    cnum = [(k, n) for k, n, _, _ in ct if n]
    print(f'\nNumbered heading sequence equal: {pnum == cnum} ({len(pnum)} paper, {len(cnum)} companion).\n')
    print('## Unnumbered toc entries (paragraph/subparagraph)\n')
    print('| Text | Kind | Title | Page |')
    print('|---|---|---|---|')
    for who, toc in (('paper', pt), ('companion', ct)):
        for k, n, t, p in toc:
            if not n:
                print(f'| {who} | {k} | {t[:70]} | {p} |')
    print('\n## Figures and tables\n')
    print('| Kind | No. | Caption (start) | Paper p. | Companion p. |')
    print('|---|---|---|---|---|')
    cfm = {(k, n): p for k, n, _, p in cf}
    for k, n, c, p in pf:
        print(f'| {k} | {n} | {c} | {p} | {cfm.get((k, n), "MISSING")} |')
    print('\n## Formal statements\n')
    print('| Kind | No. (reconstructed) | Optional title | Label | Paper no./p. | Companion no./p. |')
    print('|---|---|---|---|---|---|')
    ps, cs = statements(psrc), statements(csrc)
    for (k, n, t, lab), (k2, n2, t2, lab2) in zip(ps, cs):
        if lab:
            pn, pp, _ = pl.get(lab, ('MISSING', '?', ''))
            cn, cp, _ = cl.get(lab, ('MISSING', '?', ''))
        else:
            pn, pp = n, page_of(ptxt, k, n) + ' (text)'
            cn, cp = n2, page_of(ctxt, k2, n2) + ' (text)'
        flag = '' if (k, n, t, lab) == (k2, n2, t2, lab2) and pn == n and cn == n2 else ' **DIFF**'
        print(f'| {k} | {n} | {t} | {lab or "(none)"} | {pn} / {pp} | {cn} / {cp} |{flag}')
    print(f'\nStatements: paper {len(ps)}, companion {len(cs)}; source-order kind/number/title/label lists equal: {ps == cs}.\n')
    print('## All labels\n')
    print('| Label | Anchor kind | Paper no. | Paper p. | Comp. no. | Comp. p. |')
    print('|---|---|---|---|---|---|')
    mism = []
    for key, (num, page, anchor) in pl.items():
        c = cl.get(key)
        cn, cp = (c[0], c[1]) if c else ('MISSING', '')
        if not c or cn != num:
            mism.append((key, num, cn))
        print(f'| {key} | {anchor.split(".")[0]} | {num} | {page} | {cn} | {cp} |')
    extra = sorted(set(cl) - set(pl))
    print(f'\nPaper labels {len(pl)}, companion labels {len(cl)}; number mismatches {mism}; companion-only {extra}.')
    for who, txt in (('paper', ptxt), ('companion', ctxt)):
        n, bad = printed_vs_physical(txt)
        print(f'\n{who}: {n} text pages (incl. trailing), printed-vs-physical page mismatches (heuristic header/footer scan): {bad[:10]}')


if __name__ == '__main__':
    main()
