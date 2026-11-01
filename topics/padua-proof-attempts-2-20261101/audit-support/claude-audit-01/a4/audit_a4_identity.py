#!/usr/bin/env python3
"""Claude audit-01, A4(a) sub-audit: independent finite checks of identities 70, 71, 74(5)/76(2).

Independent of developer code (imports nothing from the repository).
Direct Padua cardinals are obtained by inverting the product-Chebyshev
Vandermonde matrix in mpmath at high precision (dps=50).  This is a
high-precision numerical check (supporting evidence only), not exact arithmetic.

Checks, for n = 1..NMAX:
 (A) three independent evaluations of D_n agree: Fourier rhombus sum,
     product-U form with continuous extension, polynomial divided difference (70.3);
 (B) formula 70.(1)/(2): signed edge cardinals on all four edges equal the
     direct cardinals, at random t and at all special t (node ordinates/abscissae,
     0, pi, pi/2, complementary ordinates, cell endpoints);
 (C) formula 71.(2) at every admissible (epsilon, q), using direct Lambda_c and
     direct lambda_n(epsilon, cos beta); also the size of the error if the
     2/N correction were dropped;
 (D) the decomposition lambda(eps, cos(beta+s/m)) = S_n(s) - Delta_n(beta,s)
     (74.(5), 76.(2)), S_n(0)=Lambda_c, S_n even, for several s including s=+-pi.
Output: JSON on stdout.
"""
import json, sys, time, random
import mpmath as mp

mp.mp.dps = 50
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 8
random.seed(20261101)
PI = mp.pi

def cheb(a, x):
    # T_a(x) by three-term recurrence (exact polynomial evaluation)
    if a == 0:
        return mp.mpf(1)
    t0, t1 = mp.mpf(1), mp.mpf(x)
    for _ in range(a - 1):
        t0, t1 = t1, 2 * x * t1 - t0
    return t1

def chebu(a, x):
    # second-kind U_a(x) by recurrence; U_{-1}=0
    if a < 0:
        return mp.mpf(0)
    u0, u1 = mp.mpf(1), 2 * mp.mpf(x)
    if a == 0:
        return u0
    for _ in range(a - 1):
        u0, u1 = u1, 2 * x * u1 - u0
    return u1

def nodes(n):
    m = n + 1
    out = []
    for j in range(n + 1):
        for k in range(m + 1):
            if (j + k) % 2 == 0:
                ej = mp.mpf(1) / 2 if j in (0, n) else mp.mpf(1)
                ek = mp.mpf(1) / 2 if k in (0, m) else mp.mpf(1)
                w = 2 * ej * ek / (n * m)
                out.append((j, k, mp.cos(j * PI / n), mp.cos(k * PI / m), w, ej, ek))
    return out

def basis(n):
    return [(a, b) for a in range(n + 1) for b in range(n + 1 - a)]

def direct_cardinal_solver(n):
    nd = nodes(n)
    bs = basis(n)
    N = len(nd)
    assert N == len(bs) == (n + 1) * (n + 2) // 2
    V = mp.matrix(N, N)
    for i, (j, k, x, y, w, _, _) in enumerate(nd):
        for c, (a, b) in enumerate(bs):
            V[i, c] = cheb(a, x) * cheb(b, y)
    Vinv = mp.inverse(V)
    def cardinals(x, y):
        phi = [cheb(a, x) * cheb(b, y) for (a, b) in bs]
        return [mp.fsum(phi[c] * Vinv[c, i] for c in range(N)) for i in range(N)]
    return nd, cardinals

def U_ext(mm, x):
    # sin(mm x)/sin x, continuously extended at multiples of pi
    l = mp.nint(x / PI)
    d = x - l * PI
    sgn = (-1) ** (int((mm - 1) * l) % 2)
    if abs(d) < mp.mpf(10) ** (-40):
        return sgn * mm
    return sgn * mp.sin(mm * d) / mp.sin(d)

def D_U(n, u, v):
    S = (u + v) / 2
    T = (v - u) / 2
    return U_ext(n + 1, S) * U_ext(n + 1, T) + U_ext(n, S) * U_ext(n, T)

def D_F(n, u, v):
    s = mp.mpf(0)
    for p in range(n + 1):
        cp = 1 if p == 0 else 2
        for q in range(n + 1 - p):
            cq = 1 if q == 0 else 2
            s += cp * cq * mp.cos(p * u) * mp.cos(q * v)
    return s

def P(n, z):
    return cheb(n + 1, z) + cheb(n, z)

def Pp(n, z):
    # derivative of T_{n+1}+T_n, via T_k' = k U_{k-1}
    return (n + 1) * chebu(n, z) + n * chebu(n - 1, z)

def D_dd(n, u, v):
    cu, cv = mp.cos(u), mp.cos(v)
    if abs(cu - cv) < mp.mpf(10) ** (-35):
        return Pp(n, cu)
    return (P(n, cv) - P(n, cu)) / (cv - cu)

def maxabs(a):
    return max([abs(x) for x in a]) if a else mp.mpf(0)

def special_ts(n):
    m = n + 1
    ts = set()
    for k in range(m + 1):
        ts.add(mp.mpf(k) * PI / m)
    for j in range(n + 1):
        ts.add(mp.mpf(j) * PI / n)
    ts.update([mp.mpf(0), PI, PI / 2, PI / 2 + PI / m, PI / 2 - PI / m,
               PI / 2 + PI / (2 * m), PI / 2 - PI / (2 * m)])
    return sorted(ts)

def run_n(n, rec):
    m = n + 1
    N = n * m
    nd, cardinals = direct_cardinal_solver(n)
    # (A) D_n three ways
    errsA = []
    args = []
    for _ in range(12):
        args.append((mp.mpf(random.uniform(-7, 7)), mp.mpf(random.uniform(-7, 7))))
    for j in range(n + 1):
        for k in range(m + 1):
            args.append((j * PI / n, k * PI / m))
    args += [(mp.mpf(0), mp.mpf(0)), (PI, PI), (PI, -PI), (mp.mpf(0), 2 * PI), (PI / 3, -PI / 3)]
    for (u, v) in args:
        f = D_F(n, u, v)
        errsA.append(abs(D_U(n, u, v) - f))
        errsA.append(abs(D_dd(n, u, v) - f))
    rec["A_D_three_way_maxerr"] = mp.nstr(maxabs(errsA), 5)
    # (B) edge formulas
    errsB = []
    ts = special_ts(n) + [mp.mpf(random.uniform(0, 3.14159)) for _ in range(6)]
    for t in ts:
        ct = mp.cos(t)
        for th in (mp.mpf(0), PI):        # x edges x=cos th, free y=cos t
            dc = cardinals(mp.cos(th), ct)
            for i, (j, k, x, y, w, _, _) in enumerate(nd):
                a_j = j * PI / n; b_k = k * PI / m
                val = w * ((D_U(n, th + a_j, t + b_k) + D_U(n, th + a_j, t - b_k)) / 2
                           - mp.cos(n * th) * (-1) ** j)
                errsB.append(abs(val - dc[i]))
        for ph in (mp.mpf(0), PI):        # y edges y=cos ph, free x=cos t
            dc = cardinals(ct, mp.cos(ph))
            for i, (j, k, x, y, w, _, _) in enumerate(nd):
                a_j = j * PI / n; b_k = k * PI / m
                val = w * ((D_U(n, t + a_j, ph + b_k) + D_U(n, t - a_j, ph + b_k)) / 2
                           - mp.cos(n * t) * (-1) ** j)
                errsB.append(abs(val - dc[i]))
    rec["B_edge_cardinal_checks"] = len(errsB)
    rec["B_edge_cardinal_maxerr"] = mp.nstr(maxabs(errsB), 5)
    # direct corner values
    corners = {}
    for (cx, cy) in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
        corners[f"{cx},{cy}"] = mp.fsum(abs(c) for c in cardinals(mp.mpf(cx), mp.mpf(cy)))
    Lc = max(corners.values())
    rec["corner_values"] = {k: mp.nstr(v, 20) for k, v in corners.items()}
    rec["Lambda_c"] = mp.nstr(Lc, 25)
    # (C) 71 identity
    errsC = []; nochk = []; ptsC = []
    for eps in (1, -1):
        r = n if eps == -1 else 0
        for q in range(1, m):
            if (r + q) % 2 == 0:
                continue
            beta = q * PI / m
            lam = mp.fsum(abs(c) for c in cardinals(mp.mpf(eps), mp.cos(beta)))
            hs = mp.mpf(0)
            for (j, k, x, y, w, ej, ek) in nd:
                A = eps * mp.cos(j * PI / n)
                b = k * PI / m
                zp = mp.cos(beta + b); zm = mp.cos(beta - b)
                if zp < A < zm and abs(A - zp) > mp.mpf(10) ** (-30) and abs(zm - A) > mp.mpf(10) ** (-30):
                    hs += ej * ek * min((1 + zp) / (A - zp), (1 + zm) / (zm - A))
            rhs = 4 * hs / N + mp.mpf(2) / N
            errsC.append(abs((Lc - lam) - rhs))
            nochk.append(abs((Lc - lam) - 4 * hs / N))
            ptsC.append({"eps": eps, "q": q, "gap_direct": mp.nstr(Lc - lam, 15),
                         "rhs71": mp.nstr(rhs, 15)})
    rec["C_71_points"] = len(errsC)
    rec["C_71_maxerr"] = mp.nstr(maxabs(errsC), 5)
    rec["C_71_min_error_if_2overN_dropped"] = mp.nstr(min(nochk), 8) if nochk else None
    rec["C_71_sample"] = ptsC[:4]
    # (D) S_n - Delta decomposition
    def S_n(s):
        tot = mp.mpf(0)
        for j in range(2 * n):
            for rr in range(2 * m):
                if (j + rr) % 2 == 1:
                    H = ((-1) ** j * D_U(n, j * PI / n, rr * PI / m + s / m) - 1) / 2
                    tot += abs(H)
        return tot / N
    errsD = []; evenD = []
    S0 = S_n(mp.mpf(0))
    rec["D_S0_minus_Lambda_c"] = mp.nstr(S0 - Lc, 5)
    svals = [mp.mpf(0), mp.mpf('0.3'), mp.mpf('-0.7'), PI, -PI, mp.mpf('2.1')]
    for eps in (1, -1):
        r = n if eps == -1 else 0
        for q in range(1, m):
            if (r + q) % 2 == 0:
                continue
            beta = q * PI / m
            for s in svals:
                phi = beta + s / m
                lam = mp.fsum(abs(c) for c in cardinals(mp.mpf(eps), mp.cos(phi)))
                Sv = S_n(s)
                Dl = mp.mpf(0)
                for (j, k, x, y, w, ej, ek) in nd:
                    jp = j if eps == 1 else n - j
                    tau = (-1) ** jp
                    Hp = (tau * D_U(n, jp * PI / n, phi + k * PI / m) - 1) / 2
                    Hm = (tau * D_U(n, jp * PI / n, phi - k * PI / m) - 1) / 2
                    Dl += w * (abs(Hp) + abs(Hm) - abs(Hp + Hm))
                errsD.append(abs(lam - (Sv - Dl)))
                if Dl < -mp.mpf(10) ** (-30):
                    errsD.append(mp.mpf(1))
            break  # one q per edge is enough for the decomposition check
    for s in (mp.mpf('0.4'), mp.mpf('1.3'), PI):
        evenD.append(abs(S_n(s) - S_n(-s)))
    rec["D_decomposition_checks"] = len(errsD)
    rec["D_decomposition_maxerr"] = mp.nstr(maxabs(errsD), 5)
    rec["D_evenness_maxerr"] = mp.nstr(maxabs(evenD), 5)
    rec["D_S_at_pi"] = mp.nstr(S_n(PI), 15)

def main():
    t0 = time.time()
    out = {"script": "audit_a4_identity.py", "mp_dps": mp.mp.dps, "nmax": NMAX, "per_n": {}}
    for n in range(1, NMAX + 1):
        rec = {}
        run_n(n, rec)
        out["per_n"][str(n)] = rec
        print(f"n={n} done {time.time()-t0:.1f}s", file=sys.stderr, flush=True)
    out["elapsed_seconds"] = round(time.time() - t0, 2)
    print(json.dumps(out, indent=1))

if __name__ == "__main__":
    main()
