#!/usr/bin/env python3
"""Exact Chebyshev pencils for fixed even-checkerboard Padua conventions.

Requires python-flint; numerical scipy eigensolves only select endpoints/witnesses.
Exact integer congruence and signed diagonal dominance certify inertia.
"""
import argparse
import hashlib
import json
import math
import platform
import sys
import time
from fractions import Fraction as F
from pathlib import Path

import flint
from flint import fmpz_mat

ROOT = Path(__file__).resolve().parents[3]


def h(k):
    return F(0) if k % 2 else F(2, 1-k*k)


def fold(k, n):
    k %= 2*n
    return min(k, 2*n-k)


def moment(m, r, s):
    a, b = fold(r, m), fold(s, m+1)
    return h(a)*h(b) if a+b <= m else h(m-a)*h(m+1-b)


def pencil(m):
    basis = [(a, t-a) for t in range(m) for a in range(t, -1, -1)]
    H, Q = [], []
    for a,b in basis:
        hr, qr = [], []
        for c,d in basis:
            modes = [(r,s) for r in (a+c,abs(a-c)) for s in (b+d,abs(b-d))]
            hr.append(sum((h(r)*h(s) for r,s in modes), F(0))/4)
            qr.append(sum((moment(m,r,s) for r,s in modes), F(0))/4)
        H.append(hr); Q.append(qr)
    # For even m, x degree parity is preserved; for odd m, y parity.
    coordinate = 0 if m%2 == 0 else 1
    blocks = [[i for i,ab in enumerate(basis) if ab[coordinate]%2 == p] for p in (0,1)]
    for i in blocks[0]:
        for j in blocks[1]:
            assert H[i][j] == Q[i][j] == 0
    return basis, H, Q, blocks


def inertia(H,Q,blocks,t,transforms):
    """Exact signed diagonal-dominance certificate after integer congruence.

    B=R.T*A*R for A=den*(Q-tH), den positive. Strict dominance
    |Bii|>sum(j!=i)|Bij| implies inertia equals diagonal signs: continuously
    turn off off-diagonal entries, retaining dominance and nonsingularity.
    Since B is nonsingular, square R is invertible, so inertia(A)=inertia(B).
    Numerical eigenvectors merely propose R; all acceptance tests are integer.
    """
    counts=[0,0,0]; records=[]
    for indices,R in zip(blocks,transforms):
        rows=[[Q[i][j]-t*H[i][j] for j in indices] for i in indices]
        den=1
        for row in rows:
            for x in row: den=math.lcm(den,x.denominator)
        A=fmpz_mat([[x.numerator*(den//x.denominator) for x in row] for row in rows])
        start=time.monotonic()
        B=R.transpose()*A*R
        n=len(indices); signs=[]; margins=[]
        assert B == B.transpose()
        for i in range(n):
            diag=B[i,i]
            margin=abs(diag)-sum(abs(B[i,j]) for j in range(n) if j!=i)
            assert margin>0, 'increase congruence rounding scale or endpoint width'
            signs.append(1 if diag>0 else -1)
            counts[0 if diag<0 else 2]+=1
            margins.append(margin)
        records.append({'dimension':n,'common_denominator':str(den),'diagonal_signs':signs,
                        'minimum_strict_dominance_margin':str(min(margins)),
                        'integer_transform_sha256':hashlib.sha256(str(R).encode()).hexdigest(),
                        'seconds':time.monotonic()-start})
    return {'endpoint':str(t),'negative':counts[0],'zero':counts[1],'positive':counts[2],'blocks':records}


def exact_witness(H,Q,vector):
    nonzero=[i for i,x in enumerate(vector) if x]
    def quadratic(M):
        return sum((vector[i]*vector[j]*M[i][j] for i in nonzero for j in nonzero), F(0))
    a,b=quadratic(Q),quadratic(H)
    assert b>0
    return a,b


def run(m, width, witness=False):
    import numpy as np
    import scipy.linalg
    basis,H,Q,blocks=pencil(m)
    Hf=np.array(H,dtype=float);Qf=np.array(Q,dtype=float)
    vals,vecs=scipy.linalg.eigh(Qf,Hf,check_finite=False)
    scale=10**12
    transforms=[]
    for indices in blocks:
        ix=np.ix_(indices,indices)
        _,v=scipy.linalg.eigh(Qf[ix],Hf[ix],check_finite=False)
        transforms.append(fmpz_mat([[int(round(float(x)*scale)) for x in row] for row in v]))
    result={'m':m,'n':m-1,'dimension':len(basis),'measured_extrema':[float(vals[0]),float(vals[-1])],'integer_transform_rounding_scale':str(scale),'checks':[]}
    for key,value,target in [('minimum',vals[0],0),('maximum',vals[-1],len(basis)-1)]:
        lo=F(math.floor(float(value)/float(width)))*width
        hi=lo+width
        lower=inertia(H,Q,blocks,lo,transforms);upper=inertia(H,Q,blocks,hi,transforms)
        expected=(0,1) if key=='minimum' else (len(basis)-1,len(basis))
        assert (lower['negative'],upper['negative'])==expected
        result['checks'].append({'extremum':key,'lower':lower,'upper':upper,'open_interval':[str(lo),str(hi)]})
    if witness:
        # Rounded rational coefficients in the unnormalized product Chebyshev basis.
        v=vecs[:,0];v=v/max(abs(v))
        nums=[int(round(float(x)*10000)) for x in v]
        a,b=exact_witness(H,Q,nums)
        assert 4*a < b
        result['witness']={'basis':'unnormalized T_a(x)T_b(y), total-degree ascending, a descending',
                           'coefficients':[[basis[i][0],basis[i][1],x] for i,x in enumerate(nums) if x],
                           'Q_p_squared':str(a),'integral_p_squared':str(b),'rayleigh_quotient':str(a/b),
                           'strict_b_minus_4a':str(b-4*a),'conclusion':'lambda_min < 1/4, hence eta > 3/4'}
    return result


def main():
    import numpy
    import scipy
    ap=argparse.ArgumentParser();ap.add_argument('--m',type=int,nargs='+',default=[10,20,30,40]);ap.add_argument('--width',default='1/1000000');ap.add_argument('--witness-m',type=int,default=30);ap.add_argument('--output',required=True)
    args=ap.parse_args()
    out={'status':'exact finite checks; mathematical reduction and independent rerun required for PROVED',
         'command':sys.argv,'rules_sha':'806cc7b4509fd93bae652f9545d32d95529f8281',
         'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'definitions_sha256':hashlib.sha256((ROOT/'topics/padua-mz-2d-20261101/definitions.md').read_bytes()).hexdigest(),
         'python':sys.version,'python_flint':flint.__version__,'numpy':numpy.__version__,'scipy':scipy.__version__,'platform':platform.platform(),'results':[]}
    for m in args.m:
        print('start m',m,flush=True)
        out['results'].append(run(m,F(args.width),m==args.witness_m))
        Path(args.output).write_text(json.dumps(out,separators=(',',':'))+'\n')
        print('done m',m,flush=True)

if __name__=='__main__':main()
