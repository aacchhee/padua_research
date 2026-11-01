"""PR-preparation allocation for topic bivariate-lanczos-20261031.

Maps every provisional ID of the topic to a final repository ID (block authorised by AC
on 2026-11-01: Claude allocates as the next free ranges after main's reservations),
writes pr-prep/id-map.json, inserts a `Final ID:` line into every theory file, rewrites
the topic's literature-statement headings and index rows to final IDs (provisional kept
in parentheses), and generates registry rows (PROOF_STATUS, ID_CROSSWALK, IDEAS,
NEGATIVE_RESULTS) into pr-prep/*.rows.md for review before insertion.

Run from the repository root:  python3 -I topics/bivariate-lanczos-20261031/pr-prep/allocate.py [--apply]
Without --apply only the map and the row files are written (dry run).
"""
import glob, json, re, sys

APPLY = '--apply' in sys.argv
P = 'bivariate-lanczos-claude'
TOPIC = 'topics/bivariate-lanczos-20261031'
START = {'PD-T': 29, 'PD-N': 7, 'LIT': 66, 'IDEA': 77}   # next unreserved on main 9739a0c

def key(n):
    m = re.match(r'N?(\d+)$', n)
    return int(m.group(1))

# ---------- inventory ----------
theory = {}
for f in sorted(glob.glob('tracks/bivariate-lanczos/theory/*.md')):
    h = open(f).read().split('\n', 1)[0]
    m = re.search(r'(PD-[TN])\?' + P + r'-N?(\d+)', h)
    theory[(m.group(1), m.group(2))] = f
pdt = sorted([n for (ns, n) in theory if ns == 'PD-T'], key=key)
pdn = sorted([n for (ns, n) in theory if ns == 'PD-N'], key=key)

idea = set()
for f in glob.glob(TOPIC + '/directions/*/candidates.md'):
    idea |= set(re.findall(r'^#{2,3} IDEA\?' + P + r'-(\d{3})\b', open(f).read(), re.M))
idea |= set(re.findall(r'^\| IDEA\?' + P + r'-(0\d\d)\b', open(TOPIC + '/baseline-candidates.md').read(), re.M))
idea = sorted(idea, key=key)

idx = open('literature/INDEX.md').read()
lit = sorted(set(re.findall(r'^\| LIT\?' + P + r'-(\d{3})\b', idx, re.M)), key=key)

M = {}
for ns, seq in (('PD-T', pdt), ('PD-N', pdn), ('IDEA', idea), ('LIT', lit)):
    for i, n in enumerate(seq):
        width = 3
        M[f'{ns}?{P}-{n}'] = f'{ns}{"-" if ns in ("LIT","IDEA") else ""}{START[ns]+i:0{width}d}'
counts = {ns: len(seq) for ns, seq in (('PD-T', pdt), ('PD-N', pdn), ('IDEA', idea), ('LIT', lit))}
ranges = {ns: (START[ns], START[ns] + counts[ns] - 1) for ns in counts}
json.dump({'block_start': START, 'counts': counts, 'ranges': ranges, 'map': M,
           'theory_files': {f'{ns}?{P}-{n}': f for (ns, n), f in theory.items()}},
          open(TOPIC + '/pr-prep/id-map.json', 'w'), indent=1, ensure_ascii=False)
print(counts, ranges)

def fin(ns, n):
    return M.get(f'{ns}?{P}-{n}')

REF = re.compile(r'(PD-T|PD-N|IDEA|LIT)\?(?:' + P + r'|…)-N?(\d{3})')
def finals_in(text, ns_allowed=('PD-T', 'PD-N', 'LIT')):
    out = []
    for ns, n in REF.findall(text):
        if ns in ns_allowed:
            f = fin(ns, n)
            if f and f not in out:
                out.append(f)
    return out

def section(s, title):
    m = re.search(r'^## ' + re.escape(title) + r'.*?$(.*?)(?=^## |\Z)', s, re.M | re.S)
    return m.group(1).strip() if m else ''

def finalize(t):
    return REF.sub(lambda m: (fin(m.group(1), m.group(2)) or m.group(0)), t)

def cell(t, n=220):
    t = finalize(' '.join(t.split()).replace('|', '/'))
    return t if len(t) <= n else t[:n - 1] + '…'

# ---------- registry rows ----------
ps_rows, cw_rows, neg_rows = [], [], []
for (ns, n), f in sorted(theory.items(), key=lambda kv: (kv[0][0], key(kv[0][1]))):
    s = open(f).read()
    title = s.split('\n', 1)[0].split('—', 1)[-1].strip()
    st = re.search(r'Overall status:\s*\**([A-Z]+)', s).group(1)
    disp = re.search(r'Candidate / claim disposition:\s*(.*)', s)
    disp = cell(disp.group(1), 160) if disp and disp.group(1).strip() not in ('', 'none', 'none.', '—') else 'none'
    parts = []
    sp = section(s, 'Status by part')
    for line in sp.split('\n'):
        if line.startswith('|') and not line.startswith('|---') and 'Mathematical part' not in line:
            c = [x.strip() for x in line.strip().strip('|').split('|')]
            if len(c) >= 2:
                parts.append(f'{cell(c[0], 50)}: {c[1]}')
    deps = finals_in(section(s, 'Depends on'))
    final = fin(ns, n)
    rel = '../' * 0 + f
    ps_rows.append(f'| {final} | {cell(title, 200)} | {st} | {cell("; ".join(parts), 260) or "—"} | {disp} | {", ".join(d for d in deps if d != final) or "—"} | [{f.split("/")[-1]}]({f}) | bivariate-lanczos audits 01–03 (Codex); Claude reconstructions in topic reviews/ |')
    cw_rows.append(f'| {ns}?{P}-{n} | {final} | claude/bivariate-lanczos-20261031; PR preparation 2026-11-01 | [{f}]({f}) | bivariate-lanczos PR (Claude-allocated block, AC 2026-11-01) |')
    if ns == 'PD-N':
        scope = section(s, 'Negative-result scope (PD-N only)') or section(s, 'Scope')
        neg_rows.append(f'| {final} ({ns}?{P}-{n}) | {cell(title, 140)} | {cell(scope, 220)} | {st} | [{f.split("/")[-1]}](theory/{f.split("/")[-1]}) |')

# IDEA rows (final registration in state/IDEAS.md)
idea_rows = []
src = {}
for f in glob.glob(TOPIC + '/directions/*/candidates.md'):
    s = open(f).read()
    for m in re.finditer(r'^#{2,3} IDEA\?' + P + r'-(\d{3})\b\s*—\s*(.*)$', s, re.M):
        n = m.group(1)
        body = s[m.end():]
        nxt = re.search(r'^#{2,3} ', body, re.M)
        body = body[:nxt.start()] if nxt else body
        d = re.search(r'^- Disposition[^:]*:\s*(.*)$', body, re.M)
        src[n] = (m.group(2).strip(), cell(d.group(1), 180) if d else 'see record', f)
bc = open(TOPIC + '/baseline-candidates.md').read()
for m in re.finditer(r'^\| IDEA\?' + P + r'-(0\d\d) \| ([^|]*)\|(.*)$', bc, re.M):
    n = m.group(1)
    if n not in src:
        src[n] = (cell(m.group(2), 120), 'Step 0 seed; campaign disposition in the seed table', TOPIC + '/baseline-candidates.md')
for n in idea:
    t, d, f = src[n]
    idea_rows.append(f'| {fin("IDEA", n)} | IDEA?{P}-{n} | {cell(t, 150)} | {d} | [{f.split("/")[-2] + "/" + f.split("/")[-1]}](../{f}) |')
    cw_rows.append(f'| IDEA?{P}-{n} | {fin("IDEA", n)} | claude/bivariate-lanczos-20261031; PR preparation 2026-11-01 | [{f}]({f}) | bivariate-lanczos PR (Claude-allocated block, AC 2026-11-01) |')
for n in lit:
    rec = re.search(r'^\| LIT\?' + P + r'-' + n + r' \|.*?\| ([a-z0-9-]+) \|', idx, re.M)
    k = rec.group(1) if rec else '?'
    cw_rows.append(f'| LIT?{P}-{n} | {fin("LIT", n)} | claude/bivariate-lanczos-20261031; PR preparation 2026-11-01 | [literature/records/{k}.md](literature/records/{k}.md) | bivariate-lanczos PR (Claude-allocated block, AC 2026-11-01) |')

for name, rows in (('proof_status', ps_rows), ('crosswalk', cw_rows), ('ideas', idea_rows), ('negative', neg_rows)):
    open(f'{TOPIC}/pr-prep/{name}.rows.md', 'w').write('\n'.join(rows) + '\n')
print({k: len(v) for k, v in (('ps', ps_rows), ('cw', cw_rows), ('idea', idea_rows), ('neg', neg_rows))})

if not APPLY:
    sys.exit(0)

# ---------- apply: theory headers ----------
for (ns, n), f in theory.items():
    s = open(f).read()
    if '\nFinal ID: ' in s.split('\n\n', 1)[0] + '\n':
        continue
    first, rest = s.split('\n', 1)
    s = first + f'\n\nFinal ID: **{fin(ns, n)}** (allocated at PR preparation, 2026-11-01; the provisional ID above and in the text is retained as provenance — see ID_CROSSWALK.md).\n' + rest
    open(f, 'w').write(s)

# ---------- apply: literature headings and index rows ----------
def litsub(text, heading_only):
    def r(m):
        f = fin('LIT', m.group(2))
        return f'{m.group(1)}{f} (LIT?{P}-{m.group(2)})' if f else m.group(0)
    if heading_only:
        return re.sub(r'^(#{2,4} )LIT\?' + P + r'-(\d{3})\b', r, text, flags=re.M)
    return re.sub(r'^(\| )LIT\?' + P + r'-(\d{3})\b', r, text, flags=re.M)
for f in glob.glob('literature/records/*.md'):
    s = open(f).read(); t = litsub(s, True)
    if t != s:
        open(f, 'w').write(t)
open('literature/INDEX.md', 'w').write(litsub(idx, False))
print('applied')
