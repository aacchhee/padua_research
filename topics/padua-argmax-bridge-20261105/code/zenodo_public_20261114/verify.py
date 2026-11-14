#!/usr/bin/env python3
"""Verify the standalone public package; numerical replay is explicitly selected."""
import argparse
import copy
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parent
MODES = ('produce', 'verify')

def need(value, message):
    if not value:
        raise ValueError(message)

def loads(text):
    def pairs(items):
        d = {}
        for k, v in items:
            need(k not in d, 'duplicate JSON key')
            d[k] = v
        return d
    def finite_float(value):
        result = float(value)
        need(math.isfinite(result), 'nonfinite JSON number')
        return result
    return json.loads(text, object_pairs_hook=pairs, parse_float=finite_float,
                      parse_constant=lambda v: (_ for _ in ()).throw(ValueError(v)))

def load(path):
    return loads(path.read_bytes())

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def integrity(root=ROOT):
    checks = (root / 'SHA256SUMS').read_text().splitlines()
    names = set()
    for line in checks:
        sha, name = line.split('  ', 1)
        p = Path(name)
        need(not p.is_absolute() and '..' not in p.parts and name not in names, 'unsafe/duplicate checksum path')
        names.add(name)
        need((root / name).is_file() and not (root / name).is_symlink(), 'missing/unsafe file ' + name)
        need(digest(root / name) == sha, 'checksum ' + name)
    actual = {p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file()}
    need(actual == names | {'SHA256SUMS'}, 'package file population differs')
    manifest = load(root / 'MANIFEST.json')
    payload = manifest['payload']
    payload_paths = [r['path'] for r in payload]
    need(len(payload_paths) == len(set(payload_paths)), 'duplicate manifest payload path')
    need(set(payload_paths) == actual - {'MANIFEST.json', 'SHA256SUMS'}, 'manifest payload population differs')
    for row in payload:
        p = root / row['path']
        need(p.stat().st_size == row['bytes'] and digest(p) == row['sha256'], 'manifest payload identity ' + row['path'])
    expected = {(n, m) for n in range(41, 512) for m in MODES}
    rows = manifest['phase_inputs']
    need(len(rows) == 942 and {(r['n'], r['pass']) for r in rows} == expected, 'manifest phase scope')
    paths = {f'phase/inputs/n{n:04d}-{m}.json' for n, m in expected}
    need({r['path'] for r in rows} == paths, 'manifest phase paths')
    need({p.relative_to(root).as_posix() for p in (root/'phase/inputs').iterdir()} == paths, 'phase input population')
    data = {}
    for row in rows:
        p = root / row['path']
        need(p.stat().st_size == row['bytes'] and digest(p) == row['sha256'], 'phase manifest identity')
        d = load(p)
        need(type(d['n']) is int and d['n'] == row['n'], 'phase input degree')
        data[row['n'],row['pass']] = d
    fields = ['format','status','n','tree','pi_bracket','S_upper_columns','S_upper_rows','origin_lower_hex','lambda_upper_columns','lambda_upper_rows','norm','floor','corner','analytic_far']
    for n in range(41,512):
        need(all(data[n,'produce'][k] == data[n,'verify'][k] for k in fields), 'phase pair scientific fields')
    results = [loads(s) for s in (root/'phase/expected-results.jsonl').read_text().splitlines()]
    need(len(results) == 942 and {(r['n'],r['pass']) for r in results} == expected, 'expected result population')
    resultmap = {(r['n'],r['pass']):r for r in results}
    for n in range(41,512):
        need(all(r['accepted'] is True for r in (resultmap[n,m] for m in MODES)), 'expected rejected record')
        need({k:v for k,v in resultmap[n,'produce'].items() if k != 'pass'} == {k:v for k,v in resultmap[n,'verify'].items() if k != 'pass'}, 'expected scientific pair')
    poly = manifest['polynomial_inputs']
    need(len(poly) == 39 and {r['n'] for r in poly} == set(range(2,41)), 'polynomial scope')
    poly_paths = {f'polynomial/inputs/n{n:04d}.json.gz' for n in range(2,41)}
    need({r['path'] for r in poly} == poly_paths, 'polynomial manifest paths')
    need({p.relative_to(root).as_posix() for p in (root/'polynomial/inputs').iterdir()} == poly_paths, 'polynomial input population')
    for row in poly:
        p = root/row['path']
        need(digest(p) == row['sha256'] and p.stat().st_size == row['bytes'], 'polynomial input identity')
    polynomial_records(root, manifest)
    print('PASS integrity: 942 phase records / 471 degrees; 39 polynomial certificates', flush=True)
    return manifest, data, resultmap

def degrees(text, lo, hi):
    if text == 'all':
        return list(range(lo,hi+1))
    ns = [int(v) for v in text.split(',')]
    need(ns and len(set(ns)) == len(ns) and all(lo <= n <= hi for n in ns), 'degree selection')
    return sorted(ns)

def phase(data, expected, selected, controls):
    sys.path.insert(0,str(ROOT/'phase'))
    import check
    import controls as ctrl
    import runtime_probe
    runtime_probe.main()
    for n in selected:
        cache = {}
        for mode in MODES:
            result = check.check(data[n,mode],cache)
            want = {k:v for k,v in expected[n,mode].items() if k not in ('pass','accepted')}
            need(result == want, f'scientific result mismatch {n}/{mode}')
            print(f'PASS phase n={n} record={mode}',flush=True)
    if controls:
        negative = ctrl.corruption_controls(data[199,'produce'],{})
        base = data[41,'produce']; cache = {}; original = check.check(base,cache)
        changed = []
        for field in ('S_upper_rows','lambda_upper_rows'):
            d = copy.deepcopy(base)
            for row in d[field]: row[2] = (float.fromhex(row[2])+1.0).hex()
            changed.append(d)
        d = copy.deepcopy(base); d['origin_lower_hex'] = '0x0p+0'; changed.append(d)
        diag = {'native_S_upper_contained','native_lower_contained'}
        for d in changed:
            actual = check.check(d,cache)
            need({k:v for k,v in actual.items() if k not in diag} == {k:v for k,v in original.items() if k not in diag}, 'positive substitution')
        print(f'PASS controls: {len(negative)} corruptions rejected; 3 substitutions accepted',flush=True)

def polynomial_records(root, manifest):
    records = {}
    for name, lo, hi in [('degrees-2-16.json', 2, 16), ('degrees-17-32.json', 17, 32)]:
        rows = load(root/'polynomial/receipts'/name)['accepted_rows']
        need(len(rows) == hi-lo+1 and {r['n'] for r in rows} == set(range(lo,hi+1)), 'stored polynomial receipt scope')
        for row in rows:
            n = row['n']
            if n <= 16:
                need(row['actual_returncode'] == 0, 'stored polynomial return code')
            records[n] = dict(certificate_sha256=row['certificate_sha256'],
                              counts=dict(bound=row['bound_leaves'] if n <= 16 else row['bound'],
                                          corner=row['corner_leaves'] if n <= 16 else row['corner'],
                                          splits=row['splits']))
    for n in range(33,41):
        row = load(root/f'polynomial/receipts/n{n:04d}.json')
        need(row['n'] == n and all(row[k] is True for k in ('accepted','complete_partition','all_supplied_bounds_verified')), 'stored polynomial acceptance')
        records[n] = {k:row[k] for k in ('certificate_sha256','counts')}
    for row in manifest['polynomial_inputs']:
        need(records[row['n']]['certificate_sha256'] == row['sha256'], 'stored polynomial certificate identity')
    return records

def polynomial(selected, manifest):
    records = polynomial_records(ROOT, manifest)
    base = ROOT/'topics/padua-argmax-bridge-20261105/code/small_degree_unification'
    with tempfile.TemporaryDirectory(prefix='padua-public-') as tmp:
        tmp = Path(tmp); binary = tmp/'kernel'
        subprocess.run(['g++','-O3','-std=c++17',str(base/'metadata_kernel.cpp'),'-lgmpxx','-lgmp','-o',str(binary)],check=True,timeout=300)
        for n in selected:
            receipt = tmp/f'n{n}.json'
            subprocess.run([sys.executable,'-E','-B',str(base/'check.py'),str(ROOT/f'polynomial/inputs/n{n:04d}.json.gz'),'--binary',str(binary),'--output',str(receipt)],check=True,stdout=subprocess.DEVNULL)
            r = load(receipt)
            need(r['n'] == n and all(r[k] is True for k in ('accepted','complete_partition','all_supplied_bounds_verified')), 'polynomial acceptance')
            need({k:r[k] for k in ('certificate_sha256','counts')} == records[n], f'polynomial stored result mismatch {n}')
            print(f'PASS polynomial n={n}',flush=True)

def main():
    need(not sys.flags.optimize, 'Python optimization is not permitted')
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--degrees', help='phase degrees, e.g. 41,511 or all')
    p.add_argument('--polynomial-degrees',help='polynomial degrees, e.g. 2,17 or all')
    p.add_argument('--analytic',action='store_true')
    p.add_argument('--controls',action='store_true')
    a = p.parse_args()
    manifest, data, expected = integrity()
    if a.degrees or a.controls: phase(data,expected,degrees(a.degrees,41,511) if a.degrees else [],a.controls)
    if a.analytic:
        subprocess.run([sys.executable,'-E','-B',str(ROOT/'analytic/check.py')],check=True)
        subprocess.run([sys.executable,'-E','-B',str(ROOT/'analytic/base_table.py'),'--paper',str(ROOT/'analytic/tables/paper.tex'),'--companion',str(ROOT/'analytic/tables/companion.tex')],check=True)
        print('PASS analytic: exact gates and both 60-entry tables',flush=True)
    if a.polynomial_degrees: polynomial(degrees(a.polynomial_degrees,2,40),manifest)
    print('PASS requested verification',flush=True)

if __name__ == '__main__':
    main()
