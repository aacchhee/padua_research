#!/usr/bin/env python3
"""Frozen T9 maxima refinement; binary64 lower samples, no certification."""
import itertools as it,json,sys,time,hashlib,math,os
from pathlib import Path
import numpy as np
import scipy
from scipy.linalg import qr
from scipy.optimize import minimize
TOP=Path(__file__).resolve().parents[1]; ROOT=TOP.parents[1]
sys.path.insert(0,str(ROOT/'tracks/lattice-unisolvence/code'))
import c3_lebesgue as old
from c3_rank import exponents
from t4_stacks import permutation,stack
START=time.monotonic()
DET={}
def basis_angle(t,n,gradient=False):
    a=np.asarray(exponents(n)); c=np.cos(a*t)
    v=np.prod(c,axis=1)
    if not gradient:return v
    g=np.array([-a[:,j]*np.sin(a[:,j]*t[j])*np.prod(c[:,[k for k in range(3) if k!=j]],axis=1) for j in range(3)])
    return v,g
def angular_mesh(q):return np.array(list(it.product(np.linspace(0,np.pi,q),repeat=3)))
def grid(inv,n,q,all_values=False):
    t=angular_mesh(q); vals=[]
    for k in range(0,len(t),512):
        cards=old.basis(np.cos(t[k:k+512]),n)@inv
        vals.append(cards if all_values else np.sum(abs(cards),axis=1))
    return t,np.concatenate(vals)
def refine(inv,n,starts,column=None):
    def objective(t):
        v,g=basis_angle(t,n,True)
        if column is None:
            c=v@inv; s=np.sign(c); return -sum(abs(c)),-g@inv@s
        c=v@inv[:,column];return -abs(c),-np.sign(c)*(g@inv[:,column])
    best=-np.inf;where=None;good=0
    for t in starts:
        r=minimize(objective,t,jac=True,bounds=[(0,np.pi)]*3,method='L-BFGS-B',options={'maxiter':200,'maxfun':5000,'ftol':1e-12,'gtol':1e-8})
        good+=bool(r.success)
        # Include initial value because nonsmooth search may terminate early.
        for x in (t,r.x):
            z=-objective(x)[0]
            if z>best:best=z;where=np.asarray(x)
    return best,where,good
def qrpoints(n):
    cand=np.array(list(it.product(old.lobatto(2*n+1),repeat=3)))
    piv=qr(old.basis(cand,n).T,pivoting=True,mode='economic')[2]
    return cand[piv[:math.comb(n+3,3)]].copy()
def points(n,family):
    if family=='qr':return qrpoints(n)
    if family=='leja':
        x=old.discrete_leja(old.lobatto(n+1))
        return np.array([[x[a],x[b],x[c]] for a,b,c in exponents(n)])
    if family=='stack':return stack(n,permutation(n,'L'))[0]
    if family=='cyclic':return np.cos(2*np.pi*np.arange(35)[:,None]*np.array([1,15,19])[None,:]/69)
    p=qrpoints(n)
    initial=float(np.linalg.slogdet(old.basis(p,n))[1])
    for sweep in range(2):
        for j in range(len(p)):
            inv=np.linalg.inv(old.basis(p,n)); t,c=grid(inv,n,21,True)
            idx=np.argsort(abs(c[:,j]))[-4:]
            starts=list(t[idx])+[np.arccos(np.clip(p[j],-1,1))]
            val,where,_=refine(inv,n,starts,j)
            if val>1+1e-10:p[j]=np.cos(where)
    DET[n]=[initial,float(np.linalg.slogdet(old.basis(p,n))[1])]
    return p
def measure(n,family):
    before=time.monotonic(); p=points(n,family);v=old.basis(p,n)
    cond=float(np.linalg.cond(v)); inv=np.linalg.inv(v)
    residual=float(np.linalg.norm(v@inv-np.eye(len(p)),ord=np.inf))
    r={'n':n,'family':family,'cond':cond,'resid':residual}
    if family=='localdet':r['logdet']=DET[n]
    if cond>=1e12 or residual>1e-7:r['suppressed']=True;return r
    t,c=grid(inv,n,21);r['mesh21']=float(max(c))
    t,c=grid(inv,n,41);r['mesh41']=float(max(c))
    if r['mesh41']<r['mesh21']-1e-8*max(1,r['mesh21']):raise RuntimeError('nested mesh maximum decreased')
    starts=list(t[np.argsort(c)[-4:]])+list(it.product([0,np.pi],repeat=3))
    val,where,good=refine(inv,n,starts)
    r.update({'local':float(max(val,r['mesh41'])),'argtheta':[round(float(x),9) for x in where],'success':good,'seconds':round(time.monotonic()-before,2)})
    # Raw nodes are regeneration-only; they are not essential theorem evidence.
    np.save('/tmp/t9-'+family+'-'+str(n)+'.npy',p)
    return r
def fit(rows,family):
    x=np.array([r['n'] for r in rows if r['family']==family and 'local'in r]); y=np.log([r['local'] for r in rows if r['family']==family and 'local'in r])
    if len(x)<4:return {'status':'INCONCLUSIVE','count':len(x)}
    z=np.log(x);alpha=max(1,float(np.cov(z,y,bias=True)[0,1]/np.var(z)))
    sse=lambda pred:float(sum((y-pred)**2))
    return {'count':len(x),'polylog_sse':{str(k):sse(np.mean(y-k*np.log(z))+k*np.log(z)) for k in (1,2,3,4)},'polynomial_alpha':alpha,'polynomial_sse':sse(np.mean(y-alpha*z)+alpha*z)}
def main():
    sources=[ROOT/'tracks/lattice-unisolvence/code/c3_lebesgue.py',ROOT/'tracks/lattice-unisolvence/code/c3_rank.py',Path(__file__).with_name('t4_stacks.py')]
    out={'schema':'t9-maxima-v1','status':'MEASURED samples; no exact unisolvence or sup enclosure','sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'sources':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},'versions':[np.__version__,scipy.__version__],'rows':[],'unrun':[]}
    cases=[(n,f) for n in range(4,13) for f in ('qr','leja')]+[(n,'stack') for n in range(4,8)]+[(4,'cyclic')]+[(n,'localdet') for n in (2,3,4)]
    path=TOP/'evidence/t9-maxima.json'
    for i,(n,f) in enumerate(cases):
        if time.monotonic()-START>1200:out['unrun']=cases[i:];break
        r=measure(n,f);out['rows'].append(r);print(json.dumps(r),flush=True)
        path.write_text(json.dumps(out,separators=(',',':'))+'\n')
    out['fits']={f:fit(out['rows'],f) for f in ('qr','leja')};out['seconds']=round(time.monotonic()-START,2)
    out['threads']={k:os.environ.get(k) for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS')}
    path.write_text(json.dumps(out,separators=(',',':'))+'\n')
if __name__=='__main__':main()
