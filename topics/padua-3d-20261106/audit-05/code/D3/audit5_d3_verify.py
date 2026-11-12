"""Audit-05 (Claude) independent verifier for the D3 certificate.

Imports no repository code.  Reads only the certificate JSON.  Formulation
differs from the producer: the 56 cubature equations are written in the
tensor Chebyshev basis T_a(x)T_b(y)T_c(z), |(a,b,c)|<=5, with exact moments
delta_{(a,b,c),0}; the preconditioner is this script's own mpmath inverse of
the exact center Jacobian, rounded to dyadics; all accepting predicates are
exact rational/integer comparisons (Fraction endpoints, no rounding at all).
Rank transfer uses the exact inverse of the Chebyshev-basis cubic matrix at
the center plus an exact whole-box perturbation bound.
Failures raise SystemExit (not assert), so -O cannot disable them.
Usage: python -I audit5_d3_verify.py CERT.json OUT.json
"""
import hashlib
import itertools
import json
import math
import sys
import time
from fractions import Fraction as Fr


def req(cond, msg):
    if not cond:
        raise SystemExit("FAIL: " + msg)


t0 = time.monotonic()
cert_path, out_path = sys.argv[1], sys.argv[2]
raw = open(cert_path, 'rb').read()
cert = json.loads(raw)
out = {"certificate_sha256": hashlib.sha256(raw).hexdigest(),
       "certificate_bytes": len(raw),
       "python": sys.version.split()[0], "optimize_flag": sys.flags.optimize}

# ---------------------------------------------------------------- decode
req(set(cert) == {"schema", "center_bits", "radius_bits",
                  "center_numerators", "active"}, "unexpected keys")
req(cert["schema"] == "fd3-dyadic-v1", "schema")
CB, RB = cert["center_bits"], cert["radius_bits"]
req(CB == 180 and RB == 100, "bits")
strs = cert["center_numerators"]
req(len(strs) == 80 and all(isinstance(s, str) and str(int(s)) == s
                            for s in strs), "numerators")
act = cert["active"]
req(len(act) == 56 and all(type(i) is int for i in act), "active ints")
req(act == sorted(set(act)) and 0 <= act[0] and act[-1] < 80, "active set")
N = 20
c = [Fr(int(s), 2 ** CB) for s in strs]
r = Fr(1, 2 ** RB)
actset = set(act)
fixed = [i for i in range(80) if i not in actset]
out["fixed_indices"] = fixed
out["all_weights_active"] = all(60 + j in actset for j in range(N))
box = [(c[i] - r, c[i] + r) if i in actset else (c[i], c[i])
       for i in range(80)]

# ---------------------------------------------------------- geometry checks
req(all(-1 < lo and hi < 1 for lo, hi in box[:60]), "open cube")
req(all(lo > 0 for lo, hi in box[60:]), "positive weights")
for i, j in itertools.combinations(range(N), 2):
    req(any(box[3*i+d][1] < box[3*j+d][0] or box[3*j+d][1] < box[3*i+d][0]
            for d in range(3)), "distinct boxes %d %d" % (i, j))
minw = min(lo for lo, hi in box[60:])
maxx = max(max(-lo, hi) for lo, hi in box[:60])
out["min_weight_lower_ge_47e-4"] = minw > Fr(47, 10000)
out["max_abs_coord_upper_lt_0.999924"] = maxx < Fr(999924, 1000000)
out["min_weight_lower"] = float(minw)
out["max_abs_coord_upper"] = float(maxx)


# ------------------------------------------------------ interval arithmetic
def iadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def isub(a, b):
    return (a[0] - b[1], a[1] - b[0])


def imul(a, b):
    p = (a[0]*b[0], a[0]*b[1], a[1]*b[0], a[1]*b[1])
    return (min(p), max(p))


def iscal(k, a):
    return (k*a[0], k*a[1]) if k >= 0 else (k*a[1], k*a[0])


ONE = (Fr(1), Fr(1))
DEG = 5


def cheb_point(x):
    T = [Fr(1), x]
    U = [Fr(1), 2*x]
    for k in range(1, DEG):
        T.append(2*x*T[k] - T[k-1])
        U.append(2*x*U[k] - U[k-1])
    dT = [Fr(0)] + [k*U[k-1] for k in range(1, DEG+1)]
    return T, dT


def cheb_int(X):
    T = [ONE, X]
    U = [ONE, iscal(2, X)]
    for k in range(1, DEG):
        T.append(isub(iscal(2, imul(X, T[k])), T[k-1]))
        U.append(isub(iscal(2, imul(X, U[k])), U[k-1]))
    dT = [(Fr(0), Fr(0))] + [iscal(k, U[k-1]) for k in range(1, DEG+1)]
    return T, dT


# Exact sanity of point recurrences against cos formulas is implicit; check
# T_k(x)=cos(k arccos x) numerically for one value as a smoke test.
_T, _dT = cheb_point(Fr(3, 7))
req(all(abs(float(_T[k]) - math.cos(k*math.acos(3/7))) < 1e-12
        for k in range(6)), "Chebyshev recurrence smoke")

alphas = sorted(a for a in itertools.product(range(DEG+1), repeat=3)
                if sum(a) <= DEG)
req(len(alphas) == 56, "56 equations")
beta3 = sorted(a for a in itertools.product(range(4), repeat=3)
               if sum(a) <= 3)
req(len(beta3) == 20, "20 cubic functions")

Pc = [cheb_point(c[i]) for i in range(60)]
Pb = [cheb_int(box[i]) for i in range(60)]
# enclosure sanity: center value inside interval
for i in range(60):
    for k in range(DEG+1):
        req(Pb[i][0][k][0] <= Pc[i][0][k] <= Pb[i][0][k][1], "T encl")
        req(Pb[i][1][k][0] <= Pc[i][1][k] <= Pb[i][1][k][1], "dT encl")


def residual_and_jac_point(cc, P):
    G, J = [], []
    for a in alphas:
        g = Fr(0)
        row = [Fr(0)]*80
        for j in range(N):
            T = [P[3*j+d][0] for d in range(3)]
            dT = [P[3*j+d][1] for d in range(3)]
            t = T[0][a[0]]*T[1][a[1]]*T[2][a[2]]
            g += cc[60+j]*t
            row[60+j] = t
            for d in range(3):
                o = [e for e in range(3) if e != d]
                row[3*j+d] = (cc[60+j]*dT[d][a[d]] *
                              T[o[0]][a[o[0]]]*T[o[1]][a[o[1]]])
        G.append(g - (1 if a == (0, 0, 0) else 0))
        J.append(row)
    return G, J


def jac_box(bx, P):
    J = []
    for a in alphas:
        row = [(Fr(0), Fr(0))]*80
        for j in range(N):
            T = [P[3*j+d][0] for d in range(3)]
            dT = [P[3*j+d][1] for d in range(3)]
            row[60+j] = imul(imul(T[0][a[0]], T[1][a[1]]), T[2][a[2]])
            for d in range(3):
                o = [e for e in range(3) if e != d]
                row[3*j+d] = imul(imul(imul(bx[60+j], dT[d][a[d]]),
                                       T[o[0]][a[o[0]]]), T[o[1]][a[o[1]]])
        J.append(row)
    return J


Gc, Jc_full = residual_and_jac_point(c, Pc)
Jb_full = jac_box(box, Pb)
Jc = [[row[k] for k in act] for row in Jc_full]
Jb = [[row[k] for k in act] for row in Jb_full]
for i in range(56):
    for k in range(56):
        req(Jb[i][k][0] <= Jc[i][k] <= Jb[i][k][1], "J(c) in J(B)")
out["max_abs_G_center_float"] = float(max(abs(g) for g in Gc))


# ----------------------------------------------- own preconditioner (mpmath)
def dyadic_inverse(M, bits):
    import mpmath as mp
    mp.mp.dps = 250
    A = mp.matrix([[mp.mpf(v.numerator)/v.denominator for v in row]
                   for row in M])
    Ai = mp.inverse(A)
    n = len(M)
    return [[Fr(int(mp.nint(Ai[i, k]*mp.mpf(2)**bits)), 2**bits)
             for k in range(n)] for i in range(n)]


R = dyadic_inverse(Jc, 240)


def pow2exp(fr):
    d = fr.denominator
    req(d & (d-1) == 0, "non-dyadic")
    return d.bit_length()-1


def to_int(M, K):
    return [[int(v*(1 << K)) if (v*(1 << K)).denominator == 1
             else req(False, "scale") for v in row] for row in M]


Jm = [[(lo+hi)/2 for lo, hi in row] for row in Jb]
Jr = [[(hi-lo)/2 for lo, hi in row] for row in Jb]
KJ = max(pow2exp(v) for M in (Jm, Jr, [Gc], Jc) for row in M for v in row)
KR = 240
Ri, Jmi, Jri, Jci = to_int(R, KR), to_int(Jm, KJ), to_int(Jr, KJ), to_int(Jc, KJ)
Gci = to_int([Gc], KJ)[0]
SC = 1 << (KR+KJ)
n = 56
colsm = list(zip(*Jmi))
colsr = list(zip(*Jri))
colsc = list(zip(*Jci))
rows_sum, rows_sum_c, RG = [], [], []
for i in range(n):
    Ri_row = Ri[i]
    absR = [abs(v) for v in Ri_row]
    s, sc = 0, 0
    for k in range(n):
        e = (SC if i == k else 0) - sum(a*b for a, b in zip(Ri_row, colsm[k]))
        p = sum(a*b for a, b in zip(absR, colsr[k]))
        s += abs(e) + p
        ec = (SC if i == k else 0) - sum(a*b for a, b in zip(Ri_row, colsc[k]))
        sc += abs(ec)
    rows_sum.append(s)
    rows_sum_c.append(sc)
    RG.append(sum(a*b for a, b in zip(Ri_row, Gci)))
# All quantities above are exact integers at scale 2^(KR+KJ).
q = Fr(max(rows_sum), SC)
qc = Fr(max(rows_sum_c), SC)
z = Fr(max(abs(v) for v in RG), SC)
req(qc < 1, "||I-RJ(c)||<1 (R invertible)")
req(q < 1, "q<1")
# componentwise Krawczyk K(B) in interior(B) and the norm criterion
req(all(Fr(abs(RG[i]), SC) + r*Fr(rows_sum[i], SC) < r for i in range(n)),
    "Krawczyk componentwise")
req(z + q*r < r, "z+qr<r")
out["krawczyk"] = {"q_upper": float(q), "q_center": float(qc),
                   "z": float(z), "margin_over_r": float(1 - (z + q*r)/r),
                   "q_lt_3e-17": q < Fr(3, 10**17),
                   "z_lt_4e-55": z < Fr(4, 10**55),
                   "scale_bits": KR+KJ}


# ---- independent invertibility cross-check: det mod primes of scaled R, J(c)
def det_mod(M, p):
    a = [[v % p for v in row] for row in M]
    m = len(a)
    det = 1
    for j in range(m):
        piv = next((i for i in range(j, m) if a[i][j]), None)
        if piv is None:
            return 0
        if piv != j:
            a[piv], a[j] = a[j], a[piv]
            det = -det
        det = det*a[j][j] % p
        inv = pow(a[j][j], -1, p)
        for i in range(j+1, m):
            f = a[i][j]*inv % p
            if f:
                a[i] = [(x - f*y) % p for x, y in zip(a[i], a[j])]
    return det % p


def is_prime(p):
    return p > 1 and all(p % d for d in range(2, math.isqrt(p)+1))


P1, P2 = 998244353, 1000000007
req(is_prime(P1) and is_prime(P2), "primes")
out["det_R_mod"] = [det_mod(Ri, P1), det_mod(Ri, P2)]
out["det_Jc_mod"] = [det_mod(Jci, P1), det_mod(Jci, P2)]
req(any(out["det_R_mod"]) and any(out["det_Jc_mod"]), "R/J(c) det mod p")


# ----------------------------------------------------- unisolvence transfer
def gauss_inverse_det(M):
    m = len(M)
    a = [list(row) + [Fr(int(i == k)) for k in range(m)]
         for i, row in enumerate(M)]
    det = Fr(1)
    for j in range(m):
        piv = next((i for i in range(j, m) if a[i][j] != 0), None)
        if piv is None:
            return None, Fr(0)
        if piv != j:
            a[piv], a[j] = a[j], a[piv]
            det = -det
        pv = a[j][j]
        det *= pv
        a[j] = [v/pv for v in a[j]]
        for i in range(m):
            if i != j and a[i][j] != 0:
                f = a[i][j]
                a[i] = [x - f*y for x, y in zip(a[i], a[j])]
    return [row[m:] for row in a], det


Wc = [[Pc[3*j][0][b[0]]*Pc[3*j+1][0][b[1]]*Pc[3*j+2][0][b[2]]
       for b in beta3] for j in range(N)]
Wb = [[imul(imul(Pb[3*j][0][b[0]], Pb[3*j+1][0][b[1]]), Pb[3*j+2][0][b[2]])
       for b in beta3] for j in range(N)]
Winv, detW = gauss_inverse_det(Wc)
req(detW != 0, "Chebyshev cubic matrix at center singular")
Delta = [[max(Wc[j][k] - Wb[j][k][0], Wb[j][k][1] - Wc[j][k])
          for k in range(N)] for j in range(N)]
req(all(v >= 0 for row in Delta for v in row), "W(c) in W(B)")
qW = max(sum(sum(abs(Winv[i][l])*Delta[l][k] for l in range(N))
             for k in range(N)) for i in range(N))
req(qW < 1, "rank transfer bound")
out["rank"] = {"det_cheb_center_float": float(detW), "qW_upper": float(qW)}
# monomial Vandermonde exact determinant at center; producer reports mod 65537
Vc = [[c[3*j]**b[0]*c[3*j+1]**b[1]*c[3*j+2]**b[2] for b in beta3]
      for j in range(N)]
_, detV = gauss_inverse_det(Vc)
req(detV != 0, "monomial V(c) singular")
dmod = [detV.numerator*pow(detV.denominator, -1, p) % p
        for p in (65537, 1000003, P1)]
out["rank"].update(det_monomial_center_float=float(detV),
                   det_monomial_center_mod_65537_1000003_998244353=dmod)


# ------------------------------------------------------------- moments
def mono_to_cheb(k):
    co = {0: Fr(1)}
    for _ in range(k):
        nco = {}
        for m, v in co.items():
            if m == 0:
                nco[1] = nco.get(1, 0) + v
            else:
                nco[m+1] = nco.get(m+1, 0) + v/2
                nco[m-1] = nco.get(m-1, 0) + v/2
        co = nco
    return co


mom1 = [mono_to_cheb(k).get(0, Fr(0)) for k in range(6)]
binom = [Fr(math.comb(k, k//2), 2**k) if k % 2 == 0 else Fr(0)
         for k in range(6)]
req(mom1 == binom, "1D arcsine moments")
import mpmath as mp  # noqa: E402
mp.mp.dps = 30
quad = [mp.quad(lambda t: mp.cos(t)**k, [0, mp.pi])/mp.pi for k in range(6)]
req(all(abs(quad[k] - mp.mpf(binom[k].numerator)/binom[k].denominator)
        < mp.mpf(10)**-25 for k in range(6)), "quadrature sanity")
out["moments_1d"] = [str(v) for v in binom]
# monomial residual at the center (consistency with producer's formulation)
F = []
for a in alphas:
    s = sum(c[60+j]*c[3*j]**a[0]*c[3*j+1]**a[1]*c[3*j+2]**a[2]
            for j in range(N))
    F.append(s - binom[a[0]]*binom[a[1]]*binom[a[2]])
out["max_abs_monomial_F_center_float"] = float(max(abs(v) for v in F))

# ------------------------------------------------------------- nonlattice
req(0 in fixed and 3 in fixed, "coords 0,3 fixed")
a_, b_ = c[0], c[3]
D = (1 - a_*a_)*(1 - b_*b_)
req(D > 0, "D>0")
sq = (math.isqrt(D.numerator)**2 == D.numerator and
      math.isqrt(D.denominator)**2 == D.denominator)
req(not sq, "D nonsquare")
tr = 4*a_*b_
req(tr.denominator != 1, "4ab nonintegral")
# minimal polynomial t^2 - tr t + nrm of 2ab +/- 2 sqrt(D)
nrm = (2*a_*b_)**2 - 4*D
req(nrm == 4*(a_*a_ + b_*b_ - 1), "norm identity")
pairs = []
for i, j in itertools.combinations([k for k in fixed if k < 60], 2):
    if i % 3 == j % 3:
        A, B = c[i], c[j]
        d = (1-A*A)*(1-B*B)
        s2 = (math.isqrt(d.numerator)**2 == d.numerator and
              math.isqrt(d.denominator)**2 == d.denominator)
        pairs.append((i, j, (not s2) and (4*A*B).denominator != 1))
out["nonlattice"] = {"a": str(a_), "b": str(b_), "D": str(D),
                     "trace": str(tr), "nodes": [0, 1], "axis": 0,
                     "same_axis_fixed_pairs": len(pairs),
                     "pairs_passing": sum(p[2] for p in pairs)}
out["fixed_node_coords"] = [i for i in fixed if i < 60]
out["verdict"] = "PASS"
out["elapsed_seconds"] = time.monotonic() - t0
open(out_path, 'w').write(json.dumps(out, indent=1, sort_keys=True) + "\n")
print(json.dumps(out, indent=1, sort_keys=True))
