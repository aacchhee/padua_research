"""Audit-03 feasibility probe (not a developer artifact): exhaustive row-HNF
check of whether any integer lattice L<=Z^3 of determinant q has shortest
nonzero l1 norm >= 2n. Exact integer arithmetic."""
import itertools, math, sys, time
import numpy as np

def short_vectors(r):
    out=[]
    for v in itertools.product(range(-r, r+1), repeat=3):
        if 0 < sum(map(abs, v)) <= r: out.append(v)
    return np.array(out, dtype=np.int64)

def admissible_count(n, q, V):
    """Count HNFs of determinant q whose lattice avoids every vector in V."""
    v1, v2, v3 = V[:,0], V[:,1], V[:,2]
    hits = 0; tested = 0
    for a in [x for x in range(1, q+1) if q % x == 0]:
        mask1 = (v1 % a == 0); x1 = v1 // a
        for d in [y for y in range(1, q//a+1) if (q//a) % y == 0]:
            f = q // (a*d)
            for b in range(d):
                r2 = v2 - x1*b
                mask2 = mask1 & (r2 % d == 0); x2 = r2 // d
                if not mask2.any():
                    hits += f*f; tested += f*f; continue
                idx = np.nonzero(mask2)[0]
                X1 = x1[idx]; X2 = x2[idx]; V3 = v3[idx]
                for c in range(f):
                    base = V3 - X1*c
                    for e in range(f):
                        tested += 1
                        if not ((base - X2*e) % f == 0).any():
                            hits += 1
    return tested, hits

if __name__ == '__main__':
    n = int(sys.argv[1]); qs = [int(x) for x in sys.argv[2:]]
    V = short_vectors(2*n-1)
    for q in qs:
        t0 = time.process_time(); tested, hits = admissible_count(n, q, V)
        print(f"n={n} q={q} hnf_tested={tested} admissible={hits} cpu_s={time.process_time()-t0:.2f}", flush=True)
