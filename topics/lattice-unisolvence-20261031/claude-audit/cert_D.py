"""Claude audit-01: additive-separation (repeated-layer) annihilator certificate, tested on every C3 representative.
Certificate D(r): classes C of nonempty r-layers with identical projected index sets P_C;
E = sum_C (|P_C| + |C| - 1).  If E < binom(n+2,2) + n then no within-axis-distinct labelling is unisolvent
(proof in audit-01.md: nonzero f = g(x_r) + Q(x_s,x_t) in Pi_n vanishing on S)."""
import json
from math import comb
R=json.load(open('topics/lattice-unisolvence-20261031/directions/C3/ranks.json'))
S=json.load(open('topics/lattice-unisolvence-20261031/directions/C3/structure.json'))
O=json.load(open('topics/lattice-unisolvence-20261031/directions/C3/obstructions.json'))
nine=['C3-146194f53e09','C3-63a9bc46428d','C3-b312ad59cf2d','C3-e94fa0f84746','C3-ed5be2a8aa20','C3-a86caab28e7a','C3-4b8f5204bfc8','C3-e52f073b516e','C3-1173efd58918']
def certD(r):
    n=r['n']; P=[tuple(q) for q in r['points']]; hits=[]
    for a in range(3):
        cls={}
        for v in range(r['lengths'][a]):
            proj=frozenset(tuple(q[o] for o in range(3) if o!=a) for q in P if q[a]==v)
            if proj: cls.setdefault(proj,[]).append(v)
        E=sum(len(pc)+len(c)-1 for pc,c in cls.items())
        if E<comb(n+2,2)+n: hits.append({'axis':a,'E':E,'bound':comb(n+2,2)+n,'classes':sorted(c for c in cls.values() if len(c)>1)})
    return hits
full=[r for r in R['representatives'] if r['rank_max']==r['N']]
defi=[r for r in R['representatives'] if r['rank_max']<r['N']]
bad=[r['id'] for r in full if certD(r)]
cov=[r['id'] for r in defi if certD(r)]
print('full-rank reps satisfying D (must be 0):',len(bad))
print('deficient reps covered by D:',len(cov),'of',len(defi))
print('nine residual all covered:',all(i in cov for i in nine))
for i in nine: print(i,certD(next(r for r in defi if r['id']==i)))
json.dump({'covered':cov,'nine':{i:certD(next(r for r in defi if r['id']==i)) for i in nine}},open('topics/lattice-unisolvence-20261031/claude-audit/outputs/certD.json','w'),indent=1)
