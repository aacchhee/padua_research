#!/usr/bin/env python3
"""Direct finite-sum re-validation of a FINAL-HYBRID receipt (audit G-assembly).

For each retained S key (a,b) (phase turns), compute an Arb enclosure of
  S^t(a,b) = (1/(2N)) sum_{0<=r<2n,0<=s<2m,r+s odd} |G_n((r+a)pi/n,(s+b)pi/m)|
directly from PD-T364 (4), with
  G_n(u,v) = R_{n+1}(p)R_{n+1}(q) + R_n(p)R_n(q) - cos(nu), p=(u+v)/2, q=(u-v)/2,
  R_k(z) = sin(kz)/sin z, continuous value k(-1)^((k-1)l) at z=l*pi (exact
  rational detection; phases are rational multiples of pi).
For each actual corner point (xi,zeta turns) compute lambda_n directly by the
four-copy cardinal formula PD-T364 (1):
  lambda = sum_{j+k even} (w_jk/4) |sum_{sigma,eta} G(theta+sigma j pi/n, phi+eta k pi/m)|,
  theta = pi - xi, phi = pi - zeta  (canonical chart at (-1,-1)).
The origin S(0,0)=Lambda_c gives a fresh lower L.
Checks: every native upper >= our lower (soundness of engine uppers at these
points) and native L <= our upper; then rerun the rational predicates with
OUR uppers/L substituted (no D23/C02/C06/N5/D06/C11 truncation theorem used).
Uses the same Arb library family (python-flint) but none of the engine code.
"""
import json, sys, copy
from fractions import Fraction as Fr
from flint import arb, fmpq, ctx
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import phase_rational_indep as PRI
ctx.prec = 160

def q(fr): return fmpq(fr.numerator, fr.denominator)

def R(k, zt):
    # zt = z/pi as Fraction
    if zt.denominator == 1:
        l = zt.numerator
        return arb(k * (-1) ** (((k - 1) * l) % 2))
    return arb(q(k * zt)).sin_pi() / arb(q(zt)).sin_pi()

def G(n, ut, vt):
    pt = (ut + vt) / 2; qt = (ut - vt) / 2
    return R(n + 1, pt) * R(n + 1, qt) + R(n, pt) * R(n, qt) - arb(q(n * ut)).cos_pi()

def S_direct(n, a, b):
    m = n + 1; N = n * m; s_ = arb(0)
    for r in range(2 * n):
        ut = Fr(r, 1) / n + a / n
        for s in range((r + 1) % 2, 2 * m, 2):
            vt = Fr(s, 1) / m + b / m
            s_ += abs(G(n, ut, vt))
    return s_ / (2 * N)

def lam_direct(n, xi, zeta):
    m = n + 1; N = n * m
    th = 1 - xi; ph = 1 - zeta  # turns
    tot = arb(0)
    for j in range(n + 1):
        ej = Fr(1, 2) if j in (0, n) else Fr(1)
        for k in range((j % 2), m + 1, 2):
            fk = Fr(1, 2) if k in (0, m) else Fr(1)
            w = 2 * ej * fk / N
            v = arb(0)
            for sg in (1, -1):
                for et in (1, -1):
                    v += G(n, th + sg * Fr(j, n), ph + et * Fr(k, m))
            tot += arb(q(w / 4)) * abs(v)
    return tot

def run(path):
    d = json.load(open(path)); n = int(d['n'])
    out = {'file': path.split('/')[-1], 'n': n, 'S_points': 0, 'native_upper_valid': True, 'worst_native_minus_direct_upper': None}
    newrows = []; worst = None
    for a, b, h in d['S_upper_rows']:
        val = S_direct(n, Fr(a), Fr(b)); nat = PRI.hexfr(h)
        lo = Fr(val.lower().mid().str(30, radius=False)) if False else None
        # rigorous comparisons via arb
        natb = arb(q(nat))
        if not (natb >= val):  # certain-only: native upper >= every point of our ball
            out['native_upper_valid'] = False
        up = val.upper(); upfr = Fr(up.mid().man_exp()[0]) * Fr(2) ** up.mid().man_exp()[1] if False else None
        # our upper as exact rational: use mid+rad rounded up to 2^-100 grid
        mid = val.mid(); rad = val.rad()
        mn, me = mid.man_exp(); rn, re_ = rad.man_exp()
        U = Fr(int(mn)) * Fr(2) ** int(me) + Fr(int(rn)) * Fr(2) ** int(re_)
        U = Fr(-((-U * 2 ** 100) // 1), 2 ** 100)
        gap = nat - U; worst = gap if worst is None else min(worst, gap)
        newrows.append([a, b, U]); out['S_points'] += 1
    out['worst_native_minus_direct_upper'] = float(worst)
    # origin lower
    S00 = S_direct(n, Fr(0), Fr(0)); mid = S00.mid(); rad = S00.rad()
    mn, me = mid.man_exp(); rn, re_ = rad.man_exp()
    Lmine = Fr(int(mn)) * Fr(2) ** int(me) - Fr(int(rn)) * Fr(2) ** int(re_)
    Lmine = Fr((Lmine * 2 ** 100) // 1, 2 ** 100)
    Lnat = PRI.hexfr(d['origin_lower_hex'])
    out['native_L_valid'] = bool(arb(q(Lnat)) <= S00)
    out['L_direct'] = float(Lmine); out['L_native'] = float(Lnat)
    lamrows = []
    if d.get('lambda_upper_rows'):
        for x, y, h in d['lambda_upper_rows']:
            val = lam_direct(n, Fr(x), Fr(y)); nat = PRI.hexfr(h)
            ok = bool(arb(q(nat)) >= val)
            out['native_upper_valid'] = out['native_upper_valid'] and ok
            mid = val.mid(); rad = val.rad(); mn, me = mid.man_exp(); rn, re_ = rad.man_exp()
            U = Fr(int(mn)) * Fr(2) ** int(me) + Fr(int(rn)) * Fr(2) ** int(re_)
            U = Fr(-((-U * 2 ** 100) // 1), 2 ** 100)
            lamrows.append([x, y, U]); out.setdefault('lambda_native_minus_direct', []).append(float(nat - U))
    # substitute and rerun the independent rational predicates
    d2 = copy.deepcopy(d)
    tmp_rows = [[a, b, None] for a, b, _ in newrows]
    PRI_hex_backup = PRI.hexfr
    table = {('S', a, b): U for a, b, U in newrows}
    table.update({('L',): Lmine}); table.update({('lam', x, y): U for x, y, U in lamrows})
    d2['S_upper_rows'] = [[a, b, ('S', a, b)] for a, b, _ in newrows]
    d2['origin_lower_hex'] = ('L',)
    d2['lambda_upper_rows'] = [[x, y, ('lam', x, y)] for x, y, _ in lamrows]
    PRI.hexfr = lambda h: table[tuple(h)] if isinstance(h, (tuple, list)) else PRI_hex_backup(h)
    tmp = path + '.direct-substituted.json'
    import tempfile, os
    fd, tp = tempfile.mkstemp(suffix='.json', dir=__file__.rsplit('/', 1)[0]); os.close(fd)
    json.dump(d2, open(tp, 'w'))
    try:
        res = PRI.verify(tp)
    finally:
        PRI.hexfr = PRI_hex_backup; os.remove(tp)
    out['predicates_with_direct_enclosures'] = {k: res[k] for k in ('method', 'M', 'grid_bound', 'counts', 'min_far_margin', 'min_near_margin', 'corner', 'ok')}
    return out

if __name__ == '__main__':
    print(json.dumps([run(p) for p in sys.argv[1:]], indent=1, default=str))
