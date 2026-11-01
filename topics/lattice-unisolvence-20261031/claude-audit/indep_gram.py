"""Claude audit-01: independent numerical check of PD-T?lattice-c1-codex-04 (Gram reduction)."""
import numpy as np, json
def setup(n,p):
    def axis(M):
        th=np.pi*np.arange(M+1)/M; nu=np.full(M+1,1/M); nu[[0,M]]=1/(2*M); return th,nu
    tx,nx=axis(n); ty,ny=axis(n+1)
    modes=[(a,b) for a in range(n+1) for b in range(n+1-a)]
    def psi(a,th,M): h=1.0 if a in (0,M) else 0.5; return np.cos(a*th)/np.sqrt(h)
    sel=[(i,j) for i in range(n+1) for j in range(n+2) if (i+j-p)%4 in (0,1)]
    V=np.array([[psi(a,tx[i],n)*psi(b,ty[j],n+1) for a,b in modes] for i,j in sel])
    W=np.array([nx[i]*ny[j] for i,j in sel])
    return modes,V,W,sel
def check(n,p):
    modes,V,W,sel=setup(n,p); N=len(modes); assert len(sel)==N
    G=V.T@(W[:,None]*V)
    ev=[k for k,(a,b) in enumerate(modes) if (a+b)%2==0]; od=[k for k,(a,b) in enumerate(modes) if (a+b)%2]
    same=max(np.abs(G[np.ix_(ev,ev)]-0.5*np.eye(len(ev))).max(), np.abs(G[np.ix_(od,od)]-0.5*np.eye(len(od))).max())
    A=2*G[np.ix_(ev,od)]
    # explicit formula
    def S(M,r): return M if abs(r-1)<1e-14 else (1+r)*(1-r**M)/(2*(1-r))
    def C(M,t): return (S(M,1j*np.exp(1j*np.pi*t/M))+S(M,1j*np.exp(-1j*np.pi*t/M)))/(2*M)
    def h(M,a): return 1.0 if a in (0,M) else 0.5
    def Z(M,a,c): return (C(M,a-c)+C(M,a+c))/(2*np.sqrt(h(M,a)*h(M,c)))
    Af=np.array([[((1-1j)*(1j)**(-p)*Z(n,modes[e][0],modes[o][0])*Z(n+1,modes[e][1],modes[o][1])).real for o in od] for e in ev])
    sig=np.linalg.svd(A,compute_uv=False)[0] if len(od) else 0.0
    sd,ld=np.linalg.slogdet(V); lhs=2*ld+np.log(W).sum()
    s2,l2=np.linalg.slogdet(np.eye(len(od))-A.T@A) if len(od) else (1,0.0)
    rhs=-N*np.log(2)+l2
    # Lebesgue bound check on random points
    rng=np.random.default_rng(n*7+p); z=rng.uniform(-1,1,(4000,2))
    def phi(z):
        tx=np.arccos(z[:,0]); ty=np.arccos(z[:,1])
        return np.array([np.cos(a*tx)/np.sqrt(1.0 if a in (0,n) else .5)*np.cos(b*ty)/np.sqrt(1.0 if b in (0,n+1) else .5) for a,b in modes]).T
    Lv=np.abs(np.linalg.solve(V.T,phi(z).T)).sum(0).max()
    bound=2*np.sqrt(N)/np.sqrt(1-sig)
    return dict(n=n,p=p,same_parity_offblock=float(same),formula_err=float(np.abs(A-Af).max()),sigma=float(sig),
                gap=float(1-sig),detid_err=float(abs(lhs-rhs)),lebesgue_sample=float(Lv),bound=float(bound),bound_ok=bool(Lv<=bound))
rows=[]
for n in range(1,49):
    rows.append(check(n,0 if n%2 else 1))
for r in rows[:6]+rows[-6:]: print(r)
print("max offblock",max(r['same_parity_offblock'] for r in rows),"max formula err",max(r['formula_err'] for r in rows),
      "max detid err",max(r['detid_err'] for r in rows),"min gap",min(r['gap'] for r in rows),"all bound ok",all(r['bound_ok'] for r in rows))
# negative check: unshifted phase0 at n=2,6,10 should be singular
for n in (2,6,10):
    modes,V,W,sel=setup(n,0); s=np.linalg.svd(V,compute_uv=False); print("phase0 n",n,"numerical nullity",int((s<1e-10*s[0]).sum()),"bound (n+2)/4 =",(n+2)//4)
json.dump(rows,open('topics/lattice-unisolvence-20261031/claude-audit/outputs/indep_gram.json','w'),indent=1)
