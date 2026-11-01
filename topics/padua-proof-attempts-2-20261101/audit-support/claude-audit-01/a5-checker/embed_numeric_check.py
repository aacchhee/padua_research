#!/usr/bin/env python3
"""Claude audit-01 probe: does each frozen A5 checker (n=4..7) reconstruct the
*actual* Padua cardinals in its chosen real embedding?

Independent of the checker's exact algebra: nodes cos(j*pi/n), cos(k*pi/(n+1)),
j+k even, are generated in mpmath (80 digits), the Lagrange cardinals of the
total-degree<=n space are obtained by an mpmath Vandermonde solve, and their
values at random rational points are compared with the checker's own outward
interval enclosure (its polynomial_terms/evaluate/field_interval path, i.e. the
basis conversion + radical/tensor brackets that every sign decision uses).

Usage: embed_numeric_check.py N [certificate]   (certificate needed for n=6,7:
its field_embedding record is extracted by raw_decode, the rest is not parsed).
"""
import gzip, json, lzma, random, sys, time
from fractions import Fraction
from pathlib import Path
import importlib

import mpmath as mp

HERE = Path(__file__).resolve()
CODE = HERE.parents[3] / "code"
sys.path.insert(0, str(CODE))
mp.mp.dps = 80


def embedding_record(path):
    raw = Path(path).read_bytes()
    text = (lzma.decompress(raw) if raw.startswith(b"\xfd7zXZ\x00") else
            gzip.decompress(raw) if raw[:2] == b"\x1f\x8b" else raw).decode()
    key = '"field_embedding":'
    start = text.index(key) + len(key)
    record, _ = json.JSONDecoder().raw_decode(text, start)
    return record


def numeric_cardinals(n):
    nodes = [(mp.cos(j*mp.pi/n), mp.cos(k*mp.pi/(n+1)))
             for j in range(n+1) for k in range(n+2) if (j+k) % 2 == 0]
    powers = [(i, d-i) for d in range(n+1) for i in range(d, -1, -1)]
    V = mp.matrix([[u**i*w**j for (i, j) in powers] for (u, w) in nodes])
    Vinv = mp.inverse(V)
    def value(b, px, py):
        return mp.fsum(Vinv[k, b]*px**i*py**j for k, (i, j) in enumerate(powers))
    return nodes, value


def main():
    n = int(sys.argv[1])
    started = time.monotonic()
    mod = importlib.import_module({4: "a5_checker_n4", 5: "a5_checker_n5",
                                   6: "a5_checker_n6", 7: "a5_checker_n7"}[n])
    V = mod.Verifier(embedding_record(sys.argv[2])) if n >= 6 else mod.Verifier()
    t_build = time.monotonic() - started
    nodes_num, card = numeric_cardinals(n)
    unit = mod.UNIT
    as_mp = lambda z: (mp.mpf(z.lo)/unit, mp.mpf(z.hi)/unit)
    # 1. node coordinates: checker FIELD -> its own interval enclosure
    worst_node = mp.mpf(0)
    for (fx, fy), (nx, ny) in zip(V.nodes, nodes_num):
        for f, nv in ((fx, nx), (fy, ny)):
            lo, hi = as_mp(mod.field_interval(mod.basis_coefficients(f)))
            # mpmath cos(pi/2) etc. carry ~1e-80 rounding; exact rational nodes have
            # zero-width enclosures, so allow 1e-60 (far below any decision scale).
            tol = mp.mpf(10)**-60
            assert lo - tol <= nv <= hi + tol, ("node outside checker enclosure", n, nv, lo, hi)
            worst_node = max(worst_node, hi - lo)
    # 2. cardinal values at random rational points, via the checker's own terms
    rng = random.Random(20261101 + n)
    points = [(Fraction(rng.randint(-999, 999), 1000), Fraction(rng.randint(-999, 999), 1000))
              for _ in range(6)] + [(Fraction(-1), Fraction(-1)), (Fraction(1), Fraction(-1)),
                                    (Fraction(-1), Fraction(1))]
    worst_width, checks = mp.mpf(0), 0
    for px, py in points:
        box = (mod.Interval.point(px), mod.Interval.point(py))
        for b, terms in enumerate(V.lterms):
            lo, hi = as_mp(mod.evaluate(terms, box))
            nv = card(b, mp.mpf(px.numerator)/px.denominator, mp.mpf(py.numerator)/py.denominator)
            assert lo - mp.mpf(10)**-60 <= nv <= hi + mp.mpf(10)**-60, (
                "cardinal value outside checker enclosure", n, b, px, py, nv, lo, hi)
            worst_width = max(worst_width, hi - lo)
            checks += 1
    # 3. lambda at the two claimed non-node corners vs exact checker sign rule
    out = {"n": n, "cardinals": len(V.lterms), "node_checks": 2*len(V.nodes),
           "cardinal_value_checks": checks,
           "max_node_enclosure_width": mp.nstr(worst_node, 5),
           "max_cardinal_enclosure_width": mp.nstr(worst_width, 5),
           "lambda_corners_numeric": {str(c): mp.nstr(mp.fsum(abs(card(b, mp.mpf(c[0]), mp.mpf(c[1])))
                                                            for b in range(len(V.lterms))), 25)
                                      for c in ((-1, -1), (-1, 1), (1, -1), (1, 1))},
           "verifier_build_seconds": round(t_build, 2),
           "seconds": round(time.monotonic() - started, 2), "passed": True}
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
