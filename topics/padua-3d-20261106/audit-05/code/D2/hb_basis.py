"""Basis-dependence of HB nonzero count: RREF under permuted unknown orders."""
import sys, json, random
sys.path.insert(0, '.')
from hb_check import *
def count(n, order):
    q = [padd(cheb(n + 1, X), cheb(n - 1, X), -1)] + [
        padd(pmul(cheb(n + 1 - k, X), cheb(k, Y)), pmul(cheb(k - 1, X), cheb(n + 1 - k, Y)), -1) for k in range(1, n + 2)]
    cols = [pmul(t, g) for g in q for t in (ONE, X, Y)]
    cols = [cols[i] for i in order]
    mons = sorted({m for c in cols for m in c})
    ns = nullspace([[c.get(m, F(0)) for c in cols] for m in mons], len(cols))
    inv = {o: i for i, o in enumerate(order)}
    nz = 0
    for b in ns:
        for g in range(n + 2):
            if any(b[inv[3 * g + t]] != 0 for t in range(3)): nz += 1
    return len(ns), nz
for n in (2, 3, 4):
    L = 3 * (n + 2); res = {count(n, list(range(L)))}
    rng = random.Random(7)
    for _ in range(30):
        o = list(range(L)); rng.shuffle(o); res.add(count(n, o))
    print(n, sorted(res))
