#!/usr/bin/env python3
"""Frozen T8 round08 half-shift screen; exact positive ranks, MEASURED norms.

All raw tuple records are regenerate-only under a unique scratch directory.
No inference of singularity is made from a deficient modular rank.
"""
from __future__ import annotations
import argparse
import hashlib
import itertools as it
import json
import math
from pathlib import Path
import platform
import sys
import tempfile
import time

import numpy as np
import scipy
import scipy.linalg as la
import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
TOP = ROOT / 'topics/padua-3d-20261106'
sys.path.insert(0, str(ROOT / 'tracks/lattice-unisolvence/code'))
import c3_lebesgue as leb
import c3_rank as helper_rank

RULES = '9042e1c42964150f30fdbe8563c12ba6c6a8692a'
SEED = 202611060808

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def modes(n):
    return helper_rank.exponents(n)

def trace(n, odd):
    m = n // 2
    if n % 2 == 0:
        return m + 1 if odd == 2 else (m + 1) ** 2
    if odd == 2:
        return 0
    return (1 if odd == 1 else -1) * (m + 1) * (m + 2)

def exact_nodes(n, z):
    N = math.comb(n + 3, 3)
    M, L = 2 * N, 4 * N
    rows = sorted({tuple(min(v, L-v) for v in
                         (((2*k+1)*a) % L for a in z)) for k in range(M)})
    assert len(rows) == N
    return L, rows

def splitting_prime(L, start=1000000):
    q = max(1, (start-1 + L-1)//L)
    p = q*L + 1
    while not sp.isprime(p):
        p += L
    assert p < 1000000000, 'int64 arithmetic bound'
    w = pow(int(sp.primitive_root(p)), (p-1)//L, p)
    assert pow(w,L,p) == 1
    assert all(pow(w,L//int(q),p) != 1 for q in sp.factorint(L))
    return int(p), w

def rank_det(A, p):
    A = np.asarray(A, dtype=np.int64).copy() % p
    rank, determinant = 0, 1
    nr, nc = A.shape
    for c in range(nc):
        pivots = np.flatnonzero(A[rank:, c])
        if not len(pivots):
            continue
        k = rank + int(pivots[0])
        if k != rank:
            A[[k, rank]] = A[[rank, k]]
            determinant = -determinant
        pivot = int(A[rank,c])
        determinant = determinant*pivot % p
        A[rank,c:] = A[rank,c:]*pow(pivot,-1,p) % p
        if rank+1 < nr:
            A[rank+1:,c:] = (A[rank+1:,c:] -
                 A[rank+1:,c,None]*A[rank,None,c:]) % p
        rank += 1
        if rank == nr:
            break
    return rank, int(determinant % p) if rank == nc == nr else None

def modular_check(n, z, p, w):
    L, nodes = exact_nodes(n,z)
    X = np.array([[(pow(w,v,p)+pow(w,(-v)%L,p))*pow(2,-1,p) % p
                   for v in node] for node in nodes], dtype=np.int64)
    tab = [np.ones((len(nodes),n+1),dtype=np.int64) for _ in range(3)]
    for j in range(3):
        tab[j][:,1] = X[:,j]
        for k in range(2,n+1):
            tab[j][:,k] = (2*X[:,j]*tab[j][:,k-1] - tab[j][:,k-2]) % p
    V = np.array([tab[0][:,a]*tab[1][:,b] % p * tab[2][:,c] % p
                  for a,b,c in modes(n)]).T
    rank,det = rank_det(V,p)
    return {'p':p,'omega':w,'rank':rank,'det':det}

def certificate(n, z):
    L,nodes = exact_nodes(n,z)
    p,w = splitting_prime(L)
    p2,w2 = splitting_prime(L,p+L)
    checks = [modular_check(n,z,p,w), modular_check(n,z,p2,w2)]
    return {'L':L,'nodes':len(nodes),'checks':checks,
            'full_rank_certified':all(r['rank']==len(nodes) for r in checks)}

def actual_points(n,z):
    L,nodes = exact_nodes(n,z)
    return np.cos(2*np.pi*np.array(nodes,dtype=float)/L)

def logdet(n,z):
    V = leb.basis(actual_points(n,z),n)
    sign,val = np.linalg.slogdet(V)
    if not sign or not np.isfinite(val):
        return None
    return float(val + sum(sum(a>0 for a in m) for m in modes(n))*math.log(2)/2)

def control_quality(n):
    mesh = np.array(list(it.product(leb.lobatto(21),repeat=3)))
    E = leb.basis(mesh,n)
    axis = leb.discrete_leja(leb.lobatto(n+1))
    P = np.array([[axis[a],axis[b],axis[c]] for a,b,c in modes(n)])
    leja = leb.diagnose(P,n,mesh,E)
    can = np.array(list(it.product(leb.lobatto(2*n+1),repeat=3)))
    _,_,perm = la.qr(leb.basis(can,n).T,mode='economic',pivoting=True)
    qr = leb.diagnose(can[perm[:len(modes(n))]],n,mesh,E)
    return mesh,E,{'Leja':leja,'QR':qr}

def record(out, row):
    out.write(json.dumps(row,separators=(',',':'),allow_nan=False)+'\n')
    out.flush()

def degree(n,out):
    started = time.monotonic()
    N = math.comb(n+3,3)
    M = 2*N
    fixed = N % 2
    ceilings = {str(t):N-abs(trace(n,t)-fixed)//2 for t in (1,2,3)}
    row = {'n':n,'N':N,'M':M,'L':2*M,'phase':'z/(2M)',
           'node_fixed_trace':fixed,'polynomial_traces':{str(t):trace(n,t) for t in (1,2,3)},
           'rank_ceilings':ceilings,'all_pairs':math.comb(M-1,2)}
    permitted = [t for t in (1,2,3) if trace(n,t)==fixed]
    row['permitted_odd_counts']=permitted
    if not permitted:
        row.update({'outcome':'PROVED analytic trace exclusion; no rank/quality search',
                    'searched_pairs':0,'elapsed_seconds':round(time.monotonic()-started,4)})
        return row
    pairs = list(it.combinations(range(1,M),2))
    proposed, seen, rank_counts, survivors = [], set(), {}, []
    p,w = splitting_prime(2*M)
    fallback_used = False
    prefix_count = 0
    for b,c in pairs:
        if time.monotonic()-started > 180:
            fallback_used=True
            break
        prefix_count += 1
        seen.add((b,c))
        z=[1,b,c]
        t=sum(a%2 for a in z)
        datum={'n':n,'z':z,'odd_count':t,'phase_denominator':2*M,'nodes':N}
        if n==3:
            chk=modular_check(n,z,p,w)
            datum['check']=chk
            rank_counts[str(chk['rank'])]=rank_counts.get(str(chk['rank']),0)+1
            if chk['rank']==N:
                cert=certificate(n,z)
                assert cert['full_rank_certified']
                survivors.append({'z':z,'certificate':cert})
        if t in permitted:
            score=logdet(n,z)
            datum['orthonormal_logabsdet']=score
            if score is not None:
                proposed.append((score,b,c))
        else:
            datum['analytic_rank_upper']=ceilings[str(t)]
        record(out,datum)
    fallback_count=0
    if fallback_used:
        rng=np.random.default_rng(SEED+n)
        for i in rng.choice(len(pairs),size=min(4096,len(pairs)),replace=False):
            b,c=pairs[int(i)]
            if (b,c) in seen:
                continue
            seen.add((b,c)); fallback_count+=1
            z=[1,b,c]; t=sum(a%2 for a in z)
            datum={'n':n,'z':z,'odd_count':t,'fallback':True,'nodes':N}
            if t in permitted:
                score=logdet(n,z)
                datum['orthonormal_logabsdet']=score
                if score is not None:
                    proposed.append((score,b,c))
            else:
                datum['analytic_rank_upper']=ceilings[str(t)]
            record(out,datum)
    proposed.sort(key=lambda a:(-a[0],a[1],a[2]))
    finalists=[]; selected=None
    for score,b,c in proposed[:10]:
        z=[1,b,c]; cert=certificate(n,z)
        datum={'z':z,'orthonormal_logabsdet':score,'certificate':cert}
        finalists.append(datum)
        if cert['full_rank_certified']:
            selected=datum
            break
    row.update({'searched_pairs':len(seen),'lex_prefix_pairs':prefix_count,
                'fallback_used':fallback_used,'fallback_pairs':fallback_count,
                'numeric_determinants':len(proposed),'modular_rank_histogram':rank_counts,
                'scan_seconds':round(time.monotonic()-started,4),
                'finalist_certificates':finalists})
    if selected is None:
        row['outcome']='OPEN; no exact full-rank finalist; not a nonexistence result'
    else:
        mesh,E,controls=control_quality(n)
        row['baselines']=controls
        selected['quality']=leb.diagnose(actual_points(n,selected['z']),n,mesh,E)
        row['selected']=selected
        row['outcome']='exact finite positive; quality MEASURED only'
        if n==3:
            for s in survivors:
                s['orthonormal_logabsdet']=logdet(n,s['z'])
                s['quality']=leb.diagnose(actual_points(n,s['z']),n,mesh,E)
            row['all_cubic_survivors']=survivors
        val=selected['quality']['sampled_lebesgue']
        row['D2']={'QR_loss_excludes_promising':n>=4 and val is not None and val>controls['QR']['sampled_lebesgue'],
                   'eligible_Leja_loss':n>=6 and val is not None and val>controls['Leja']['sampled_lebesgue'],
                   'eligible_for_Leja_sequence':n>=6 and val is not None}
    row['elapsed_seconds']=round(time.monotonic()-started,4)
    return row

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--scratch')
    parser.add_argument('--receipt',default=str(TOP/'evidence/t8-r08-halfshift.json'))
    args=parser.parse_args()
    scratch=Path(args.scratch or tempfile.mkdtemp(prefix='padua-t8-r08-'))
    scratch.mkdir(parents=True,exist_ok=True)
    raw=scratch/'halfshift-tuples.jsonl'
    assert not raw.exists(), 'fresh scratch required'
    started=time.monotonic(); rows=[]; streak=0
    with raw.open('w') as out:
        for n in range(3,9):
            row=degree(n,out); rows.append(row)
            d2=row.get('D2',{})
            if d2.get('eligible_for_Leja_sequence'):
                streak=streak+1 if d2['eligible_Leja_loss'] else 0
            print(json.dumps({'n':n,'searched':row['searched_pairs'],'outcome':row['outcome'],
                  'z':row.get('selected',{}).get('z'),
                  'Lambda21':row.get('selected',{}).get('quality',{}).get('sampled_lebesgue'),
                  'seconds':row['elapsed_seconds']}),flush=True)
            if streak>=2:
                break
    source={str(Path(f).relative_to(ROOT)):sha(f) for f in
            [__file__,leb.__file__,helper_rank.__file__]}
    result={'schema':'t8-r08-halfshift-v1','rules_sha':RULES,'seed':SEED,
            'command':sys.argv,'code_dependencies_sha256':source,
            'versions':{'python':platform.python_version(),'numpy':np.__version__,
                        'scipy':scipy.__version__,'sympy':sp.__version__},
            'raw':{'path':str(raw),'sha256':sha(raw),'bytes':raw.stat().st_size,
                   'retention':'local regenerate-only, not archival delivery'},
            'rows':rows,'D2_eligible_Leja_rows':sum(r.get('D2',{}).get('eligible_for_Leja_sequence',False) for r in rows),
            'D2_two_loss_kill':streak>=2,
            'elapsed_seconds':round(time.monotonic()-started,4)}
    data=json.dumps(result,separators=(',',':'),allow_nan=False)+'\n'
    assert len(data.encode())<16384,'receipt size limit'
    Path(args.receipt).write_text(data)
    print(json.dumps({'receipt':args.receipt,'bytes':len(data.encode()),'raw_sha256':sha(raw)}),flush=True)

if __name__=='__main__':
    main()
