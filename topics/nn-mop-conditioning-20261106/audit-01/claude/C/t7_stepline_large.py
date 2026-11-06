"""Balanced-terminal step-line witness of c1-gauge-invariants (3) at larger N,
original frame p1=2/5, p2=1/2, parity on second weights; independent z-moment solve."""
import sys, json, time; sys.path.insert(0, '.')
import mpmath as mp
from fractions import Fraction as Fr
from t3_param_growth_lib import terminal_b
out = []
for N in (8, 15, 24, 33, 40):
    M = N-1; n = (M+1)//2; m = M//2
    for dps in (120+9*N, 60+9*N):
        with mp.workdps(dps):
            z = [mp.mpf(2*k)/M-1 for k in range(N)]
            w1 = [mp.binomial(M, k)*mp.mpf(2)**k*mp.mpf(3)**(M-k)/mp.mpf(5)**M for k in range(N)]
            w2 = [mp.binomial(M, k)/mp.mpf(2)**M for k in range(N)]
            eps = mp.mpf(10)**(-(dps//3))
            wp = [w2[k]*(1+eps*(-1)**k) for k in range(N)]; wm = [w2[k]*(1-eps*(-1)**k) for k in range(N)]
            d = (terminal_b(z, w1, wp, n, m)-terminal_b(z, w1, wm, n, m))/(2*eps)
            b0 = terminal_b(z, w1, w2, n, m)
            if dps == 120+9*N: dhi, bhi = d, b0
    with mp.workdps(50):
        ratio = abs(dhi)*5
        lb = (4*mp.sqrt(6))**M/(4*M*(M-1))
        # PD-T437 (4) exact formula for comparison: (5^M/M)[v^(m-1)]((1-v/25)/(1-v))^n
        c = mp.taylor(lambda v: ((1-v/25)/(1-v))**n, 0, m-1)[m-1]
        formula = mp.mpf(5)**M/M*c
        rec = {'N': N, 'n_m': [n, m], 'terminal_b': mp.nstr(bhi, 15), 'expected_b=n/(5M)': mp.nstr(mp.mpf(n)/(5*M), 15),
               'ratio': mp.nstr(ratio, 15), 'PD-T437(4)': mp.nstr(formula, 15), 'rel_diff_formula': mp.nstr(abs(ratio-formula)/formula, 3),
               'bound3': mp.nstr(lb, 15), 'ok': bool(ratio >= lb), 'prec_diff': mp.nstr(abs(dhi-d)/abs(dhi), 3)}
    out.append(rec); print(json.dumps(rec), flush=True)
print('ALL_OK', all(r['ok'] for r in out))
