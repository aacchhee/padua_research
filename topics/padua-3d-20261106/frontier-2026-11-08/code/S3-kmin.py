import numpy as np, itertools
rng=np.random.default_rng(2)
for n in [2,5,10,20,30]:
    K=np.array([k for k in itertools.product(range(n+1),repeat=3) if sum(k)<=n]); N=len(K)
    th=np.vstack([np.pi*rng.uniform(0,1,(4000,3)), np.pi*np.array(list(itertools.product(np.linspace(0,1,13),repeat=3)))])
    # K(x,x)=sum_k prod_i c_{k_i} cos^2(k_i th_i), c=2 for k>0
    vals=np.zeros(len(th))
    for k in K:
        v=np.ones(len(th))
        for i in range(3):
            if k[i]>0: v*=2*np.cos(k[i]*th[:,i])**2
        vals+=v
    print(n,N,"min K/N=%.3f  max K/N=%.3f"%(vals.min()/N, vals.max()/N))
