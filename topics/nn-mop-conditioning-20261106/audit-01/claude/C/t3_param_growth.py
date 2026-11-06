"""High-precision terminal parity responses for larger N (independent moment solves in z,
central FD in epsilon), compared with the parameter lower bound and identity (11)."""
import sys, json, time
import mpmath as mp
from fractions import Fraction as Fr
from math import comb

def terminal_b(z, w1, w2, n, m):
    M = n+m
    rows, rhs = [], []
    for w, cnt in ((w1, n), (w2, m)):
        for r in range(cnt):
            rows.append([mp.fsum(w[l]*z[l]**(r+j) for l in range(len(z))) for j in range(M)])
            rhs.append(-mp.fsum(w[l]*z[l]**(r+M) for l in range(len(z))))
    c = mp.lu_solve(mp.matrix(rows), mp.matrix(rhs))
    return c[M-1] + mp.fsum(z)

def run(p1, p2, N, dps, perturb, eps):
    with mp.workdps(dps):
        M = N-1
        z = [mp.mpf(2*k)/M-1 for k in range(N)]
        P = [mp.mpf(p.numerator)/p.denominator for p in (p1, p2)]
        w = [[mp.binomial(M, k)*Pp**k*(1-Pp)**(M-k) for k in range(N)] for Pp in P]
        resp = []
        for n in range(M):
            m = M-n
            wp = [list(w[0]), list(w[1])]; wm = [list(w[0]), list(w[1])]
            wp[perturb] = [w[perturb][k]*(1+eps*(-1)**k) for k in range(N)]
            wm[perturb] = [w[perturb][k]*(1-eps*(-1)**k) for k in range(N)]
            d = (terminal_b(z, wp[0], wp[1], n, m)-terminal_b(z, wm[0], wm[1], n, m))/(2*eps)
            resp.append(d)
        return resp

def theory(p1, p2, M):
    P1, P2 = mp.mpf(p1.numerator)/p1.denominator, mp.mpf(p2.numerator)/p2.denominator
    s = max(abs(1-2*P1), abs(1-2*P2)); qs = min(P1*(1-P1), P2*(1-P2))
    A = (P1+P2-2*P1*P2)/abs(P2-P1); rho = A+mp.sqrt(A*A-1)
    return s, qs, rho, A

def orient(p1, p2):
    if abs(1-2*p1) > abs(1-2*p2):   # swap
        p1, p2 = p2, p1
    if p2 < Fr(1, 2):               # reflect
        p1, p2 = 1-p1, 1-p2
    assert p1 < p2
    return p1, p2

out = []
pairs = [(Fr(2,5),Fr(1,2)), (Fr(1,5),Fr(2,5)), (Fr(1,3),Fr(2,3)), (Fr(1,10),Fr(9,10)), (Fr(9,20),Fr(11,20)), (Fr(3,10),Fr(1,2))]
for p1, p2 in pairs:
    o1, o2 = orient(p1, p2)
    for N in (6, 12, 20, 28, 36):
        M = N-1
        t0 = time.time()
        dps = 120 + 9*N
        eps = mp.mpf(10)**(-(dps//3))
        resp = run(o1, o2, N, dps, 1, eps)          # oriented frame, parity on second
        resp_lo = run(o1, o2, N, dps-60, 1, mp.mpf(10)**(-((dps-60)//3)))
        with mp.workdps(60):
            prec = max(abs(a-b)/max(abs(a), mp.mpf('1e-300')) for a, b in zip(resp, resp_lo))
            s, qs, rho, A = theory(p1, p2, M)
            mx = max(abs(r) for r in resp)
            bound = 2*qs/(s*M*M)*(rho**(M-1)+rho**(-(M-1)))
            # identity (11): sum (-1)^n dot B (integer coords) = coefficient
            O1, O2 = mp.mpf(o1.numerator)/o1.denominator, mp.mpf(o2.numerator)/o2.denominator
            e = 2*O2-1
            cos = [(rho**L+rho**(-L))/2 for L in range(M)]
            coeff = 2*O2*(1-O2)*mp.fsum((j+1)*e**j*cos[M-1-j] for j in range(M))
            signed = mp.fsum((-1)**n*resp[n]*M/2 for n in range(M))
            rec = {'p1': str(p1), 'p2': str(p2), 'oriented': [str(o1), str(o2)], 'N': N, 'dps': dps,
                   'max_terminal_ratio': mp.nstr(mx/s, 15), 'bound1': mp.nstr(bound, 15),
                   'ratio_over_bound': mp.nstr(mx/s/bound, 8), 'ok': bool(mx/s >= bound),
                   'signed_sum_integer': mp.nstr(signed, 20), 'identity11': mp.nstr(coeff, 20),
                   'identity_rel_err': mp.nstr(abs(signed-coeff)/abs(coeff), 3),
                   'max_root_M': mp.nstr((mx/s)**(mp.mpf(1)/M), 10), 'rho': mp.nstr(rho, 12),
                   'precision_rel_diff': mp.nstr(prec, 3), 'seconds': round(time.time()-t0, 1)}
        out.append(rec); print(json.dumps(rec), flush=True)
json.dump(out, open('t3_param_growth.json', 'w'), indent=1)
print('ALL_OK', all(r['ok'] for r in out), 'max identity err', max(float(r['identity_rel_err']) for r in out),
      'max prec diff', max(float(r['precision_rel_diff']) for r in out))
