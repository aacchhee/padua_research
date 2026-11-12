# Supplementary MEASURED census: cyclic H=<g/q> in T^3, unshifted; min folded count among those exact through 2n-1.
import numpy as np, itertools as it, math, sys
qmax=int(sys.argv[1])
for n in (1,2,3):
    D=2*n-1; K=np.array([k for k in it.product(range(-D,D+1),repeat=3) if 0<sum(map(abs,k))<=D])
    best={}
    for q in range(2,qmax+1):
        G=np.array(list(it.product(range(q),repeat=3)))
        ok=np.all((G@K.T)%q!=0,axis=1)  # no dual vector of l1<=D
        for g in G[ok]:
            m=np.arange(q)[:,None]*g[None,:]%q
            X={tuple(r) for r in np.minimum(m,(q-m)%q)}
            c=len(X)
            if c<best.get('min',10**9): best={'min':c,'q':q,'g':tuple(int(x) for x in g),'H':len({tuple(r) for r in m})}
    N=math.comb(n+3,3)
    print('n',n,'D',D,'q<=%d'%qmax,'min folded nodes of exact unshifted cyclic Haar rule',best,'N',N, 'bound n^3/(6*18/19)=%.2f'%(19*n**3/108))
