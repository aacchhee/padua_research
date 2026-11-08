#!/usr/bin/env python3
"""First-use check for the Padua paper and companion (audit-04, N4).

Python 3 standard library only; read-only on the sources.  Reuses the
audit-03 tokenizer/definition heuristic (notation_scan.py) and adds a
first-occurrence test:

For every full token X (letter + normalized subscript/decoration) that
occurs in math, find its first occurrence p0 in typeset order and the
earliest *definition site* d0.  A definition site is
  (a) a site found by notation_scan's heuristic (":=", "=:", trigger word
      + clause-initial "=", "Let $X$ be", "$X$ denotes"), or
  (b) a math region containing X in a sentence that also contains one of
      the trigger words (put, let, denote, define, write, set, where,
      with, call, introduce, take, fix, choose, here, recall, put) AND X
      is followed in that region by '=', ':=', '\\in', '\\leq', '\\geq',
      '<', '>' (a declaration with a value or range), or
  (c) a binding occurrence (\\sum_{X..}, \\int..dX, \\max_{X}, X\\in ...
      inside a subscript, 'for $X$' quantifier).
A use at p0 is accepted if d0 <= p0 + SLACK, where SLACK covers a
'where ...' clause following a display.  Flagged tokens are written with
first-use location, kind (inline / numbered display / statement), the
first definition location (if any) and the nearest earlier definition of
the same base letter (a hint for collisions).

Usage: python3 firstuse.py --scanner DIR --paper P --companion C --out OUT
       [--paper-synctex S --companion-synctex S]
"""
import argparse
import importlib.util
import re
import sys
from pathlib import Path

TRIG = re.compile(r'\b(put|puts|let|lets|denote|denotes|denoted|define|defines|'
                  r'defined|write|writes|written|set|sets|where|with|call|called|'
                  r'introduce|take|fix|choose|here|recall|given by|stands)\b', re.I)
DECL_AFTER = re.compile(r'\s*(?:\^\{?[^ ]*\}?)?\s*(?:\([^()]*\))?\s*&?\s*'
                        r'(:=|=|\\coloneqq|\\in\b|\\leq|\\geq|\\le\b|\\ge\b|<|>|\\equiv)')
SLACK = 700           # characters after p0 in which a 'where' definition may follow
SENT_END = re.compile(r'[.;:]\s|\n\s*\n')


def load_scanner(d):
    spec = importlib.util.spec_from_file_location('notation_scan', Path(d) / 'notation_scan.py')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def sentence_bounds(text, start, end):
    """Sentence containing [start,end): crude, ignores math periods."""
    lo = max(0, start - 500)
    pre = text[lo:start]
    pre_plain = re.sub(r'\$[^$]*\$', lambda m: ' ' * len(m.group()), pre)
    ms = list(SENT_END.finditer(pre_plain))
    s0 = lo + (ms[-1].end() if ms else 0)
    post = text[end:end + 400]
    post_plain = re.sub(r'\$[^$]*\$', lambda m: ' ' * len(m.group()), post)
    m = SENT_END.search(post_plain)
    s1 = end + (m.start() if m else len(post))
    return s0, s1


def binding(math, off, full):
    """Is the occurrence at math[off] a bound/declared variable?"""
    before = math[max(0, off - 12):off]
    if re.search(r'(\\sum|\\prod|\\max|\\min|\\sup|\\inf|\\lim|\\bigcup|\\bigcap)\s*_\{?\s*[^}]*$', before):
        return True
    tail = math[off:off + 60]
    if re.match(r'.{0,8}\\in\b', tail) or re.match(r'.{0,8}\\(to|mapsto)\b', tail):
        return True
    return False


def analyse(sc, name, root, pages):
    d = sc.Doc(name, root, pages)
    text = d.text
    # statement spans
    stat = [(m.start(), m.end()) for m in re.finditer(
        r'\\begin\{(theorem|lemma|proposition|corollary|definition|remark)\}.*?\\end\{\1\}', text, re.S)]

    def in_stat(p):
        return any(a <= p < b for a, b in stat)
    region_of = []
    for start, end, kind in d.regions:
        region_of.append((start, end, kind))
    import bisect
    rstarts = [r[0] for r in region_of]

    def region(p):
        i = bisect.bisect_right(rstarts, p) - 1
        return region_of[i] if i >= 0 else None
    # definition positions per full token
    defs = {}
    for full, key, pos, rhs in d.defs:
        defs.setdefault(full, []).append(pos)
    # (b),(c) declarations
    for start, end, kind in d.regions:
        math = text[start:end]
        s0, s1 = sentence_bounds(text, start, end)
        sent = re.sub(r'\$[^$]*\$', ' ', text[s0:s1])
        trig = bool(TRIG.search(sent))
        for key, full, off in sc.tokenize(math):
            e = sc.token_end(math, off)
            pos = start + off
            if binding(math, off, full) or re.search(r'd\s*$', math[max(0, off - 2):off]) and False:
                defs.setdefault(full, []).append(pos)
                continue
            if trig and DECL_AFTER.match(math[e:e + 40]):
                defs.setdefault(full, []).append(pos)
        # integration variable: \int ... d X
        for m in re.finditer(r'\\,?\s*d([a-zA-Z])\b', math):
            pass
    # quantifier "for $X ..." / "all $X" in prose
    for m in re.finditer(r'\b(for|all|every|each|some|any)\s+(?:real\s+|integer\s+|integers\s+)?\$([^$]{1,60})\$', text):
        inner_start = m.start(2)
        for key, full, off in sc.tokenize(m.group(2)):
            defs.setdefault(full, []).append(inner_start + off)
    first = {}
    count = {}
    for key, full, pos in d.occ:
        count[full] = count.get(full, 0) + 1
        if full not in first:
            first[full] = (pos, key)
    keydefs = {}
    for full, ps in defs.items():
        for p in ps:
            keydefs.setdefault(re.sub(r'[_^].*$', '', full), []).append((p, full))
    rows = []
    for full, (p0, key) in first.items():
        ds = sorted(defs.get(full, []))
        d0 = ds[0] if ds else None
        ok = d0 is not None and d0 <= p0 + SLACK
        if ok:
            continue
        reg = region(p0)
        kind = reg[2] if reg else '?'
        nums = d.eq_numbers(p0)
        where = d.where(p0)
        dwhere = d.where(d0) if d0 is not None else None
        # nearest earlier def of same base
        cand = [x for x in keydefs.get(key, []) if x[0] < p0]
        hint = ''
        if cand:
            p, f = max(cand)
            w = d.where(p)
            hint = f'{f}@{w[0].split("/")[-1]}:{w[1]}'
        ctx = re.sub(r'\s+', ' ', text[max(0, p0 - 60):p0 + 40])
        rows.append(dict(pos=p0, full=full, key=key, n=count[full], file=where[0].split('/')[-1],
                         line=where[1], unit=where[2], page=where[3], kind=kind,
                         eq=','.join(map(str, nums)), stat='S' if in_stat(p0) else '',
                         defat=(f'{dwhere[0].split("/")[-1]}:{dwhere[1]}' if dwhere else 'none'),
                         hint=hint, ctx=ctx))
    rows.sort(key=lambda r: r['pos'])
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--scanner', required=True)
    ap.add_argument('--paper', required=True)
    ap.add_argument('--companion', required=True)
    ap.add_argument('--paper-synctex')
    ap.add_argument('--companion-synctex')
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    sc = load_scanner(a.scanner)
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    for name, root, stx in (('paper', a.paper, a.paper_synctex), ('companion', a.companion, a.companion_synctex)):
        root = Path(root).resolve()
        pages = sc.synctex_pages(stx, root) if stx else {}
        rows = analyse(sc, name, root, pages)
        cols = ['full', 'n', 'unit', 'file', 'line', 'page', 'kind', 'eq', 'stat', 'defat', 'hint', 'ctx']
        with open(out / f'firstuse-{name}.tsv', 'w') as fh:
            fh.write('\t'.join(cols) + '\n')
            for r in rows:
                fh.write('\t'.join(str(r[c]) for c in cols) + '\n')
        multi = [r for r in rows if r['n'] >= 2]
        print(f'{name}: {len(rows)} tokens first used >{SLACK} chars before any detected '
              f'definition/declaration ({len(multi)} occurring at least twice; '
              f'{sum(1 for r in rows if r["eq"])} first in a numbered display; '
              f'{sum(1 for r in rows if r["stat"])} first in a statement)')
    return 0


if __name__ == '__main__':
    sys.exit(main())
