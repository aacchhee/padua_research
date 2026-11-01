"""Semantic checks for the bivariate-Lanczos integration (run from the repository root of a
checkout of the squash-integrated tree).  Prints a JSON report; exit code 1 on any failure.

Checks: (1) final IDs unique across PROOF_STATUS rows, IDEAS final tables and INDEX rows,
and no collision with main's reserved ranges; (2) every theory file of the track carries
exactly one Final ID line matching the map; (3) every map entry appears in ID_CROSSWALK;
(4) statuses in PROOF_STATUS equal the theory files' Overall status; (5) relative links in
the new registry rows resolve; (6) committed generated outputs of the topic within limits.
"""
import glob, json, os, re, sys

T = 'topics/bivariate-lanczos-20261031'
m = json.load(open(T + '/pr-prep/id-map.json'))
M, files = m['map'], m['theory_files']
fail, rep = [], {}

ps = open('PROOF_STATUS.md').read()
ps_ids = re.findall(r'^\| (PD-[TN]\d{3}) \|', ps, re.M)
dup = sorted({x for x in ps_ids if ps_ids.count(x) > 1})
rep['proof_status_rows'] = len(ps_ids); rep['proof_status_duplicates'] = dup
if dup: fail.append('duplicate PROOF_STATUS IDs')

ideas = open('state/IDEAS.md').read()
idea_ids = re.findall(r'^\| (IDEA-\d{3}) \|', ideas, re.M)
dup_i = sorted({x for x in idea_ids if idea_ids.count(x) > 1 and int(x[5:]) >= 77})
rep['idea_rows_final_block'] = sum(1 for x in idea_ids if int(x[5:]) >= 77); rep['idea_duplicates_in_block'] = dup_i
if dup_i: fail.append('duplicate IDEA IDs in block')

idx = open('literature/INDEX.md').read()
lit_ids = re.findall(r'^\| (LIT-\d{3})\b', idx, re.M)
dup_l = sorted({x for x in lit_ids if lit_ids.count(x) > 1})
rep['index_lit_rows'] = len(lit_ids); rep['index_duplicates'] = dup_l
if dup_l: fail.append('duplicate LIT IDs')

ours = set(M.values())
for x in ours:
    n = int(re.sub(r'\D', '', x))
    lo = {'PD-T': 29, 'PD-N': 7, 'IDEA': 77, 'LIT': 66}[re.match(r'(PD-T|PD-N|IDEA|LIT)', x).group(1)]
    if n < lo: fail.append(f'{x} inside main reserved range')

bad_hdr = []
for prov, f in files.items():
    s = open(f).read()
    k = re.findall(r'^Final ID: \*\*(PD-[TN]\d{3})\*\*', s, re.M)
    if k != [M[prov]]: bad_hdr.append(f)
rep['theory_files'] = len(files); rep['bad_final_id_headers'] = bad_hdr
if bad_hdr: fail.append('theory header mismatch')

cw = open('ID_CROSSWALK.md').read()
missing = [p for p in M if f'| {p} | {M[p]} |' not in cw]
rep['crosswalk_missing'] = missing[:10]; rep['crosswalk_missing_count'] = len(missing)
if missing: fail.append('crosswalk incomplete')

st_bad = []
for prov, f in files.items():
    s = open(f).read()
    st = re.search(r'Overall status:\s*\**([A-Z]+)', s).group(1)
    row = re.search(r'^\| ' + M[prov] + r' \| .*? \| ([A-Z]+) \|', ps, re.M)
    if not row or row.group(1) != st: st_bad.append((M[prov], st, row.group(1) if row else None))
rep['status_mismatch'] = st_bad
if st_bad: fail.append('status mismatch')

def links(path, start_marker):
    s = open(path).read()
    s = s[s.find(start_marker):] if start_marker in s else ''
    base = os.path.dirname(path)
    bad = []
    for l in re.findall(r'\]\(([^)#\s]+)\)', s):
        if l.startswith('http'): continue
        if not os.path.exists(os.path.normpath(os.path.join(base, l))): bad.append(l)
    return bad
bl = {}
for path, mark in (('PROOF_STATUS.md', '## Bivariate Lanczos track'), ('ID_CROSSWALK.md', '## Bivariate Lanczos campaign'),
                   ('state/IDEAS.md', '## Bivariate Lanczos campaign'), ('tracks/bivariate-lanczos/NEGATIVE_RESULTS.md', '# Negative'),
                   ('state/CURRENT.md', '[Bivariate-Lanczos campaign]'), ('PAPER_MAP.md', '## Bivariate Lanczos briefs')):
    b = links(path, mark)
    if b: bl[path] = sorted(set(b))[:10]
rep['broken_links'] = bl
if bl: fail.append('broken links')

gen = [f for f in glob.glob(T + '/**/*', recursive=True) if os.path.isfile(f) and re.search(r'/(logs|logs_[^/]*|analysis|audit-0\d)/', f)]
big = [f for f in gen if os.path.getsize(f) > 1_000_000]
rep['generated_files'] = len(gen); rep['generated_bytes'] = sum(os.path.getsize(f) for f in gen); rep['files_over_1MB'] = big
if big or rep['generated_bytes'] > 5_000_000: fail.append('size limits')

rep['failures'] = fail
print(json.dumps(rep, indent=1, ensure_ascii=False))
sys.exit(1 if fail else 0)
