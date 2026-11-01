"""Allocate final IDs for the lattice-unisolvence and programme-ideas provisional records.

AC's explicit instruction of 2026-11-01 (session log in topics/programme-ideas-20261031/LOG.md):
"allocate this block now" for PR #6, and "are the lattice ids allocated now? if not, do that as well".

Run from repository root:  python3 -I topics/programme-ideas-20261031/pr-prep/allocate.py [--apply]

Without --apply it only builds and validates the map and prints it. With --apply it
writes the map, rewrites the two campaigns' rows in the shared registries and adds
"Final ID" lines to the canonical records. Provisional IDs are kept as provenance.

Order: lattice (merged in PR #4) first, then programme-ideas, each from the boundary
after the bivariate-Lanczos block (PD-T081, PD-N032, IDEA-177) and after the LIT-293–299
reservation of draft PR #11 (LIT-300).
"""
import argparse
import json
import re
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument('--apply', action='store_true')
args = ap.parse_args()

START = {'PD-T': 81, 'PD-N': 32, 'IDEA': 177, 'LIT': 300}
NS = ['PD-T', 'PD-N', 'IDEA', 'LIT']
TOPIC = Path('topics/programme-ideas-20261031')
LAT = json.loads(Path('topics/lattice-unisolvence-20261031/provisional-id-map.json').read_text())
LANCZOS = json.loads(Path('topics/bivariate-lanczos-20261031/pr-prep/id-map.json').read_text())['map']


def fmt(ns, n):
    return f'{ns}{n:03d}' if ns.startswith('PD') else f'{ns}-{n:03d}'


def lat_key(pid):
    m = re.fullmatch(r'(PD-[TN]|IDEA|LIT)\?lattice-(?:c(\d)-)?codex-(\d+)', pid)
    assert m, pid
    return (int(m[2] or 0), int(m[3]))


# --- provisional inventories -------------------------------------------------
lat = {ns: sorted([r['id'] for r in LAT['rows'] if r['id'].startswith(ns + '?')], key=lat_key) for ns in NS}
lat_path = {r['id']: r['path'] for r in LAT['rows']}
assert [len(lat[n]) for n in NS] == [14, 7, 13, 32], [len(lat[n]) for n in NS]

P = 'programme-ideas-claude'
pi_theory = {}
for p in sorted((TOPIC / 'theory').glob('*.md')):
    m = re.match(r'# (PD-[TN]\?' + P + r'-\d\d) ', p.read_text().splitlines()[0])
    assert m, p
    pi_theory[m[1]] = str(p)
pi = {'PD-T': sorted(k for k in pi_theory if k.startswith('PD-T')),
      'PD-N': sorted(k for k in pi_theory if k.startswith('PD-N')),
      'IDEA': [f'IDEA?{P}-{k:02d}' for k in range(1, 21)]}
merged = {}  # LIT rows merged into an existing ID (same statement)
for m in json.loads((TOPIC / 'lit/integration-map.json').read_text()):
    if m['relation'] == 'same':
        merged[m['id']] = m['existing_ids'][0]
for m in json.loads((TOPIC / 'lit/integration-map-pr10.json').read_text()):
    if m['relation_vs_pr10'] == 'same':
        merged[m['id']] = m['pr10_ids'][0]
base = [l.split('|')[1].strip() for l in (TOPIC / 'lit/baseline.md').read_text().splitlines()
        if l.startswith('| LIT?' + P)]
assert len(base) == 111 and len(merged) == 16
pi['LIT'] = [k for k in base if k not in merged]
assert [len(pi[n]) for n in NS] == [6, 5, 20, 95], [len(pi[n]) for n in NS]

# --- allocation -------------------------------------------------------------
M, blocks = {}, {}
for camp, inv in (('lattice-unisolvence', lat), ('programme-ideas', pi)):
    blocks[camp] = {}
    for ns in NS:
        lo = START[ns]
        for k in inv[ns]:
            M[k] = fmt(ns, START[ns])
            START[ns] += 1
        blocks[camp][ns] = [fmt(ns, lo), fmt(ns, START[ns] - 1), len(inv[ns])]
assert len(set(M.values())) == len(M) == 66 + 126
nxt = {ns: fmt(ns, START[ns]) for ns in NS}

# no collision with any ID already used in the shared registries
used = set()
for f in ['PROOF_STATUS.md', 'state/IDEAS.md', 'literature/INDEX.md', 'ID_CROSSWALK.md']:
    used |= set(re.findall(r'\b(?:PD-[TN]\d{3}|IDEA-\d{3}|LIT-\d{3})\b', Path(f).read_text()))
clash = sorted(set(M.values()) & used)
assert not clash, clash

out = {'authorisation': 'AC, 2026-11-01: "allocate this block now" (PR #6) and "are the lattice ids allocated now? if not, do that as well"',
       'boundary_used': {'PD-T': 'PD-T081', 'PD-N': 'PD-N032', 'IDEA': 'IDEA-177', 'LIT': 'LIT-300 (after draft PR #11 LIT-293-299)'},
       'blocks': blocks, 'next_unreserved': nxt, 'map': M,
       'merged_without_new_id': merged}
print(json.dumps({'blocks': blocks, 'next': nxt}, indent=1))
if not args.apply:
    raise SystemExit(0)
FINAL = {**M, **merged}

(TOPIC / 'pr-prep').mkdir(exist_ok=True)
(TOPIC / 'pr-prep/id-map.json').write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n')

SHORT = {'PD-T?…-301': LANCZOS['PD-T?bivariate-lanczos-claude-301'],
         'PD-T?…-304': LANCZOS['PD-T?bivariate-lanczos-claude-304'],
         'PD-N?…-02': M['PD-N?programme-ideas-claude-02']}
PROV = re.compile(r'(?:PD-[TN]|IDEA|LIT)\?(?:lattice-(?:c\d-)?codex|programme-ideas-claude)-\d+\b')
LZ = re.compile(r'(?:PD-[TN]|IDEA|LIT)\?bivariate-lanczos-claude-\d+\b')


def fin(m):
    return FINAL[m.group(0)]


def section(s, head):
    i = s.index(head)
    j = s.find('\n## ', i + 5)
    return i, (j if j > 0 else len(s))


def rewrite_block(f, head, newhead, first_cell, intro):
    s = Path(f).read_text()
    i, j = section(s, head)
    lines = s[i:j].split('\n')
    lines[0] = newhead
    for n, l in enumerate(lines):
        if l.startswith('| ') and PROV.match(l[2:]):
            cells = l.split(' | ')
            c0 = cells[0][2:]
            pid = PROV.match(c0).group(0)
            rest = ' | '.join(cells[1:])
            rest = PROV.sub(fin, rest)
            lines[n] = '| ' + first_cell(pid, c0) + ' | ' + rest
        elif not l.startswith('## '):
            lines[n] = PROV.sub(fin, l)
        for a, b in SHORT.items():
            lines[n] = lines[n].replace(a, b)
        lines[n] = LZ.sub(lambda m: LANCZOS[m.group(0)], lines[n])
    blk = '\n'.join(lines)
    blk = blk.replace(newhead + '\n', newhead + '\n\n' + intro + '\n', 1)
    Path(f).write_text(s[:i] + blk + s[j:])


def intro(camp):
    b = blocks[camp]
    return (f"**Final IDs allocated 2026-11-01** by Claude under AC's explicit authorisation, recorded in the "
            f"[batch ledger](topics/padua-batch-20261031/ALLOCATIONS.md): "
            + ', '.join(f'{b[ns][0]}–{b[ns][1]}' for ns in NS if b[ns][2])
            + ". Provisional IDs are kept in parentheses or as aliases for provenance; the full map is "
            "[id-map.json](topics/programme-ideas-20261031/pr-prep/id-map.json).")


for camp, tag in (('lattice-unisolvence', 'Lattice campaign'), ('programme-ideas', 'Programme-ideas campaign')):
    head = f'## {tag} — provisional registrations'
    nh = f'## {tag} — final allocation (2026-11-01)'
    rel = intro(camp)
    rewrite_block('PROOF_STATUS.md', head, nh, lambda p, c: FINAL[p] + ' (' + p + ')', rel)
    rewrite_block('state/IDEAS.md', head, nh, lambda p, c: FINAL[p] + '; ' + c, rel.replace('](topics/', '](../topics/'))
    rewrite_block('literature/INDEX.md', head, nh, lambda p, c: FINAL[p] + ' (' + p + ')',
                  rel.replace('](topics/', '](../topics/'))

# ID_CROSSWALK: fill the Final ID column; keep the provisional column and historical tables.
s = Path('ID_CROSSWALK.md').read_text()
for camp, tag in (('lattice-unisolvence', 'Lattice campaign'), ('programme-ideas', 'Programme-ideas campaign')):
    head = f'## {tag} — provisional registrations'
    i, j = section(s, head)
    lines = s[i:j].split('\n')
    lines[0] = f'## {tag} — final allocation (2026-11-01)'
    for n, l in enumerate(lines):
        m = re.match(r'\| (' + PROV.pattern + r') \| ([^|]*) \|(.*)$', l)
        if m:
            pid, cur, rest = m.group(1), m.group(2).strip(), m.group(3)
            new = cur if cur.startswith('Merged into') else FINAL[pid] + ' (allocated 2026-11-01, AC-authorised)'
            rest = rest.replace('[shared ledger](topics/padua-batch-20261031/ALLOCATIONS.md)',
                                '[shared ledger](topics/padua-batch-20261031/ALLOCATIONS.md); [id-map](topics/programme-ideas-20261031/pr-prep/id-map.json)')
            lines[n] = f'| {pid} | {new} |{rest}'
    blk = '\n'.join(lines).replace(lines[0] + '\n', lines[0] + '\n\n' + intro(camp) + '\n', 1)
    s = s[:i] + blk + s[j:]
Path('ID_CROSSWALK.md').write_text(s)

# Canonical records: a Final ID line after the heading (PD records), after each IDEA heading.
NOTE = ' (allocated 2026-11-01 under AC\'s authorisation; the provisional ID above and in the text is retained as provenance — see ID_CROSSWALK.md).'
pd_paths = {**{k: v for k, v in lat_path.items() if k.startswith('PD')}, **pi_theory}
for pid, path in pd_paths.items():
    p = Path(path)
    t = p.read_text().split('\n')
    assert not any(x.startswith('Final ID:') for x in t[:4]), path
    assert pid in t[0], (pid, path)
    p.write_text('\n'.join([t[0], '', f'Final ID: **{M[pid]}**' + NOTE] + t[1:]))
idea_files = {}
for k in lat['IDEA']:
    idea_files.setdefault(lat_path[k], []).append(k)
idea_files.setdefault(str(TOPIC / 'ideas/candidates.md'), []).extend(pi['IDEA'])
for path, ids in idea_files.items():
    p = Path(path)
    t = p.read_text().split('\n')
    out_l = []
    for l in t:
        out_l.append(l)
        m = re.match(r'#+ (IDEA\?[a-z0-9-]+-\d+) ', l)
        if m and m.group(1) in ids:
            out_l += ['', f'Final ID: **{M[m.group(1)]}**' + NOTE]
            ids.remove(m.group(1))
    assert not ids, (path, ids)
    p.write_text('\n'.join(out_l))
LITNOTE = ('\n> **Final IDs (2026-11-01).** The provisional LIT IDs in this file were allocated final IDs under AC\'s '
           'authorisation; see `{}` and ID_CROSSWALK.md. Rows merged into an existing statement have no new ID.\n')
for path in [TOPIC / 'lit/baseline.md', Path('literature/lattice-unisolvence/baseline.md')]:
    t = path.read_text().split('\n', 1)
    path.write_text(t[0] + '\n' + LITNOTE.format('topics/programme-ideas-20261031/pr-prep/id-map.json') + t[1])
print('applied')
