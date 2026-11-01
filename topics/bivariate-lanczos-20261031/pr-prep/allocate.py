"""Regenerate the frozen AC-authorized bivariate-Lanczos allocation package.

Run from repository root: python3 -I topics/bivariate-lanczos-20261031/pr-prep/allocate.py [--apply | --check]
id-map.json is immutable input: IDs are never reassigned. Provisional and finalized
literature rows are accepted. Default writes four *.rows.md files for review;
--apply also adds missing headers and finalizes literature; --check writes nothing.
All source, inventory, header and map validation precedes writes. Shared registries
are integrated separately. Explicit reviewed semantics replace first-line parsing.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path

P = 'bivariate-lanczos-claude'
TOPIC = Path('topics/bivariate-lanczos-20261031')
PREP = TOPIC / 'pr-prep'
EXPECTED = {'PD-T': (29, 80), 'PD-N': (7, 31), 'IDEA': (77, 176), 'LIT': (66, 292)}
parser = argparse.ArgumentParser(description=__doc__)
mode = parser.add_mutually_exclusive_group()
mode.add_argument('--apply', action='store_true')
mode.add_argument('--check', action='store_true')
args = parser.parse_args()

def require(ok, message):
    if not ok:
        raise SystemExit('Refusing to write: ' + message)

def read(path):
    return Path(path).read_text(encoding='utf-8')

def splitrow(line):
    return [x.strip() for x in re.split(r'(?<!\\)\|', line.strip())[1:-1]]

def source_body(s):
    return re.sub(r'\n\nFinal ID:[^\n]*\n', '\n', s, count=1)

data = json.loads(read(PREP / 'id-map.json'))
M = data['map']
sem = json.loads(read(PREP / 'registry-semantics.json'))
require(hashlib.sha256((PREP / 'id-map.json').read_bytes()).hexdigest() == sem['allocation_sha256'],
        'allocation bytes differ from the reviewed immutable map')
require(len(M) == 404 and len(set(M.values())) == 404, 'map must retain 404 unique final IDs')
for ns, (lo, hi) in EXPECTED.items():
    values = {v for k, v in M.items() if k.startswith(ns + '?')}
    desired = {f'{ns}{"-" if ns in ("IDEA", "LIT") else ""}{n:03}' for n in range(lo, hi + 1)}
    require(values == desired, 'changed allocation range ' + ns)
    require(data['counts'][ns] == len(desired), 'incorrect count ' + ns)
    require(data['ranges'][ns] == [lo, hi], 'incorrect range metadata ' + ns)
    require(data['block_start'][ns] == lo, 'incorrect block start ' + ns)

theory = {}
for path in sorted(Path('tracks/bivariate-lanczos/theory').glob('*.md')):
    s = read(path)
    m = re.search(r'(PD-[TN])\?' + P + r'-N?(\d{3})', s.splitlines()[0])
    require(m is not None, 'unrecognized theory heading: ' + str(path))
    prov = f'{m[1]}?{P}-{m[2]}'
    require(prov not in theory, 'duplicate theory ID ' + prov)
    theory[prov] = str(path)
    require(prov in M, 'unallocated theory ' + prov)
    headers = re.findall(r'^Final ID:.*$', s, re.M)
    require(not headers or (len(headers) == 1 and re.match(r'^Final ID: \*\*' + M[prov] + r'\*\*', headers[0])),
            'duplicate or mismatched Final ID header: ' + str(path))
require(theory == data['theory_files'], 'theory inventory differs from frozen map')

idea = {}
for path in sorted((TOPIC / 'directions').glob('*/candidates.md')):
    for m in re.finditer(r'^#{2,3} IDEA\?' + P + r'-(\d{3})\b\s*—\s*(.*)$', read(path), re.M):
        require(m[1] not in idea, 'duplicate candidate heading ' + m[1])
        idea[m[1]] = (m[2], str(path))
for line in read(TOPIC / 'baseline-candidates.md').splitlines():
    m = re.match(r'^\| IDEA\?' + P + r'-(0\d\d)\b', line)
    if m:
        require(m[1] not in idea, 'duplicate seed/candidate ' + m[1])
        idea[m[1]] = (splitrow(line)[1], str(TOPIC / 'baseline-candidates.md'))
require({f'IDEA?{P}-{n}' for n in idea} == {p for p in M if p.startswith('IDEA?')}, 'IDEA inventory differs from map')
require(set(sem['idea_dispositions']) == set(idea), 'explicit disposition inventory incomplete')
require(set(sem['dependencies']) == {M[p] for p in theory}, 'explicit dependency inventory incomplete')
for fid, entry in sem['dependencies'].items():
    require(len(entry['ids']) == len(set(entry['ids'])), 'duplicate dependency in ' + fid)
    require(all(v in M.values() and v != fid for v in entry['ids']), 'invalid dependency in ' + fid)
for path, expected_hash in sem['source_sha256'].items():
    actual = hashlib.sha256(source_body(read(path)).encode('utf-8')).hexdigest()
    require(actual == expected_hash, 'scientific source changed; review explicit semantics: ' + path)

idx = read('literature/INDEX.md')
lit = {}
for line in idx.splitlines():
    if not line.startswith('| '):
        continue
    cells = splitrow(line)
    if not cells:
        continue
    m = re.search(r'LIT\?' + P + r'-(\d{3})', cells[0])
    if m:
        n = m[1]
        require(n not in lit, 'duplicate literature alias ' + n)
        prov = f'LIT?{P}-{n}'
        require(prov in M, 'unallocated literature alias ' + prov)
        final = re.match(r'LIT-\d{3}', cells[0])
        require(not final or final[0] == M[prov], 'changed literature allocation ' + prov)
        record = re.search(r'\b(records/[a-z0-9-]+\.md)\b', line)
        require(record is not None, 'missing literature record link ' + prov)
        path = 'literature/' + record[1]
        require(Path(path).is_file(), 'missing literature record ' + path)
        lit[n] = path
require({f'LIT?{P}-{n}' for n in lit} == {p for p in M if p.startswith('LIT?')}, 'literature inventory differs from map')

REF = re.compile(r'(PD-T|PD-N|IDEA|LIT)\?(?:' + P + r'|…|\.\.\.)-N?(\d{3})')
CONT = re.compile(r'((?:(?:\([a-z0-9′,– -]+\)|[–-]\([a-z0-9′]+\)))*)' r'(\s*[,/]\s*)-?N?(\d{3})(?!\d)')
def finalize(text):
    """Resolve explicit IDs and adjacent comma/slash lists; never guess other numbers."""
    pieces, end = [], 0
    for m in REF.finditer(text):
        if m.start() < end:
            continue
        pieces.append(text[end:m.start()])
        ns = m[1]
        key = f'{ns}?{P}-{m[2]}'
        require(key in M, 'unknown provisional reference ' + key)
        pieces.append(M[key]); end = m.end()
        while (tail := CONT.match(text, end)):
            key = f'{ns}?{P}-{tail[3]}'
            require(key in M, 'unknown contextual reference ' + key)
            pieces.append(tail[1] + tail[2] + M[key]); end = tail.end()
    pieces.append(text[end:])
    return ''.join(pieces)

def cell(text, limit=None):
    text = finalize(' '.join(text.split()))
    text = re.sub(r'(?<!\\)\|', r'\\|', text)
    return text[:limit - 1] + '…' if limit and len(text) > limit else text

def section(s, name):
    m = re.search(r'^## ' + re.escape(name) + r'[^\n]*\n(.*?)(?=^## |\Z)', s, re.M | re.S)
    return m[1].strip() if m else ''

ps_rows, cw_rows, neg_rows = [], [], []
for prov, path in sorted(theory.items(), key=lambda kv: M[kv[0]]):
    s = read(path); fid = M[prov]
    override = sem['proof_status_overrides'].get(fid, {})
    title = override.get('title', s.splitlines()[0].split('—', 1)[-1].strip())
    st = re.search(r'Overall status:\s*\**([A-Z]+)', s)
    require(st is not None and st[1] in ('PROVED', 'PARTIAL', 'CONDITIONAL', 'MEASURED', 'OPEN'), 'invalid status ' + prov)
    d = re.search(r'^Candidate / claim disposition:[ \t]*(.*)$', s, re.M)
    disp = override.get('disposition', d[1] if d and d[1].strip() not in ('', 'none', 'none.', '—') else 'none')
    parts = []
    for line in (section(s, 'Status by part') or section(s, 'Statement status')).splitlines():
        c = splitrow(line) if line.startswith('|') else []
        if len(c) >= 2 and c[1] != 'Status' and not set(c[0]) <= set('-: '):
            parts.append(c[0] + ': ' + c[1])
    parts_text = override.get('parts', '; '.join(parts) or '—')
    parts_text = parts_text.replace('uses 303(f)', 'uses PD-T059(f)')
    entry = sem['dependencies'][fid]
    # Keep nondependency IDs out of this column: consumers may build a graph from it.
    # Detailed exclusions and source rationale remain in registry-semantics.json.
    deps = ', '.join(entry['ids']) if entry['ids'] else 'none'
    if entry.get('qualifier'):
        deps += ' (' + entry['qualifier'] + ')'
    ps_rows.append(f'| {fid} | {cell(title)} | {st[1]} | {cell(parts_text)} | {cell(disp)} | {cell(deps)} | [{Path(path).name}]({path}) | bivariate-lanczos audits 01–03 (Codex); registry integration response to audit-04, independent review pending |')
    cw_rows.append(f'| {prov} | {fid} | claude/bivariate-lanczos-20261031; PR preparation 2026-11-01 | [{path}]({path}) | bivariate-lanczos PR (Claude-allocated block, AC 2026-11-01) |')
    if prov.startswith('PD-N?'):
        scope = section(s, 'Negative-result scope (PD-N only)') or section(s, 'Scope')
        neg_rows.append(f'| {fid} ({prov}) | {cell(title)} | {cell(scope)} | {st[1]} | [{Path(path).name}](theory/{Path(path).name}) |')

idea_rows = []
for n, (title, path) in sorted(idea.items()):
    prov = f'IDEA?{P}-{n}'
    disp = sem['idea_dispositions'][n]
    require(disp and disp not in ('pending.', 'see record'), 'placeholder disposition ' + prov)
    idea_rows.append(f'| {M[prov]} | {prov} | {cell(title)} | {cell(disp)} | [{Path(path).parent.name}/{Path(path).name}](../{path}) |')
    cw_rows.append(f'| {prov} | {M[prov]} | claude/bivariate-lanczos-20261031; PR preparation 2026-11-01 | [{path}]({path}) | bivariate-lanczos PR (Claude-allocated block, AC 2026-11-01) |')
for n, path in sorted(lit.items()):
    prov = f'LIT?{P}-{n}'
    cw_rows.append(f'| {prov} | {M[prov]} | claude/bivariate-lanczos-20261031; PR preparation 2026-11-01 | [{path}]({path}) | bivariate-lanczos PR (Claude-allocated block, AC 2026-11-01) |')

outputs = {PREP / (name + '.rows.md'): '\n'.join(rows) + '\n'
           for name, rows in [('proof_status', ps_rows), ('crosswalk', cw_rows), ('ideas', idea_rows), ('negative', neg_rows)]}
if args.apply:
    for prov, path in theory.items():
        s = read(path)
        if re.search(r'^Final ID:', s, re.M):
            continue  # already validated exactly one correct allocation header
        first, rest = s.split('\n', 1)
        outputs[Path(path)] = first + f'\n\nFinal ID: **{M[prov]}** (allocated at PR preparation, 2026-11-01; the provisional ID above and in the text is retained as provenance — see ID_CROSSWALK.md).\n' + rest
    def litsub(text, heading):
        pat = (r'^(#{2,4} )' if heading else r'^(\| )') + r'LIT\?' + P + r'-(\d{3})\b'
        return re.sub(pat, lambda m: m[1] + M[f'LIT?{P}-{m[2]}'] + f' (LIT?{P}-{m[2]})', text, flags=re.M)
    for path in Path('literature/records').glob('*.md'):
        s = read(path); t = litsub(s, True)
        if s != t:
            outputs[path] = t
    new_idx = litsub(idx, False)
    if new_idx != idx:
        outputs[Path('literature/INDEX.md')] = new_idx

# Validate the complete output package before changing any file.
require(len(cw_rows) == 404 and len(ps_rows) == 77 and len(idea_rows) == 100 and len(neg_rows) == 25, 'incorrect output cardinality')
require(not REF.search('\n'.join(ps_rows)), 'unconverted provisional reference in theory rows')
if not args.check:
    for path, content in outputs.items():
        if not path.exists() or read(path) != content:
            path.write_text(content, encoding='utf-8')
print(json.dumps({'map_entries': len(M), 'theory_headers_validated': len(theory),
                  'idea_dispositions': len(idea_rows), 'forward_dependency_rows': len(ps_rows),
                  'literature_aliases': len(lit), 'crosswalk_rows': len(cw_rows),
                  'mode': 'check' if args.check else 'apply' if args.apply else 'rows',
                  'map_reassigned': False}, sort_keys=True))
