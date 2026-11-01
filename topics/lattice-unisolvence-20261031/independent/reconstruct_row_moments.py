#!/usr/bin/env python3
"""Independent exact edge-case check of the general row-root kernel reduction."""
from hashlib import sha256
from itertools import product
from math import comb
from pathlib import Path
import json
import random
import sys
import sympy as sp
from reconstruct_rank import independent_rank

ROOT=Path(__file__).resolve().parents[3]
TOPIC=ROOT/'topics/lattice-unisolvence-20261031'


def coefficients(roots,p):
    coeff=[1]
    for root in roots:
        updated=[0]*(len(coeff)+1)
        for j,value in enumerate(coeff):
            updated[j]=(updated[j]-root*value)%p
            updated[j+1]=(updated[j+1]+value)%p
        coeff=updated
    return coeff


def main():
    rng=random.Random(61931217);checked=0;edge_counts=set();scope=[];full_row_seen=False
    for n in range(1,6):
        primes=[p for p in [2,3,5,7,11] if p>=n+1][:2]
        N,M=comb(n+2,2),n*(n+1)//2
        for p in primes:
            scope.append([n,p])
            for trial in range(20):
                slots=list(range((n+1)**2))
                chosen=slots[:N] if trial==0 else rng.sample(slots,N)
                counts=[sum(v//(n+1)==i for v in chosen) for i in range(n+1)]
                edge_counts.update(q for q in counts if q in (0,n+1))
                full_row_seen |= (n+1 in counts)
                x=rng.sample(range(p),n+1)
                ys=[rng.sample(range(p),q) for q in counts]
                polys=[coefficients(roots,p) for roots in ys]
                exps=[(a,b) for a,b in product(range(n+1),repeat=2) if a+b<=n]
                V=[[pow(x[i],a,p)*pow(y,b,p)%p for a,b in exps] for i,roots in enumerate(ys) for y in roots]
                cols=[(i,r) for i,q in enumerate(counts) for r in range(n-q+1)]
                B=[[pow(x[i],t,p)*(polys[i][b-r] if 0<=b-r<len(polys[i]) else 0)%p for i,r in cols] for b in range(1,n+1) for t in range(b)]
                assert len(B)==len(cols)==M and len(V)==N
                assert N-independent_rank(V,p)==M-independent_rank(B,p),(n,p,counts)
                checked+=1
    path=TOPIC/'directions/C1/symbolic.json';symbolic=json.loads(path.read_text())
    x=[sp.sympify(v) for v in symbolic['normalized_axes']['x']]
    yy=[sp.sympify(v) for v in symbolic['normalized_axes']['y']]
    z=sp.Symbol('z')
    Q=[sp.Poly(sp.prod(z-yy[j] for j in range(5) if (i+j)%4<2),z) for i in range(4)]
    cols=[(i,r) for i,q in enumerate(Q) for r in range(4-q.degree())]
    rows=[(b,t) for b in range(1,4) for t in range(b)]
    B=sp.Matrix([[x[i]**t*(Q[i].nth(b-r) if b>=r else 0) for i,r in cols] for b,t in rows])
    assert B==sp.Matrix([[sp.sympify(v) for v in row] for row in symbolic['matrix']])
    determinant=sp.expand(B.det(method='domain-ge'))
    assert sp.expand(determinant-sp.sympify(symbolic['factorization']))==0
    assert determinant!=0
    out={'all_checks_passed':True,'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
         'symbolic_input_sha256':sha256(path.read_bytes()).hexdigest(),'seed':61931217,
         'exact_kernel_dimension_comparisons':checked,'degree_prime_scope':scope,
         'zero_root_rows_tested':0 in edge_counts,'full_degree_root_rows_tested':full_row_seen,
         'n3_symbolic_matrix_and_factorization_checked':True,'sympy':sp.__version__,
         'method':'Fresh coefficient multiplication, independent exact rank/nullity comparison including zero/full rows and small characteristic, direct symbolic matrix identity.'}
    Path(sys.argv[1]).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,sort_keys=True))


if __name__=='__main__':
    main()
