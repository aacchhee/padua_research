import numpy as np, itertools as it
rng=np.random.default_rng(1); worst=0
for n in (1,2,3,5):
    E=[(a,b,c) for a in range(n+1) for b in range(n-a+1) for c in range(n-a-b+1)]
    K=[k for k in it.product(range(-n,n+1),repeat=3) if sum(map(abs,k))<=n]
    for _ in range(20):
        th,ps=rng.uniform(-np.pi,np.pi,3),rng.uniform(-np.pi,np.pi,3)
        lhs=sum(2**sum(1 for x in al if x)*np.prod([np.cos(a*t)*np.cos(a*p) for a,t,p in zip(al,th,ps)]) for al in E)
        D=lambda t: sum(np.cos(np.dot(k,t)) for k in K)
        rhs=sum(D(th+np.array(e)*ps) for e in it.product([1,-1],repeat=3))/8
        worst=max(worst,abs(lhs-rhs))
print('max |K_n - (1/8) sum D_n(theta+eps psi)|',worst)
