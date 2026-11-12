"""D3 single-round producer and exact dyadic interval-Newton checker.

Search/refinement are proposals only. `check` uses Python integer arithmetic,
Fraction, Decimal (only to propose a preconditioner), and the certificate.
Every acceptance inequality is an exact integer comparison.
"""
import argparse
import hashlib
import itertools
import json
import math
import platform
import time
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path

N = 20
CBITS = 180
BITS = 256
RBITS = 100
S = 1 << BITS
RAD = 1 << (BITS - RBITS)
SEED = 20261112


def idx(n):
    return [(i, j, k) for i in range(n + 1)
            for j in range(n + 1 - i) for k in range(n + 1 - i - j)]


A5, A3 = idx(5), idx(3)


def moment(a):
    v = Fraction(1)
    for k in a:
        if k % 2:
            return Fraction(0)
        v *= Fraction(math.comb(k, k // 2), 2 ** k)
    return v


def mul(a, b):
    p = [a[0]*b[0], a[0]*b[1], a[1]*b[0], a[1]*b[1]]
    return min(p)//S, -((-max(p))//S)


def add(a, b):
    return a[0]+b[0], a[1]+b[1]


def neg(a):
    return -a[1], -a[0]


def scalar(a, k):
    return (a[0]*k, a[1]*k) if k >= 0 else (a[1]*k, a[0]*k)


def value(q):
    t = Fraction(q)*S
    return t.numerator//t.denominator, -((-t.numerator)//t.denominator)


def powers(x, degree):
    p = [(S, S)]
    for _ in range(degree):
        p.append(mul(p[-1], x))
    return p


def polys(box, alphas, jac=False):
    """Enclose monomial moments and their Jacobian on the 80-box."""
    pp = [powers(x, 5) for x in box[:60]]
    f, jj = [], []
    for a in alphas:
        row = [(0, 0)] * 80
        total = (0, 0)
        for n in range(N):
            t = (S, S)
            for d in range(3):
                t = mul(t, pp[3*n+d][a[d]])
            total = add(total, mul(box[60+n], t))
            if jac:
                row[60+n] = t
                for d in range(3):
                    if a[d]:
                        dt = box[60+n]
                        for e in range(3):
                            dt = mul(dt, pp[3*n+e][a[e]-(e == d)])
                        row[3*n+d] = scalar(dt, a[d])
        f.append(add(total, neg(value(moment(a)))))
        jj.append(row)
    return (f, jj) if jac else f


def evaluations(box):
    pp = [powers(x, 3) for x in box[:60]]
    rows = []
    for n in range(N):
        row = []
        for a in A3:
            t = (S, S)
            for d in range(3):
                t = mul(t, pp[3*n+d][a[d]])
            row.append(t)
        rows.append(row)
    return rows


def inverse_proposal(matrix):
    """Decimal inversion proposes dyadic R; exact checks never trust it."""
    n = len(matrix)
    with localcontext() as ctx:
        ctx.prec = 85
        a = [[Decimal(v[0]+v[1])/Decimal(2*S) for v in row] +
             [Decimal(int(i == j)) for j in range(n)]
             for i, row in enumerate(matrix)]
        for j in range(n):
            p = max(range(j, n), key=lambda i: abs(a[i][j]))
            a[j], a[p] = a[p], a[j]
            pivot = a[j][j]
            a[j] = [v/pivot for v in a[j]]
            for i in range(n):
                if i != j:
                    c = a[i][j]
                    a[i] = [x-c*y for x, y in zip(a[i], a[j])]
        scale = Decimal(1 << 60)
        return [[int((v*scale).to_integral_value()) << (BITS-60)
                 for v in row[n:]] for row in a]


def dot(r, intervals):
    lo, hi = 0, 0
    for c, a in zip(r, intervals):
        lo += c * (a[0] if c >= 0 else a[1])
        hi += c * (a[1] if c >= 0 else a[0])
    return lo//S, -((-hi)//S)


def defect_norm(r, j):
    n = len(r)
    cols = list(zip(*j))
    maximum = 0
    for i in range(n):
        row = 0
        for k in range(n):
            a = neg(dot(r[i], cols[k]))
            if i == k:
                a = add(a, (S, S))
            row += max(abs(a[0]), abs(a[1]))
        maximum = max(maximum, row)
    return maximum


def determinant_mod(centers, prime=65537):
    inv = pow(pow(2, CBITS, prime), -1, prime)
    x = [c*inv % prime for c in centers[:60]]
    a = [[math.prod(pow(x[3*n+d], e[d], prime) for d in range(3)) % prime
          for e in A3] for n in range(N)]
    det = 1
    for j in range(N):
        candidates = [i for i in range(j, N) if a[i][j]]
        if not candidates:
            return 0
        p = candidates[0]
        if p != j:
            a[p], a[j] = a[j], a[p]
            det = -det
        v = a[j][j]
        det = det*v % prime
        iv = pow(v, -1, prime)
        for i in range(j+1, N):
            c = a[i][j]*iv % prime
            for k in range(j+1, N):
                a[i][k] = (a[i][k]-c*a[j][k]) % prime
    return det % prime


def nonlattice(centers, active):
    fixed = [i for i in range(60) if i not in active]
    for i, j in itertools.combinations(fixed, 2):
        if i % 3 != j % 3:
            continue
        a, b = [Fraction(centers[k], 1 << CBITS) for k in (i, j)]
        d = (1-a*a)*(1-b*b)
        square = (math.isqrt(d.numerator)**2 == d.numerator and
                  math.isqrt(d.denominator)**2 == d.denominator)
        trace = 4*a*b
        if d > 0 and not square and trace.denominator != 1:
            return {"fixed_coordinate_indices": [i, j],
                    "a": str(a), "b": str(b),
                    "D": str(d), "trace_4ab": str(trace)}
    raise AssertionError("no fixed rational nonlattice pair")


def check(cert):
    assert cert['schema'] == 'fd3-dyadic-v1'
    assert cert['center_bits'] == CBITS and cert['radius_bits'] == RBITS
    centers = [int(c) for c in cert['center_numerators']]
    active = cert['active']
    assert len(centers) == 80 and len(active) == 56
    assert active == sorted(set(active)) and all(0 <= i < 80 for i in active)
    center = [(c << (BITS-CBITS),)*2 for c in centers]
    box = [(v[0]-RAD, v[1]+RAD) if i in active else v
           for i, v in enumerate(center)]
    assert all(-S < a[0] <= a[1] < S for a in box[:60])
    assert all(0 < a[0] <= a[1] for a in box[60:])
    for i, j in itertools.combinations(range(N), 2):
        assert any(box[3*i+d][1] < box[3*j+d][0] or
                   box[3*j+d][1] < box[3*i+d][0] for d in range(3))
    fc, jc = polys(center, A5, True)
    _, jb = polys(box, A5, True)
    jc = [[row[k] for k in active] for row in jc]
    jb = [[row[k] for k in active] for row in jb]
    r = inverse_proposal(jc)
    q = defect_norm(r, jb)
    z = max(max(abs(v) for v in dot(row, fc)) for row in r)
    assert q < S and z*S + q*RAD < RAD*S, (q/S, z/S)
    vc, vb = evaluations(center), evaluations(box)
    rv = inverse_proposal(vc)
    qv = defect_norm(rv, vb)
    assert qv < S
    det = determinant_mod(centers)
    assert det != 0
    nl = nonlattice(centers, active)
    # Exact numerator bounds are canonical; decimals below are display only.
    return {"verdict": "PASS_EXACT_INTERVAL_NEWTON_AND_RANK",
            "arithmetic": "integer directed dyadic intervals; scale 2^256",
            "equations": 56, "variables": 80, "active_variables": 56,
            "radius": "2^-100", "newton_q_num": str(q),
            "newton_z_num": str(z), "scale_bits": BITS,
            "strict_selfmap_margin_num": str(RAD*S-z*S-q*RAD),
            "rank_q_num": str(qv), "modular_prime": 65537,
            "center_det_mod": det, "nonlattice": nl,
            "q_display": q/S, "z_display": z/S,
            "rank_q_display": qv/S,
            "min_weight_lower_display": min(a[0] for a in box[60:])/S,
            "max_abs_coordinate_upper_display": max(max(abs(t) for t in a)
                                                        for a in box[:60])/S}


def search(started):
    import numpy as np
    import scipy.linalg
    from importlib.metadata import version
    alphas = np.array(A5)
    rng = np.random.default_rng(SEED)

    def rj(z):
        th, s = z[:60].reshape(N, 3), z[60:]
        c = np.cos(th[:, None, :]*alphas[None, :, :])
        sn = np.sin(th[:, None, :]*alphas[None, :, :])
        t = c.prod(axis=2)
        rr = t.T@(s*s)
        rr[0] -= 1
        jac = np.empty((56, 80))
        for d in range(3):
            dt = -alphas[None, :, d]*sn[:, :, d]*np.delete(c,d,axis=2).prod(axis=2)
            jac[:, d:60:3] = (dt*(s*s)[:,None]).T
        jac[:,60:] = (t*(2*s)[:,None]).T
        return rr, jac

    attempts = []
    for trial in range(12):
        if time.monotonic()-started > 180:
            break
        z = np.r_[np.pi*rng.random(60),
                  np.full(N, 1/np.sqrt(N))*(1+.1*rng.standard_normal(N))]
        mu = .01
        r, j = rj(z)
        f = r@r
        for step in range(4000):
            if time.monotonic()-started > 180:
                break
            h = j.T@j
            dz = np.linalg.solve(h+mu*np.diag(np.diag(h)+1e-12), -j.T@r)
            zz = z+dz
            rr, jj = rj(zz)
            ff = rr@rr
            if ff < f:
                z, r, j, f = zz, rr, jj, ff
                mu = max(mu/3, 1e-12)
            else:
                mu *= 4
            if f < 1e-28 or mu > 1e12:
                break
        x = np.cos(z[:60]).reshape(N,3)
        w = z[60:]**2
        v = np.array([[math.prod(x[n,d]**a[d] for d in range(3))
                       for a in A3] for n in range(N)])
        cond = float(np.linalg.cond(v))
        eligible = f < 1e-24 and w.min() > 1e-5 and np.abs(x).max() < 1-1e-8 and cond < 1e7
        attempts.append(dict(trial=trial, iterations=step+1, residual_squared=float(f),
                             min_weight=float(w.min()), max_abs_x=float(np.abs(x).max()),
                             condition_monomial=cond, eligible=bool(eligible)))
        print(json.dumps(attempts[-1]), flush=True)
        if eligible:
            z = np.r_[x.ravel(),w]
            # Square subsystem via pivoted QR of the polynomial Jacobian.
            jj = numeric_polys(z)[1]
            active = sorted(int(i) for i in scipy.linalg.qr(jj,pivoting=True)[2][:56])
            versions = {p:version(p) for p in ['numpy','scipy','mpmath']}
            return z, active, attempts, versions
    raise RuntimeError('D3 search exhausted: '+json.dumps(attempts))


def numeric_polys(z, mp=None):
    zero = mp.mpf(0) if mp else 0.
    out, jj = [], []
    for a in A5:
        f = zero
        row = [zero]*80
        for n in range(N):
            t = math.prod(z[3*n+d]**a[d] for d in range(3))
            f += z[60+n]*t
            row[60+n] = t
            for d in range(3):
                if a[d]:
                    row[3*n+d] = z[60+n]*a[d]*math.prod(
                        z[3*n+e]**(a[e]-(d == e)) for e in range(3))
        m = moment(a)
        out.append(f-m.numerator/m.denominator)  # targets are exactly dyadic
        jj.append(row)
    if mp:
        return mp.matrix(out), mp.matrix(jj)
    import numpy as np
    return np.array(out), np.array(jj)


def produce():
    import mpmath as mp
    started = time.monotonic()
    z, active, attempts, versions = search(started)
    mp.mp.dps = 100
    refined = [mp.mpf(round(float(v)*(1 << 60)))/(1 << 60) for v in z]
    steps = []
    for step in range(12):
        if time.monotonic()-started > 300:
            raise RuntimeError('D3 total refinement time cap')
        f,j = numeric_polys(refined,mp)
        norm = max(abs(v) for v in f)
        steps.append(str(norm))
        if norm < mp.mpf('1e-75'):
            break
        sub = mp.matrix([[j[i,k] for k in active] for i in range(56)])
        dz = mp.lu_solve(sub,-f)
        for k,v in zip(active,dz):
            refined[k] += v
    centers = [int(mp.nint(v*(1 << CBITS))) for v in refined]
    cert = dict(schema='fd3-dyadic-v1',center_bits=CBITS,radius_bits=RBITS,
                center_numerators=[str(v) for v in centers],active=active)
    exact = check(cert)
    # Fixed quality measurement: 31^3 cosine mesh plus 20000 random-angle queries.
    import numpy as np
    x = np.array([float(Fraction(v,1 << CBITS)) for v in centers[:60]]).reshape(N,3)
    v = np.array([[math.prod(x[n,d]**a[d] for d in range(3)) for a in A3]
                  for n in range(N)])
    g = np.cos(np.pi*np.arange(31)/30)
    mesh = np.array(list(itertools.product(g, repeat=3)))
    random = np.cos(np.pi*np.random.default_rng(SEED+1).random((20000,3)))
    mesh = np.vstack([mesh,random])
    maximum, witness = -1., None
    for k in range(0,len(mesh),1000):
        q = mesh[k:k+1000]
        ev = np.array([np.prod(q**np.array(a),axis=1) for a in A3]).T
        lebs = np.abs(np.linalg.solve(v.T,ev.T)).sum(axis=0)
        p = int(lebs.argmax())
        if lebs[p] > maximum:
            maximum, witness = float(lebs[p]),q[p].tolist()
    receipt = dict(search_seed=SEED,search_starts_limit=12,attempts=attempts,
                   newton_residuals=steps,versions=versions,python=platform.python_version(),
                   quality_status='MEASURED',sampled_Lambda=maximum,
                   quality_witness=witness,quality_queries=len(mesh),
                   quality_seed=SEED+1,exact_check=exact,
                   wall_seconds=time.monotonic()-started)
    return cert,receipt


def save(path,obj):
    data=(json.dumps(obj,indent=2,sort_keys=True)+'\n').encode()
    assert len(data) <= 32768
    Path(path).write_bytes(data)


if __name__ == '__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('mode',choices=['produce','check'])
    ap.add_argument('--certificate',required=True)
    ap.add_argument('--receipt',required=True)
    args=ap.parse_args()
    begin=time.monotonic()
    try:
        if args.mode == 'produce':
            cert,receipt=produce()
            save(args.certificate,cert)
        else:
            receipt=check(json.loads(Path(args.certificate).read_text()))
        receipt.update(code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                       command_mode=args.mode,elapsed_seconds=time.monotonic()-begin)
        save(args.receipt,receipt)
        print(json.dumps(receipt),flush=True)
    except Exception as exc:
        save(args.receipt,dict(verdict='FAIL_OR_INCOMPLETE',error=repr(exc),
                              elapsed_seconds=time.monotonic()-begin))
        raise
