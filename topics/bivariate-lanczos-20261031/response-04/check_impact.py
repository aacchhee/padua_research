"""Check the exact integration repair; preserve science, IDs and frozen audits."""
from pathlib import Path
import hashlib
import json
import re
import subprocess

BASE = '183d33760e8d6c3ecdeb588576bd65ba312f65fe'
CANDIDATE = '98945cbcf10c4f8eb53f77c996db358392d42391'
MAIN = '9739a0c56b7a3976422ce60a8441bfbbfd6554df'
TOPIC = 'topics/bivariate-lanczos-20261031'
TRACK = 'tracks/bivariate-lanczos'
ROOT = Path(__file__).resolve().parents[3]

def git(*args):
    return subprocess.check_output(['git', '-C', str(ROOT), *args])

def blob(rev, p):
    return git('show', rev + ':' + p)

def files(rev, *paths):
    return git('ls-tree', '-r', '--name-only', rev, *paths).decode().splitlines()

changed = git('diff', '--name-only', BASE, CANDIDATE).decode().splitlines()
frozen = []
exceptions = {TOPIC + '/report.md', TRACK + '/README.md', TRACK + '/NEGATIVE_RESULTS.md'}
for p in files(BASE, TOPIC, TRACK):
    if p in exceptions or p.startswith(TOPIC + '/pr-prep/'):
        continue
    assert blob(BASE, p) == blob(CANDIDATE, p), p
    frozen.append(p)
theory = files(BASE, TRACK + '/theory')
code = files(BASE, TRACK + '/code')
assert len(theory) == 77 and len(code) == 139
assert files(CANDIDATE, TRACK + '/theory') == theory
assert files(CANDIDATE, TRACK + '/code') == code
for p in ('AGENTS.md', 'agents/WORKFLOW.md', 'agents/codex/CODEX.md', TOPIC + '/pr-prep/id-map.json'):
    assert blob(BASE, p) == blob(CANDIDATE, p), p

m = json.loads(blob(CANDIDATE, TOPIC + '/pr-prep/id-map.json'))['map']
assert len(m) == len(set(m.values())) == 404
ps = blob(CANDIDATE, 'PROOF_STATUS.md').decode()
counts = {}
for p in theory:
    s = blob(CANDIDATE, p).decode()
    fid = re.search(r'^Final ID: \*\*(PD-[TN]\d+)\*\*', s, re.M)[1]
    st = re.search(r'Overall status:\s*\**([A-Z]+)', s)[1]
    assert re.search(r'^\| ' + fid + r' \| .*? \| ' + st + r' \|', ps, re.M), fid
    counts[st] = counts.get(st, 0) + 1
for p in ('PROOF_STATUS.md', 'ID_CROSSWALK.md', 'state/IDEAS.md', 'literature/INDEX.md'):
    now = blob(CANDIDATE, p).decode().splitlines()
    assert all(l in now for l in blob(MAIN, p).decode().splitlines() if l.startswith('|')), p
ids = lambda s: re.findall(r'^\| ((?:PD-[TN]|IDEA|LIT)\?[^|]+) \| ((?:PD-[TN]|IDEA-|LIT-)\d+) \|', s, re.M)
assert ids(blob(BASE, 'ID_CROSSWALK.md').decode()) == ids(blob(CANDIDATE, 'ID_CROSSWALK.md').decode())
negative = blob(CANDIDATE, TOPIC + '/pr-prep/negative.rows.md').decode().strip()
assert negative in blob(CANDIDATE, TRACK + '/NEGATIVE_RESULTS.md').decode()
result = {
    'base': BASE, 'candidate': CANDIDATE, 'main': MAIN,
    'protected_topic_track_files_byte_identical': len(frozen),
    'theory_files_byte_identical': len(theory), 'code_files_byte_identical': len(code),
    'rules_byte_identical': True, 'allocation_map_bytes_identical': True,
    'crosswalk_id_pairs_identical': True, 'main_table_rows_preserved': True,
    'negative_artifact_and_published_table_synchronized': True,
    'status_counts': counts,
    'changed_files': [{'path': p, 'bytes': len(blob(CANDIDATE, p)),
                       'sha256': hashlib.sha256(blob(CANDIDATE, p)).hexdigest()} for p in changed],
    'pass': True,
}
print(json.dumps(result, indent=2))
