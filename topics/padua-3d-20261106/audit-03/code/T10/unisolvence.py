"""Auditor: independent exact unisolvence check of the frozen restricted-QR subsets.
Selection reproduces the producer's definition (pivoted QR on unscaled lexicographic
Chebyshev evaluation of the folded parity-aniso nodes); certification is own code:
monomial basis, Python big-int Gaussian elimination over F_p for primes p = 1 mod q
other than the producer's, with a randomly chosen primitive q-th root."""
import sys, os, json, math, hashlib, random, itertools as it
import numpy as np, scipy.linalg as la
from sympy import isprime, factorint
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from minfold_search import dual_numerators
random.seed(20261106)
def exps(n): return [(a,b,c) for a in range(n+1) for b in range(n-a+1) for c in range(n-a-b+1)]
def folded_parity(n):
    v=(n,n+1,0,n+1,n+1,2*(n+1)); q,H=dual_numerators(v)
    F=np.unique(np.minimum(H,q-H),axis=0); return q,[tuple(map(int,r)) for r in F]
def select(n,q,keys):
    P=np.cos(2*np.pi*np.array(keys)/q)
    T=[np.polynomial.chebyshev.chebvander(P[:,j],n) for j in range(3)]
    V=np.array([T[0][:,a]*T[1][:,b]*T[2][:,c] for a,b,c in exps(n)]).T
    perm=la.qr(V.T,pivoting=True,mode='economic',check_finite=False)[2]
    return [keys[int(i)] for i in perm[:math.comb(n+3,3)]]
def primitive_qth_root(q,p):
    while True:
        g=random.randrange(2,p-1); z=pow(g,(p-1)//q,p)
        if pow(z,q,p)==1 and all(pow(z,q//r,p)!=1 for r in factorint(q)): return z
def rank_det_mod(rows,p):
    M=[r[:] for r in rows]; n=len(M); m=len(M[0]); r=0; det=1
    for j in range(m):
        piv=next((i for i in range(r,n) if M[i][j]%p),None)
        if piv is None: det=0; continue
        if piv!=r: M[r],M[piv]=M[piv],M[r]; det=-det
        det=det*M[r][j]%p; inv=pow(M[r][j],p-2,p)
        for i in range(r+1,n):
            if M[i][j]%p:
                f=M[i][j]*inv%p; M[i]=[(x-f*y)%p for x,y in zip(M[i],M[r])]
        r+=1
    return r,det%p
def certify(sel,q,n,p,z):
    inv2=pow(2,p-2,p); E=exps(n)
    rows=[]
    for k in sel:
        x=[(pow(z,h,p)+pow(z,(q-h)%q,p))*inv2%p for h in k]
        rows.append([pow(x[0],a,p)*pow(x[1],b,p)%p*pow(x[2],c,p)%p for a,b,c in E])
    return rank_det_mod(rows,p)
if __name__=='__main__':
    receipt=json.load(open(sys.argv[1])); expected={r[0]:r for r in receipt['rows']}
    out=[]
    for n in map(int,sys.argv[3:]):
        q,keys=folded_parity(n); sel=select(n,q,keys); N=math.comb(n+3,3)
        h=hashlib.sha256(json.dumps({'denominator':q,'selected_folded_keys':[list(k) for k in sel]},separators=(',',':')).encode()).hexdigest()
        ps=[];k=1
        while len(ps)<3:
            if isprime(q*k+1) and q*k+1!=expected[n][2]: ps.append(q*k+1)
            k+=1
        res=[]
        for p in ps[:2]:
            z=primitive_qth_root(q,p); rk,det=certify(sel,q,n,p,z); res.append([p,z,rk,det])
        rec={'n':n,'q':q,'folded':len(keys),'N':N,'hash_matches_receipt':h==expected[n][7],'witnesses':res,
             'full_rank_certified':any(r[2]==N and r[3]!=0 for r in res)}
        print(rec,flush=True); out.append(rec)
    json.dump(out,open(sys.argv[2],'w'))
