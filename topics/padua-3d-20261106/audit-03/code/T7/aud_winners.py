#!/usr/bin/env python3
"""Auditor (Claude): independent exact count/rank and Lambda of the selected
Phi / equal-U / unequal-U winners, at the rationalised (den 1009) phases and at
the floating optima.  Own monomial F_p evaluator; own float Lebesgue code."""
import itertools as it, json, math, sys
import numpy as np, sympy as sp

def group_pts(f, A):
    m = math.prod(f); A = np.array(A, dtype=np.int64)
    k = np.array(list(it.product(*(range(d) for d in f))), dtype=np.int64)
    P = ((k*np.array([m//d for d in f])) @ A) % m
    assert len({tuple(r) for r in P}) == m
    return P, m

def modes(n): return [a for a in it.product(range(n+1), repeat=3) if sum(a) <= n]

def exact(cosets, n):
    """cosets: list of (P,m,nums) with phase nums/1009. returns count, rank mod p"""
    D = math.lcm(1009, *(m for _, m, _ in cosets))
    rows = set()
    for P, m, nums in cosets:
        q = (P*(D//m) + np.array(nums)*(D//1009)) % D
        for r in q: rows.add(tuple(min(int(v), D-int(v)) for v in r))
    rows = sorted(rows)
    k = 2
    while not (sp.isprime(k*D+1)) or k*D+1 in (5051, 40361): k += 1
    p = k*D+1; w = pow(int(sp.primitive_root(p)), (p-1)//D, p); i2 = pow(2, -1, p)
    X = [[(pow(w, t, p)+pow(w, (D-t) % D, p))*i2 % p for t in r] for r in rows]
    A = [[math.prod(pow(x, e, p) for x, e in zip(r, al)) % p for al in modes(n)] for r in X]
    rk = 0; A = [row[:] for row in A]
    for j in range(len(A[0])):
        piv = next((i for i in range(rk, len(A)) if A[i][j]), None)
        if piv is None: continue
        A[rk], A[piv] = A[piv], A[rk]; inv = pow(A[rk][j], -1, p); A[rk] = [v*inv % p for v in A[rk]]
        for i in range(rk+1, len(A)):
            if A[i][j]:
                c = A[i][j]; A[i] = [(x-c*y) % p for x, y in zip(A[i], A[rk])]
        rk += 1
    return len(rows), rk, p, np.cos(2*np.pi*np.array(rows)/D)

def basis(x, n):
    th = np.arccos(np.clip(x, -1, 1))
    return np.stack([np.prod([np.cos(a[j]*th[:, j])*(np.sqrt(2) if a[j] else 1) for j in range(3)], axis=0) for a in modes(n)], axis=1)

g21 = np.cos(np.linspace(0, np.pi, 21)); MESH = np.array(list(it.product(g21, repeat=3)))
def lam(X, n):
    Vi = np.linalg.inv(basis(X, n)); return float(np.abs(basis(MESH, n) @ Vi).sum(axis=1).max())

def floatX(cosets_f):
    return np.concatenate([np.cos(2*np.pi*(P/m + np.array(a))) for P, m, a in cosets_f])

def main():
    E = sys.argv[1]; out = []
    phi = json.load(open(E+'/t7-r06-phi.json'))['phi']
    for r in phi:
        w = r['winner']
        if not w: continue
        P, m = group_pts(w['type'], w['embedding']); n = r['n']
        cnt, rk, p, Xr = exact([(P, m, w['rationalized_phase_mod1009'])], n)
        Xf = floatX([(P, m, w['lambda_phase'])])
        out.append(('Phi', n, cnt, rk, p, lam(Xr, n), lam(Xf, n), w['lambda_quality']['lambda21']))
    for name, key in (('U-equal', 'unions'), ):
        for r in json.load(open(E+'/t7-r06-unions.json'))['unions']:
            w = r['winner']
            if not w: continue
            P, m = group_pts(w['type'], w['embedding']); n = r['n']
            cnt, rk, p, Xr = exact([(P, m, nm) for nm in w['phase_mod1009']], n)
            Xf = floatX([(P, m, a) for a in w['phase']])
            out.append((name, n, cnt, rk, p, lam(Xr, n), lam(Xf, n), w['quality']['lambda21']))
    for r in json.load(open(E+'/t7-r06-unions-unequal.json'))['unequal_unions']:
        w = r['winner']; n = r['n']
        gs = [group_pts(f, A) for f, A in zip(w['types'], w['embeddings'])]
        cnt, rk, p, Xr = exact([(P, m, nm) for (P, m), nm in zip(gs, w['phase_mod1009'])], n)
        Xf = floatX([(P, m, a) for (P, m), a in zip(gs, w['phase'])])
        out.append(('U-unequal', n, cnt, rk, p, lam(Xr, n), lam(Xf, n), w['quality']['lambda21']))
    for o in out: print(json.dumps(o))

main()
