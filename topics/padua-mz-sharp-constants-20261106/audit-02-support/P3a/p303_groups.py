# Group norms (bulk, endpoints, all) and full-space lambda_min(Pi_N) at finite N
import numpy as np, json, time
from p303_cc import ccw, left_rows, card
res=[]
for N in [400,401,800,801,1600,1601,3200,3201]:
    w=ccw(N); th,mu=left_rows(N); ks=np.arange(N+1); C=card(N,th,ks)
    Y=(C*np.sqrt(mu)[:,None])/np.sqrt(w)[None,:]; G=Y.T@Y; G=G+G[::-1,::-1]
    L=np.log(N); M=int(np.floor(N/L))
    def nrm(idx): return float(np.sqrt(np.linalg.eigvalsh(G[np.ix_(idx,idx)])[-1]))
    bulk=np.arange(M+1,N-M); ends=np.array([0,N])
    full=nrm(ks)
    o=dict(N=N,L=L,M=M,lam_min_PiN=1/full**2,L2lam_PiN=L*L/full**2,
           bulk=nrm(bulk),bulk_claim=np.sqrt(np.pi*L/2),ends=nrm(ends),ends_claim=10*np.sqrt(L+5),
           sum_weights=float(w.sum()),minw=float(w.min()))
    res.append(o); print({k:(round(float(v),5)) for k,v in o.items()},flush=True)
json.dump(res,open('p303_groups.json','w'),indent=1)
