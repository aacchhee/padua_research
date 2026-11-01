"""Validate the final focused audit envelope and inventory its retained evidence."""
from pathlib import Path
import hashlib
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent
TARGET = HERE / 'artifact-manifest.json'


def main():
    subprocess.run(['python3', str(HERE / 'check_impact.py')],
                   stdout=subprocess.DEVNULL, check=True)
    names = ['L1', 'L2', 'L3-conventions', 'L3-formula-scope', 'L5', 'protocol']
    reports = [HERE / (name + '.md') for name in names] + [TOPIC / 'audit-02.md']
    assert all(p.is_file() for p in reports)
    missing = []
    for report in reports:
        for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', report.read_text()):
            if '://' in target or target.startswith('#'):
                continue
            path = target.split('#')[0]
            if path and not (report.parent / path).resolve().exists():
                missing.append({'source': str(report.relative_to(ROOT)), 'target': target})
    assert not missing, missing
    artifacts = []
    for path in sorted(HERE.rglob('*')) + [TOPIC / 'audit-02.md']:
        if not path.is_file() or path == TARGET or '__pycache__' in path.parts:
            continue
        assert path.suffix in {'.py', '.md', '.json', '.jsonl', '.log', '.txt', '.diff'} or path.name == 'SHA256SUMS', path
        data = path.read_bytes()
        assert len(data) <= 1000000, path
        artifacts.append({'path': str(path.relative_to(ROOT)), 'bytes': len(data),
                          'sha256': hashlib.sha256(data).hexdigest()})
    impact = json.loads((HERE / 'impact-check.json').read_text())
    total = sum(row['bytes'] for row in artifacts)
    result = {'candidate': impact['candidate'], 'published_response_head': impact['publication_head'],
              'prior_audit': impact['prior_audit'],
              'main_at_audit': '0d058fb410166bd97b178be57910f2d256d0b529',
              'theory_files_unchanged_from_response': impact['theory_files'],
              'response_impact_inventory_pass': impact['pass'],
              'local_report_links_valid': True, 'scope_reports': names,
              'verdict': 'Original findings resolved in scope; four new low qualifications; WORK.',
              'artifact_count': len(artifacts), 'audit_bytes': total,
              'conservative_candidate_output_plus_inventoried_audit_bytes': total + impact['conservative_candidate_output_bytes'],
              'manifest_excludes_itself': True,
              'regeneration_command': 'python3 topics/bivariate-lanczos-20261031/audit-02/record_completion.py',
              'retention': 'Necessary small committed audit evidence; no new external archive.',
              'artifacts': artifacts}
    TARGET.write_text(json.dumps(result, indent=2) + '\n')
    assert result['conservative_candidate_output_plus_inventoried_audit_bytes'] + TARGET.stat().st_size < 5000000
    print(json.dumps({key: value for key, value in result.items() if key != 'artifacts'}, indent=2))


if __name__ == '__main__':
    main()
