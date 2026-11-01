"""Independent Claude audit-01 checker for the MZ-constants campaign.

Written from scratch by the Claude auditor; it does not import or reuse campaign code.
Weights are obtained by solving moment equations (not from the campaign's closed forms),
continuous Gram matrices use Gauss-Legendre quadrature, and exact claims use Fractions.

Checks:
  E1  PD-T013 closed-form CC weights vs moment-equation weights (floating, N<=30);
      positivity of the closed form (floating, N<200).
  E2  PD-T022 off-diagonal signs of A_rho=(1+rho)M-R, all 0<=n<N, N<=60 (exact).
  E3  PD-T019 exact U_{N-1} norms (exact, N<=60).
  E4  PD-T015 telescoping row sums (Mb)_i and floor ratios (exact, N<=40).
  M1  Floating spectra: lambda_max(n=N-1) vs PD-T014 bound 2-2/(pi N) and PD-T022 bound
      2-4/N+4/N^2; lambda_min vs PD-T017 1/K_N; PD-T018 witness endpoint/degree.
  M2  PD-T021: Padua Lebesgue weights by moment solve; marginal == 2 w_CC; compression
      inequalities for lambda_min, lambda_max and deviation at n=N-1, N<=14.
Exact parts are certificates of finite instances only; floating parts are MEASURED.
"""
import json, math, sys, hashlib
from fractions import Fraction as F
import numpy as np
from numpy.polynomial import chebyshev as C, legendre as L

out = {"script_sha256": hashlib.sha256(open(__file__, 'rb').read()).hexdigest(),
       "numpy": np.__version__, "python": sys.version.split()[0]}

def mu(k):  # exact int_{-1}^1 T_k
    return F(0) if k % 2 else F(2, 1 - k * k)

# ---------- E1 (floating, MEASURED): weights from the Chebyshev moment equations
def cc_weights_moments(N):
    x = np.cos(np.arange(N + 1) * np.pi / N)
    V = C.chebvander(x, N).T  # rows T_k(x_j)
    m = np.array([float(mu(k)) for k in range(N + 1)])
    return x, np.linalg.solve(V, m)

def cc_weights_formula(N):
    th = np.arange(N + 1) * np.pi / N
    c = np.ones(N + 1); c[0] = c[-1] = 0.5
    s = np.ones(N + 1)
    for k in range(1, (N - 1) // 2 + 1):
        s -= 2 * np.cos(2 * k * th) / (4 * k * k - 1)
    if N % 2 == 0:
        s -= np.cos(N * th) / (N * N - 1)
    return 2 * c / N * s

e1 = max(np.max(np.abs(cc_weights_moments(N)[1] - cc_weights_formula(N))) for N in range(2, 31))
out["E1_weight_formula_maxabs_N2_30"] = e1
out["E1_all_positive"] = all((cc_weights_formula(N) > 0).all() for N in range(2, 200))

# ---------- E2: exact sign check of A_rho off-diagonals
def Qcc_T(k, N):  # exact CC value of T_k, 0<=k<=2N
    return mu(k) if k <= N else mu(2 * N - k)

bad = 0; count = 0
for N in range(2, 61):
    for n in range(0, N):
        rho = F(max(2 * n - N, 0), N) ** 2
        for i in range(n + 1):
            for j in range(n + 1):
                if i == j or (i + j) % 2: continue
                Mij = (mu(abs(i - j)) + mu(i + j)) / 2
                Rij = (mu(abs(i - j)) + Qcc_T(i + j, N)) / 2
                a = (1 + rho) * Mij - Rij
                count += 1
                if not a < 0 and not (a == 0 and rho == 0):
                    bad += 1
out["E2_Arho_offdiag_entries_checked"] = count
out["E2_Arho_offdiag_violations"] = bad

# ---------- E3: exact U_{N-1} norms
ok3 = True
for N in range(2, 61):
    S = sum(F(1, 2 * j - 1) for j in range(1, N + 1))
    # continuous: U^2 = sum_{s} U_{2s}, int U_{2s} = 2/(2s+1); recompute via Chebyshev-T expansion
    # U_{N-1} = sum over T: U_r = 2 sum_{k odd/even <= r} T_k - [r even] T_0
    r = N - 1
    coef = [F(0)] * (r + 1)
    for k in range(r % 2, r + 1, 2):
        coef[k] = F(2)
    if r % 2 == 0: coef[0] = F(1)
    # exact integral of square via T products
    tot = F(0)
    for a_ in range(r + 1):
        for b_ in range(r + 1):
            if coef[a_] and coef[b_]:
                tot += coef[a_] * coef[b_] * (mu(abs(a_ - b_)) + mu(a_ + b_)) / 2
    ok3 &= (tot == 2 * S)
    # discrete: endpoints only, exact endpoint weight
    w0 = F(1, N * N) if N % 2 else F(1, N * N - 1)
    Qd = 2 * w0 * N * N
    ok3 &= (Qd == (2 if N % 2 else F(2 * N * N, N * N - 1)))
out["E3_U_identity_N2_60"] = ok3

# ---------- E4: exact telescoping row sums of M b on indices 0..N-1
ok4 = True; minratio = []
for N in range(2, 41):
    n = N - 1
    b = [F(1, 2)] + [F(1)] * n
    rat = []
    for i in range(n + 1):
        Mb = sum((mu(abs(i - j)) + mu(i + j)) / 2 * b[j] for j in range(n + 1))
        m_i = N if (N - i) % 2 == 0 else N + 1
        k_i = m_i - 1
        pred = F(1, k_i) if i == 0 else F(k_i, k_i * k_i - i * i)
        ok4 &= (Mb == pred)
        rat.append(Mb / b[i] * N)  # should be >= 1 (>=2 at i=0)
    ok4 &= (rat[0] >= 2) and min(rat[1:]) >= 1
out["E4_telescoping_floor_N2_40"] = ok4

# ---------- M1: spectra
def leg_orth_vander(x, n):
    V = L.legvander(x, n)
    return V * np.sqrt((2 * np.arange(n + 1) + 1) / 2)

def cc_gram(N, n):
    x, w = cc_weights_moments(N)
    P = leg_orth_vander(x, n)
    return (P.T * w) @ P

rows = []
for N in [4, 8, 16, 32, 64, 128, 256, 512]:
    G = cc_gram(N, N - 1); ev = np.linalg.eigvalsh(G)
    hN = 2 * sum(1 / r for r in range(1, N + 2)) - 1
    K = 4 * math.pi ** 2 * (math.pi + 1) ** 2 * hN * (hN + 2 * sum(1 / r for r in range(1, N // 2 + 2)))
    rows.append({"N": N, "lmin": ev[0], "lmax": ev[-1], "T014": 2 - 2 / (math.pi * N),
                 "T022_at_N-1": 2 - 4 / N + 4 / N ** 2, "T017_lower": 1 / K,
                 "lmin_log2": ev[0] * math.log(N) ** 2, "lmin_log1": ev[0] * math.log(N)})
out["M1_spectra"] = rows
out["M1_T022_strictly_below_T014_all_N2_10000"] = all(2 - 4 / N + 4 / N ** 2 < 2 - 2 / (math.pi * N) for N in range(2, 10001))

# PD-T018 witness: degree and endpoints
wit = []
for N in [8, 33, 64]:
    Mx = (N - 1) // 2
    def U(r):  # Chebyshev-T coefficients of U_r
        c = np.zeros(N);
        for k in range(r % 2, r + 1, 2): c[k] = 2
        if r % 2 == 0: c[0] = 1
        return c
    p = sum((U(N - 1 - 2 * m) - (1 - 2 * m / N) * U(N - 1)) / m for m in range(1, Mx + 1))
    wit.append({"N": N, "deg<=N-1": len(p) <= N, "p(1)": float(C.chebval(1, p)), "p(-1)": float(C.chebval(-1, p))})
out["M1_witness"] = wit

# ---------- M2: Padua
def padua(N):
    pts = [(math.cos(j * math.pi / N), math.cos(k * math.pi / (N + 1)), j)
           for j in range(N + 1) for k in range(N + 2) if (j + k) % 2 == 0]
    return np.array(pts)

def total_degree_basis(n):
    return [(a, n_ - a) for n_ in range(n + 1) for a in range(n_ + 1)]

pad = []
for N in range(2, 15):
    P = padua(N); x, y, jj = P[:, 0], P[:, 1], P[:, 2].astype(int)
    basis = total_degree_basis(N)
    Tx = C.chebvander(x, N); Ty = C.chebvander(y, N)
    V = np.array([Tx[:, a] * Ty[:, b] for a, b in basis])
    m = np.array([float(mu(a) * mu(b)) for a, b in basis])
    W = np.linalg.solve(V, m)
    marg = np.array([W[jj == j].sum() for j in range(N + 1)])
    _, wcc = cc_weights_moments(N)
    n = N - 1
    bas = total_degree_basis(n)
    Lx = leg_orth_vander(x, n); Ly = leg_orth_vander(y, n)
    B = np.array([Lx[:, a] * Ly[:, b] for a, b in bas]).T
    GP = (B.T * W) @ B; evP = np.linalg.eigvalsh(GP)
    evC = np.linalg.eigvalsh(cc_gram(N, n))
    pad.append({"N": N, "n_neg_weights": int((W < 0).sum()), "marg_err": float(np.max(np.abs(marg - 2 * wcc))),
                "lminP": evP[0], "lminCC": evC[0], "lmaxP": evP[-1], "lmaxCC": evC[-1],
                "etaP": float(max(abs(evP - 1))), "etaCC": float(max(abs(evC - 1))),
                "domination_ok": bool(evP[0] <= evC[0] + 1e-12 and evP[-1] >= evC[-1] - 1e-12)})
out["M2_padua"] = pad
print(json.dumps(out, indent=1, default=float))


# ---------- M3 (appended, MEASURED): shifted-logarithm fits of the endpoint lambda_min
# Fit on N in FIT, predict on PRED (outside fitted range). Diagnostic for OPEN PD-T020 only.
def endpoint_lmin(N):
    return float(np.linalg.eigvalsh(cc_gram(N, N - 1))[0])

if "--fits" in sys.argv:
    from scipy.optimize import curve_fit
    FIT = [40, 80, 160, 320, 640, 1280]
    PRED = [2560, 5120]
    lf = np.array([endpoint_lmin(N) for N in FIT])
    lp = np.array([endpoint_lmin(N) for N in PRED])
    xf, xp = np.log(FIT), np.log(PRED)
    m2 = lambda x, c, b: c / (x + b) ** 2
    m1 = lambda x, a, b: a / (x + b)
    p2, _ = curve_fit(m2, xf, lf, p0=(13, 3)); p1, _ = curve_fit(m1, xf, lf, p0=(0.8, 0))
    fits = {"fit_N": FIT, "pred_N": PRED, "lmin_fit": lf.tolist(), "lmin_pred": lp.tolist(),
            "log2_shift": {"c": p2[0], "b": p2[1],
                           "max_rel_resid_fit": float(np.max(np.abs(m2(xf, *p2) / lf - 1))),
                           "rel_err_pred": (m2(xp, *p2) / lp - 1).tolist()},
            "log1_shift": {"a": p1[0], "b": p1[1],
                           "max_rel_resid_fit": float(np.max(np.abs(m1(xf, *p1) / lf - 1))),
                           "rel_err_pred": (m1(xp, *p1) / lp - 1).tolist()}}
    print(json.dumps({"M3_fits": fits}, indent=1, default=float))
