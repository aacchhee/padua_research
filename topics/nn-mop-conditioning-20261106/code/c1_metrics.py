#!/usr/bin/env python3
"""C1 analytic scalar controls and terminal diagonal gauge lower bounds.

Floating evaluations are MEASURED. No finite-difference substitution and no
whole-triangle NN Jacobian sweep. Frozen source identities are checked.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import platform
import sys
import time
import mpmath as mp

ROOT = Path(__file__).resolve().parents[3]
AD = ROOT/'topics/nn-mop-stability-20261105/code/conditioning.py'
BASE = ROOT/'topics/nn-mop-iep-20261103/code/c4_float_baseline.py'
PINS = {AD: '11c4b49be8541697e74d383b908db47b42480e11c60f92c35821340eacea929c',
        BASE: '9ce76ae88fb798f73127f75819bcdfb6c7bffb0d9cd092d70957164cb9b6a2e8'}
for path, digest in PINS.items():
    if hashlib.sha256(path.read_bytes()).hexdigest() != digest:
        raise RuntimeError(f'frozen input hash mismatch: {path}')
spec = importlib.util.spec_from_file_location('c1_frozen_ad', AD)
ad = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ad)
base = ad.base


def weighted_median_support(g, w):
    """Support of |z_i|<=1, sum w_i z_i=0, objective sum w_i*g_i*z_i."""
    pairs = sorted(zip(g, w))
    half = sum(w)/2
    cumulative = mp.mpf(0)
    median = pairs[-1][0]
    for value, mass in pairs:
        cumulative += mass
        if cumulative >= half:
            median = value
            break
    return sum(wi*abs(gi-median) for gi, wi in zip(g, w))


def row_norms(gx, gw, x, w, denom):
    dx = sum(map(abs, gx))
    dw = sum(wi*abs(gi) for wi, gi in zip(w, gw))
    constrained = weighted_median_support(gw, w)
    numerators = {'mixed': dx+dw, 'spacing': 2*dx/(len(x)-1)+dw,
                  'componentwise_nodes': sum(abs(xi*gi) for xi, gi in zip(x, gx))+dw,
                  'fixed_mass': dx+constrained}
    return {key: value/denom for key, value in numerators.items()}


def scalar_rows(x, w):
    """Return alpha,beta gradients from differentiated orthogonality.

    A_k=(x-alpha_k)p_k²-2sqrt(beta_k)p_k*p_(k-1),
    B_k=beta_k(p_k²-p_(k-1)²). The corresponding gradients are
    g_w=f(x_l), g_x=w_l*f'(x_l).
    """
    N = len(x)
    p0 = 1/mp.sqrt(sum(w))
    prev, cur = [mp.mpf(0)]*N, [p0]*N
    dprev, dcur = [mp.mpf(0)]*N, [mp.mpf(0)]*N
    b = mp.mpf(0)
    alphas, betas, rows = [], [], []
    for k in range(N):
        alpha = sum(wi*xi*pi*pi for wi, xi, pi in zip(w, x, cur))
        alphas.append(alpha)
        betas.append(b*b)
        fa = [(xi-alpha)*pi*pi-2*b*pi*qi for xi, pi, qi in zip(x, cur, prev)]
        dfa = [pi*pi+2*(xi-alpha)*pi*dpi-2*b*(dpi*qi+pi*dqi)
               for xi, pi, dpi, qi, dqi in zip(x, cur, dcur, prev, dprev)]
        fb = [b*b*(pi*pi-qi*qi) for pi, qi in zip(cur, prev)]
        dfb = [2*b*b*(pi*dpi-qi*dqi) for pi, dpi, qi, dqi in zip(cur, dcur, prev, dprev)]
        rows.append({'alpha': (fa, [wi*gi for wi, gi in zip(w, dfa)]),
                     'beta': (fb, [wi*gi for wi, gi in zip(w, dfb)])})
        if k+1 < N:
            residual = [(xi-alpha)*pi-b*qi for xi, pi, qi in zip(x, cur, prev)]
            dresidual = [pi+(xi-alpha)*dpi-b*dqi for xi, pi, dpi, dqi in zip(x, cur, dcur, dprev)]
            next_b = mp.sqrt(sum(wi*ri*ri for wi, ri in zip(w, residual)))
            prev, cur = cur, [ri/next_b for ri in residual]
            dprev, dcur = dcur, [ri/next_b for ri in dresidual]
            b = next_b
    return alphas, betas, rows


def scalar_case(N, family, dps, verify=False):
    started = time.monotonic()
    xq, wq = base.inputs(N, family)
    x = [base.convert(v, mp.mpf) for v in xq]
    out = []
    for s, ws in enumerate(wq):
        w = [base.convert(v, mp.mpf) for v in ws]
        alpha, beta, rows = scalar_rows(x, w)
        symmetric = ws == list(reversed(ws))
        scale_alpha = mp.mpf(1) if symmetric else max(map(abs, alpha))
        scale_beta = max(beta)
        scale_sqrt = mp.sqrt(scale_beta)
        norms = {metric: {model: mp.mpf(0) for model in ('mixed', 'spacing', 'componentwise_nodes', 'fixed_mass')}
                 for metric in ('monic', 'orthonormal')}
        locations = {metric: {} for metric in norms}
        for k, row in enumerate(rows):
            for field, (gw, gx) in row.items():
                for metric in norms:
                    denom = scale_alpha if field == 'alpha' else scale_beta
                    if metric == 'orthonormal' and field == 'beta':
                        if not k:
                            continue
                        factor = 1/(2*mp.sqrt(beta[k]))
                        gw0, gx0 = [v*factor for v in gw], [v*factor for v in gx]
                        denom = scale_sqrt
                    else:
                        gw0, gx0 = gw, gx
                    values = row_norms(gx0, gw0, x, w, denom)
                    for model, value in values.items():
                        if value > norms[metric][model]:
                            norms[metric][model] = value
                            locations[metric][model] = [field, k]
        record = {'marginal': s+1, 'alpha_scale': str(scale_alpha),
                  'alpha_scale_convention': 'absolute one; exact symmetry gives zero field' if symmetric else 'field sup',
                  'kappa': {metric: {model: str(value) for model, value in values.items()} for metric, values in norms.items()},
                  'maximizer': locations}
        if verify:
            # A distinct forward-AD path on every scalar coefficient/coordinate.
            xd, wd = ad.seed_inputs(xq, wq)
            da, db = ad.marginal(xd, wd[s])
            err = mp.mpf(0)
            for k, row in enumerate(rows):
                for field, dual in (('alpha', da[k]), ('beta', db[k])):
                    gw, gx = row[field]
                    expected = gx+[mp.mpf(0)]*(2*N)
                    expected[(s+1)*N:(s+2)*N] = gw
                    for a, b in zip(dual.g or [mp.mpf(0)]*(3*N), expected):
                        err = max(err, abs(a-b)/max(1, abs(a), abs(b)))
            record['forward_AD_max_scaled_entry_difference'] = str(err)
        out.append(record)
    return {'N': N, 'family': family, 'dps': dps, 'marginals': out,
            'elapsed_seconds': time.monotonic()-started}


def terminal_row(x, w, n, m):
    """One terminal b=t_nu+sum x_l, using a moment solve and adjoint."""
    N, k = len(x), len(x)-1
    indices = [(s, r) for s, count in enumerate((n, m)) for r in range(count)]
    powers = [[xi**j for j in range(2*N)] for xi in x]
    mu = [[sum(wi*row[j] for wi, row in zip(ws, powers)) for j in range(2*N)] for ws in w]
    A = mp.matrix([[mu[s][r+j] for j in range(k)] for s, r in indices])
    c = mp.lu_solve(A, mp.matrix([-mu[s][r+k] for s, r in indices]))
    rhs = mp.matrix(k, 1)
    rhs[k-1] = 1
    adjoint = mp.lu_solve(A.T, rhs)
    poly = [sum(c[j]*row[j] for j in range(k))+row[k] for row in powers]
    deriv = [sum(j*c[j]*row[j-1] for j in range(1, k))+k*row[k-1] for row in powers]
    gx, gw = [mp.mpf(1)]*N, [[mp.mpf(0)]*N for _ in w]
    for z, (s, r) in zip(adjoint, indices):
        for ell in range(N):
            xr = powers[ell][r]
            gw[s][ell] -= z*xr*poly[ell]
            gx[ell] -= z*w[s][ell]*(xr*deriv[ell]+(r*powers[ell][r-1]*poly[ell] if r else 0))
    return c[k-1]+sum(x), gx, gw


def terminal_case(N, family, dps, verify=False):
    started = time.monotonic()
    xq, wq = base.inputs(N, family)
    x = [base.convert(v, mp.mpf) for v in xq]
    w = [[base.convert(v, mp.mpf) for v in row] for row in wq]
    fields, _ = base.layers(N, *(base.marginal(x, row) for row in w))
    n, m = N//2, (N-1)//2
    value, gx, gw = terminal_row(x, w, n, m)
    scales = {f: max(abs(row[f]) for row in fields.values()) for f in ('b1', 'b2')}
    step = ad.step_line({nu: {f: ad.Dual(v) for f, v in row.items()} for nu, row in fields.items()}, N)
    scale_beta = max(abs(row['beta'].v) for row in step.values())
    dx = sum(map(abs, gx))
    dw = sum(wi*abs(gi) for ws, gs in zip(w, gw) for wi, gi in zip(ws, gs))
    fixed = sum(weighted_median_support(gs, ws) for gs, ws in zip(gw, w))
    numerator = {'mixed': dx+dw, 'spacing': 2*dx/(N-1)+dw,
                 'componentwise_nodes': sum(abs(xi*gi) for xi, gi in zip(x, gx))+dw,
                 'fixed_mass': dx+fixed}
    result = {'N': N, 'family': family, 'dps': dps, 'terminal_index': [n, m],
              'terminal_b': str(value), 'b_scales': {key: str(v) for key, v in scales.items()},
              'step_beta_scale': str(scale_beta),
              'NN_gauge_lower': {model: str(num/min(scales.values())) for model, num in numerator.items()},
              'step_gauge_lower': {model: str(num/scale_beta) for model, num in numerator.items()},
              'node_numerator': str(dx), 'weight_numerator': str(dw),
              'base_layer_terminal_value_difference': str(abs(value-fields[n, m]['b1']))}
    if verify:
        xd, wd = ad.seed_inputs(xq, wq)
        direct = ad.layers(N, *(ad.marginal(xd, row) for row in wd))[n, m]['b1']
        gradient = gx+gw[0]+gw[1]
        result['forward_AD_max_scaled_entry_difference'] = str(max(abs(a-b)/max(1, abs(a), abs(b)) for a, b in zip(gradient, direct.g)))
    result['elapsed_seconds'] = time.monotonic()-started
    return result


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--mode', choices=('scalar', 'terminal'), required=True)
    ap.add_argument('--family', choices=('krawtchouk', 'hahn'), required=True)
    ap.add_argument('--sizes', nargs='+', type=int, default=list(range(4, 65)))
    ap.add_argument('--dps', type=int, default=180)
    ap.add_argument('--verify', action='store_true')
    args = ap.parse_args()
    started = time.monotonic()
    result = {'status': 'MEASURED; floating analytic derivative evaluation',
              'source_commit': 'b4a04981d42c7cd872957facf5e3995e4096ca67',
              'python': platform.python_version(), 'mpmath': mp.__version__,
              'argv': sys.argv[1:], 'code_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'dependencies': {str(p.relative_to(ROOT)): digest for p, digest in PINS.items()}, 'cases': []}
    for N in args.sizes:
        with mp.workdps(args.dps):
            fn = scalar_case if args.mode == 'scalar' else terminal_case
            row = fn(N, args.family, args.dps, verify=args.verify)
        result['cases'].append(row)
        print(json.dumps({'N': N, 'family': args.family, 'seconds': row['elapsed_seconds']}), file=sys.stderr, flush=True)
    result['elapsed_seconds'] = time.monotonic()-started
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
