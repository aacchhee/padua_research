"""Exact construction of f=g(x_r)+Q(x_s,x_t) from certificate D's reduced system, over Q, for the nine residuals."""
import json, random, sympy as sp
from math import comb
R=json.load(open('topics/lattice-unisolvence-20261031/directions/C3/ranks.json'))
reps={r['id']:r for r in R['representatives']}
D=json.load(open('topics/lattice-unisolvence-20261031/claude-audit/outputs/certD.json'))['nine']
rng=random.Random(99)
for rid,h in D.items():
    r=reps[rid]; n=r['n']; a=h[0]['axis']; o=[t for t in range(3) if t!=a]; P=[tuple(q) for q in r['points']]
    ax=[[sp.Rational(v,rng.randint(1,7)) for v in rng.sample(range(-60,61),L)] for L in r['lengths']]
    gs=sp.symbols(f'g0:{n+1}'); qm=[(i,n_-i) for n_ in range(n+1) for i in range(n_+1)]; qs=sp.symbols(f'q0:{len(qm)}')
    def f(pt):
        t=ax[a][pt[a]]; u=ax[o[0]][pt[o[0]]]; v=ax[o[1]][pt[o[1]]]
        return sum(gs[k]*t**k for k in range(1,n+1))+sum(qs[m]*u**e1*v**e2 for m,(e1,e2) in enumerate(qm))
    # reduced system: one representative layer per class for Q-equations, plus g-equalities
    cls={}
    for val in range(r['lengths'][a]):
        pr=frozenset(tuple(q[t] for t in o) for q in P if q[a]==val)
        if pr: cls.setdefault(pr,[]).append(val)
    eqs=[]
    for pr,c in cls.items():
        rep=c[0]
        for (j,k) in pr:
            pt=[0,0,0]; pt[a]=rep; pt[o[0]]=j; pt[o[1]]=k; eqs.append(f(pt))
        for other in c[1:]:
            eqs.append(sum(gs[k]*(ax[a][other]**k-ax[a][rep]**k) for k in range(1,n+1)))
    unknowns=list(gs[1:])+list(qs)
    A=sp.Matrix([[sp.diff(e,u) for u in unknowns] for e in eqs])
    ns=A.nullspace(); assert ns, rid
    sol=dict(zip(unknowns,ns[0]))
    vals=[sp.simplify(f(pt).subs(sol)) for pt in P]
    nonzero=any(v!=0 for v in ns[0])
    print(rid,'reduced eqs',len(eqs),'unknowns',len(unknowns),'f vanishes on all',len(P),'nodes:',all(v==0 for v in vals),'f nonzero:',nonzero)
