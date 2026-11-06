import numpy as np, json
from cc_common import *
res={}
worst=dict(floor=np.inf, sinfloor=np.inf, dev=0)
for N in list(range(2,400))+[511,512,1000,1001,2047,2048,4999,5000]:
    w=cc_weights(N); k=np.arange(N+1); th=k*np.pi/N; d=np.minimum(k,N-k)
    worst['floor']=min(worst['floor'], np.min(w*N**2/(1+d)))
    if N>2:
        i=k[1:-1]
        worst['sinfloor']=min(worst['sinfloor'], np.min(w[i]*N/np.sin(th[i])))
        worst['dev']=max(worst['dev'], np.max(np.abs(w[i]-np.pi/N*np.sin(th[i])))*N**2)
    assert abs(w.sum()-2)<1e-12
print(worst)
# lambda check vs evidence N=100,101
for N in [100,101]:
    print(N, lam_min(N)[0], lam_min(N,sub=True)[0])
json.dump({k:float(v) for k,v in worst.items()},open('t1_weights.json','w'))
