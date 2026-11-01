"""Hash retained audit artifacts, check links and conservatively inventory outputs."""
from pathlib import Path
import hashlib
import json
import platform
import re
import subprocess

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
TARGET = HERE / 'artifact-manifest.json'
HEAD = 'a2dd845b8a231e1b00733e1361e2a9ad3bad222f'

artifacts = []
paths = sorted(p for p in HERE.rglob('*') if p.is_file() and p != TARGET
               and '__pycache__' not in p.parts)
paths.append(HERE.parent / 'audit-04.md')
for p in paths:
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

# This intentionally overcounts audit code/prose, input data and metadata alongside
# output files. It covers the whole repository, not only this topic's run folders.
prior = []
lower_bound = []
rows = subprocess.check_output(['git', '-C', str(ROOT), 'ls-tree', '-rl', HEAD], text=True)
for line in rows.splitlines():
    meta, p = line.split('\t', 1)
    if (re.search(r'/(?:logs(?:_[^/]*)?|analysis|independent|directions|outputs|evidence|audit-\d\d)/', p)
            and Path(p).suffix in {'.json', '.csv', '.raw', '.log', '.txt', '.gz'}
            and not re.search('manifest|targets|inventory|snapshot|map|input|environment|config', Path(p).name)):
        lower_bound.append({'path': p, 'bytes': int(meta.split()[3]), 'git_blob': meta.split()[2]})
    if (re.search(r'/(?:logs(?:_[^/]*)?|analysis|audit-\d\d)/', p)
            or re.search(r'/audit-\d\d.md$', p)
            or Path(p).suffix in {'.json', '.csv', '.raw', '.log', '.txt', '.gz'}):
        n = int(meta.split()[3])
        assert n <= 1_000_000, p
        prior.append((p, n))

lower_target = HERE / 'aggregate-output-lower-bound.json'
lower_target.write_text(json.dumps({'source': HEAD, 'description': 'Selected existing experiment/checker data files under run/evidence/audit directories; metadata filenames, code, prose and this new audit excluded. Lower bound, not exhaustive.',
                                    'files': len(lower_bound), 'bytes': sum(x['bytes'] for x in lower_bound),
                                    'limit': 5_000_000, 'artifacts': lower_bound}, indent=2) + '\n')
# Rehash the inventory after regeneration so the manifest never records stale bytes.
for row in artifacts:
    if row['path'] == str(lower_target.relative_to(ROOT)):
        data = lower_target.read_bytes()
        row.update(bytes=len(data), sha256=hashlib.sha256(data).hexdigest())

result = {
    'reviewed_head': HEAD,
    'base': '9739a0c56b7a3976422ce60a8441bfbbfd6554df',
    'accepted_science': 'cf01449fc96233c9074ce25efcb056535414aa1d',
    'verdict': 'WORK; four medium integration findings and one low generator finding',
    'environment': {'python': platform.python_version(), 'platform': platform.platform()},
    'artifact_count': len(artifacts),
    'audit_bytes_excluding_manifest': sum(x['bytes'] for x in artifacts),
    'conservative_prior_repository_inventory_files': len(prior),
    'conservative_prior_repository_inventory_bytes': sum(n for _, n in prior),
    'inventory_definition': 'All tracked audit/logs/analysis directories and audit reports, plus all .json/.csv/.raw/.log/.txt/.gz files at reviewed head; deliberately includes code, prose, inputs and metadata. New audit counted in full.',
    'manifest_excludes_itself': True,
    'repository_aggregate_requires_reconciliation': True,
    'links_valid': True,
    'regeneration_command': 'python3 topics/bivariate-lanczos-20261031/audit-04/record_completion.py',
    'retention': 'Small necessary committed review evidence/checkers; no external archive created or accessed.',
    'artifacts': artifacts,
}
TARGET.write_text(json.dumps(result, indent=2) + '\n')
total = sum(n for _, n in prior) + sum(x['bytes'] for x in artifacts) + TARGET.stat().st_size
print(json.dumps({'artifacts': len(artifacts), 'audit_bytes': result['audit_bytes_excluding_manifest'],
                  'conservative_repository_total_bytes': total, 'links_valid': True,
                  'aggregate_under_5MB': total < 5_000_000}))
