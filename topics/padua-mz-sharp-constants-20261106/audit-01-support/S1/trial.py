"""S1 audit: exact Rayleigh quotient of the parity-reflected logarithmic trial p_N.
Usage: python3 -I trial.py out.json
"""
import json, sys, time
import numpy as np
from scipy.integrate import quad
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from cc_tools import cc_weights, cheb_coeffs, l2_norm_sq, l2_norm_sq_TH


def smoothstep(u):
    u = np.clip(u, 0.0, 1.0)
    with np.errstate(divide='ignore', over='ignore'):
        a = np.where(u > 0, np.exp(-1.0 / np.where(u > 0, u, 1)), 0.0)
        b = np.where(u < 1, np.exp(-1.0 / np.where(u < 1, 1 - u, 1)), 0.0)
    return a / (a + b)


def make_f(lo, hi, eps):
    def f(x):
        x = np.asarray(x, float)
        return np.cos(np.pi * x / 2) * smoothstep((x - lo) / eps) * smoothstep((hi - x) / eps)
    return f


def model_constant(f, lo, hi):
    ff = quad(lambda x: f(x) ** 2, 0, 1, points=[lo, hi], limit=400, epsabs=1e-14)[0]
    F = lambda x: quad(f, 0, x, points=[p for p in (lo, hi) if p < x], limit=400, epsabs=1e-14)[0]
    FF = quad(lambda x: F(x) ** 2, 0, 1, points=[lo, hi], limit=200, epsabs=1e-13)[0]
    return (np.pi ** 2 / 2) * ff / FF, ff, FF


def trial(N, f, check_TH=False):
    L = np.log(N)
    a = np.zeros(N + 1)
    k = np.arange(1, (N + 1) // 2 + (0 if N % 2 else 0))
    k = k[k < N / 2]
    a[k] = (N / k) * f(np.log(k) / L)
    a[N - k] = -a[k]
    v = (-1.0) ** np.arange(N + 1) * a
    w = cc_weights(N)
    Q = float(w @ v ** 2)
    b = cheb_coeffs(v)
    topcoef = b[-1]
    scale = np.max(np.abs(b))
    b = b[:-1]  # degree <= N-1 (top coefficient verified ~0 below)
    M2 = l2_norm_sq(b)
    out = dict(N=N, L=L, Q=Q, mass=M2, quotient=Q / M2, scaled=L ** 2 * Q / M2,
               B_ratio=Q / (2 * np.pi ** 2 * L), C_ratio=M2 / (4 * L ** 3),
               top_coef_rel=float(abs(topcoef) / scale))
    # parity: p(-x) = (-1)^(N-1) p(x) <=> b_j = 0 for j with parity != N-1
    wrong = b[(np.arange(N) % 2) != ((N - 1) % 2)]
    out['parity_rel'] = float(np.max(np.abs(wrong)) / scale)
    if check_TH:
        out['mass_TH_rel_diff'] = float(abs(l2_norm_sq_TH(b) - M2) / M2)
    return out


def main():
    res = dict(script='trial.py', runs=[])
    Ns_data = [100, 101, 142, 143, 200, 201, 282, 283, 400, 401, 566, 567, 800, 801, 1132, 1133, 1600, 1601,
               2262, 2263, 3200, 3201, 4526, 4527, 6400, 6401, 9050, 9051, 12800, 12801, 18102, 18103,
               25600, 25601, 36204, 36205, 51200, 51201, 72408, 72409, 102400, 102401]
    extra = [10 ** 6, 10 ** 6 + 1, 10 ** 7]
    for (lo, hi, eps) in [(0.05, 0.95, 0.05), (0.01, 0.99, 0.01)]:
        f = make_f(lo, hi, eps)
        c, ff, FF = model_constant(f, lo, hi)
        run = dict(f=f'cos(pi x/2)*smooth cutoff on ({lo},{hi}), ramp {eps}', model_constant=c,
                   f_norm_sq=ff, F_norm_sq=FF, rows=[])
        print('model constant', c, 'pi^4/8 =', np.pi ** 4 / 8, flush=True)
        for N in Ns_data + extra:
            t0 = time.time()
            r = trial(N, f, check_TH=(N <= 102401))
            r['sec'] = time.time() - t0
            run['rows'].append(r)
            print({k: (round(v, 6) if isinstance(v, float) else v) for k, v in r.items()}, flush=True)
        res['runs'].append(run)
    json.dump(res, open(sys.argv[1], 'w'), indent=1)


if __name__ == '__main__':
    main()
