# Discrimination control: mis-scaled primitive (factor 1.1) or indicator k<=t-1 should give remainder growing ~ L
import numpy as np, json
from p303_cc import ccw, left_rows, card
z=np.linspace(-np.pi,1.5*np.pi,200001); z=z[np.abs(z)>1e-9]; e=1/np.tan(z/2)-2/z
out=dict(max_abs_e_on_range=float(np.max(np.abs(e))),claim_lt=2.0,rows=[])
for N in [512,2048,8192]:
    w=ccw(N); th,mu=left_rows(N); t=N*th/np.pi; L=np.log(N); M=int(N/L)
    left=np.arange(1,M+1); ks=np.concatenate([left,N-left]); C=card(N,th,ks)
    base=2*np.sin(np.pi*t)/(np.pi*t)
    def rem(fac,shift):
        P=np.zeros_like(C); P[:,:M]=fac*base[:,None]*((-1.0)**left)[None,:]*(left[None,:]+shift<t[:,None])
        Y=((C-P)*np.sqrt(mu)[:,None])/np.sqrt(w[ks])[None,:]; G=Y.T@Y
        perm=np.concatenate([np.arange(M,2*M),np.arange(M)]); G=G+G[np.ix_(perm,perm)]
        return float(np.sqrt(np.linalg.eigvalsh(G)[-1]))
    r=dict(N=N,L=L,exact=rem(1,0),scaled1p1=rem(1.1,0),shifted_indicator=rem(1,1))
    out['rows'].append(r); print(r,flush=True)
json.dump(out,open('p303_discrim.json','w'),indent=1)
print(out['max_abs_e_on_range'])
