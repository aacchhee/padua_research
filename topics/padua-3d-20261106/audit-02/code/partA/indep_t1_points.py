"""Auditor's independent actual-point census of reflection-invariant single cosets in T^3.
Written from the classification statement only (no repository code imported).
Coset: t_j=(i_j+eps_j/2)/m_j, i_j mod m_j, with sum_j b_j i_j = s_b (mod 2) for each basis vector b of a
unit-free binary code B (support = active coords, m_j even there), eps_j in {0,1} on inactive coords only.
Prune: each folded point has <=8 torus preimages, so |X|>=|H|/8; |H|=m1 m2 m3/|B|; skip |H|>8N.
Cap m_j<=2N: each axis projection of X has all its levels and <=N of them.  Exact integer folding:
cos(2 pi r/(2m)) equality <=> r = +-r' (mod 2m)."""
import itertools, math, sys, json
import numpy as np

def subspaces():
    out = []
    for mask in range(1, 1 << 8):
        S = [v for v in range(8) if mask >> v & 1]
        if 0 not in S: continue
        if all((a ^ b) in S for a in S for b in S): out.append(tuple(S))
    return out

def basis(S):
    B = []
    span = {0}
    for v in sorted(S):
        if v not in span:
            B.append(v); span |= {x ^ v for x in span}
    return B

def run(n):
    N = math.comb(n + 3, 3); cap = 2 * N
    codes = [S for S in subspaces() if not any((1 << j) in S for j in range(3))]
    assert len(codes) == 6, codes
    res = {"degree": n, "N": N, "cap": cap, "target_cases": 0, "short": 0, "alias_only": 0, "survivors": 0,
           "constructed_cases": 0, "per_code": {}}
    for S in codes:
        Bb = basis(S); k = len(Bb)
        active = [j for j in range(3) if any(v >> j & 1 for v in S)]
        inactive = [j for j in range(3) if j not in active]
        tc = 0
        for m in itertools.product(range(1, cap + 1), repeat=3):
            if any(m[j] % 2 for j in active): continue
            H = m[0] * m[1] * m[2] // (1 << k)
            if H > 8 * N: continue
            I = np.indices(m).reshape(3, -1).astype(np.int64)
            for synd in itertools.product((0, 1), repeat=k):
                mask = np.ones(I.shape[1], dtype=bool)
                for b, s in zip(Bb, synd):
                    tot = sum(I[j] for j in range(3) if b >> j & 1)
                    mask &= (tot % 2 == s)
                J = I[:, mask]
                for ph in itertools.product((0, 1), repeat=len(inactive)):
                    eps = [0, 0, 0]
                    for j, e in zip(inactive, ph): eps[j] = e
                    K = []
                    for j in range(3):
                        r = (2 * J[j] + eps[j]) % (2 * m[j])
                        K.append(np.minimum(r, 2 * m[j] - r))
                    code = (K[0] * (4 * cap + 1) + K[1]) * (4 * cap + 1) + K[2]
                    cnt = len(np.unique(code))
                    res["constructed_cases"] += 1
                    if cnt != N: continue
                    tc += 1
                    levels = [len(np.unique(K[j])) for j in range(3)]
                    short = min(levels) <= n
                    alias = (len(S) == 4) and sum(m[j] // 2 <= n for j in range(3)) >= 2
                    res["target_cases"] += 1
                    if short: res["short"] += 1
                    elif alias: res["alias_only"] += 1
                    else:
                        res["survivors"] += 1; print("SURVIVOR", n, S, m, synd, ph, levels, file=sys.stderr)
        res["per_code"][str(sorted(S))] = tc
    return res

if __name__ == "__main__":
    caps12 = {}
    out = [run(n) for n in range(2, 7)]
    print(json.dumps(out, indent=1))
