"""Full-Jacobian check of c2-krawtchouk-parameter-lower (1), its fixed-mass half,
and PD-T437(13) specialization, with independent FD derivatives."""
import sys, json, time; sys.path.insert(0, '.')
import mpmath as mp
from fractions import Fraction as Fr
from indep_nn import *
mp.mp.dps = 70
H = mp.mpf('1e-28')

def wmed_support(g, w):
    # independent: minimize sum w|g-lam| over lam in the finite set {g}
    return min(sum(wi*abs(gi-lam) for gi, wi in zip(g, w)) for lam in g)

def fixed_mass_support(row, q, N):
    x, w = q
    return sum(abs(row[l]) for l in range(N)) + wmed_support(row[N:2*N], w[0]) + wmed_support(row[2*N:3*N], w[1])

pairs = [(Fr(2,5),Fr(1,2)), (Fr(1,5),Fr(2,5)), (Fr(1,3),Fr(2,3)), (Fr(3,5),Fr(4,5)), (Fr(1,10),Fr(9,10)),
         (Fr(7,10),Fr(1,2)), (Fr(1,20),Fr(3,20)), (Fr(9,20),Fr(11,20))]
results = []
for p1, p2 in pairs:
    P1, P2 = mp.mpf(p1.numerator)/p1.denominator, mp.mpf(p2.numerator)/p2.denominator
    s = max(abs(1-2*P1), abs(1-2*P2))
    qstar = min(P1*(1-P1), P2*(1-P2))
    A = (P1+P2-2*P1*P2)/abs(P2-P1)
    rho = A + mp.sqrt(A*A-1)
    rho_closed = (P1+P2-2*P1*P2+2*mp.sqrt(P1*P2*(1-P1)*(1-P2)))/abs(P2-P1)
    # marginal to perturb by parity: largest |1-2p|
    sstar = 0 if abs(1-2*P1) >= abs(1-2*P2) else 1
    sym = [k for k, P in enumerate((P1, P2)) if P == mp.mpf(1)/2]
    for N in range(2, 9):
        M = N-1
        q = inputs(N, 'krawtchouk', p1, p2)
        t0 = time.time()
        base, J = jacobian(lambda qq: nn_map(*qq)[0], q, N, H)
        kappa, arg, per, sc = condition(base, J, q, N)
        sc_all = scales_of(base, list(J))
        kfm = max(fixed_mass_support(J[k], q, N)/sc_all[k[0]] for k in J)
        # parity witness on marginal sstar, terminal sites
        def parity_resp(smarg, direction=None):
            w = q[1][smarg]
            vals = []
            for n in range(0, M+1):
                m = M-n
                for f in ('b1', 'b2'):
                    row = J[(f, (n, m))]
                    d = sum(row[N*(1+smarg)+l]*w[l]*(-1)**l for l in range(N))
                    vals.append(((n, m), f, d))
            return vals
        pr = parity_resp(sstar)
        maxresp = max(abs(d) for _, f, d in pr if f == 'b2' or True)
        bound1 = 2*qstar/(s*M*M)*(rho**(M-1)+rho**(-(M-1)))
        rec = {'p1': str(p1), 'p2': str(p2), 'N': N, 'kappa': mp.nstr(kappa, 12), 'kappa_fixed_mass': mp.nstr(kfm, 12),
               'argmax': str(arg), 'b_scales': [mp.nstr(sc['b1'], 12), mp.nstr(sc['b2'], 12)], 's': mp.nstr(s, 12),
               'parity_max_terminal_ratio': mp.nstr(maxresp/s, 12), 'bound1': mp.nstr(bound1, 12),
               'ok_kappa_ge_bound1': bool(kappa >= bound1*(1-mp.mpf('1e-30'))),
               'ok_parity_ge_bound1': bool(maxresp/s >= bound1*(1-mp.mpf('1e-30'))),
               'ok_fixedmass_ge_half': bool(kfm >= bound1/2*(1-mp.mpf('1e-30'))),
               'rho': mp.nstr(rho, 15), 'rho_closed_diff': mp.nstr(abs(rho-rho_closed), 3),
               'scale_check': mp.nstr(max(abs(sc['b1']-s), abs(sc['b2']-s)), 3),
               'seconds': round(time.time()-t0, 2)}
        if sym:
            ss = sym[0]
            pr2 = parity_resp(ss)
            mr2 = max(abs(d) for _, _, d in pr2)
            b2 = 1/(2*s*M*M)*(rho**(M-1)+rho**(-(M-1)))
            rec['sym_parity_ratio'] = mp.nstr(mr2/s, 12)
            rec['sym_bound'] = mp.nstr(b2, 12)
            rec['ok_sym'] = bool(mr2/s >= b2*(1-mp.mpf('1e-30')))
            # mass of symmetric parity
            rec['sym_parity_mass'] = mp.nstr(sum(q[1][ss][l]*(-1)**l for l in range(N)), 3)
            rec['ok_kfm_ge_sym'] = bool(kfm >= b2*(1-mp.mpf('1e-30')))
        results.append(rec)
        print(json.dumps(rec), flush=True)
json.dump(results, open('t2_param_lower.json', 'w'), indent=1)
print('ALL_OK', all(r['ok_kappa_ge_bound1'] and r['ok_parity_ge_bound1'] and r['ok_fixedmass_ge_half'] and r.get('ok_sym', True) and r.get('ok_kfm_ge_sym', True) for r in results))
