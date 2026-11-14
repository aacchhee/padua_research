#!/usr/bin/env python3
"""Validate and summarize fresh PD-T376 readiness regenerations.

Run the frozen commands recorded in readiness-witness-replay.md first. This
checker consumes local scratch results and emits one small essential receipt;
it neither creates nor claims a deposit/cold-storage delivery.
"""
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import platform
import subprocess
import sys

import flint
import numpy
import scipy

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / 'topics/padua-mz-paper-20261113'
CLEAN = ROOT / 'topics/padua-mz-cleanup-20261105'
DATA = Path('/tmp/mz-readiness-data')
FROZEN = '39479ffca76052ea79f90c2e5e0c4bfc80bf1584'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def main():
    spec = importlib.util.spec_from_file_location('compare_receipts', TOPIC / 'zenodo/compare_receipts.py')
    comparator = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(comparator)
    code = read(DATA / 'audit-receipts/code-identities.json')
    for rel, identity in code.items():
        blob = subprocess.check_output(['git', 'show', FROZEN + ':' + rel], cwd=ROOT)
        assert blob == (ROOT / rel).read_bytes()
        assert sha(ROOT / rel) == identity['sha256']
    pinned = {r['m']: r for r in read(CLEAN / 'evidence/witness-payload-identities.json')['witnesses']}
    scan = read(DATA / 'audit-receipts/scan.json')
    scan_rows = {r['m']: r for r in scan['results']}
    result = {
        'audit_input_head': '9705c75876a74ac6bcce5625d20a45e3676c1992',
        'frozen_code_commit': FROZEN,
        'auditor': 'Codex gpt-6-astra high (inherited configured assignment)',
        'scope': 'Fresh source-vector generation, exact polynomial reconstruction, producer and independent checker; no new mathematical result',
        'python': sys.version, 'numpy': numpy.__version__, 'scipy': scipy.__version__,
        'python_flint': flint.__version__, 'flint': flint.__FLINT_VERSION__,
        'platform': platform.platform(),
        'thread_environment': 'OPENBLAS_NUM_THREADS=OMP_NUM_THREADS=MKL_NUM_THREADS=1',
        'code_identity': code, 'summary_checker_sha256': sha(__file__),
        'scan_command': scan['command'], 'witnesses': [],
        'limitations': ['Scratch files are regenerated local outputs, not a verified delivery to AC',
                        'Independent checker assumes its stated IEEE BLAS gamma_k model',
                        'Gzip-container identities may differ with zlib; decompressed JSON identity is decisive']}
    for m in [1101, 1240, 1600]:
        vector = DATA / f'source-vectors/m{m}-n{m-1}-min.npy'
        witness = DATA / f'witnesses/cert-m{m}/witness.json.gz'
        norm = witness.with_name('exact-norm.txt')
        producer_path = DATA / f'audit-receipts/producer-m{m}.json'
        checker_path = DATA / f'audit-receipts/independent-m{m}.json'
        producer = read(producer_path)
        independent = read(checker_path)
        old_producer = read(CLEAN / f'evidence/witness-producer-m{m}.json')
        old_independent = read(CLEAN / f'evidence/witness-independent-m{m}.json')
        payload = gzip.decompress(witness.read_bytes())
        assert sha(vector) == old_producer['witness']['source_vector_sha256']
        assert hashlib.sha256(payload).hexdigest() == pinned[m]['payload_sha256']
        assert sha(norm) == old_producer['exact_norm']['sha256']
        assert producer['witness']['source_vector_sha256'] == sha(vector)
        assert producer['sign'] == independent['sign'] == 'negative'
        assert independent['accepted'] is True
        assert producer['exact_norm']['sign'] == 'positive'
        diffs = []
        comparator.walk(producer, old_producer, '', diffs)
        comparator.walk(independent, old_independent, '', diffs)
        assert not diffs, diffs
        row = {
            'm': m, 'n': m-1,
            'source_vector_sha256': sha(vector), 'source_vector_matches_original': True,
            'payload_sha256': hashlib.sha256(payload).hexdigest(), 'payload_bytes': len(payload),
            'payload_matches_original': True, 'exact_norm_sha256': sha(norm),
            'exact_norm_matches_original': True,
            'gzip_sha256': sha(witness), 'gzip_bytes': witness.stat().st_size,
            'gzip_matches_original': sha(witness) == old_producer['witness']['sha256'],
            'producer_sign': producer['sign'], 'positive_exact_norm': True,
            'producer_energy_enclosure': producer['energy_enclosure'],
            'producer_rayleigh_enclosure': producer['rayleigh_enclosure'],
            'independent_sign': independent['sign'], 'independent_accepted': independent['accepted'],
            'independent_q_enclosure': independent['q_enclosure'],
            'original_receipt_comparisons_pass': True,
            'scan_seconds': scan_rows[m]['seconds'], 'producer_seconds': producer['seconds'],
            'independent_seconds': independent['total_seconds'],
            'producer_command': producer['command'], 'independent_command': independent['command'],
            'producer_receipt_sha256': sha(producer_path),
            'independent_receipt_sha256': sha(checker_path)}
        result['witnesses'].append(row)
    result['verdict'] = 'PASS: all three vectors, exact payloads and norms match; both sign paths accept'
    target = TOPIC / 'audit-support/readiness-witness-replay.json'
    target.write_text(json.dumps(result, indent=2) + '\n')
    assert target.stat().st_size < 16384
    print('PASS', target, target.stat().st_size, 'bytes')


if __name__ == '__main__':
    main()
