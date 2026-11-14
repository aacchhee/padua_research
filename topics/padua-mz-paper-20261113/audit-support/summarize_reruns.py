#!/usr/bin/env python3
"""Check fresh audit receipts and emit small essential evidence, not bulk matrices.

Run the commands in audit-01.md first. Scratch artifacts are local rerun output,
not a cold-storage delivery. This script neither reruns proofs nor pins prose.
"""
import hashlib
import json
from pathlib import Path
import platform
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / 'topics/padua-mz-paper-20261113'
SHARP = ROOT / 'topics/padua-mz-sharp-constants-20261106'
FRONT = ROOT / 'topics/padua-mz-2d-frontier-20261105'


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def main():
    out = {'audited_head': 'be28d3267bf6117878190b10f2d29840e524eac7',
           'auditor': 'Codex, gpt-6-astra high (configured assignment)',
           'python': sys.version, 'platform': platform.platform(),
           'checker_sha256': digest(__file__), 'builds': {}, 'certificates': {},
           'limitations': ['PD-T376 exact witnesses unavailable; no pinned replay',
                           'Scratch files are not delivered or archived artifacts',
                           'Existing checkers share arithmetic dependencies; see audit report']}
    for paper, suffix, pages in [('paper', 'cc', 32), ('paper-sp', 'sp', 50)]:
        src = ROOT / 'tracks/mz-constants' / paper
        build = Path('/tmp/mz-audit-' + suffix)
        aux = dict(re.findall(r'\\newlabel\{([^}]+)\}\{\{([^}]*)\}',
                              (build / 'manuscript.aux').read_text()))
        correspondence = (TOPIC / ('correspondence-' + suffix + '.md')).read_text()
        frozen = correspondence.split('## Frozen numbering', 1)[1]
        labels = re.findall(r'^\| `([^`]+)` \| ([^|]+)\|', frozen, re.M)
        checked = 0
        for key, expected in labels:
            if key.endswith('@cref'):
                continue
            assert aux[key] == expected.strip(), (suffix, key, expected, aux.get(key))
            checked += 1
        info = subprocess.check_output(['pdfinfo', str(build / 'manuscript.pdf')], text=True)
        assert int(re.search(r'^Pages:\s+(\d+)', info, re.M)[1]) == pages
        fonts = subprocess.check_output(['pdffonts', str(build / 'manuscript.pdf')], text=True)
        assert 'Type 3' not in fonts
        issues = [s for s in (build / 'manuscript.log').read_text().splitlines()
                  if re.search(r'Warning|Overfull|Underfull|undefined|^!', s)
                  and 'infwarerr' not in s]
        assert not issues, issues
        out['builds'][suffix] = {
            'pages': pages, 'log_issues': issues, 'type3_fonts': False,
            'frozen_non_cref_labels_checked': checked,
            'tex_sha256': digest(src / 'manuscript.tex'),
            'bib_sha256': digest(src / 'refs.bib'),
            'pdf_sha256': digest(build / 'manuscript.pdf'),
            'pdflatex': subprocess.check_output(['pdflatex', '--version'], text=True).splitlines()[0]}
    for name, fresh, old, field in [
        ('P4_producer', '/tmp/mz-audit-P4-producer.json', 'P4-rayleigh.json', 'quotient'),
        ('P4_grouped', '/tmp/mz-audit-P4-grouped.json', 'P4-grouped-check.json', 'quotient'),
        ('P1_rectangle', '/tmp/mz-audit-P1.json', 'P1-rectangle-N16.json', 'r')]:
        receipt = read(fresh)
        assert receipt[field] == read(SHARP / 'evidence' / old)[field]
        if name.startswith('P4'):
            assert receipt['finite_threshold_pass']
        if name == 'P4_grouped':
            assert receipt['producer_enclosure_overlap']
        if name == 'P1_rectangle':
            assert receipt['strict_positive_lower']
        out['certificates'][name] = {
            'command': receipt['command'], 'exact_interval_matches_committed': True,
            'interval': receipt[field], 'receipt_sha256': digest(fresh),
            'seconds': receipt['seconds']}
    moderate = []
    for m in [10, 20, 30, 40, 60, 80]:
        fresh = Path('/tmp/mz-audit-native') / f'cert-m{m}.json'
        receipt = read(fresh)
        result = receipt['result']
        old = read(FRONT / 'evidence' / f'cert-m{m}.json')['result']
        dimension = m * (m+1) // 2
        assert result['dimension'] == dimension
        for check, previous, counts in zip(result['checks'], old['checks'],
                                            [(0, 1), (dimension-1, dimension)]):
            assert check['open_interval'] == previous['open_interval']
            for side, wanted in zip(['lower', 'upper'], counts):
                assert check[side]['negative'] == wanted
                assert check[side]['zero'] == 0
                assert all(int(b['minimum_strict_dominance_margin']) > 0
                           for b in check[side]['blocks'])
        moderate.append({'m': m, 'dimension': dimension,
                         'minimum': result['checks'][0]['open_interval'],
                         'maximum': result['checks'][1]['open_interval'],
                         'exact_counts_pass': True, 'committed_brackets_match': True,
                         'receipt_sha256': digest(fresh), 'seconds': result['wall_seconds']})
    out['moderate_degree_brackets'] = moderate
    independent = read('/tmp/mz-audit-native/independent-m10.json')
    assert independent['result']['verdict'] == 'PASS'
    out['independent_fraction_pencil'] = {
        'm': 10, 'verdict': 'PASS',
        'all_native_entries_compared': independent['result']['native_integer_entries_compared_as_rationals'],
        'offblock_pairs_checked': independent['result']['offblock_pairs_checked'],
        'seconds': independent['result']['seconds'],
        'receipt_sha256': digest('/tmp/mz-audit-native/independent-m10.json'),
        'command': independent['command'],
        'python_flint': independent['python_flint'], 'flint': independent['flint']}
    measured = read('/tmp/mz-audit-reproduction.json')
    assert measured['status'] == 'MEASURED'
    out['measured_rerun'] = {'command': measured['command'],
                             'numpy': measured['numpy'], 'scipy': measured['scipy'],
                             'cc_Nminus1': [{k: row[k] for k in ['N', 'lmin', 'lmax', 'eta']}
                                            for row in measured['results']['cc_Nminus1']],
                             'receipt_sha256': digest('/tmp/mz-audit-reproduction.json')}
    paths = [SHARP / 'code' / name for name in
             ['P4_rayleigh.py', 'P4_check_grouped.py', 'P1_rectangle.py', 'interval_dyadic.py']]
    paths += [FRONT / 'code' / name for name in
              ['cert_native.py', 'cert_pencil.c', 'independent_cert.py']]
    paths += [SHARP / 'evidence/P4-trial-J512.json',
              ROOT / 'tracks/mz-constants/code/reproduce.py']
    out['source_and_input_sha256'] = {str(p.relative_to(ROOT)): digest(p) for p in paths}
    target = TOPIC / 'audit-support/reruns.json'
    target.write_text(json.dumps(out, indent=2) + '\n')
    assert target.stat().st_size < 16384
    print('PASS', target, target.stat().st_size, 'bytes')


if __name__ == '__main__':
    main()
