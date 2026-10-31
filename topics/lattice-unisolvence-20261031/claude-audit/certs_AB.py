"""Claude audit-01: independent exhaustive search for PD-T?lattice-c3-codex-02 certificates (A) cover and (B) projection."""
import json, itertools
from math import comb
R=json.load(open('topics/lattice-unisolvence-20261031/directions/C3/ranks.json'))
D=json.load(open('topics/lattice-unisolvence-20261031/claude-audit/outputs/certD.json'))['covered']
defi=[r for r in R['representatives'] if r['rank_max']<r['N']]; full=[r for r in R['representatives'] if r['rank_max']==r['N']]
def coverA(r):
    n=r['n']; L=r['lengths']; P=[tuple(q) for q in r['points']]
    layers=[(a,v) for a in range(3) for v in range(L[a])]
    masks={}
    for idx,q in enumerate(P):
        for a in range(3): masks[(a,q[a])]=masks.get((a,q[a]),0)|(1<<idx)
    allm=(1<<len(P))-1
    lm=[masks.get(l,0) for l in layers]
    for size in range(1,n+1):
        for comb_ in itertools.combinations(range(len(layers)),size):
            m=0
            for c in comb_: m|=lm[c]
            if m==allm: return [layers[c] for c in comb_]
    return None
def projB(r):
    n=r['n']; L=r['lengths']; P=[tuple(q) for q in r['points']]
    for a in range(3):
        for q in range(0,n+1):
            for A in itertools.combinations(range(L[a]),q):
                proj={tuple(p[o] for o in range(3) if o!=a) for p in P if p[a] not in A}
                if len(proj)<comb(n-q+2,2): return (a,A)
    return None
a=[r['id'] for r in defi if coverA(r)]
b=[r['id'] for r in defi if not coverA(r) and projB(r)]
rest=[r['id'] for r in defi if not coverA(r) and not projB(r)]
print('cover A:',len(a),' projection B (not A):',len(b),' neither:',len(rest))
print('neither == developer nine:',sorted(rest)==sorted(['C3-146194f53e09','C3-63a9bc46428d','C3-b312ad59cf2d','C3-e94fa0f84746','C3-ed5be2a8aa20','C3-a86caab28e7a','C3-4b8f5204bfc8','C3-e52f073b516e','C3-1173efd58918']))
print('neither all covered by D:',all(x in D for x in rest))
print('false positives on full-rank reps: A',sum(1 for r in full if coverA(r)),'B',sum(1 for r in full if projB(r)))
