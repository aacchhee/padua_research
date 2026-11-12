#!/usr/bin/env python3
"""Dated correction of n3 numerical roundoff ties under the frozen lex rule.

The original producer and receipt remain unchanged. Exact cubic determinant
scores resolve the proved mathematical tie before any selection; quality is
still evaluated only after selection. All other degree rules are unchanged.
"""
import hashlib
import itertools as it
import json
import math
from pathlib import Path
import sys

import t8_r08_halfshift as run

SIGN = tuple(it.product((-1,1),repeat=3))

def cosine_coefficients(n,z):
    N=math.comb(n+3,3); M=2*N
    C=[[0 for _ in range(N)] for _ in range(N)]
    for j,alpha in enumerate(run.modes(n)):
        for eps in SIGN:
            r=sum(e*a*b for e,a,b in zip(eps,alpha,z)) % (2*M)
            r=min(r,2*M-r)
            if r==N:
                continue
            sign=1
            if r>N:
                r=M-r; sign=-1
            C[r][j]+=sign
    return C

def bareiss_det(A):
    A=[r[:] for r in A]; n=len(A); previous=1; sign=1
    for k in range(n-1):
        pivot=next((i for i in range(k,n) if A[i][k]),None)
        if pivot is None:
            return 0
        if pivot!=k:
            A[k],A[pivot]=A[pivot],A[k]; sign=-sign
        a=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=A[i][j]*a-A[i][k]*A[k][j]
                q,rem=divmod(num,previous)
                assert rem==0,'exact Bareiss division'
                A[i][j]=q
            A[i][k]=0
        previous=a
    return sign*A[-1][-1]

ORIGINAL_LOGDET=run.logdet
CUBIC = {}

def corrected_logdet(n,z):
    if n!=3:
        return ORIGINAL_LOGDET(n,z)
    key=tuple(z)
    if key not in CUBIC:
        CUBIC[key]=bareiss_det(cosine_coefficients(n,z))
    d=abs(CUBIC[key])
    if not d:
        return None
    N=math.comb(n+3,3)
    K=sum(sum(a>0 for a in alpha) for alpha in run.modes(n))
    # V=DCT*C/8, |det DCT|=sqrt(N*(N/2)^(N-1)).
    return math.log(d)+N*math.log(N)/2-(N-1)*math.log(2)/2-N*math.log(8)+K*math.log(2)/2

if __name__=='__main__':
    original=run.TOP/'evidence/t8-r08-halfshift.json'
    original_identity={'path':str(original.relative_to(run.ROOT)),
                       'bytes':original.stat().st_size,'sha256':run.sha(original)}
    if '--receipt' not in sys.argv:
        sys.argv+=['--receipt',str(run.TOP/'evidence/t8-r08-halfshift-corrected.json')]
    target=Path(sys.argv[sys.argv.index('--receipt')+1])
    run.logdet=corrected_logdet
    run.main()
    result=json.loads(target.read_text())
    positives={z:d for z,d in CUBIC.items() if d}
    assert len(CUBIC)==380,'all trace-permitted cubic pairs including survivor rechecks'
    assert len(positives)==8
    assert {abs(d) for d in positives.values()}=={2**49}
    result['code_dependencies_sha256'][str(Path(__file__).relative_to(run.ROOT))]=run.sha(__file__)
    result['correction']={'date':'2026-11-06','original_receipt':original_identity,
       'reason':'exact cubic determinant tie resolved by preregistered lex order; floating roundoff changed original selection',
       'method':'integer cosine coefficients and checked-division Bareiss; V=DCT*C/8',
       'cubic_trace_permitted_pairs':len(CUBIC),'nonzero_cubic_determinants':len(positives),
       'common_abs_det_C':2**49,
       'selected_exact_lexicographic_tie':[1,4,11]}
    data=json.dumps(result,separators=(',',':'),allow_nan=False)+'\n'
    assert len(data.encode())<16384
    target.write_text(data)
    print(json.dumps({'corrected_receipt':str(target),'bytes':len(data.encode()),
                      'sha256':run.sha(target)}),flush=True)
