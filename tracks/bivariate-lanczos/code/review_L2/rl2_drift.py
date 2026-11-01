"""L2 reconstruction 01, item 3: is the span drift of PD-N?bivariate-lanczos-claude-201 real?
Independent code (rl2_lib only).  MEASURED.

Part A  rot pi/4 (rng(11) square, M = 1681, n = 24):  BJ(=ZN grevlex) + CGS2-all in double and in x87 long double,
        BJ one-pass window (double), mirror + CGS2-all (double, long double); references of S_n:
        R1 Legendre product basis in the unrotated frame, Householder QR in long double (own code);
        R2 Chebyshev product basis, unrotated frame, long double;  R3 = R1 basis, LAPACK QR in double;
        R4 box-frame Chebyshev (developer's pre-registered reference), double.  kappa of every basis.
Part B  triangle (rng(11), M = 1681, n = 20): Koornwinder-Dubiner basis (own Jacobi recurrences) in long double.
Part C  M-dependence: fresh uniform squares rotated by pi/4, M in {1681, 1e4, 1e5}, seeds 1..3, BJ + CGS2-all
        (double), reference R3-type (double LAPACK QR of the unrotated Legendre basis).
Usage: python3 -I rl2_drift.py [A] [B] [C] > logs_L2/drift.log
"""
import sys, os, time, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import rl2_lib as R

LD = R.LD
U = R.U
f64 = np.float64


def ortho_ld(Q):
    W, _ = R.hqr(Q.astype(LD))
    return W


def report_run(tag, Q, refs, x, y, nmax, ns, extra=None):
    W = ortho_ld(Q)
    L = float(np.abs(Q.astype(LD).T @ Q.astype(LD) - np.eye(Q.shape[1], dtype=LD)).max())
    dX, dY = R.defects(W, x, y, nmax)
    nX, nY = float(np.abs(x).max()), float(np.abs(y).max())
    out = dict(run=tag, loss=L)
    for rn, Uo in refs.items():
        ang = R.sin_angles_nested(W, Uo, ns)
        out['sin_' + rn] = ang
    out['thetaLB'] = {n: float(max(dX[:n].max() / (2 * nX), dY[:n].max() / (2 * nY))) for n in ns}
    out['thetaLB_J'] = {n: float(dX[:n].max() / (2 * nX)) for n in ns}
    if extra:
        out.update(extra)
    line = f"  {tag:22s} loss={L:.1e} | " + " ".join(
        f"n={n}: sinR1={out['sin_R1'][n]:.1e} LB={out['thetaLB'][n]:.1e}" for n in ns if n in (12, 16, 18, 20, 22, 24))
    print(line, flush=True)
    print('JSON ' + json.dumps(out), flush=True)
    return W, out


def part_A():
    print("== Part A: rot pi/4, rng(11) square, M = 1681, unit weights, n = 24", flush=True)
    t0 = time.time()
    sq, dk, tr = R.rng11_sets()
    P = R.rotate(sq, np.pi / 4)
    x, y = P[:, 0].copy(), P[:, 1].copy()
    w = np.ones(len(x))
    n = 24
    ns = list(range(2, n + 1, 2))
    # references
    xu, yu = R.unrotated_coords(P, np.pi / 4, LD)
    V1 = R.vander_product(xu, yu, w, n, 'legendre')
    V2 = R.vander_product(xu, yu, w, n, 'cheb')
    xd, yd = R.unrotated_coords(P, np.pi / 4, f64)
    V3 = R.vander_product(xd, yd, w, n, 'legendre')
    bx, by = R.box_coords(P)
    V4 = R.vander_product(bx, by, w, n, 'cheb')
    # monomials in the unrotated frame (for kappa only)
    V5 = np.column_stack([xd ** (t - j) * yd ** j for t in range(n + 1) for j in range(t + 1)])
    V5 = V5 / np.linalg.norm(V5, axis=0)
    for nm, V in (('R1 Legendre unrot', V1), ('R2 Chebyshev unrot', V2), ('R4 Chebyshev box (dev pre-reg)', V4),
                  ('monomial unrot', V5)):
        ks = {s: R.kappa(np.asarray(V[:, :R.Nof(s)], dtype=f64)) for s in (8, 12, 16, 20, 24)}
        print(f"  kappa {nm:32s}: " + " ".join(f"n={s}:{k:.2e}" for s, k in ks.items()), flush=True)
    U1 = R.hqr(V1)[0]
    U2 = R.hqr(V2)[0]
    U3 = np.linalg.qr(V3)[0].astype(LD)
    U4 = np.linalg.qr(V4)[0].astype(LD)
    refs = dict(R1=U1, R2=U2, R3=U3, R4=U4)
    for a, b in (('R1', 'R2'), ('R1', 'R3'), ('R1', 'R4')):
        ang = R.sin_angles_nested(refs[a], refs[b], ns)
        print(f"  reference angle {a} vs {b}: " + " ".join(f"{s}:{v:.1e}" for s, v in ang.items()), flush=True)
    print(f"  (references built in {time.time() - t0:.0f}s)", flush=True)
    res = {}
    for tag, rule, orth, dt in (('bj cgs2all f64', 'bj', 'cgs2all', f64),
                                ('bj cgs2all LD', 'bj', 'cgs2all', LD),
                                ('bj cgs1win f64', 'bj', 'cgs1win', f64),
                                ('bj cgs2win f64', 'bj', 'cgs2win', f64),
                                ('mirror cgs2all f64', 'mirror', 'cgs2all', f64),
                                ('mirror cgs2all LD', 'mirror', 'cgs2all', LD)):
        t1 = time.time()
        Q = R.recur(x, y, w, n, rule=rule, orth=orth, dtype=dt)
        W, out = report_run(tag, Q, refs, x, y, n, ns, extra=dict(time=time.time() - t1))
        res[tag] = W
    # double vs long-double runs of the same algorithm (reference-free)
    for a, b in (('bj cgs2all f64', 'bj cgs2all LD'), ('bj cgs1win f64', 'bj cgs2all f64'),
                 ('mirror cgs2all f64', 'mirror cgs2all LD')):
        ang = R.sin_angles_nested(res[a], res[b], ns)
        print(f"  span angle [{a}] vs [{b}]: " + " ".join(f"{s}:{v:.1e}" for s, v in ang.items()), flush=True)
    print(f"# Part A done in {time.time() - t0:.0f}s", flush=True)


def part_B():
    print("== Part B: triangle, rng(11), M = 1681, n = 20", flush=True)
    t0 = time.time()
    sq, dk, tr = R.rng11_sets()
    P = tr
    x, y = P[:, 0].copy(), P[:, 1].copy()
    w = np.ones(len(x))
    n = 20
    ns = list(range(2, n + 1, 2))
    V = R.koornwinder_vander(P, w, n, LD)
    print("  kappa Koornwinder: " + " ".join(f"n={s}:{R.kappa(np.asarray(V[:, :R.Nof(s)], dtype=f64)):.2e}"
                                             for s in (8, 12, 16, 20)), flush=True)
    bx, by = R.box_coords(P)
    Vb = R.vander_product(bx, by, w, n, 'legendre')
    print("  kappa box Legendre: " + " ".join(f"n={s}:{R.kappa(Vb[:, :R.Nof(s)]):.2e}" for s in (8, 12, 16, 20)),
          flush=True)
    U1 = R.hqr(V)[0]
    U3 = np.linalg.qr(np.asarray(V, dtype=f64))[0].astype(LD)
    refs = dict(R1=U1, R3=U3)
    ang = R.sin_angles_nested(U1, U3, ns)
    print("  reference angle KD-LD vs KD-f64: " + " ".join(f"{s}:{v:.1e}" for s, v in ang.items()), flush=True)
    res = {}
    for tag, rule, orth, dt in (('bj cgs2all f64', 'bj', 'cgs2all', f64), ('bj cgs2all LD', 'bj', 'cgs2all', LD),
                                ('bj cgs2win f64', 'bj', 'cgs2win', f64)):
        t1 = time.time()
        Q = R.recur(x, y, w, n, rule=rule, orth=orth, dtype=dt)
        W, out = report_run(tag, Q, refs, x, y, n, ns, extra=dict(time=time.time() - t1))
        res[tag] = W
    ang = R.sin_angles_nested(res['bj cgs2all f64'], res['bj cgs2all LD'], ns)
    print("  span angle [bj cgs2all f64] vs [bj cgs2all LD]: " + " ".join(f"{s}:{v:.1e}" for s, v in ang.items()),
          flush=True)
    print(f"# Part B done in {time.time() - t0:.0f}s", flush=True)


def part_C():
    print("== Part C: M-dependence, fresh uniform squares rotated by pi/4, n = 24, BJ + CGS2-all (double)", flush=True)
    n = 24
    for M in (1681, 10000, 100000):
        for seed in ((1, 2, 3) if M <= 10000 else (1, 2)):
            t0 = time.time()
            P = R.rotate(R.fresh_square(M, seed), np.pi / 4)
            x, y = P[:, 0].copy(), P[:, 1].copy()
            w = np.ones(M)
            Q = R.recur(x, y, w, n, rule='bj', orth='cgs2all', dtype=f64)
            xd, yd = R.unrotated_coords(P, np.pi / 4, f64)
            V = R.vander_product(xd, yd, w, n, 'legendre')
            kap = R.kappa(V)
            Uo = np.linalg.qr(V)[0]
            Wd = np.linalg.qr(Q)[0]
            ang = R.sin_angles_nested(Wd, Uo, [16, 20, 22, 24])
            dX, dY = R.defects(Wd, x, y, n)
            lb = float(max(dX.max() / (2 * np.abs(x).max()), dY.max() / (2 * np.abs(y).max())))
            L = float(np.abs(Q.T @ Q - np.eye(Q.shape[1])).max())
            print(f"  M={M:6d} seed={seed}: loss={L:.1e} kappa(Leg,unrot,n=24)={kap:.2e} (u*kappa={U * kap:.1e}) "
                  f"sin: " + " ".join(f"n={s}:{v:.1e}" for s, v in ang.items()) + f" thetaLB(24)={lb:.1e} "
                  f"({time.time() - t0:.0f}s)", flush=True)
            print('JSON ' + json.dumps(dict(part='C', M=M, seed=seed, loss=L, kappa=kap, sin=ang, thetaLB=lb)),
                  flush=True)
            del Q, V, Uo, Wd


if __name__ == '__main__':
    print(f"# rl2_drift.py numpy={np.__version__} u=2^-53 u_LD={np.finfo(LD).epsneg:.2e}", flush=True)
    parts = sys.argv[1:] or ['A', 'B', 'C']
    for p in parts:
        {'A': part_A, 'B': part_B, 'C': part_C}[p]()
