#!/usr/bin/env python3
"""Audit-05 independent counts from FRESH .aux files (+ source envs + pdftotext).

Usage: aux_counts.py PAPER_BUILD COMPANION_BUILD PAPER_SRC COMPANION_SRC PAPER_TXT COMPANION_TXT

Own brace-balanced aux parser (does not import check_correspondence.py).
Read-only.  Reports: labels (keys, numbers, anchors), numbered headings (toc),
floats (lof/lot), labeled statements, equation numbers rendered, statement and
numbered-display environment counts in source (unstarred), and equality checks.
"""
import re
import sys
from pathlib import Path


def balanced(text, i):
    assert text[i] == '{', (i, text[i:i + 20])
    depth = 0
    for j in range(i, len(text)):
        ch = text[j]
        if ch == '\\':
            continue
        if ch == '{' and (j == 0 or text[j - 1] != '\\'):
            depth += 1
        elif ch == '}' and text[j - 1] != '\\':
            depth -= 1
            if depth == 0:
                return text[i + 1:j], j + 1
    raise ValueError('unbalanced')


def groups(text, i, n):
    out = []
    for _ in range(n):
        while text[i] in ' \n':
            i += 1
        g, i = balanced(text, i)
        out.append(g)
    return out, i


def parse_aux(path):
    text = Path(path).read_text(errors='replace')
    labels, toc, floats = {}, [], []
    for m in re.finditer(r'\\newlabel\{', text):
        (key, payload), _ = groups(text, m.end() - 1, 2)
        fields, _ = groups(payload, 0, 5)
        if key in labels:
            raise SystemExit('duplicate label ' + key)
        labels[key] = dict(num=fields[0], page=fields[1], title=fields[2], anchor=fields[3])
    for m in re.finditer(r'\\@writefile\{(toc|lof|lot)\}', text):
        (body,), _ = groups(text, m.end(), 1)
        cm = re.match(r'\\contentsline \{(\w+)\}', body)
        if not cm:
            continue
        kind = cm.group(1)
        rest, j = body[cm.end():], 0
        (title, page, anchor), _ = groups(rest, 0, 3)
        nm = re.match(r'\\numberline \{([^}]*)\}', title)
        num = nm.group(1) if nm else ''
        (toc if m.group(1) == 'toc' else floats).append((kind, num, page, anchor))
    last = re.search(r'\\gdef \\@abspage@last\{(\d+)\}', text)
    return labels, toc, floats, int(last.group(1)) if last else None


def strip_comments(t):
    return '\n'.join(re.split(r'(?<!\\)%', l, maxsplit=1)[0] for l in t.split('\n'))


def expand(src, name):
    t = strip_comments((Path(src) / (name + '.tex')).read_text())
    return re.sub(r'\\input\{([^}]+)\}', lambda m: expand(src, m.group(1)), t)


STMT = r'theorem|lemma|proposition|corollary|remark|definition'
DISP = r'equation|align|gather|multline|flalign|alignat|eqnarray'


def source_counts(src):
    t = expand(src, 'main')
    body = t.split('\\begin{document}', 1)[1]
    stm = re.findall(r'\\begin\{(' + STMT + r')\}', body)
    disp = list(re.finditer(r'\\begin\{(' + DISP + r')\}(.*?)\\end\{\1\}', body, re.S))
    rows = 0
    for d in disp:
        inner = d.group(2)
        if d.group(1) in ('equation', 'multline'):
            r = 1 - len(re.findall(r'\\(?:nonumber|notag)\b', inner))
        else:
            inner2 = re.sub(r'\\begin\{(aligned|split|gathered|cases|array|matrix|pmatrix|bmatrix)\}.*?\\end\{\1\}', '', inner, flags=re.S)
            parts = re.split(r'\\\\', inner2)
            parts = [p for p in parts if p.strip()]
            r = sum(1 for p in parts if not re.search(r'\\(?:nonumber|notag)\b', p))
        rows += r
    starred = len(re.findall(r'\\begin\{(?:' + DISP + r')\*\}', body))
    heads = re.findall(r'\\(section|subsection|subsubsection)(\*?)\{', body.split('\\backmatter')[0])
    lab = re.findall(r'\\label\{([^}]+)\}', body)
    return dict(statements=len(stm), stmt_kinds={k: stm.count(k) for k in sorted(set(stm))},
                numbered_display_envs=len(disp), numbered_rows_est=rows, starred_display_envs=starred,
                numbered_headings=sum(1 for h in heads if not h[1]), source_labels=len(lab),
                distinct_source_labels=len(set(lab)), label_list=lab)


def rendered_eq_numbers(txt):
    s = Path(txt).read_text(errors='replace')
    found = set(int(x) for x in re.findall(r'\((\d{1,3})\)\s*$', s, re.M))
    return found


def main():
    pb, cb, ps, cs, pt, ct = sys.argv[1:7]
    P = parse_aux(Path(pb) / 'main.aux')
    C = parse_aux(Path(cb) / 'main.aux')
    out = []
    for who, (labels, toc, floats, last) in (('paper', P), ('companion', C)):
        kinds = {}
        for v in labels.values():
            k = v['anchor'].split('.')[0]
            kinds[k] = kinds.get(k, 0) + 1
        eqn = sorted(int(v['num']) for v in labels.values() if v['anchor'].startswith('equation.'))
        out.append(f"{who}: aux labels {len(labels)}; anchors {kinds}; numbered toc headings "
                   f"{sum(1 for e in toc if e[1] and e[0] in ('section','subsection','subsubsection'))}; "
                   f"floats {[(k, n, p) for k, n, p, a in floats]}; @abspage@last {last}; "
                   f"labeled eq numbers min/max {eqn[0]}/{eqn[-1]}")
    pl, cl = P[0], C[0]
    out.append(f"label key sets equal: {set(pl) == set(cl)}; numbers differ: "
               f"{[k for k in pl if k in cl and pl[k]['num'] != cl[k]['num']]}; anchors differ: "
               f"{[k for k in pl if k in cl and pl[k]['anchor'] != cl[k]['anchor']]}")
    ph = [(k, n) for k, n, p, a in P[1] if n]
    ch = [(k, n) for k, n, p, a in C[1] if n]
    out.append(f"numbered heading sequences equal: {ph == ch} ({len(ph)})")
    out.append(f"floats equal (kind,num): {[(k, n) for k, n, p, a in P[2]] == [(k, n) for k, n, p, a in C[2]]}")
    sp, sc = source_counts(ps), source_counts(cs)
    for who, s in (('paper', sp), ('companion', sc)):
        out.append(f"{who} source: " + ', '.join(f'{k}={v}' for k, v in s.items() if k != 'label_list'))
    out.append(f"source label lists equal: {sp['label_list'] == sc['label_list']}; source labels == aux labels: "
               f"paper {set(sp['label_list']) == set(pl)}, companion {set(sc['label_list']) == set(cl)}")
    stp = [k for k, v in pl.items() if v['anchor'].startswith('theorem.')]
    out.append(f"labeled statements (theorem-class anchors): {len(stp)}; unlabeled statements = "
               f"{sp['statements'] - len(stp)}")
    for who, txt in (('paper', pt), ('companion', ct)):
        f = rendered_eq_numbers(txt)
        rng = set(range(1, 87))
        out.append(f"{who} rendered right-margin (k) found for 1..86: {len(f & rng)}; missing {sorted(rng - f)}; "
                   f"above 86: {sorted(x for x in f if x > 86)[:10]}")
    print('\n'.join(out))


if __name__ == '__main__':
    main()
