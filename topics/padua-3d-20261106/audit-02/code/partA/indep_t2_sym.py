"""Auditor's independent check of T2 survivor node-set classes (no repo code).
Node set of z=(1,b,c), odd M=2N-1: {(f(k), f(kb), f(kc))}, f(r)=min(r mod M, -r mod M).
Equivalence: equal node sets after some axis permutation (union-find over frozensets)."""
import itertools, math
def nodes(z, M):
    f = lambda r: min(r % M, (-r) % M)
    return frozenset((f(k*z[0]), f(k*z[1]), f(k*z[2])) for k in range(M))
for n in (2, 3, 4):
    N = math.comb(n+3, 3); M = 2*N - 1
    gens = list(itertools.combinations(range(1, N), 2))
    sets = {}
    for b, c in gens:
        X = nodes((1, b, c), M); assert len(X) == N
        sets[(1, b, c)] = X
    index = {}
    parent = {z: z for z in sets}
    def find(z):
        while parent[z] != z: z = parent[z]
        return z
    by_set = {}
    for z, X in sets.items(): by_set.setdefault(X, []).append(z)
    for z, X in sets.items():
        for p in itertools.permutations(range(3)):
            Y = frozenset(tuple(x[i] for i in p) for x in X)
            for w in by_set.get(Y, []):
                a, b2 = find(z), find(w)
                if a != b2: parent[max(a, b2)] = min(a, b2)
    classes = {}
    for z in sets: classes.setdefault(find(z), []).append(z)
    print(f"n={n} M={M} pairs={len(gens)} classes={len(classes)}")
    if n == 2:
        for z in [(1,3,7),(1,4,6),(1,5,8),(1,7,8)]: print("  ", z, "class rep", find(z), "members", sorted(classes[find(z)]))
    if n == 4:
        for z in [(1,11,15),(1,15,19),(1,21,29),(1,25,30)]: print("  ", z, "class rep", find(z), "members", sorted(classes[find(z)]))
        print("   lexicographic min of best pair:", min([(1,15,19),(1,21,29)]))
        u = pow(29, -1, M); print("   29^-1 mod 69 =", u, "(1,21,29)*u mod 69 =", tuple((u*x) % M for x in (1,21,29)), "gcd(21,69)=", math.gcd(21, 69))
