"""Audit probe: M=2N first-unit half-shifted strata (h=1, J empty), predicted by PD-T r06-02."""
import math, sys, json, itertools as it
sys.path.insert(0, '.')
import t8_exact_audit as ex
res = {}
for n in (2, 3, 4):
    N = math.comb(n+3, 3); M = 2*N
    cnt = full = 0; first = None
    pairs = list(it.combinations(range(1, M), 2))
    for b, c in pairs:
        z = (1, b, c)
        L, nodes = ex.nodes_exact(M, z, [z], 2*M)   # a = z/(2M)
        if len(nodes) != N: continue
        cnt += 1
        p, w = ex.primes_for(L, 1)[0]
        r = ex.modular_rank(n, L, nodes, p, w)
        if r == N:
            full += 1
            if first is None: first = z
    res[n] = {'M': M, 'pairs': len(pairs), 'count_N': cnt, 'modular_full_rank': full, 'first': first}
    print(n, res[n], flush=True)
json.dump(res, open(sys.argv[1], 'w'))
