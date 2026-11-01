#!/usr/bin/env python3
"""Independent finite response diagnostics, not an all-N computer proof.

Uses no campaign imports. Universal validity comes from the analytic proof.
Run from repository root. Output is JSON on stdout only.
"""
import hashlib
import json
import platform
import re
import subprocess
from collections import Counter
from fractions import Fraction as F
from pathlib import Path


def git(*args):
    return subprocess.check_output(['git', *args], text=True).strip()


def mu(k):
    return F(0) if k % 2 else F(2, 1-k*k)


pairs = 0
for N in range(2, 1001):
    endpoint = F(2)-F(4,N)+F(4,N*N)
    assert endpoint == 1 + (1-F(2,N))**2
    # pi > 3: this rational comparison is stronger than the required one.
    assert endpoint < 2-F(2,3*N) < 2
    for n in range(N):
        assert 1+max(F(2*n,N)-1,F(0))**2 <= endpoint
        pairs += 1

entries = 0
for N in range(2, 41):
    n = N-1
    rho = (1-F(2,N))**2
    for i in range(N):
        for j in range(N):
            s, d = i+j, abs(i-j)
            mass = (mu(s)+mu(d))/2
            discrete = (mu(min(s,2*N-s))+mu(d))/2
            defect = 2*(mass-discrete)
            assert defect >= 0
            if i != j:
                assert (1+rho)*mass-discrete <= 0
                entries += 1
            if N == 2:
                assert mass == discrete

base = '6d10a82cf6fd6f7ef6fbe76e68133ccbcbe51994'
statuses = []
for p in sorted(Path('tracks/mz-constants/theory').glob('*.md')):
    current = p.read_text()
    old = git('show', f'{base}:{p.as_posix()}')
    pattern = r'Overall status:\s*\*{0,2}(PROVED|OPEN|MEASURED|CONDITIONAL|PARTIAL)'
    before = re.search(pattern, old).group(1)
    after = re.search(pattern, current).group(1)
    assert before == after, p
    statuses.append(after)
assert len(statuses) == 21

receipt = json.loads(Path('topics/mz-constants/ledger-reconciliation-01.json').read_text())
ledger_path = 'topics/padua-batch-20261031/ALLOCATIONS.md'
ledger = Path(ledger_path).read_bytes()
assert hashlib.sha256(ledger).hexdigest() == receipt['ledger_sha256']
ledger_checks = []
for member in receipt['members']:
    commit = member['published_ledger_commit']
    paths = git('diff-tree','--no-commit-id','--name-only','-r',commit).splitlines()
    assert paths == [ledger_path]
    blob = git('rev-parse',f'{commit}:{ledger_path}')
    assert blob == receipt['ledger_git_blob']
    assert git('rev-parse',f'origin/{member["branch"]}:{ledger_path}') == blob
    ledger_checks.append({'branch':member['branch'],'commit':commit,'changed_paths':paths,'blob':blob})
assert git('rev-parse',f'{receipt["owner_mz_ledger_commit"]}:{ledger_path}') == receipt['ledger_git_blob']

charter_main = receipt['merged_charter_main']
charter_paths = git('ls-tree','-r','--name-only',charter_main,
                    'tracks/unisolvence','topics/charter-unisolvence-20261031').splitlines()
assert len(charter_paths) == 105
for path in charter_paths:
    assert Path(path).read_bytes() == subprocess.check_output(['git','show',charter_main+':'+path])
charter_registry_rows = 0
for registry, pattern in [('PROOF_STATUS.md',r'^\| PD-[TN]\d{3} \|'),
                          ('literature/INDEX.md',r'^\| LIT-\d{3} \|')]:
    current_rows = set(Path(registry).read_text().splitlines())
    for row in git('show',charter_main+':'+registry).splitlines():
        if re.match(pattern,row):
            assert row in current_rows, row
            charter_registry_rows += 1
assert Path('topics/mz-constants/audit-01.md').read_bytes() == subprocess.check_output(['git','show',base+':topics/mz-constants/audit-01.md'])
for path in git('ls-tree','-r','--name-only',base,'tracks/mz-constants/code').splitlines():
    assert Path(path).read_bytes() == subprocess.check_output(['git','show',base+':'+path])

map_path = 'topics/mz-constants/final-id-map.json'
old_map = json.loads(git('show',base+':'+map_path))
new_map = json.loads(Path(map_path).read_text())
assert len(old_map['mappings']) == 65 and len(new_map['mappings']) == 70
assert all(new_map['mappings'][key] == value for key,value in old_map['mappings'].items())
assert len(set(new_map['mappings'].values())) == 70
new_ids = set(new_map['mappings'].values())-set(old_map['mappings'].values())
assert new_ids == {f'LIT-{i:03}' for i in range(61,66)}

sources = [
    'AGENTS.md','agents/WORKFLOW.md','agents/codex/CODEX.md',
    'PROOF_STATUS.md','ID_CROSSWALK.md','PAPER_MAP.md','state/IDEAS.md',
    'literature/INDEX.md','literature/CORPUS.md','literature/records/mz-mean-convergence-screen.md',
    'topics/mz-constants/audit-01.md','topics/mz-constants/scientific-response-01.md',
    'topics/mz-constants/response-01.md','topics/mz-constants/report.md',
    'topics/mz-constants/directions/M1/IDEAS.md','topics/mz-constants/directions/M3/IDEAS.md',
    'topics/mz-constants/final-id-map.json',
    'topics/mz-constants/literature-response-01.md','topics/mz-constants/literature-search.md',
    'topics/mz-constants/ledger-reconciliation-01.json',ledger_path,
    'tracks/mz-constants/code/m3_exact_check.py','tracks/mz-constants/paper/manuscript.tex',
    'tracks/mz-constants/paper/refs.bib','tracks/mz-constants/paper/README.md',
] + [p.as_posix() for p in sorted(Path('tracks/mz-constants/theory').glob('*.md'))]
hashes = {p:{'sha256':hashlib.sha256(Path(p).read_bytes()).hexdigest(),'bytes':Path(p).stat().st_size} for p in sources}
print(json.dumps({
    'scope':'Independent exact finite diagnostics and read-only repository identity checks; not proof of universal mathematical statements',
    'command':'python -I tracks/mz-constants/evidence/astra-response-01-check.py',
    'python':platform.python_version(),'platform':platform.platform(),'head':git('rev-parse','HEAD'),
    'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'endpoint_and_all_degree_pairs_N2_1000':pairs,
    'endpoint_offdiagonal_sign_entries_N2_40':entries,
    'N2_exact_mass_equal_discrete':True,
    'original_21_theory_statuses_preserved':dict(Counter(statuses)),
    'original_65_mappings_preserved_five_unique_LIT_additions':True,
    'charter_105_files_unchanged':True,'charter_registry_rows_preserved':charter_registry_rows,
    'original_audit_and_source_checkers_unchanged':True,
    'ledger_propagation':ledger_checks,'source_files':hashes,'result':'PASS'
},indent=2))
