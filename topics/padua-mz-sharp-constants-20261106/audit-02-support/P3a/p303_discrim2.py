import numpy as np, json
from p303_cc import ccw, left_rows, card
out=[]
for N in [512,2048,8192]:
    w=ccw(N); th,mu=left_rows(N); t=N*th/np.pi; L=np.log(N); M=int(N/L)
    left=np.arange(1,M+1); ks=np.concatenate([left,N-left]); C=card(N,th,ks)
    base=2*np.sin(np.pi*t)/(np.pi*t)
    perm=np.concatenate([np.arange(M,2*M),np.arange(M)])
    r=dict(N=N,L=L)
    for fac in [0,0.5,1,1.5,2]:
        P=np.zeros_like(C); P[:,:M]=fac*base[:,None]*((-1.0)**left)[None,:]*(left[None,:]<t[:,None])
        Y=((C-P)*np.sqrt(mu)[:,None])/np.sqrt(w[ks])[None,:]; G=Y.T@Y; G=G+G[np.ix_(perm,perm)]
        ev,V=np.linalg.eigh(G); r['fac%.1f'%fac]=float(np.sqrt(ev[-1]))
        if fac==1:
            v=V[:,-1]**2; r['top_vec_mass_k<=3']=float(v[:3].sum()+v[M:M+3].sum()); r['second_sv']=float(np.sqrt(ev[-2]))
            # remainder norm excluding k=1 column (both edges)
            keep=[i for i in range(2*M) if i not in (0,M)]
            r['excl_k1']=float(np.sqrt(np.linalg.eigvalsh(G[np.ix_(keep,keep)])[-1]))
    out.append(r); print(r,flush=True)
json.dump(out,open('p303_discrim2.json','w'),indent=1)
