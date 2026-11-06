#!/usr/bin/env python3
"""Recompute the committed finite Hahn receipt; checks survive python -O."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import conditioning_exact_normality as producer


def verify(receipt):
    payload = receipt.read_bytes()
    text = payload.decode()
    sources = {
        'conditioning_exact_normality.py': Path(producer.__file__),
        'conditioning.py': Path(producer.cond.__file__),
        'c4_float_baseline.py': Path(producer.cond.base.__file__),
    }
    observed = {}
    for name, path in sources.items():
        pins = re.findall(r'- `' + re.escape(name) + r'`: `([0-9a-f]{64})`', text)
        if len(pins) != 1:
            raise ValueError('missing or duplicate code pin: ' + name)
        observed[name] = hashlib.sha256(path.read_bytes()).hexdigest()
        if observed[name] != pins[0]:
            raise ValueError('code identity mismatch: ' + name)
    rows = re.findall(r'^\| (\d+) \| (\d+) \| `([0-9a-f]{64})` \| `([0-9a-f]{64})` \|$', text, re.M)
    if [int(row[0]) for row in rows] != list(range(4, 65)):
        raise ValueError('receipt coverage mismatch')
    total = 0
    for Ns, count, identity, digest in rows:
        result = producer.case(int(Ns), 'hahn')
        checks = {
            'nonzero interior divisors': result['passed'],
            'check count': result['interior_sites'] == int(count),
            'exact input': result['input_sha256'] == identity,
            'coefficient payload': result['exact_coefficient_payload_sha256'] == digest,
        }
        for label, passed in checks.items():
            if not passed:
                raise ValueError('N=' + Ns + ': ' + label + ' mismatch')
        total += int(count)
    return dict(status='PASS', sizes=61, exact_interior_checks=total,
                checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                producer_sha256=observed['conditioning_exact_normality.py'],
                graph_sha256=observed['conditioning.py'],
                baseline_sha256=observed['c4_float_baseline.py'],
                receipt_sha256=hashlib.sha256(payload).hexdigest(),
                code_pins_verified=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--receipt', type=Path, default=Path(__file__).resolve().parents[1]/'theory/conditioning-hahn-normality-finite.md')
    args = ap.parse_args()
    print(json.dumps(verify(args.receipt), sort_keys=True))


if __name__ == '__main__':
    main()
