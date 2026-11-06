import numpy as np, json, math, scipy.sparse.linalg as spl
from cc_common import cell_grid
out={}
def opnorm2(Amat):
    # Amat rows = sqrt(quad weight) * operator; largest singular value^2
    G=Amat.T@Amat
    return np.linalg.eigvalsh(G)[-1]
for n in [16,64,256,1024]:
    k=np.arange(1,n+1).astype(float)
    T=6*n
    t,wt=cell_grid(T,q=10)
    # P3-01 operator: (Eg)(t)=sin(pi t) sum g_k B_k(t); input norm sum|g|^2/k -> g=sqrt(k) h
    rows=[]
    G=np.zeros((n,n))
    for s in range(0,len(t),20000):
        tt=t[s:s+20000]; ww=wt[s:s+20000]
        B=tt[:,None]**2/(k[None,:]*(tt[:,None]**2-k[None,:]**2)) - (k[None,:]<tt[:,None])/k[None,:]
        A=(np.sin(np.pi*tt)[:,None]*B)*np.sqrt(k)[None,:]*np.sqrt(ww/tt)[:,None]
        G+=A.T@A
    ev,V=np.linalg.eigh(G)
    out[f'P301_n{n}']=float(np.sqrt(ev[-1]))
    # pieces: pole only (k in J_j) etc. skip; test alternating and constant inputs
    for name,g in [('alt',(-1)**k),('const',np.ones(n)),('alt_sqrtk',(-1)**k*np.sqrt(k))]:
        h=g/np.sqrt(k); out[f'P301_n{n}_{name}']=float(np.sqrt(h@G@h/(h@h)))
    # P3-02: T=n, J=n ; operator g -> sin(pi t) S(t) on [0,T] dt/t
    T2=n; t2,w2=cell_grid(T2,q=10)
    S=(k[None,:]<t2[:,None])/k[None,:]
    A=(np.sin(np.pi*t2)[:,None]*S)*np.sqrt(k)[None,:]*np.sqrt(w2/t2)[:,None]
    nm2=np.linalg.eigvalsh(A.T@A)[-1]
    H=np.sum(1/k); Aj=2*H/math.pi+1
    out[f'P302_n{n}']=dict(norm2=float(nm2),bound=Aj**2/2+1.5,lead=2/math.pi**2*math.log(n)**2, lead_H=2/math.pi**2*H**2)
    print(n,out[f'P301_n{n}'],out[f'P302_n{n}'],flush=True)
json.dump(out,open('t2_lemmas.json','w'),indent=1)
