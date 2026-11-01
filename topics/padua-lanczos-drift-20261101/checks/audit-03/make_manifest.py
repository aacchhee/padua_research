"""Pin audit03 inputs/outputs and count conservative campaign bytes."""
import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path.cwd()
TOPIC = 'topics/padua-lanczos-drift-20261101/'
OUT = TOPIC + 'checks/audit-03/manifest.json'
MAIN = '28aaa20861d08074b77efc74eaef75cdcb36234d'
CANDIDATE = 'ea829d92d509f79326a1cc037844a1bac3b4de13'
START = '1df5f89fe52f62c49d5addd58dcfea7246c5a688'

def git(*args):
    return subprocess.check_output(['git', *args])

def identity(path, data):
    return {'path': path, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}

changed = git('diff', '--name-only', START, CANDIDATE).decode().splitlines()
inputs = [identity(p, git('show', f'{CANDIDATE}:{p}')) for p in changed]
paths = sorted(set(git('ls-files', '--cached', '--others', '--exclude-standard').decode().splitlines()))
outputs = [p for p in paths if p != OUT and (
    p.startswith(TOPIC + 'checks/audit-03/') or
    p.startswith(TOPIC + 'evidence/audit-03-') or
    p in [TOPIC + 'audit-03.md', TOPIC + 'LOG.md', 'results/padua-lanczos-drift-20261101.md'])]
main_paths = set(git('ls-tree', '-r', '--name-only', MAIN).decode().splitlines())
own = [p for p in paths if p != OUT and p not in main_paths and (
    p.startswith(TOPIC) or p.startswith('tracks/bivariate-lanczos/code/drift/') or
    p.startswith('tracks/bivariate-lanczos/theory/drift-codex-') or
    p == 'results/padua-lanczos-drift-20261101.md')]
sizes = [(p, (ROOT / p).stat().st_size) for p in own]
record = {
    'auditor': 'Codex; requested/configured gpt-6-astra xhigh; resolved runtime metadata unexposed',
    'rules_head': 'c8849a89a601e0a56342d3d568086ab8abdbc4c0',
    'candidate': CANDIDATE, 'response_start': START, 'main': MAIN,
    'candidate_changed_inputs': inputs,
    'audit_output_files_excluding_this_manifest': [identity(p, (ROOT / p).read_bytes()) for p in outputs],
    'conservative_campaign_inventory': {
        'definition': 'All own new files versus main, including prose/code/results; excludes this manifest itself',
        'files_excluding_this_manifest': len(sizes),
        'bytes_excluding_this_manifest': sum(n for _, n in sizes),
        'largest_file': max(sizes, key=lambda pair: pair[1]),
        'per_file_limit_decimal': 1000000, 'total_limit_decimal': 5000000,
        'handoff_publication_note': 'Next handoff adds only compact prose/status; final publication count is checked separately.',
    },
    'frozen_history': 'Previous audits/responses/checks/evidence unchanged; see protocol receipt.',
    'commands': 'python3 topics/padua-lanczos-drift-20261101/checks/audit-03/make_manifest.py',
}
Path(OUT).write_text(json.dumps(record, indent=1) + '\n')
total = sum(n for _, n in sizes) + Path(OUT).stat().st_size
assert total < 5000000 and max(n for _, n in sizes) < 1000000
print(json.dumps({'campaign_files': len(sizes) + 1, 'campaign_bytes': total,
                  'largest_file': record['conservative_campaign_inventory']['largest_file'],
                  'manifest_bytes': Path(OUT).stat().st_size, 'pass': True}))
