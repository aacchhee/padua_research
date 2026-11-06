import sys,math; sys.path.insert(0,'.')
from local_lemma import *
from fractions import Fraction as Q
def inputs(N,fam):
    M=N-1; x=[Q(2*k,M)-1 for k in range(N)]
    if fam=='krawtchouk': w=[[Q(math.comb(M,k))*p**k*(1-p)**(M-k) for k in range(N)] for p in (Q(2,5),Q(1,2))]
    else: w=[[math.prod((b+1+j for j in range(k)),start=Q(1))/math.factorial(k)*(N-k) for k in range(N)] for b in (Q(1),Q(3,2))]
    return x,w
def nn(x,W,N):
    Pd={(n,k-n):P(x,W,(n,k-n)) for k in range(N+1) for n in range(k+1)}
    return {(n,k-n):true_nn(x,W,(n,k-n),Pd) for k in range(N) for n in range(k+1)}
for fam in ('hahn','krawtchouk'):
    N=4; x,W=inputs(N,fam); c=nn(x,W,N)
    z=[(nu,f) for nu in c for f in c[nu] if c[nu][f]==0 and not ((f=='a1' and nu[0]==0) or (f=='a2' and nu[1]==0))]
    print(fam,'nonstructural zeros:',z)
    # sensitivity: perturb each weight separately by relative eps, check change
    for nu,f in z:
        sens=[]
        for s in range(2):
            for l in range(N):
                for eps in (Q(1,10**6),):
                    W2=[r[:] for r in W]; W2[s][l]*=(1+eps)
                    sens.append((nn(x,W2,N)[nu][f])/eps)
        print('  ',nu,f,'max |dF/dw (rel)| approx', float(max(abs(v) for v in sens)))
