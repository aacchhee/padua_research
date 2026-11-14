#!/usr/bin/env python3
"""Notation register scanner for the Padua paper and its companion.

Offline, python3 standard library only.  Read-only on the sources.

What it does
  (a) tokenizes the math of both texts (document order, following \\input)
      and lists, for each symbol, its candidate definition sites;
  (b) flags symbols with more than one definition site inside one
      section unit (subsection, or section preamble);
  (c) checks that the numbered statement and numbered display blocks of
      the two texts agree (the same test as check_correspondence.py, but
      paper-current against companion-current), and optionally that the
      only changes against a baseline revision are those of a rename map;
  (d) writes baseline tables and a summary.

Definition sites are found heuristically (see DEFINITION HEURISTIC below);
they are candidates for a human check, not a parse of the mathematics.

Usage (from anywhere):
  python3 notation_scan.py --repo /path/to/padua_research \
      [--topic topics/padua-argmax-bridge-20261105] [--out OUTDIR] \
      [--paper-synctex P.synctex.gz --companion-synctex C.synctex.gz] \
      [--baseline-rev SHA --rename-map renames.json] [--symbol 'Q' ...]
"""
from pathlib import Path
import argparse
import collections
import gzip
import json
import re
import subprocess
import sys

GREEK = ('alpha beta gamma delta epsilon varepsilon zeta eta theta vartheta '
         'iota kappa lambda mu nu xi pi varpi rho varrho sigma varsigma tau '
         'upsilon phi varphi chi psi omega Gamma Delta Theta Lambda Xi Pi '
         'Sigma Upsilon Phi Psi Omega ell').split()
DECOR = ('bar overline hat widehat tilde widetilde mathcal mathsf mathbb '
         'mathfrak mathscr mathbf boldsymbol check breve dot ddot vec '
         'underline mathrm').split()
DROP_ARG = ('text textrm textit textbf hbox mbox operatorname label eqref ref '
            'cite tag hspace vspace phantom').split()
MATH_ENVS = ('equation equation* align align* gather gather* multline '
             'multline* flalign flalign* alignat alignat* eqnarray eqnarray* '
             'displaymath math').split()
CLAIMS = r'theorem|lemma|proposition|corollary|definition|remark'
DISPLAYS = r'equation|align|gather|multline|flalign|alignat|eqnarray'
SKIP_ENVS = ('tikzpicture',)
TRIGGER = re.compile(
    r'\b(put|puts|let|lets|write|writes|written|define|defines|defined|'
    r'denote|denotes|denoted|set|sets|introduce|take|fix|call|called|'
    r'where|with|here|recall|abbreviate|choose|notation|means|throughout|'
    r'hereafter|once|retain|keep|use)\b', re.I)
SENTENCE_END = re.compile(r'[.;:]\s|\n\s*\n')
UNIT_RE = re.compile(r'\\(section|subsection|subsubsection|paragraph)(\*?)\s*\{')


# ---------------------------------------------------------------- loading
def strip_comment(line):
    out, i = [], 0
    while i < len(line):
        c = line[i]
        if c == '\\' and i + 1 < len(line):
            out.append(line[i:i + 2]); i += 2; continue
        if c == '%':
            break
        out.append(c); i += 1
    return ''.join(out)


def load_document(root):
    """Return list of (relfile, lineno, text) in typeset order."""
    lines = []

    def walk(path):
        for no, raw in enumerate(path.read_text().split('\n'), 1):
            text = strip_comment(raw)
            m = re.search(r'\\input\{([^}]+)\}', text)
            if m:
                before = text[:m.start()]
                if before.strip():
                    lines.append((path.relative_to(root).as_posix(), no, before))
                target = root / m.group(1)
                if target.suffix != '.tex':
                    target = target.with_suffix('.tex')
                walk(target)
                after = text[m.end():]
                lines.append((path.relative_to(root).as_posix(), no, after))
            else:
                lines.append((path.relative_to(root).as_posix(), no, text))
    walk(root / 'main.tex')
    return lines


def flatten(lines):
    """Join lines; return text and position->(file,line) via line starts."""
    starts, parts, pos = [], [], 0
    for f, no, t in lines:
        starts.append((pos, f, no))
        parts.append(t + '\n')
        pos += len(t) + 1
    return ''.join(parts), starts


class Locator:
    def __init__(self, starts):
        self.starts = starts
        self.keys = [s[0] for s in starts]

    def __call__(self, pos):
        import bisect
        i = bisect.bisect_right(self.keys, pos) - 1
        return self.starts[i][1], self.starts[i][2]


# ---------------------------------------------------------- units/sections
def balanced(text, i, open_='{', close='}'):
    """text[i]==open_; return index after matching close."""
    depth = 0
    j = i
    while j < len(text):
        c = text[j]
        if c == '\\':
            j += 2; continue
        if c == open_:
            depth += 1
        elif c == close:
            depth -= 1
            if depth == 0:
                return j + 1
        j += 1
    return len(text)


def section_units(text):
    """List of (pos, unit_id, title).  unit_id like '3', '3.2', '4.2'."""
    sec = sub = 0
    units = [(0, '0', 'front matter')]
    seen_body = False
    for m in UNIT_RE.finditer(text):
        kind, star = m.group(1), m.group(2)
        end = balanced(text, m.end() - 1)
        title = text[m.end():end - 1]
        if kind == 'section' and not star:
            sec += 1; sub = 0
            units.append((m.start(), str(sec), title))
        elif kind == 'subsection' and not star:
            sub += 1
            units.append((m.start(), f'{sec}.{sub}', title))
    return units


def unit_of(units, pos):
    uid = units[0][1]
    for p, u, _ in units:
        if p <= pos:
            uid = u
        else:
            break
    return uid


# ------------------------------------------------------------ math regions
def math_regions(text):
    """Yield (start, end, kind) of math content (excluding delimiters)."""
    regions = []
    i, n = 0, len(text)
    env_re = re.compile(r'\\begin\{([^}]+)\}')
    while i < n:
        c = text[i]
        if c == '\\':
            if text.startswith('\\begin{', i):
                m = env_re.match(text, i)
                name = m.group(1)
                if name in SKIP_ENVS:
                    e = text.find('\\end{' + name + '}', m.end())
                    i = e + len(name) + 6 if e >= 0 else n
                    continue
                if name in MATH_ENVS:
                    endtag = '\\end{' + name + '}'
                    e = text.find(endtag, m.end())
                    regions.append((m.end(), e, 'display:' + name))
                    i = e + len(endtag)
                    continue
                i = m.end(); continue
            if text.startswith('\\[', i):
                e = text.find('\\]', i + 2)
                regions.append((i + 2, e, 'display:\\['))
                i = e + 2; continue
            if text.startswith('\\(', i):
                e = text.find('\\)', i + 2)
                regions.append((i + 2, e, 'inline'))
                i = e + 2; continue
            i += 2; continue
        if c == '$':
            if text.startswith('$$', i):
                e = text.find('$$', i + 2)
                regions.append((i + 2, e, 'display:$$'))
                i = e + 2; continue
            j = i + 1
            while j < n:
                if text[j] == '\\':
                    j += 2; continue
                if text[j] == '$':
                    break
                j += 1
            regions.append((i + 1, j, 'inline'))
            i = j + 1; continue
        i += 1
    return regions


# --------------------------------------------------------------- tokenizer
CS = re.compile(r'\\([A-Za-z]+)\*?|\\(.)')


def read_arg(s, i):
    """Read one TeX argument at s[i:] (after spaces). Return (content, j)."""
    while i < len(s) and s[i] in ' \n\t':
        i += 1
    if i >= len(s):
        return '', i
    if s[i] == '{':
        j = balanced(s, i)
        return s[i + 1:j - 1], j
    m = CS.match(s, i)
    if m:
        return m.group(0), m.end()
    return s[i], i + 1


def norm(s):
    s = re.sub(r'\\rm\b', '', s)
    s = re.sub(r'\s+', '', s)
    s = re.sub(r'^\{(.*)\}$', r'\1', s)
    return s


def is_decoration_sup(sup, has_sub):
    s = norm(sup)
    if s in ('*', '+', '-', '\\pm', '\\prime', "'", '\\phi', '\\star', '\\sharp', '\\flat', '\\circ'):
        return True
    if s.startswith('(') and s.endswith(')'):
        return True
    if has_sub and re.fullmatch(r'[A-Za-z]', s):
        return True
    return False


def tokenize(math):
    """Return list of (key, full, offset_in_math).

    key  : base symbol, e.g. 'Q', '\\bar{e}', '\\mathcal{H}', '\\ell'
    full : key with normalized subscript and decorative superscript.
    """
    toks = []
    i, n = 0, len(math)
    while i < n:
        c = math[i]
        if c == '\\':
            m = CS.match(math, i)
            if not m:
                i += 1; continue
            name = m.group(1) or ''
            j = m.end()
            if name in DROP_ARG:
                _, j = read_arg(math, j)
                i = j; continue
            if name == 'begin' or name == 'end':
                arg, j = read_arg(math, j)
                if norm(arg) in ('array', 'tabular'):
                    _, j = read_arg(math, j)
                i = j; continue
            if name == 'multicolumn':
                _, j = read_arg(math, j); _, j = read_arg(math, j)
                i = j; continue
            if name in ('rm', 'mathrm') and name == 'rm':
                # {\rm near}: skip the rest of the group word
                k = j
                while k < n and (math[k].isalpha() or math[k] == ' '):
                    k += 1
                i = k; continue
            if name in DECOR:
                arg, j2 = read_arg(math, j)
                inner = norm(arg)
                if name == 'mathrm' and not re.fullmatch(r'[A-Za-z]', inner):
                    i = j2; continue
                if re.fullmatch(r'\d+', inner):
                    key = '\\%s{%s}' % (name, inner)
                else:
                    key = '\\%s{%s}' % (name, inner)
                start = i
                i = j2
            elif name in GREEK:
                key = '\\' + name
                start = i
                i = j
            else:
                i = j; continue
        elif c.isalpha():
            # differentials dt, dx, \frac{d}{ds}, df': not the symbol d
            if c == 'd' and (
                    (i + 1 < n and math[i + 1].isalpha() and
                     (i + 2 >= n or not math[i + 2].isalpha()) and
                     (i == 0 or not math[i - 1].isalpha())) or
                    (i > 0 and math[i - 1] == '{' and i + 1 < n and math[i + 1] == '}')):
                i += 1
                continue
            key = c
            start = i
            i += 1
        else:
            i += 1; continue
        # subscript / superscript
        sub = sup = ''
        k = i
        for _ in range(2):
            while k < n and math[k] in ' ':
                k += 1
            if k < n and math[k] == '_' and not sub:
                sub, k = read_arg(math, k + 1)
            elif k < n and math[k] == '^' and not sup:
                sup, k2 = read_arg(math, k + 1)
                if is_decoration_sup(sup, bool(sub)):
                    k = k2
                else:
                    sup = ''
                    break
            else:
                break
        full = key
        if sub:
            full += '_{%s}' % norm(sub)
        if sup:
            full += '^{%s}' % norm(sup)
        toks.append((key, full, start))
        # tokens inside the subscript are not separate symbols here
        i = k if sub or sup else i
    return toks


# ---------------------------------------------------- definition heuristic
CLAUSE_SEP = re.compile(r'(,|;|\\quad|\\qquad|&|\\\\|\\text\{[^}]*\}|'
                        r'\\begin\{[a-z*]+\}|\\end\{[a-z*]+\}|\\,|\\;|\\ )')
ASSIGN = re.compile(r'\s*(:=|\\coloneqq|=(?!:))')


def skip_args(math, j):
    """Skip a function argument list like (x,y) or (C,D;t) after a token."""
    while j < len(math) and math[j] == ' ':
        j += 1
    if j < len(math) and math[j] in '([':
        close = ')' if math[j] == '(' else ']'
        depth = 0
        for k in range(j, len(math)):
            if math[k] in '([':
                depth += 1
            elif math[k] in ')]':
                depth -= 1
                if depth == 0:
                    return k + 1
    if math.startswith('\\left(', j):
        e = math.find('\\right)', j)
        if e > 0:
            return e + 7
    return j


def token_end(math, start):
    """End offset of the token (with sub/superscript) starting at start."""
    toks = tokenize(math[start:])
    if not toks:
        return start + 1
    key, full, _ = toks[0]
    # recompute by re-reading: crude but adequate
    j = start
    m = CS.match(math, j)
    if m and (m.group(1) or '') in DECOR:
        _, j = read_arg(math, m.end())
    elif m:
        j = m.end()
    else:
        j += 1
    for _ in range(2):
        while j < len(math) and math[j] == ' ':
            j += 1
        if j < len(math) and math[j] in '_^':
            _, j2 = read_arg(math, j + 1)
            if math[j] == '^' and '^' not in full:
                break
            j = j2
    return j


def definitions_in(math, triggered):
    """Return list of (full, key, offset, rhs) candidate definitions."""
    out = []
    toks = tokenize(math)
    for key, full, off in toks:
        end = token_end(math, off)
        # explicit definition marks anywhere
        tail = math[end:]
        after_args = skip_args(math, end)
        tail2 = math[after_args:]
        m_def = re.match(r'\s*&?\s*(:=|\\coloneqq)', tail2)
        prev = math[:off]
        m_rev = re.search(r'(=:|\\eqqcolon)\s*$', prev)
        clause_start = True
        pm = prev.rstrip()
        if pm and not re.search(r'(,|;|\\quad|\\qquad|&|\\\\|\$|\{|\\[,;: ]|'
                                r'\\begin\{[a-z*]+\}|\\end\{[a-z*]+\}|'
                                r'\\text\{[^}]*\}|\\hbox\{[^}]*\}|'
                                r'\\label\{[^}]*\}|\\[a-z]+\*?\{[a-z*]+\})$', pm):
            clause_start = False
        if pm.endswith('{') and not re.search(r'\\begin\{[a-z*]+\}$', pm):
            clause_start = False  # inside a group, e.g. \frac{x}
        m_eq = re.match(r'\s*&?\s*=(?!:)', tail2)
        if m_def or m_rev or (triggered and clause_start and m_eq):
            rhs = re.split(r',\s|\\quad|\\qquad|\\\\', tail2.lstrip(' &'), maxsplit=1)[0]
            rhs = re.sub(r'\s+', ' ', rhs.strip())[:48]
            out.append((full, key, off, rhs))
    return out


# --------------------------------------------------------------- synctex
def synctex_pages(path, root):
    """Map (relfile, line) -> min page from a .synctex.gz file."""
    tags, pages = {}, {}
    page = 0
    rec = re.compile(r'^[x$](\d+),(\d+)[:(]')
    with gzip.open(path, 'rt', errors='replace') as fh:
        for raw in fh:
            if raw.startswith('Input:'):
                _, tag, p = raw.rstrip('\n').split(':', 2)
                p = p.replace('/./', '/')
                try:
                    rel = Path(p).resolve().relative_to(root.resolve()).as_posix()
                except ValueError:
                    rel = None
                tags[tag] = rel
            elif raw.startswith('{'):
                try:
                    page = int(raw[1:].strip())
                except ValueError:
                    pass
            else:
                m = rec.match(raw)
                if m and tags.get(m.group(1)):
                    k = (tags[m.group(1)], int(m.group(2)))
                    pages.setdefault(k, collections.Counter())[page] += 1
    # The output routine tags running heads, footers and footnotes with the
    # input line being read when a page is shipped; take the page holding
    # most of a line's glyphs (ties: the earlier page).
    return {k: min(c, key=lambda p: (-c[p], p)) for k, c in pages.items()}


def page_lookup(pages, f, line):
    if not pages:
        return ''
    if (f, line) in pages:
        return pages[(f, line)]
    for d in range(1, 7):          # a line without glyphs (e.g. \\begin{equation})
        if (f, line + d) in pages:  # is typeset with the lines that follow it
            return pages[(f, line + d)]
    for d in range(1, 60):
        if (f, line - d) in pages:
            return pages[(f, line - d)]
    return ''


# ----------------------------------------------------------- the analysis
class Doc:
    def __init__(self, name, root, pages=None):
        self.name, self.root = name, root
        self.lines = load_document(root)
        self.text, starts = flatten(self.lines)
        self.loc = Locator(starts)
        self.units = section_units(self.text)
        self.pages = pages or {}
        self.regions = math_regions(self.text)
        self._numbered_rows()
        self._scan()

    def where(self, pos):
        f, line = self.loc(pos)
        return f, line, unit_of(self.units, pos), page_lookup(self.pages, f, line)

    def _numbered_rows(self):
        """Map positions to equation numbers (rows of numbered displays)."""
        self.eqspans = []  # (start, end, numbers)
        number = 0
        pat = re.compile(r'\\begin\{(' + DISPLAYS + r')\}(.*?)\\end\{\1\}', re.S)
        for m in pat.finditer(self.text):
            body_start = m.start(2)
            body = m.group(2)
            env = m.group(1)
            rows, pos = [], 0
            if env == 'equation':
                parts = [(0, len(body))]
            else:
                parts, last = [], 0
                depth = 0
                for k in range(len(body)):
                    ch = body[k]
                    if body.startswith('\\begin{', k):
                        depth += 1
                    elif body.startswith('\\end{', k):
                        depth -= 1
                    if depth == 0 and body.startswith('\\\\', k):
                        parts.append((last, k)); last = k + 2
                parts.append((last, len(body)))
            env_numbers, row_numbers = [], []
            for a, b in parts:
                seg = body[a:b]
                if env == 'equation':
                    if '\\nonumber' in seg or '\\notag' in seg:
                        nums = []
                    else:
                        number += 1; nums = [number]
                else:
                    if '\\nonumber' in seg or '\\notag' in seg or not seg.strip():
                        nums = []
                    else:
                        number += 1; nums = [number]
                row_numbers.append((a, b, nums))
                env_numbers += nums
            for a, b, nums in row_numbers:
                self.eqspans.append((body_start + a, body_start + b,
                                     nums or env_numbers))
        self.eqspans.sort()

    def eq_numbers(self, pos):
        for a, b, nums in self.eqspans:
            if a <= pos < b:
                return nums
            if a > pos:
                break
        return []

    def _scan(self):
        self.occ = []      # (key, full, pos)
        self.defs = []     # (full, key, pos, rhs)
        text = self.text
        prev_end = 0
        for start, end, kind in self.regions:
            math = text[start:end]
            # prose context: from last sentence end before the region
            ctx_start = max(0, start - 400)
            ctx = text[ctx_start:start]
            # strip math from the context crudely
            ctx_plain = re.sub(r'\$[^$]*\$', ' M ', ctx)
            ends = list(SENTENCE_END.finditer(ctx_plain))
            sentence = ctx_plain[ends[-1].end():] if ends else ctx_plain
            sentence = re.sub(r'\\begin\{(equation|align|gather|multline)\*?\}', ' ', sentence)
            triggered = bool(TRIGGER.search(sentence))
            # 'where $X$ is / denotes' and 'Let $X$ be'
            after = text[end:end + 40]
            mword = re.match(r'\$?\s*(is|are|denotes|denote|be|stands)\b', after)
            weak = bool(re.search(r'\b(let|where|here|denote|call)\b', sentence, re.I))
            if kind == 'inline' and mword and (mword.group(1) in ('denotes', 'denote', 'stands', 'be') or weak):
                toks = tokenize(math)
                if 1 <= len(toks) <= 3 and '=' not in math:
                    for key, full, off in toks:
                        self.defs.append((full, key, start + off, '(prose: ' + re.sub(r'\s+', ' ', after.strip())[:30] + ')'))
            for key, full, off in tokenize(math):
                self.occ.append((key, full, start + off))
            for full, key, off, rhs in definitions_in(math, triggered):
                self.defs.append((full, key, start + off, rhs))
        self.defs.sort(key=lambda d: d[2])

    # -- reports
    def def_table(self):
        rows = []
        for full, key, pos, rhs in self.defs:
            f, line, unit, page = self.where(pos)
            rows.append(dict(doc=self.name, key=key, full=full, file=f,
                             line=line, page=page, unit=unit, rhs=rhs,
                             eq=','.join(map(str, self.eq_numbers(pos)))))
        return rows

    def occurrence_index(self):
        """key -> unit -> count, and key/full -> numbered eq set."""
        per_unit = collections.defaultdict(collections.Counter)
        eqs_key = collections.defaultdict(set)
        eqs_full = collections.defaultdict(set)
        for key, full, pos in self.occ:
            unit = unit_of(self.units, pos)
            per_unit[key][unit] += 1
            for e in self.eq_numbers(pos):
                eqs_key[key].add(e)
                eqs_full[full].add(e)
        return per_unit, eqs_key, eqs_full


def blocks(text, names):
    pattern = r'\\begin\{(' + names + r')\}.*?\\end\{\1\}'
    return [m.group() for m in re.finditer(pattern, text, re.S)]


def section_texts(root):
    return {p.name: p.read_text() for p in sorted((root / 'sections').glob('*.tex'))}


def apply_renames(text, fname, renames):
    for r in renames:
        files = r.get('files')
        if files and fname not in files:
            continue
        if r.get('regex'):
            text = re.sub(r['from'], r['to'], text)
        else:
            text = text.replace(r['from'], r['to'])
    return text


def check_blocks(paper_root, comp_root, repo, topic, baseline, renames):
    report, ok = [], True
    P, C = section_texts(paper_root), section_texts(comp_root)
    total = collections.Counter()
    for name in sorted(P):
        for names, kind in [(CLAIMS, 'statements'), (DISPLAYS, 'numbered displays')]:
            a, b = blocks(P[name], names), blocks(C.get(name, ''), names)
            total[kind] += len(a)
            if a != b:
                ok = False
                diff = [i for i, (x, y) in enumerate(zip(a, b)) if x != y]
                tags = [(re.findall(r'\\label\{([^}]+)\}', a[i]) or [f'#{i}'])[0] for i in diff]
                report.append(f'MISMATCH {name} {kind}: paper {len(a)} vs companion '
                              f'{len(b)} blocks; differing: {", ".join(tags)}')
    report.append(('PASS' if ok else 'FAIL') +
                  f': current paper vs current companion: {total["statements"]} '
                  f'statements, {total["numbered displays"]} numbered display blocks')
    if baseline:
        bok = True
        for name in sorted(P):
            rel = f'{topic}/paper/sections/{name}'
            try:
                old = subprocess.check_output(['git', 'show', f'{baseline}:{rel}'],
                                              cwd=repo, text=True)
            except subprocess.CalledProcessError:
                report.append(f'baseline: cannot read {rel}'); bok = False; continue
            for names, kind in [(CLAIMS, 'statements'), (DISPLAYS, 'numbered displays')]:
                exp = [apply_renames(x, name, renames) for x in blocks(old, names)]
                for label, cur in (('paper', P[name]), ('companion', C.get(name, ''))):
                    got = blocks(cur, names)
                    if exp != got:
                        bok = False
                        bad = [i for i, (x, y) in enumerate(zip(exp, got)) if x != y]
                        if len(exp) != len(got):
                            bad.append(min(len(exp), len(got)))
                        tags = [(re.findall(r'\\label\{([^}]+)\}', exp[i]) or [f'#{i}'])[0]
                                for i in bad if i < len(exp)]
                        report.append(f'RENAME-CHECK {label} {name} {kind}: '
                                      f'{len(bad)} blocks differ from baseline+renames: '
                                      f'{", ".join(tags)}')
        report.append(('PASS' if bok else 'FAIL') +
                      f': numbered blocks equal baseline {baseline[:12]} after '
                      f'{len(renames)} declared renames (both texts)')
        ok = ok and bok
    return ok, report


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--repo', default='.')
    ap.add_argument('--topic', default='topics/padua-argmax-bridge-20261105')
    ap.add_argument('--out', default='notation-out')
    ap.add_argument('--paper-synctex')
    ap.add_argument('--companion-synctex')
    ap.add_argument('--baseline-rev')
    ap.add_argument('--rename-map')
    ap.add_argument('--paper-dir', help='override the paper source directory')
    ap.add_argument('--companion-dir', help='override the companion source directory')
    ap.add_argument('--free', help='file with one proposed TeX name per line; '
                    'reports its occurrences (full token, base symbol, raw text) in both texts')
    ap.add_argument('--symbol', action='append', default=[],
                    help='print every occurrence unit and definition of KEY')
    args = ap.parse_args()
    repo = Path(args.repo).resolve()
    proot = Path(args.paper_dir).resolve() if args.paper_dir else repo / args.topic / 'paper'
    croot = Path(args.companion_dir).resolve() if args.companion_dir else repo / args.topic / 'companion-paper'
    out = Path(args.out); out.mkdir(parents=True, exist_ok=True)
    ppages = synctex_pages(args.paper_synctex, proot) if args.paper_synctex else {}
    cpages = synctex_pages(args.companion_synctex, croot) if args.companion_synctex else {}
    docs = [Doc('paper', proot, ppages), Doc('companion', croot, cpages)]
    summary = []
    for d in docs:
        rows = d.def_table()
        with open(out / f'definitions-{d.name}.tsv', 'w') as fh:
            cols = ['key', 'full', 'unit', 'file', 'line', 'page', 'eq', 'rhs']
            fh.write('\t'.join(cols) + '\n')
            for r in rows:
                fh.write('\t'.join(str(r[c]) for c in cols) + '\n')
        # (b) flags
        by_unit_full = collections.defaultdict(list)
        by_unit_key = collections.defaultdict(list)
        for r in rows:
            by_unit_full[(r['unit'], r['full'])].append(r)
            by_unit_key[(r['unit'], r['key'])].append(r)
        flags_full = {k: v for k, v in by_unit_full.items()
                      if len({x['line'] for x in v}) > 1}
        flags_key = {k: v for k, v in by_unit_key.items()
                     if len({x['full'] for x in v}) > 1}
        units_per_key = collections.defaultdict(set)
        for r in rows:
            units_per_key[r['key']].add(r['unit'])
        with open(out / f'flags-{d.name}.txt', 'w') as fh:
            fh.write('# same token, more than one definition site in one unit\n')
            for (u, full), v in sorted(flags_full.items()):
                sites = '; '.join(f"{x['file'].split('/')[-1]}:{x['line']}"
                                  f"(p{x['page']}) ={x['rhs']}" for x in v)
                fh.write(f'{u}\t{full}\t{sites}\n')
            fh.write('\n# same base letter, several decorated/subscripted tokens defined in one unit\n')
            for (u, key), v in sorted(flags_key.items()):
                toks = sorted({x['full'] for x in v})
                fh.write(f'{u}\t{key}\t{len(toks)}\t{" ".join(toks)}\n')
        per_unit, eqs_key, eqs_full = d.occurrence_index()
        with open(out / f'symbols-{d.name}.tsv', 'w') as fh:
            fh.write('key\toccurrences\tunits\tdef_sites\tdef_units\tnumbered_eqs\n')
            for key in sorted(per_unit, key=lambda k: -sum(per_unit[k].values())):
                ndef = sum(1 for r in rows if r['key'] == key)
                fh.write(f"{key}\t{sum(per_unit[key].values())}\t"
                         f"{' '.join(f'{u}:{c}' for u, c in sorted(per_unit[key].items()))}\t"
                         f"{ndef}\t{' '.join(sorted(units_per_key.get(key, [])))}\t"
                         f"{','.join(map(str, sorted(eqs_key.get(key, []))))}\n")
        with open(out / f'numbered-{d.name}.tsv', 'w') as fh:
            fh.write('full_token\tnumbered_eqs\n')
            for full in sorted(eqs_full):
                fh.write(f"{full}\t{','.join(map(str, sorted(eqs_full[full])))}\n")
        multi_units = {k for k, v in units_per_key.items() if len(v) > 1}
        summary.append(
            f'{d.name}: {len(d.lines)} lines, {len(d.regions)} math regions, '
            f'{len(d.occ)} symbol occurrences, {len(per_unit)} base symbols, '
            f'{len(rows)} candidate definition sites; '
            f'{len(flags_full)} (unit, token) pairs with >1 definition site; '
            f'{len(flags_key)} (unit, base) pairs with >1 defined token; '
            f'{len(multi_units)} base symbols defined in >1 unit; '
            f'{max(n for a, b, ns in d.eqspans for n in ns) if d.eqspans else 0} '
            f'numbered equations')
        for key in args.symbol:
            print(f'== {d.name} {key}')
            for r in rows:
                if r['key'] == key:
                    print(f"  def {r['unit']:5} {r['file'].split('/')[-1]}:{r['line']} "
                          f"p{r['page']} {r['full']} = {r['rhs']}  eq[{r['eq']}]")
            print('  units:', dict(sorted(per_unit.get(key, {}).items())))
            print('  numbered:', sorted(eqs_key.get(key, [])))
    if args.free:
        rows = []
        for raw in Path(args.free).read_text().split('\n'):
            name = raw.split('#')[0].strip()
            if not name:
                continue
            toks = tokenize(name)
            if not toks:
                continue
            key, full, _ = toks[0]
            cells = []
            for d in docs:
                nfull = sum(1 for k, f, p in d.occ if f == full)
                nkey = sum(1 for k, f, p in d.occ if k == key)
                nraw = d.text.count(name)
                cells.append(f'{d.name}: token {nfull}, base {nkey}, text {nraw}')
            rows.append(f'{name}\t{full}\t' + '\t'.join(cells))
        (out / 'free-check.tsv').write_text('\n'.join(rows) + '\n')
        print('\n'.join(rows))
    renames = json.loads(Path(args.rename_map).read_text()) if args.rename_map else []
    ok, rep = check_blocks(proot, croot, repo, args.topic, args.baseline_rev, renames)
    summary += rep
    (out / 'summary.txt').write_text('\n'.join(summary) + '\n')
    print('\n'.join(summary))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
