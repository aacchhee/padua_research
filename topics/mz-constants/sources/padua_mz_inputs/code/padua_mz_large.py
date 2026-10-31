import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
"""F7 2D: weak MZ constant of the interpolatory Padua rule (Lebesgue measure on [-1,1]^2, degree m)
for the orthonormal Legendre-product basis of P_n, n = m-1 (and m-2), larger m than pad_split.py.
Uses three-term recurrences (no chebval loops)."""
import sys, time, numpy as np
sys.path.insert(0, ".")
from mz_padua_cc_check import padua, total_degree
def cheb_all(t, n):
    T = np.zeros((len(t), n+1)); T[:,0]=1
    if n>=1: T[:,1]=t
    for k in range(1,n): T[:,k+1]=2*t*T[:,k]-T[:,k-1]
    T[:,1:]*=np.sqrt(2); return T
def leg_all(t, n):
    P=np.zeros((len(t),n+1)); P[:,0]=1/np.sqrt(2)
    if n>=1: P[:,1]=np.sqrt(1.5)*t
    for k in range(1,n):
        a=np.sqrt((2*k+1)*(2*k+3))/(k+1); b=k/(k+1)*np.sqrt((2*k+3)/(2*k-1)); P[:,k+1]=a*t*P[:,k]-b*P[:,k-1]
    return P
def run(m, ns):
    P,_=padua(m); idx=total_degree(m); x,y=P[:,0],P[:,1]
    Tx,Ty=cheb_all(x,m),cheb_all(y,m)
    V=np.column_stack([Tx[:,a]*Ty[:,b] for a,b in idx])
    mom1=lambda k: 0.0 if k%2 else 2/(1-k*k)
    mom=np.array([mom1(a)*mom1(b)*(1 if a==0 else np.sqrt(2))*(1 if b==0 else np.sqrt(2)) for a,b in idx])
    w=np.linalg.solve(V.T,mom)
    Lx,Ly=leg_all(x,m),leg_all(y,m); out=[]
    for n in ns:
        B=np.column_stack([Lx[:,a]*Ly[:,b] for a,b in total_degree(n)])
        ev=np.linalg.eigvalsh(B.T@(w[:,None]*B)); out.append((n,ev[0],ev[-1],max(1-ev[0],ev[-1]-1)))
    return out,(w<0).sum(),w.min()
for m in [int(s) for s in sys.argv[1:]]:
    t=time.time(); out,neg,wmin=run(m,(m-2,m-1))
    print(f"m={m} (#neg w={neg}, min w={wmin:.2e}): "+"  ".join(f"n={n}: lmin={a:.4f} lmax={b:.4f} eta={e:.4f}" for n,a,b,e in out)+f" [{time.time()-t:.0f}s]",flush=True)
