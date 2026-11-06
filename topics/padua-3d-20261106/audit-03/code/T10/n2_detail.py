import sys,os,math,json,collections
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from hnf_search import ball, admissible_at
from minfold_search import fold, rank_mod
n=2;N=10;K=ball(3);stats=collections.Counter();full=[]
for q in range(N,89):
    good,_=admissible_at(q,K)
    for v in good:
        _,F=fold(v);m=len(F)
        if N<=m<12:
            r=rank_mod(v,n);stats[(q,m,r)]+=1
            if r==N: full.append((v,m))
print(sorted(stats.items()))
print('full-rank count',len(full),'by det',collections.Counter(v[0]*v[3]*v[5] for v,m in full),'by fold',collections.Counter(m for v,m in full))
json.dump({'stats':[[list(k),c] for k,c in sorted(stats.items())],'full':full},open(sys.argv[1],'w'))
