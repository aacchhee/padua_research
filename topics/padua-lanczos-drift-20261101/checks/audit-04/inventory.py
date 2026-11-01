"""Read-only response03 preservation, pins and conservative audit04 inventory."""
import hashlib
import json
import subprocess
from pathlib import Path

T = 'topics/padua-lanczos-drift-20261101/'
OLD = '3cca9b929ac006a5ed4295b3beba909dfd602271'
CANDIDATE = '02bd97b892ed409ec64e9b281130c71a85e914e9'
READ = '39b3c5d8690566ce461e6e3a0a628e772a695dbc'
MAIN = '28aaa20861d08074b77efc74eaef75cdcb36234d'
PR12 = '0dd4a6df2db4a2019541604bb97c05926ab3c22b'
OUT = T+'evidence/audit-04-inventory.json'

def git(*args):
    return subprocess.check_output(['git', *args])

def identity(path, data):
    return {'path': path, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}

def own(path):
    return (path.startswith(T) or path.startswith('tracks/bivariate-lanczos/code/drift/')
            or path.startswith('tracks/bivariate-lanczos/theory/drift-codex-')
            or path == 'results/padua-lanczos-drift-20261101.md')

changed = git('diff','--name-only',OLD,CANDIDATE).decode().splitlines()
expected = {T+'LOG.md', T+'response-03.md', T+'ideas-e3-e4.md',
            T+'evidence/response-03-e1-regeneration-check.json',
            'results/padua-lanczos-drift-20261101.md',
            'tracks/bivariate-lanczos/code/drift/README.md',
            'tracks/bivariate-lanczos/code/drift/e1_scalar_finite_check.py',
            'tracks/bivariate-lanczos/theory/drift-codex-e1-05-finite-scalar-cgs2-capacities.md',
            'tracks/bivariate-lanczos/theory/drift-codex-e1-06-finite-scalar-cgs2-separation.md'}
assert set(changed) == expected
scientific = [p for p in changed if p not in [T+'LOG.md','results/padua-lanczos-drift-20261101.md']]
assert all(Path(p).read_bytes() == git('show',f'{CANDIDATE}:{p}') for p in scientific)
previous_paths = git('ls-tree','-r','--name-only',OLD,T).decode().splitlines()
frozen = [p for p in previous_paths if p.startswith((T+'checks/', T+'evidence/'))
          or p.startswith(T+'audit-') or p in [T+'response-01.md',T+'response-02.md']]
assert all(Path(p).read_bytes() == git('show',f'{OLD}:{p}') for p in frozen)
protected = ['AGENTS.md','agents','templates','.github','PROOF_STATUS.md','state',
             'literature','PAPER_MAP.md','RESULTS.md']
assert not git('diff','--name-only',MAIN,READ,'--',*protected).strip()
old_theory = [p for p in git('ls-tree','-r','--name-only',MAIN,
             'tracks/bivariate-lanczos/theory').decode().splitlines() if 'drift-codex-' not in p]
assert len(old_theory) == 77 and not git('diff','--name-only',MAIN,READ,'--',*old_theory).strip()
registry = ['PROOF_STATUS.md','state/IDEAS.md','literature/INDEX.md','ID_CROSSWALK.md']
ledgers = ['topics/charter-unisolvence-20261031/ALLOCATIONS.md',
           'topics/padua-batch-20261031/ALLOCATIONS.md']
assert not git('diff','--name-only',MAIN,PR12,'--',*registry,*ledgers).strip()
integration = json.loads(Path(T+'evidence/audit-04-integration.json').read_text())
assert integration['result'] == 'PASS'
assert all(r['clean'] for r in integration['checks']['merge_tree_vs_open_prs'].values())
assert all(not r['final_assignments_of_reserved_ids'] for r in
           integration['checks']['reserved_range_usage'].values())
paths = sorted(set(git('ls-files','--cached','--others','--exclude-standard').decode().splitlines()))
mainpaths = set(git('ls-tree','-r','--name-only',MAIN).decode().splitlines())
sizes = [(p,Path(p).stat().st_size) for p in paths if p != OUT and p not in mainpaths and own(p)]
outputs = [p for p in paths if p != OUT and (p.startswith(T+'checks/audit-04/')
           or p.startswith(T+'evidence/audit-04-') or p in
           [T+'audit-04.md',T+'LOG.md','results/padua-lanczos-drift-20261101.md'])]
out = {
    'rules_head': READ, 'candidate': CANDIDATE, 'previous_published_head': OLD,
    'main': MAIN, 'other_open_PR12': PR12,
    'candidate_changed_inputs': [identity(p,git('show',f'{CANDIDATE}:{p}')) for p in changed],
    'scientific_inputs_equal_candidate': True,
    'historical_frozen_files_unchanged': len(frozen),
    'protected_paths_unchanged': True, 'original_theory_files_unchanged': len(old_theory),
    'PR12_registry_and_ledger_bytes_equal_main': True,
    'registry_ledger_identities': {
        label: [identity(p,git('show',f'{ref}:{p}')) for p in registry+ledgers]
        for label,ref in {'main':MAIN,'read_head':READ,'PR12':PR12}.items()},
    'reserved_ranges_unassigned': True,
    'audit_outputs_excluding_this_inventory': [identity(p,Path(p).read_bytes()) for p in outputs],
    'campaign_inventory': {'definition': 'All own new files vs main, including prose/code/results; excludes this inventory',
                           'files_excluding_this_inventory': len(sizes),
                           'bytes_excluding_this_inventory': sum(n for _,n in sizes),
                           'largest': max(sizes,key=lambda pair:pair[1])},
    'limits': 'No allocation or readiness declaration. Preparation refreshes union/retired reservations again. Later handoff adds compact prose only.',
    'result': 'PASS',
}
Path(OUT).write_text(json.dumps(out,indent=1)+'\n')
total = sum(n for _,n in sizes)+Path(OUT).stat().st_size
assert total < 5000000 and max(n for _,n in sizes) < 1000000
print(json.dumps({'result':'PASS','frozen_files':len(frozen),'campaign_files':len(sizes)+1,
                  'campaign_bytes':total,'largest':out['campaign_inventory']['largest']}))
