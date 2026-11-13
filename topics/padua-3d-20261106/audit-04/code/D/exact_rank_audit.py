#!/usr/bin/env python3
"""Independent auditor exact-rank checker for pdpr canonical-parity payloads.

Written from the prose definition in pruning-certificate.md only; imports no
repository code.  Usage:
  python -I exact_rank_audit.py PAYLOAD.json N_EXPECTED M_EXPECTED  [primes...]

For each prime p (p % L == 1, p < 2^31, proved prime by complete trial
division) it builds the K-by-N matrix over F_p in a chosen basis, computes
its rank by exact modular Gaussian elimination (numpy int64, every product
of two residues < p^2 < 2^62 reduced immediately), extracts N pivot rows,
rebuilds that square minor from scratch and recomputes its determinant with
pure-Python integers (no fixed width at all).
Bases:  'cheb_closed'  T_a(x_p) = (rho^{a e} + rho^{-a e})/2  (no recurrence)
        'monomial_rev' x1^a x2^b x3^c, exponents in reverse-lex order
"""
import hashlib, json, math, sys, time
import numpy as np


def is_prime_td(p):
    if p < 2:
        return False
    if p % 2 == 0:
        return p == 2
    r = math.isqrt(p)
    d = 3
    while d <= r:
        if p % d == 0:
            return False
        d += 2
    return True


def prime_factors(n):
    f, d = [], 2
    while d * d <= n:
        if n % d == 0:
            f.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        f.append(n)
    return f


def decode(orders):
    m1, m2, m3 = orders
    full = []
    for i1 in range(m1 + 1):
        for i2 in range(m2 + 1):
            for i3 in range(m3 + 1):
                if i1 % 2 == i2 % 2 == i3 % 2:
                    full.append((i1, i2, i3))
    expect = 1
    for m in orders:
        expect *= m // 2 + 1
    e2 = 1
    for m in orders:
        e2 *= (m + 1) // 2
    assert len(full) == expect + e2, (len(full), expect, e2)
    return full


def exponents(n):
    out = []
    for a in range(n, -1, -1):  # reverse lexicographic, independent of producer
        for b in range(n - a, -1, -1):
            for c in range(n - a - b, -1, -1):
                out.append((a, b, c))
    assert len(out) == math.comb(n + 3, 3) and len(set(out)) == len(out)
    return out


def find_root(p, L):
    qs = prime_factors(L)
    for h in range(2, p):
        r = pow(h, (p - 1) // L, p)
        if pow(r, L, p) == 1 and all(pow(r, L // q, p) != 1 for q in qs):
            return r, {str(q): pow(r, L // q, p) for q in qs}
    raise RuntimeError("no root")


def build(p, L, rho, tri, orders, n, basis):
    inv2 = pow(2, p - 2, p)
    K = len(tri)
    exps = exponents(n)
    # per coordinate exponent e = L*i/(2m); per coordinate value tables
    cols = []
    # tables[t][j][a] residue of basis function degree a in coordinate t at row j
    tables = []
    for t in range(3):
        m = orders[t]
        tab = np.zeros((K, n + 1), dtype=np.int64)
        for j, tr in enumerate(tri):
            num = L * tr[t]
            assert num % (2 * m) == 0
            e = num // (2 * m)
            x = (pow(rho, e % L, p) + pow(rho, (-e) % L, p)) * inv2 % p
            for a in range(n + 1):
                if basis == "cheb_closed":
                    v = (pow(rho, (a * e) % L, p) + pow(rho, (-a * e) % L, p)) * inv2 % p
                else:
                    v = pow(x, a, p)
                tab[j, a] = v
        tables.append(tab)
    E = np.zeros((K, len(exps)), dtype=np.int64)
    for k, (a, b, c) in enumerate(exps):
        u = tables[0][:, a] * tables[1][:, b] % p      # < p^2 < 2^62
        E[:, k] = u * tables[2][:, c] % p
    return E


def rank_rows(E, p):
    """Exact row-reduction; returns rank and the original row indices of pivots."""
    A = E.copy() % p
    K, N = A.shape
    rows = np.arange(K)
    r = 0
    piv_rows = []
    for col in range(N):
        nz = np.nonzero(A[r:, col])[0]
        if nz.size == 0:
            continue
        i = r + int(nz[0])
        if i != r:
            A[[r, i]] = A[[i, r]]
            rows[[r, i]] = rows[[i, r]]
        inv = pow(int(A[r, col]), p - 2, p)
        A[r, col:] = A[r, col:] * inv % p
        f = A[r + 1:, col].copy()
        if f.size:
            A[r + 1:, col:] = (A[r + 1:, col:] - (f[:, None] * A[r, col:][None, :]) % p) % p
        piv_rows.append(int(rows[r]))
        r += 1
        if r == K:
            break
    return r, piv_rows


def det_python(Mat, p):
    """Pure-Python-int determinant of a square list-of-lists over F_p."""
    a = [[int(v) % p for v in row] for row in Mat]
    n = len(a)
    det = 1
    for c in range(n):
        piv = None
        for i in range(c, n):
            if a[i][c]:
                piv = i
                break
        if piv is None:
            return 0
        if piv != c:
            a[c], a[piv] = a[piv], a[c]
            det = -det
        det = det * a[c][c] % p
        inv = pow(a[c][c], p - 2, p)
        rc = a[c]
        for i in range(c + 1, n):
            f = a[i][c] * inv % p
            if f:
                ri = a[i]
                for k in range(c, n):
                    ri[k] = (ri[k] - f * rc[k]) % p
    return det % p


def det_numpy(Mat, p):
    A = np.array(Mat, dtype=np.int64) % p
    n = A.shape[0]
    det = 1
    for c in range(n):
        nz = np.nonzero(A[c:, c])[0]
        if nz.size == 0:
            return 0
        i = c + int(nz[0])
        if i != c:
            A[[c, i]] = A[[i, c]]
            det = -det
        pv = int(A[c, c])
        det = det * pv % p
        inv = pow(pv, p - 2, p)
        f = A[c + 1:, c] * inv % p
        A[c + 1:, c:] = (A[c + 1:, c:] - (f[:, None] * A[c, c:][None, :]) % p) % p
    return det % p


def main():
    path = sys.argv[1]
    Nexp = int(sys.argv[2]); Mexp = int(sys.argv[3])
    primes = [int(x) for x in sys.argv[4:]]
    raw = open(path, "rb").read()
    d = json.loads(raw)
    out = {"payload": path, "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()}
    n = d["n"]; orders = d["orders"]; ids = d["ids"]
    assert type(n) is int and orders == [n, n + 1, n + 1]
    assert all(type(v) is int for v in orders)
    assert all(type(v) is int for v in ids), "non-int id"
    assert all(b > a for a, b in zip(ids, ids[1:])), "not strictly increasing"
    full = decode(orders)
    assert 0 <= ids[0] and ids[-1] < len(full)
    K = len(ids); N = math.comb(n + 3, 3)
    assert K == Mexp == d["M"] and N == Nexp == d["N"] and K >= N
    tri = [full[j] for j in ids]
    assert len(set(tri)) == K
    for tr in tri:
        assert tr[0] % 2 == tr[1] % 2 == tr[2] % 2
    out.update(n=n, orders=orders, K=K, N=N, full=len(full))
    # float sanity of the angle convention cos(pi i/m) == cos(2 pi e/L)
    L = 1
    for m in orders:
        L = L * (2 * m) // math.gcd(L, 2 * m)
    out["L"] = L; out["L_factors"] = prime_factors(L)
    mx = 0.0
    for tr in tri:
        for t in range(3):
            e = L * tr[t] // (2 * orders[t])
            mx = max(mx, abs(math.cos(math.pi * tr[t] / orders[t]) - math.cos(2 * math.pi * e / L)))
    out["float_angle_convention_maxdiff"] = mx
    # complement / removed IDs
    out["removed_ids_count"] = len(full) - K
    out["checks"] = []
    for p in primes:
        rec = {"p": p}
        assert p % L == 1 and p < 2 ** 31, p
        t0 = time.process_time()
        rec["prime_trial_division"] = is_prime_td(p)
        assert rec["prime_trial_division"]
        rho, ordtests = find_root(p, L)
        rec["rho"] = rho; rec["rho^L"] = pow(rho, L, p); rec["rho^(L/q)"] = ordtests
        for basis in ("cheb_closed", "monomial_rev"):
            E = build(p, L, rho, tri, orders, n, basis)
            rnk, piv = rank_rows(E, p)
            sub = {"basis": basis, "rank": rnk}
            if rnk == N:
                minor_ids = sorted(ids[r] for r in piv)
                pos = {j: k for k, j in enumerate(ids)}
                Mtx = [E[pos[j]].tolist() for j in minor_ids]
                sub["minor_ids_sha256"] = hashlib.sha256(json.dumps(minor_ids).encode()).hexdigest()
                sub["det_numpy"] = det_numpy(Mtx, p)
                if N <= 500:
                    sub["det_python"] = det_python(Mtx, p)
                    assert sub["det_python"] == sub["det_numpy"]
                assert sub["det_numpy"] != 0
                sub["minor_ids_first"] = minor_ids[:6]
            rec[basis] = sub
        rec["cpu_s"] = round(time.process_time() - t0, 3)
        out["checks"].append(rec)
        print(json.dumps(rec), flush=True)
    # replay the producer's stated minor with an independent Chebyshev route at the producer prime
    c = d["certificate"]
    pp = c["p"]; prho = c["rho"]
    assert pp % L == 1 and is_prime_td(pp)
    qs = prime_factors(L)
    assert pow(prho, L, pp) == 1 and all(pow(prho, L // q, pp) != 1 for q in qs)
    # producer columns: d=0..n, a=0..d, b=0..d-a, c=d-a-b ; unscaled Chebyshev
    pex = [(a, b, dd - a - b) for dd in range(n + 1) for a in range(dd + 1) for b in range(dd - a + 1)]
    inv2 = pow(2, pp - 2, pp)
    def T(a, i, m):
        e = L * i // (2 * m)
        return (pow(prho, (a * e) % L, pp) + pow(prho, (-a * e) % L, pp)) * inv2 % pp
    mids = c["minor_row_ids"]
    assert len(mids) == N == len(set(mids)) and set(mids) <= set(ids)
    Mtx = []
    for j in mids:
        i1, i2, i3 = full[j]
        Mtx.append([T(a, i1, orders[0]) * T(b, i2, orders[1]) % pp * T(cc, i3, orders[2]) % pp for (a, b, cc) in pex])
    dprod = det_numpy(Mtx, pp)
    out["producer_minor_replay"] = {"p": pp, "rho": prho, "det": dprod, "stated": c["det_mod_p"],
                                    "match": dprod == c["det_mod_p"],
                                    "match_up_to_sign": dprod in (c["det_mod_p"], (-c["det_mod_p"]) % pp)}
    print(json.dumps(out["producer_minor_replay"]), flush=True)
    json.dump(out, open(sys.argv[0].rsplit("/", 2)[0] + "/out/exact-rank-n" + str(n) + ".json", "w"), indent=1)


if __name__ == "__main__":
    main()
