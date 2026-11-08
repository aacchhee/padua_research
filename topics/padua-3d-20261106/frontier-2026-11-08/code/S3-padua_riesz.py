import numpy as np, itertools
for n in [4,8,16,32,48]:
    P=np.array([(np.cos(j*np.pi/n),np.cos(k*np.pi/(n+1))) for j in range(n+1) for k in range(n+2) if (j-k)%2==0])
    K=[k for k in itertools.product(range(n+1),repeat=2) if sum(k)<=n]; N=len(K)
    th=np.arccos(np.clip(P,-1,1))
    V=np.array([[ (np.sqrt(2) if k[0] else 1)*np.cos(k[0]*t[0])*(np.sqrt(2) if k[1] else 1)*np.cos(k[1]*t[1]) for k in K] for t in th])
    Kjj=(V**2).sum(1); B=V/np.sqrt(Kjj)[:,None]; ev=np.linalg.eigvalsh(B@B.T)
    print(f"Padua n={n} N={N} |P|={len(P)} riesz=[{ev[0]:.4f},{ev[-1]:.4f}]")
