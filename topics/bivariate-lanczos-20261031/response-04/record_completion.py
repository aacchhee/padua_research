"""Record the final publication's metadata-only delta and retained small evidence."""
from pathlib import Path
import hashlib
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[3]
TOPIC = 'topics/bivariate-lanczos-20261031'
HERE = Path(__file__).resolve().parent
TARGET = HERE / 'artifact-manifest.json'
SOURCE = '98945cbcf10c4f8eb53f77c996db358392d42391'

def git(*args):
    return subprocess.check_output(['git', '-C', str(ROOT), *args])

metadata = {'PROOF_STATUS.md', 'state/CURRENT.md', TOPIC + '/LOG.md',
            'tracks/bivariate-lanczos/AUDIT_LOG.md'}
protected = []
for p in git('ls-tree', '-r', '--name-only', SOURCE).decode().splitlines():
    if p in metadata:
        continue
    assert git('show', SOURCE + ':' + p) == (ROOT / p).read_bytes(), p
    protected.append(p)
old_ps = git('show', SOURCE + ':PROOF_STATUS.md').decode()
new_ps = (ROOT / 'PROOF_STATUS.md').read_text()
assert [l for l in old_ps.splitlines() if l.startswith('|')] == [l for l in new_ps.splitlines() if l.startswith('|')]

paths = [ROOT / TOPIC / 'response-04.md', ROOT / TOPIC / 'audit-05.md',
         ROOT / TOPIC / 'pr-prep/PR.md']
paths += [p for folder in (HERE, ROOT / TOPIC / 'audit-05')
          for p in folder.rglob('*') if p.is_file() and p != TARGET and '__pycache__' not in p.parts]
paths += [ROOT / p for p in sorted(metadata)]
artifacts = []
for p in sorted(set(paths)):
    data = p.read_bytes()
    assert len(data) <= 1_000_000, p
    artifacts.append({'path': str(p.relative_to(ROOT)), 'bytes': len(data),
                      'sha256': hashlib.sha256(data).hexdigest()})
    if p.suffix == '.md':
        for dest in re.findall(r'\[[^\]]+\]\(([^)\s]+)\)', data.decode()):
            if '://' in dest or dest.startswith('#'):
                continue
            q = (p.parent / dest.split('#')[0]).resolve()
            assert q == TARGET or q.exists(), (p, dest)

# Conservatively include code, prose and metadata as well as known outputs.
prior = 0
for line in git('ls-tree', '-rl', SOURCE).decode().splitlines():
    meta, p = line.split('\t', 1)
    if (re.search(r'/(?:logs(?:_[^/]*)?|analysis|audit-\d\d)/', p)
            or re.search(r'/audit-\d\d.md$', p)
            or Path(p).suffix in {'.json', '.csv', '.raw', '.log', '.txt', '.gz'}):
        n = int(meta.split()[3]); assert n <= 1_000_000, p
        prior += n
result = {
    'technical_candidate': SOURCE,
    'verdict': 'READY for AC merge decision; independent technical audit clean and A4-P1 resolved by explicit scoped AC exception',
    'unchanged_candidate_files_in_worktree': len(protected),
    'publication_existing_metadata_paths': sorted(metadata),
    'proof_status_table_rows_unchanged': True,
    'artifact_count': len(artifacts),
    'conservative_prior_repository_inventory_bytes': prior,
    'publication_artifact_bytes_excluding_manifest': sum(x['bytes'] for x in artifacts),
    'inventory_limit': 'Conservative inventory includes code/prose/metadata; not an exact output-only total. The existing output lower bound is independently verified in audit-05. Publication inventory additionally counts some existing metadata again.',
    'aggregate_exception_authority': TOPIC + '/response-04/AC-EXCEPTION.md',
    'individual_artifacts_under_1MB': True,
    'future_experiment_outputs_authorized': False,
    'manifest_excludes_itself': True,
    'regeneration_command': 'python3 topics/bivariate-lanczos-20261031/response-04/record_completion.py',
    'artifacts': artifacts,
}
TARGET.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({k: v for k, v in result.items() if k != 'artifacts'}, indent=2))
