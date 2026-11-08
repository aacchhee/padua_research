"""Auditor's independent S (sparse DCT support) census. No producer imports."""
import json, math, sys, time, random
from fractions import Fraction as F
from collections import Counter
import numpy as np
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from alib import modes, perfect_matching, has_alternating_cycle, frac_inverse, bareiss_rank

OUT = sys.argv[1]
DEG = [int(x) for x in sys.argv[2].split(',')] if len(sys.argv) > 2 else [3, 5, 7]


def cos_expand(alpha, z):
    """8 * prod_j cos(alpha_j z_j t) as dict freq>=0 -> integer (product-to-sum)."""
    cur = {0: 1}
    for a, g in zip(alpha, z):
        A = a * g
        nxt = Counter()
        for f, c in cur.items():
            nxt[abs(f - A)] += c
            nxt[f + A] += c
        cur = nxt
    return cur


def alias_matrix(n, z, raw=False):
    """C with V = B C / 8 at theta_k=(2k+1)pi/(2N). raw=True also returns pre-cancellation support."""
    N = len(modes(n)); P = 4 * N
    C = [[0] * N for _ in range(N)]
    touched = set()
    for j, al in enumerate(modes(n)):
        for f, c in cos_expand(al, z).items():
            m = f % P
            if m > 2 * N:
                m = P - m
            if m == N:
                continue
            s = 1
            if m > N:
                m = 2 * N - m; s = -1
            C[m][j] += s * c
            touched.add((m, j))
    return (C, touched) if raw else C


def numeric_check(n, z, C):
    N = len(modes(n)); th = (2 * np.arange(N) + 1) * np.pi / (2 * N)
    B = np.cos(np.outer(th, np.arange(N)))
    V = np.array([[math.prod(math.cos(a * g * t) for a, g in zip(al, z)) for al in modes(n)] for t in th])
    Cn = 8 * np.linalg.solve(B, V)
    return float(np.max(np.abs(Cn - np.array(C, dtype=float))))


def classify(C, N, edge_deletion=False):
    adj = [[j for j in range(N) if C[i][j]] for i in range(N)]
    mc = perfect_matching(adj, N)
    if mc is None:
        return 'none', None
    cyc = has_alternating_cycle(adj, mc, N)
    if edge_deletion:
        # independent uniqueness test: delete each matched edge, look for another perfect matching
        alt = False
        for c, r in enumerate(mc):
            adj2 = [[j for j in row if not (i == r and j == c)] for i, row in enumerate(adj)]
            if perfect_matching(adj2, N) is not None:
                alt = True; break
        assert alt == cyc, 'edge-deletion and cycle tests disagree'
    return ('nonunique' if cyc else 'unique'), mc


def main():
    t0 = time.time(); res = {}
    rng = random.Random(20261108)
    for n in DEG:
        N = len(modes(n)); hist = Counter(); uniq = []; nonuniq = []; cancel_mats = 0; cls_change = 0
        maxnum = 0.0; numcount = 0
        pairs = [(b, c) for b in range(1, 2 * N) for c in range(b + 1, 2 * N)]
        sample = set(rng.sample(range(len(pairs)), 400)) if n == 7 else None
        for idx, (b, c) in enumerate(pairs):
            z = (1, b, c)
            C, touched = alias_matrix(n, z, raw=True)
            supp = {(i, j) for i in range(N) for j in range(N) if C[i][j]}
            if supp != touched:
                cancel_mats += 1
            cl, mc = classify(C, N, edge_deletion=(n <= 5))
            if supp != touched:
                # classification if one (wrongly) used pre-cancellation support
                Craw = [[1 if (i, j) in touched else 0 for j in range(N)] for i in range(N)]
                cl2, _ = classify(Craw, N)
                if cl2 != cl:
                    cls_change += 1
            hist[cl] += 1
            if n <= 5 or idx in sample or cl != 'none':
                maxnum = max(maxnum, numeric_check(n, z, C)); numcount += 1
            if cl == 'unique':
                inv = frac_inverse(C)  # C^{-1}
                S = sum(abs(8 * x) for row in inv for x in row)
                infn = max(sum(abs(8 * x) for x in row) for row in inv)
                # determinant from matching product (unique matching)
                det = 1
                for col, r in enumerate(mc):
                    det *= C[r][col]
                uniq.append({'z': z, 'S': str(S), 'inf': str(infn), 'abs_det_C': abs(det)})
            elif cl == 'nonunique':
                nonuniq.append({'z': z, 'rank': bareiss_rank(C)})
        res[n] = {'N': N, 'pairs': len(pairs), 'hist': dict(hist), 'unique': uniq,
                  'nonunique_rank_hist': dict(Counter(r['rank'] for r in nonuniq)),
                  'nonunique_full_rank': [list(r['z']) for r in nonuniq if r['rank'] == N],
                  'matrices_with_cancellation': cancel_mats, 'class_changes_if_precancel_support': cls_change,
                  'numeric_alias_check_max_abs': maxnum, 'numeric_checked': numcount,
                  'seconds': time.time() - t0}
        print(n, res[n]['hist'], res[n]['nonunique_rank_hist'], cancel_mats, cls_change, maxnum, numcount, time.time() - t0, flush=True)
    json.dump(res, open(OUT, 'w'), indent=1, default=str)


if __name__ == '__main__':
    main()
