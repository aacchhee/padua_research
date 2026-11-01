"""HL SIMAX window variants (exact listing window / block window / full orthogonalization) and a long-double run.
MEASURED only.  Usage: python3 -I l1_simax_variants.py"""
import sys; import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, l1_recurrence as L
def simax(x,y,w,nmax,wmode,dtype=complex):
    idx,pos,parent,op,start=L.tables(nmax); N=len(idx)
    z=(np.asarray(x)+1j*np.asarray(y)).astype(dtype); M=len(z)
    Q=np.zeros((M,N),dtype=dtype); v=np.sqrt(np.asarray(w)).astype(dtype); Q[:,0]=v/np.sqrt(np.vdot(v,v).real)
    skipmax=0.0
    for k in range(1,N):
        t,s=idx[k]
        if s==0: u=np.conj(z)*Q[:,pos[(t-1,0)]]; W=list(range(start[max(t-2,0)],k))
        else:
            u=z*Q[:,pos[(t-1,s-1)]]
            lo=(start[t-2]+(s-1)) if t>=2 else 0
            if wmode=='block': lo=start[max(t-2,0)]
            if wmode=='full': lo=0
            W=list(range(lo,k))
        # measure skipped coefficients
        if k>1:
            Wc=[l for l in range(k) if l not in W]
            if Wc: skipmax=max(skipmax,float(np.abs(Q[:,Wc].conj().T@u).max()))
        nrm0=np.sqrt(np.vdot(u,u).real)
        for _ in range(2):
            for l in W:
                c=np.vdot(Q[:,l],u); u=u-c*Q[:,l]
            if np.sqrt(np.vdot(u,u).real)>0.707*nrm0: break
            nrm0=np.sqrt(np.vdot(u,u).real)
        Q[:,k]=u/np.sqrt(np.vdot(u,u).real)
    return Q,skipmax
P,w=L.nodes_random(1681,0); x,y=P[:,0],P[:,1]
for wm in ['exact','block','full']:
    Q,sk=simax(x,y,w,20,wm); G=Q.conj().T@Q
    out=[]
    for n in [8,12,16,20]:
        Nn=(n+1)*(n+2)//2; out.append('%d:%.1e'%(n,np.abs(G[:Nn,:Nn]-np.eye(Nn)).max()))
    print('double',wm,' '.join(out),'max skipped coef %.1e'%sk)
Q,sk=simax(x,y,w,14,'exact',dtype=np.clongdouble); G=Q.conj().T@Q
print('longdouble exact window: loss %.1e  max skipped coef %.1e'%(float(np.abs(G-np.eye(G.shape[0])).max()),sk))
