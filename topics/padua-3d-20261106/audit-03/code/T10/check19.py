import json,sys,os,itertools as it, numpy as np
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from minfold_search import fold, rank_mod
cert=json.load(open(sys.argv[1]))
def minl1(v,R=40):
    a,b,c,d,e,f=v; best=10**9
    for u in range(-R,R+1):
        for w2 in range(-R,R+1):
            base=u*c+w2*e
            # third coordinate base + f*w; choose w minimizing |.|
            for w in (-(base//f)-1,-(base//f),-(base//f)+1):
                k=(u*a, u*b+w2*d, base+f*w)
                s=sum(map(abs,k))
                if 0<s<best: best=s
    return best
rows=[]
for a,b_,c_,r,s,t in cert['prime_survivors_HNF']:
    v=(a,r,s,b_,t,c_)   # rows (a,r,s),(0,b,t),(0,0,c) -> my (a,b,c,d,e,f)
    q,F=fold(v); rows.append((v,minl1(v),len(F),rank_mod(v,2)))
adm=[x for x in rows if x[1]>=4]
print('total',len(rows),'admissible(min l1>=4)',len(adm),'fold/rank of admissible',set((x[2],x[3]) for x in adm))
print('nonadmissible min l1 values',sorted(set(x[1] for x in rows if x[1]<4)))
for x in rows: print(x)
