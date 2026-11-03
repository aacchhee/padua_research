"""Claude audit-01 auditor B: high-precision check of gated-06 cusp S_n(alpha,0)=Lc+L_n|alpha|+o(|alpha|),
the n=2 exception, the beta-direction (no linear term), N01 failure of a pure quadratic bound, and that the
ACTUAL Lebesgue function has no linear cusp at the nonnode corner (obstruction not transferred).
Independent kernel (Fourier sum, PD-T185 (5)); independent Lagrange lambda. MEASURED, mpmath 60 digits."""
import mpmath as mp, json, sys
sys.path.insert(0, sys.argv[1])
mp.mp.dps = 60
pi = mp.pi
def Dfour(n, u, v):
    cu = [mp.cos(p*u) for p in range(n+1)]; cv = [mp.cos(q*v) for q in range(n+1)]
    return sum((1 if p == 0 else 2)*(1 if q == 0 else 2)*cu[p]*cv[q] for p in range(n+1) for q in range(n+1-p))
def S(n, al, be):
    m = n+1; s = mp.mpf(0)
    for j in range(2*n):
        for r in range(2*m):
            if (j+r) % 2:
                u, v = j*pi/n + al/n, r*pi/m + be/m
                s += abs(Dfour(n, u, v) - mp.cos(n*u))/2
    return s/(n*m)
def Ln(n):
    return sum(mp.cot(k*pi/n) for k in range(1, n//2 + 1))/(n*(n+1))
from indep_identities_lib import lagrange_lebesgue
rows = []
for n in range(2, 13):
    Lc = S(n, 0, 0)
    a = mp.mpf('1e-20')
    sp_ = (S(n, a, 0) - Lc)/a; sm = (S(n, -a, 0) - Lc)/a
    a2 = mp.mpf('1e-10')
    sec = (S(n, a2, 0) - Lc - Ln(n)*a2)/a2**2
    beta_slope = (S(n, 0, a) - Lc)/a
    row = {'n': n, 'Lc': mp.nstr(Lc, 25), 'slope_plus': mp.nstr(sp_, 25), 'slope_minus': mp.nstr(sm, 25),
           'L_n': mp.nstr(Ln(n), 25), 'slope_minus_L_n': mp.nstr(sp_ - Ln(n), 5),
           'second_order_coef_est': mp.nstr(sec, 8), 'beta_direction_slope': mp.nstr(beta_slope, 5)}
    # N01: (S - a Lc)/alpha^2 blows up for n>=3 as alpha->0
    vals = []
    for e in (4, 8, 12):
        al = mp.mpf(10)**(-e)
        A = (mp.cos(al) + 1)/2
        vals.append(mp.nstr((S(n, al, 0) - A*Lc)/al**2, 6))
    row['N01_ratio_(S-aLc)/alpha^2_at_1e-4,1e-8,1e-12'] = vals
    if n <= 9:
        lamc, _ = lagrange_lebesgue(n, mp.mpf(-1), mp.mpf(-1))
        row['lagrange_corner_minus_Lc'] = mp.nstr(lamc - Lc, 5)
        t = mp.mpf('1e-12')
        l1, _ = lagrange_lebesgue(n, mp.cos(pi - t), mp.mpf(-1))
        l2, _ = lagrange_lebesgue(n, mp.mpf(-1), mp.cos(pi - t))
        l3, _ = lagrange_lebesgue(n, mp.cos(pi - t), mp.cos(pi - t))
        row['actual_lambda_slope_along_x_edge'] = mp.nstr((l1 - lamc)/t, 5)
        row['actual_lambda_slope_along_y_edge'] = mp.nstr((l2 - lamc)/t, 5)
        row['actual_lambda_slope_diagonal'] = mp.nstr((l3 - lamc)/t, 5)
        row['actual_lambda_second_order_x'] = mp.nstr((l1 - lamc)/t**2, 8)
    rows.append(row)
    print(json.dumps(row))
