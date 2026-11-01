import numpy as np
def mats(N):
    k=np.arange(N+1); th=k*np.pi/N
    cc=np.ones(N+1); cc[0]=cc[-1]=2
    A=(2/N)*np.cos(np.outer(k,th))/np.outer(cc,cc)
    h=np.zeros(2*N+1); ev=np.arange(0,2*N+1,2); h[ev]=2/(1-ev.astype(float)**2)
    Gam=0.5*(h[np.add.outer(k,k)]+h[np.abs(np.subtract.outer(k,k))])
    Mc=A.T@Gam@A; w=h[:N+1]@A; s=1/np.sqrt(w)
    return k, s[:,None]*(Mc-np.diag(w))*s[None,:]
for N in [80,320,1280,2560]:
    k,Mt=mats(N); m=np.maximum(np.minimum(k,N-k),1).astype(float)
    dg=np.abs(np.diag(Mt))*m
    out=[]
    for name,v in [('m^-1/2',m**-0.5),('(-1)^k m^-1/2',(-1.0)**k*m**-0.5),
                   ('one-end (-1)^k m^-1/2',np.where(k<N/2,(-1.0)**k*m**-0.5,0))]:
        out.append(f"{name}: RQ={v@Mt@v/(v@v):.3f}")
    lam=np.linalg.eigvalsh(Mt).max()
    sgn=np.sign(Mt[0,1:6]); 
    print(f"N={N} lmax(Mt)={lam:.3f} max|diag|*m={dg.max():.3f} at k={dg.argmax()} ;", '; '.join(out), '; sign row0:',sgn, f"; lmax/log^2N={lam/np.log(N)**2:.4f}")
