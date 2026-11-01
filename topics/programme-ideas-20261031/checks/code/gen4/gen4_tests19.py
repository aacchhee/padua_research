import numpy as np, sys, itertools
sys.path.insert(0,'.')
from gen4_tests import cheb_basis
# (A) 2D equispaced grid, equal weights: saturation s_k(B)=w_B K_k(B,B); where is s=1?
for n in (24,40,60):
    g=np.linspace(-1,1,n+1); XX,YY=np.meshgrid(g,g); X=XX.ravel(); Y=YY.ravel(); w=np.ones(len(X))/len(X)
    for th in (0.5,0.75,0.9):
        k=int(round(th*n)); V,idx=cheb_basis(X,Y,k); Q,R=np.linalg.qr(np.sqrt(w)[:,None]*V); s=np.sum(Q**2,axis=1)
        r=np.maximum(np.abs(X),np.abs(Y)); rad=np.sqrt(X**2+Y**2)
        sat=s>1-1e-6
        # is saturated set a product/strip near boundary? report min max-norm among saturated, and whether saturation is monotone in max-norm
        print('eq2D n',n,'theta',th,'N_k/M %.3f'%(len(idx)/len(X)),'frac s>1-1e-6: %.3f'%sat.mean(),'frac s>0.99: %.3f'%np.mean(s>0.99),'min maxnorm of saturated: %.3f'%(r[sat].min() if sat.any() else -1),'1D r=sqrt(1-th^2)=%.3f'%np.sqrt(1-th**2),
              '| s at (1,1) %.3f (1,0) %.3f (0,0) %.3f (0.5,0.5) %.3f'%(s[(X==1)&(Y==1)][0], s[(X==1)&(np.abs(Y)<1e-9)][0], s[(np.abs(X)<1e-9)&(np.abs(Y)<1e-9)][0], s[np.argmin((X-.5)**2+(Y-.5)**2)]))
# (B) 3D product Chebyshev sections on Pi_{n-1}(R^3): pairwise commutator ranks and Koiran-type bound dim + rank/2
def sec3(m):
    idx=[(i,j,l) for d in range(m+1) for i in range(d+1) for j in range(d-i+1) for l in [d-i-j]]
    pos={p:q for q,p in enumerate(idx)}; N=len(idx)
    def J(i,i2): return (1/np.sqrt(2) if min(i,i2)==0 else 0.5) if abs(i-i2)==1 else 0.0
    H=[np.zeros((N,N)) for _ in range(3)]
    for p,q in pos.items():
        for c in range(3):
            for s in (-1,1):
                p2=list(p); p2[c]+=s; p2=tuple(p2)
                if p2 in pos: H[c][pos[p2],q]=J(p[c],p2[c])
    return H,N
for n in range(2,8):
    H,N=sec3(n-1)
    C=[H[a]@H[b]-H[b]@H[a] for a,b in ((0,1),(0,2),(1,2))]
    ranks=[np.linalg.matrix_rank(c,tol=1e-10) for c in C]
    S=np.hstack(C); rs=np.linalg.matrix_rank(S,tol=1e-10)
    # Möller-type 3D lower bound for centrally symmetric: N >= dim Pi_{n-1} + ... (Mysovskikh): use dim + (number of odd-degree ... ) skip; print LSX n^3/4
    print('3D n',n,'dim Pi_{n-1}',N,'pairwise commutator ranks',ranks,'dim of sum of images',rs,'bound dim+rank/2',N+ranks[0]//2,'Koiran hyp (sum=3*rank/2)?',rs==3*ranks[0]//2,'LSX n^3/4=%.1f'%(n**3/4),'dim Pi_n',(n+1)*(n+2)*(n+3)//6)
