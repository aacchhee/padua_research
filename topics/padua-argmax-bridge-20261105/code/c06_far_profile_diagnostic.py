#!/usr/bin/env python3
"""MEASURED fixed-count far model diagnostic; no rigorous arithmetic claim."""
import argparse
import hashlib
import json
import math
from pathlib import Path
import platform
import resource
import time
import warnings
import numpy as np
import scipy
from scipy.integrate import quad, IntegrationWarning
from scipy.special import digamma

PI = math.pi
GAMMA = float(np.euler_gamma)
R = 64
DELTA = .01
K = 4096


def phi(t):
    t = t % 1.0
    if t == 0.0:
        return 1.0
    return math.sin(PI*t)/PI*(-digamma(t)-digamma(1-t)-2*math.log(PI))


def J(u, s, eps):
    if s <= u:
        if u == 0:
            return 0.0
        c, b = (u-s)/2, (u+s)/2
        return 2*((c*math.log(c/u) if c else 0.0) + b*math.log(b/u))
    logsin = math.log(max(math.sin(eps), 1e-300))
    base = 2*s*logsin
    if s*math.sin(eps) >= u or u == 0:
        return base
    theta = math.asin(min(1.0, s*math.sin(eps)/u))
    x1 = max(0., (theta-eps)/2)
    c, b = (s-u)/2, (s+u)/2
    q1 = math.log(max(math.cos(x1), 1e-300))-math.log(max(math.sin(x1+eps), 1e-300))
    q2 = math.log(max(math.cos(x1+eps), 1e-300))-math.log(max(math.sin(x1), 1e-300))
    return base + 2*(b*q1-c*q2)


def I(alpha, beta, v):
    a = (math.cos(alpha)+math.cos(beta))/2
    p, q = math.sin(alpha), math.sin(beta)
    eps = abs(v-PI) if abs(v-PI) <= PI/2 else min(v, 2*PI-v)
    s = abs(q/2 + a/math.tan(v/2))
    return J(p/2, s, eps)


def g_R(t):
    x = np.arange(R, K+1, dtype=float) + t
    z = R+t-.5
    # Fixed count. The omitted analytic tail is <=(log(K+t+.5)+2)/(8*(K+t+.5)^2).
    return -.5*math.log(z)**2 + float(np.sum(np.log(x)/x
        -.5*(np.log(x+.5)**2-np.log(x-.5)**2)))


def ell(alpha, b, r):
    w = r*PI+b
    if w == 0.0:
        return 1.0
    js = np.arange(-r+1, r, 2)
    zs = js*PI+alpha
    sig1 = 1-2*(((r-js-1)//2) % 2)
    sig2 = 1-2*(((js+r-1)//2) % 2)
    ce, cd = math.cos((alpha+b)/2), math.cos((alpha-b)/2)
    fs = (ce*sig1*np.sinc((zs-w)/(2*PI))
          +cd*sig2*np.sinc((zs+w)/(2*PI)))/w
    return math.sin(b)/w+2*float(np.sum(fs))


def profile(alpha, beta, L):
    a = max(0., (math.cos(alpha)+math.cos(beta))/2)
    ce, cd = math.cos((alpha+beta)/2), math.cos((alpha-beta)/2)
    U0 = ce*phi(.5+(alpha-beta)/(2*PI))+cd*phi(.5+(alpha+beta)/(2*PI))
    B0 = 4*a/PI**2
    b = 2*U0/PI+(8*a*math.log(2)+(4*a*math.log(a) if a else 0.)
                  +2*(alpha*math.sin(alpha)+beta*math.sin(beta)))/PI**2
    CR = (math.sin(beta)/beta if beta else 1.)
    CR += sum(ell(alpha, beta, r) for r in range(1, R))
    CR += sum(ell(alpha, -beta, r) for r in range(1, R+1))
    ts = [beta/PI, 1-beta/PI]
    D0 = U0/PI+B0*math.log(PI)
    kap = math.log(DELTA/PI)
    cm = B0*kap**2+2*D0*kap-D0*sum(digamma(R+t) for t in ts)
    cm += B0*sum(g_R(t) for t in ts)

    def bv(v):
        value = (ce*phi(.5+(alpha-beta+v)/(2*PI))
                 +cd*phi(.5+(alpha+beta-v)/(2*PI)))/(2*math.sin(v/2))
        return value+I(alpha,beta,v)/PI

    marks = sorted(set([DELTA, PI/2, PI, 3*PI/2, 2*PI-DELTA] +
                       [x for x in [PI-alpha+beta, PI+alpha+beta, PI+alpha-beta]
                        if DELTA<x<2*PI-DELTA]))
    integral, estimate = 0., 0.
    messages = []
    with warnings.catch_warnings(record=True) as ws:
        warnings.simplefilter('always', IntegrationWarning)
        for lo, hi in zip(marks, marks[1:]):
            val, err = quad(bv, lo, hi, epsabs=1e-8, epsrel=2e-9, limit=200)
            integral += val
            estimate += err
        messages = [str(w.message) for w in ws]
    C = CR+cm+integral/PI
    return dict(a=a,b=b,constant=C,value=B0*L*L+b*L+C,
                endpoint_rows=CR,mesh_constant=cm,integral=integral/PI,
                integration_error_estimate=estimate/PI,warnings=messages)


def controls():
    ans = []
    for u,s,eps in [(.1,.2,.3),(.2,.1,.3),(.3,.5,1.1),(.2,.25,.1)]:
        C,D=(u-s)/2,(u+s)/2
        def f(x):
            xx, yy = C/math.tan(x),D/math.tan(x+eps)
            return -2*min(abs(xx),abs(yy)) if xx*yy<0 else 0.
        marks=sorted(set([0., PI, PI/2, PI-eps, PI/2-eps]))
        integ=sum(quad(f,lo,hi,epsabs=1e-10,limit=200)[0]
                  for lo,hi in zip(marks,marks[1:]))
        formula=J(u,s,eps)
        ans.append(dict(u=u,s=s,epsilon=eps,direct=integ,formula=formula,
                        discrepancy=abs(integ-formula)))
    return ans


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    dest=Path(args.output)
    if dest.exists():
        raise FileExistsError(dest)
    resource.setrlimit(resource.RLIMIT_CPU,(180,180))
    start=time.process_time()
    ctrl=controls()
    if max(x['discrepancy'] for x in ctrl)>1e-7:
        raise ArithmeticError(ctrl)
    L=math.log(1e6)
    bc=8*(GAMMA+math.log(8/PI))/PI**2
    corner=4/PI**2*L*L+bc*L+1.8461603104239261
    rows=[]
    for rho in [.5,.75,1.,1.5,2.,2.5,PI]:
        for fraction in [0.,.25,.5,.75,1.]:
            alpha,beta=rho*fraction,rho*(1-fraction)
            row=profile(alpha,beta,L)
            row.update(rho=rho,alpha=alpha,beta=beta,
                       fraction=fraction,model_minus_corner=row['value']-corner)
            rows.append(row)
    result=dict(status='MEASURED',scope='35 fixed-count continuous model cases, no finite-n primitive evaluation',
                input_head='b6e67b3c78cb668b6d2f9da5a5560537d2960bf3',
                source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                R=R,delta=DELTA,g_R_last_index=K,L=L,corner_polynomial=corner,
                versions=dict(python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__),
                cpu_seconds=time.process_time()-start,controls=ctrl,rows=rows,
                limitation='Binary64 quadrature estimates are not rigorous errors. The all-phase model approximation and maximum remain unproved.')
    dest.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(output=str(dest),sha256=hashlib.sha256(dest.read_bytes()).hexdigest(),
        bytes=dest.stat().st_size,cpu_seconds=result['cpu_seconds'],cases=len(rows),
        max_model_minus_corner=max(r['model_minus_corner'] for r in rows),
        warnings=sum(len(r['warnings']) for r in rows),max_control_error=max(r['discrepancy'] for r in ctrl))))

if __name__=='__main__':
    main()
