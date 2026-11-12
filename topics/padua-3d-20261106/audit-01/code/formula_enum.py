"""Auditor: exhaustive formula enumeration over the classified parameter space,
cap = 2*binom(n+3,3) so that EVERY reflection-invariant coset with |X|=binom(n+3,3)
is included (each axis has <= |X| levels). Check screens and lower bounds."""
import numpy as np, math, itertools as it, sys
def e(q): return q//2+1
def o(q): return (q+1)//2
def run(n, cap):
    N=math.comb(n+3,3)
    m=np.arange(1,cap+1,dtype=np.int64)
    lev0=m//2+1                                  # inactive eps=0
    lev1=np.where(m%2==0,m//2,(m+1)//2)          # inactive eps=1
    q=m//2; E=e(q); O=o(q); even=(m%2==0)
    res={}
    codes={"0":[],"pair12":[0,1],"pair13":[0,2],"pair23":[1,2],"triple":[0,1,2],"plane":[0,1,2]}
    for name,act in codes.items():
        inact=[j for j in range(3) if j not in act]
        # parity classes on active coords
        if name=="0": classes=[[()]]
        elif name.startswith("pair"): classes=[[(0,0),(1,1)],[(0,1),(1,0)]]
        elif name=="triple": classes=[[p for p in it.product((0,1),repeat=3) if sum(p)%2==s] for s in (0,1)]
        else: classes=[[p,tuple(1-x for x in p)] for p in [(0,0,0),(0,0,1),(0,1,0),(1,0,0)]]
        bad=0; tgt=0; minpass=None
        for C in classes:
            for eps in it.product((0,1),repeat=len(inact)):
                # build axis arrays shape (cap,cap,cap) lazily via broadcasting
                shp=[None]*3
                def ax(j,arr):
                    s=[1,1,1]; s[j]=cap; return arr.reshape(s)
                cnt=0
                for p in C:
                    term=1
                    for jj,j in enumerate(act):
                        term=term*ax(j,np.where(p[jj],O,E))
                    cnt=cnt+term
                levels=[None]*3
                for j in act: levels[j]=ax(j,q+1)
                for jj,j in enumerate(inact):
                    L=ax(j,lev1 if eps[jj] else lev0)
                    cnt=cnt*L; levels[j]=L
                valid=np.ones((cap,cap,cap),bool)
                for j in act: valid&=ax(j,even)
                cnt=np.broadcast_to(cnt,(cap,cap,cap))
                short=np.zeros((cap,cap,cap),bool)
                for j in range(3): short|=np.broadcast_to(levels[j]<=n,(cap,cap,cap))
                alias=np.zeros((cap,cap,cap),bool)
                if name=="plane":
                    low=sum(np.broadcast_to(ax(j,q<=n).astype(np.int8),(cap,cap,cap)) for j in range(3))
                    alias=low>=2
                hit=valid&(cnt==N)
                tgt+=int(hit.sum())
                bad+=int((hit&~short&~alias).sum())
                ps=valid&~short&~alias
                if ps.any():
                    mn=int(cnt[ps].min()); minpass=mn if minpass is None else min(minpass,mn)
        res[name]=(tgt,bad,minpass)
    return N,res
for n in [int(x) for x in sys.argv[1].split(",")]:
    N=math.comb(n+3,3)
    cap=int(sys.argv[2]) if len(sys.argv)>2 else 2*N
    N,res=run(n,cap)
    ee,oo=e(n),o(n); delta=1 if n%2==0 else 0
    Mn=(n+1)*(n+2)**2//4 if n%2==0 else (n+1)**2*(n+3)//4
    claims={"0":(n+1)**3,"pair":n*(n+1)*(n+2)//2,"pair_exact":2*ee*oo*(n+1),"triple":((n+1)**3-delta)//2,"plane":Mn}
    print("n",n,"N",N,"cap",cap,res,"claimed lower bounds",claims)
