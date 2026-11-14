#!/usr/bin/env python3
"""Interval (mpmath.iv, outward rounded) evaluation of the literal E13/E14-outer320,
E12-corner256 and E14 annular/half-near scalar functions at their bases, plus
a MEASURED log-grid scan of the all-real-n directions (not a proof; the proof
of directions is the analytic argument recorded in the audit report).
Auditor: Claude Opus 5.5 xhigh, 2026-11-07.  Exit 1 on any FAIL.
"""
import sys
from fractions import Fraction as Fr
from mpmath import iv, mp, mpf
import mpmath

iv.dps = 40
mp.dps = 40
FAILS = []
def chk(name, ok, det=""):
    print(("PASS " if ok else "FAIL ") + name + (" :: " + det if det else ""))
    if not ok:
        FAILS.append(name)

def q(fr):  # exact rational -> interval
    fr = Fr(fr)
    return iv.mpf(fr.numerator) / iv.mpf(fr.denominator)

def lt(x, bound):  # interval x strictly below rational bound
    return x.b < q(bound)
def gt(x, bound):
    return x.a > q(bound)
def show(x):
    return f"[{mpmath.nstr(x.a, 10)}, {mpmath.nstr(x.b, 10)}]"

PI = iv.pi
def common(nn):
    n = iv.mpf(nn); m = n + 1
    L = iv.log(n); H = 1 + L
    T = (4 * L ** 2 - 3 * L) / PI ** 2
    b = 4 / PI ** 2
    hr = iv.log(iv.mpf(5) / 2) + iv.mpf(1) / 18
    Da = ((52 / PI ** 2) * H + 7) / n + 20 * H / (PI * n ** 2)
    D = Da + 10 / n ** 2
    Mesh = b * (2 * L + 2 * hr) / n + (4 + b * (L + 1 / n)) / (4 * n ** 2 - 1) \
        + b / (2 * n - 1) ** 2 + (5 + b * (iv.log(n + iv.mpf(1) / 2) + 2)) / (4 * (n - iv.mpf(1) / 2) ** 2)
    ebar = D + Mesh + 1 / n
    KD = ((6 + 16 / (3 * PI)) * H + 2 / PI) / n
    W = (3 * iv.log(m) + iv.log(2) + 2 * iv.log(PI) + 2) / (PI * m)
    A4 = 4 / n + 40 * H / (PI * n ** 2)
    C4 = A4 + 20 / n ** 2
    db = (17 * L + 27) / n ** 2
    return dict(n=n, m=m, L=L, H=H, T=T, b=b, hr=hr, Da=Da, D=D, Mesh=Mesh, ebar=ebar,
                KD=KD, W=W, A4=A4, C4=C4, db=db)

# ---------------- E14 half-near / annular at 320 ----------------
c = common(320)
for nm, val, op, bd in (("T", c["T"], gt, Fr(293, 25)), ("D", c["D"], lt, Fr(27, 200)),
                        ("Mesh", c["Mesh"], lt, Fr(7, 400)), ("ebar", c["ebar"], lt, Fr(249, 1600)),
                        ("C4", c["C4"], lt, Fr(677, 50000))):
    chk(f"320 {nm} {'<' if op is lt else '>'} {bd}", op(val, bd), show(val))
L, H, n = c["L"], c["H"], c["n"]
kWx = ((iv.mpf(19) / 2) * H + (iv.mpf(23) / 3) * L + iv.mpf(155) / 2) / n + 152 / n ** 2
kWy = kWx + c["db"]
chk("320 kWx<583/1000", lt(kWx, Fr(583, 1000)), show(kWx))
chk("320 kWy<117/200", lt(kWy, Fr(117, 200)), show(kWy))
kNx = ((iv.mpf(19) / 2) * H + (iv.mpf(23) / 3) * L + iv.mpf(677) / 10) / n + 82 / n ** 2
chk("320 kNx<11031/20000", lt(kNx, Fr(11031, 20000)), show(kNx))
chk("320 kNy<11056/20000", lt(kNx + c["db"], Fr(11056, 20000)), show(kNx + c["db"]))

# ---------------- E14-outer320 = E13 system at 320 ----------------
a0, p0, P0, w0, eta, u1 = q(Fr(337, 384)), q(Fr(12, 25)), q(Fr(24, 25)), q(Fr(721, 384)), q(Fr(3, 2)), q(Fr(47, 384))
jS, tS = q(Fr(23, 250)), q(Fr(221, 500))
def E13(nn, ebar_choice="ebar"):
    c = common(nn)
    n, m, L, H, b, r = c["n"], c["m"], c["L"], c["H"], c["b"], c["hr"]
    eps = 3 * PI / (2 * m)
    ell = -iv.log(iv.sin(eps))
    C = 1 + 8 * a0 * m / (3 * PI)
    Gam = p0 * (1 + iv.log(1 + C / p0))
    gam = 1 + iv.log(1 + C / p0) - C / (p0 + C)
    MA = p0 / PI + 4 * a0 / PI ** 2
    VB = 23 + (3 * Gam + (2 * p0 + 6 * P0) * ell + 26 * a0 + 20) / PI
    CB = 6 + (4 + 4 * a0 / iv.e) / PI
    Genv = 7 * L * MA / m + VB / (2 * m) + (4 / m) * (7 + (P0 / PI) * (5 + 2 * iv.log(2 * m))) + 2 * CB / m
    Denv = a0 * c["Da"] + 10 / n ** 2
    R6 = (21 + 21 * a0 + 2 * L + ((1 + 48 * p0) * H + 24 * p0) / PI) / n + (317 + iv.mpf(5) / 12) / n ** 2
    Dm = 4 * w0 / PI + a0 * b * iv.log(PI)
    Zm = Dm + a0 * b / n
    Menv = a0 * b * (2 * L + 2 * r) / n + (Dm + a0 * b * (L + 1 / n)) / (4 * n ** 2 - 1) \
        + a0 * b / (2 * n - 1) ** 2 + (Zm + a0 * b * (iv.log(n + iv.mpf(1) / 2) + 2)) / (4 * (n - iv.mpf(1) / 2) ** 2)
    Cb = Denv + Genv + R6 + Menv
    Cs = eta * (7 * L / (PI * m) + (3 * gam + 2 * ell) / (2 * PI * m) + (48 * H + 24) / (PI * n)) \
        + 3 * ((iv.log(2) + 4 * iv.log(PI)) / (PI * m) + c["W"])
    Cl = (12 * ell + 16 * (5 + 2 * iv.log(2 * m))) / (PI * m)
    em = c["ebar"]
    Gb = u1 * (c["T"] + jS) - tS * p0 - Cb - P0 * c["KD"] - em
    K = c["T"] + jS - Cl - 4 * c["KD"]
    A = eta * tS + Cs
    Fv = Gb - A ** 2 / (4 * K)
    return dict(ell=ell, Gam=Gam, gam=gam, MA=MA, VB=VB, CB=CB, Genv=Genv, Denv=Denv, R6=R6, Menv=Menv,
                Cb=Cb, Cs=Cs, Cl=Cl, Gb=Gb, K=K, A=A, F=Fv, KD=c["KD"], W=c["W"], ebar=em)
o = E13(320)
claims = [("KD", lt, Fr(1, 6)), ("W", lt, Fr(3, 125)), ("ell", lt, Fr(13, 3)), ("Gam", lt, Fr(18, 5)),
          ("gam", lt, Fr(15, 2)), ("MA", lt, Fr(13, 25)), ("CB", lt, Fr(8)), ("Denv", lt, Fr(3, 25)),
          ("VB", lt, Fr(50)), ("Genv", lt, Fr(9, 25)), ("R6", lt, Fr(17, 50)), ("Menv", lt, Fr(2, 125)),
          ("Cb", lt, Fr(209, 250)), ("Cs", lt, Fr(71, 100)), ("Cl", lt, Fr(7, 20)), ("ebar", lt, Fr(5, 32)),
          ("Gb", gt, Fr(3, 40)), ("K", gt, Fr(10)), ("A", lt, Fr(7, 5)), ("F", gt, Fr(13, 500))]
for nm, op, bd in claims:
    chk(f"outer320 {nm} {'<' if op is lt else '>'} {bd}", op(o[nm], bd), show(o[nm]))

# ---------------- E12-corner256 ----------------
def corner(nn):
    c = common(nn)
    n, m, L, H = c["n"], c["m"], c["L"], c["H"]
    MAc = 1 / PI + 4 / PI ** 2
    g = 1 + iv.log(2 + 8 * m / (3 * PI))
    Gg = (7 * MAc * L + iv.mpf(111) / 2 + (63 + iv.log(2) + 4 * iv.log(PI) + 7 * iv.log(m) + 16 * iv.log(2 * m) + iv.mpf(3) / 2 * g) / PI) / m
    six = (64 + 16 * L) / n + 318 / n ** 2
    CEbar = c["D"] + Gg + six + c["Mesh"] + c["W"]
    kWy = ((iv.mpf(19) / 2) * H + 15 * L + iv.mpf(265) / 3) / n + (179 + 17 * L) / n ** 2
    M = (4 * L ** 2 + (iv.mpf(79) / 5) * L) / PI ** 2 + iv.mpf(9) / 4 + CEbar + 2 * c["KD"]
    q0, rU, j = q(Fr(7, 48)), q(Fr(2, 125)), q(Fr(23, 250))
    h = PI / 4
    dA = q0 * (c["T"] - c["ebar"] + j) - iv.mpf(1) / 4 - c["C4"] - h * kWy
    dD = 2 * q0 * (c["T"] + j) - iv.mpf(4) / 15 - CEbar - iv.mpf(3) / 2 * c["KD"] - c["ebar"]
    FA = dA - rU * M
    FD = dD - 2 * rU * M
    return dict(T=c["T"], D=c["D"], Gg=Gg, six=six, Mesh=c["Mesh"], W=c["W"], CEbar=CEbar, ebar=c["ebar"],
                KD=c["KD"], C4=c["C4"], kWy=kWy, M=M, dA=dA, dD=dD, FA=FA, FD=FD)
k = corner(256)
for nm, op, bd in (("T", gt, Fr(107, 10)), ("D", lt, Fr(1, 6)), ("Gg", lt, Fr(5, 8)), ("six", lt, Fr(61, 100)),
                   ("Mesh", lt, Fr(11, 500)), ("W", lt, Fr(7, 250)), ("CEbar", lt, Fr(3, 2)), ("ebar", lt, Fr(1, 5)),
                   ("KD", lt, Fr(1, 5)), ("C4", lt, Fr(9, 500)), ("kWy", lt, Fr(93, 100)), ("M", lt, Fr(26)),
                   ("dA", gt, Fr(2293, 4200)), ("dD", gt, Fr(881, 1000)), ("FA", gt, Fr(1, 8)), ("FD", gt, Fr(49, 1000))):
    chk(f"corner256 {nm} {'<' if op is lt else '>'} {bd}", op(k[nm], bd), show(k[nm]))

# ---------------- MEASURED direction scan (floating, 40 digits) ----------------
def mid(x):
    return (x.a + x.b) / 2
grid = [320 * (1.01 ** i) for i in range(0, 2200, 7)] + [10 ** e for e in range(4, 16)]
grid = sorted(set(grid))
prev = None
viol = {}
for nn in grid:
    c = common(nn)
    L, H, nI = c["L"], c["H"], c["n"]
    kWx = ((iv.mpf(19) / 2) * H + (iv.mpf(23) / 3) * L + iv.mpf(155) / 2) / nI + 152 / nI ** 2
    cur = dict(kWx=mid(kWx), kWy=mid(kWx + c["db"]), C4=mid(c["C4"]), TEJ=mid(c["T"] - c["ebar"]),
               ebar=mid(c["ebar"]))
    oo = E13(nn); kk = corner(max(nn, 256))
    cur.update(Gb=mid(oo["Gb"]), K=mid(oo["K"]), A=mid(oo["A"]), F=mid(oo["F"]), FA=mid(kk["FA"]), FD=mid(kk["FD"]))
    if prev is not None:
        for key, sgn in (("kWx", -1), ("kWy", -1), ("C4", -1), ("ebar", -1), ("TEJ", 1), ("Gb", 1), ("K", 1),
                         ("A", -1), ("F", 1), ("FA", 1), ("FD", 1)):
            if sgn * (cur[key] - prev[key]) <= 0:
                viol.setdefault(key, []).append(nn)
    prev = cur
chk("[MEASURED grid 320..1e15] directions kWx,kWy,C4,ebar dec; T-ebar inc; E13 Gb,K inc, A dec, F inc; E12 FA,FD inc",
    not viol, str({k: v[:3] for k, v in viol.items()}))
print("grid points:", len(grid))
print("\nFAILS:", FAILS)
sys.exit(1 if FAILS else 0)
