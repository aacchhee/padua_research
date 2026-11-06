"""Exact F_p certificate that the M=N=20, n=3 translated class (outside PD-N T8-02) has unisolvent members."""
import itertools as it, math, random, sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from audit_census import modes, rank_mod_p, prim_root_of_unity, primes_1_mod
L = 120; M = 20; p = primes_1_mod(L, 1, start=10**6)[0]; w = prim_root_of_unity(L, p); i2 = pow(2, -1, p)
cv = [(pow(w, e, p) + pow(w, -e % L, p)) * i2 % p for e in range(L)]
random.seed(3); found = []; tested = 0; byr = {}
for z in [(1, 2, 7), (1, 3, 4), (1, 5, 6), (2, 3, 9), (1, 4, 9), (1, 3, 9), (1, 2, 4)]:
    r = sum(c % 2 for c in z)
    for _ in range(20):
        ph = tuple(random.randrange(L) for _ in range(3))
        angs = [tuple((h + 6 * k * c) % L for c, h in zip(z, ph)) for k in range(M)]
        if len({tuple(min(a, L - a) for a in t) for t in angs}) < M: continue
        A = [[cv[a] ** e1 * cv[b] ** e2 * cv[c] ** e3 % p for e1, e2, e3 in modes(3)] for a, b, c in angs]
        rk = rank_mod_p(A, p); tested += 1; byr[r] = max(byr.get(r, 0), rk)
        if rk == 20 and len(found) < 3: found.append((z, ph))
print('p', p, 'tested', tested, 'max F_p rank by r', byr, 'certified unisolvent examples (z, phase numerators /120):', found)
