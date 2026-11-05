#!/usr/bin/env python3
"""Bounded C4 baseline. Monic Stieltjes marginals, then known A/B recursion.

N is number of nodes (paper binomial degree M=N-1). All arithmetic, including
input rounding, uses z=2*k/M-1. No C3 or stability assertion. JSON is a receipt,
not a coefficient archive. A 100/160-digit comparison is a convergence check,
not an independent reference algorithm; N=4 additionally uses exact moments.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import platform
import sys
import time
import mpmath as mp


def inputs(N, family):
    M = N - 1
    nodes = [Q(2*k, M)-1 for k in range(N)]
    if family == 'krawtchouk':
        weights = [[Q(math.comb(M,k))*p**k*(1-p)**(M-k) for k in range(N)]
                   for p in (Q(2,5), Q(1,2))]
    elif family == 'hahn':
        def poch(a, n):
            return math.prod((a+i for i in range(n)),start=Q(1))
        weights = [[poch(beta+1,k)/math.factorial(k) *
                    poch(Q(2),M-k)/math.factorial(M-k) for k in range(N)]
                   for beta in (Q(1),Q(3,2))]
    else:
        raise ValueError('unknown source family')
    return nodes, weights


def convert(q, cast):
    return cast(q.numerator)/cast(q.denominator)


def marginal(x, w):
    N = len(x)
    zero = x[0]*0
    prev, cur = [zero]*N, [zero+1]*N
    beta, alpha = [], []
    oldnorm = None
    for n in range(N):
        norm = sum(wi*ci*ci for wi,ci in zip(w,cur))
        if norm <= 0 or not mp.isfinite(norm):
            raise ArithmeticError(f'marginal norm invalid at n={n}')
        b = sum(wi*xi*ci*ci for wi,xi,ci in zip(w,x,cur))/norm
        a = norm/oldnorm if n else zero
        beta.append(b)
        alpha.append(a)
        prev,cur,oldnorm = cur,[(xi-b)*ci-a*pi for xi,ci,pi in zip(x,cur,prev)],norm
    return beta,alpha


def layers(N, mar1, mar2):
    (be1,al1),(be2,al2) = mar1,mar2
    z = be1[0]*0
    c = {(0,0):dict(a1=z,a2=z,b1=be1[0],b2=be2[0])}
    degrees = []
    cancellation = []
    def d(nu):
        return c[nu]['b2']-c[nu]['b1']
    def div(num,nu):
        den=d(nu)
        if den == 0 or not mp.isfinite(den):
            raise ArithmeticError(f'zero/nonfinite divisor at {nu}')
        degrees.append(sum(nu))
        cancellation.append((abs(c[nu]['b1'])+abs(c[nu]['b2']))/abs(den))
        return num/den
    for s in range(N-1):
        new={}
        for p in range(s+2):
            q=s+1-p
            a1 = z if p==0 else al1[p] if q==0 else div(c[p,q-1]['a1']*d((p,q-1)),(p-1,q-1))
            a2 = z if q==0 else al2[q] if p==0 else div(c[p-1,q]['a2']*d((p-1,q)),(p-1,q-1))
            new[p,q]=dict(a1=a1,a2=a2)
        for p in range(s+1):
            nu=(p,s-p)
            up1,up2=(p+1,s-p),(p,s-p+1)
            lhs=new[up1]['a1']-new[up2]['a2']+new[up1]['a2']-new[up2]['a1']
            new[up2]['b1']=c[nu]['b1']-div(lhs,nu)
            new[up1]['b2']=new[up2]['b1']+d(nu)
        new[s+1,0]['b1']=be1[s+1]
        new[0,s+1]['b2']=be2[s+1]
        if any(not mp.isfinite(v) for r in new.values() for v in r.values()):
            raise ArithmeticError(f'nonfinite coefficient at layer {s+1}')
        c.update(new)
    return c,dict(divisions=len(degrees),max_divisor_degree=max(degrees),
                  max_d_subtraction_condition=float(max(cancellation)))


def compute(N,family,dps=None):
    x,w=inputs(N,family)
    cast=float if dps is None else mp.mpf
    def run():
        xx=[convert(t,cast) for t in x]
        ww=[[convert(t,cast) for t in row] for row in w]
        return layers(N,*(marginal(xx,row) for row in ww))
    if dps is None:
        return run()
    with mp.workdps(dps):
        return run()


def errors(got,ref):
    # Per-field sup norm relative error: zeros contribute to numerator but no
    # individual near-zero denominator; then maximum over the four fields.
    es={}
    for key in ('a1','a2','b1','b2'):
        scale=max(abs(row[key]) for row in ref.values())
        es[key]=max(abs(mp.mpf(got[nu][key])-r[key]) for nu,r in ref.items())/scale
    return max(es.values()),{k:float(v) for k,v in es.items()}


def exact_check(N,family,ref):
    path=Path(__file__).resolve().parents[1]/'audit-01/claude_layer_recursion_check.py'
    spec=importlib.util.spec_from_file_location('moment_checker',path)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    x,w=inputs(N,family)
    _,truth=module.ground_truth(x,w)
    converted={nu:{k:convert(v,mp.mpf) for k,v in r.items()} for nu,r in truth.items()}
    err,_=errors(ref,converted)
    return dict(N=N,method='auditor exact Fraction moment solve and coefficient matching',
                code_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                max_field_relative_error=float(err),passed=bool(err < mp.mpf('1e-70')))


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--sizes',nargs='+',type=int,default=[4,8,12,16,24,32])
    ap.add_argument('--family',choices=['krawtchouk','hahn'],default='krawtchouk')
    ap.add_argument('--dps',nargs=2,type=int,default=[100,160])
    args=ap.parse_args()
    if min(args.sizes)<2 or args.dps[0]<80 or args.dps[1]<=args.dps[0]:
        ap.error('N >= 2 and 80 <= lower precision < upper precision required')
    start=time.monotonic()
    out=[]
    with mp.workdps(args.dps[1]):
        for N in args.sizes:
            x,w=inputs(N,args.family)
            ident=json.dumps(dict(nodes=list(map(str,x)),weights=[list(map(str,r)) for r in w]),sort_keys=True)
            row=dict(N=N,M=N-1,family=args.family,input_sha256=hashlib.sha256(ident.encode()).hexdigest())
            try:
                lo,_=compute(N,args.family,args.dps[0])
                hi,diag=compute(N,args.family,args.dps[1])
                convergence,_=errors(lo,hi)
                row.update(reference_relative_agreement=float(convergence),reference_converged=bool(convergence<mp.mpf('1e-60')),reference_divisors=diag)
                if not row['reference_converged']:
                    raise ArithmeticError('reference precision convergence failed')
                dbl,diag=compute(N,args.family)
                error,fields=errors(dbl,hi)
                row.update(status='completed',relative_error_below_one=bool(error<1),max_field_relative_error=float(error),field_relative_errors=fields,
                           correct_decimal_digits=float(-mp.log10(error)) if error else None,
                           digits_lost_vs_binary64_epsilon=float(mp.log10(error/mp.mpf(sys.float_info.epsilon))) if error else None,
                           double_divisors=diag,
                           terminal_max_abs_d=float(max(abs(r['b2']-r['b1']) for nu,r in dbl.items() if sum(nu)==N-1)))
                if N==4:
                    row['exact_moment_check']=exact_check(N,args.family,hi)
                    if not row['exact_moment_check']['passed']:
                        raise ArithmeticError('exact moment cross-check failed')
            except (ArithmeticError,ZeroDivisionError,OverflowError,ValueError) as exc:
                row.update(status='failure',reason=str(exc))
            out.append(row)
    result=dict(status='MEASURED bounded pilot; no stability claim',
                python=platform.python_version(),mpmath=mp.__version__,platform=platform.platform(),
                code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                argv=sys.argv[1:],precision_dps=args.dps,epsilon=sys.float_info.epsilon,
                convention='N nodes k=0..M=N-1; z=2*k/M-1; monic a,b in z',
                elapsed_seconds=time.monotonic()-start,cases=out)
    print(json.dumps(result,indent=2,sort_keys=True,allow_nan=False))
    return 0 if all(r['status']=='completed' for r in out) else 1

if __name__=='__main__':
    sys.exit(main())
