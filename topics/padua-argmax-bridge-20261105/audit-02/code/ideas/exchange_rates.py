"""Exchange rates: how much each region's finite-error charges (or floors) must shrink so that
the literal E14 recipe closes at a target degree N.  MEASURED formula evaluation (mpmath, grid
in r).  escale multiplies EVERY finite-n error charge of that region (k-slopes, C4, origin ebar,
and for the outer E13 gate Cb,Cs,Cl,KD,e0); the completed-model terms (T, j, Ec, t0) are fixed.
fscale multiplies the projected-defect floors.
"""
import json
import mpmath as mp
mp.mp.dps = 25
from e14_formulas import scalars, floors, floor_min, BETA0, KAPPA

R_HN = [mp.mpf(1)/8 + (mp.mpf(3)/8)*i/96 for i in range(97)]
R_W = [mp.mpf(1)/2 + (mp.mpf(1)/2)*i/80 for i in range(81)]


def hn_gap(n, es=1, fs=1):
    s = scalars(n)
    U = s['T'] - es*s['eorig'] + s['A4'] + s['JN']/8 + s['j']
    c0 = mp.mpf(47)/192
    d1 = c0*U - mp.mpf(15)/32; d2 = c0*U + BETA0
    l1 = es*s['kNx'] + mp.mpf(3)/40; l2 = es*s['kNy']
    e = d1*d2/(d1+d2); f = (d2*l1 + d1*l2)/(d1+d2); g = (l1-l2)**2/(4*(d1+d2))
    best = None
    for r in R_HN:
        v = fs*floor_min(n, r) - (es*s['C4'] + g + f*r - e*r*r)
        if best is None or v < best[0]:
            best = (v, r)
    return best


def wide_gap(n, es=1, fs=1):
    s = scalars(n)
    base = s['T'] - es*s['eorig'] + s['j']
    d1 = mp.mpf(11)/48*base - mp.mpf(5)/12; d2 = mp.mpf(11)/48*base
    l1 = es*s['kWx'] + mp.mpf(5)/48; l2 = es*s['kWy']
    e = d1*d2/(d1+d2); f = (d2*l1 + d1*l2)/(d1+d2); g = (l1-l2)**2/(4*(d1+d2))
    best = None
    for r in R_W:
        P = es*s['C4'] + g + f*r - e*r*r
        c = -P
        if r <= mp.pi/4:
            c = max(c, fs*floor_min(n, r) - P)
        if best is None or c < best[0]:
            best = (c, r)
    return best


def outer_gap(n, es=1):
    from e14_formulas import outer_E13
    o = outer_E13(n)
    s = scalars(n)
    jst = mp.mpf(23)/250; tst = mp.mpf(221)/500; u1 = mp.mpf(47)/384
    Gb = u1*(s['T']+jst) - tst*mp.mpf(12)/25 - es*(o['Cb'] + mp.mpf(24)/25*o['KD'] + o['e0'])
    K = s['T'] + jst - es*(o['Cl'] + 4*o['KD'])
    A = mp.mpf(3)/2*tst + es*o['Cs']
    if K <= 0:
        return (mp.mpf(-10), None)
    return (Gb - A*A/(4*K), None)


def solve_scale(fun, N, lo=0.0, hi=1.0, it=30):
    """largest scale s in [lo,hi] (escale) such that fun(N,s)>0; returns None if even lo fails."""
    if fun(N, hi)[0] > 0:
        return hi
    if fun(N, lo)[0] <= 0:
        return None
    for _ in range(it):
        mid = (lo+hi)/2
        if fun(N, mid)[0] > 0:
            lo = mid
        else:
            hi = mid
    return lo


def solve_floor(fun, N, hi=20.0, it=30):
    """smallest floor factor fs>=1 with gap>0 (errors unchanged); None if > hi."""
    if fun(N, 1, 1)[0] > 0:
        return 1.0
    if fun(N, 1, hi)[0] <= 0:
        return None
    lo = 1.0
    for _ in range(it):
        mid = (lo+hi)/2
        if fun(N, 1, mid)[0] > 0:
            hi = mid
        else:
            lo = mid
    return hi


if __name__ == '__main__':
    out = []
    for N in [300, 280, 256, 224, 200, 160, 128, 96, 64]:
        row = dict(N=N)
        row['hn_escale'] = solve_scale(lambda n, s: hn_gap(n, es=s), N)
        row['hn_escale_f2'] = solve_scale(lambda n, s: hn_gap(n, es=s, fs=2), N)
        row['hn_escale_f4'] = solve_scale(lambda n, s: hn_gap(n, es=s, fs=4), N)
        row['hn_floor'] = solve_floor(lambda n, e, f: hn_gap(n, es=e, fs=f), N)
        row['wide_escale'] = solve_scale(lambda n, s: wide_gap(n, es=s), N)
        row['wide_escale_f2'] = solve_scale(lambda n, s: wide_gap(n, es=s, fs=2), N)
        row['wide_floor'] = solve_floor(lambda n, e, f: wide_gap(n, es=e, fs=f), N)
        row['outer_escale'] = solve_scale(lambda n, s: outer_gap(n, es=s), N)
        out.append(row)
        print(' '.join(f"{k}={('%.3f' % v) if isinstance(v, float) else v}" for k, v in row.items()), flush=True)
    json.dump(out, open('exchange_rates_out.json', 'w'), indent=1)
