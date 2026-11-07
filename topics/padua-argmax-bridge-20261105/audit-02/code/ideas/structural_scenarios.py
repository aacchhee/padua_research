"""Structural what-if scenarios (MEASURED formula evaluation, planning only; none is a proof):
 B  : one-sided origin allowance e0 replaced by lam*e0 (lam=0 means a proved E_n(0)>=0) in the
      E13 outer gate, the E15 far192 gate and the E12 corner gates.
 A  : outer seam moved from rho=1 to rho=pi/2: a HYPOTHETICAL relative (origin-cancelled) wide
      allowance on the closed signed diamond rho<=pi/2 with the E14 annular coefficient formulas
      inflated by a factor c (the extension is NOT proved), using the valid cosine bound
      u>=(2/pi^2)(x^2+y^2) on rho<=pi/2 (min of (1-cos x)/(2x^2) at x=pi/2) and the E11 closed
      pi/2 model majorant kappa p^{3/2}/sqrt(a) (Bbeta dropped); E15 covers rho>=pi/2 (n>=181).
 Combined scenarios report the first integer n at which every region closes.
"""
import json
import mpmath as mp
mp.mp.dps = 25
from e14_formulas import scalars, KAPPA, outer_E13, far_E15, corner_E12, first_close
from exchange_rates import hn_gap, wide_gap


def outer_gap_e0(n, lam):
    o = outer_E13(n)
    s = scalars(n)
    jst = mp.mpf(23)/250; tst = mp.mpf(221)/500; u1 = mp.mpf(47)/384
    Gb = u1*(s['T']+jst) - tst*mp.mpf(12)/25 - o['Cb'] - mp.mpf(24)/25*o['KD'] - lam*o['e0']
    K = o['K']; A = o['A']
    return Gb - A*A/(4*K)


def far_gap_e0(n, lam):
    f = far_E15(n)
    return f['G'] + (1-lam)*f['e0']


def ext_wide_gap(n, c, r_lo=1, r_hi=mp.pi/2, nr=24, nx=40):
    s = scalars(n)
    cu = 2/mp.pi**2
    worst = None
    for i in range(nr+1):
        r = r_lo + (r_hi - r_lo)*i/nr
        best = None
        for k in range(nx+1):
            x = r*k/nx; y = r - x
            a = (mp.cos(x)+mp.cos(y))/2
            Ec = KAPPA*mp.sin(x)**mp.mpf(1.5)/mp.sqrt(a)
            U = s['T'] - s['eorig'] + s['A4'] + r*s['JW'] + s['j']
            u = cu*(x*x+y*y)
            v = Ec - u*U + c*(s['C4'] + s['kWx']*x + s['kWy']*y)
            if best is None or v > best:
                best = v
        if worst is None or -best < worst[0]:
            worst = (-best, r)
    return worst


if __name__ == '__main__':
    out = {}
    print('--- B: origin allowance scaling lam (outer E13 / far E15 first closing n)')
    for lam in [1, 0.5, 0.25, 0]:
        no = first_close(lambda n: outer_gap_e0(n, lam), 32, 400)
        nf = first_close(lambda n: far_gap_e0(n, lam), 32, 400)
        out[f'B_lam{lam}'] = dict(outer=no, far192=nf)
        print(f' lam={lam}: outer E13 closes from n={no}; far E15 closes from n={nf}', flush=True)
    print('--- A: hypothetical relative wide allowance on [1,pi/2], inflation c')
    for c in [1, 1.5, 2, 3]:
        na = first_close(lambda n: ext_wide_gap(n, c)[0], 64, 400)
        out[f'A_c{c}'] = na
        print(f' c={c}: [1,pi/2] relative primitive negative from n={na}; outer becomes max(n_A, 181)', flush=True)
    json.dump(out, open('structural_scenarios_out.json', 'w'), indent=1)
