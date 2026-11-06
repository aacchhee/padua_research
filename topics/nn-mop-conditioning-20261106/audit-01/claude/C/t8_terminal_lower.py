"""Independent check of the C1 pointwise lower envelope L_N (terminal balanced row)
against the reproduced 260-dps producer output, all four input models."""
import sys, json; sys.path.insert(0, '.')
import mpmath as mp
from indep_nn import *
mp.mp.dps = 70
H = mp.mpf('1e-28')
def wmed(g, w): return min(mp.fsum(wi*abs(gi-l) for gi, wi in zip(g, w)) for l in g)
worst = mp.mpf(0); n = 0
for family in ('krawtchouk', 'hahn'):
    raw = {c['N']: c for c in json.load(open(f'raw/c1-terminal-{family}260.json'))['cases']}
    for N in range(4, 10):
        q = inputs(N, family); x, w = q
        M = N-1; nu = (N//2, (N-1)//2)
        def F(qq):
            out, P = nn_map(*qq)
            return {k: v for k, v in out.items() if not isinstance(k, str)}
        base, J = jacobian(F, q, N, H)
        row = J[('b1', nu)]
        row2 = J[('b2', nu)]
        sb = {f: max(abs(base[k]) for k in base if k[0] == f) for f in ('b1', 'b2')}
        # step-line beta scale: beta_k = b1 at even k, b2 at odd k along nu_k
        sbeta = max(abs(base[('b1' if k % 2 == 0 else 'b2', ((k+1)//2, k//2))]) for k in range(N))
        dx = mp.fsum(abs(row[l]) for l in range(N))
        dw = mp.fsum(abs(row[N+l])*w[0][l] for l in range(N))+mp.fsum(abs(row[2*N+l])*w[1][l] for l in range(N))
        nums = {'mixed': dx+dw, 'spacing': 2*dx/(N-1)+dw, 'componentwise_nodes': mp.fsum(abs(row[l]*x[l]) for l in range(N))+dw,
                'fixed_mass': dx+wmed(row[N:2*N], w[0])+wmed(row[2*N:], w[1])}
        same_rows = max(abs(a-b) for a, b in zip(row, row2))
        for model, v in nums.items():
            for key, den in (('NN_gauge_lower', min(sb.values())), ('step_gauge_lower', sbeta)):
                t = mp.mpf(raw[N][key][model])
                rel = abs(v/den-t)/t; worst = max(worst, rel); n += 1
        print(family, N, 'NN lower mixed', mp.nstr(nums['mixed']/min(sb.values()), 12), 'producer', mp.nstr(mp.mpf(raw[N]['NN_gauge_lower']['mixed']), 12),
              'b1=b2 terminal row diff', mp.nstr(same_rows, 3))
print('compared', n, 'max rel diff', mp.nstr(worst, 3))
