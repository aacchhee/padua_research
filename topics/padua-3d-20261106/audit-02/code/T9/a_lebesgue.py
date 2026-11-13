# Independent Lebesgue-constant re-evaluation of the T9-06 node sets (own basis, finer mesh, more starts). MEASURED lower samples.
import numpy as np, itertools as it, json, sys, math
from scipy.optimize import minimize
B=sys.argv[1]; rec=json.load(open(B+'/orig/t9-maxima.json'))
def E(n): return [(a,b,c) for a in range(n+1) for b in range(n+1-a) for c in range(n+1-a-b)]
def basis_t(T,n):  # angle input
    e=np.array(E(n)); return np.prod(np.cos(e[None,:,:]*T[:,None,:]),axis=2)
out=[]
q=int(sys.argv[2]) if len(sys.argv)>2 else 51
grid=np.array(list(it.product(np.linspace(0,np.pi,q),repeat=3)))
for r in rec['rows']:
    n,fam=r['n'],r['family']
    P=np.load(f"{B}/out/t9-{fam}-{n}.npy"); T=np.arccos(np.clip(P,-1,1))
    Vi=np.linalg.inv(basis_t(T,n))
    vals=np.concatenate([np.abs(basis_t(grid[k:k+4096],n)@Vi).sum(1) for k in range(0,len(grid),4096)])
    top=grid[np.argsort(vals)[-24:]]
    rng=np.random.default_rng(n); rand=rng.uniform(0,np.pi,(16,3))
    f=lambda t: -np.abs(basis_t(np.clip(t,0,np.pi)[None,:],n)@Vi).sum()
    best=vals.max()
    for s in list(top)+list(rand):
        z=-minimize(f,s,method='Nelder-Mead',options={'xatol':1e-10,'fatol':1e-12,'maxiter':4000}).fun
        best=max(best,z)
    out.append((fam,n,r['local'],vals.max(),best,best/r['local']-1))
    print(fam,n,'receipt local',round(r['local'],6),' mesh%d'%q,round(vals.max(),6),' audit local',round(best,6),' rel diff %.2e'%(best/r['local']-1),flush=True)
print('min rel diff (audit - receipt)/receipt',min(o[5] for o in out),' max',max(o[5] for o in out))
