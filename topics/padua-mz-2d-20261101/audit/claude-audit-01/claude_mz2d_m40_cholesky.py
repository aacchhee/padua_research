#!/usr/bin/env python3
"""Claude audit-01 addendum: exact m=40 bracket certificate (auditor code).

PD side: for each parity block, A = d*(Q - lo*H) (min) or d*(hi*H - Q) (max) as an
exact integer matrix. A float Cholesky factor proposes an integer lower-triangular
Z ~ 2^k L^{-1}. B = Z A Z^T is computed exactly (FLINT). If B is symmetric with
positive diagonal and strict row dominance, B is positive definite (Gershgorin),
hence nonsingular, hence Z invertible, hence A is PD (Sylvester). Floats only
propose Z. Rayleigh sides: exact quotients of rounded eigenvectors.
Reuses the auditor's own pencil construction from claude_mz2d_audit_check.py.
"""
import sys, json, math, time, hashlib, platform
from fractions import Fraction as F
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import numpy as np, scipy.linalg
from flint import fmpz_mat
import claude_mz2d_audit_check as c


def fail(msg):
    raise SystemExit('FAIL: ' + msg)


def pd_certificate(rows, k=40):
    den, M = c.int_matrix(rows)
    n = len(M)
    Mf = np.array(M, dtype=float)
    s = np.max(np.abs(Mf))
    L = np.linalg.cholesky(Mf / s)
    W = scipy.linalg.solve_triangular(L, np.eye(n), lower=True)
    Z = fmpz_mat([[int(round(x * 2.0 ** k)) for x in row] for row in W])
    A = fmpz_mat(M)
    B = Z * A * Z.transpose()
    if B != B.transpose():
        fail('asym')
    minmargin = None
    for i in range(n):
        d = B[i, i]
        off = sum(abs(B[i, j]) for j in range(n) if j != i)
        if not (d > 0 and d > off):
            fail(f'dominance row {i}')
        mg = F(int(d - off), int(d))
        minmargin = mg if minmargin is None or mg < minmargin else minmargin
    return {'dimension': n, 'min_relative_margin': float(minmargin)}


def main():
    m = 40
    width = F(1, 10**6)
    t0 = time.time()
    B, H, Q = c.mass_pair(m, m - 1)
    blocks = c.parity_blocks(m, B, H, Q)
    Hf = np.array([[float(x) for x in r] for r in H]); Qf = np.array([[float(x) for x in r] for r in Q])
    mins, maxs = [], []
    for idx in blocks:
        ix = np.ix_(idx, idx)
        w, V = scipy.linalg.eigh(Qf[ix], Hf[ix])
        mins.append((w[0], idx, V[:, 0])); maxs.append((w[-1], idx, V[:, -1]))
    out = {'m': m, 'method': 'exact inverse-Cholesky congruence + positive Gershgorin (PD sides); exact Rayleigh (other sides)',
           'python': sys.version, 'numpy': np.__version__, 'scipy': scipy.__version__, 'platform': platform.platform(),
           'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), 'checks': []}
    for kind, (val, idx, vec) in (('minimum', min(mins, key=lambda t: t[0])), ('maximum', max(maxs, key=lambda t: t[0]))):
        lo = F(math.floor(val / float(width))) * width; hi = lo + width
        recs = []
        for b in blocks:
            rows = [[(Q[i][j] - lo * H[i][j]) if kind == 'minimum' else (hi * H[i][j] - Q[i][j]) for j in b] for i in b]
            recs.append(pd_certificate(rows))
        v = vec / np.max(np.abs(vec)); z = [int(round(x * 10**9)) for x in v]
        qa = c.rayleigh(z, [[Q[i][j] for j in idx] for i in idx]); hb = c.rayleigh(z, [[H[i][j] for j in idx] for i in idx])
        if hb <= 0: fail('H')
        if kind == 'minimum' and not qa < hi * hb: fail('rayleigh min')
        if kind == 'maximum' and not qa > lo * hb: fail('rayleigh max')
        out['checks'].append({'extremum': kind, 'open_interval': [str(lo), str(hi)], 'pd_blocks': recs, 'rayleigh_float': float(qa / hb)})
        print(kind, lo, hi, recs, flush=True)
    out['seconds'] = time.time() - t0
    Path(sys.argv[1]).write_text(json.dumps(out, indent=1) + '\n')
    print('PASS')


if __name__ == '__main__':
    main()
