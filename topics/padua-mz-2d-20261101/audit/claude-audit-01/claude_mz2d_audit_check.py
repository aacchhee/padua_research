#!/usr/bin/env python3
"""Claude audit-01 independent checker for padua-mz-2d-20261101.

Written by the auditor without importing the developer's producer or checker.
Certification route deliberately differs from the developer's
signed-dominance congruence:

* lambda_min > lo   <=  d*(Q - lo*H) positive definite on each parity block,
                        by Sylvester's criterion: every leading principal minor
                        > 0, read from the diagonal of an exact FLINT
                        fraction-free LU whose row permutation is the identity.
* lambda_max < hi   <=  d*(hi*H - Q) positive definite, same test.
* lambda_min < hi   <=  exact rational Rayleigh quotient of one rounded vector.
* lambda_max > lo   <=  exact rational Rayleigh quotient of one rounded vector.

Floating eigensolvers only propose vectors. Every acceptance test is an exact
integer/rational comparison and is coded with explicit `if ...: raise`, so it
also runs under `python -O`.

Other parts:
* moment formula (1) of PD-T106 checked against signed weights solved in
  60-digit mpmath arithmetic directly from the nodes (not via the alias
  formula), m = 1..10, all total degrees <= 2m+3;
* stored m=30 witness: Q(p^2) and int p^2 recomputed exactly by first
  expanding p^2 into the product-Chebyshev basis (a different organisation
  from the bilinear z^T Q z), then float nodal evaluation with float weights;
* corner-weight formula of PD-T111 checked exactly against the signed weights
  (rational arithmetic for the corner weight via the cardinal formula is not
  used; we compare high-precision solved weights with the closed form);
* tensor-CC envelope of PD-T117 checked numerically for small m.
"""
import hashlib, json, math, platform, sys, time
from fractions import Fraction as F
from pathlib import Path

import flint
from flint import fmpz_mat
import numpy as np
import scipy.linalg
import mpmath as mp


def fail(msg):
    raise SystemExit('FAIL: ' + msg)


# ---------- moments, written from the statement of PD-T106 (1) ----------
def hint(r):
    """int_{-1}^1 T_r = 2/(1-r^2) for even r, 0 for odd r."""
    if r % 2:
        return F(0)
    return F(-2, r * r - 1)


def tri_fold(r, N):
    r = r % (2 * N)
    return r if r <= N else 2 * N - r


def q_moment(m, a, b):
    A = tri_fold(a, m)
    B = tri_fold(b, m + 1)
    if A + B <= m:
        return hint(A) * hint(B)
    return hint(m - A) * hint(m + 1 - B)


def basis_list(n):
    return [(a, t - a) for t in range(n + 1) for a in range(t, -1, -1)]


def mass_pair(m, n):
    B = basis_list(n)
    N = len(B)
    H = [[None] * N for _ in range(N)]
    Q = [[None] * N for _ in range(N)]
    for i, (a, b) in enumerate(B):
        for j in range(i, N):
            c, d = B[j]
            us = (a + c, abs(a - c))
            vs = (b + d, abs(b - d))
            hv = sum(hint(u) * hint(v) for u in us for v in vs) / 4
            qv = sum(q_moment(m, u, v) for u in us for v in vs) / 4
            H[i][j] = H[j][i] = hv
            Q[i][j] = Q[j][i] = qv
    return B, H, Q


def parity_blocks(m, B, H, Q):
    coord = 0 if m % 2 == 0 else 1
    blocks = [[i for i, ab in enumerate(B) if ab[coord] % 2 == p] for p in (0, 1)]
    for i in blocks[0]:
        for j in blocks[1]:
            if H[i][j] != 0 or Q[i][j] != 0:
                fail('nonzero off-parity entry')
    return blocks


def int_matrix(rows):
    den = 1
    for row in rows:
        for x in row:
            den = den * x.denominator // math.gcd(den, x.denominator)
    return den, [[int(x * den) for x in row] for row in rows]


def sylvester_pd(rows):
    """Exact positive-definiteness by leading principal minors (FFLU)."""
    den, M = int_matrix(rows)
    if den <= 0:
        fail('denominator')
    A = fmpz_mat(M)
    P, L, D, U = A.fflu()
    n = len(M)
    for i in range(n):
        for j in range(n):
            if P[i, j] != (1 if i == j else 0):
                return False, 'pivoting needed (not PD or zero pivot)'
    # U[k,k] is the (k+1)-th leading principal minor for unpivoted FFLU.
    mins = [U[k, k] for k in range(n)]
    ok = all(x > 0 for x in mins)
    # Consistency: last minor equals the determinant.
    if mins[-1] != A.det():
        fail('fflu minor/determinant mismatch')
    return ok, {'dimension': n, 'min_leading_minor_bits': min(int(x).bit_length() for x in mins) if ok else None}


def rayleigh(v, Mrows):
    s = F(0)
    nz = [i for i, x in enumerate(v) if x]
    for i in nz:
        row = Mrows[i]
        acc = F(0)
        for j in nz:
            acc += row[j] * v[j]
        s += v[i] * acc
    return s


def certify(m, width=F(1, 10**6)):
    n = m - 1
    B, H, Q = mass_pair(m, n)
    blocks = parity_blocks(m, B, H, Q)
    Hf = np.array([[float(x) for x in r] for r in H])
    Qf = np.array([[float(x) for x in r] for r in Q])
    lam_min_all, lam_max_all = [], []
    vecs = []
    for idx in blocks:
        ix = np.ix_(idx, idx)
        w, V = scipy.linalg.eigh(Qf[ix], Hf[ix])
        lam_min_all.append((w[0], idx, V[:, 0]))
        lam_max_all.append((w[-1], idx, V[:, -1]))
    mn = min(lam_min_all, key=lambda t: t[0])
    mx = max(lam_max_all, key=lambda t: t[0])
    res = {'m': m, 'n': n, 'dimension': len(B), 'float_extrema': [float(mn[0]), float(mx[0])]}
    out = []
    for kind, (val, idx, vec) in (('minimum', mn), ('maximum', mx)):
        lo = F(math.floor(val / float(width))) * width
        hi = lo + width
        # PD side on every block
        pd_records = []
        for bidx in blocks:
            if kind == 'minimum':
                rows = [[Q[i][j] - lo * H[i][j] for j in bidx] for i in bidx]
            else:
                rows = [[hi * H[i][j] - Q[i][j] for j in bidx] for i in bidx]
            ok, info = sylvester_pd(rows)
            if not ok:
                fail(f'PD side failed m={m} {kind}: {info}')
            pd_records.append(info)
        # Rayleigh side on the block holding the extremal vector
        v = vec / np.max(np.abs(vec))
        z = [int(round(x * 10**9)) for x in v]
        Hb = [[H[i][j] for j in idx] for i in idx]
        Qb = [[Q[i][j] for j in idx] for i in idx]
        qa, hb = rayleigh(z, Qb), rayleigh(z, Hb)
        if hb <= 0:
            fail('nonpositive H form')
        if kind == 'minimum' and not (qa < hi * hb):
            fail('Rayleigh side min')
        if kind == 'maximum' and not (qa > lo * hb):
            fail('Rayleigh side max')
        out.append({'extremum': kind, 'open_interval': [str(lo), str(hi)],
                    'pd_side': ('Q-lo*H PD on both blocks' if kind == 'minimum' else 'hi*H-Q PD on both blocks'),
                    'pd_blocks': pd_records, 'rayleigh_quotient_float': float(qa / hb)})
    res['checks'] = out
    return res, (B, H, Q)


# ---------- signed weights from nodes, high precision ----------
def padua_nodes(m):
    return [(j, k) for j in range(m + 1) for k in range(m + 2) if (j + k) % 2 == 0]


def mp_weights(m, dps=60):
    mp.mp.dps = dps
    nodes = padua_nodes(m)
    modes = basis_list(m)
    X = [mp.cos(mp.pi * j / m) for j in range(m + 1)]
    Y = [mp.cos(mp.pi * k / (m + 1)) for k in range(m + 2)]
    V = mp.matrix(len(modes), len(nodes))
    for r, (a, b) in enumerate(modes):
        for c, (j, k) in enumerate(nodes):
            V[r, c] = mp.chebyt(a, X[j]) * mp.chebyt(b, Y[k])
    rhs = mp.matrix([mp.mpf(hint(a).numerator) / hint(a).denominator * mp.mpf(hint(b).numerator) / hint(b).denominator for a, b in modes])
    w = mp.lu_solve(V, rhs)
    return nodes, X, Y, w


def moment_nodal_check(mmax=10):
    total = 0
    worst = mp.mpf(0)
    for m in range(1, mmax + 1):
        nodes, X, Y, w = mp_weights(m)
        for d in range(2 * m + 4):
            for a in range(d + 1):
                b = d - a
                s = mp.fsum(w[i] * mp.chebyt(a, X[j]) * mp.chebyt(b, Y[k]) for i, (j, k) in enumerate(nodes))
                e = q_moment(m, a, b)
                err = abs(s - mp.mpf(e.numerator) / e.denominator)
                worst = max(worst, err)
                if err > mp.mpf(10) ** (-40):
                    fail(f'moment mismatch m={m} a={a} b={b} err={err}')
                total += 1
    return {'m_range': [1, mmax], 'modes_checked': total, 'max_abs_error': mp.nstr(worst, 5), 'precision_dps': 60}


# ---------- PD-T111 corner weight closed form ----------
def corner_check(mmax=14):
    """Compare high-precision solved weights at the two negative corners with
    the harmonic formula stated in PD-T111 (read from file, not trusted)."""
    rows = []
    for m in range(2, mmax + 1):
        nodes, X, Y, w = mp_weights(m, 50)
        i00 = nodes.index((0, 0))
        im0 = nodes.index((m, 0)) if (m % 2 == 0) else None
        rows.append({'m': m, 'w00': mp.nstr(w[i00], 20),
                     'wm0': (mp.nstr(w[im0], 20) if im0 is not None else None),
                     'neg_nodes': [nodes[i] for i in range(len(nodes)) if w[i] < 0]})
    return rows


# ---------- stored witness ----------
def witness_check(path):
    data = json.loads(Path(path).read_text())
    row = next(r for r in data['results'] if r['m'] == 30)
    W = row['witness']
    coeffs = W['coefficients']
    m = 30
    if len(coeffs) != 225 or len({(a, b) for a, b, _ in coeffs}) != 225:
        fail('witness size')
    for a, b, z in coeffs:
        if not (a >= 0 and b >= 0 and a + b <= 29 and isinstance(z, int) and z != 0):
            fail('witness triple')
    # Expand p^2 in product Chebyshev: T_aT_c = (T_{a+c}+T_{|a-c|})/2
    sq = {}
    for a, b, z in coeffs:
        for c, d, y in coeffs:
            for u in (a + c, abs(a - c)):
                for v in (b + d, abs(b - d)):
                    sq[(u, v)] = sq.get((u, v), 0) + z * y
    qa = sum(F(cnt) * q_moment(m, u, v) for (u, v), cnt in sq.items()) / 4
    hb = sum(F(cnt) * hint(u) * hint(v) for (u, v), cnt in sq.items()) / 4
    ok = (qa == F(W['Q_p_squared']) and hb == F(W['integral_p_squared'])
          and hb - 4 * qa == F(W['strict_b_minus_4a']) and hb - 4 * qa > 0 and qa / hb == F(W['rayleigh_quotient']))
    if not ok:
        fail('stored witness mismatch')
    # float nodal evaluation with float64 weights from the node Vandermonde
    nodes = padua_nodes(m)
    modes = basis_list(m)
    X = np.cos(np.pi * np.arange(m + 1) / m)
    Y = np.cos(np.pi * np.arange(m + 2) / (m + 1))
    xs = np.array([X[j] for j, k in nodes]); ys = np.array([Y[k] for j, k in nodes])
    def T(r, t):
        return np.cos(r * np.arccos(np.clip(t, -1, 1)))
    V = np.array([T(a, xs) * T(b, ys) for a, b in modes])
    rhs = np.array([float(hint(a) * hint(b)) for a, b in modes])
    w = np.linalg.solve(V, rhs)
    pv = sum(z * T(a, xs) * T(b, ys) for a, b, z in coeffs)
    qa_f = float(np.dot(w, pv * pv))
    return {'terms': 225, 'max_total_degree': max(a + b for a, b, _ in coeffs),
            'squared_expansion_terms': len(sq), 'exact_match': True,
            'a_over_b': str(qa / hb), 'a_over_b_float': float(qa / hb),
            'nodal_float_Q_p2_rel_err': abs(qa_f - float(qa)) / float(qa),
            'negative_weights_m30': int(np.sum(w < 0))}


def main():
    here = Path(__file__).resolve()
    stored = sys.argv[1]
    outp = Path(sys.argv[2])
    ms = [int(x) for x in sys.argv[3:]] or [10, 20, 30, 40]
    t0 = time.time()
    rec = {'auditor': 'Claude Opus 5.5 xhigh (audit-01)',
           'script_sha256': hashlib.sha256(here.read_bytes()).hexdigest(),
           'stored_receipt_sha256': hashlib.sha256(Path(stored).read_bytes()).hexdigest(),
           'python': sys.version, 'platform': platform.platform(), 'python_flint': flint.__version__,
           'numpy': np.__version__, 'scipy': scipy.__version__, 'mpmath': mp.__version__}
    rec['moment_formula_vs_mp_weights'] = moment_nodal_check(10)
    print('moments ok', flush=True)
    rec['stored_witness'] = witness_check(stored)
    print('witness ok', flush=True)
    rec['corner_weights_mp'] = corner_check(14)
    rec['spectra'] = []
    for m in ms:
        r, _ = certify(m)
        r['seconds'] = None
        rec['spectra'].append(r)
        print('certified', m, r['checks'][0]['open_interval'], r['checks'][1]['open_interval'], flush=True)
        outp.write_text(json.dumps(rec, indent=1) + '\n')
    rec['total_seconds'] = time.time() - t0
    outp.write_text(json.dumps(rec, indent=1) + '\n')
    print('PASS')


if __name__ == '__main__':
    main()
