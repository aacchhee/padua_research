"""Auditor: re-enumerate admissible lattices with N <= |X| < target and compute EXACT rational
rank (Fraction elimination of the character-incidence matrix) to confirm the minimum full-rank fold."""
import sys,os,json,math,itertools as it,collections
from fractions import Fraction
import numpy as np
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from hnf_search import ball, admissible_at
from minfold_search import fold, exps
def exact_rank(v,n):
    a,b,c,d,e,f=v; q=a*d*f
    adj=np.array([[d*f,-b*f,b*e-c*d],[0,a*f,-a*e],[0,0,a*d]],dtype=np.int64)
    rows=[]
    for al in exps(n):
        col=collections.Counter()
        for s in it.product(*[[-x,x] if x else [0] for x in al]):
            col[tuple(((np.array(s)@adj)%q).tolist())]+=1
        rows.append({k:Fraction(x) for k,x in col.items()})
    piv={}
    for r in rows:
        r=dict(r)
        while r:
            k=min(r)
            if k not in piv: piv[k]={kk:vv/r[k] for kk,vv in r.items()}; break
            val=r[k]
            for kk,vv in piv[k].items():
                z=r.get(kk,0)-val*vv
                if z: r[kk]=z
                else: r.pop(kk,None)
    return len(piv)
n=int(sys.argv[2]); target=int(sys.argv[3]); N=math.comb(n+3,3); K=ball(2*n-1)
stats=collections.Counter(); best=None
for q in range(N,8*(target-1)+1):
    good,_=admissible_at(q,K)
    for v in good:
        _,F=fold(v); m=len(F)
        if N<=m<target:
            r=exact_rank(v,n); stats[(m,r)]+=1
            if r==N and (best is None or m<best[1]): best=(v,m)
res={'n':n,'target':target,'fold_rank_hist':sorted([[k[0],k[1],c] for k,c in stats.items()]),'min_full_rank':best}
print(res,flush=True); json.dump(res,open(sys.argv[1],'w'))
