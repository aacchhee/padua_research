"""Claude audit-01, B1 sub-audit: high-precision SANITY scan of record 93 (supporting only).

Literal source Ldiag taper (orf2d.py taper/make_lines at programme pin 9bd14a6d):
  eps_j(sigma) = exp(-sigma (sqrt m - sqrt j)), j=1..m;  a_j = 2 + sqrt(2) eps_j;
  near order = j-th degree gets eps_j; far order = reversed.
For each t=2..T=m-1 we evaluate the scale-free indicator
  phi_t(sigma) = s_{2t+1}(G_t) / s_1(G_t),
G_t = weighted generator of R_t = (I-P_Wt-P_Wt-1)(W_{t-1}+W_t+xW_t+yW_t)/ell_{t+1}.
phi_t(sigma) = 0  <=>  rank R_t < 2t+1  <=>  record-91 p_t(a(sigma)) = 0.
Also reported: s_{2t+2}/s_1 (record-90 upper bound predicts ~0 at working precision),
and the constraint check (smallest canonical cosine between ker and W_{t+1}).
mpmath floating point at high precision: this is MEASURED-type support, not a proof,
and it cannot locate or exclude isolated zeros between grid points.
"""
import json, sys, time, random, math
from fractions import Fraction as Fr
import mpmath as mp

mp.mp.dps = 45


def monos(j):
    return [(d - i, i) for d in range(j + 1) for i in range(d + 1)]


def N(j):
    return (j + 1) * (j + 2) // 2


def blocks(nodes, sw, a, T):
    """weighted-orthonormal block bases W_0..W_{T+1} via QR of the graded evaluated basis"""
    M = len(nodes)
    cols = []
    for (u, v) in monos(T + 1):
        d = u + v
        col = []
        for i, (x, y) in enumerate(nodes):
            pi = mp.mpf(1)
            for r in range(d):
                pi *= (x + y - a[r])
            col.append(sw[i] * x ** u * y ** v / pi)
        cols.append(col)
    A = mp.matrix(M, len(cols))
    for j, c in enumerate(cols):
        for i in range(M):
            A[i, j] = c[i]
    Q, R = mp.qr(A, mode='skinny')
    # verify full column rank (diagonal of R not tiny)
    rdiag = min(abs(R[j, j]) for j in range(R.cols)) / max(abs(R[j, j]) for j in range(R.cols))
    B = {}
    for j in range(T + 2):
        idx = list(range(N(j - 1) if j else 0, N(j)))
        B[j] = Q[:, idx[0]:idx[-1] + 1]
    return B, rdiag


def svals(G):
    H = G.T * G
    ev = mp.eigsy(H, eigvals_only=True)
    ev = sorted([max(e, mp.mpf(0)) for e in ev], reverse=True)
    return [mp.sqrt(e) for e in ev]


def scan_point(nodes, sw, a, T):
    M = len(nodes)
    B, rdiag = blocks(nodes, sw, a, T)
    out = {"basis_rdiag_ratio": float(rdiag)}
    xs = [x for x, y in nodes]
    ys = [y for x, y in nodes]
    for t in range(2, T + 1):
        ell = [x + y - a[t] for x, y in nodes]
        parts = [B[t - 1], B[t]]
        Xt = B[t].copy()
        Yt = B[t].copy()
        for i in range(M):
            for j in range(Xt.cols):
                Xt[i, j] = xs[i] * B[t][i, j]
                Yt[i, j] = ys[i] * B[t][i, j]
        parts += [Xt, Yt]
        ncol = sum(p.cols for p in parts)
        C = mp.matrix(M, ncol)
        c0 = 0
        for p in parts:
            for j in range(p.cols):
                for i in range(M):
                    C[i, c0 + j] = p[i, j] / ell[i]
            c0 += p.cols
        Pj = B[t] * B[t].T + B[t - 1] * B[t - 1].T
        G = C - Pj * C
        s = svals(G)
        r = 2 * t + 1
        out[t] = {"phi": float(s[r - 1] / s[0]), "next": float(s[r] / s[0]) if len(s) > r else 0.0}
    return out


def run_config(name, nodes_q, w_q, m, sigmas):
    T = m - 1
    nodes = [(mp.mpf(x.numerator) / x.denominator, mp.mpf(y.numerator) / y.denominator) for x, y in nodes_q]
    sw = [mp.sqrt(mp.mpf(v.numerator) / v.denominator) for v in w_q]
    res = {"name": name, "m": m, "M": len(nodes), "orders": {}}
    for order in ("near", "far"):
        rows = []
        for sg in sigmas:
            sg = mp.mpf(sg)
            eps = [mp.exp(-sg * (mp.sqrt(m) - mp.sqrt(j))) for j in range(1, m + 1)]
            if order == "far":
                eps = eps[::-1]
            a = [2 + mp.sqrt(2) * e for e in eps]
            pt = scan_point(nodes, sw, a, T)
            rows.append({"sigma": float(sg), "eps_min": float(min(eps)), **{str(k): v for k, v in pt.items()}})
        summ = {}
        for t in range(2, T + 1):
            phis = [rw[str(t)]["phi"] for rw in rows]
            nxt = [rw[str(t)]["next"] for rw in rows]
            imin = min(range(len(phis)), key=lambda i: phis[i])
            summ[t] = {"min_phi": phis[imin], "argmin_sigma": rows[imin]["sigma"],
                       "phi_at_0": phis[0], "phi_at_max_sigma": phis[-1], "max_next": max(nxt)}
        res["orders"][order] = {"summary": summ, "rows": rows}
    return res


if __name__ == "__main__":
    t0 = time.time()
    rng = random.Random(931)
    out = []
    # m=4 (T=3): random interior nodes, and a tensor grid containing the corner (1,1)
    m = 4
    nodes = sorted({(Fr(rng.randint(-97, 96), 97), Fr(rng.randint(-97, 96), 97)) for _ in range(N(m) + 2)})
    w = [Fr(rng.randint(1, 9), rng.randint(1, 5)) for _ in nodes]
    sig4 = [0, 1e-6, 1e-3] + [0.05 * k for k in range(1, 201)] + [12.5, 15, 20]
    out.append(run_config("m4 random interior nodes", nodes, w, m, sig4))
    g = [Fr(-1), Fr(-1, 2), Fr(1, 5), Fr(2, 3), Fr(1)]
    nodes = [(x, y) for x in g for y in g]
    w = [Fr(1 + (i % 3), 1 + (i % 2)) for i in range(len(nodes))]
    out.append(run_config("m4 tensor grid with corner (1,1)", nodes, w, m, [0, 1e-6, 1e-3] + [0.1 * k for k in range(1, 101)] + [12.5, 15]))
    # m=6 (T=5): random interior nodes, coarser grid
    m = 6
    nodes = sorted({(Fr(rng.randint(-97, 96), 97), Fr(rng.randint(-97, 96), 97)) for _ in range(N(m) + 2)})
    w = [Fr(rng.randint(1, 9), rng.randint(1, 5)) for _ in nodes]
    out.append(run_config("m6 random interior nodes", nodes, w, m, [0, 1e-6, 1e-3] + [0.2 * k for k in range(1, 31)] + [8, 10]))
    for r in out:
        for o, d in r["orders"].items():
            print(json.dumps({"name": r["name"], "order": o, "summary": d["summary"]}), flush=True)
    path = sys.argv[1] if len(sys.argv) > 1 else "b1_taper_scan.json"
    with open(path, "w") as fh:
        json.dump({"configs": out, "dps": mp.mp.dps, "total_seconds": round(time.time() - t0, 1),
                   "mpmath": mp.__version__, "python": sys.version}, fh, indent=1)
    print("wrote", path, "seconds", round(time.time() - t0, 1))
