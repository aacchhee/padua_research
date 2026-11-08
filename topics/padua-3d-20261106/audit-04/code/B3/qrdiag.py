import sys; sys.path.insert(0, __file__.rsplit('/',1)[0])
import numpy as np, scipy.linalg as sla, itertools
from aud_q import basis_rec, lebesgue, pivoted_gs
from alib import modes
for n in (3,7,8):
    N=len(modes(n)); ax2=np.cos(np.pi*np.arange(2*n+1)/(2*n))
    can=np.array([(x,y,z) for x in ax2 for y in ax2 for z in ax2]); A=basis_rec(can,n).T
    mine=pivoted_gs(A,N); _,R,piv=sla.qr(A,mode='economic',pivoting=True)
    lap=piv[:N].tolist()
    for s,(x,y) in enumerate(zip(mine,lap)):
        if x!=y: break
    Q=np.linalg.qr(A[:,lap[:s]])[0] if s else np.zeros((N,0))
    Rm=A-Q@(Q.T@A); nr=np.sqrt((Rm*Rm).sum(0)); nr[lap[:s]]=-1
    print(n,'diverge step',s,'mine',x,'lapack',y,'resid norms',nr[x],nr[y],'rel diff',abs(nr[x]-nr[y])/nr[y])
    l1=[lebesgue(can[sorted(lap)],n,m)[0] for m in (21,41)]; l2=[lebesgue(can[sorted(mine)],n,m)[0] for m in (21,41)]
    print(' Lebesgue lapack-set',l1,' own-GS set',l2)
    def canon(S):
        best=None
        for perm in itertools.permutations(range(3)):
            for sg in itertools.product((1,-1),repeat=3):
                T=sorted(tuple(round(sg[i]*p[perm[i]]+0.0,9) for i in range(3)) for p in S)
                if best is None or T<best: best=T
        return best
    print(' symmetric-equivalent:', canon(can[lap])==canon(can[mine]), 'identical:', sorted(lap)==sorted(mine))
