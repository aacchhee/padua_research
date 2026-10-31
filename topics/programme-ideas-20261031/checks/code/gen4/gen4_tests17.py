import numpy as np, sys
sys.path.insert(0,'.')
from gen4_tests import cheb_basis
def checker(X,Y): return np.array([(X[j],Y[k]) for j in range(len(X)) for k in range(len(Y)) if (j+k)%2==0])
def logdet_mon(X,Y,n):
    P=checker(X,Y); V,_=cheb_basis(P[:,0],P[:,1],n); return np.sum(np.log(np.linalg.svd(V,compute_uv=False)))
rng=np.random.default_rng(3)
for n in (4,5,6,7):
    Y=np.sort(rng.uniform(-1,1,n+2))[::-1]
    # hypothesis: logdet = const + sum_{j<k} a(j,k) log|x_j-x_k| + sum_j b_j log|1-x_j|?... test pure pairwise with parity classes: same parity vs different parity
    def feats(X):
        s=d=0.0
        for j in range(n+1):
            for k in range(j+1,n+1):
                if (j-k)%2==0: s+=np.log(abs(X[j]-X[k]))
                else: d+=np.log(abs(X[j]-X[k]))
        return s,d
    rows=[];rhs=[]
    for t in range(40):
        X=np.sort(rng.uniform(-1,1,n+1))[::-1]
        s,d=feats(X); rows.append([s,d,1.0]); rhs.append(logdet_mon(X,Y,n))
    c,res,_,_=np.linalg.lstsq(np.array(rows),np.array(rhs),rcond=None)
    print('n',n,'fit exponents: same-parity %.4f diff-parity %.4f const %.4f  residual %.2e'%(c[0],c[1],c[2],np.sqrt(res[0]/40) if len(res) else 0))
