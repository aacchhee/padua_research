"""Transcription of the E14/E13/E12/E15 explicit scalar allowance formulas.

Sources (branch codex/padua-argmax-bridge-20261105 @ 1b6aa31ae759022ce89bb8a3be70a881790e259f):
  theory/E14-halfnear320.md   (half-near recipe, sections 2-5)
  theory/E14-annular320.md    (annulus/wide recipe, sections 1-3)
  theory/E14-outer320.md + theory/E13-joint-radius-outer.md (outer gate (2),(7)-(10))
  theory/E12-corner256.md     (corner gates (4)-(12))
  theory/E15-analytic-far192.md (far192 gate (5),(21))
  theory/E02-assembly768.md (8) (floor functions Fn,Fs,Fh,Fw)

Everything here is evaluated in mpmath floating arithmetic (default 50 digits) or
mpmath.iv intervals when ctx=iv is passed.  These are evaluations of the stated
SUFFICIENT allowance formulas, not of the Padua Lebesgue function.  Nothing here
is a proof; all outputs are MEASURED formula evaluations unless enclosed with iv.
"""
import mpmath as mp

mp.mp.dps = 50


class Ctx:
    """Thin wrapper so the same formulas run in mp (float) or mp.iv (interval)."""

    def __init__(self, iv=False):
        self.iv = iv
        self.m = mp.iv if iv else mp
        if iv:
            mp.iv.dps = 60

    def c(self, x):
        # exact rational/integer constant
        if self.iv:
            return mp.iv.mpf(x) if not isinstance(x, tuple) else mp.iv.mpf(x)
        return mp.mpf(x)

    def frac(self, p, q):
        if self.iv:
            return mp.iv.mpf(p) / q
        return mp.mpf(p) / q


def scalars(n, cx=None, jstar=None):
    """Common scalars of E09/E14 section 2 and E13 section 4 at real degree n."""
    if cx is None:
        cx = Ctx(False)
    m_ = cx.m
    n = m_.mpf(n)
    pi = m_.pi
    L = m_.log(n)
    H = 1 + L
    m = n + 1
    s = {}
    s['n'] = n
    s['L'] = L
    s['H'] = H
    s['T'] = (4 * L ** 2 - 3 * L) / pi ** 2
    Da = ((52 / pi ** 2) * H + 7) / n + 20 * H / (pi * n ** 2)
    s['Da'] = Da
    s['D'] = Da + 10 / n ** 2
    b = 4 / pi ** 2
    hr = m_.log(m_.mpf(5) / 2) + m_.mpf(1) / 18
    s['Mesh'] = (b * (2 * L + 2 * hr) / n + (4 + b * (L + 1 / n)) / (4 * n ** 2 - 1)
                 + b / (2 * n - 1) ** 2 + (5 + b * (m_.log(n + m_.mpf(1) / 2) + 2)) / (4 * (n - m_.mpf(1) / 2) ** 2))
    # one-sided actual-origin lower: ebar valid n>=160; e_minus valid n>=32
    s['ebar'] = s['D'] + s['Mesh'] + 1 / n
    Borig = pi * (L + 25 * m_.log(2 * m) + m_.mpf(193) / 3) / (8 * m ** 2) + 1 / (8 * n ** 2)
    extra = 71 / n ** 2 - m_.mpf(22) / (45 * m)
    if not cx.iv:
        extra = max(extra, 0)
    else:
        extra = extra if extra.a > 0 else m_.mpf(0)
    s['eminus'] = s['D'] + s['Mesh'] + Borig + extra
    s['eorig'] = s['ebar'] if (float(mp.mpf(n.a if cx.iv else n)) >= 160) else s['eminus']
    s['j'] = m_.mpf(23) / 250 if jstar is None else jstar
    s['A4'] = 4 / n + 40 * H / (pi * n ** 2)
    s['C4'] = s['A4'] + 20 / n ** 2
    s['JN'] = ((m_.mpf(3) / 2) * H + m_.mpf(16) / 5) / n + 78 / n ** 2
    s['db'] = (17 * L + 27) / n ** 2
    s['kNx'] = ((m_.mpf(19) / 2) * H + (m_.mpf(23) / 3) * L + m_.mpf(677) / 10) / n + 82 / n ** 2
    s['kNy'] = s['kNx'] + s['db']
    s['JW'] = ((m_.mpf(3) / 2) * H + 6) / n + 148 / n ** 2
    s['kWx'] = ((m_.mpf(19) / 2) * H + (m_.mpf(23) / 3) * L + m_.mpf(155) / 2) / n + 152 / n ** 2
    s['kWy'] = s['kWx'] + s['db']
    # old E04 wide coefficient used by E12 corner256
    s['kWy_old'] = ((m_.mpf(19) / 2) * H + 15 * L + m_.mpf(265) / 3) / n + (179 + 17 * L) / n ** 2
    s['KD'] = ((6 + 16 / (3 * pi)) * H + 2 / pi) / n
    return s


def floors(n, r, cx=None):
    """E01/E02 floor functions (E02-assembly768 eq. (8)); valid n>=64.
    Fn,Fs,Fw for actual rho<=r<=pi/4; Fh through rB=21/40."""
    if cx is None:
        cx = Ctx(False)
    m_ = cx.m
    n = m_.mpf(n)
    r = m_.mpf(r)
    p = m_.mpf(22) / 7
    a = 1 - r ** 2 / 4
    eta = a * (1 - (4 * p + r) / n) - r / 2
    Fn = (2 * eta / (p + r)) * (n / (n + 1)) * (m_.mpf(1) / 4 - 1 / n)
    Fs = (m_.mpf(35) / 286) * (1 - 6 / n) ** 2 * (a - r / 2)
    A0 = 97 * a / 100 - r / 2
    Ih = 2303 * a / 5000 - 471 * r / 1250
    Rh = 4837 * a / 1875 - 5 * r / 3
    Iw = 5369 * a / 15000 - 7379 * r / 30000
    Rw = 37621 * a / 15000 - 3 * r / 2
    Fh = (m_.mpf(539) / 1936) * Ih - 140 * A0 / (157 * n) - 400 * Rh / (157 * n) - 800 * A0 / (3 * n ** 2)
    Fw = (m_.mpf(539) / 1936) * Iw - 140 * A0 / (157 * n) - 400 * Rw / (157 * n) - 800 * A0 / (3 * n ** 2)
    return dict(Fn=Fn, Fs=Fs, Fh=Fh, Fw=Fw)


def floor_min(n, r):
    f = floors(n, r)
    rB = mp.mpf(21) / 40
    if r <= rB:
        return min(f['Fn'], f['Fs'], f['Fh'])
    elif r <= mp.pi / 4:
        return min(f['Fn'], f['Fs'], f['Fw'])
    return None


# ---------------------------------------------------------------- half-near
BETA0 = mp.mpf(1679) / 8000


def halfnear_recipe(n, scale=None):
    """Literal E14-halfnear recipe (section 5) at real n: returns (e,f,g,C4) so that
    S-Lambda_c < C4+g+f r-e r^2 on 1/8<=r<=1/2 (whole-line maximisation, fixed tangent
    sqrt x<=(5/4)x+1/5, u>=(47/192)(x^2+y^2), U>=T-ebar+A4+JN/8+j).
    scale: optional dict of multiplicative factors applied to kNx/kNy linear parts."""
    s = scalars(n)
    kx, ky = s['kNx'], s['kNy']
    if scale:
        kx = kx * scale.get('k', 1)
        ky = ky * scale.get('k', 1)
    U = s['T'] - s['eorig'] + s['A4'] + s['JN'] / 8 + s['j']
    c0 = mp.mpf(47) / 192
    d1 = c0 * U - mp.mpf(15) / 32
    d2 = c0 * U + BETA0
    l1 = kx + mp.mpf(3) / 40
    l2 = ky
    e = d1 * d2 / (d1 + d2)
    f = (d2 * l1 + d1 * l2) / (d1 + d2)
    g = (l1 - l2) ** 2 / (4 * (d1 + d2))
    return dict(e=e, f=f, g=g, C4=s['C4'], d1=d1, d2=d2, l1=l1, l2=l2, U=U)


def halfnear_recipe_gap(n, rgrid=None, floor_scale=1, kscale=1):
    rec = halfnear_recipe(n, scale={'k': kscale})
    if rgrid is None:
        rgrid = [mp.mpf(1) / 8 + (mp.mpf(3) / 8) * i / 400 for i in range(401)]
    best = None
    for r in rgrid:
        up = rec['C4'] + rec['g'] + rec['f'] * r - rec['e'] * r ** 2
        fl = floor_min(n, r) * floor_scale
        gap = fl - up
        if best is None or gap < best[0]:
            best = (gap, r, fl, up)
    # small-r branch 0<=r<=1/8 (E14: curvature>2 crude) -- use same quadratic w/o JN/8
    return best, rec


def Bbeta_lower(a, q):
    """E14-halfnear (2): Bbeta >= q*b/pi^2*[log(1/b)+3/2], b=2atan(q/(2a)); 0 at q=0."""
    if q == 0:
        return mp.mpf(0)
    b = 2 * mp.atan(q / (2 * a))
    return q * b / mp.pi ** 2 * (mp.log(1 / b) + mp.mpf(3) / 2)


KAPPA = 4 * mp.quad(lambda z: mp.sqrt(1 - z ** 4), [0, 1]) / mp.pi ** 2


def halfnear_ideal_upper(n, x, y, s=None, kscale=1, keepB=True):
    """Same finite allowance (E14-halfnear (5)) but exact u, exact E11 majorant
    kappa p^{3/2}/sqrt(a) - Bbeta_lower, exact r*JN, no tangent."""
    if s is None:
        s = scalars(n)
    r = x + y
    a = (mp.cos(x) + mp.cos(y)) / 2
    u = 1 - a
    p = mp.sin(x)
    q = mp.sin(y)
    Ec = KAPPA * p ** mp.mpf(1.5) / mp.sqrt(a)
    if keepB:
        Ec -= Bbeta_lower(a, q)
    U = s['T'] - s['eorig'] + s['A4'] + r * s['JN'] + s['j']
    return Ec - u * U + s['C4'] + kscale * (s['kNx'] * x + s['kNy'] * y)


def max_on_segment(fun, r, N=200):
    best = None
    for i in range(N + 1):
        x = r * i / N
        v = fun(x, r - x)
        if best is None or v > best[0]:
            best = (v, x)
    # local refine
    v0, x0 = best
    h = r / N
    for _ in range(40):
        for x in (x0 - h, x0 + h):
            if 0 <= x <= r:
                v = fun(x, r - x)
                if v > v0:
                    v0, x0 = v, x
        h /= 2
    return v0, x0


def halfnear_ideal_gap(n, nr=60, kscale=1, floor_scale=1):
    s = scalars(n)
    best = None
    for i in range(nr + 1):
        r = mp.mpf(1) / 2 * i / nr
        if r == 0:
            continue
        up, x = max_on_segment(lambda x, y: halfnear_ideal_upper(n, x, y, s, kscale), r, N=60)
        fl = floor_min(n, r) * floor_scale
        gap = fl - up
        if best is None or gap < best[0]:
            best = (gap, r, fl, up, x)
    return best


# ---------------------------------------------------------------- annulus / wide
def wide_recipe(n, kscale=1):
    s = scalars(n)
    base = s['T'] - s['eorig'] + s['j']
    d1 = mp.mpf(11) / 48 * base - mp.mpf(5) / 12
    d2 = mp.mpf(11) / 48 * base
    l1 = kscale * s['kWx'] + mp.mpf(5) / 48
    l2 = kscale * s['kWy']
    e = d1 * d2 / (d1 + d2)
    f = (d2 * l1 + d1 * l2) / (d1 + d2)
    g = (l1 - l2) ** 2 / (4 * (d1 + d2))
    return dict(e=e, f=f, g=g, C4=s['C4'])


def wide_recipe_gap(n, kscale=1, floor_scale=1, nr=200):
    """min over r in [1/2,1] of max(-P(r), floor(r)-P(r) if r<=pi/4)."""
    w = wide_recipe(n, kscale)
    best = None
    for i in range(nr + 1):
        r = mp.mpf(1) / 2 + mp.mpf(1) / 2 * i / nr
        P = w['C4'] + w['g'] + w['f'] * r - w['e'] * r ** 2
        cand = -P
        if r <= mp.pi / 4:
            cand = max(cand, floor_min(n, r) * floor_scale - P)
        if best is None or cand < best[0]:
            best = (cand, r, P)
    return best, w


def wide_ideal_upper(n, x, y, s, kscale=1):
    r = x + y
    a = (mp.cos(x) + mp.cos(y)) / 2
    u = 1 - a
    p = mp.sin(x)
    Ec = KAPPA * p ** mp.mpf(1.5) / mp.sqrt(a)  # E11 closed pi/2 model majorant, Bbeta dropped
    U = s['T'] - s['eorig'] + s['A4'] + r * s['JW'] + s['j']
    return Ec - u * U + s['C4'] + kscale * (s['kWx'] * x + s['kWy'] * y)


def wide_ideal_gap(n, nr=50, kscale=1, floor_scale=1):
    s = scalars(n)
    best = None
    for i in range(nr + 1):
        r = mp.mpf(1) / 2 + mp.mpf(1) / 2 * i / nr
        P, x = max_on_segment(lambda x, y: wide_ideal_upper(n, x, y, s, kscale), r, N=60)
        cand = -P
        if r <= mp.pi / 4:
            cand = max(cand, floor_min(n, r) * floor_scale - P)
        if best is None or cand < best[0]:
            best = (cand, r, P, x)
    return best


# ---------------------------------------------------------------- outer E13
def outer_E13(n, use_ebar=True):
    m_ = mp
    s = scalars(n)
    n = mp.mpf(n)
    pi = mp.pi
    L = s['L']
    H = s['H']
    m = n + 1
    a0 = mp.mpf(337) / 384
    p0 = mp.mpf(12) / 25
    P0 = mp.mpf(24) / 25
    w0 = mp.mpf(721) / 384
    eta = mp.mpf(3) / 2
    u1 = mp.mpf(47) / 384
    b = 4 / pi ** 2
    hr = mp.log(mp.mpf(5) / 2) + mp.mpf(1) / 18
    eps = 3 * pi / (2 * m)
    ell = -mp.log(mp.sin(eps))
    W = (3 * mp.log(m) + mp.log(2) + 2 * mp.log(pi) + 2) / (pi * m)
    C = 1 + 8 * a0 * m / (3 * pi)
    Gamma_b = p0 * (1 + mp.log(1 + C / p0))
    gamma_b = 1 + mp.log(1 + C / p0) - C / (p0 + C)
    MA_b = p0 / pi + 4 * a0 / pi ** 2
    VB_b = 23 + (3 * Gamma_b + (2 * p0 + 6 * P0) * ell + 26 * a0 + 20) / pi
    CB_b = 6 + (4 + 4 * a0 / mp.e) / pi
    G_env = 7 * L * MA_b / m + VB_b / (2 * m) + (4 / m) * (7 + (P0 / pi) * (5 + 2 * mp.log(2 * m))) + 2 * CB_b / m
    D_env = a0 * s['Da'] + 10 / n ** 2
    R6_env = (21 + 21 * a0 + 2 * L + ((1 + 48 * p0) * H + 24 * p0) / pi) / n + (317 + mp.mpf(5) / 12) / n ** 2
    Dmesh_b = 4 * w0 / pi + a0 * b * mp.log(pi)
    Zmesh_b = Dmesh_b + a0 * b / n
    M_env = (a0 * b * (2 * L + 2 * hr) / n + (Dmesh_b + a0 * b * (L + 1 / n)) / (4 * n ** 2 - 1)
             + a0 * b / (2 * n - 1) ** 2 + (Zmesh_b + a0 * b * (mp.log(n + mp.mpf(1) / 2) + 2)) / (4 * (n - mp.mpf(1) / 2) ** 2))
    Cb = D_env + G_env + R6_env + M_env
    Cs = eta * (7 * L / (pi * m) + (3 * gamma_b + 2 * ell) / (2 * pi * m) + (48 * H + 24) / (pi * n)) + 3 * ((mp.log(2) + 4 * mp.log(pi)) / (pi * m) + W)
    Cl = (12 * ell + 16 * (5 + 2 * mp.log(2 * m))) / (pi * m)
    KD = s['KD']
    jst = mp.mpf(23) / 250
    tst = mp.mpf(221) / 500
    e0 = s['ebar'] if (use_ebar and n >= 160) else s['eminus']
    Gb = u1 * (s['T'] + jst) - tst * p0 - Cb - P0 * KD - e0
    K = s['T'] + jst - Cl - 4 * KD
    A = eta * tst + Cs
    F = Gb - A ** 2 / (4 * K) if K > 0 else None
    return dict(Gb=Gb, K=K, A=A, F=F, Cb=Cb, Cs=Cs, Cl=Cl, KD=KD, e0=e0, D_env=D_env, G_env=G_env,
                R6_env=R6_env, M_env=M_env, u1T=u1 * (s['T'] + jst))


# ---------------------------------------------------------------- far192 E15
def far_E15(n, u0=mp.mpf(7) / 24):
    s = scalars(n)
    n = mp.mpf(n)
    pi = mp.pi
    L, H = s['L'], s['H']
    m = n + 1
    u = u0
    A = 1 - u
    Cc = 2 - u
    F = 2 * mp.sqrt(u * (1 - u)) if u <= 0.5 else mp.mpf(1)
    Q = min(mp.mpf(2), mp.sqrt(8 * u))
    eps = 3 * pi / (2 * m)
    ell = -mp.log(mp.sin(eps))
    b = 4 / pi ** 2
    hr = mp.log(mp.mpf(5) / 2) + mp.mpf(1) / 18
    Dhat = A * s['Da'] + 10 / n ** 2
    Gam = F * (1 + mp.log(1 + (1 + 8 * A * m / (3 * pi)) / F))
    MA = F / pi + 4 * A / pi ** 2
    VB = 23 + (3 * Gam + (2 * F + 6 * Q) * ell + 26 * A + 20 + 2 * F * mp.log(2)) / pi
    CB = 6 + (4 + 4 * A / mp.e) / pi
    Ghat = 7 * L * MA / m + VB / (2 * m) + (4 / m) * (7 + (Q / pi) * (5 + 2 * mp.log(2 * m))) + 4 * F * mp.log(pi) / (pi * m) + 2 * CB / m
    C6 = (21 + 21 * A + 2 * L + ((1 + 48 * F) * H + 24 * F) / pi) / n + (317 + mp.mpf(5) / 12) / n ** 2
    Dbar = 4 * Cc / pi + A * b * mp.log(pi)
    Zbar = Dbar + A * b / n
    Mhat = (A * b * (2 * L + 2 * hr) / n + (Dbar + A * b * (L + 1 / n)) / (4 * n ** 2 - 1) + A * b / (2 * n - 1) ** 2
            + (Zbar + A * b * (mp.log(n + mp.mpf(1) / 2) + 2)) / (4 * (n - mp.mpf(1) / 2) ** 2))
    W = (3 * mp.log(m) + mp.log(2) + 2 * mp.log(pi) + 2) / (pi * m)
    CE = Dhat + Ghat + C6 + Mhat + F * W
    t0 = mp.mpf(221) / 500
    e0 = s['ebar'] if n >= 160 else s['eminus']
    G = u * (s['T'] + s['j']) - t0 * F - CE - s['KD'] * Q - e0
    return dict(G=G, CE=CE, Ghat=Ghat, C6=C6, e0=e0, KDQ=s['KD'] * Q, uT=u * (s['T'] + s['j']))


# ---------------------------------------------------------------- corner E12
def corner_E12(n, new_wide=False, exactq=False, exactEc=False):
    s = scalars(n)
    n = mp.mpf(n)
    pi = mp.pi
    L, H = s['L'], s['H']
    m = n + 1
    h = pi / 4
    MA = 1 / pi + 4 / pi ** 2
    g = 1 + mp.log(2 + 8 * m / (3 * pi))
    Gg = (7 * MA * L + mp.mpf(111) / 2 + (63 + mp.log(2) + 4 * mp.log(pi) + 7 * mp.log(m) + 16 * mp.log(2 * m) + mp.mpf(3) / 2 * g) / pi) / m
    W = (3 * mp.log(m) + mp.log(2) + 2 * mp.log(pi) + 2) / (pi * m)
    CEbar = s['D'] + Gg + (64 + 16 * L) / n + 318 / n ** 2 + s['Mesh'] + W
    KD = s['KD']
    M = (4 * L ** 2 + mp.mpf(79) / 5 * L) / pi ** 2 + mp.mpf(9) / 4 + CEbar + 2 * KD
    q0 = (1 - mp.cos(h)) / 2 if exactq else mp.mpf(7) / 48
    Ecax = KAPPA * (1 / mp.sqrt(2)) ** mp.mpf(1.5) / mp.sqrt((1 + 1 / mp.sqrt(2)) / 2) if exactEc else mp.mpf(1) / 4
    e0 = s['ebar'] if n >= 160 else s['eminus']
    kW = s['kWy'] if new_wide else s['kWy_old']
    dA = q0 * (s['T'] - e0 + s['j']) - Ecax - s['C4'] - h * kW
    Ecd = KAPPA / mp.sqrt(2) if exactEc else mp.mpf(4) / 15
    dD = 2 * q0 * (s['T'] + s['j']) - Ecd - CEbar - mp.mpf(3) / 2 * KD - e0
    peano = pi ** 4 / 6144
    rU = mp.mpf(2) / 125
    FA = dA - rU * M
    FD = dD - 2 * rU * M
    exact_margin = min(dA, dD / 2) - M * peano
    return dict(dA=dA, dD=dD, M=M, CEbar=CEbar, FA=FA, FD=FD, gate=min(FA, FD / 2), exact_margin=exact_margin,
                loss_coeff=16 / pi ** 2 * exact_margin)


def first_close(fun, lo, hi):
    """smallest integer n in [lo,hi] with fun(n)>0 assuming monotone; None if never."""
    if fun(hi) <= 0:
        return None
    if fun(lo) > 0:
        return lo
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if fun(mid) > 0:
            hi = mid
        else:
            lo = mid
    return hi
