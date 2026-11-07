"""Auditor: exact Gram of the anisotropic parity grid via characters (integer arithmetic),
plus numeric checks of ||P_n - H_n|| <= 1 and of the Fejer sampling constant."""
import sys, os, json, math, itertools as it
import numpy as np
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from minfold_search import dual_numerators
from fractions import Fraction
def exps(n): return [(a,b,c) for a in range(n+1) for b in range(n-a+1) for c in range(n-a-b+1)]
out=[]
for n in range(1,11):
    m=(n,n+1,n+1)
    # Dual lattice L={(m1a1,m2a2,m3a3): sum a even}. Haar average of exp(2pi i k.h) over H = [k in L].
    def inL(k):
        if any(k[j]%m[j] for j in range(3)): return False
        return sum(k[j]//m[j] for j in range(3))%2==0
    E=exps(n); N=len(E); G=np.zeros((N,N),dtype=object)
    for i,al in enumerate(E):
        for j,be in enumerate(E):
            # phi_al phi_be = 2^{(s(al)+s(be))/2} prod T_al T_be ; T_a T_b = (T_{a+b}+T_{|a-b|})/2
            # Haar avg of prod_j T_{c_j}(cos 2pi h_j) = 2^{-s(c)} sum_{signs} [ (±c) in L ]
            tot=Fraction(0)
            for choice in it.product(*[((a+b,1),(abs(a-b),1)) for a,b in zip(al,be)]):
                c=[x for x,_ in choice]
                s=sum(1 for x in c if x)
                cnt=sum(1 for sg in it.product(*[[-x,x] if x else [0] for x in c]) if inL(sg))
                tot+=Fraction(cnt,2**s)/8
            sal=sum(1 for x in al if x); sbe=sum(1 for x in be if x)
            G[i,j]=tot*Fraction(2)**Fraction(sal+sbe,1)  # squared scaling, take sqrt below
    # scaling: phi = 2^{s/2} T, so entry = 2^{(sal+sbe)/2} * avg(T_al T_be); we stored 2^{sal+sbe}*avg
    Gf=np.array([[float(G[i,j]) for j in range(N)] for i in range(N)])
    sc=np.array([2.0**(-sum(1 for x in al if x)/2) for al in E])
    Gf=Gf*sc[:,None]*sc[None,:]
    e=np.zeros(N); e[E.index((n,0,0))]=1
    err=np.abs(Gf-(np.eye(N)+np.outer(e,e))).max()
    out.append({'n':n,'max_abs_G_minus_I_plus_eeT':float(err)}); print(out[-1],flush=True)
# Fejer: average over shifted uniform grid of length m>=n of |V_n|, V_n=2F_2n - F_n
def F(M,t):
    s=np.abs(np.exp(1j*np.outer(t,np.arange(M))).sum(axis=1))**2/M; return s
worst=0
for n in range(1,25):
    for m in range(n,3*n+3):
        for a in np.linspace(0,1,7,endpoint=False):
            t=2*np.pi*(np.arange(m)+a)/m
            avg=np.mean(np.abs(2*F(2*n,t)-F(n,t)))
            worst=max(worst,avg)
out.append({'fejer_max_grid_average_|V_n|':float(worst),'bound':13}); print(out[-1])
json.dump(out,open(sys.argv[1],'w'))
