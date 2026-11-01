#!/usr/bin/env python3
"""Audit repaired allocation default path; never invoke --apply or modify inputs."""
import hashlib
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SOURCE = '37820a528c863e5cfe2dc2f1f8879b4fd40cf210'
PREALLOCATION = '6954664fc0906b7e5c8ff0f1804b077bd3b5861f^'
PR11 = '97968d2c2d039cb0910e0ea50747fb2d9e01a262'
TOPIC = 'topics/programme-ideas-20261031/'
SCRIPT = TOPIC+'pr-prep/allocate.py'
MAP = TOPIC+'pr-prep/id-map.json'
LEDGER = 'topics/padua-batch-20261031/ALLOCATIONS.md'
REGISTRIES = ['PROOF_STATUS.md','state/IDEAS.md','literature/INDEX.md','ID_CROSSWALK.md']
checks = []
manifest = {}

def digest(data):
    return hashlib.sha256(data).hexdigest()

def git(*args):
    return subprocess.check_output(['git',*args],cwd=ROOT)

def original(path,revision=SOURCE):
    data = git('show',revision+':'+path)
    manifest[revision+':'+path] = digest(data)
    return data

def current(path):
    data = (ROOT/path).read_bytes()
    manifest['worktree:'+path] = digest(data)
    return data

def check(name,success,detail=None):
    checks.append({'name':name,'pass':bool(success),'detail':detail})

def rows(text):
    return [[c.strip() for c in line.split('|')[1:-1]] for line in text.splitlines() if line.startswith('| ')]

lat_path = 'topics/lattice-unisolvence-20261031/provisional-id-map.json'
lat = json.loads(original(lat_path))['rows']
theory = git('ls-tree','-r','--name-only',SOURCE,TOPIC+'theory').decode().splitlines()
canonical = sorted({r['path'] for r in lat if r['id'].startswith(('PD','IDEA'))} | set(theory) | {TOPIC+'ideas/candidates.md'})
inputs = sorted(set(REGISTRIES+[lat_path,'topics/bivariate-lanczos-20261031/pr-prep/id-map.json',TOPIC+'lit/integration-map.json',TOPIC+'lit/integration-map-pr10.json',TOPIC+'lit/baseline.md',SCRIPT,MAP,LEDGER]+theory))
snapshot = {path:current(path) for path in inputs}
allocation = json.loads(snapshot[MAP])
check('allocation_map_byte_identical_to_source',snapshot[MAP] == original(MAP))
changed_canonical = [path for path in canonical if current(path) != original(path)]
check('canonical_changes_limited_to_lattice_README',not set(changed_canonical)-{'tracks/lattice-unisolvence/README.md'},changed_canonical)
readme = 'tracks/lattice-unisolvence/README.md'
allowed_metadata = {
    'The topic retains provisional candidates and result IDs until coordinated PR preparation.':'The original provisional headings remain provenance; final IDs were allocated during PR #6 preparation as recorded above.',
    'All IDs remain provisional as AC requested.':'The table below retains the originally requested provisional IDs as aliases; each canonical record now also states its allocated final ID.'}
expected_readme = original(readme).decode()
for before,after in allowed_metadata.items():
    expected_readme = expected_readme.replace(before,after)
check('canonical_README_only_two_exact_metadata_replacements',current(readme).decode() == expected_readme)
check('canonical_scientific_records_preserved',all(current(path)==original(path) for path in canonical if path!=readme),len(canonical)-1)
for path in REGISTRIES:
    old_rows,new_rows = rows(original(path).decode()),rows(snapshot[path].decode())
    if path=='ID_CROSSWALK.md':
        old_ids = [(r[0],r[1]) for r in old_rows if len(r)>1 and r[0] in {**allocation['map'],**allocation['merged_without_new_id']}]
        new_ids = [(r[0],r[1]) for r in new_rows if len(r)>1 and r[0] in {**allocation['map'],**allocation['merged_without_new_id']}]
    else:
        old_ids = [r[0] for r in old_rows if re.match(r'(PD-[TN]\d{3}|IDEA-\d{3}|LIT-\d{3})\b',r[0])]
        new_ids = [r[0] for r in new_rows if re.match(r'(PD-[TN]\d{3}|IDEA-\d{3}|LIT-\d{3})\b',r[0])]
    check(path+'_ID_cells_identical',old_ids==new_ids)
    if path=='PROOF_STATUS.md':
        old_science = [r[:-1] for r in old_rows if re.match(r'PD-[TN]\d{3}\b',r[0])]
        new_science = [r[:-1] for r in new_rows if re.match(r'PD-[TN]\d{3}\b',r[0])]
        check('proof_registry_all_cells_except_audit_metadata_identical',old_science==new_science)
    if path=='state/IDEAS.md':
        check('IDEA_primary_rows_all_cells_identical',[r for r in old_rows if re.match(r'IDEA-\d{3}',r[0])]==[r for r in new_rows if re.match(r'IDEA-\d{3}',r[0])])
reservation = {f'LIT-{i}' for i in range(293,300)}
pr11_ledger = original(LEDGER,PR11).decode()
check('actual_PR11_reservation_preserved', '**LIT-293–LIT-299**' in pr11_ledger and not reservation & set(allocation['map'].values()) and PR11 in snapshot[LEDGER].decode() and 'LIT-293–299' in snapshot[LEDGER].decode())

def snapshot_hashes(directory):
    return {str(p.relative_to(directory)):digest(p.read_bytes()) for p in directory.rglob('*') if p.is_file()}

def alter_line(files,path,prefix,transform):
    lines = files[path].decode().splitlines(keepends=True)
    indices = [i for i,line in enumerate(lines) if line.startswith(prefix)]
    assert len(indices)==1,(path,prefix,indices)
    index = indices[0]
    lines[index] = transform(lines[index])
    files[path] = ''.join(lines).encode()

def mutate(files,case):
    if case=='mutated_installed_map':
        changed = json.loads(files[MAP]);changed['map']['PD-T?lattice-c0-codex-01']='PD-T082'
        files[MAP]=(json.dumps(changed)+'\n').encode()
    elif case=='duplicate_primary_ID':
        alter_line(files,'PROOF_STATUS.md','| PD-T081 ',lambda line:line+line)
    elif case=='wrong_crosswalk_target':
        alter_line(files,'ID_CROSSWALK.md','| PD-T?lattice-c0-codex-01 | ',lambda line:line.replace('| PD-T081 ','| PD-T082 ',1))
    elif case=='wrong_merged_crosswalk_target':
        alter_line(files,'ID_CROSSWALK.md','| LIT?programme-ideas-claude-48 | ',lambda line:line.replace('Merged into LIT-002','Merged into LIT-003',1))
    elif case=='missing_primary_row':
        alter_line(files,'PROOF_STATUS.md','| PD-T081 ',lambda line:'')
    elif case=='wrong_primary_alias':
        alter_line(files,'PROOF_STATUS.md','| PD-T081 ',lambda line:line.replace('PD-T?lattice-c0-codex-01','PD-T?lattice-c0-codex-02'))
    elif case=='missing_map_with_allocated_registries':
        del files[MAP]
    elif case!='valid_installed':
        raise ValueError(case)

runs=[]
cases = ['valid_installed','valid_preallocation','mutated_installed_map','duplicate_primary_ID','wrong_crosswalk_target','wrong_merged_crosswalk_target','missing_primary_row','wrong_primary_alias','missing_map_with_allocated_registries']
for case in cases:
    if case=='valid_preallocation':
        files={path:(data if path==SCRIPT else original(path,PREALLOCATION)) for path,data in snapshot.items() if path!=MAP}
    else:
        files = dict(snapshot);mutate(files,case)
    with tempfile.TemporaryDirectory(prefix='allocation-repair-audit-') as directory:
        tmp=Path(directory)
        for path,data in files.items():
            destination=tmp/path;destination.parent.mkdir(parents=True,exist_ok=True);destination.write_bytes(data)
        before=snapshot_hashes(tmp)
        result=subprocess.run([sys.executable,'-I',SCRIPT],cwd=tmp,capture_output=True,text=True)
        after=snapshot_hashes(tmp)
        runs.append({'case':case,'argv':['python3','-I',SCRIPT],'returncode':result.returncode,'stdout':result.stdout,'stderr':result.stderr,'bytes_unchanged':before==after,'input_hashes_changed_from_valid':{p:digest(data) for p,data in files.items() if data!=snapshot.get(p)},'inputs_removed':sorted(set(snapshot)-set(files))})
        check(case+'_no_writes',before==after)
        if case in ('valid_installed','valid_preallocation'):
            check(case+'_success_and_map_boundaries_match',result.returncode==0 and json.loads(result.stdout)=={'blocks':allocation['blocks'],'next':allocation['next_unreserved']})
        else:
            check(case+'_rejected',result.returncode!=0 and 'AssertionError' in result.stderr)
check('source_inputs_not_changed_during_audit',all((ROOT/path).read_bytes()==data for path,data in snapshot.items()))
print(json.dumps({'source':SOURCE,'worktree_head_at_end':git('rev-parse','HEAD').decode().strip(),'PR11':PR11,'python':sys.version,'checks':checks,'runs':runs,'sha256':manifest,'all_checks_pass':all(item['pass'] for item in checks)},indent=2,ensure_ascii=False))
sys.exit(0 if all(item['pass'] for item in checks) else 1)
