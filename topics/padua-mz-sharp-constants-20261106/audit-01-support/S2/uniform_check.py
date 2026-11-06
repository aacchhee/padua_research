import numpy as np
from scipy.linalg import eigh
worst=dict(ident=0,Hmin=0,betaM_K=1e9,ratio=0)
for N in range(2,121):
    i=np.arange(N); S=i[:,None]+i[None,:]; D=np.abs(i[:,None]-i[None,:])
    mu=lambda k: np.where(k%2==0,2/(1-k.astype(float)**2),0.0)
    M=0.5*(mu(D)+mu(S)); Qs=np.where(S<=N,mu(S),mu(2*N-S)); R=0.5*(mu(D)+Qs)
    r=2*N-S; ev=(S%2==0)
    H=np.where(ev,1/(r**2-1.0),0)
    K=np.where(S<=N,H,np.where(ev,1/(S**2-1.0),0))
    worst['ident']=max(worst['ident'],np.abs(R-(M-H+K)).max())
    worst['Hmin']=min(worst['Hmin'],np.linalg.eigvalsh(H)[0])
    L=N if N%2==0 else N+1; beta=N*np.ceil(N/2)/(L*L-1)
    worst['betaM_K']=min(worst['betaM_K'],np.linalg.eigvalsh(beta*M-K)[0])
    lam=eigh(K,M,eigvals_only=True)[-1]; worst['ratio']=max(worst['ratio'],lam/beta)
    if N in (2,3,10,11,100,101): print(N,"lam_max(R,M)=",eigh(R,M,eigvals_only=True)[-1],"lam_max(K,M)=",lam,"beta=",beta)
print(worst)
