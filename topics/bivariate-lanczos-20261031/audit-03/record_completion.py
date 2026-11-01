"""Inventory the completed narrow verification and enforce output size caps."""
from pathlib import Path
import hashlib
import importlib.metadata
import json
import platform
import re
import subprocess

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent
TARGET = HERE / 'artifact-manifest.json'
PUBLISHED = '63ffc67f8bc60bd30abcd94769b6aa1d1e783d88'


def main():
    subprocess.run(['python3', str(HERE / 'check_response.py')],
                   stdout=subprocess.DEVNULL, check=True)
    reports = [TOPIC / 'audit-03.md', HERE / 'independent-verification.md']
    for report in reports:
        for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', report.read_text()):
            if '://' not in target and not target.startswith('#'):
                resolved = (report.parent / target.split('#')[0]).resolve()
                assert resolved == TARGET or resolved.exists(), target
    prior_bytes = 0
    rows = subprocess.check_output(['git', '-C', str(ROOT), 'ls-tree', '-r', '--long',
                                   PUBLISHED, 'topics/bivariate-lanczos-20261031'], text=True)
    for row in rows.splitlines():
        meta, name = row.split('\t', 1)
        if ('/logs/' in name or '/logs_' in name or '/audit-01/' in name or '/audit-02/' in name
                or name.endswith('/audit-01.md') or name.endswith('/audit-02.md')
                or '/repro/analysis/' in name and name.endswith('.txt')):
            size = int(meta.split()[3])
            assert size <= 1000000, name
            prior_bytes += size
    artifacts = []
    for path in sorted(HERE.rglob('*')) + [TOPIC / 'audit-03.md']:
        if not path.is_file() or path == TARGET or '__pycache__' in path.parts:
            continue
        data = path.read_bytes()
        assert len(data) <= 1000000, path
        artifacts.append({'path': str(path.relative_to(ROOT)), 'bytes': len(data),
                          'sha256': hashlib.sha256(data).hexdigest()})
    total = sum(row['bytes'] for row in artifacts)
    impact = json.loads((HERE / 'impact-check.json').read_text())
    result = {'candidate': impact['candidate'], 'published_response': PUBLISHED,
              'prior_audit': impact['base'], 'main_at_verification': impact['main_at_verification'],
              'verdict': 'CLEAN; A2-L1-A2-L4 resolved; PR preparation pending.',
              'impact_map_pass': impact['pass'], 'links_valid': True,
              'environment': {'python': platform.python_version(),
                              'numpy': importlib.metadata.version('numpy'),
                              'scipy': importlib.metadata.version('scipy')},
              'artifact_count': len(artifacts), 'verification_bytes': total,
              'conservative_prior_output_bytes': prior_bytes,
              'conservative_output_plus_verification_bytes': prior_bytes + total,
              'manifest_excludes_itself': True,
              'regeneration_command': 'python3 topics/bivariate-lanczos-20261031/audit-03/record_completion.py',
              'retention': 'Small necessary committed verification evidence; no external archive created.',
              'artifacts': artifacts}
    TARGET.write_text(json.dumps(result, indent=2) + '\n')
    assert prior_bytes + total + TARGET.stat().st_size < 5000000
    print(json.dumps({key: value for key, value in result.items() if key != 'artifacts'}, indent=2))


if __name__ == '__main__':
    main()
