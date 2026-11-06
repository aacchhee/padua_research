#!/usr/bin/env python3
"""Claude audit-02: black-box central-difference check of the gauged six-field
condition at the theorem's t (reuses audit-01 auditor library indep_nn.py,
which solves type-II polynomials from moment systems and matches the NN
recurrence by coefficients).  Compares with the exact K from gauge_exact.py
outputs.  Mixed and componentwise node models, free mass."""
import sys, json
sys.path.insert(0, '/workspace/padua_research/topics/nn-mop-conditioning-20261106/audit-01/claude/C')
import mpmath as mp
from indep_nn import inputs, nn_map, jacobian, condition

mp.mp.dps = 70
H = mp.mpf('1e-28')


def gauge_fields(q, t):
    out, P = nn_map(*q)
    s = {nu: (mp.mpf(1) if sum(nu) == 0 else t ** (sum(nu) - 1)) for nu in P}
    g = {}
    for key, val in out.items():
        if isinstance(key, str):
            continue
        f, nu = key
        if f[0] == 'b':
            j = int(f[1]); succ = (nu[0] + (j == 1), nu[1] + (j == 2))
            g[('B' + f[1], nu)] = val
            g[('u' + f[1], nu)] = s[nu] / s[succ]
        else:
            i = int(f[1]); pred = (nu[0] - (i == 1), nu[1] - (i == 2))
            g[('A' + f[1], nu)] = val * s[nu] / s[pred]
    return g


exact = {}
for fn in sys.argv[1:]:
    for line in open(fn):
        r = json.loads(line)
        for c in r['cases']:
            exact[(r['family'], r['N'], c['model'], c['fixed_mass'])] = c

for family in ('krawtchouk', 'hahn'):
    for N in (3, 4, 6):
        q = inputs(N, family)
        for model in ('mixed', 'componentwise'):
            c = exact[(family, N, model, False)]
            t = mp.mpf(c['t_star']) * (1 - mp.mpf('1e-9'))
            base, J = jacobian(lambda qq: gauge_fields(qq, t), q, N, H)
            ns = 'mixed' if model == 'mixed' else [abs(x) for x in q[0]]
            ks, arg, per, sc = condition(base, J, q, N, node_scale=ns)
            # also a deliberately too-large t, to see the a-field take over
            t_big = mp.mpf(1)
            base2, J2 = jacobian(lambda qq: gauge_fields(qq, t_big), q, N, H)
            kb, arg2, per2, _ = condition(base2, J2, q, N, node_scale=ns)
            K = mp.mpf(c['K'])
            print(json.dumps({'family': family, 'N': N, 'model': model, 't': mp.nstr(t, 10),
                              'kappa_fd': mp.nstr(ks, 12), 'K_exact': c['K'],
                              'rel_diff': mp.nstr(abs(ks - K) / K, 3), 'argmax_field': arg[0],
                              'per_field': {k: mp.nstr(v, 8) for k, v in per.items()},
                              'kappa_fd_t1': mp.nstr(kb, 10), 'argmax_t1': arg2[0]}), flush=True)
