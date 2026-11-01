"""C01: checks of reconstruction 01 findings (reviews/L1-reconstruction-01.md) with the developer's code and seeds.
Criteria: candidates.md section C01 (written before this script).  MEASURED only.
Usage: python3 -I l1_c01_recon_checks.py rule <R01 raw logs...>   |   python3 -I l1_c01_recon_checks.py runs"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from collections import defaultdict
import l1_recurrence as L

U53 = 2.0 ** -53
Nof = lambda n: (n + 1) * (n + 2) // 2


# ---------------------------------------------------------------- C01-1 / C01-1': re-application of the R01 rule
def judge(recs, key, u):
    tau = 1e3 * u
    D = [r for r in recs if r['loss'] >= tau or u / max(r[key], 1e-300) >= tau]
    if not D:
        return 'uninformative'
    ratios = [r['loss'] / (u / max(r[key], 1e-300)) for r in D]
    if all(1 / 3 <= q <= 3 for q in ratios):
        return 'PREDICTS'
    tag = 'tracks' if (len(ratios) >= 2 and max(ratios) / min(ratios) <= 9) else 'fails'
    if min(ratios) < 1 / 30: tag += '/over'
    if max(ratios) > 30: tag += '/under'
    return tag


def rule(files):
    rows = []
    for fn in files:
        for line in open(fn):
            if line.startswith('JSON '):
                rows.append(json.loads(line[5:]))
    rows = [r for r in rows if r['method'] != 'simax']
    for u, ulab in [(2.0 ** -52, '2^-52 (rule as written)'), (U53, '2^-53 (plan unit roundoff)')]:
        for excl, elab in [('NM', 'N = M excluded (R01)'), ('NM+chain', 'N = M and tensor41 n = 40 excluded (symmetric)')]:
            keep = [r for r in rows if r['N'] < r['M'] and not (excl == 'NM+chain' and r['run'] == 'tensorcheb41' and r['n'] >= 40)]
            runs = defaultdict(list)
            for r in keep: runs[(r['run'], r['method'])].append(r)
            V = {(k, o): judge(sorted(v, key=lambda r: r['n']), key, u) for k, v in runs.items()
                 for o, key in [('X', 'res_x'), ('Y', 'res_y'), ('Z', 'res_z')]}
            zpred = [k for (k, o), t in V.items() if o == 'Z' and t == 'PREDICTS']
            k1 = bool(zpred) and all(V[(k, 'X')] == 'PREDICTS' or V[(k, 'Y')] == 'PREDICTS' for k in zpred)
            over = [k for (k, o), t in V.items() if o in ('X', 'Y') and 'over' in t and V[(k, 'Z')] in ('PREDICTS', 'uninformative')]
            print(f"== u = {ulab}; {elab}")
            for k in sorted(zpred): print(f"   Z predicts on {k[0]:22s} {k[1]}: X {V[(k, 'X')]:13s} Y {V[(k, 'Y')]}")
            sep = [k for k in runs if V[(k, 'Z')] != 'PREDICTS' and (V[(k, 'X')] == 'PREDICTS' or V[(k, 'Y')] == 'PREDICTS')]
            for k in sorted(sep): print(f"   single predicts, Z does not: {k[0]:22s} {k[1]}: X {V[(k, 'X')]} Y {V[(k, 'Y')]} Z {V[(k, 'Z')]}")
            print(f"   K1 fires: {k1};  single-section 'over' with Z predicting/uninformative: {sorted(set(over))}", flush=True)


# ---------------------------------------------------------------- C01-2..5: runs
def parent_rule(rule_name):
    def dev(t, j): return ('X', (t - 1, 0)) if j == 0 else ('Y', (t - 1, j - 1))
    def mirror(t, j): return ('Y', (t - 1, t - 1)) if j == t else ('X', (t - 1, j))
    def alt(t, j): return ('X', (t - 1, j)) if (j < t / 2 and j <= t - 1) else ('Y', (t - 1, j - 1))
    return {'dev': dev, 'mirror': mirror, 'alt': alt}[rule_name]


def recurrence_rule(x, y, w, nmax, rule_name='dev', window='block'):
    """graded basis, column (t, j) <-> x^{t-j} y^j, one CGS pass against the window (block: degrees t-2..t;
    full: all previous columns); parent rule dev / mirror / alt / adapt (adapt: admissible product with larger
    beta/||A q_p|| after orthogonalisation)."""
    idx = [(t, j) for t in range(nmax + 1) for j in range(t + 1)]; pos = {c: k for k, c in enumerate(idx)}
    N = len(idx); M = len(x); Q = np.zeros((M, N)); v = np.sqrt(w); Q[:, 0] = v / np.linalg.norm(v)
    start = [t * (t + 1) // 2 for t in range(nmax + 2)]; ops = {'X': x, 'Y': y}
    for k in range(1, N):
        t, j = idx[k]
        W = list(range(start[max(t - 2, 0)], k)) if window == 'block' else list(range(k))
        Qw = Q[:, W]
        if rule_name == 'adapt':
            cands = []
            if j <= t - 1: cands.append(('X', (t - 1, j)))
            if j >= 1: cands.append(('Y', (t - 1, j - 1)))
        else:
            cands = [parent_rule(rule_name)(t, j)]
        best = None
        for op, p in cands:
            u0 = ops[op] * Q[:, pos[p]]; u = u0 - Qw @ (Qw.T @ u0); b = np.linalg.norm(u)
            score = b / np.linalg.norm(u0)
            if best is None or score > best[0]: best = (score, u, b)
        Q[:, k] = best[1] / best[2]
    return Q


def both(x, y, w, nmax, passes=1):
    """copy of l1_both_relations.both (that module runs its experiment at import)"""
    blocks = [(np.sqrt(w) / np.linalg.norm(np.sqrt(w)))[:, None]]
    for n in range(1, nmax + 1):
        P = blocks[-1]
        V = np.hstack([x[:, None] * P, y[:, None] * P])
        Wn = np.hstack(blocks[max(0, n - 2):])
        for _ in range(passes):
            V = V - Wn @ (Wn.T @ V)
        U, s, _ = np.linalg.svd(V, full_matrices=False)
        blocks.append(U[:, :n + 1])
    return np.hstack(blocks)


def loss_at(Q, degs):
    G = Q.T @ Q
    return {n: float(np.abs(G[:Nof(n), :Nof(n)] - np.eye(Nof(n))).max()) for n in degs}


def uz(Q, x, y, degs):
    out = {}
    for n in degs:
        Un, _ = np.linalg.qr(Q[:, :Nof(n)])
        res, _, _ = L.ritz_min(Un.astype(complex), (x + 1j * y), hermitian=False)
        out[n] = U53 / res[0]
    return out


def fmt(d): return " ".join(f"n{n}:{v:.1e}" for n, v in d.items())


def seed11_sets():
    rng = np.random.default_rng(11); M = 1681
    sq = rng.uniform(-1, 1, (M, 2))
    dk = []
    while len(dk) < M:
        p = rng.uniform(-1, 1, 2)
        if p @ p <= 1: dk.append(p)
    tr = []
    while len(tr) < M:
        p = rng.uniform(0, 1, 2)
        if p.sum() <= 1: tr.append(2 * p - 1)
    return sq, np.array(dk), np.array(tr)


def runs():
    sq, dk, tr = seed11_sets(); one = np.ones(len(sq)); degs = (12, 16, 20, 24)
    sets = [('square', sq), ('rotation 0.3', L.rotate(sq, 0.3)), ('rotation pi/4', L.rotate(sq, np.pi / 4)),
            ('disk', dk), ('triangle', tr)]
    print("== C01-2 / C01-3: loss by parent rule (block window, one CGS pass) and dev rule without truncation (full window, one pass)")
    for name, P in sets:
        x, y = P[:, 0].copy(), P[:, 1].copy()
        for rn in ('dev', 'mirror', 'alt', 'adapt'):
            print(f"   {name:14s} {rn:7s} {fmt(loss_at(recurrence_rule(x, y, one, 24, rn), degs))}", flush=True)
        print(f"   {name:14s} {'devfull':7s} {fmt(loss_at(recurrence_rule(x, y, one, 24, 'dev', 'full'), degs))}", flush=True)
        Qlib, _, _ = L.recurrence(x, y, one, 24, win='block', orth='cgs')
        print(f"   {name:14s} {'libBJ':7s} {fmt(loss_at(Qlib, degs))}  (library BJ, consistency check of dev)", flush=True)
    print("== C01-4: BJ loss vs u/rho_Z (u = 2^-53)")
    x, y = sq[:, 0].copy(), sq[:, 1].copy()
    for c in (1.0, 4.0, 8.0):
        w = np.exp(c * x * y); Q, _, _ = L.recurrence(x, y, w, 24, win='block', orth='cgs')
        print(f"   square, weights exp({c:.0f}xy): loss {fmt(loss_at(Q, degs))} | u/rho_Z {fmt(uz(Q, x, y, degs))}", flush=True)
    g = np.random.default_rng(12).standard_normal((1681, 2)); x, y = g[:, 0].copy(), g[:, 1].copy()
    Q, _, _ = L.recurrence(x, y, one, 24, win='block', orth='cgs')
    print(f"   Gaussian cloud: loss {fmt(loss_at(Q, degs))} | u/rho_Z {fmt(uz(Q, x, y, degs))}", flush=True)
    Qb = both(x, y, one, 24)
    print(f"   Gaussian cloud, two-relation 1 pass: loss {fmt(loss_at(Qb, degs))}", flush=True)
    print("== C01-5: two-relation block recurrence vs BJ")
    P, w = L.nodes_tensor_cheb(41); x, y = P[:, 0].copy(), P[:, 1].copy()
    Q, _, _ = L.recurrence(x, y, w, 24, win='block', orth='cgs')
    print(f"   tensor 41^2 BJ:            {fmt(loss_at(Q, degs))}", flush=True)
    print(f"   tensor 41^2 two-rel 1 pass: {fmt(loss_at(both(x, y, w, 24), degs))}", flush=True)
    x, y = tr[:, 0].copy(), tr[:, 1].copy()
    for ps in (1, 2):
        print(f"   triangle two-rel {ps} pass:   {fmt(loss_at(both(x, y, one, 24, ps), degs))}", flush=True)


if __name__ == '__main__':
    print(f"# l1_c01_recon_checks.py {sys.argv[1]} numpy={np.__version__}")
    if sys.argv[1] == 'rule':
        rule(sys.argv[2:])
    else:
        runs()
