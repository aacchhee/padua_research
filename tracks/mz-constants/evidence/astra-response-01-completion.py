#!/usr/bin/env python3
"""Read-only verification of final rehearsal and scoped source identities."""
import hashlib
import json
import re
import subprocess
from pathlib import Path


def git(*args):
    return subprocess.check_output(['git',*args])


def h(data):
    return hashlib.sha256(data).hexdigest()


receipt = json.loads(Path('topics/mz-constants/batch-rehearsal.json').read_text())
base, source, squash = receipt['base'], receipt['mz_source'], receipt['resolved_local_squash']
assert git('rev-parse',squash+'^').decode().strip() == base
assert git('rev-parse',source+'^{tree}') == git('rev-parse',squash+'^{tree}')
subprocess.run(['git','merge-base','--is-ancestor',base,source],check=True)
assert receipt['conflicts'] == []
patch_path = receipt['repair_patch']['path']
patch = Path(patch_path).read_bytes()
assert len(patch) == receipt['repair_patch']['bytes']
assert h(patch) == receipt['repair_patch']['sha256']
paths = re.findall(rb'^diff --git a/(\S+) b/\S+$',patch,re.M)
assert len(paths) == 10
paths = [p.decode() for p in paths]
assert git('diff','--unified=0',base,source,'--',*paths) == patch
science = json.loads(Path('tracks/mz-constants/evidence/astra-response-01-check.json').read_text())
for name, item in science['source_files'].items():
    data = Path(name).read_bytes()
    assert h(data) == item['sha256'] and len(data) == item['bytes'],name
root = json.loads(Path('tracks/mz-constants/evidence/astra-response-01-protocol-replay.json').read_text())
assert root['result'] == 'PASS' and root['historical_audit_targets_verified'] == 123
assert root['preserved_charter_files'] == 105 and root['preserved_charter_registry_rows'] == 54
assert root['current_response_targets_verified'] == 0  # final manifest is created after this review
pins = ['topics/mz-constants/batch-rehearsal.json',patch_path,
        'topics/mz-constants/integration-impact.md','topics/mz-constants/check_response_01.py',
        'topics/mz-constants/AUDIT_HANDOFF.md',
        'tracks/mz-constants/evidence/astra-response-01-check.py',
        'tracks/mz-constants/evidence/astra-response-01-check.json',
        'tracks/mz-constants/evidence/astra-response-01-m3-replay.txt',
        'tracks/mz-constants/evidence/astra-response-01-protocol-replay.json']
print(json.dumps({'result':'PASS','command':'python -I tracks/mz-constants/evidence/astra-response-01-completion.py',
    'checker_sha256':h(Path(__file__).read_bytes()),'base':base,'source':source,'squash':squash,
    'source_and_rehearsal_trees_identical':True,'source_descends_from_base':True,
    'exact_zero_context_patch_paths':paths,'science_source_hashes_unchanged':len(science['source_files']),
    'root_protocol_independent_replay':'PASS','current_response_targets':'Not yet created; root must pin and verify final packaging',
    'files':{p:{'sha256':h(Path(p).read_bytes()),'bytes':Path(p).stat().st_size} for p in pins}},indent=2))
