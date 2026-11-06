#!/usr/bin/env python3
"""Round-2 auditor's own exact rebuild of the committed projection reference.

Own formulation (PD-T286 definitions, written from the theory text):
  * type-II monic P_nu from M_nu c = -rhs with own fraction-free-free Gauss
    elimination and an explicit nonzero-determinant (normality) check for every
    1<=|nu|<=N;
  * NN coefficients obtained NOT from the h-ratio / subleading formulas but by
    exact polynomial projection: for j=1,2, R_j = x P_nu - P_(nu+e_j) is
    expanded exactly in {P_nu, P_(nu-e1), P_(nu-e2)} (triangular/least-squares
    in coefficient space, residual required exactly zero). b_(nu,j) is the
    P_nu coefficient of R_j, a_(nu,s) its P_(nu-e_s) coefficient; a from j=1
    and j=2 must agree exactly.
  * h-ratio cross-check: a_(nu,s) = h_(nu,s)/h_(nu-e_s,s) also computed.
Reads only the committed JSON (path argument). No developer code is imported.
"""
import hashlib, json, math, sys, time
from fractions import Fraction as Fr

FIELDS = ('a1', 'a2', 'b1', 'b2')
U = Fr(1, 2**53)


def family_input(N, fam):
    M = N - 1
    x = [Fr(2*k, M) - 1 for k in range(N)]
    if fam == 'krawtchouk':
        W = [[math.comb(M, k) * p**k * (1-p)**(M-k) for k in range(N)] for p in (Fr(2, 5), Fr(1, 2))]
    elif fam == 'hahn':
        def rising(a, n):
            r = Fr(1)
            for i in range(n):
                r *= a + i
            return r
        W = [[rising(b+1, k)/math.factorial(k) * rising(Fr(2), M-k)/math.factorial(M-k) for k in range(N)]
             for b in (Fr(1), Fr(3, 2))]
    else:
        raise ValueError(fam)
    W = [[w/sum(r) for w in r] for r in W]
    return x, W


def gauss_solve(A, b):
    """Solve A c = b exactly; raise if singular (det == 0). Returns c, det."""
    n = len(A)
    T = [list(r) + [v] for r, v in zip(A, b)]
    det = Fr(1)
    for col in range(n):
        piv = None
        for r in range(col, n):
            if T[r][col] != 0:
                piv = r
                break
        if piv is None:
            raise ArithmeticError('singular moment matrix')
        if piv != col:
            T[col], T[piv] = T[piv], T[col]
            det = -det
        p = T[col][col]
        det *= p
        for r in range(col+1, n):
            f = T[r][col]
            if f:
                f = f / p
                T[r] = [u - f*v for u, v in zip(T[r], T[col])]
    c = [Fr(0)]*n
    for i in range(n-1, -1, -1):
        s = T[i][n] - sum(T[i][j]*c[j] for j in range(i+1, n))
        c[i] = s / T[i][i]
    if det == 0:
        raise ArithmeticError('zero det')
    return c, det


def nn_array(x, W):
    N = len(x)
    mom = [[sum(w * xi**r for w, xi in zip(Ws, x)) for r in range(2*N+1)] for Ws in W]
    P = {(0, 0): [Fr(1)]}   # ascending coefficients
    nsys = 0
    for k in range(1, N+1):
        for n in range(k+1):
            m = k - n
            rows, rhs = [], []
            for s, cnt in ((0, n), (1, m)):
                for i in range(cnt):
                    rows.append([mom[s][i+j] for j in range(k)])
                    rhs.append(-mom[s][i+k])
            c, det = gauss_solve(rows, rhs)
            nsys += 1
            Pn = c + [Fr(1)]
            # verify orthogonality directly
            for s, cnt in ((0, n), (1, m)):
                for i in range(cnt):
                    if sum(a*mom[s][i+j] for j, a in enumerate(Pn)) != 0:
                        raise ArithmeticError('orthogonality residual')
            P[(n, m)] = Pn
    # terminal: every degree-N P equals node polynomial
    node = [Fr(1)]
    for xi in x:
        node = [Fr(0)] + node
        for i in range(len(node)-1):
            node[i] -= xi*node[i+1]
    for n in range(N+1):
        if P[(n, N-n)] != node:
            raise ArithmeticError('terminal != node polynomial')

    def h(nu, s):
        return sum(a*mom[s][nu[s]+j] for j, a in enumerate(P[nu]))

    out = {}
    for k in range(N):
        for n in range(k+1):
            nu = (n, k-n)
            xP = [Fr(0)] + P[nu]
            coeffs = {}
            for j in range(2):
                succ = (nu[0]+(j == 0), nu[1]+(j == 1))
                R = [u - v for u, v in zip(xP, P[succ])]
                # R has degree <= k (top coefficient cancels)
                if R[-1] != 0:
                    raise ArithmeticError('degree')
                R = R[:-1]
                basis = [('b', P[nu])]
                for s in range(2):
                    if nu[s] > 0:
                        pred = (nu[0]-(s == 0), nu[1]-(s == 1))
                        basis.append(('a%d' % (s+1), P[pred]))
                # b: degree-k coefficient of R (P_nu monic, others degree k-1)
                bcoef = R[k] if k < len(R) else Fr(0)
                rem = [u - bcoef*(P[nu][i] if i < len(P[nu]) else 0) for i, u in enumerate(R)]
                # remainder degree <= k-1: solve in span of predecessors exactly
                preds = basis[1:]
                vals = {'a1': Fr(0), 'a2': Fr(0)}
                if preds:
                    deg = k - 1
                    # least squares via normal equations would be inexact-free with Fractions;
                    # solve using the first len(preds) generic equations then verify all.
                    cols = [[(p[i] if i < len(p) else Fr(0)) for i in range(deg+1)] for _, p in preds]
                    target = [rem[i] if i < len(rem) else Fr(0) for i in range(deg+1)]
                    G = [[sum(u*v for u, v in zip(ci, cj)) for cj in cols] for ci in cols]
                    rh = [sum(u*v for u, v in zip(ci, target)) for ci in cols]
                    sol, _ = gauss_solve(G, rh)
                    for (name, _), v in zip(preds, sol):
                        vals[name] = v
                    resid = [t - sum(v*c[i] for v, c in zip(sol, cols)) for i, t in enumerate(target)]
                    if any(resid):
                        raise ArithmeticError('NN identity residual nonzero')
                else:
                    if any(rem):
                        raise ArithmeticError('NN identity residual nonzero (origin)')
                coeffs[j] = (bcoef, vals)
            if coeffs[0][1] != coeffs[1][1]:
                raise ArithmeticError('a depends on j')
            a = coeffs[0][1]
            # h-ratio cross-check
            for s in range(2):
                if nu[s] > 0:
                    pred = (nu[0]-(s == 0), nu[1]-(s == 1))
                    if h(nu, s)/h(pred, s) != a['a%d' % (s+1)]:
                        raise ArithmeticError('h-ratio mismatch')
            out[nu] = {'a1': a['a1'], 'a2': a['a2'], 'b1': coeffs[0][0], 'b2': coeffs[1][0]}
    return out, nsys


def digest(v):
    return hashlib.sha256(json.dumps(v, sort_keys=True).encode()).hexdigest()


def main(path, which=None):
    raw_bytes = open(path, 'rb').read()
    ref = json.loads(raw_bytes)
    print(json.dumps(dict(file_sha256=hashlib.sha256(raw_bytes).hexdigest(), bytes=len(raw_bytes),
                          cases_sha_ok=digest(ref['cases']) == ref['cases_sha256'])), flush=True)
    truth_cache = {}
    for rec in ref['cases']:
        N, fam, meth = rec['N'], rec['family'], rec['method']
        if which and (N, fam, meth) not in which:
            continue
        t0 = time.time()
        ok_ids = digest(rec['raw_coefficients']) == rec['raw_sha256'] and \
            digest(rec['rational_input']) == rec['rational_input_sha256']
        y = {}
        for row in rec['raw_coefficients']:
            vals = {}
            for f in FIELDS:
                v = float.fromhex(row[f])
                assert math.isfinite(v) and float(v).hex() == row[f] or row[f] in ('-0x0.0p+0', '0x0.0p+0')
                vals[f] = Fr(v)
            y[tuple(row['nu'])] = vals
        exp = {(n, k-n) for k in range(N) for n in range(k+1)}
        cover = set(y) == exp and len(rec['raw_coefficients']) == len(exp)
        x = [Fr(s) for s in rec['rational_input']['nodes']]
        W = [[Fr(s) for s in r] for r in rec['rational_input']['normalized_weights']]
        pos = all(w > 0 for r in W for w in r) and len(W) == 2 and all(len(r) == N for r in W) and len(x) == N
        order = all(a < b for a, b in zip(x, x[1:]))
        mass = all(sum(r) == 1 for r in W)
        if (N, fam) not in truth_cache:
            x0, W0 = family_input(N, fam)
            truth_cache[(N, fam)] = (x0, W0, nn_array(x0, W0)[0])
        x0, W0, truth = truth_cache[(N, fam)]
        scale = {f: max(abs(r[f]) for r in truth.values()) for f in FIELDS}
        arr, nsys = nn_array(x, W)
        fields = {f: max(abs(y[nu][f] - arr[nu][f]) for nu in arr) / scale[f] for f in FIELDS}
        eta_c = max(fields.values())
        eta_d = max(max(abs(a-b) for a, b in zip(x, x0)),
                    max(abs(a-b)/b for r, r0 in zip(W, W0) for a, b in zip(r, r0)))
        Qv = sum(((y[nu][f]-arr[nu][f])/scale[f])**2 for nu in arr for f in FIELDS)
        sqrtQ = math.sqrt(Qv.numerator / Qv.denominator) if Qv else 0.0
        # use high-accuracy sqrt via integer arithmetic
        from decimal import Decimal, getcontext
        getcontext().prec = 50
        sqrtQd = float((Decimal(Qv.numerator)/Decimal(Qv.denominator)).sqrt())
        trivial = max(max(abs(y[nu][f]-truth[nu][f]) for nu in truth)/scale[f] for f in FIELDS)
        m = rec['metrics']
        def rel(a, b):
            return abs(a-b)/max(abs(b), 1e-300)
        cmp = dict(eta_d=rel(float(eta_d), m['input_mixed_sup']),
                   eta_d_u=rel(float(eta_d/U), m['input_in_units_u']),
                   eta_c=rel(float(eta_c), m['full_coefficient_correction']),
                   eta_c_u=rel(float(eta_c/U), m['correction_in_units_u']),
                   sqrtQ=rel(sqrtQd, m['coefficient_SPD_norm']),
                   **{'field_'+f: rel(float(fields[f]), m['fields'][f]) for f in FIELDS})
        print(json.dumps(dict(N=N, family=fam, method=meth, ids_ok=ok_ids, coverage=cover, positive=pos,
                              ordered=order, unit_mass=mass, normal_systems=nsys,
                              stored_systems=m['exact_normality_systems_checked'],
                              eta_d_u=float(eta_d/U), eta_c_u=float(eta_c/U), sqrtQ=sqrtQd,
                              trivial_eta_c_u=float(trivial/U),
                              max_rel_diff=max(cmp.values()), rel=cmp,
                              secs=round(time.time()-t0, 1))), flush=True)


if __name__ == '__main__':
    which = None
    if len(sys.argv) > 2:
        which = set()
        for s in sys.argv[2:]:
            N, fam, meth = s.split(':')
            which.add((int(N), fam, meth))
    main(sys.argv[1], which)
