#!/usr/bin/env python3
"""D2: frozen C4 layers with Stieltjes, reorthogonalized Lanczos or oracle marginals.

Full reorthogonalization has two MGS passes at every step. It constructs the
symmetric Jacobi coefficients for diagonal X starting at sqrt(w/sum(w));
monic alpha is the square of the next orthonormal off-diagonal. This is a
known 1D comparator, not a novel algorithm or stability proof.
"""
import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import platform
import sys
import time
import mpmath as mp
from path_recovery import recover

ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'topics/nn-mop-iep-20261103/code/c4_float_baseline.py'
spec=importlib.util.spec_from_file_location('frozen_c4',BASE)
base=importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)


def lanczos(x,w):
    mass=math.fsum(w)
    q=[math.sqrt(v/mass) for v in w]
    norm=math.sqrt(math.fsum(v*v for v in q))
    q=[v/norm for v in q]
    Q=[]
    beta=[]
    alpha=[0.0]
    orth=0.0
    for k in range(len(x)):
        Q.append(q)
        z=[a*b for a,b in zip(x,q)]
        beta.append(math.fsum(a*b for a,b in zip(q,z)))
        for _ in range(2):
            for old in Q:
                dot=math.fsum(a*b for a,b in zip(old,z))
                z=[a-dot*b for a,b in zip(z,old)]
        if k+1<len(x):
            off=math.sqrt(math.fsum(a*a for a in z))
            if off==0: raise ArithmeticError('Lanczos premature breakdown')
            alpha.append(off*off)
            q=[a/off for a in z]
    for i,q in enumerate(Q):
        for j,r in enumerate(Q):
            orth=max(orth,abs(math.fsum(a*b for a,b in zip(q,r))-(i==j)))
    return (beta,alpha),orth


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--sizes',nargs='+',type=int,default=[4,8,12,16,24,32])
    ap.add_argument('--families',nargs='+',default=['krawtchouk','hahn'])
    ap.add_argument('--path-dps',type=int,default=100)
    ap.add_argument('--no-path',action='store_true')
    args=ap.parse_args()
    result=dict(status='MEASURED; reference convergence not certification',
                python=platform.python_version(),mpmath=mp.__version__,platform=platform.platform(),
                hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [BASE,Path(__file__),Path(__file__).with_name('path_recovery.py')]},
                argv=sys.argv[1:],unit_roundoff=2**-53,
                marginal_error_metric='max marginal alpha/beta sup error divided by max(1, reference marginal sup)',cases=[])
    start=time.monotonic()
    with mp.workdps(220):
        for family in args.families:
            for N in args.sizes:
                x,w=base.inputs(N,family)
                xx=[base.convert(v,float) for v in x]
                ww=[[base.convert(v,float) for v in row] for row in w]
                exact_x=[base.convert(v,mp.mpf) for v in x]
                exact_w=[[base.convert(v,mp.mpf) for v in row] for row in w]
                ident=json.dumps(dict(nodes=list(map(str,x)),weights=[list(map(str,r)) for r in w]),sort_keys=True)
                lo,_=base.compute(N,family,140)
                ref,_=base.compute(N,family,220)
                rounded_x=list(map(mp.mpf,xx))
                rounded_w=[list(map(mp.mpf,row)) for row in ww]
                rounded_ref,_=base.layers(N,*(base.marginal(rounded_x,row) for row in rounded_w))
                with mp.workdps(140):
                    rounded_lo,_=base.layers(N,*(base.marginal(rounded_x,row) for row in rounded_w))
                hp=[base.marginal(exact_x,row) for row in exact_w]
                hpr=[base.marginal(rounded_x,row) for row in rounded_w]
                methods={}
                mar_l=[]
                orth=[]
                for row in ww:
                    mar,err=lanczos(xx,row)
                    mar_l.append(mar)
                    orth.append(err)
                methods['c4_stieltjes']=[base.marginal(xx,row) for row in ww]
                methods['c4_lanczos']=mar_l
                methods['c4_oracle_exact']=[tuple(list(map(float,arr)) for arr in mar) for mar in hp]
                methods['c4_oracle_rounded']=[tuple(list(map(float,arr)) for arr in mar) for mar in hpr]
                out=dict(N=N,family=family,input_sha256=hashlib.sha256(ident.encode()).hexdigest(),
                         reference_140_220_agreement=float(base.errors(lo,ref)[0]),
                         input_rounding_forward_effect=float(base.errors(rounded_ref,ref)[0]),
                         rounded_reference_140_220_agreement=float(base.errors(rounded_lo,rounded_ref)[0]),
                         lanczos_max_orthogonality=max(orth),methods={})
                for name,mar in methods.items():
                    try:
                        got,diag=base.layers(N,*mar)
                        row=dict(forward_exact=float(base.errors(got,ref)[0]),
                                 forward_rounded=float(base.errors(got,rounded_ref)[0]),
                                 terminal_max_abs_d=float(max(abs(r['b2']-r['b1']) for nu,r in got.items() if sum(nu)==N-1)),
                                 marginal_error=max(float(max(abs(mp.mpf(v)-t) for v,t in zip(arr,truth))/max(mp.mpf(1),max(abs(t) for t in truth)))
                                      for ma,mr in zip(mar,hpr) for arr,truth in zip(ma,mr)),
                                 status='completed',divisors=diag)
                        if not args.no_path:
                            row['path']=recover(got,N,exact_x,exact_w,args.path_dps)
                        out['methods'][name]=row
                    except (ValueError,ArithmeticError,ZeroDivisionError,OverflowError) as exc:
                        out['methods'][name]=dict(status='failure',reason=type(exc).__name__+': '+str(exc))
                result['cases'].append(out)
    result['elapsed_seconds']=time.monotonic()-start
    print(json.dumps(result,indent=2,sort_keys=True,allow_nan=False))

if __name__=='__main__': main()
