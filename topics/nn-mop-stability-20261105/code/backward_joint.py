#!/usr/bin/env python3
"""Feasible full joint-data witness, not a nearest-point or raw backward solve.

Extract both marginal spectral measures. Use first marginal's ordered nodes
as the common nodes and each marginal's normalized spectral weights. Rebuild
the entire triangle from that positive common input in high precision.
Return BOTH input displacement and full coefficient correction. A path
spectrum alone is never labeled full NN backward error.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import platform
import sys
from fractions import Fraction

import mpmath as mp

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('native_joint',HERE/'native_mixed.py')
native=importlib.util.module_from_spec(spec)
spec.loader.exec_module(native)
c4=native.c4


def spectral_axes(co,N):
    nodes,weights=[],[]
    for s in (1,2):
        J=mp.matrix(N)
        for k in range(N):
            nu=(k,0) if s==1 else (0,k)
            J[k,k]=mp.mpf(co[nu]['b'+str(s)])
            if k:
                a=mp.mpf(co[nu]['a'+str(s)])
                if a<=0: raise ArithmeticError('nonpositive marginal a')
                J[k-1,k]=J[k,k-1]=mp.sqrt(a)
        e,V=mp.eigsy(J)
        nodes.append(list(e))
        weights.append([V[0,k]**2 for k in range(N)])
    return nodes,weights


def normality_exact(x,w):
    """Exact finite nonsingularity check of every defining mixed system."""
    N=len(x)
    mu=[[sum(a*b**k for a,b in zip(r,x)) for k in range(2*N+1)] for r in w]
    count=0
    for k in range(1,N+1):
        for n in range(k+1):
            m=k-n
            A=[mu[s][i:i+k] for s,cnt in enumerate((n,m)) for i in range(cnt)]
            for j in range(k):
                piv=next((i for i in range(j,k) if A[i][j]),None)
                if piv is None: raise ArithmeticError(f'exact nonnormal witness at {(n,m)}')
                A[j],A[piv]=A[piv],A[j]
                for i in range(j+1,k):
                    q=A[i][j]/A[j][j]
                    for h in range(j+1,k): A[i][h]-=q*A[j][h]
            count+=1
    return count


def witness(co,N,family,dps=160,certify=False):
    with mp.workdps(dps):
        xx,ww=c4.inputs(N,family)
        truthx=[c4.convert(q,mp.mpf) for q in xx]
        truthw=[[c4.convert(q,mp.mpf) for q in r] for r in ww]
        truthw=[[a/sum(r) for a in r] for r in truthw]
        xn,wn=spectral_axes(co,N)
        # A deliberately feasible common-support input; no least-squares
        # minimization is asserted. Each w is positive and mass one.
        # Freeze an actual rational input, not a floating approximation to
        # unspecified algebraic spectral data. Positivity/order are exact.
        xq=[Fraction(mp.nstr(a,60)) for a in xn[0]]
        wq=[[Fraction(mp.nstr(a,60)) for a in r] for r in wn]
        wq=[[a/sum(r) for a in r] for r in wq]
        if not all(a>0 for r in wq for a in r): raise ArithmeticError('nonpositive exact witness weight')
        x=[c4.convert(a,mp.mpf) for a in xq]
        wn=[[c4.convert(a,mp.mpf) for a in r] for r in wq]
        if not all(x[i]<x[i+1] for i in range(N-1)):
            raise ArithmeticError('colliding reconstructed nodes')
        rec,_=c4.layers(N,*(c4.marginal(x,w) for w in wn))
        ref,_=c4.compute(N,family,dps)
        data=max(max(abs(a-b) for a,b in zip(x,truthx))/max(map(abs,truthx)),
                 max(abs(a-b)/b for w,t in zip(wn,truthw) for a,b in zip(w,t)))
        # Use original-reference field scales, frozen independent of witness.
        fields={f:max(abs(mp.mpf(co[nu][f])-rec[nu][f]) for nu in rec)/
                   max(abs(r[f]) for r in ref.values())
                for f in ('a1','a2','b1','b2')}
        rep=dict(nodes=list(map(str,xq)),normalized_weights=[list(map(str,r)) for r in wq])
        ident=json.dumps(rep,sort_keys=True).encode()
        normality=normality_exact(xq,wq) if certify and N<=8 else None
        return dict(data_mixed_sup=float(data),data_in_units_u=float(data*2**53),
            full_coefficient_correction=max(map(float,fields.values())),
            correction_fields={f:float(a) for f,a in fields.items()},
            marginal_support_disagreement=float(max(abs(a-b) for a,b in zip(*xn))),
            min_weight=float(min(a for r in wn for a in r)),
            mass_error=float(max(abs(sum(r)-1) for r in wn)),
            witness_input_sha256=hashlib.sha256(ident).hexdigest(),
            witness_input=rep,dps=dps,exact_normality_systems_checked=normality,
            normality_scope='exact Fraction through N' if normality else 'uncertified numerical rebuild only',
            scope='positive common-node full-triangle feasible mixed witness; not nearest projection; not raw-array backward error')


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--family',required=True,choices=['krawtchouk','hahn'])
    ap.add_argument('--sizes',type=int,nargs='+',default=[4,8,12,16])
    ap.add_argument('--methods',nargs='+',default=['c4','lu','qr','svd'])
    args=ap.parse_args()
    rows=[]
    for N in args.sizes:
        for method in args.methods:
            co,_=c4.compute(N,args.family) if method=='c4' else native.compute(N,args.family,method)
            lo=witness(co,N,args.family,100)
            hi=witness(co,N,args.family,180,certify=True)
            # Rebuilding converges in precision for the SAME recovered
            # mathematical data; rounded output values are compared here.
            conv=abs(lo['full_coefficient_correction']-hi['full_coefficient_correction'])
            rows.append(dict(N=N,family=args.family,method=method,
                             correction_100_180_absolute_agreement=conv,**hi))
    print(json.dumps(dict(status='MEASURED feasible mixed witnesses',
        python=platform.python_version(),mpmath=mp.__version__,argv=sys.argv[1:],
        code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        native_code_sha256=hashlib.sha256((HERE/'native_mixed.py').read_bytes()).hexdigest(),
        frozen_baseline_sha256=hashlib.sha256(native.BASE.read_bytes()).hexdigest(),cases=rows),
        sort_keys=True,indent=2,allow_nan=False))


if __name__=='__main__': main()
