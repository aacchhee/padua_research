#!/usr/bin/env python3
"""Summarize actual readiness executions; bulk scratch stays outside Git.

Run commands in readiness-01.md first. This checker does not rerun certificates.
"""
import hashlib
import importlib.util
import json
from pathlib import Path
import platform
import re
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / 'topics/padua-mz-paper-20261113'
UPLOADED_CC = Path('/workspace/attachments/619dbbc5-3b09-47d4-aa94-f8af6e0586f7/padua-zenodo-mz-cc-20261114.zip')


def digest(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    out = {'input_head': '9705c75876a74ac6bcce5625d20a45e3676c1992',
           'pack_source_head': '90860ecdc12d9887f7d31c3b0440d3b14e8d6169',
           'model': 'Codex, gpt-6-astra high (configured assignment)',
           'python': sys.version, 'platform': platform.platform(),
           'checker_sha256': digest(__file__), 'builds': {}, 'pack_runs': {}}
    assert digest(UPLOADED_CC) == '6aa35fc712154bd51da88f3348b821f6d8436b0fbce43e1b998b353d771a2a48'
    with zipfile.ZipFile(UPLOADED_CC) as z:
        assert z.testzip() is None
        prefix = 'padua-mz-cc-evidence/'
        lines = z.read(prefix + 'MANIFEST-SHA256.txt').decode().splitlines()
        for line in lines:
            expected, rel = line.split('  ', 1)
            assert hashlib.sha256(z.read(prefix + rel)).hexdigest() == expected, rel
    out['uploaded_cc_zip'] = {'bytes': UPLOADED_CC.stat().st_size,
                             'sha256': digest(UPLOADED_CC), 'manifest_rows_pass': len(lines)}
    out['uploaded_sp_zip'] = {
        'direct_transfer': 'unavailable: exceeds executor 32 MiB transfer limit',
        'recorded_bytes_not_independently_read': 40708593,
        'recorded_sha256_not_independently_read': 'f04f65b59954528ffa59886743da5296495a9d6908f36695dc7515cad6e16b2b',
        'fallback': 'rebuilt from pinned source and independently regenerated exact data'}
    spec = importlib.util.spec_from_file_location('receipt_comparator', TOPIC / 'zenodo/compare_receipts.py')
    comparator = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(comparator)
    historical = json.loads(Path('/tmp/mz-readiness-data/table1/reproduction-historical-2b52b432.json').read_text())
    for suite in ['padua', 'marginal']:
        fresh = json.loads(Path('/tmp/mz-readiness-data/measurements/reproduction-' + suite + '.json').read_text())
        differences = []
        for key, value in fresh['results'].items():
            comparator.walk(value, historical['results'][key], key, differences)
        assert not differences, differences
    out['measured_results_against_historical_blob'] = {
        'padua': 'all numerical result fields agree', 'marginal': 'all numerical result fields agree',
        'scope': 'existing comparator runtime-field exclusions; original delivered JSON metadata not asserted'}
    for suffix, pages, count in [('cc', 32, 52), ('sp', 50, 56)]:
        build = Path('/tmp/mz-readiness-' + suffix)
        info = subprocess.check_output(['pdfinfo', str(build / 'manuscript.pdf')], text=True)
        assert int(re.search(r'^Pages:\s+(\d+)', info, re.M)[1]) == pages
        fonts = subprocess.check_output(['pdffonts', str(build / 'manuscript.pdf')], text=True)
        assert 'Type 3' not in fonts
        issues = [line for line in (build / 'manuscript.log').read_text().splitlines()
                  if re.search(r'Warning|Overfull|Underfull|undefined|^!', line)
                  and 'infwarerr' not in line]
        assert not issues, issues
        aux = dict(re.findall(r'\\newlabel\{([^}]+)\}\{\{([^}]*)\}',
                              (build / 'manuscript.aux').read_text()))
        old = dict(re.findall(r'\\newlabel\{([^}]+)\}\{\{([^}]*)\}',
                              Path('/tmp/mz-audit-' + suffix + '/manuscript.aux').read_text()))
        assert aux == old
        frozen = (TOPIC / ('correspondence-' + suffix + '.md')).read_text().split('## Frozen numbering', 1)[1]
        rows = [(key, value.strip()) for key, value in re.findall(r'^\| `([^`]+)` \| ([^|]+)\|', frozen, re.M)
                if not key.endswith('@cref')]
        assert len(rows) == count
        assert all(aux[key] == value for key, value in rows)
        out['builds'][suffix] = {'pages': pages, 'final_log_issues': issues, 'type3_fonts': False,
                                 'all_compiled_label_values_unchanged': len(aux),
                                 'frozen_non_cref_labels_pass': count,
                                 'pdf_sha256': digest(build / 'manuscript.pdf')}
    for name, log in [('uploaded_cc', '/tmp/mz-readiness-upload-cc-rerun.log'),
                      ('rebuilt_cc', '/tmp/mz-readiness-verify-cc.log'),
                      ('rebuilt_sp', '/tmp/mz-readiness-verify-sp.log')]:
        text = Path(log).read_text()
        assert text.rstrip().endswith('ALL CHECKS AGREE'), name
        assert not any(line.startswith('DIFFER ') for line in text.splitlines()), name
        out['pack_runs'][name] = {'all_required_default_checks_agree': True,
                                  'agree_lines': sum(line.startswith('AGREE ') for line in text.splitlines()),
                                  'stdout_sha256': digest(log)}
    sp = Path('/tmp/mz-readiness-packs/padua-mz-sp-evidence')
    rows = (TOPIC / 'zenodo/MANIFEST-padua-zenodo-mz-sp-20261114.txt').read_text().splitlines()
    expected_members = {line.split('  ', 1)[1] for line in rows}
    actual_members = {str(p.relative_to(sp)) for p in sp.rglob('*')
                      if p.is_file() and p.name != 'MANIFEST-SHA256.txt'}
    assert actual_members == expected_members, (actual_members - expected_members, expected_members - actual_members)
    equal, different, unavailable = [], [], []
    for line in rows:
        expected, rel = line.split('  ', 1)
        file = sp / rel
        if not file.exists():
            unavailable.append(rel)
        elif digest(file) == expected:
            equal.append(rel)
        else:
            different.append(rel)
    allowed = {f'data/witnesses/cert-m{m}/witness.json.gz' for m in [1101, 1240, 1600]}
    allowed |= {f'data/measurements/reproduction-{s}.json' for s in ['padua', 'marginal']}
    # A newly produced verification log is allowed after finalization; before it,
    # the original delivered log is unavailable. Never assert its old bytes.
    assert set(different) <= allowed | {'VERIFICATION-2026-11-14.log'}, different
    assert set(unavailable) <= {'VERIFICATION-2026-11-14.log'}, unavailable
    out['rebuilt_sp_against_delivered_manifest'] = {
        'rows': len(rows), 'exact_hash_matches': len(equal),
        'run_or_container_differences': different, 'original_members_unavailable': unavailable,
        'note': 'gzip payloads/norms checked against original pins by separate witness checker; fresh measured receipts verified, original delivered measurement/log bytes not read'}
    # The fallback ZIP is newly generated, never presented as the uploaded ZIP.
    freshzip = Path('/tmp/mz-readiness-packs/padua-mz-sp-evidence.zip')
    with zipfile.ZipFile(freshzip) as z:
        assert z.testzip() is None
        prefix = 'padua-mz-sp-evidence/'
        lines = z.read(prefix + 'MANIFEST-SHA256.txt').decode().splitlines()
        for line in lines:
            expected, rel = line.split('  ', 1)
            assert hashlib.sha256(z.read(prefix + rel)).hexdigest() == expected, rel
            assert z.read(prefix + rel) == (sp / rel).read_bytes(), rel
    out['rebuilt_sp_zip'] = {'bytes': freshzip.stat().st_size, 'sha256': digest(freshzip),
                             'manifest_rows_pass': len(lines), 'same_files_as_verified_staging': True}
    out['scientific_code_sha256'] = {
        str(path.relative_to(ROOT)): digest(path) for path in
        [TOPIC / 'zenodo/verify-mz-cc.sh', TOPIC / 'zenodo/verify-mz-sp.sh',
         TOPIC / 'zenodo/compare_receipts.py', TOPIC / 'tools/zenodo_pack.py']}
    target = TOPIC / 'audit-support/readiness-reruns.json'
    target.write_text(json.dumps(out, indent=2) + '\n')
    assert target.stat().st_size < 16384
    print('PASS', target, target.stat().st_size, 'bytes')


if __name__ == '__main__':
    main()
