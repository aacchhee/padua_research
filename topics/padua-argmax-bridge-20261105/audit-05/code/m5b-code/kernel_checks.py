#!/usr/bin/env python3
"""M5B: numeric checks (MEASURED) of two new displayed identities.
1. paper prelim: p(z)=sum_B w_B p(B) Ktilde_n(z,B) for p in Pi_n (Padua nodes eq:nodes).
2. cert: G_n(u,v)=R_{n+1}(s)R_{n+1}(t)+R_n(s)R_n(t)-cos(nu), s=(u+v)/2,t=(v-u)/2,
   with R_l(j*pi)=l(-1)^{j(l-1)} at removable arguments.
3. sine product sin(nz)=2^{n-1} prod sin(z+l pi/n); D_n(pi,pi)=(-1)^n(2n+1).
4. folding identity for Q_v (companion C4D-14 display) at random phases.
"""
import math
import random

random.seed(20261113)


def T(p, x):
    return math.cos(p * math.acos(max(-1.0, min(1.0, x))))


def nodes(n):
    m = n + 1
    out = []
    for j in range(n + 1):
        for k in range(m + 1):
            if (j + k) % 2 == 0:
                e = 0.5 if j in (0, n) else 1.0
                f = 0.5 if k in (0, m) else 1.0
                out.append((math.cos(j * math.pi / n), math.cos(k * math.pi / m), 2 * e * f / (n * m)))
    return out


def nu(r):
    return 1.0 if r == 0 else 2.0


def K(n, z, B):
    s = 0.0
    for p in range(n + 1):
        for q in range(n + 1 - p):
            s += nu(p) * nu(q) * T(p, z[0]) * T(p, B[0]) * T(q, z[1]) * T(q, B[1])
    return s


def check_reproducing():
    worst = 0.0
    for n in range(1, 8):
        P = nodes(n)
        assert len(P) == (n + 1) * (n + 2) // 2
        for _ in range(5):
            coef = {(p, q): random.uniform(-1, 1) for p in range(n + 1) for q in range(n + 1 - p)}
            poly = lambda x, y: sum(c * T(p, x) * T(q, y) for (p, q), c in coef.items())
            z = (random.uniform(-1, 1), random.uniform(-1, 1))
            rhs = sum(w * poly(bx, by) * (K(n, z, (bx, by)) - T(n, z[0]) * T(n, bx)) for bx, by, w in P)
            worst = max(worst, abs(rhs - poly(*z)))
    return worst


def G_def(n, u, v):
    s = 0.0
    for p in range(n + 1):
        for q in range(n + 1 - p):
            s += nu(p) * nu(q) * math.cos(p * u) * math.cos(q * v)
    return s - math.cos(n * u)


def R(l, x):
    j = round(x / math.pi)
    if abs(x - j * math.pi) < 1e-15:
        return l * (-1) ** (j * (l - 1))
    return math.sin(l * x) / math.sin(x)


def G_prod(n, u, v):
    s, t = (u + v) / 2, (v - u) / 2
    return R(n + 1, s) * R(n + 1, t) + R(n, s) * R(n, t) - math.cos(n * u)


def check_product():
    worst = 0.0
    for n in range(1, 10):
        pts = [(random.uniform(-7, 7), random.uniform(-7, 7)) for _ in range(30)]
        # collisions: u = +-v + 2 pi k, and u=v=0, pi
        pts += [(a, a) for a in (0.0, 0.3, math.pi, 2 * math.pi)] + [(a, -a) for a in (0.7, math.pi)] + [(a, a + 2 * math.pi) for a in (1.1,)]
        for u, v in pts:
            worst = max(worst, abs(G_prod(n, u, v) - G_def(n, u, v)))
    return worst


def check_sine_product_and_Dpipi():
    worst = 0.0
    for n in range(1, 12):
        for _ in range(10):
            z = random.uniform(-3, 3)
            lhs = math.sin(n * z)
            rhs = 2 ** (n - 1)
            for l in range(n):
                rhs *= math.sin(z + l * math.pi / n)
            worst = max(worst, abs(lhs - rhs))
        D = sum((-1) ** (p + q) for p in range(-n, n + 1) for q in range(-n, n + 1) if abs(p) + abs(q) <= n)
        assert D == (-1) ** n * (2 * n + 1), (n, D)
    return worst


def check_folding():
    worst = 0.0
    for n in (3, 4, 7):
        m = n + 1
        N = n * m
        for _ in range(3):
            J = random.randrange(0, n + 1)
            K_ = random.choice([k for k in range(m + 1) if (J + k) % 2 == 1])
            al, be = random.uniform(-1, 1), random.uniform(-1, 1)
            H = lambda r, s: G_def(n, (r * math.pi + al) / n, (s * math.pi + be) / m)
            d = lambda a, b: abs(a) + abs(b) - abs(a + b)
            lhs = sum(d(H(r, s), H(r, (2 * K_ - s) % (2 * m))) for r in range(2 * n) for s in range(2 * m) if (r + s) % 2 == 1) / (4 * N)
            phi = (K_ * math.pi + be) / m
            rhs = 0.0
            for k in range(m + 1):
                eta = 0.5 if k in (0, m) else 1.0
                for r in range(2 * n):
                    if (r + k) % 2 == J % 2:
                        Vp = (-1) ** r * G_def(n, (r * math.pi + al) / n, phi + k * math.pi / m) / 2
                        Vm = (-1) ** r * G_def(n, (r * math.pi + al) / n, phi - k * math.pi / m) / 2
                        rhs += eta * d(Vp, Vm)
            rhs /= N
            worst = max(worst, abs(lhs - rhs))
    return worst


if __name__ == '__main__':
    print('reproducing kernel max err n=1..7:', check_reproducing())
    print('product-form kernel max err n=1..9 incl. collisions:', check_product())
    print('sine product max err; D_n(pi,pi) exact n=1..11:', check_sine_product_and_Dpipi())
    print('Q_v folding identity max err:', check_folding())
