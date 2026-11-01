"""Structural and immutability checks for the pinned response-01 re-audit.

Prints a receipt; does not modify developer files. Mathematical findings live
in audit-02.md and the independent component reports.
"""
import hashlib
import json
from pathlib import Path
import platform
import re
import subprocess

ROOT = Path(__file__).resolve().parents[3]
SOURCE = 'cadb35066160e466cb1704b9791ad6f374446422'
MAIN = '9739a0c56b7a3976422ce60a8441bfbbfd6554df'
ORIGINAL = '614709d4a60fb0c2593b05764e8d5aceda1be381'
AUDIT1 = '988f9126e9c3b6e7a378c7f60c3cd309bb3dc4a3'
TOPIC = 'topics/programme-ideas-20261031'


def git(*args):
    return subprocess.check_output(['git', '-C', str(ROOT), *args])


def blob(path, sha=SOURCE):
    return git('show', sha+':'+path)


def digest(path, sha=SOURCE):
    b = blob(path, sha)
    return {'path': path, 'source': sha, 'git_blob_sha': git('rev-parse', sha+':'+path).decode().strip(),
            'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest()}


assert git('merge-base', MAIN, SOURCE).decode().strip() == MAIN
all_paths = git('ls-tree', '-r', '--name-only', SOURCE).decode().splitlines()
old_paths = git('ls-tree', '-r', '--name-only', ORIGINAL, TOPIC+'/checks/code').decode().splitlines()
assert len(old_paths) == 125
for p in old_paths:
    assert blob(p) == blob(p, ORIGINAL), p
prior_audit = git('ls-tree', '-r', '--name-only', AUDIT1, TOPIC+'/audit-01.md', TOPIC+'/audit-support').decode().splitlines()
for p in prior_audit:
    assert blob(p) == blob(p, AUDIT1), p

protected = ['AGENTS.md', 'agents/codex/CODEX.md', 'topics/padua-batch-20261031/ALLOCATIONS.md']
protected += [p for p in all_paths if p.startswith(('templates/', '.github/'))]
for p in protected:
    assert blob(p) == blob(p, MAIN), p

theory = [p for p in all_paths if p.startswith(TOPIC+'/theory/')]
assert len(theory) == 11
expected = {'PD-T?programme-ideas-claude-01':'PROVED',
            'PD-T?programme-ideas-claude-02':'PROVED',
            'PD-T?programme-ideas-claude-03':'PROVED',
            'PD-T?programme-ideas-claude-04':'OPEN',
            'PD-T?programme-ideas-claude-05':'OPEN',
            'PD-T?programme-ideas-claude-06':'MEASURED',
            'PD-N?programme-ideas-claude-01':'PROVED',
            'PD-N?programme-ideas-claude-02':'MEASURED',
            'PD-N?programme-ideas-claude-03':'PROVED',
            'PD-N?programme-ideas-claude-04':'PROVED',
            'PD-N?programme-ideas-claude-05':'MEASURED'}
proof = blob('PROOF_STATUS.md').decode()
cross = blob('ID_CROSSWALK.md').decode()
for id_, status in expected.items():
    rows = [l for l in proof.splitlines() if l.startswith('| '+id_+' |')]
    assert len(rows) == 1 and rows[0].split('|')[3].strip() == status, id_
    assert '| '+id_+' |' in cross, id_

idea = blob(TOPIC+'/ideas/candidates.md').decode()
ids = re.findall(r'^# IDEA\?programme-ideas-claude-(\d+) —', idea, re.M)
assert sorted(map(int, ids)) == list(range(1,21))
lit = re.findall(r'^\| LIT\?programme-ideas-claude-(\d+) \|', blob(TOPIC+'/lit/baseline.md').decode(), re.M)
assert sorted(map(int, lit)) == list(range(1,112))

new_scope = git('diff', '--name-only', AUDIT1, SOURCE, '--', TOPIC).decode().splitlines()
source_paths = sorted(set(new_scope + ['PROOF_STATUS.md','ID_CROSSWALK.md','state/IDEAS.md','literature/INDEX.md',
                                        'AGENTS.md','agents/WORKFLOW.md','agents/codex/CODEX.md',
                                        TOPIC+'/audit-01.md']))
outputs = [p for p in all_paths if Path(p).suffix.lower() in
           {'.out','.log','.json','.jsonl','.pdf','.zip','.png','.stdout'}]
sizes = [len(blob(p)) for p in outputs]
assert max(sizes) <= 1_000_000
assert sum(sizes) < 5_000_000

# Report the current canonical remnant without repairing or hiding it.
remnants = []
for i, line in enumerate(idea.splitlines(),1):
    if 'certified 41/50/62' in line or 'stands and is now MEASURED to 12 digits' in line:
        remnants.append({'path': TOPIC+'/ideas/candidates.md', 'line': i, 'text': line})

print(json.dumps({'candidate_sha':SOURCE,'current_main':MAIN,'python':platform.python_version(),
    'main_is_ancestor':True,'old_code_output_files_unchanged':len(old_paths),
    'prior_audit_files_unchanged':len(prior_audit),'protected_against_main':protected,
    'theory_statuses':expected,'idea_records':len(ids),'literature_rows':len(lit),
    'generated_like_bytes_at_source':sum(sizes),'largest_generated_like_file_bytes':max(sizes),
    'canonical_remnants':remnants,'source_identities':[digest(p) for p in source_paths],
    'result':'PASS for structural checks; canonical claim contradictions require developer response'},indent=2))
