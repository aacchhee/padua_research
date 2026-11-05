"""Versioned correction summary: never relabel or overwrite historical evidence."""
if not __debug__:
    raise RuntimeError('Scientific verification requires assertions; do not use -O.')

import hashlib
import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
OUT = Path('/workspace/padua-work/independent')
CHECK = REPO / 'topics/padua-argmax-effective-20261103/code/native_checker'
OLD_SUMMARY = '01df7fd5e61793e49a13eb216ba1a0a4402d6b799f87b94682677058459feeaf'
NEW_KERNEL = 'b0c871e7711219edfe3ce01480d8d1de3503a20d9b59f82b63a00eff248bc6e0'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    return json.loads(path.read_text())


def main():
    old_path = OUT/'independent-summary.json'
    assert digest(old_path) == OLD_SUMMARY
    old = read(old_path)
    assert digest(CHECK/'kernel.cpp') == NEW_KERNEL
    weight = OUT/'canonical-weight-differential.json'
    w = read(weight)
    assert w['source_sha256'] == NEW_KERNEL and w['total_weights'] == 23816
    assert all(d['exact_match'] and d['all_canonical'] for d in w['degrees'])
    corrected = []
    pending = []
    failures = []
    for n in (32, 40):
        receipt, run = OUT/f'canonical-check-n{n}.json', OUT/f'canonical-check-n{n}-run.json'
        if run.exists() and read(run)['returncode'] != 0:
            r = read(run)
            metrics = OUT/f'canonical-check-n{n}-resources.json'
            failures.append(dict(n=n, run_receipt_sha256=digest(run),
                                 returncode=r['returncode'], accepted=False,
                                 failure=r.get('failure'), kernel_sha256=r['kernel_sha256'],
                                 status='CPU cap reached' if 'SIGXCPU' in r.get('failure', '') else 'run failed',
                                 resources=read(metrics) if metrics.exists() else None,
                                 mathematical_rejection=False))
            continue
        if not receipt.exists() or not run.exists():
            pending.append(n)
            continue
        a, r = read(receipt), read(run)
        assert a['accepted'] and r['accepted'] and r['returncode'] == 0
        assert a['kernel_sha256'] == r['kernel_sha256'] == NEW_KERNEL
        assert digest(receipt) == r['checker_receipt_sha256']
        cert = Path(f'/workspace/padua-work/producer/final/n{n}.json.gz')
        assert digest(cert) == a['certificate_sha256'] == r['certificate_sha256']
        corrected.append(dict(n=n, accepted=True, certificate_sha256=digest(cert),
                              checker_receipt_sha256=digest(receipt), run_receipt_sha256=digest(run),
                              counts=a['counts'], seconds=a['seconds'], resources=r['resources'],
                              binary_sha256=a['binary_sha256'], kernel_sha256=NEW_KERNEL))
    result = dict(format='padua-independent-canonical-impact-v1',
                  rules_input_sha=old['rules_input_sha'], role=old['role'],
                  historical_native=dict(summary_sha256=OLD_SUMMARY,
                     kernel_sha256='ae4f20b69c5e676a5d2fefa55c903c8b3efd87a5807a5c5617ca21390a1cab3d',
                     degrees=[r['n'] for r in old['canonical_native_replay']],
                     status='historical observations only; not supporting corrected-native proof acceptance',
                     reason='noncanonical mpq operands violated GMP API precondition; bytes preserved'),
                  reference_g0_status='unaffected, valid independent Python producer/checker executions',
                  reference_source_sha256={k: v for k, v in old['source_sha256'].items()
                                           if 'padua-argmax-alln-20261101/code/part3/' in k},
                  reference_g0=old['reference_g0'],
                  unaffected_reference_controls=[r for r in old['controls']
                        if r['receipt'].endswith('-reference-controls.json') or
                           r['receipt'] == 'reference-n17-controls.json'],
                  corrected_source_sha256={p.name: digest(p) for p in
                        (CHECK/'kernel.cpp', CHECK/'check.py', CHECK/'controls.py')},
                  exact_weight_differential=dict(receipt_sha256=digest(weight), bytes=weight.stat().st_size,
                        degrees=[2, 40], total_weights=23816, all_exact_and_canonical=True,
                        source_impact_receipt_sha256=digest(OUT/'canonical-source-impact.json')),
                  corrected_native_replay=corrected, pending_corrected_degrees=pending,
                  failed_or_capped_corrected_runs=failures,
                  unverified_corrected_degrees=pending+[r['n'] for r in failures])
    output = OUT/'independent-summary-canonical.json'
    output.write_text(json.dumps(result, sort_keys=True, separators=(',', ':'))+'\n')
    print(json.dumps(dict(path=str(output), bytes=output.stat().st_size, sha256=digest(output),
                          corrected_degrees=[r['n'] for r in corrected], pending=pending,
                          failed_or_capped=[r['n'] for r in failures])))


if __name__ == '__main__':
    main()
