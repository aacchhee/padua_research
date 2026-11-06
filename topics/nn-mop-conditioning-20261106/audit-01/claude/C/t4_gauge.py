"""Independent numeric checks of c1-gauge-invariants: fixed and data-dependent gauges."""
import sys, json, random; sys.path.insert(0, '.')
import mpmath as mp
from indep_nn import *
mp.mp.dps = 70
H = mp.mpf('1e-28')
random.seed(20261106)

def gauge_fields(q, sfun):
    """Rescaled NN fields (4) with all six fields; sfun(q, P) -> dict nu->scale incl. degree N."""
    out, P = nn_map(*q)
    N = len(q[0]); M = N-1
    s = sfun(q, P)
    g = {}
    for key, val in out.items():
        if isinstance(key, str):
            continue
        f, nu = key
        if f[0] == 'b':
            g[('B'+f[1], nu)] = val
            j = int(f[1]); succ = (nu[0]+(j == 1), nu[1]+(j == 2))
            g[('u'+f[1], nu)] = s[nu]/s[succ]
        else:
            i = int(f[1]); pred = (nu[0]-(i == 1), nu[1]-(i == 2))
            g[('A'+f[1], nu)] = val*s[nu]/s[pred]
    return g

def nn_fields(q):
    return {k: v for k, v in nn_map(*q)[0].items() if not isinstance(k, str)}

def check(family, N, label, sfun):
    q = inputs(N, family)
    base_m, Jm = jacobian(nn_fields, q, N, H)
    kmon, _, per_m, _ = condition(base_m, Jm, q, N)
    kb = max(per_m['b1'], per_m['b2'])
    base_g, Jg = jacobian(lambda qq: gauge_fields(qq, sfun), q, N, H)
    kg, arg, per_g, sc = condition(base_g, Jg, q, N)
    # B rows identical to b rows?
    dB = max(abs(Jg[('B'+k[0][1], k[1])][i]-Jm[k][i]) for k in Jm if k[0][0] == 'b' for i in range(3*N))
    rec = {'family': family, 'N': N, 'gauge': label, 'kappa_gauge': mp.nstr(kg, 10), 'argmax': str(arg),
           'kappa_b': mp.nstr(kb, 10), 'kappa_monic': mp.nstr(kmon, 10),
           'per_field_gauge': {f: mp.nstr(v, 6) for f, v in per_g.items()},
           'B_minus_b_jac_max': mp.nstr(dB, 3), 'ok_lower': bool(kg >= kb*(1-mp.mpf('1e-25')))}
    print(json.dumps(rec), flush=True)
    return rec

def fixed_random(N):
    vals = {}
    def sfun(q, P):
        if not vals:
            for nu in P:
                vals[nu] = mp.mpf(1) if nu == (0, 0) else mp.mpf(10)**random.uniform(-3, 3)
        return vals
    return sfun

def fixed_t(t):
    def sfun(q, P):
        return {nu: (mp.mpf(1) if sum(nu) == 0 else mp.mpf(t)**(sum(nu)-1)) for nu in P}
    return sfun

def dep_orthonormal(q, P):
    x, w = q
    def L(s, poly):
        return sum(w[s][l]*sum(c*x[l]**j for j, c in enumerate(poly))**2 for l in range(len(x)))
    s = {}
    for nu, poly in P.items():
        if sum(nu) == len(x):     # support polynomial: use derivative values instead
            val = sum(sum(j*c*xl**(j-1) for j, c in enumerate(poly) if j)**2 for xl in x)
        else:
            val = L(0, poly)+L(1, poly)
        s[nu] = 1/mp.sqrt(val)
    s0 = s[(0, 0)]
    return {nu: v/s0 for nu, v in s.items()}

def dep_normalize_one(q, P):
    """Data-dependent gauge making A1 at site (1,0) identically 1, others monic.
    A1_(1,0) = a1_(1,0) s_(1,0)/s_(0,0) -> choose s_(1,0)=1/a1_(1,0), keep all others 1."""
    out, _ = nn_map(*q)
    s = {nu: mp.mpf(1) for nu in P}
    s[(1, 0)] = 1/out[('a1', (1, 0))]
    return s

recs = []
for family in ('krawtchouk', 'hahn'):
    for N in (4, 6):
        recs.append(check(family, N, 'identity', lambda q, P: {nu: mp.mpf(1) for nu in P}))
        recs.append(check(family, N, 'fixed_random', fixed_random(N)))
        for t in ('0.1', '0.001'):
            recs.append(check(family, N, 'fixed_t^(|nu|-1), t='+t, fixed_t(t)))
        recs.append(check(family, N, 'dep_orthonormal_like', dep_orthonormal))
        recs.append(check(family, N, 'dep_normalize_A1(1,0)', dep_normalize_one))
json.dump(recs, open('t4_gauge.json', 'w'), indent=1)
print('ALL_OK', all(r['ok_lower'] for r in recs))
