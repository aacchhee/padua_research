# A6: independent (own code) sampled Lebesgue values for M/A/L stacks and Leja lower set at n=5..7,
# on the 21^3 Lobatto mesh and a finer 41^3 Lobatto mesh (MEASURED only).
import numpy as np, itertools as it, math
from numpy.polynomial.chebyshev import chebvander
def lob(L): return np.cos(np.pi*np.arange(L)/(L-1))
def expo(n): return [(a,b,c) for d in range(n+1) for a in range(d+1) for b in range(d-a+1) for c in [d-a-b]]
def basis(P,n):
    T=[chebvander(P[:,k],n) for k in range(3)]
    return np.stack([T[0][:,a]*T[1][:,b]*T[2][:,c] for a,b,c in expo(n)],axis=1)
def padua(m):
    if m==0: return np.array([[1.,1.]])
    return np.array([[np.cos(i*np.pi/m),np.cos(j*np.pi/(m+1))] for i in range(m+1) for j in range(m+2) if (i+j)%2==0])
def order(n,f):
    if f=='M': return list(range(n+1))
    if f=='A':
        o=[]
        for j in range((n+2)//2):
            o.append(j)
            if n-j!=j: o.append(n-j)
        return o
    h=np.cos(np.pi*np.arange(n+1)/n); o=[0]; rem=list(range(1,n+1))
    while rem:
        v={j:np.prod([abs(h[j]-h[i]) for i in o]) for j in rem}; b=max(v.values())
        w=min(j for j in rem if v[j]>=b*(1-1e-12)); o.append(w); rem.remove(w)
    return o
def stack(n,o):
    h=np.cos(np.pi*np.arange(n+1)/n)
    return np.vstack([np.column_stack((padua(n-k),np.full(len(padua(n-k)),h[o[k]]))) for k in range(n+1)])
def leja_lower(n):
    v=lob(n+1); o=[0]; rem=list(range(1,n+1))
    while rem:
        b=max(rem,key=lambda i:(np.prod([abs(v[i]-v[j]) for j in o]),-i)); o.append(b); rem.remove(b)
    ax=v[o]; return np.array([[ax[a],ax[b],ax[c]] for a,b,c in expo(n)])
def leb(P,n,mesh,chunk=20000):
    V=basis(P,n); Vinv=np.linalg.inv(V); best=0
    for s in range(0,len(mesh),chunk):
        L=np.abs(basis(mesh[s:s+chunk],n)@Vinv).sum(axis=1); best=max(best,L.max())
    return best
for Lm in [21,41]:
    mesh=np.array(list(it.product(lob(Lm),repeat=3)))
    for n in [5,6,7]:
        out={f:leb(stack(n,order(n,f)),n,mesh) for f in 'MAL'}
        out['Leja']=leb(leja_lower(n),n,mesh)
        print('mesh %d^3 n=%d '%(Lm,n)+'  '.join('%s=%.4f'%(k,v) for k,v in out.items()), 'orders L=',order(n,'L'))
