#!/usr/bin/env python3
"""Recompute and check the committed finite Hahn normality receipt exactly."""
import hashlib
import json
from pathlib import Path
import re
import conditioning_exact_normality as producer


def main():
    receipt = Path(__file__).resolve().parents[1]/'theory/conditioning-hahn-normality-finite.md'
    payload = receipt.read_bytes()
    rows = re.findall(r'^\| (\d+) \| (\d+) \| `([0-9a-f]{64})` \| `([0-9a-f]{64})` \|$',payload.decode(),re.M)
    assert [int(row[0]) for row in rows]==list(range(4,65)), 'receipt coverage mismatch'
    total = 0
    for Ns,count,identity,digest in rows:
        result = producer.case(int(Ns),'hahn')
        assert result['passed'], 'zero interior divisor'
        assert result['interior_sites']==int(count), 'check-count mismatch'
        assert result['input_sha256']==identity, 'exact-input mismatch'
        assert result['exact_coefficient_payload_sha256']==digest, 'coefficient-payload mismatch'
        total += int(count)
    print(json.dumps(dict(status='PASS',sizes=61,exact_interior_checks=total,
                          checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                          producer_sha256=hashlib.sha256(Path(producer.__file__).read_bytes()).hexdigest(),
                          receipt_sha256=hashlib.sha256(payload).hexdigest()),sort_keys=True))


if __name__=='__main__':
    main()
