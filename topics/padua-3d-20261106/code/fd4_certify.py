#!/usr/bin/env python3
"""D4 frozen diagnostics and exact fixed-point residual/mesh certificates."""
import argparse,base64,hashlib,itertools,json,math,os,platform,sys,time
from fractions import Fraction as F
from pathlib import Path
import numpy as np
import scipy
import mpmath as mp
from scipy.linalg import qr
TOP=Path(__file__).resolve().parents[1]
S=2**24

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ident(p): return {'path':str(p),'bytes':Path(p).stat().st_size,'sha256':sha(p)}
def idx(n): return [(a,b,c) for a in range(n+1) for b in range(n+1-a) for c in range(n+1-a-b)]
def basis(x,n):
    t=[np.polynomial.chebyshev.chebvander(x[:,j],n) for j in range(3)]
    return np.array([t[0][:,a]*t[1][:,b]*t[2][:,c] for a,b,c in idx(n)]).T

def beta(n):
    # Exact absolute error for float64 Chebyshev recurrence, then two products,
    # then nearest fixed-point quantization. Inputs are exact binary64 dyadics.
    u=F(1,2**53); e0=e1=F(0)
    for k in range(1,n): e0,e1=e1,2*e1+e0+8*u*(1+max(e0,e1))
    e=max(e0,e1); g=2*u/(1-2*u)
    v=3*e*(1+e)**2+g*(1+e)**3+F(1,2*S)
    return F(math.ceil(v*2**40),2**40)

def integer(x):
    assert np.isfinite(x).all() and np.max(abs(x))*S<2**62
    return np.rint(x*S).astype(np.int64)

def mul(a,b):
    # Scalar upper bound proves no integer multiply or partial sum overflows.
    assert a.shape[1]*int(np.max(abs(a)))*int(np.max(abs(b)))<2**63
    return a@b

def rownorm(a):
    assert a.shape[1]*int(np.max(abs(a)))<2**63
    return int(np.max(np.sum(abs(a),axis=1,dtype=np.int64)))

def rational_mpf(t):
    sign,man,exponent,bc=t
    return F((-1 if sign else 1)*man)*(F(2)**exponent)

def mesh(n,m):
    mp.iv.dps=60
    values=[];err=F(0)
    for j in range(m*n+1):
        z=mp.iv.cos(mp.iv.pi*j/(m*n));lo,hi=map(rational_mpf,z._mpi_)
        x=float((lo+hi)/2);x=max(-1.,min(1.,x))
        err=max(err,abs(F(x)-lo),abs(F(x)-hi));values.append(x)
    c=1/mp.iv.cos(mp.iv.pi/(2*m));cu=rational_mpf(c._mpi_[1])
    assert err<=F(1,2**52)
    return np.array(list(itertools.product(values,repeat=3))),F(1,2**52),F(math.ceil(cu*2**40),2**40)

def diagnostic(x,n):
    v=basis(x,n);scale=np.array([2.**(sum(k>0 for k in a)/2) for a in idx(n)])
    v=v*scale;d=np.sum(v*v,axis=1);b=v/np.sqrt(d[:,None]);e=np.linalg.eigvalsh(b@b.T)
    kinf=sum(2**sum(k>0 for k in a) for a in idx(n))
    return {'status':'MEASURED','lambda_min':float(e[0]),'lambda_max':float(e[-1]),
      'kernel_max_exact':kinf,'sum_inverse_kernel':float(np.sum(1/d)),
      'gram_bound_measured':float(np.sqrt(kinf*np.sum(1/d)/e[0]))}

def certificate(x,n,m,cap):
    started=time.monotonic();N=len(x);A=integer(basis(x,n));W=integer(np.linalg.inv(basis(x,n)))
    w=F(rownorm(W),S);R=np.eye(N,dtype=np.int64)*(S*S)-mul(A,W)
    r0=F(rownorm(R),S*S);be=beta(n);rho=r0+N*be*w
    assert rho<1,(n,float(rho))
    grid,delta,cm=mesh(n,m);bem=be+n*n*delta;maximum=0;arg=None;done=0
    for begin in range(0,len(grid),128):
        if time.monotonic()-started>cap:
            return {'status':'MEASURED_INFEASIBLE_AT_CAP','n':n,'m':m,'evaluated':done,'required':len(grid),'seconds':time.monotonic()-started,'cap':cap}
        P=integer(basis(grid[begin:begin+128],n));C=mul(P,W)
        assert N*int(np.max(abs(C)))<2**63
        norms=np.sum(abs(C),axis=1,dtype=np.int64);ii=int(np.argmax(norms));z=int(norms[ii])
        if z>maximum:maximum=z;arg=grid[begin+ii].tolist()
        done+=len(P)
    mid=F(maximum,S*S);error=N*bem*w
    lower=max(F(0),mid-error)/(1+rho);upper=(mid+error)/(1-rho)*cm
    return {'status':'CERTIFIED_WITH_EXPLICIT_LITERATURE_DEPENDENCY_PENDING_INDEPENDENT_RERUN',
      'n':n,'m':m,'N':N,'evaluated':done,'seconds':time.monotonic()-started,
      'fixedpoint_bits':24,'beta_fraction':str(be),'mesh_coordinate_error_fraction':str(delta),
      'inverse_norm_fraction':str(w),'residual_quantized_fraction':str(r0),'rho_fraction':str(rho),
      'mesh_max_integer':maximum,'mesh_arg_dyadic':arg,'mesh_error_fraction':str(error),
      'mesh_constant_upper_fraction':str(cm),'lower_fraction':str(lower),'upper_fraction':str(upper),
      'interval_display':[float(lower),float(upper)],'rho_display':float(rho)}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--degrees',nargs='+',type=int,required=True)
    ap.add_argument('--family',choices=['qr','payload12'],required=True);ap.add_argument('--m',type=int,default=2)
    ap.add_argument('--cap',type=float,default=120);ap.add_argument('--scratch',type=Path,required=True);ap.add_argument('--output',type=Path,required=True)
    a=ap.parse_args();a.scratch.mkdir(parents=True,exist_ok=False);rows=[]
    out={'schema':'fd4-exact-certificate-v1','command':sys.argv,'source':ident(__file__),
      'versions':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,'mpmath':mp.__version__},
      'seed':None,'threads':{k:os.getenv(k) for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS')},'rows':rows}
    for n in a.degrees:
        started=time.monotonic()
        if a.family=='payload12':
            assert n==12
            source=TOP/'evidence/u2-degree12-nodes.json';d=json.loads(source.read_text())
            raw=base64.b85decode(d['coordinates_base85']);assert hashlib.sha256(raw).hexdigest()==d['coordinates_sha256']
            x=np.frombuffer(raw,dtype='<f8').reshape(-1,3).copy();inputid=ident(source)
        else:
            # Deterministic inherited QR candidate grid; new runtime coordinates
            # are their exact dyadic values, not historical optimized endpoints.
            t=np.cos(np.linspace(0,np.pi,2*n+1));candidate=np.array(list(itertools.product(t,repeat=3)))
            piv=qr(basis(candidate,n).T,pivoting=True,mode='economic')[2]
            x=candidate[piv[:math.comb(n+3,3)]].copy();inputid={'generator':'QR on (2n+1)^3 rounded Lobatto grid; fd4 basis order'}
        assert len(x)==math.comb(n+3,3) and len(np.unique(x,axis=0))==len(x) and np.max(abs(x))<=1
        nodefile=a.scratch/f'n{n}-{a.family}.npy';np.save(nodefile,x)
        raw=x.astype('<f8').tobytes()
        payloadfile=TOP/'evidence'/f'fd4-{a.family}-n{n}-nodes.json'
        payload=json.dumps({'n':n,'N':len(x),'dtype':'<f8','shape':[len(x),3],'coordinates_sha256':hashlib.sha256(raw).hexdigest(),'coordinates_base85':base64.b85encode(raw).decode()},separators=(',',':'))+'\n'
        assert len(payload.encode())<=32768
        if a.family=='qr': payloadfile.write_text(payload)
        row={'n':n,'family':a.family,'input':inputid,'nodes':ident(nodefile),'coordinates_sha256':hashlib.sha256(raw).hexdigest()}
        if a.family=='qr': row['essential_payload']=ident(payloadfile)
        row['gram']=diagnostic(x,n);row['certificate']=certificate(x,n,a.m,a.cap);row['total_seconds']=time.monotonic()-started;rows.append(row)
        payload=json.dumps(out,separators=(',',':'))+'\n';assert len(payload.encode())<=32768;a.output.write_text(payload)
        print(json.dumps({'n':n,'family':a.family,'gram':row['gram'],'certificate':row['certificate']['status'],'interval':row['certificate'].get('interval_display'),'seconds':row['total_seconds']}),flush=True)

if __name__=='__main__':main()
