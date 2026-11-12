# Auditor check of the R-Leja transfer (MEASURED numerics only; not a proof).
import numpy as np, itertools, math, cmath, json, sys
from math import comb
def rleja35(K):
    r=[1.0,-1.0,0.0]
    j=2
    while len(r)<K:
        a=math.sqrt((r[j]+1)/2); r+= [a,-a]; j+=1
    return np.array(r[:K])
def lejaF(levels):
    F=[1+0j]
    for n in range(levels):
        rho=cmath.exp(1j*math.pi/2**n); F=F+[rho*z for z in F]
    return F
def proj_norep(E,K):
    out=[]
    for z in E:
        x=z.real
        if all(abs(x-y)>1e-12 for y in out): out.append(x)
        if len(out)==K: break
    return np.array(out)
K=257
r=rleja35(K); p=proj_norep(lejaF(10),K)
print("(3.5) equals no-repeat real projection of F for first",K,":",np.allclose(r,p,atol=1e-12))
print("distinct:",len(np.unique(np.round(r,13)))==K)
for n in range(1,9):
    S=sorted(r[:2**n+1]); L=sorted(np.cos(np.arange(2**n+1)*np.pi/2**n))
    assert np.allclose(S,L)
print("prefixes 2^n+1 are Gauss-Lobatto sets n<=8: True")
# 1D operator norms D_k = ||I_{k+1 pts} - I_{k pts}|| via Lagrange coefficients on fine mesh (lower estimates)
xs=np.cos(np.linspace(0,np.pi,200001))
def lag(nodes,x):
    # barycentric Lagrange basis values, shape (len(x),len(nodes))
    nodes=np.asarray(nodes); w=np.array([1/np.prod([nodes[j]-nodes[i] for i in range(len(nodes)) if i!=j]) for j in range(len(nodes))])
    diff=x[:,None]-nodes[None,:]
    exact=np.isclose(diff,0,atol=1e-15)
    with np.errstate(divide='ignore',invalid='ignore'):
        M=w[None,:]/diff; Lm=M/np.sum(M,axis=1,keepdims=True)
    rows=np.any(exact,axis=1); Lm[rows]=exact[rows].astype(float)
    return Lm
def Dk(k):
    if k==0: return 1.0
    A=lag(r[:k+1],xs); B=lag(r[:k],xs)
    C=A.copy(); C[:,:k]-=B
    return np.max(np.sum(np.abs(C),axis=1))
viol=[]; Ds=[]
for k in range(0,41):
    d=Dk(k); Ds.append(d)
    if k>=1:
        m=int(math.floor(math.log2(k))); bd=2**bin(k).count('1')*2**m
    else: bd=1
    if d>bd*(1+1e-9) or d>(k+1)**2*(1+1e-9): viol.append((k,d,bd))
print("D_k mesh lower estimates k<=40 vs Cor4.3 bound: violations",viol)
print("sample D_k:",[(k,round(Ds[k],4)) for k in (1,2,3,4,5,7,8,9,15,16,17,31,32,33,40)])
json.dump({"D":Ds},open(sys.argv[1],"w"))
