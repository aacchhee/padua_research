#!/usr/bin/env python3
"""Measured full-data Gauss-Newton fits and exact rational common-data witness.

Fixed coefficient SPD metric: sum of squared field-scaled errors, with
scales from the exact-input reference. Input chart: ordered nodes and two
softmax weight vectors (last logit fixed). Full analytic Jacobian from D1.
This computes a stationary candidate, NOT a certified global nearest point.
Raw-array strict backward error is not replaced by this two-part witness.
"""
import argparse
from fractions import Fraction
import hashlib
import importlib.util
import json
from pathlib import Path
import platform
import sys
import time

import mpmath as mp

HERE=Path(__file__).resolve().parent


def imported(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    out=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(out)
    return out


native=imported('native_projection',HERE/'native_mixed.py')
joint=imported('joint_projection',HERE/'backward_joint.py')
ad=imported('ad_projection',HERE/'conditioning.py')
c4=native.c4
FIELDS=('a1','a2','b1','b2')


def image(x,w):
    return c4.layers(len(x),*(c4.marginal(x,r) for r in w))[0]


def full_ad(x,w):
    N=len(x)
    def seed(v,k):
        g=[mp.mpf(0)]*(3*N)
        g[k]=mp.mpf(1)
        return ad.Dual(v,g)
    xx=[seed(v,k) for k,v in enumerate(x)]
    ww=[[seed(v,(s+1)*N+k) for k,v in enumerate(r)] for s,r in enumerate(w)]
    return ad.layers(N,*(ad.marginal(xx,r) for r in ww))


def chart(v,x0,w0):
    N=len(x0)
    x=list(v[:N])
    weights=[]
    for s in range(2):
        q=[w0[s][i]*mp.exp(v[N+s*(N-1)+i]) for i in range(N-1)]+[w0[s][-1]]
        weights.append([a/sum(q) for a in q])
    if not all(x[i]<x[i+1] for i in range(N-1)):
        raise ArithmeticError('trial node ordering failed')
    return x,weights


def chart_jacobian(c,w,order,scale,N):
    """Complete coefficient Jacobian in the fixed-mass softmax chart."""
    J=mp.matrix(len(order),3*N-2)
    for row,(nu,f) in enumerate(order):
        g=c[nu][f].g or [mp.mpf(0)]*(3*N)
        for i in range(N): J[row,i]=g[i]/scale[f]
        for s in range(2):
            avg=sum(w[s][l]*g[(s+1)*N+l] for l in range(N))
            for i in range(N-1):
                J[row,N+s*(N-1)+i]=w[s][i]*(g[(s+1)*N+i]-avg)/scale[f]
    return J


def least_squares(A,b):
    """Real Householder QR with sign(0)=+1, including structural zero rows.

    mpmath1.3.0 qr_solve uses sign(0)=0 in its reflector and fails when
    the first structural-zero derivative row meets the diagonal pivot.
    """
    m,n=A.rows,A.cols
    R=[list(A[i,:])+[b[i]] for i in range(m)]
    for j in range(n):
        v=[R[i][j] for i in range(j,m)]
        norm=mp.sqrt(mp.fdot(v,v))
        if not norm:raise ArithmeticError('rank loss in full-data Jacobian')
        alpha=-norm if v[0]>=0 else norm
        v[0]-=alpha
        den=mp.fdot(v,v)
        for k in range(j+1,n+1):
            fac=2*mp.fdot(v,[R[i][k] for i in range(j,m)])/den
            for i,z in zip(range(j,m),v):R[i][k]-=fac*z
        R[j][j]=alpha
        for i in range(j+1,m):R[i][j]=mp.mpf(0)
    out=[mp.mpf(0)]*n
    for j in reversed(range(n)):
        out[j]=(R[j][n]-mp.fsum(R[j][k]*out[k] for k in range(j+1,n)))/R[j][j]
    return mp.matrix(out)


def fit(raw,N,family,dps=100,maxiter=10):
    with mp.workdps(dps):
        xq,wq=c4.inputs(N,family)
        x0=[c4.convert(a,mp.mpf) for a in xq]
        w0=[[c4.convert(a,mp.mpf) for a in r] for r in wq]
        w0=[[a/sum(r) for a in r] for r in w0]
        ref=image(x0,w0)
        sites=sorted(ref,key=lambda p:(sum(p),p))
        order=[(nu,f) for nu in sites for f in FIELDS]
        scale={f:max(abs(r[f]) for r in ref.values()) for f in FIELDS}
        def residual(c,dual=False):
            return mp.matrix([(mp.mpf(raw[nu][f])-(c[nu][f].v if dual else c[nu][f]))/scale[f]
                              for nu,f in order])
        v=mp.matrix(x0+[mp.mpf(0)]*(2*(N-1)))
        history=[]
        converged=False
        stop_reason='iteration limit'
        for iteration in range(maxiter):
            x,w=chart(v,x0,w0)
            c=full_ad(x,w)
            r=residual(c,True)
            J=chart_jacobian(c,w,order,scale,N)
            gradient=J.T*r
            denom=mp.norm(J)*mp.norm(r)
            stationarity=mp.norm(gradient)/denom if denom else mp.mpf(0)
            delta=least_squares(J,r)
            cost=mp.fdot(r,r)
            history.append(dict(iteration=iteration,cost=str(cost),
                                scaled_stationarity=str(stationarity),
                                chart_step_sup=str(max(map(abs,delta)))))
            if stationarity<mp.mpf('1e-55') or max(map(abs,delta))<mp.mpf('1e-70'):
                converged=bool(stationarity<mp.mpf('1e-55'))
                stop_reason='stationarity threshold' if converged else 'small chart step'
                break
            accepted=False
            for backtrack in range(24):
                fac=mp.mpf(2)**(-backtrack)
                trial=v+fac*delta
                try:
                    xt,wt=chart(trial,x0,w0)
                    rt=residual(image(xt,wt))
                    trialcost=mp.fdot(rt,rt)
                except (ArithmeticError,ZeroDivisionError,ValueError):
                    continue
                if trialcost<cost:
                    v=trial
                    accepted=True
                    history[-1]['step_factor']=str(fac)
                    break
            if not accepted:
                history[-1]['stopped']='no decreasing line-search step'
                stop_reason='no decreasing line-search step'
                break
        x,w=chart(v,x0,w0)
        qx=[Fraction(mp.nstr(a,70)) for a in x]
        qw=[[Fraction(mp.nstr(a,70)) for a in row] for row in w]
        qw=[[a/sum(row) for a in row] for row in qw]
        assert all(a>0 for row in qw for a in row)
        assert all(qx[i]<qx[i+1] for i in range(N-1))
        normality=joint.normality_exact(qx,qw) if N<=8 else None
    # Evaluate the actual frozen rational witness at a higher precision.
    with mp.workdps(180):
        xx=[c4.convert(a,mp.mpf) for a in qx]
        ww=[[c4.convert(a,mp.mpf) for a in row] for row in qw]
        xtruth=[c4.convert(a,mp.mpf) for a in xq]
        wtruth=[[c4.convert(a,mp.mpf) for a in row] for row in wq]
        wtruth=[[a/sum(row) for a in row] for row in wtruth]
        rec=image(xx,ww)
        truth=image(xtruth,wtruth)
        fields={f:max(abs(mp.mpf(raw[nu][f])-rec[nu][f]) for nu in rec)/
                   max(abs(row[f]) for row in truth.values()) for f in FIELDS}
        r=mp.matrix([(mp.mpf(raw[nu][f])-rec[nu][f])/
                     max(abs(row[f]) for row in truth.values()) for nu,f in order])
        scale={f:max(abs(row[f]) for row in truth.values()) for f in FIELDS}
        Jreturned=chart_jacobian(full_ad(xx,ww),ww,order,scale,N)
        denom=mp.norm(Jreturned)*mp.norm(r)
        returned_stationarity=mp.norm(Jreturned.T*r)/denom if denom else mp.mpf(0)
        data=max(max(abs(a-b) for a,b in zip(xx,xtruth))/max(map(abs,xtruth)),
                 max(abs(a-b)/b for row,old in zip(ww,wtruth) for a,b in zip(row,old)))
        rep=dict(nodes=list(map(str,qx)),normalized_weights=[list(map(str,row)) for row in qw])
        ident=json.dumps(rep,sort_keys=True).encode()
        originalE,_=c4.errors(raw,truth)
        return dict(optimizer_stationarity_converged=converged,
                    optimizer_iterations=len(history),optimizer_history=history,
                    optimizer_stop_reason=stop_reason,optimizer_stationarity_threshold='1e-55',
                    returned_witness_scaled_stationarity=float(returned_stationarity),
                    returned_witness_stationarity_dps=180,
                    input_mixed_sup=float(data),input_in_units_u=float(data*2**53),
                    full_coefficient_correction=float(max(fields.values())),
                    correction_in_units_u=float(max(fields.values())*2**53),
                    coefficient_SPD_norm=float(mp.norm(r)),
                    original_forward_E=float(originalE),fields={f:float(a) for f,a in fields.items()},
                    exact_normality_systems_checked=normality,
                    min_rational_weight=float(min(a for row in ww for a in row)),
                    rational_input_sha256=hashlib.sha256(ident).hexdigest(),rational_input=rep,
                    dps=dps,scope='unrounded optimizer convergence and returned rational witness stationarity are separate; finite positive common-data witness, not certified nearest minimizer or raw strict backward error')


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--family',required=True,choices=['krawtchouk','hahn'])
    ap.add_argument('--sizes',type=int,nargs='+',default=[4,8])
    ap.add_argument('--methods',nargs='+',default=['c4','lu','nodeqr'])
    ap.add_argument('--dps',type=int,default=100)
    args=ap.parse_args()
    rows=[]
    start=time.monotonic()
    for N in args.sizes:
        for method in args.methods:
            raw,_=c4.compute(N,args.family) if method=='c4' else native.compute(N,args.family,method)
            row=fit(raw,N,args.family,args.dps)
            rows.append(dict(N=N,family=args.family,method=method,**row))
    hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in
            [Path(__file__),HERE/'conditioning.py',HERE/'native_mixed.py',HERE/'backward_joint.py',native.BASE]}
    print(json.dumps(dict(status='MEASURED full-Jacobian common-data stationary fits',
        python=platform.python_version(),mpmath=mp.__version__,argv=sys.argv[1:],
        source_sha256=hashes,elapsed_seconds=time.monotonic()-start,cases=rows),indent=2,sort_keys=True,allow_nan=False))


if __name__=='__main__':main()
