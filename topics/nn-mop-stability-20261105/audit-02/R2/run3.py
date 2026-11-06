import sys,random; sys.path.insert(0,'.')
from local_lemma import *
from fractions import Fraction as F
random.seed(7); stats=dict(cert_pass=0,cert_fail=0,impl_ok=0)
for trial in range(60):
    N=random.randint(3,7)
    x=sorted(random.sample(range(-20,21),N)); x=[F(v,3) for v in x]
    w1=[F(random.randint(1,9),random.randint(1,4)) for _ in range(N)]
    w2=[F(random.randint(1,9),random.randint(1,4)) for _ in range(N)]
    if trial%3==0: w2=list(w1); w2[0]+=F(1,7)  # near-degenerate
    try:
        c=c4(x,[w1,w2],N-2); passed=all(c[nu]['b2']!=c[nu]['b1'] for nu in c)
    except ZeroDivisionError: passed=False
    allnorm=all(normal(x,[w1,w2],(n,k-n)) for k in range(N+1) for n in range(k+1))
    if passed:
        stats['cert_pass']+=1; assert allnorm
        # computed equals true
        Pd={(n,k-n):P(x,[w1,w2],(n,k-n)) for k in range(N+1) for n in range(k+1)}
        for k in range(N-1):
            for n in range(k+1):
                tr=true_nn(x,[w1,w2],(n,k-n),Pd)
                assert all(tr[f]==c[(n,k-n)][f] for f in tr)
        stats['impl_ok']+=1
    else: stats['cert_fail']+=1; print('cert fail, allnormal=',allnorm,'N',N)
# planted degree-N singular case from run2 (N=6): (3,3) singular
print(stats)
