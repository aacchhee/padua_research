#!/usr/bin/env python3
"""MEASURED (float64, NOT a proof) sample check of the E14 global320 regional
conclusions at n=320 and n=321, using an independent implementation of the
PD-T364 cardinal identity L_jk=(w_jk/4)sum_{sigma,eta} G_n(theta+sigma a_j, phi+eta b_k),
G_n(u,v)=R_{n+1}(s)R_{n+1}(t)+R_n(s)R_n(t)-cos(n u), s=(u+v)/2,t=(u-v)/2.
lambda=sum|L|, and the primitive S at the chart phase equals M=sum (w/4)sum|g|.
Self-tests at n=5,6 against the direct D_n double sum, partition of unity,
cardinality at nodes.  Auditor Claude Opus 5.5 xhigh, 2026-11-07.
Usage: python3 sample320.py <seed> <points_per_region>
"""
import sys, math, time
import numpy as np

def Rk(k, z):
    l = np.round(z / np.pi)
    qq = z - l * np.pi
    sgn = np.where(((k - 1) * l.astype(np.int64)) % 2 == 0, 1.0, -1.0)
    small = np.abs(qq) < 1e-9
    with np.errstate(invalid="ignore", divide="ignore"):
        val = np.where(small, k * (1 - (k * k - 1) * qq * qq / 6.0), np.sin(k * qq) / np.where(small, 1.0, np.sin(qq)))
    return sgn * val

def G(n, u, v):
    s = (u + v) / 2.0; t = (u - v) / 2.0
    return Rk(n + 1, s) * Rk(n + 1, t) + Rk(n, s) * Rk(n, t) - np.cos(n * u)

def Gdirect(n, u, v):
    tot = 0.0
    for a in range(n + 1):
        for b in range(n + 1 - a):
            ha = 1 if a == 0 else 2; hb = 1 if b == 0 else 2
            tot += ha * hb * math.cos(a * u) * math.cos(b * v)
    return tot - math.cos(n * u)

class Padua:
    def __init__(self, n):
        self.n = n; m = n + 1; self.m = m; N = n * m
        J, K = np.meshgrid(np.arange(n + 1), np.arange(m + 1), indexing="ij")
        mask = (J + K) % 2 == 0
        self.j = J[mask].astype(float); self.k = K[mask].astype(float)
        e = np.where((self.j == 0) | (self.j == n), 0.5, 1.0)
        f = np.where((self.k == 0) | (self.k == m), 0.5, 1.0)
        self.w = 2 * e * f / N
        self.aj = self.j * np.pi / n; self.bk = self.k * np.pi / m
    def cards(self, th, ph):
        n = self.n
        g = [G(n, th + s * self.aj, ph + t * self.bk) for s in (1, -1) for t in (1, -1)]
        L = self.w / 4 * (g[0] + g[1] + g[2] + g[3])
        M = np.sum(self.w / 4 * (np.abs(g[0]) + np.abs(g[1]) + np.abs(g[2]) + np.abs(g[3])))
        return L, M
    def lam(self, th, ph):
        L, M = self.cards(th, ph)
        return float(np.sum(np.abs(L))), float(M), float(np.sum(L))

def selftest():
    ok = True
    rng = np.random.default_rng(1)
    for n in (5, 6):
        for _ in range(20):
            u, v = rng.uniform(-7, 7, 2)
            d = abs(float(G(n, np.array([u]), np.array([v]))[0]) - Gdirect(n, u, v))
            ok &= d < 1e-9
        for (u, v) in ((0.0, 0.0), (math.pi, math.pi), (0.0, math.pi), (1.3, 1.3), (1.3, -1.3), (2.0, 2.0 + 2 * math.pi)):
            d = abs(float(G(n, np.array([u]), np.array([v]))[0]) - Gdirect(n, u, v))
            ok &= d < 1e-8
        P = Padua(n)
        for _ in range(10):
            th, ph = rng.uniform(0, math.pi, 2)
            lam, M, s = P.lam(th, ph)
            ok &= abs(s - 1) < 1e-10 and M >= lam - 1e-12
        # cardinality at nodes
        for idx in range(len(P.j)):
            L, _ = P.cards(P.aj[idx], P.bk[idx])
            e = np.zeros_like(L); e[idx] = 1
            ok &= np.max(np.abs(L - e)) < 1e-9
    return ok

def main():
    seed = int(sys.argv[1]); npts = int(sys.argv[2])
    t0 = time.process_time()
    st = selftest()
    print("selftest (closed form vs direct D_n, partition of unity, cardinality n=5,6):", "PASS" if st else "FAIL")
    rng = np.random.default_rng(seed)
    allok = st
    for n in (320, 321):
        P = Padua(n); m = n + 1
        Lc, Mc, _ = P.lam(math.pi, math.pi)
        print(f"n={n}: Lambda_c=lambda(-1,-1)={Lc:.10f}, S(0)={Mc:.10f}, |diff|={abs(Lc-Mc):.2e}")
        other = (0.0, math.pi) if n % 2 == 0 else (math.pi, 0.0)
        Lc2, _, _ = P.lam(*other)
        print(f"   second parity corner lambda={Lc2:.10f}, |diff|={abs(Lc2-Lc):.2e}")
        corners = [(n, m), (0, m)] if n % 2 == 0 else [(n, m), (n, 0)]
        # noncorner centres concentrated near the corners + random
        near = []
        for (cj, ck) in corners:
            for dj in range(-4, 5):
                for dk in range(-4, 5):
                    J, K = cj + dj, ck + dk
                    if 0 <= J <= n and 0 <= K <= m and (J + K) % 2 == 1 and (J, K) not in corners:
                        near.append((J, K))
        def rand_centre():
            if rng.random() < 0.7:
                return near[rng.integers(len(near))]
            while True:
                J = int(rng.integers(0, n + 1)); K = int(rng.integers(0, m + 1))
                if (J + K) % 2 == 1 and (J, K) not in corners:
                    return (J, K)
        def rand_phase(J, K, rlo, rhi):
            for _ in range(1000):
                r = rng.uniform(rlo, rhi); tt = rng.uniform(-1, 1)
                al = r * tt; be = (r - abs(al)) * (1 if rng.random() < 0.5 else -1)
                if -J * math.pi <= al <= (n - J) * math.pi and -K * math.pi <= be <= (m - K) * math.pi:
                    return al, be
            return None
        stats = {}
        def rec(key, gap):
            s = stats.setdefault(key, [math.inf, 0, 0]); s[0] = min(s[0], gap); s[1] += 1
        regions = [("noncorner rho<=1/2 lambda gap>1/20000", 0.0, 0.5, "lam", 1 / 20000),
                   ("noncorner 1/2<=rho<=3/5 lambda gap>3/1000", 0.5, 0.6, "lam", 3 / 1000),
                   ("all 3/5<=rho<=1 S gap>99/2500", 0.6, 1.0, "S", 99 / 2500),
                   ("all 1<=rho<=pi S gap>13/500", 1.0, math.pi, "S", 13 / 500)]
        for name, rlo, rhi, kind, need in regions:
            for i in range(npts):
                if kind == "S" and rng.random() < 0.3:
                    J, K = corners[rng.integers(len(corners))]
                else:
                    J, K = rand_centre()
                ph = rand_phase(J, K, rlo, rhi)
                if ph is None:
                    continue
                al, be = ph
                lam, M, _ = P.lam((J * math.pi + al) / n, (K * math.pi + be) / m)
                gap = Lc - (lam if kind == "lam" else M)
                rec(name, gap)
                if gap <= need:
                    allok = False
                    print("  VIOLATION", name, J, K, al, be, gap)
        # corner squares: inward A,B in [0,pi/4]^2 at both corners, loss (A^2+B^2)/30
        cname = "corner squares lambda<=Lc-(A^2+B^2)/30"
        for i in range(npts):
            J, K = corners[rng.integers(len(corners))]
            A, B = rng.uniform(0, math.pi / 4, 2) * (rng.uniform(0, 1) ** (1 if i % 2 else 3))
            al = -A if J == n else A; be = -B if K == m else B
            lam, M, _ = P.lam((J * math.pi + al) / n, (K * math.pi + be) / m)
            rec(cname, (Lc - lam) - (A * A + B * B) / 30)
            if A * A + B * B > 1e-6:
                rec("corner squares min (Lc-lambda)/(A^2+B^2) [need>=1/30=0.0333]", (Lc - lam) / (A * A + B * B))
            if Lc - lam < (A * A + B * B) / 30 - 1e-11:  # run2: float64 roundoff tolerance (run1 flagged A,B~3e-12, diff -3.6e-15)
                allok = False; print("  VIOLATION corner", J, K, A, B, Lc - lam)
        # nodes: lambda=1
        idx = rng.integers(len(P.j), size=5)
        nodedev = max(abs(P.lam(P.aj[i], P.bk[i])[0] - 1) for i in idx)
        print(f"   nodes: max|lambda-1| over 5 random nodes = {nodedev:.2e}")
        for k_, v in stats.items():
            print(f"   {k_}: samples={v[1]}, min observed gap(excess)={v[0]:.6f}")
    print(f"CPU seconds: {time.process_time()-t0:.1f}")
    print("OVERALL", "PASS" if allok else "FAIL")
    sys.exit(0 if allok else 1)

if __name__ == "__main__":
    main()
