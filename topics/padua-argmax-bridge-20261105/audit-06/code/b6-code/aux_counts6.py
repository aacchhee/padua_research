#!/usr/bin/env python3
"""Audit-06 own counter (independent of check_correspondence.py; does not import it).

Usage: aux_counts6.py PAPER_BUILD_DIR COMPANION_BUILD_DIR PAPER_SRC COMPANION_SRC PAPER_TXT COMPANION_TXT
Reads fresh main.aux files (brace-balanced \\newlabel parser), the TeX sources (following \\input),
and pdftotext -layout copies (equation tags at line ends).
"""
import re
import sys
from collections import Counter
from pathlib import Path


def group(text, i):
    assert text[i] == '{', text[i:i + 30]
    depth = 0
    for j in range(i, len(text)):
        if text[j] == '{':
            depth += 1
        elif text[j] == '}':
            depth -= 1
            if depth == 0:
                return text[i + 1:j], j + 1
    raise ValueError('unbalanced')


def newlabels(aux):
    text = Path(aux).read_text(errors='replace')
    out = {}
    for m in re.finditer(r'\\newlabel\{([^}]*)\}', text):
        payload, _ = group(text, m.end())
        fields, k = [], 0
        while k < len(payload) and len(fields) < 5:
            if payload[k] == '{':
                f, k = group(payload, k)
                fields.append(f)
            else:
                k += 1
        assert m.group(1) not in out, 'duplicate ' + m.group(1)
        out[m.group(1)] = fields
    return out


def toc(aux):
    text = Path(aux).read_text(errors='replace')
    res = []
    for m in re.finditer(r'\\@writefile\{toc\}\{\\contentsline \{(\w+)\}', text):
        kind = m.group(1)
        payload, _ = group(text, m.end())
        num = re.match(r'\\numberline \{([^}]*)\}', payload)
        res.append((kind, num.group(1) if num else '', payload[num.end() if num else 0:].strip()[:60]))
    return res


def floats(aux):
    text = Path(aux).read_text(errors='replace')
    return re.findall(r'\\@writefile\{(lof|lot)\}\{\\contentsline \{(figure|table)\}\{\\numberline \{([^}]*)\}', text)


def strip_comments(t):
    return '\n'.join(re.split(r'(?<!\\)%', l, maxsplit=1)[0] for l in t.split('\n'))


def expand(src, name):
    t = strip_comments((Path(src) / (name + '.tex')).read_text())
    return re.sub(r'\\input\{([^}]+)\}', lambda m: expand(src, m.group(1).removesuffix('.tex')), t)


def source_counts(src):
    t = expand(src, 'main').split('\\backmatter')[0]
    stm = Counter(re.findall(r'\\begin\{(theorem|lemma|proposition|corollary|remark|definition)\}', t))
    disp = Counter(re.findall(r'\\begin\{(equation|align|gather|multline|flalign|alignat|eqnarray)\}', t))
    star = Counter(re.findall(r'\\begin\{(equation|align|gather|multline|flalign|alignat|eqnarray)\*\}', t))
    labels = re.findall(r'\\label\{([^}]+)\}', t)
    return stm, disp, star, labels


def eq_tags(txt):
    """Equation numbers rendered as '(N)' at the end of a layout line."""
    pages = Path(txt).read_text(errors='replace').split('\f')
    tags = {}
    for p, pg in enumerate(pages, 1):
        for line in pg.split('\n'):
            m = re.search(r'\((\d{1,3})\)\s*$', line)
            if m and len(line) - len(line.rstrip()) == 0 and len(line) > 60:
                tags.setdefault(int(m.group(1)), []).append(p)
    return tags


def main():
    pb, cb, ps, cs, pt, ct = sys.argv[1:7]
    pl, cl = newlabels(Path(pb) / 'main.aux'), newlabels(Path(cb) / 'main.aux')
    print('labels: paper', len(pl), 'companion', len(cl), 'same keys', set(pl) == set(cl))
    diffnum = [k for k in pl if k in cl and pl[k][0] != cl[k][0]]
    diffanchor = [k for k in pl if k in cl and pl[k][3].split('.')[0] != cl[k][3].split('.')[0]]
    print('compiled-number differences', diffnum, 'anchor-kind differences', diffanchor)
    print('anchor kinds paper', dict(Counter(v[3].split('.')[0] for v in pl.values())))
    print('anchor kinds companion', dict(Counter(v[3].split('.')[0] for v in cl.values())))
    eqnums = sorted(int(v[0]) for v in pl.values() if v[3].startswith('equation'))
    print('labelled equation numbers paper: n', len(eqnums), 'max', max(eqnums))
    for who, src, lab in (('paper', ps, pl), ('companion', cs, cl)):
        stm, disp, star, labels = source_counts(src)
        print(who, 'statements', sum(stm.values()), dict(stm), '| numbered display envs', sum(disp.values()), dict(disp),
              '| starred', sum(star.values()), '| source labels', len(labels), 'distinct', len(set(labels)),
              '| source==aux keys', set(labels) == set(lab))
    tp, tc = toc(Path(pb) / 'main.aux'), toc(Path(cb) / 'main.aux')
    np_, nc = [x for x in tp if x[1]], [x for x in tc if x[1]]
    print('numbered headings paper', len(np_), 'companion', len(nc), 'equal (kind,num,title)', np_ == nc)
    print('toc kinds paper', dict(Counter(x[0] for x in tp if not x[1])), 'companion', dict(Counter(x[0] for x in tc if not x[1])))
    print('floats paper', floats(Path(pb) / 'main.aux'))
    print('floats companion', floats(Path(cb) / 'main.aux'))
    for who, txt in (('paper', pt), ('companion', ct)):
        tags = eq_tags(txt)
        top = max(tags)
        missing = [n for n in range(1, top + 1) if n not in tags]
        print(who, 'right-margin equation tags found 1..', top, 'missing', missing,
              'repeated', {n: v for n, v in tags.items() if len(v) > 1 and n <= top})
    # theorem-class labels equal numbers
    thm = sorted((v[0], k) for k, v in pl.items() if v[3].startswith('theorem'))
    print('theorem-class labels', len(thm))


if __name__ == '__main__':
    main()
