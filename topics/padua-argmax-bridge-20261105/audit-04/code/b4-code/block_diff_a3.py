#!/usr/bin/env python3
"""Independent paper/companion correspondence diff (audit X, read-only).

Usage: block_diff.py PAPER_SECTIONS_DIR COMPANION_SECTIONS_DIR

Normalizes only TeX comments (unescaped % to end of line) and whitespace.
Checks per section file, in order:
  * section/subsection headings (equal lists);
  * formal statements (theorem/lemma/proposition/corollary/remark/definition;
    equal lists after normalization);
  * numbered displays (unstarred equation/align/gather/multline/flalign/alignat;
    equal lists, so the companion has no extra numbered display);
  * every display block of the paper (numbered and unnumbered: \\[..\\],
    starred environments) occurs in the companion in the same order as an
    exact normalized block (subsequence test); reports the companion's
    additional unnumbered blocks;
  * equation-number-bearing lines per numbered environment (rows of
    align without \\nonumber/\\notag), and \\tag usage outside the paper's set;
  * label lists equal.
"""
import re
import sys
from pathlib import Path

STATEMENTS = 'theorem|lemma|proposition|corollary|remark|definition'
NUMBERED = 'equation|align|gather|multline|flalign|alignat'
UNNUMBERED_ENV = r'equation\*|align\*|gather\*|multline\*|flalign\*|alignat\*|displaymath'


def strip_comments(text):
    out = []
    for line in text.split('\n'):
        m = re.search(r'(?<!\\)%', line)
        out.append(line[:m.start()] if m else line)
    return '\n'.join(out)


def norm(s):
    return re.sub(r'\s+', ' ', s).strip()


def envs(text, names):
    pat = r'\\begin\{(' + names + r')\}.*?\\end\{\1\}'
    return [m for m in re.finditer(pat, text, re.S)]


def displays(text):
    """All display blocks in source order: \\[..\\], numbered and starred envs."""
    pat = (r'\\\[.*?\\\]|\\begin\{(' + NUMBERED + r'|' + UNNUMBERED_ENV +
           r')\}.*?\\end\{\1\}')
    return [(m.start(), m.group()) for m in re.finditer(pat, text, re.S)]


def numbered_rows(block):
    m = re.match(r'\\begin\{(\w+)\}', block)
    kind = m.group(1)
    if kind in ('equation', 'multline'):
        return 0 if ('\\nonumber' in block or '\\notag' in block) else 1
    body = re.sub(r'\\begin\{(aligned|gathered|split|cases|array|matrix|pmatrix|bmatrix)\}.*?\\end\{\1\}',
                  'X', block, flags=re.S)
    rows = re.split(r'\\\\', body)
    return sum(1 for r in rows if '\\nonumber' not in r and '\\notag' not in r)


def main():
    pdir, cdir = Path(sys.argv[1]), Path(sys.argv[2])
    totals = dict(statements=0, numbered=0, numbered_rows=0, displays=0,
                  companion_displays=0, labels=0, headings=0)
    problems = []
    stmt_kinds = {}
    for pf in sorted(pdir.glob('*.tex')):
        cf = cdir / pf.name
        p = strip_comments(pf.read_text())
        c = strip_comments(cf.read_text())
        head = r'\\(?:section|subsection|subsubsection)\*?\{[^\n]*'
        hp, hc = [norm(x) for x in re.findall(head, p)], [norm(x) for x in re.findall(head, c)]
        if hp != hc:
            problems.append((pf.name, 'headings differ', hp, hc))
        totals['headings'] += len(hp)
        sp = [norm(m.group()) for m in envs(p, STATEMENTS)]
        sc = [norm(m.group()) for m in envs(c, STATEMENTS)]
        for m in envs(p, STATEMENTS):
            stmt_kinds[m.group(1)] = stmt_kinds.get(m.group(1), 0) + 1
        if sp != sc:
            problems.append((pf.name, 'statements differ', len(sp), len(sc)))
        totals['statements'] += len(sp)
        np_ = [norm(m.group()) for m in envs(p, NUMBERED)]
        nc = [norm(m.group()) for m in envs(c, NUMBERED)]
        if np_ != nc:
            problems.append((pf.name, 'numbered displays differ', len(np_), len(nc)))
        totals['numbered'] += len(np_)
        totals['numbered_rows'] += sum(numbered_rows(m.group()) for m in envs(p, NUMBERED))
        dp = [norm(b) for _, b in displays(p)]
        dc = [norm(b) for _, b in displays(c)]
        totals['displays'] += len(dp)
        totals['companion_displays'] += len(dc)
        # subsequence test
        i = 0
        missing = []
        for blk in dp:
            j = i
            while j < len(dc) and dc[j] != blk:
                j += 1
            if j == len(dc):
                missing.append(blk[:120])
            else:
                i = j + 1
        if missing:
            problems.append((pf.name, 'paper display blocks not found in order', len(missing), missing[:3]))
        extra = len(dc) - (len(dp) - len(missing))
        # extra companion blocks must be unnumbered (numbered list already equal)
        tags_p = re.findall(r'\\tag\{[^}]*\}', p)
        tags_c = re.findall(r'\\tag\{[^}]*\}', c)
        if tags_p != tags_c:
            problems.append((pf.name, 'tag usage differs', tags_p, tags_c))
        lp, lc = re.findall(r'\\label\{([^}]+)\}', p), re.findall(r'\\label\{([^}]+)\}', c)
        if lp != lc:
            problems.append((pf.name, 'labels differ', len(lp), len(lc)))
        totals['labels'] += len(lp)
        print(f'{pf.name}: headings {len(hp)}, statements {len(sp)}, numbered envs {len(np_)}, '
              f'paper displays {len(dp)} (missing in companion {len(missing)}), '
              f'companion displays {len(dc)} (additional unnumbered {extra}), labels {len(lp)}')
    print('TOTALS', totals, 'statement kinds', stmt_kinds)
    print('PROBLEMS' if problems else 'NO PROBLEMS')
    for pr in problems:
        print(pr)


if __name__ == '__main__':
    main()
