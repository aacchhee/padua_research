"""Independent scalar Jacobi controls (Stieltjes on monic polynomials + FD Jacobian)
compared with the reproduced c1_metrics scalar raw outputs; LP check of the
weighted-median fixed-mass dual (including the producer's function)."""
import sys, json, random; sys.path.insert(0, '.')
import mpmath as mp
import numpy as np
from scipy.optimize import linprog
from indep_nn import inputs
mp.mp.dps = 80
H = mp.mpf('1e-30')
RAW = 'raw'

def monic_jacobi(x, w):
    N = len(x)
    Pm, P = [mp.mpf(0)]*N, [mp.mpf(1)]*N
    alphas, betas = [], []
    hprev = None
    for k in range(N):
        h = mp.fsum(wi*pi*pi for wi, pi in zip(w, P))
        alpha = mp.fsum(wi*xi*pi*pi for wi, xi, pi in zip(w, x, P))/h
        beta = h/hprev if hprev is not None else mp.mpf(0)
        alphas.append(alpha); betas.append(beta)
        Pn = [(xi-alpha)*pi-beta*qi for xi, pi, qi in zip(x, P, Pm)]
        Pm, P, hprev = P, Pn, h
    return alphas, betas

def wmed(g, w):
    return min(mp.fsum(wi*abs(gi-l) for gi, wi in zip(g, w)) for l in g)

def conds(x, w, symmetric):
    N = len(x)
    a0, b0 = monic_jacobi(x, w)
    def F(xx, ww):
        a, b = monic_jacobi(xx, ww)
        return a+b[1:]+[mp.sqrt(v) for v in b[1:]]
    base = F(x, w)
    cols = []
    for i in range(2*N):
        xp, xm, wp, wm = list(x), list(x), list(w), list(w)
        if i < N: xp[i] += H; xm[i] -= H
        else: wp[i-N] += H; wm[i-N] -= H
        fp, fm = F(xp, wp), F(xm, wm)
        cols.append([(u-v)/(2*H) for u, v in zip(fp, fm)])
    J = [[cols[i][r] for i in range(2*N)] for r in range(len(base))]
    sa = mp.mpf(1) if symmetric else max(abs(v) for v in a0)
    sb = max(b0[1:]); ss = mp.sqrt(sb)
    res = {}
    for metric in ('monic', 'orthonormal'):
        for model in ('mixed', 'spacing', 'componentwise_nodes', 'fixed_mass'):
            best = mp.mpf(0)
            rows = list(range(N)) + (list(range(N, 2*N-1)) if metric == 'monic' else list(range(2*N-1, 3*N-2)))
            for r in rows:
                den = sa if r < N else (sb if r < 2*N-1 else ss)
                gx, gw = J[r][:N], J[r][N:]
                if model == 'mixed': nx = mp.fsum(abs(v) for v in gx)
                elif model == 'spacing': nx = mp.mpf(2)/(N-1)*mp.fsum(abs(v) for v in gx)
                elif model == 'componentwise_nodes': nx = mp.fsum(abs(v*xi) for v, xi in zip(gx, x))
                else: nx = mp.fsum(abs(v) for v in gx)
                nw = wmed(gw, w) if model == 'fixed_mass' else mp.fsum(wi*abs(v) for wi, v in zip(w, gw))
                best = max(best, (nx+nw)/den)
            res[(metric, model)] = best
    return res

worst = mp.mpf(0); count = 0; rows_out = []
for family in ('krawtchouk', 'hahn'):
    raw = json.load(open(f'{RAW}/c1-scalar-{family}260.json'))
    bycase = {c['N']: c for c in raw['cases']}
    for N in list(range(4, 13)) + [16, 20]:
        x, ws = inputs(N, family)
        for s in (0, 1):
            w = ws[s]
            sym = all(abs(w[l]-w[N-1-l]) == 0 for l in range(N))
            mine = conds(x, w, sym)
            theirs = bycase[N]['marginals'][s]['kappa']
            for (metric, model), v in mine.items():
                t = mp.mpf(theirs[metric][model])
                rel = abs(v-t)/t
                worst = max(worst, rel); count += 1
            rows_out.append({'family': family, 'N': N, 'marginal': s+1, 'symmetric': sym,
                             'mixed_monic': mp.nstr(mine[('monic', 'mixed')], 10),
                             'mixed_orth': mp.nstr(mine[('orthonormal', 'mixed')], 10)})
print('scalar compared values:', count, 'max relative difference vs producer:', mp.nstr(worst, 3))
for r in rows_out:
    if r['N'] in (4, 8, 16, 20): print(r)

# weighted-median dual vs LP, plus producer's function
sys.path.insert(0, '/workspace/padua_research/topics/nn-mop-conditioning-20261106/code')
import importlib.util
spec = importlib.util.spec_from_file_location('c1m', '/workspace/padua_research/topics/nn-mop-conditioning-20261106/code/c1_metrics.py')
c1m = importlib.util.module_from_spec(spec); spec.loader.exec_module(c1m)
random.seed(7); worst_lp = 0.0; worst_prod = 0.0
for trial in range(400):
    n = random.randint(1, 9)
    g = [random.choice([random.uniform(-3, 3), float(random.randint(-2, 2))]) for _ in range(n)]
    w = [random.choice([random.uniform(0.01, 2), 1.0]) for _ in range(n)]
    # primal LP: maximize sum w g z  s.t. |z|<=1, sum w z = 0
    res = linprog(c=[-wi*gi for wi, gi in zip(w, g)], A_eq=[w], b_eq=[0], bounds=[(-1, 1)]*n, method='highs')
    primal = -res.fun
    dual = min(sum(wi*abs(gi-l) for gi, wi in zip(g, w)) for l in g)
    prod = float(c1m.weighted_median_support([mp.mpf(v) for v in g], [mp.mpf(v) for v in w]))
    worst_lp = max(worst_lp, abs(primal-dual)/max(1, abs(dual)))
    worst_prod = max(worst_prod, abs(prod-dual)/max(1, abs(dual)))
print('weighted-median dual vs LP primal: 400 random cases, max rel diff', worst_lp, '; producer function vs dual', worst_prod)
