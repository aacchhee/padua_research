#!/usr/bin/env python3
"""Finite endpoint-model Galerkin measurements; no actual-N fit or proof."""
import argparse, datetime, hashlib, json, math, platform, sys, time
from pathlib import Path
import numpy as np
import scipy
from scipy.integrate import quad
from scipy.linalg import eigh
from scipy.special import sici

PIN='2143ad622fa98faf8fe7d5cb8ed2bb7e0062f861'
PREDICTION_COMMIT='513f3bd802abf23f9c1470930a68f4e09e2a8c77'
def gram(J):
    j=np.arange(1,J+1,dtype=float); a=np.pi*j; a2=a*a
    sign=(-1.)**j
    si,ci=sici(2*a); d=np.euler_gamma+np.log(2*a)-ci
    den=a2[:,None]-a2[None,:]
    num=a2[:,None]*d[None,:]-a2[None,:]*d[:,None]
    np.fill_diagonal(den,1.)
    C=2*(sign[:,None]*sign[None,:])*num/den
    np.fill_diagonal(C,2*(a*si+d))
    omega=2*(sign+a*sici(a)[0])
    D=np.diag(omega)+4*np.outer(sign,sign)
    return C,D

def fj(t,j):
    a=math.pi*j
    if abs(t-a)<0.25:
        z=t-a
        sinc=1. if z==0 else math.sin(z)/z
        return 2*a*a*sinc/(t*(t+a))
    sinc=1. if t==0 else math.sin(t)/t
    return 2*((-1)**j)*a*a*sinc/(t*t-a*a)

def quadrature(i,j,periods=2000):
    # Split at every zero of sin(t); the remote tail has a recorded envelope.
    total=error=0.
    for k in range(periods):
        val,err=quad(lambda t:t*fj(t,i)*fj(t,j),k*math.pi,(k+1)*math.pi,
                     epsabs=2e-13,epsrel=2e-13,limit=50)
        total+=val;error+=err
    T=periods*math.pi
    assert T>=2*math.pi*max(i,j)
    # |f_j(t)| <= (8/3) a_j^2/t^3 for t >= 2 max a_j.
    tail_bound=(16/9)*(math.pi*i)**2*(math.pi*j)**2/T**4
    return dict(value=total,quadrature_reported_error=error,
                analytic_absolute_tail_bound=tail_bound,T=T)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--sizes',type=int,nargs='+',default=[32,64,128,256,512]);ap.add_argument('--output',type=Path,required=True);ap.add_argument('--quad-periods',type=int,default=2000);args=ap.parse_args()
    start=time.monotonic()
    result=dict(status='MEASURED',input_sha=PIN,prediction_commit=PREDICTION_COMMIT,
        started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        command=sys.argv,python=sys.version,numpy=np.__version__,scipy=scipy.__version__,
        platform=platform.platform(),producer_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        finite_N_fit_executed=False,infinite_model_tail_certified=False,
        description='Finite Galerkin eigenvalues and numerical quadrature checks of the registered exact endpoint form.',quadrature=[],galerkin=[])
    C3,_=gram(3)
    for i,j in [(1,1),(1,2),(2,2),(1,3),(2,3),(3,3)]:
        q=quadrature(i,j,args.quad_periods);q.update(i=i,j=j,closed_form=float(C3[i-1,j-1]));q['absolute_difference']=abs(q['value']-q['closed_form']);q['within_reported_quad_plus_tail']=q['absolute_difference']<=q['quadrature_reported_error']+q['analytic_absolute_tail_bound']+1e-12;result['quadrature'].append(q)
    previous=None
    for J in args.sizes:
        tick=time.monotonic();C,D=gram(J)
        vals,vecs=eigh(D,C,subset_by_index=[J-1,J-1],driver='gvx');lam=float(vals[0]);v=vecs[:,0]
        res=np.linalg.norm(D@v-lam*(C@v))/max(np.linalg.norm(D@v),1.)
        row=dict(J=J,lambda_max=lam,relative_generalized_residual=float(res),seconds=time.monotonic()-tick,change_from_previous=None if previous is None else lam-previous)
        result['galerkin'].append(row);previous=lam
        print(row,flush=True)
    result['elapsed_seconds']=time.monotonic()-start
    result['limits']='No certified infinite Galerkin tail and no full actual-CC spectral limit. Floating residuals do not certify eigenvalues.'
    args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
if __name__=='__main__':main()
