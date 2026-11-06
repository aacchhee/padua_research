# Independent matrix-free Padua minimum at large m (own Lanczos via scipy eigsh). No repo imports.
import numpy as np, json, sys, time
from scipy.sparse.linalg import LinearOperator, eigsh
sys.path.insert(0,sys.argv[0].rsplit('/',1)[0])
from ind_padua import legn, weights_formula, nodes
out=[]
for m in [int(a) for a in sys.argv[2:]]:
    t0=time.time(); c0=time.process_time()
    J,K,th,ph=nodes(m); w=weights_formula(m)
    W=np.zeros((m+1,m+2)); W[J,K]=w
    n=m; Px=legn(n,np.cos(np.arange(m+1)*np.pi/m)); Py=legn(n,np.cos(np.arange(m+2)*np.pi/(m+1)))
    mask=np.add.outer(np.arange(n),np.arange(n))<=n-1; dim=int(mask.sum()); cnt=[0]
    def mv(v):
        cnt[0]+=1; C=np.zeros((n,n)); C[mask]=v.ravel()
        V=Px.T@C@Py; R=Px@(W*V)@Py.T; return R[mask]
    op=LinearOperator((dim,dim),matvec=mv,dtype=float)
    rng=np.random.default_rng(12345+m)
    vals,vecs=eigsh(op,k=1,which='SA',tol=1e-12,ncv=60,maxiter=3000,v0=rng.standard_normal(dim))
    v=vecs[:,0]; res=np.linalg.norm(mv(v)-vals[0]*v)/np.linalg.norm(v)
    d=dict(m=m,dim=dim,weight_sum=w.sum(),neg_count=int((w<0).sum()),neg_mass=float(-w[w<0].sum()),lam_min=float(vals[0]),residual=float(res),matvecs=cnt[0],wall=time.time()-t0,cpu=time.process_time()-c0)
    out.append(d); print(d,flush=True)
json.dump(out,open(sys.argv[1],'w'),indent=1)
