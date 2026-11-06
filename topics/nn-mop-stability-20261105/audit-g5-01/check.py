#!/usr/bin/env python3
"""Verify the auditor's source inventory and recorded output comparison.

This checks actual committed output data; it does not execute the third-party
source or independently authenticate the inaccessible paper reference table.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path
import zipfile

HERE = Path(__file__).resolve().parent
ARCHIVE_SHA256 = 'cdd0e98d2b411f24cfcecb49d83e16f9d50a7622a0d4f0d3eb17eb334a405145'


def require(ok, message):
    if not ok:
        raise ValueError(message)


def rows(path):
    value = [list(map(float, line.split())) for line in path.read_text().splitlines() if line.strip()]
    require(len(value) == 26 and all(len(row) == 7 for row in value), 'table dimensions: '+str(path))
    require([row[0] for row in value] == list(range(5, 31)), 'size coverage')
    require(all(math.isfinite(x) and x > 0 for row in value for x in row), 'nonpositive/nonfinite table field')
    return value


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--archive', type=Path, help='Optional supplied ZIP for full source-identity verification')
    args = ap.parse_args()
    receipt = json.loads((HERE/'receipt.json').read_text())
    for name, expected in receipt['files'].items():
        require(hashlib.sha256((HERE/name).read_bytes()).hexdigest() == expected, 'auditor artifact identity: '+name)
    if args.archive:
        payload = args.archive.read_bytes()
        require(hashlib.sha256(payload).hexdigest() == ARCHIVE_SHA256, 'supplied ZIP identity')
        inventory = json.loads((HERE/'source-inventory.json').read_text())
        with zipfile.ZipFile(args.archive) as z:
            require({x.filename for x in z.infolist() if not x.is_dir()} == {r['path'] for r in inventory}, 'ZIP file coverage')
            for row in inventory:
                data = z.read(row['path'])
                require(len(data) == row['bytes'] and hashlib.sha256(data).hexdigest() == row['sha256'], 'source identity: '+row['path'])
    result = []
    for expected in receipt['comparison']:
        family = expected['family']
        a = rows(HERE/('ours_'+family+'.dat'))
        b = rows(HERE.parent/'g5-run'/('ours_'+family+'.dat'))
        largest = max(abs(math.log10(x/y)) for u,v in zip(a,b) for x,y in zip(u[1:],v[1:]))
        require(math.isclose(largest, expected['max_log10_ratio'], rel_tol=1e-14), 'output comparison mismatch')
        row = dict(family=family, max_abs_log10_auditor_developer=largest)
        if family == 'kravchuk':
            measured = next(v[1] for v in a if v[0] == 10)
            paper = expected['paper_reference_from_receipt']
            ratio = math.log10(measured/paper)
            require(measured == expected['gate_error'] and abs(ratio) <= 1, 'selected reproduction gate')
            row.update(gate_error=measured, log10_ratio_to_quoted_paper=ratio, gate_pass=True)
        result.append(row)
    print(json.dumps(dict(status='PASS', archive_verified=args.archive is not None,
        paper_table_verified=False, comparison=result,
        checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()), sort_keys=True))


if __name__ == '__main__':
    main()
