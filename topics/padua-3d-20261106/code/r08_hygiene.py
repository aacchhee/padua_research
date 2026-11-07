#!/usr/bin/env python3
"""Audit03 supplemental replay. Hash code/data only; leave historical pins intact.

This is a developer replay/linkage check, not an independent audit. No prose file
is opened or hashed. Receipt limits are enforced before writing.
"""
import argparse
import hashlib
import itertools as it
import json
import math
import os
from pathlib import Path
import platform
import sys
import time

import numpy as np
import scipy
import scipy.linalg as la
import sympy

import t10_lattices as t
import independent_r06 as independent

TOP = Path(__file__).resolve().parents[1]
RULES = '9042e1c42964150f30fdbe8563c12ba6c6a8692a'


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def identity(path):
    path = Path(path)
    return [path.stat().st_size, sha(path)]


def read(path):
    return json.loads(Path(path).read_text())


def save(path, data):
    payload = json.dumps(data, separators=(',', ':')) + '\n'
    if len(payload.encode()) >= 16384:
        raise ValueError('receipt must remain below 16 KiB')
    Path(path).write_text(payload)


def common():
    paths = [Path(__file__), Path(t.__file__), Path(independent.__file__),
             Path(t.inherited.__file__), TOP/'code/t9_r06_complement.py',
             TOP/'code/t9_r06_manifest.py']
    return {'rules_read': RULES, 'command': sys.argv, 'seed': None,
            'versions': {'python': platform.python_version(), 'numpy': np.__version__,
                         'scipy': scipy.__version__, 'sympy': sympy.__version__},
            'threads': {k: os.getenv(k) for k in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS')},
            'code_inputs': {str(p): identity(p) for p in paths}}


def halfshifts(a):
    raw = read(a.census)
    counts = []; cases = 0
    for row in raw['rows']:
        B = np.array(row['B'], dtype=np.int64)
        q, H = t.group(B)
        # Denominator 2q permits pi shifts even for odd q.
        base = independent.fold(2 * H, 2 * q)
        shifted_counts = []
        for mask in it.product((0, 1), repeat=3):
            shifted = independent.fold(2 * H + q * np.array(mask), 2 * q)
            expected = sorted(tuple(q - x if z else x for x, z in zip(k, mask))
                              for k in base)
            assert shifted == expected
            assert len(shifted) == row['fold']
            shifted_counts.append(len(shifted)); cases += 1
        assert shifted_counts == row['halfshift_counts']
        assert row['halfshift_ranks'] == [row['rank']] * 8
        counts.append([row['n'], row['family'], row['det'], row['fold'], row['rank']])
    return {'status': 'EXACT folded counts replayed; shifted ranks are derived',
            'inputs': {str(a.census): identity(a.census)}, 'lattices': len(counts),
            'shift_cases': cases, 'all_eight_counts_match': True,
            'columns': ['n', 'family', 'det', 'fold', 'unshifted_rank'], 'rows': counts,
            'rank_method': 'Derived, not eight rank computations: x_j -> (-1)^mask_j x_j is a node bijection, and T_alpha((-1)^mask x)=(-1)^(alpha dot mask) T_alpha(x). Hence the evaluation matrix changes by an invertible row permutation and diagonal column signs.',
            'historical_fields': 't10_lattices.py halfshift_counts/ranks were analytic copies, not independently measured ranks. Half-period means pi, not half a grid step.'}


def selections(a):
    raw = read(a.census); old = read(TOP/'evidence/t10-subset-rank.json')
    quality = read(a.quality_raw); quality_receipt = read(TOP/'evidence/t10-quality.json')
    assert sha(a.census) == quality_receipt['input_sha256'] == old['input_sha256']
    assert identity(a.quality_raw) == [quality_receipt['raw_bytes'], quality_receipt['raw_sha256']]
    rows = []
    for n in range(2, 8):
        N = math.comb(n+3, 3)
        best = min((r for r in raw['rows'] if r['n'] == n and r['rank'] == N),
                   key=lambda r: (r['fold'], r['det'], r['family']))
        q, keys, weights, points = t.folded(np.array(best['B']))
        ids = la.qr(t.basis(points, n).T, pivoting=True, mode='economic', check_finite=False)[2][:N]
        selected = [keys[int(i)] for i in ids]
        payload = json.dumps({'denominator': q, 'selected_folded_keys': selected}, separators=(',', ':')).encode()
        nodehash = hashlib.sha256(payload).hexdigest()
        prior = next(r for r in old['rows'] if r[0] == n)
        assert nodehash == prior[-1]
        C, diag = t.interpolate(points[ids], n)
        assert C is not None
        ref = next(r for r in quality['rows'] if r['n'] == n and r['name'] == 'extract-QR')
        replay = [t.mesh_norm(C, n, side, 120) for side in (21, 41)]
        assert all(r['complete'] for r in replay)
        differences = [abs(r['lower_bound']-s['lower_bound']) for r,s in zip(replay,ref['meshes'])]
        assert max(differences) < 1e-7
        assert abs(diag['condition']-ref['condition']) < 1e-7 * ref['condition']
        # Different matrix basis and fresh splitting prime from the old cert.
        k = (prior[2]-1)//q + 1
        while not sympy.isprime(k*q+1):
            k += 1
        cert = independent.actual_certificate(selected, q, n, k*q+1)
        assert cert['rank_lower'] == N
        rows.append([n, nodehash, q, cert['prime'], cert['root'], cert['rank_lower'],
                     [r['lower_bound'] for r in replay], max(differences)])
    return {'status': 'MEASURED quality replay and exact fresh-prime rank check for same hashed selections',
            'inputs': {str(p): identity(p) for p in (a.census, a.quality_raw,
                TOP/'evidence/t10-quality.json', TOP/'evidence/t10-subset-rank.json')},
            'columns': ['n', 'selected_node_sha256', 'q', 'fresh_prime', 'root', 'rank', 'norm21_norm41', 'max_mesh_delta'],
            'rows': rows,
            'limitation': 'Original n2..7 quality raw did not save selected-node hashes. This closes the link by rerunning its exact selection algorithm and matching both full-precision mesh norms to the hash-authenticated quality raw; it does not invent historical selection logs.'}


def complement(a):
    old = read(TOP/'evidence/t9-r06-complement.json')
    fresh = read(TOP/'evidence/r08-hygiene-complement-producer.json')
    assert fresh['code_sha256'] == sha(TOP/'code/t9_r06_complement.py')
    assert 'theory/t10-parity-log4.md' not in fresh['inputs']
    owner = read(TOP/'evidence/t10-census.json')
    def count(n):
        return (n//2+1)*((n+1)//2+1)**2 + ((n+1)//2)*((n+2)//2)**2
    rows = [[n, math.comb(n+3, 3), 2*n*(n+1)**2, count(n), math.comb(n+3,3), (19*n**3+107)//108]
            for n in range(1,110)]
    assert rows == old['rows']
    assert rows == fresh['rows']
    assert fresh['dense_feasibility'] == old['dense_feasibility']
    assert all(count(r['n']) == r['fold'] for r in owner['best_full_rank'])
    probes = []
    for n in (17,24,32):
        B = np.array([[n,n+1,0],[0,n+1,n+1],[0,0,2*(n+1)]], dtype=np.int64)
        started = time.process_time(); q, keys, weights, points = t.folded(B)
        rank = t.exact_rank(B,n,2*n)
        payload = json.dumps({'denominator':q,'folded_keys':keys,'multiplicities':np.rint(weights*q).astype(int).tolist()}, separators=(',',':')).encode()
        nodehash = hashlib.sha256(payload).hexdigest()
        ref = next(r for r in old['timed_probes'] if r['n'] == n)
        assert (len(keys),rank,nodehash) == (ref['fold'],ref['rank'],ref['exact_node_sha256'])
        probes.append([n,len(keys),rank,nodehash,time.process_time()-started])
    return {'status':'EXACT family numerical fields replayed; no prose input or global minimum claim',
            'inputs':{str(p):identity(p) for p in (TOP/'evidence/t9-r06-complement.json',TOP/'evidence/t10-census.json',TOP/'evidence/r08-hygiene-complement-producer.json')},
            'rows_1_to_109_equal':True,'probes_columns':['n','fold','rank','node_sha256','cpu_seconds'],'probes':probes,
            'historical_prose_pin_disposition':'The old complement receipt inputs/theory entry is historical and invalid as a reproducible input identity. It is not used by this replay. Current scientific fields depend on the code/data inputs only.',
            'independent_algebra':independent.t9_algebra()}


def raw_inventory(a):
    paths = [TOP/'evidence/legacy-t9-metadata-r06.json']
    paths += sorted((TOP/'evidence').glob('t7-r06-*.json'))
    paths += sorted((TOP/'evidence').glob('t8-r06-*.json'))
    found = {}
    def add(path, size, digest, receipt):
        if not str(path).startswith('/tmp/'):
            return
        item = [int(size), str(digest), str(receipt.relative_to(TOP))]
        if path in found:
            assert found[path][:2] == item[:2]
        else:
            found[path] = item
    def walk(value, receipt):
        if isinstance(value,dict):
            if {'path','bytes','sha256'} <= value.keys():
                add(value['path'],value['bytes'],value['sha256'],receipt)
            if {'scratch','raw_bytes','raw_sha256'} <= value.keys():
                add(value['scratch'],value['raw_bytes'],value['raw_sha256'],receipt)
            for child in value.values():
                walk(child,receipt)
        elif isinstance(value,list):
            for child in value:
                walk(child,receipt)
    for path in paths:
        walk(read(path),path)
    assert len(found) == 51, len(found)
    assert sum(r[0] for r in found.values()) == 54836138
    missing = []; rows = []
    for path, (size,digest,receipt) in sorted(found.items()):
        if Path(path).is_file():
            assert identity(path) == [size,digest],path
        else:
            missing.append(path)
        rows.append([path,size,digest,receipt])
    assert not missing, missing
    save(a.inventory, {'status':'51 existing raw paths stream-hashed and matched',
         'columns':['path','bytes','sha256','source_receipt'],'rows':rows})
    return {'status':'PASS actual streaming SHA-256 and byte comparison',
            'scope':'26 legacy-T9 raw arrays plus 25 T7/T8 round06 raw paths; excludes the five T10 raw identities and T9-r06 node-only hashes',
            'checked_files':len(found),'checked_bytes':sum(r[0] for r in found.values()),
            'missing_paths':missing,'inventory':{str(a.inventory):identity(a.inventory)},
            'receipt_inputs':{str(p.relative_to(TOP)):identity(p) for p in paths}}


def pin_check(a):
    pins = read(TOP/'evidence/independent-r06-pins.json')
    for path, expected in pins['files'].items():
        assert path.startswith('code/'), 'prose pin rejected'
        assert identity(TOP/path) == expected, path
    manifests = [TOP/'evidence/t9-r06-run-manifest.json',
                 TOP/'evidence/r08-hygiene-t9-manifest.json']
    for path in manifests:
        manifest = read(path)
        assert 'record_sha256' not in manifest
        for row in manifest['receipts']:
            assert identity(TOP/row['receipt']) == [row['bytes'],row['sha256']]
    return {'status':'PASS code pins and receipt identities; no theory or other prose pins',
            'code_pins':len(pins['files']),'manifest_receipts_checked':18,
            'inputs':{str(p):identity(p) for p in [TOP/'evidence/independent-r06-pins.json']+manifests},
            'historical_executions':'Historical generator hashes are execution metadata. Current code pins were refreshed only for the two edited generators; fresh manifest and complement producer replays are separate receipts.'}


def main():
    p=argparse.ArgumentParser()
    p.add_argument('mode',choices=('halfshifts','selections','complement','raw-inventory','pins'))
    p.add_argument('--census',type=Path,default=Path('/tmp/padua-t10-20261106-7afa6a54/census.json'))
    p.add_argument('--quality-raw',type=Path,default=Path('/tmp/padua-t10-20261106-7afa6a54/t10-quality-raw.json'))
    p.add_argument('--inventory',type=Path)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args(); started=time.process_time(); data=common()
    data['result']={'halfshifts':halfshifts,'selections':selections,'complement':complement,'raw-inventory':raw_inventory,'pins':pin_check}[a.mode](a)
    data['cpu_seconds']=time.process_time()-started
    save(a.out,data)
    print(json.dumps({'output':str(a.out),'bytes':a.out.stat().st_size,'cpu_seconds':data['cpu_seconds']}))


if __name__=='__main__':
    main()
