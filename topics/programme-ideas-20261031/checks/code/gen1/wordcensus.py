import numpy as np, itertools
rng=np.random.default_rng(0)
M=30; x=rng.uniform(-1,1,M); y=rng.uniform(-1,1,M); w=rng.uniform(0.5,2,M); w=w/w.sum()
deg=8
idx=[(a,b) for s in range(deg+1) for a in range(s,-1,-1) for b in [s-a]]
V=np.array([x**a*y**b for a,b in idx]).T
W=np.sqrt(w)
Q,R=np.linalg.qr(W[:,None]*V)
Hx=Q.T@(x[:,None]*Q); Hy=Q.T@(y[:,None]*Q)
e=np.zeros(len(idx)); e[0]=1
def mom(word): 
    return np.sum(w*np.prod([x if c=='x' else y for c in word],axis=0)) if word else w.sum()
for k in range(1,5):
    Nk=(k+1)*(k+2)//2
    A=Hx[:Nk,:Nk]; B=Hy[:Nk,:Nk]; ek=e[:Nk]
    out={}
    for L in range(1,2*k+4):
        errs=[]
        for word in itertools.product('xy',repeat=L):
            v=ek.copy()
            for c in reversed(word):
                v=(A if c=='x' else B)@v
            errs.append(abs(ek@v-mom(word)))
        out[L]=max(errs)
    # anti-Gauss: section k+1 with coupling blocks scaled by sqrt2
    Nk1=(k+2)*(k+3)//2
    A2=Hx[:Nk1,:Nk1].copy(); B2=Hy[:Nk1,:Nk1].copy()
    A2[Nk:,:Nk]*=np.sqrt(2); A2[:Nk,Nk:]*=np.sqrt(2); B2[Nk:,:Nk]*=np.sqrt(2); B2[:Nk,Nk:]*=np.sqrt(2)
    ek1=e[:Nk1]
    flips=[];
    for a in range(2*k+3):
        b=2*k+2-a
        word='x'*a+'y'*b
        def val(A_,B_,ek_):
            v=ek_.copy()
            for c in reversed(word): v=(A_ if c=='x' else B_)@v
            return ek_@v
        eg=val(A,B,ek)-mom(word); ea=val(A2,B2,ek1)-mom(word)
        flips.append((a,b,eg,ea))
    print("k",k,"max err by word length:",{L:f"{v:.1e}" for L,v in out.items()})
    print("   deg",2*k+2,"gauss err / antigauss err:",[(a,b,f"{eg:.2e}",f"{ea:.2e}") for a,b,eg,ea in flips])
