"""Compact, hash-bound independent evidence receipt; never invent pending runs."""
if not __debug__:
    raise RuntimeError("Scientific verification requires assertions; do not use -O or PYTHONOPTIMIZE.")

import gzip
import hashlib
import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
TOPIC = REPO / 'topics/padua-argmax-effective-20261103'
REF = REPO / 'topics/padua-argmax-alln-20261101/code/part3'
OUT = Path('/workspace/padua-work/independent')
NATIVE = Path('/workspace/padua-work/producer/final')


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    data = path.read_bytes()
    return json.loads(gzip.decompress(data) if path.suffix == '.gz' else data)


def mathematical(data):
    ignored = {'setup_seconds', 'search_seconds', 'total_seconds', 'producer_provenance'}
    return {k: v for k, v in data.items() if k not in ignored}


def main():
    # This summarizes the original execution, not later corrected kernels.
    # Never relabel old native receipts with a new current source hash.
    assert digest(TOPIC/'code/native_checker/kernel.cpp') == 'ae4f20b69c5e676a5d2fefa55c903c8b3efd87a5807a5c5617ca21390a1cab3d', \
        'Historical native summary: use canonical impact records for corrected source.'
    reference = []
    native = []
    controls = []
    for n in range(9, 33):
        cert = NATIVE / f'n{n}.json.gz'
        receipt = OUT / f'native-final-check-final-n{n}.json'
        if cert.exists() and receipt.exists():
            d, c = read(cert), read(receipt)
            assert c['accepted'] and c['certificate_sha256'] == digest(cert)
            native.append(dict(n=n, certificate_sha256=digest(cert), bytes=cert.stat().st_size,
                               checker_receipt_sha256=digest(receipt), accepted=True,
                               leaves=len(d['leaves']), depth=d['statistics']['maximum_depth'],
                               checker_seconds=c['seconds']))
        cert = OUT / f'reference-n{n}.json'
        receipt = OUT / f'reference-n{n}-check.json'
        if cert.exists() and receipt.exists():
            d, c = read(cert), read(receipt)
            assert c['accepted'] and c['certificate_sha256'] == digest(cert)
            e = read(NATIVE / f'n{n}.json.gz')
            assert mathematical(d) == mathematical(e), f'mathematical disagreement n={n}'
            content = json.dumps(mathematical(d), sort_keys=True, separators=(',', ':')).encode()
            reference.append(dict(n=n, certificate_sha256=digest(cert), bytes=cert.stat().st_size,
                                  checker_receipt_sha256=digest(receipt), accepted=True,
                                  producer_seconds=d['total_seconds'], checker_seconds=c['seconds'],
                                  leaves=len(d['leaves']), depth=d['statistics']['maximum_depth'],
                                  native_mathematical_payload_equal=True,
                                  mathematical_payload_sha256=hashlib.sha256(content).hexdigest()))
    for name in ('native-final-n9-reference-controls.json', 'reference-n17-native-final-controls.json',
                 'reference-n17-controls.json'):
        p = OUT / name
        if not p.exists():
            continue
        c = read(p)
        assert c['positive_complete_accepted'] and c['positive_partial_not_accepted']
        controls.append(dict(receipt=name, receipt_sha256=digest(p), n=c['n'],
                             input_certificate_sha256=c['certificate_sha256'],
                             negative_count=c['negative_count'], complete_accepted=True,
                             partial_not_accepted=True, seconds=c['seconds']))
    paths = [REF / name for name in ('finite_general.py', 'finite_general_run.py', 'finite_general_check.py',
             'finite_general_controls.py', 'finite_bernstein.py', 'finite_n2_exact.py', 'proof_runtime.py')]
    paths += [TOPIC / 'code' / part / name for part, name in (
        ('native_producer', 'producer.c'), ('native_producer', 'run.py'),
        ('native_checker', 'kernel.cpp'), ('native_checker', 'check.py'), ('native_checker', 'controls.py'))]
    result = dict(format='padua-effective-supplementary-check-v1',
                  rules_input_sha='8a1f394739293953e1566fd24a0a193cc78ff26f',
                  role='Codex, configured gpt-6-astra high; supplementary, not Claude audit',
                  independent_output_root=str(OUT), canonical_native_root=str(NATIVE),
                  source_sha256={str(p.relative_to(REPO)): digest(p) for p in paths},
                  native_binary_sha256=digest(OUT/'checker-kernel-final'),
                  reference_g0=reference, canonical_native_replay=native, controls=controls,
                  pending_reference_degrees=[n for n in range(17, 25) if n not in {r['n'] for r in reference}])
    p = OUT / 'independent-summary.json'
    p.write_text(json.dumps(result, sort_keys=True, separators=(',', ':'))+'\n')
    print(json.dumps(dict(path=str(p), sha256=digest(p), bytes=p.stat().st_size,
                          reference_degrees=[r['n'] for r in reference],
                          native_degrees=[r['n'] for r in native])))


if __name__ == '__main__':
    main()
