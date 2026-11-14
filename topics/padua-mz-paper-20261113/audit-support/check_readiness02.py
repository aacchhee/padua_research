#!/usr/bin/env python3
"""Check focused-readiness executions and unchanged allocation/content boundaries.

Run staging, controls and CC commands in readiness-02.md first. No certificate
or archive delivery is asserted merely by inspecting an old receipt.
"""
import hashlib
import json
from pathlib import Path
import platform
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / 'topics/padua-mz-paper-20261113'
INPUT = 'b2e47412e74d2082d2c4e5587baf89cf7b25ab3a'
SOURCE = '52030d1d22d6397a02c2831145a962e02105973b'


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT).decode().strip()


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    result = {'rules_input': INPUT, 'pack_source': SOURCE,
              'model_effort': 'Codex gpt-6-astra medium (configured assignment)',
              'python': sys.version, 'platform': platform.platform(),
              'checker_sha256': digest(__file__), 'controls': {}, 'manifests': {}}
    for pack, expected_count in [('cc', 2), ('sp', 6)]:
        path = Path('/tmp/mz-focused-controls-' + pack + '.json')
        data = json.loads(path.read_text())
        assert len(data['results']) == expected_count
        assert all(row['pass_'] for row in data['results'])
        result['controls'][pack] = [{k: row[k] for k in ['mode', 'args', 'exit', 'summary', 'pass_']}
                                    for row in data['results']]
    result['real_cc_runs'] = {}
    for mode, path in [('relative_venv', '/tmp/mz-focused-cc-full.log'),
                       ('bare_PATH_python3', '/tmp/mz-focused-cc-bare.log')]:
        text = Path(path).read_text()
        assert text.rstrip().endswith('ALL REQUIRED CHECKS AGREE')
        assert sum(line.startswith('AGREE ') for line in text.splitlines()) == 4
        assert not any(line.startswith(('DIFFER', 'FAILED')) for line in text.splitlines())
        result['real_cc_runs'][mode] = {'comparisons_agree': 4, 'summary': 'ALL REQUIRED CHECKS AGREE',
                                        'stdout_sha256': digest(path)}
    for pack, expected_rows in [('cc', 377), ('sp', 706)]:
        stage = Path('/tmp/mz-focused-packs/padua-mz-' + pack + '-evidence')
        manifest = TOPIC / f'zenodo/MANIFEST-padua-zenodo-mz-{pack}-20261114.txt'
        rows = [line.split('  ', 1) for line in manifest.read_text().splitlines()]
        assert len(rows) == expected_rows
        names = {rel for _, rel in rows}
        actual = {str(p.relative_to(stage)) for p in stage.rglob('*') if p.is_file()}
        assert actual == names - {'VERIFICATION-2026-11-14.log'}, (actual-names, names-actual)
        same, changed, missing = [], [], []
        for expected, rel in rows:
            path = stage / rel
            if not path.exists():
                missing.append(rel)
            elif digest(path) == expected:
                same.append(rel)
            else:
                changed.append(rel)
        allowed = {'data/table1/reproduction.json'} if pack == 'cc' else {
            'data/measurements/reproduction-padua.json', 'data/measurements/reproduction-marginal.json',
            *(f'data/witnesses/cert-m{m}/witness.json.gz' for m in [1101, 1240, 1600])}
        assert set(changed) <= allowed, changed
        assert missing == ['VERIFICATION-2026-11-14.log'], missing
        source_members = [rel for rel in names if rel.startswith('repository/')]
        for rel in source_members:
            blob = subprocess.check_output(['git', 'show', SOURCE + ':' + rel.removeprefix('repository/')], cwd=ROOT)
            assert hashlib.sha256(blob).hexdigest() == digest(stage / rel), rel
        assert (stage / 'verify.sh').read_bytes() == (TOPIC / f'zenodo/verify-mz-{pack}.sh').read_bytes()
        result['manifests'][pack] = {'rows': len(rows), 'repository_members_pass': len(source_members),
                                     'exact_hash_matches': len(same), 'runtime_container_differences': changed,
                                     'original_delivered_log_unavailable': missing,
                                     'new_verifier_and_template_hashes_match': True}
    paths = ['topics/padua-mz-cleanup-20261105', 'topics/padua-mz-2d-frontier-20261105',
             'topics/padua-mz-sharp-constants-20261106', 'tracks/mz-constants']
    assert not git('diff', '--name-only', '9705c75', SOURCE, '--', *paths)
    result['scientific_paths_unchanged_from_readiness01'] = paths
    registry_paths = ['PROOF_STATUS.md', 'state/IDEAS.md', 'literature/INDEX.md', 'ID_CROSSWALK.md',
                      ':(glob)topics/**/ALLOCATIONS.md']
    previous = '9d3f5e0f8b270d039d78d4ebc0df53269a7892ab'
    current = '50070f520b3d5cfe9afbc75f10fdb1bc664b7b71'
    assert not git('diff', '--name-only', previous, current, '--', *registry_paths)
    assert git('rev-parse', 'origin/main') == '99a9b1d161e41a80c4fd425b63022c681fbe8779'
    assert not git('diff', '--name-only', '9705c75', INPUT, '--', *registry_paths)
    result['reservation_reuse'] = {'main': git('rev-parse', 'origin/main'),
                                   'previous_PR27': previous, 'current_PR27': current,
                                   'previous_PR35': '9705c75876a74ac6bcce5625d20a45e3676c1992',
                                   'current_PR35': INPUT, 'ledger_and_four_registry_changes': []}
    result['limitations'] = ['Replacement delivered ZIP bytes and their original console logs were not available',
                              'SP numerical certificate suite not repeated; accepted readiness-01 executions remain unchanged',
                              'Stubbed controls test shell outcomes, not numerical claims',
                              'Fresh venv used system site packages plus /tmp/mz-python, not a fresh pip installation']
    target = TOPIC / 'audit-support/readiness02-checks.json'
    target.write_text(json.dumps(result, indent=2) + '\n')
    assert target.stat().st_size < 16384
    print('PASS', target, target.stat().st_size, 'bytes')


if __name__ == '__main__':
    main()
