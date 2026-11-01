"""Read-only audit03 registry/ledger identities; run from repository root."""
import datetime
import hashlib
import json
import subprocess
from pathlib import Path

def git(*args):
    return subprocess.check_output(['git', *args])

refs = {
    'main': '28aaa20861d08074b77efc74eaef75cdcb36234d',
    'PR15': 'c8849a89a601e0a56342d3d568086ab8abdbc4c0',
    'PR12': '7f226c1cec873fd8069feae1f4749f13d95f5c9d',
}
registry = ['PROOF_STATUS.md', 'state/IDEAS.md', 'literature/INDEX.md', 'ID_CROSSWALK.md']
out = {'purpose': 'Fresh union identities; no ID assignment or reservation',
       'generated_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
       'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
       'heads': {}}
for label, ref in refs.items():
    ledgers = [p for p in git('ls-tree', '-r', '--name-only', ref).decode().splitlines()
               if p.endswith('/ALLOCATIONS.md')]
    records = []
    for path in registry + ledgers:
        data = git('show', f'{ref}:{path}')
        records.append({'path': path, 'blob': git('rev-parse', f'{ref}:{path}').decode().strip(),
                        'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()})
    out['heads'][label] = {'sha': ref, 'complete_ledgers': ledgers, 'files': records}
ev = Path('topics/padua-lanczos-drift-20261101/evidence')
integration = json.loads((ev / 'audit-03-integration.json').read_text())
remote = json.loads((ev / 'audit-03-remote-state.json').read_text())
out['final_assignments_of_own_ranges'] = {
    label: value['final_assignments_of_reserved_ids']
    for label, value in integration['checks']['reserved_range_usage'].items()}
out['closed_unmerged'] = remote['closed_unmerged']
out['interpretation'] = (
    'Root read both complete ledgers at PR15 and inspected differences against main and PR12. '
    'Same owner/range copies are duplicate reservations; boundary prose is not allocation. '
    'PR12 and main have identical registry/ledger bytes; PR15 adds only its reservation crosswalk '
    'and local scan locator. Existing permanent ranges/gaps are preserved. '
    'All returned closed PRs are merged; no missing retired reservation was found. '
    'This audit does not declare readiness or allocate IDs; preparation must refresh again.')
out['pass'] = (integration['result'] == 'PASS' and not out['closed_unmerged']
               and all(not v for v in out['final_assignments_of_own_ranges'].values())
               and all(c['clean'] for c in integration['checks']['merge_tree_vs_open_prs'].values()))
(ev / 'audit-03-union-scan.json').write_text(json.dumps(out, indent=1) + '\n')
print(json.dumps({'pass': out['pass'], 'heads': refs}))
