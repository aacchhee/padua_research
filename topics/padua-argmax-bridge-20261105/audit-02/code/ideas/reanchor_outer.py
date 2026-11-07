"""Hypothetical re-anchoring of the E13 outer gate at an inner seam rho1>=1 (planning only).
The E13 geometry constants are replaced by the rho1 analogues a0=cos(rho1/2), u1=1-a0,
p0=sin(rho1/2), P0=2sqrt(2u1-u1^2), w0=1+a0 (eta=3/2 kept).  This is NOT a proved theorem; the
E13 proof of (1) was written for rho1=1 and would have to be redone.  Paired with the hypothetical
relative wide allowance on [1,rho1] (structural_scenarios.ext_wide_gap, inflation c)."""
import json
import mpmath as mp
mp.mp.dps = 25
from e14_formulas import scalars, first_close
from structural_scenarios import ext_wide_gap


def outer_reanchored(n, rho1, lam=1):
    s = scalars(n)
    n = mp.mpf(n); pi = mp.pi; L = s['L']; H = s['H']; m = n + 1
    a0 = mp.cos(mp.mpf(rho1)/2); u1 = 1 - a0
    p0 = max(mp.sin(mp.mpf(rho1)/2), mp.mpf(12)/25)
    P0 = 2*mp.sqrt(2*u1 - u1*u1); w0 = 1 + a0; eta = mp.mpf(3)/2
    b = 4/pi**2; hr = mp.log(mp.mpf(5)/2) + mp.mpf(1)/18
    eps = 3*pi/(2*m); ell = -mp.log(mp.sin(eps))
    W = (3*mp.log(m) + mp.log(2) + 2*mp.log(pi) + 2)/(pi*m)
    C = 1 + 8*a0*m/(3*pi)
    Gamma_b = p0*(1 + mp.log(1 + C/p0)); gamma_b = 1 + mp.log(1 + C/p0) - C/(p0 + C)
    MA_b = p0/pi + 4*a0/pi**2
    VB_b = 23 + (3*Gamma_b + (2*p0 + 6*P0)*ell + 26*a0 + 20)/pi
    CB_b = 6 + (4 + 4*a0/mp.e)/pi
    G_env = 7*L*MA_b/m + VB_b/(2*m) + (4/m)*(7 + (P0/pi)*(5 + 2*mp.log(2*m))) + 2*CB_b/m
    D_env = a0*s['Da'] + 10/n**2
    R6_env = (21 + 21*a0 + 2*L + ((1 + 48*p0)*H + 24*p0)/pi)/n + (317 + mp.mpf(5)/12)/n**2
    Dm = 4*w0/pi + a0*b*mp.log(pi); Zm = Dm + a0*b/n
    M_env = (a0*b*(2*L + 2*hr)/n + (Dm + a0*b*(L + 1/n))/(4*n**2 - 1) + a0*b/(2*n - 1)**2
             + (Zm + a0*b*(mp.log(n + mp.mpf(1)/2) + 2))/(4*(n - mp.mpf(1)/2)**2))
    Cb = D_env + G_env + R6_env + M_env
    Cs = eta*(7*L/(pi*m) + (3*gamma_b + 2*ell)/(2*pi*m) + (48*H + 24)/(pi*n)) + 3*((mp.log(2) + 4*mp.log(pi))/(pi*m) + W)
    Cl = (12*ell + 16*(5 + 2*mp.log(2*m)))/(pi*m)
    KD = s['KD']; jst = mp.mpf(23)/250; tst = mp.mpf(221)/500
    Gb = u1*(s['T'] + jst) - tst*p0 - Cb - P0*KD - lam*s['eorig']
    K = s['T'] + jst - Cl - 4*KD
    A = eta*tst + Cs
    return Gb - A*A/(4*K) if K > 0 else mp.mpf(-10)


if __name__ == '__main__':
    out = []
    for rho1 in [1, 1.1, 1.2, 1.3, 1.4, 1.5, float(mp.pi/2)]:
        no = first_close(lambda n: outer_reanchored(n, rho1), 32, 500)
        row = dict(rho1=rho1, outer_reanchored=no)
        for c in [1, 1.25, 1.5]:
            if rho1 > 1:
                row[f'rel_wide_c{c}'] = first_close(lambda n: ext_wide_gap(n, c, r_lo=1, r_hi=mp.mpf(rho1), nr=12)[0], 64, 500)
            else:
                row[f'rel_wide_c{c}'] = 'n/a'
        out.append(row)
        print(row, flush=True)
    json.dump(out, open('reanchor_outer_out.json', 'w'), indent=1)
