"""Claude audit-01, target A2: certified DIRECT corner Lebesgue values.

Independent of the developer code, of the A1 corner formula and of the -04
simplification.  For each n the Padua cardinal functions are obtained by
solving the transposed product-Chebyshev Vandermonde system in ball (arb)
arithmetic (python-flint), and the Lebesgue function sum_B |L_B(c)| is
enclosed at all four corners c=(+-1,+-1).

Node convention (repository A1): B_jk=(cos(j pi/n), cos(k pi/(n+1))),
0<=j<=n, 0<=k<=n+1, j+k even.  Basis T_a(x)T_b(y), a+b<=n.

Also computed in arb from its definition: L_n (the -04 odd-cosecant sum) and
the endpoint Lebesgue value of interpolation at n Chebyshev roots (side
remark of -03, not load-bearing).  Every inequality claimed by -01..-04 is
then tested on the certified enclosures; a test passes only if the whole
enclosure satisfies it.  Finite-range evidence only (n<=NMAX); not a proof.

Usage: python3 audit_a2_direct.py NMAX > out.json
"""
import json
import platform
import sys
import time

import flint
from flint import arb, arb_mat, ctx

ctx.prec = 256
PI = arb.pi()
GAMMA = arb.const_euler()


def padua_nodes(n):
    return [(j, k) for j in range(n + 1) for k in range(n + 2) if (j + k) % 2 == 0]


def modes(n):
    return [(a, b) for a in range(n + 1) for b in range(n + 1 - a)]


def corner_values(n):
    nodes = padua_nodes(n)
    ms = modes(n)
    assert len(nodes) == len(ms) == (n + 1) * (n + 2) // 2
    cx = [[(arb(a * j) * PI / n).cos() for j in range(n + 1)] for a in range(n + 1)]
    cy = [[(arb(b * k) * PI / (n + 1)).cos() for k in range(n + 2)] for b in range(n + 1)]
    m = len(nodes)
    # VT[mode, node] = q_mode(node);  solve VT X = Q, X[node, corner] = L_node(corner)
    VT = arb_mat(m, m)
    for p, (a, b) in enumerate(ms):
        for q, (j, k) in enumerate(nodes):
            VT[p, q] = cx[a][j] * cy[b][k]
    corners = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
    Q = arb_mat(m, 4)
    for p, (a, b) in enumerate(ms):
        for c, (sx, sy) in enumerate(corners):
            Q[p, c] = arb(sx ** a * sy ** b)
    X = VT.solve(Q)
    vals = []
    for c in range(4):
        s = arb(0)
        for q in range(m):
            s += abs(X[q, c])
        vals.append(s)
    node_corner = {}
    for c, (sx, sy) in enumerate(corners):
        jj = 0 if sx == 1 else n
        kk = 0 if sy == 1 else n + 1
        node_corner[c] = (jj + kk) % 2 == 0
    return corners, vals, node_corner


def L_sum(n):
    s = arb(0)
    for r in range(1, n + 1, 2):
        d = arb(1) / 2 if r == n else arb(1)
        s += d / (arb(r) * PI / (2 * n)).sin()
    return 2 * s / n


def cheb_root_endpoint_lebesgue(n):
    xs = [(arb(2 * k - 1) * PI / (2 * n)).cos() for k in range(1, n + 1)]
    tot = arb(0)
    for i in range(n):
        p = arb(1)
        for l in range(n):
            if l != i:
                p *= (1 - xs[l]) / (xs[i] - xs[l])
        tot += abs(p)
    return tot


def B_sum(n):
    s = arb(0)
    for r in range(1, n + 1, 2):
        s += (arb(1) / 2 if r == n else arb(1)) / r
    return s


def le(x, y):
    """Certified x<=y: whole enclosure."""
    return bool(x <= y)


def main():
    nmax = int(sys.argv[1])
    t0 = time.time()
    b = 8 / PI ** 2 * (GAMMA + (8 / PI).log())
    c1 = 2 / PI * (GAMMA + (8 / PI).log())
    rows = []
    allok = True
    for n in range(2, nmax + 1):
        t1 = time.time()
        corners, vals, isnode = corner_values(n)
        nonnode = [vals[c] for c in range(4) if not isnode[c]]
        node = [vals[c] for c in range(4) if isnode[c]]
        lam = nonnode[0]
        Ln = L_sum(n)
        logn = arb(n).log()
        lead = 4 / PI ** 2 * logn ** 2
        An = 2 / PI * logn + c1
        rem = lam - lead - b * logn
        chk = {
            "two_node_corners_contain_1": all(v.overlaps(arb(1)) for v in node) and len(node) == 2,
            "two_nonnode_corners_overlap": len(nonnode) == 2 and nonnode[0].overlaps(nonnode[1]),
            "nonnode_ge_1": le(arb(1), lam),
            "04_abs_corner_minus_square_le_precise": le(abs(lam - Ln ** 2), PI ** 4 / 2 + 4 + arb(1) / (n + 1)),
            "04_abs_corner_minus_square_le_54": le(abs(lam - Ln ** 2), arb(54)),
            "01_lower_lead_minus_54": le(lead - 54, lam),
            "01_lower_lead_minus_80log": le(lead - 80 * logn, lam),
            "01_Ln_ge_2overpi_logn": le(2 / PI * logn, Ln),
            "02_upper": le(lam, lead + 12 / PI * logn + 63),
            "02_abs_le_95log": le(abs(lam - lead), 95 * logn),
            "02_Ln_le_2overpi_logn_plus_3": le(Ln, 2 / PI * logn + 3),
            "04_Ln_le_2_plus_logn": le(Ln, 2 + logn),
            "03_B_main_le_1overn": le(abs(B_sum(n) - (logn + GAMMA + arb(2).log()) / 2), arb(1) / n),
            "03_eq6_abs_Ln_minus_An_le": le(abs(Ln - An), (1 + 2 / PI) / n),
            "03_eq7_abs_Ln2_minus_An2_le_9": le(abs(Ln ** 2 - An ** 2), arb(9)),
            "03_abs_corner_minus_An2_le_63": le(abs(lam - An ** 2), arb(63)),
            "03_abs_remainder_le_67": le(abs(rem), arb(67)),
            "03_abs_remainder_le_68": le(abs(rem), arb(68)),
            "03_side_Ln_equals_cheb_root_endpoint": Ln.overlaps(cheb_root_endpoint_lebesgue(n)),
        }
        ok = all(chk.values())
        allok &= ok
        rows.append({
            "n": n,
            "corner_values": {str(corners[c]): vals[c].str(25, radius=True) for c in range(4)},
            "node_corners": [str(corners[c]) for c in range(4) if isnode[c]],
            "Lambda_c": lam.str(25, radius=True),
            "Lambda_c_mid": float(lam.mid()),
            "Lambda_c_rad": float(lam.rad()),
            "L_n_sq": (Ln ** 2).str(25, radius=True),
            "corner_minus_square": float((lam - Ln ** 2).mid()),
            "remainder_after_lead_and_b": float(rem.mid()),
            "checks": chk,
            "all_checks_pass": ok,
            "seconds": round(time.time() - t1, 3),
        })
        print(f"n={n} ok={ok} lam={float(lam.mid()):.15f} rad={float(lam.rad()):.2e} t={time.time()-t1:.1f}s", file=sys.stderr)
    out = {
        "script": "audit_a2_direct.py (Claude audit-01, independent; no developer code imported)",
        "status": "finite certified ball-arithmetic evidence for n=2..NMAX only; not an all-n proof",
        "python": platform.python_version(),
        "python_flint": flint.__version__,
        "prec_bits": ctx.prec,
        "nmax": nmax,
        "b": b.str(30, radius=True),
        "c1": c1.str(30, radius=True),
        "all_checks_pass_all_n": allok,
        "max_abs_corner_minus_square": max(abs(r["corner_minus_square"]) for r in rows),
        "max_abs_remainder": max(abs(r["remainder_after_lead_and_b"]) for r in rows),
        "results": rows,
        "total_seconds": round(time.time() - t0, 2),
    }
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
