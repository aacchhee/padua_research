import numpy as np, sys, time
from scipy.optimize import least_squares
sys.path.insert(0,'.')
from gen4_tests14 import sections
t=time.time()
def solve_ext(kind, n, trials=12, seed=0):
    A1,A2,N = sections(kind,n-1)   # sections on Pi_{n-1}
    m = n//2                        # Möller excess
    r = N+m
    rng=np.random.default_rng(seed)
    def unpack(p):
        B1=p[:N*m].reshape(N,m); B2=p[N*m:2*N*m].reshape(N,m); q=p[2*N*m:]
        D1=np.zeros((m,m)); D2=np.zeros((m,m)); iu=np.triu_indices(m)
        D1[iu]=q[:len(iu[0])]; D1=D1+D1.T-np.diag(np.diag(D1)); D2[iu]=q[len(iu[0]):]; D2=D2+D2.T-np.diag(np.diag(D2))
        Z1=np.block([[A1,B1],[B1.T,D1]]); Z2=np.block([[A2,B2],[B2.T,D2]]); return Z1,Z2
    def res(p):
        Z1,Z2=unpack(p); C=Z1@Z2-Z2@Z1; return C[np.triu_indices(r,1)]
    sols=[]
    npar=2*N*m+m*(m+1)
    for tr in range(trials):
        p0=rng.standard_normal(npar)*0.5
        s=least_squares(res,p0,method='trf',xtol=1e-15,ftol=1e-15,gtol=1e-15,max_nfev=3000)
        if np.linalg.norm(s.fun)<1e-10:
            Z1,Z2=unpack(s.x)
            # joint eigen: eig of Z1 (symmetric) ; nodes
            lam,U=np.linalg.eigh(Z1); mu=np.einsum('ij,ij->j',U,Z2@U); rs=np.linalg.norm(Z2@U-U*mu,axis=0).max()
            wts=U[0,:]**2   # weights via first component (phi_0 = 1 normalised)
            # Jacobian rank at solution -> local dimension of solution set
            J=s.jac; rk=np.linalg.matrix_rank(J,tol=1e-8); dimsol=npar-rk
            sols.append((np.sort(lam),np.sort(mu),wts,rs,dimsol))
    return N,m,r,npar,len(res(np.zeros(npar))),sols
for kind in ('cheb','leg'):
    for n in (2,3,4,5,6):
        N,m,r,npar,neq,sols=solve_ext(kind,n,trials=10)
        gauge=m*(m-1)//2  # O(m) gauge dimension
        print(kind,'n',n,'N',N,'m',m,'r',r,'unknowns',npar,'eqs',neq,'solutions found',len(sols),'of 10',
              '| local dim of sol set (minus O(m) gauge):',sorted(set(d-gauge for *_,d in sols)) if sols else None,
              '| min weight %.2e'%(min(s[2].min() for s in sols) if sols else float('nan')),'| nodes in square?', all((np.abs(s[0]).max()<=1+1e-9) and (np.abs(s[1]).max()<=1+1e-9) for s in sols) if sols else None, 'time %.0f'%(time.time()-t))
        if sols and n<=4:
            s=sols[0]; print('    sample node x-coords',np.round(s[0],4)); print('    weights',np.round(np.sort(s[2]),4))
