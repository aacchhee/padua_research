#!/usr/bin/env python3
"""Auditor B2 independent exact checker (standard library only).

Decodes the stored payload with a hand-written RFC1924 base85 decoder and a
hand-written IEEE754 binary64 integer decoder, checks 455 distinct dyadic
points in [-1,1]^3, builds the integer-scaled monomial matrix over Z
(row i scaled by 2^(12*k_i), k_i = max denominator exponent of point i), and
computes det mod several primes (primality by trial division).  Also builds
the integer-scaled product-Chebyshev matrix as a second basis.
"""
import json, sys, hashlib, time
from fractions import Fraction

ALPH = ("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "abcdefghijklmnopqrstuvwxyz!#$%&()*+-;<=>?@^_`{|}~")
assert len(ALPH) == 85 and len(set(ALPH)) == 85
IDX = {c: i for i, c in enumerate(ALPH)}


def b85dec(s):
    assert len(s) % 5 == 0, "padding not expected"
    out = bytearray()
    for g in range(0, len(s), 5):
        v = 0
        for c in s[g:g + 5]:
            v = v * 85 + IDX[c]
        assert v < 2 ** 32
        out += v.to_bytes(4, "big")
    return bytes(out)


def f64(b8):
    bits = int.from_bytes(b8, "little")
    sign = bits >> 63
    e = (bits >> 52) & 0x7FF
    f = bits & ((1 << 52) - 1)
    if e == 0x7FF:
        raise ValueError("nonfinite")
    if e == 0:
        m, ex = f, -1074
    else:
        m, ex = f + (1 << 52), e - 1075
    q = Fraction(m) * (Fraction(2) ** ex)
    return -q if sign else q


def is_prime_td(p):
    if p < 2:
        return False
    d = 2
    while d * d <= p:
        if p % d == 0:
            return False
        d += 1
    return True


def det_mod(rows, p):
    A = [[x % p for x in r] for r in rows]
    n = len(A)
    det = 1
    for c in range(n):
        piv = None
        for r in range(c, n):
            if A[r][c]:
                piv = r
                break
        if piv is None:
            return 0, c
        if piv != c:
            A[c], A[piv] = A[piv], A[c]
            det = -det
        pv = A[c][c]
        det = det * pv % p
        inv = pow(pv, p - 2, p)
        rowc = A[c]
        for r in range(c + 1, n):
            a = A[r][c]
            if a:
                fct = a * inv % p
                rr = A[r]
                for k in range(c, n):
                    rr[k] = (rr[k] - fct * rowc[k]) % p
    return det % p, n


def main():
    path = sys.argv[1]
    primes = [int(x) for x in sys.argv[2].split(",")]
    raw = open(path, "rb").read()
    rep = {"payload_bytes": len(raw), "payload_sha256": hashlib.sha256(raw).hexdigest()}
    d = json.loads(raw)
    by = b85dec(d["coordinates_base85"])
    rep["coord_bytes"] = len(by)
    rep["coord_sha256"] = hashlib.sha256(by).hexdigest()
    assert len(by) == 455 * 24
    pts = []
    for i in range(455):
        pts.append(tuple(f64(by[24 * i + 8 * j: 24 * i + 8 * j + 8]) for j in range(3)))
    # cross-check with struct decoding
    import struct
    for i, p in enumerate(pts):
        fl = struct.unpack("<3d", by[24 * i: 24 * i + 24])
        assert all(Fraction(*fl[j].as_integer_ratio()) == p[j] for j in range(3))
    dy = all((q.denominator & (q.denominator - 1)) == 0 for p in pts for q in p)
    incube = all(-1 <= q <= 1 for p in pts for q in p)
    rep["all_dyadic"] = dy
    rep["in_closed_cube"] = incube
    rep["distinct"] = len(set(pts))
    rep["boundary_coord_count"] = sum(1 for p in pts for q in p if abs(q) == 1)
    rep["max_denominator_log2"] = max(q.denominator.bit_length() - 1 for p in pts for q in p)
    exps = [(a, b, c) for a in range(13) for b in range(13) for c in range(13) if a + b + c <= 12]
    assert len(exps) == 455
    # integer-scaled monomial rows
    mono = []
    cheb = []
    for p in pts:
        k = max(q.denominator.bit_length() - 1 for q in p)
        D = 1 << k
        nums = [q.numerator * (D // q.denominator) for q in p]  # coords = nums/D
        # monomial x^a y^b z^c * D^12 = nums^a nums^b nums^c * D^(12-a-b-c)
        row = [nums[0] ** a * nums[1] ** b * nums[2] ** c * D ** (12 - a - b - c) for (a, b, c) in exps]
        mono.append(row)
        # Chebyshev T_e(x)*D^e as integers via recurrence: U_e = T_e(x) D^e
        T = []
        for j in range(3):
            t = [1, nums[j]]
            for e in range(2, 13):
                t.append(2 * nums[j] * t[-1] - D * D * t[-2])
            T.append(t)
        cheb.append([T[0][a] * T[1][b] * T[2][c] * D ** (12 - a - b - c) for (a, b, c) in exps])
    # sanity: scaled monomial row equals D^12 * exact monomials for a few points
    for i in (0, 100, 454):
        p = pts[i]
        k = max(q.denominator.bit_length() - 1 for q in p)
        s = Fraction(2) ** (12 * k)
        for col in (0, 7, 200, 454):
            a, b, c = exps[col]
            assert mono[i][col] == p[0] ** a * p[1] ** b * p[2] ** c * s
    res = []
    for pr in primes:
        t0 = time.process_time()
        assert pr % 2 == 1 and is_prime_td(pr), pr
        dm, rk = det_mod(mono, pr)
        dc, rc = det_mod(cheb, pr)
        res.append({"prime": pr, "prime_trial_division": True,
                    "det_scaled_monomial_mod_p": dm, "rank_or_failcol_mono": rk,
                    "det_scaled_chebyshev_mod_p": dc, "rank_or_failcol_cheb": rc,
                    "cpu_s": round(time.process_time() - t0, 2)})
        print(res[-1], flush=True)
    rep["determinants"] = res
    json.dump(rep, open(sys.argv[3], "w"), indent=1)
    print(json.dumps({k: v for k, v in rep.items() if k != "determinants"}))


if __name__ == "__main__":
    main()
