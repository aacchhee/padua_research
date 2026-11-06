import sys; sys.path.insert(0,'.'); import numpy as np, io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    from fixedJ_check import model
from scipy.linalg import eigh
for N in [10**4,10**6,4.4e6,10**7,10**8,4096**2*16,1e12,1e18]:
    T=max(1,int(np.floor(N**(1/12)+1e-9))); best=1.0; which=None
    for J in range(1,T+1):
        if N<np.ceil(2*np.pi*J): continue
        C,D=model(J); lamJ=eigh(D,C,eigvals_only=True)[-1]; mJ=np.linalg.eigvalsh(C)[0]
        e=1000*J*(1+(np.pi*J)**4)/N**2; d=20*(1+8*(np.pi*J)**3)/N+4*J/(N*N-1)
        v=d+5/3*e; x=mJ-e; val=max(1,lamJ-v/max(x,2*v))
        if val>best: best,which=val,(J,lamJ,v/max(x,2*v))
    print(f"N={N:.3g} T_N={T} L_N={best:.6f} via {which}")
