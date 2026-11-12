#!/usr/bin/env python3
"""Compact canonical parity subset delivery and exact finite-field minor check.

No quality estimate or rounded binary64 matrix rank is certified. Exact geometry
is cos(pi*i_j/m_j); load() gives the original NumPy evaluation recipe. Build
reads pinned raw provenance once; verify and load never read raw scratch files.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import itertools as it
import json
import math
import os
from pathlib import Path
import platform
import sys
import subprocess
import time
import numpy as np

TOP = Path(__file__).resolve().parents[1]
SCHEMA = 'pdpr-canonical-parity-v1'
SOURCE_COMMITS = {12: '562309744165cd601a489510ddc8026d933b1b27',
                  16: 'e761a12bcc7acfbf47dc6db77592854211931df5'}
LEGACY_SOURCE12 = '46d1e2b9356e0e5cc385615906c500684cd9ad77'
LIMIT = 16384

def require(test, message):
    if not test:
        raise ValueError(message)

def sha(data):
    return hashlib.sha256(data).hexdigest()

def identity(path):
    p = Path(path)
    return {'path': str(p), 'bytes': p.stat().st_size, 'sha256': sha(p.read_bytes())}

def dump(path, obj):
    data = (json.dumps(obj, separators=(',', ':'), allow_nan=False)+'\n').encode()
    require(len(data) < LIMIT, 'one logical evidence file exceeds 16KiB')
    Path(path).write_bytes(data)

def alpha(n):
    return [(a, b, d-a-b) for d in range(n+1) for a in range(d+1) for b in range(d-a+1)]

def grid(orders):
    return np.array([i for i in it.product(*(range(m+1) for m in orders))
                     if i[0] % 2 == i[1] % 2 == i[2] % 2], dtype=np.int64)

def validate(record):
    require(record['schema'] == SCHEMA, 'schema mismatch')
    n, orders, ids = record['n'], record['orders'], record['ids']
    require(type(n) is int and n >= 1, 'invalid degree')
    require(all(type(m) is int for m in orders) and orders == [n, n+1, n+1], 'noncanonical anisotropic orders')
    require(len(grid(orders)) == math.prod(m//2+1 for m in orders)+math.prod((m+1)//2 for m in orders), 'parity grid count')
    require(len(alpha(n)) == math.comb(n+3,3) and len(set(alpha(n))) == len(alpha(n)), 'exponent count/uniqueness')
    require(all(type(i) is int for i in ids) and ids == sorted(set(ids)), 'IDs not unique sorted integers')
    require(type(record['N']) is int and type(record['M']) is int and record['N'] == math.comb(n+3, 3) and record['M'] == len(ids) >= record['N'], 'count mismatch')
    require(0 <= ids[0] and ids[-1] < len(grid(orders)), 'ID outside parity support')
    require(record['id_order'] == 'itertools.product(range(m_j+1)); i3 fastest; retain equal index parities', 'ID convention')
    require(record['basis_order'] == 'd=0..n,a=0..d,b=0..d-a; (a,b,d-a-b); unscaled product Chebyshev T', 'basis convention')
    return n, orders, ids

def load(payload):
    """Return physical M-by-3 binary64 nodes, reconstructed without raw files."""
    record = json.loads(Path(payload).read_text()) if isinstance(payload, (str, Path)) else payload
    _, orders, ids = validate(record)
    return np.cos(np.pi*grid(orders)[ids]/np.array(orders))

def factors(value):
    out, q = [], 2
    while q*q <= value:
        if value % q == 0:
            out.append(q)
            while value % q == 0:
                value //= q
        q += 1
    if value > 1:
        out.append(value)
    return out

def prime(p):
    return type(p) is int and p >= 2 and all(p % q for q in range(2, math.isqrt(p)+1))

def field(p, rho, L):
    require(type(p) is int and 2 < p < 2**30 and (p-1)**2+(p-1) <= np.iinfo(np.int64).max, 'int64 intermediate overflow bound')
    require(prime(p) and p % 2 == 1 and (p-1) % L == 0, 'invalid prime field')
    require(type(rho) is int and 1 <= rho < p and pow(rho,L,p) == 1
            and all(pow(rho,L//q,p) != 1 for q in factors(L)), 'rho not exact order L')

def matrix(record, p, rho, ids=None):
    n, orders, allids = validate(record)
    L = math.lcm(*(2*m for m in orders))
    field(p, rho, L)
    indices = grid(orders)[allids if ids is None else ids]
    tabs = []
    for j, m in enumerate(orders):
        z = [pow(rho, L//(2*m)*int(i), p) for i in indices[:,j]]
        x = np.array([((v+pow(v,-1,p))*pow(2,-1,p)) % p for v in z], dtype=np.int64)
        t = np.ones((len(indices), n+1), dtype=np.int64)
        t[:,1] = x
        for k in range(2,n+1):
            # Reduce x*T before multiplying by 2: every product is bounded.
            t[:,k] = (2*((x*t[:,k-1]) % p)-t[:,k-2]) % p
        tabs.append(t)
    return np.column_stack([(((tabs[0][:,a]*tabs[1][:,b]) % p)*tabs[2][:,c]) % p
                            for a,b,c in alpha(n)])

def minor(A, p, labels):
    """Deterministic row-pivot elimination; ordered chosen rows define minor.

    Each update uses one outer product with reduction, never an int64 dot.
    The returned determinant is for the ORIGINAL rows in pivot-selection order;
    rectangular row swaps do not add a determinant sign in that convention.
    """
    A, labels, chosen, determinant = A.copy(), list(labels), [], 1
    for k in range(A.shape[1]):
        hits = np.flatnonzero(A[k:,k])
        if not len(hits):
            return k, chosen, 0
        r = k+int(hits[0])
        if r != k:
            A[[k,r]] = A[[r,k]]
            labels[k], labels[r] = labels[r], labels[k]
        chosen.append(labels[k])
        pivot = int(A[k,k])
        determinant = determinant*pivot % p
        f = A[k+1:,k]*pow(pivot,-1,p) % p
        A[k+1:,k:] = (A[k+1:,k:] - (f[:,None]*A[k,k:][None,:]) % p) % p
    return A.shape[1], chosen, determinant

def certify(record):
    _, orders, ids = validate(record)
    L = math.lcm(*(2*m for m in orders))
    attempts = []
    for k in range(1,257):
        p = k*L+1
        if not prime(p):
            continue
        rho = next((pow(h,k,p) for h in range(2,min(p,258))
                    if pow(pow(h,k,p),L,p) == 1 and
                    all(pow(pow(h,k,p),L//q,p) != 1 for q in factors(L))), None)
        if rho is None:
            attempts.append({'p': p, 'failure': 'bounded root search'})
            continue
        rank, rows, det = minor(matrix(record,p,rho),p,ids)
        attempts.append({'p': p, 'rho': rho, 'rank': rank})
        if rank == record['N']:
            return {'L': L, 'p': p, 'rho': rho, 'minor_row_ids': rows,
                    'det_mod_p': det, 'attempts': attempts,
                    'search': 'k=1..256,p=kL+1 prime; first h=2..min(p-1,257) giving order-L h^k; first full rank; fixed node IDs'}
    raise ValueError('bounded search exhausted; no real rank-deficiency conclusion; attempts='+str(attempts))

def verify(record):
    n, orders, ids = validate(record)
    c = record['certificate']
    if 'provenance' in record:
        pin = record['provenance']['receipt']
        rp = TOP/'evidence'/Path(pin['path']).name
        require(rp.stat().st_size == pin['bytes'] and sha(rp.read_bytes()) == pin['sha256'], 'scientific receipt pin differs')
        expected = {SOURCE_COMMITS.get(n)} | ({LEGACY_SOURCE12} if n == 12 else set())
        require(record['provenance']['scientific_source_commit'] in expected, 'scientific source commit differs')
        require(record['provenance']['published_result_commit'] == SOURCE_COMMITS.get(n), 'published result commit differs')
    require(c['L'] == math.lcm(*(2*m for m in orders)), 'L mismatch')
    require(type(c['L']) is int and type(c['det_mod_p']) is int, 'noninteger certificate metadata')
    rows = c['minor_row_ids']
    require(len(rows) == record['N'] and len(set(rows)) == len(rows)
            and all(type(i) is int and i in ids for i in rows), 'minor IDs mismatch')
    rank, chosen, det = minor(matrix(record,c['p'],c['rho'],rows),c['p'],rows)
    # For the square minor, a pivot swap would change ordered rows; account
    # for its permutation. The build's pivot order normally needs no swaps.
    perm = [rows.index(i) for i in chosen]
    inversions = sum(perm[i]>perm[j] for i in range(len(perm)) for j in range(i+1,len(perm)))
    det = det*(-1 if inversions % 2 else 1) % c['p']
    require(rank == record['N'] and det == c['det_mod_p'] and 0 < det < c['p'], 'nonzero exact minor check failed')
    linked = sha(np.asarray(load(record),dtype='<f8').tobytes()) == record['binary64_link']['sha256']
    # Binary64 reconstruction can differ across libm versions; exact geometry
    # and modular proof are independent of this measured runtime linkage.
    return {'exact_full_column_rank': True, 'n':n, 'orders':orders, 'M':len(ids), 'N':record['N'],
            'full_parity_count':len(grid(orders)), 'rank': rank, 'det_mod_p': det,
            'L':c['L'], 'L_prime_factors':factors(c['L']), 'p':c['p'], 'rho':c['rho'],
            'primality':'complete trial division through isqrt(p)',
            'order_test_residues':[[q,pow(c['rho'],c['L']//q,c['p'])] for q in factors(c['L'])],
            'rho_power_L':pow(c['rho'],c['L'],c['p']),
            'arithmetic':'NumPy int64; p<2^30; reduce each product before next multiplication; no dot summation',
            'fixed_candidate_ids_sha256':sha(json.dumps(ids,separators=(',',':')).encode()),
            'binary64_reconstruction_matches_measured_hash': linked,
            'scope': 'exact cos-grid determining set/unique positive-weight LS; no continuous norm, numerical conditioning or N-site interpolation claim'}

def build(receipt_path, n, publication):
    require(n in SOURCE_COMMITS and publication == SOURCE_COMMITS[n], 'unsupported degree/publication pin')
    source_commit = SOURCE_COMMITS[n]
    receipt_path = Path(receipt_path)
    receipt = json.loads(receipt_path.read_text())
    def pinned(pin):
        require(identity(pin['path']) == pin, 'raw provenance changed: '+pin['path'])
        return Path(pin['path'])
    details = json.loads(pinned(receipt['raw_details']).read_text())
    inventory = json.loads(pinned(receipt['raw_inventory']).read_text())
    for pin in inventory:
        pinned(pin)
    source_files = subprocess.check_output(['git','ls-tree','-r','--name-only',source_commit], cwd=TOP.parents[1], text=True).splitlines()
    for pin in receipt['executed_source_snapshots']:
        pinned(pin)
        basename = Path(pin['path']).name.removeprefix('source-')
        matches = [f for f in source_files if Path(f).name == basename]
        originals = [subprocess.check_output(['git','show',source_commit+':'+f],cwd=TOP.parents[1]) for f in matches]
        require(any(len(v) == pin['bytes'] and sha(v) == pin['sha256'] for v in originals), 'official source commit differs: '+basename)
    path = next(x for x in details['paths'] if x['n'] == n and x['rule'] == 'A')
    M, N = path['primary_M'], path['N']
    checkpoint = path['primary_prefix']['checkpoint']
    require(checkpoint in inventory and M == math.ceil(1.20*N), 'primary checkpoint identity/count')
    raw = pinned(checkpoint).parent
    pathpin = next(x for x in inventory if x['path'] == str(raw/f'n{n}-A-path.npz'))
    recipepin = next(x for x in inventory if x['path'] == str(raw/f'n{n}-recipe.json'))
    map_pin = next(x for x in inventory if x['path'] == str(raw/f'n{n}-A-m{M}-map.npz'))
    recipe = json.loads(pinned(recipepin).read_text())
    with np.load(pinned(checkpoint),allow_pickle=False) as z:
        ids, nodes = z['ids'].copy(), z['nodes'].copy()
    with np.load(pinned(pathpin),allow_pickle=False) as z:
        require(np.array_equal(ids,z[f'm{M}']), 'checkpoint/path IDs differ')
    with np.load(pinned(map_pin),allow_pickle=False) as z:
        require(nodes.tobytes() == z['nodes'].tobytes(), 'checkpoint/assessment physical nodes differ')
    require(np.array_equal(np.array(recipe['indices']),grid(recipe['orders'])), 'raw recipe not canonical parity grid')
    record = {'schema': SCHEMA, 'n': n, 'M': M, 'N': N, 'orders': recipe['orders'],
        'ids': ids.tolist(),
        'id_order': 'itertools.product(range(m_j+1)); i3 fastest; retain equal index parities',
        'basis_order': 'd=0..n,a=0..d,b=0..d-a; (a,b,d-a-b); unscaled product Chebyshev T',
        'exact_geometry': 'x_j=cos(pi*i_j/m_j), indices=canonical_parity_grid[ids]',
        'binary64_link': {'sha256': sha(np.asarray(nodes,dtype='<f8').tobytes()),
            'dtype': 'little-endian float64 M-by-3 C order', 'recipe': 'np.cos(np.pi*indices/np.array(orders))',
            'numpy': np.__version__, 'status': 'MEASURED physical-coordinate identity, distinct from exact cos geometry'},
        'provenance': {'scientific_source_commit': source_commit, 'published_result_commit': publication,
            'receipt': identity(receipt_path), 'raw_details': receipt['raw_details'],
            'raw_inventory': receipt['raw_inventory'], 'checkpoint': checkpoint,
            'path': pathpin, 'recipe': recipepin, 'assessment_map': map_pin,
            'source_snapshots': receipt['executed_source_snapshots'], 'raw_status': 'regeneration-only; not needed by verify/load'}}
    validate(record)
    require(load(record).tobytes() == nodes.tobytes(), 'NumPy recipe not bitwise actual checkpoint')
    measured = next(x for x in details['assessments'] if x['n']==n and x['name']==f'A-m{M}')
    require(measured['node_bytes_sha256'] == record['binary64_link']['sha256'], 'assessment node hash differs')
    # All node identity checks finish before the first finite-field rank query.
    record['certificate'] = certify(record)
    c = record['certificate']
    rank, chosen, det = minor(matrix(record,c['p'],c['rho'],c['minor_row_ids']), c['p'], c['minor_row_ids'])
    require(chosen == c['minor_row_ids'] and rank == N and det == c['det_mod_p'], 'square minor rebuild differs')
    return record

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('mode',choices=['build','verify','selftest'])
    p.add_argument('--payload',type=Path)
    p.add_argument('--check',type=Path)
    p.add_argument('--receipt',type=Path)
    p.add_argument('--degree',type=int,default=12)
    p.add_argument('--publication')
    args = p.parse_args()
    t,w = time.process_time(),time.perf_counter()
    utc = datetime.now(timezone.utc).isoformat()
    if args.mode == 'selftest':
        r = {'schema': SCHEMA,'n':2,'orders':[2,3,3],'N':10,'M':12,'ids':list(range(12)),
             'id_order':'itertools.product(range(m_j+1)); i3 fastest; retain equal index parities',
             'basis_order':'d=0..n,a=0..d,b=0..d-a; (a,b,d-a-b); unscaled product Chebyshev T'}
        r['M']=len(grid(r['orders']));r['ids']=list(range(r['M']))
        r['binary64_link']={'sha256':sha(np.asarray(load(r),dtype='<f8').tobytes())}
        r['certificate']=certify(r)
        result=verify(r)
        require(result['exact_full_column_rank'],'selftest rank')
        try:
            field(13,1,12)
        except ValueError:
            pass
        else:
            raise AssertionError('bad order accepted')
        result['engineering_only_research_rounds']=0
    elif args.mode == 'build':
        require(args.payload and args.receipt and args.publication,'build requires payload/receipt/publication')
        r=build(args.receipt,args.degree,args.publication)
        result=verify(r)
        dump(args.payload,r)
    else:
        require(args.payload,'verify requires payload')
        r=json.loads(args.payload.read_text())
        result=verify(r)
    report={'mode':args.mode,'command':sys.argv,'started_utc':utc,
            'ended_utc':datetime.now(timezone.utc).isoformat(),
            'cpu':time.process_time()-t,'wall':time.perf_counter()-w,
            'versions':{'python':platform.python_version(),'numpy':np.__version__},
            'threads':{k:os.getenv(k) for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS')},
            'checker':identity(__file__),'payload':identity(args.payload) if args.payload and args.payload.exists() else None,
            'result':result,'research_rounds':0}
    if args.check:
        dump(args.check,report)
    print(json.dumps(report,separators=(',',':')))

if __name__ == '__main__':
    main()
