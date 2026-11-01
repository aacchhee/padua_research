"""Claude audit-01: independent recomputation of all stored C3 rectangle determinants from stored axes."""
import json
from math import comb
O=json.load(open('topics/lattice-unisolvence-20261031/directions/C3/obstructions.json'))
R=json.load(open('topics/lattice-unisolvence-20261031/directions/C3/ranks.json'))
reps={r['id']:r for r in R['representatives']}
def mons(n): return [(a,b,c) for d in range(n+1) for a in range(d+1) for b in range(d-a+1) for c in [d-a-b]]
def det(M,p):
    M=[[v%p for v in r] for r in M]; n=len(M); d=1
    for c in range(n):
        piv=next((i for i in range(c,n) if M[i][c]),None)
        if piv is None: return 0
        if piv!=c: M[c],M[piv]=M[piv],M[c]; d=-d
        d=d*M[c][c]%p; inv=pow(M[c][c],p-2,p)
        for i in range(c+1,n):
            f=M[i][c]*inv%p
            if f: M[i]=[(x-f*y)%p for x,y in zip(M[i],M[c])]
    return d%p
t=O['rectangle_tests'][0]['tests'][0]; print({k:(v if not isinstance(v,list) else str(v)[:120]) for k,v in t.items()})
import json as _j
def build(rid,ax):
    r=reps[rid]; n=r['n']
    return [[pow(ax[0][i],a,1009)*pow(ax[1][j],b,1009)*pow(ax[2][k],c,1009) for a,b,c in mons(n)] for i,j,k in r['points']]
match={'thirdA':0,'thirdB':0}; total=0; nonzero_reps=set(); mism=[]
for rt in O['rectangle_tests']:
    rid=rt['id']
    for t in rt['tests']:
        pair=_j.loads(t['pair']) if isinstance(t['pair'],str) else t['pair']
        A=_j.loads(t['axes_a']) if isinstance(t['axes_a'],str) else t['axes_a']; B=_j.loads(t['axes_b']) if isinstance(t['axes_b'],str) else t['axes_b']
        dets=_j.loads(t['determinants_AA_AB_BA_BB']) if isinstance(t['determinants_AA_AB_BA_BB'],str) else t['determinants_AA_AB_BA_BB']
        r_,s_=pair; tt=3-r_-s_
        for conv in ('thirdA','thirdB'):
            out=[]
            for u,v in (('A','A'),('A','B'),('B','A'),('B','B')):
                ax=[None]*3; ax[r_]=(A if u=='A' else B)[r_]; ax[s_]=(A if v=='A' else B)[s_]; ax[tt]=(A if conv=='thirdA' else B)[tt]
                out.append(det(build(rid,ax),1009))
            if out==dets: match[conv]+=1
        total+=1
        rect=(dets[0]*dets[3]-dets[1]*dets[2])%1009
        if rect: nonzero_reps.add(rid)
print('tests',total,'convention matches',match)
by={}
for rid in nonzero_reps: by[reps[rid]['n']]=by.get(reps[rid]['n'],0)+1
print('reps with nonzero rectangle',len(nonzero_reps),dict(sorted(by.items())))
