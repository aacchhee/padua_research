"""Local rigorous certificate for an explicit Delsarte function of int(2O) (record -07, part (L)).

Input: the third-party DGOV ancillary evaluator `octa_double.func.cpp`
(arXiv:1510.02331v3, anc/), NOT committed; pass its path. Its SHA-256 is checked.

Definitions (exact):
  P(x) = sum_{i,j,k} c_ijk s1^i s2^j s3^k,  s_m = x1^(2m)+x2^(2m)+x3^(2m),
         with c_ijk the decimal literals of the file read as exact rationals;
  f(x) = P(x) exp(-pi |x|^2);   fhat(u) = G(u) exp(-pi |u|^2)   (fhat = int f e^{-2 pi i u.x}),
  G computed exactly in Q[1/pi] from 1-D identities FT[x^n e^{-pi x^2}] = (i/2pi)^n D^n e^{-pi u^2}.
Claims checked (rigorous, see below):
  (G)  G(u) >= 0 for all u in R^3;
  (P)  P(x) <= 0 for all x with |x|_1 >= alpha;
  (V)  gamma_1 := 6 G(0) / (alpha^3 P(0)) - 1, enclosed with arb balls.
Then phi(xi) = f(alpha xi/2)/f(0) is Delsarte-admissible for int(2O) (record -07 (a)), and
(3/4) int phi - 1 = gamma_1.

Method. Both P and G are polynomials in y = (x1^2, x2^2, x3^2) of degree 13, B3-invariant
(P by construction; G is checked to be symmetric exactly). So it suffices to work on the
fundamental domain F = {0 <= x1 <= x2 <= x3}. Boxes in x with dyadic endpoints (bisection of
[0,R]; widths >= 2^-24 never failed) map to y-boxes M +- R exactly. On each y-box the
polynomial is Taylor-shifted to the centre M (exact identity p(M+h) = sum_b D_b h^b) and
enclosed by D_0 +- (sum_{b != 0} |D_b| R^b + E), where E = 2^-46 * sum_b Dabs_b R^b bounds the
floating-point error of the computed shift (each D_b is formed in three stages of <= 14
products of rounded binom(k,j) m^(k-j); total relative error < 60 u of the absolute-value
computation Dabs; 2^-46 = 128 u). All powers m^e and R^k are formed by explicit repeated
multiplication (no library pow), so the rounding count above is literal.
Coefficients (revision of 2026-11-13, audit-01 A2): each exact coefficient c (a rational for P,
an element of Q[1/pi] for G, evaluated as an Arb ball at 256 bits) is stored as a double c~ together
with a certified bound e >= |c - c~| (exact Fraction arithmetic for P; Arb abs_upper for G,
rounded up). The polynomial with coefficients c~ is enclosed as above, and the coefficient error
is added as sum_a e_a (M+R)^a >= |sum_a (c_a - c~_a) y^a| for y in the box (y >= 0). No
correct-rounding assumption on the coefficients is used.
Tails: for rho = |x|_inf >= R the point x = rho*y has y on the face y3 = 1, 0 <= y1 <= y2 <= 1,
and P(x) = sum_k t^k P_2k(y) with t = rho^2. A 2-D branch and bound on the face encloses every
homogeneous part P_2k and requires all coefficients of the shifted univariate polynomial
p(R^2 + s) to be <= 0 (for P) or >= 0 (for G), which gives the sign for all s >= 0.
Usage: python3 -B gamma_certificate.py --anc PATH/octa_double.func.cpp --alpha 1.001 --R 4 --RG 4
        --out out.json [--leaves leaves.npz]
"""
import argparse, hashlib, json, re, sys, time
from collections import defaultdict
from fractions import Fraction
import numpy as np

ANC_SHA = "034a1aea4fafbf29743bded0812723ac8c9cf95274225213578145d016a7bc47"


# ---------------------------------------------------------------- exact data
def read_coeffs(path):
    src = open(path).read()
    C = {}
    for m in re.finditer(r"static const double c_(\d+)_(\d+)_(\d+) = ([-0-9.eE+]+);", src):
        C[tuple(map(int, m.groups()[:3]))] = Fraction(m.group(4))
    return C, hashlib.sha256(src.encode()).hexdigest()


def poly_mul(p, q):
    r = defaultdict(Fraction)
    for k1, v1 in p.items():
        for k2, v2 in q.items():
            r[(k1[0] + k2[0], k1[1] + k2[1], k1[2] + k2[2])] += v1 * v2
    return r


def P_in_y(C):
    """P as polynomial in y = x^2: dict a -> Fraction."""
    s = {1: {(1, 0, 0): 1, (0, 1, 0): 1, (0, 0, 1): 1},
         2: {(2, 0, 0): 1, (0, 2, 0): 1, (0, 0, 2): 1},
         3: {(3, 0, 0): 1, (0, 3, 0): 1, (0, 0, 3): 1}}
    cache = {}

    def pw(t, e):
        if (t, e) not in cache:
            cache[(t, e)] = {(0, 0, 0): Fraction(1)} if e == 0 else poly_mul(pw(t, e - 1), s[t])
        return cache[(t, e)]

    P = defaultdict(Fraction)
    for (i, j, k), c in C.items():
        for key, v in poly_mul(poly_mul(pw(1, i), pw(2, j)), pw(3, k)).items():
            P[key] += c * v
    return {k: v for k, v in P.items() if v != 0}


def T_tables(nmax):
    """T[a][j] = {e: q}: coefficient of u^(2j) in FT[x^(2a) e^{-pi x^2}] / e^{-pi u^2}
    equals sum_e q * pi^e (exact)."""
    h = [{0: {0: Fraction(1)}}]          # h_n: k -> {pi-exponent: q}
    for n in range(2 * nmax):
        hn, nxt = h[-1], defaultdict(lambda: defaultdict(Fraction))
        for k, d in hn.items():
            for e, q in d.items():
                if k >= 1:
                    nxt[k - 1][e] += k * q          # derivative
                nxt[k + 1][e + 1] += -2 * q          # -2 pi u h_n
        h.append({k: dict(d) for k, d in nxt.items()})
    T = {}
    for a in range(nmax + 1):
        T[a] = {}
        sgn = Fraction((-1) ** a, 4 ** a)            # (i/2pi)^(2a) = (-1)^a 2^(-2a) pi^(-2a)
        for k, d in h[2 * a].items():
            assert k % 2 == 0
            T[a][k // 2] = {e - 2 * a: sgn * q for e, q in d.items() if q != 0}
    return T


def G_in_y(P, T):
    G = defaultdict(lambda: defaultdict(Fraction))
    for a, p in P.items():
        for j1, d1 in T[a[0]].items():
            for j2, d2 in T[a[1]].items():
                for j3, d3 in T[a[2]].items():
                    for e1, q1 in d1.items():
                        for e2, q2 in d2.items():
                            for e3, q3 in d3.items():
                                G[(j1, j2, j3)][e1 + e2 + e3] += p * q1 * q2 * q3
    return {k: {e: q for e, q in d.items() if q != 0} for k, d in G.items()}


def pi_poly_to_mp(d, mp):
    return sum(mp.mpf(q.numerator) / q.denominator * mp.pi ** e for e, q in d.items())


# ---------------------------------------------------------------- float machinery
# Rigorous error budget for the Taylor-shift form (see module docstring): every computed
# shifted coefficient D_beta is a sum of at most 14^3 products formed in three stages of at
# most 14 terms, of entries binom(k,j) m^(k-j) computed with at most 14 roundings; its error is
# at most 60 u * Dabs_beta, Dabs = same computation on absolute values; we use 2^-46 > 128 u.
GAMMA = 2.0 ** -46
DEG = 13
def _binom_table():
    from math import comb
    return np.array([[float(comb(k, j)) if k >= j else 0.0 for k in range(DEG + 1)]
                     for j in range(DEG + 1)])


BINOM = _binom_table()


def tensor(coef):
    T = np.zeros((DEG + 1,) * 3)
    for a, v in coef.items():
        T[a] = v
    return T


def powers(m):
    """(nb,) -> (nb, 14): m^e by repeated multiplication (e-1 roundings for e >= 2)."""
    out = np.ones((len(m), DEG + 1))
    for e in range(1, DEG + 1):
        out[:, e] = out[:, e - 1] * m
    return out


def shift_matrices(m):
    """m: (nb,) >= 0. Returns (nb, 14, 14) with B[j,k] = binom(k,j) m^(k-j)."""
    k = np.arange(DEG + 1)
    e = k[None, :] - k[:, None]                         # k - j
    pw_tab = powers(m)
    pw = np.where(e >= 0, pw_tab[:, np.maximum(e, 0)], 0.0)
    return BINOM[None] * pw


def _shift(T, B, axis):
    """Apply per-box shift matrices B (nb,14,14) along tensor axis (1-based after batch)."""
    T = np.moveaxis(T, axis, -1)                     # (nb, ..., k)
    out = np.einsum("b...k,bjk->b...j", T, B, optimize=True)
    return np.moveaxis(out, -1, axis)


def taylor_enclose(Cten, Cabs, M, R, batch=4000, Eten=None):
    """Rigorous enclosure, over the boxes M +- R in y-space (rows, y >= 0), of the exact
    y-polynomial whose coefficients differ from the tensor Cten by at most Eten (>= 0)."""
    d = Cten.ndim
    nb = len(M); lo = np.empty(nb); hi = np.empty(nb)
    k = np.arange(DEG + 1)
    for s0 in range(0, nb, batch):
        sl = slice(s0, s0 + batch); n = len(M[sl])
        D = np.broadcast_to(Cten, (n,) + Cten.shape).copy()
        Da = np.broadcast_to(Cabs, (n,) + Cten.shape).copy()
        for i in range(d):
            Bi = shift_matrices(M[sl, i])
            D = _shift(D, Bi, i + 1)
            Da = _shift(Da, np.abs(Bi), i + 1)
        W = np.ones((n,) + (1,) * d)
        V = np.ones((n,) + (1,) * d)                  # (M+R)^a for the coefficient error
        for i in range(d):
            shp = [n] + [1] * d; shp[i + 1] = DEG + 1
            W = W * powers(R[sl, i]).reshape(shp)
            V = V * powers(M[sl, i] + R[sl, i]).reshape(shp)
        axes = tuple(range(1, d + 1))
        D0 = D[(slice(None),) + (0,) * d]
        S = (np.abs(D) * W).sum(axes) - np.abs(D0)
        E = (GAMMA * Da * W).sum(axes)
        if Eten is not None:                          # certified coefficient-conversion error
            E = E + (Eten[None] * V).sum(axes)
        tot = (S + E) * (1 + 2.0 ** -40) + 1e-300
        lo[sl] = D0 - tot
        hi[sl] = D0 + tot
    return lo, hi


def xbox_to_y(XL, XU):
    YL, YU = XL * XL, XU * XU        # exact for dyadic endpoints with <= 26 significant bits
    M = 0.5 * (YL + YU)              # exact (dyadic)
    R = 0.5 * (YU - YL)              # exact (dyadic)
    return M, R


def in_F(L, U):
    return (np.maximum(L[:, 0], L[:, 1]) <= U[:, 1]) & (np.max(L, axis=1) <= U[:, 2])


def bnb(Cten, want, R, region_alpha=None, max_boxes=20_000_000, min_width=2.0 ** -24, log=None,
        Eten=None):
    """Certify poly <= 0 (want='hi') or >= 0 (want='lo') on F cap [0,R]^3 (cap |x|_1 >= alpha)."""
    Cabs = np.abs(Cten)
    L = np.zeros((1, 3)); U = np.full((1, 3), float(R))
    certified = 0; processed = 0; failures = []; leaves = []; it = 0; min_leaf = float(R)
    while len(L):
        keep = in_F(L, U)
        if region_alpha is not None:
            keep &= U.sum(1) >= region_alpha
        L, U = L[keep], U[keep]
        if not len(L):
            break
        M, Ry = xbox_to_y(L, U)
        assert (U - L).min() >= min_width       # dyadic endpoints with <= 26 bits: exact squares
        lo, hi = taylor_enclose(Cten, Cabs, M, Ry, Eten=Eten)
        ok = (hi <= 0) if want == "hi" else (lo >= 0)
        if ok.any():
            min_leaf = min(min_leaf, float((U[ok] - L[ok]).min()))
        certified += int(ok.sum()); processed += len(L)
        leaves.append(np.hstack([L[ok], U[ok]]))
        L, U = L[~ok], U[~ok]
        small = (U - L).max(1) < min_width
        if small.any():
            failures += np.hstack([L[small], U[small]]).tolist()
            L, U = L[~small], U[~small]
        if processed > max_boxes:
            failures.append("max_boxes exceeded"); break
        idx = np.arange(len(L)); ax = np.argmax(U - L, axis=1)
        mid = 0.5 * (L[idx, ax] + U[idx, ax])
        L2, U2 = L.copy(), U.copy()
        U[idx, ax] = mid; L2[idx, ax] = mid
        L = np.vstack([L, L2]); U = np.vstack([U, U2])
        it += 1
        if log and it % 5 == 0:
            log(f"  {want}: iter {it}, processed {processed}, certified {certified}, open {len(L)}")
    return ({"processed": processed, "certified": certified, "failures": failures[:20],
             "n_failures": len(failures), "min_leaf_width": min_leaf, "iterations": it},
            np.vstack(leaves) if leaves else np.zeros((0, 6)))


def tail(Cten, sign, R, log=None, min_width=2.0 ** -24, max_boxes=2_000_000, Eten=None):
    """For rho = |x|_inf >= R, x = rho*y with y on the face y3 = 1, 0 <= y1 <= y2 <= 1:
    P(x) = sum_k t^k P_2k(y), t = rho^2. On each face box enclose every P_2k (Taylor form in
    (y1^2, y2^2); y3 = 1 exactly), shift t = R^2 + s and require all shifted coefficients
    <= 0 (sign=+1) or >= 0 (sign=-1); then the sign holds for all t >= R^2."""
    t0 = float(R) ** 2
    parts = []; perrs = []                      # P_2k restricted to y3 = 1: 2-D tensors
    E3 = np.zeros_like(Cten) if Eten is None else Eten
    for k in range(DEG + 1):
        Tk = np.zeros((DEG + 1, DEG + 1)); Ek = np.zeros((DEG + 1, DEG + 1))
        for a1 in range(DEG + 1):
            for a2 in range(DEG + 1 - a1):
                a3 = k - a1 - a2
                if 0 <= a3 <= DEG:
                    Tk[a1, a2] = Cten[a1, a2, a3]
                    Ek[a1, a2] = E3[a1, a2, a3]
        parts.append(Tk); perrs.append(Ek)
    L = np.array([[0.0, 0.0]]); U = np.array([[1.0, 1.0]])
    n_ok = 0; n_proc = 0
    from math import comb
    shiftB = np.array([[comb(k, j) * t0 ** (k - j) if k >= j else 0.0 for k in range(DEG + 1)]
                       for j in range(DEG + 1)])
    while len(L):
        keep = (L[:, 0] <= U[:, 1])
        L, U = L[keep], U[keep]
        if not len(L):
            break
        M, Ry = xbox_to_y(L, U)
        enc = [taylor_enclose(Tk, np.abs(Tk), M, Ry, Eten=Ek) for Tk, Ek in zip(parts, perrs)]
        lo = np.stack([e[0] for e in enc], 1); hi = np.stack([e[1] for e in enc], 1)
        if sign > 0:   # upper bounds of b_j = sum_k binom(k,j) t0^(k-j) a_k, coefficients >= 0
            ok = np.all(hi @ shiftB.T + 2.0 ** -40 * (np.abs(hi) @ shiftB.T) <= 0, axis=1)
        else:
            ok = np.all(lo @ shiftB.T - 2.0 ** -40 * (np.abs(lo) @ shiftB.T) >= 0, axis=1)
        n_ok += int(ok.sum()); n_proc += len(L)
        L, U = L[~ok], U[~ok]
        if len(L) and ((U - L).max() < min_width or n_proc > max_boxes):
            return {"ok": False, "processed": n_proc, "open": len(L),
                    "open_sample": np.hstack([L, U])[:: max(1, len(L) // 10)].tolist()}
        idx = np.arange(len(L)); ax = np.argmax(U - L, axis=1)
        mid = 0.5 * (L[idx, ax] + U[idx, ax])
        L2, U2 = L.copy(), U.copy()
        U[idx, ax] = mid; L2[idx, ax] = mid
        L = np.vstack([L, L2]); U = np.vstack([U, U2])
    return {"ok": True, "processed": n_proc, "certified": n_ok, "t0": t0}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--anc", required=True)
    ap.add_argument("--alpha", default="1.001")
    ap.add_argument("--R", default="4", help="box radius (|x|_inf) for P; tail beyond")
    ap.add_argument("--RG", default="4", help="box radius for G; tail beyond")
    ap.add_argument("--out", required=True)
    ap.add_argument("--leaves", default=None)
    a = ap.parse_args()
    t0 = time.time()
    log = lambda s: print(f"[{time.time()-t0:7.1f}s] {s}", flush=True)
    C, sha = read_coeffs(a.anc)
    log(f"coefficients {len(C)}, sha256 {sha} ({'MATCH' if sha == ANC_SHA else 'MISMATCH'})")
    P = P_in_y(C)
    T = T_tables(13)
    G = G_in_y(P, T)
    # exact symmetry of G (B3 invariance)
    for k, d in G.items():
        for perm in [(1, 0, 2), (0, 2, 1)]:
            kk = tuple(k[p] for p in perm)
            assert G.get(kk) == d, "G not symmetric"
    from flint import arb, ctx, fmpq
    ctx.prec = 256
    pi_b = arb.pi()
    up = lambda v: float(v) * (1 + 2.0 ** -50) + 1e-300     # round a nonnegative bound upward
    Pf, Pe, Gf, Ge = {}, {}, {}, {}
    for k, v in P.items():                       # exact rational -> double, exact error
        Pf[k] = float(v); Pe[k] = up(abs(v - Fraction(Pf[k])))
    for k, d in G.items():                       # Q[1/pi] -> Arb ball -> double + certified error
        b = sum(arb(fmpq(q.numerator, q.denominator)) * pi_b ** e for e, q in d.items())
        Gf[k] = float(b.mid())
        Ge[k] = up((b - arb(Fraction(Gf[k]).numerator) / arb(Fraction(Gf[k]).denominator)).abs_upper())
    # exact identity G_26 = -P_26
    for k, v in P.items():
        if sum(k) == 13:
            assert G[k] == {0: -v}, "top-degree identity failed"
    log(f"P terms {len(P)}, G terms {len(G)}; G symmetric; G_26 = -P_26 exactly")
    Pt, Gt = tensor(Pf), tensor(Gf)
    PE, GE = tensor(Pe), tensor(Ge)
    R = Fraction(a.R)
    RG = Fraction(a.RG)
    alpha = Fraction(a.alpha)
    res = {"anc_sha256": sha, "anc_sha_expected": ANC_SHA, "alpha": str(alpha), "R": str(R),
           "script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
           "python": sys.version.split()[0], "numpy": np.__version__,
           "max_coef_err_P": max(Pe.values()), "max_coef_err_G": max(Ge.values())}
    # tails
    res["RG"] = str(RG)
    res["tail_P"] = tail(Pt, +1, float(R), Eten=PE)
    res["tail_G"] = tail(Gt, -1, float(RG), Eten=GE)
    log(f"tails: P {res['tail_P']}, G {res['tail_G']}")
    # boxes
    assert Fraction(float(alpha)) <= alpha       # l1 discard threshold rounds in the safe direction
    rP, leavesP = bnb(Pt, "hi", float(R), region_alpha=float(alpha), log=log, Eten=PE)
    log(f"P <= 0 on |x|_1 >= alpha: {rP['processed']} boxes, certified {rP['certified']}, failures {rP['n_failures']}")
    rG, leavesG = bnb(Gt, "lo", float(RG), log=log, Eten=GE)
    log(f"G >= 0: {rG['processed']} boxes, certified {rG['certified']}, failures {rG['n_failures']}")
    res["boxes_P"], res["boxes_G"] = rP, rG
    # value with arb
    pi = pi_b
    G0 = sum(arb(fmpq(q.numerator, q.denominator)) * pi ** e for e, q in G[(0, 0, 0)].items())
    P0 = arb(fmpq(P[(0, 0, 0)].numerator, P[(0, 0, 0)].denominator))
    al = arb(fmpq(alpha.numerator, alpha.denominator))
    gam = 6 * G0 / (al ** 3 * P0) - 1
    res["P0"] = str(P0); res["G0"] = str(G0); res["gamma1"] = str(gam)
    res["gamma1_lower"] = str(gam.lower())
    res["gamma1_gt_1_36"] = bool(gam > arb(fmpq(1, 36)))
    res["verdict"] = ("PASS" if res["tail_P"]["ok"] and res["tail_G"]["ok"] and rP["n_failures"] == 0
                      and rG["n_failures"] == 0 and sha == ANC_SHA else "FAIL")
    res["seconds"] = round(time.time() - t0, 1)
    log(f"gamma1 = {gam}; > 1/36: {res['gamma1_gt_1_36']}; verdict {res['verdict']}")
    json.dump(res, open(a.out, "w"), indent=1)
    if a.leaves:
        np.savez_compressed(a.leaves, P=leavesP, G=leavesG, alpha=float(alpha), R=float(R))


if __name__ == "__main__":
    main()
