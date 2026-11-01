"""Claude audit-01: exploratory probe of the nine residual deficient C3 representatives (MEASURED only)."""
import json, random, itertools
from math import comb
R=json.load(open('topics/lattice-unisolvence-20261031/directions/C3/ranks.json'))
ids=['C3-146194f53e09','C3-63a9bc46428d','C3-b312ad59cf2d','C3-e94fa0f84746','C3-ed5be2a8aa20','C3-a86caab28e7a','C3-4b8f5204bfc8','C3-e52f073b516e','C3-1173efd58918']
reps={r['id']:r for r in R['representatives']}
src={}
for m in R['mapping']: src.setdefault(m['representative'],[]).append(m['pattern_id'])
cat={r['id']:r for r in json.load(open('topics/lattice-unisolvence-20261031/directions/C0/catalogue.json'))['patterns']}
p=1000003
def mons(n): return [(a,b,c) for a in range(n+1) for b in range(n+1-a) for c in range(n+1-a-b)]
def rank(M):
    M=[r[:] for r in M]; r=0
    if not M: return 0
    for col in range(len(M[0])):
        piv=next((i for i in range(r,len(M)) if M[i][col]),None)
        if piv is None: continue
        M[r],M[piv]=M[piv],M[r]; inv=pow(M[r][col],p-2,p)
        for i in range(len(M)):
            if i!=r and M[i][col]:
                f=M[i][col]*inv%p; M[i]=[(x-f*y)%p for x,y in zip(M[i],M[r])]
        r+=1
    return r
rng=random.Random(7)
def ev(P,ax,n): return [[pow(ax[0][i],a,p)*pow(ax[1][j],b,p)*pow(ax[2][k],c,p)%p for a,b,c in mons(n)] for i,j,k in P]
for rid in ids:
    r=reps[rid]; n=r['n']; L=r['lengths']; P=[tuple(x) for x in r['points']]; N=comb(n+3,3)
    ax=[rng.sample(range(p),l) for l in L]
    rk=rank(ev(P,ax,n))
    s=cat[src[rid][0]]
    # structure: points per layer on each axis
    layers=[[sum(1 for q in P if q[a]==v) for v in range(L[a])] for a in range(3)]
    # recursive single-layer removal with exact rank of Pi_{n-1} on the rest
    rec=[]
    for a in range(3):
        for v in range(L[a]):
            rest=[q for q in P if q[a]!=v]
            if rank(ev(rest,ax,n-1))<comb(n+2,3): rec.append((a,v))
    # bivariate-plane test: points in plane layer, rank of Pi_n restricted vs count
    print(rid,'n',n,'L',L,'src',s['k'],s['a'],s.get('residue',s.get('c')),'rank',rk,'/',N,'deficit',N-rk,'layers',layers,'single-layer-removal certs',rec)
