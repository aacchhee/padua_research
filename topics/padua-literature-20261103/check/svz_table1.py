# Reader's consistency check (not a repo claim): signed Padua weights via (L2) of
# topics/padua-mz-2d-20261101/literature.md, compare sum|w|-4 with SVZ Table 1 (journal p.421).
import numpy as np, sys
def weights(m, denom_shift=0):
    xs=np.cos(np.arange(m+1)*np.pi/m); ys=np.cos(np.arange(m+2)*np.pi/(m+1))
    h=lambda r: 2.0/(1-r*r) if r%2==0 else 0.0
    W=[];P=[]
    for j in range(m+1):
        for k in range(m+2):
            if (j+k)%2: continue
            cj=0.5 if j in (0,m) else 1.0; ck=0.5 if k in (0,m+1) else 1.0
            a=2*cj*ck/(m*(m+1))
            if denom_shift: a=2*cj*ck/((m+1)*(m+2))   # literal (25) with n=m-1
            s=0.0
            for r in range(m+1):
                Tr=np.cos(r*np.arccos(xs[j]))
                for t in range(m+1-r):
                    s+=2**((r>0)+(t>0))*h(r)*h(t)*Tr*np.cos(t*np.arccos(ys[k]))
            s-=h(m)*h(0)*np.cos(m*np.arccos(xs[j]))
            W.append(a*s); P.append((j,k))
    return np.array(W),P
for m in [5,10,15,20,25,30,35,40]:
    w,P=weights(m); wl,_=weights(m,1)
    neg=[(P[i],w[i]) for i in range(len(w)) if w[i]<0]
    print(m, "sum=%.15f"%w.sum(), "sum|w|-4=%.2e"%(abs(w).sum()-4), "#neg=%d"%len(neg), "literal(25) sum=%.6f ratio=%.6f (m/(m+2)=%.6f)"%(wl.sum(), wl.sum()/4, m/(m+2)))
print("negative nodes (j,k) and values:")
for m in [3,4,5,10,40]:
    w,P=weights(m); print(m,[(P[i],"%.3e"%w[i]) for i in range(len(w)) if w[i]<0], "corner formula -(4log m)/m^4=%.2e"%(-4*np.log(m)/m**4))
