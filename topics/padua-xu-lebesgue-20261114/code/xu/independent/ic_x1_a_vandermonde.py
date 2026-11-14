"""Independent check (a): Xu Lagrange basis by direct Vandermonde solve in mpmath.

Definitions only (literature-xu-mp.md s.1): nodes (cos(r pi/n), cos(s pi/n)),
r+s = n+1 mod 2; V_n = Pi_{n-1} + span{T_{n-j}(x)T_j(y) - sigma T_j(x)T_{n-j}(y)}.
No kernel formula, no developer code.
"""
import sys, random, json
import mpmath as mp

mp.mp.dps = 50
pi = mp.pi


def T(k, x):
    return mp.chebyt(k, x)


def nodes(n):
    return [(r, s) for r in range(n + 1) for s in range(n + 1) if (r + s) % 2 == (n + 1) % 2]


def basis_vals(n, x, y):
    sig = 1 if n % 2 == 0 else -1
    Tx = [T(k, x) for k in range(n + 1)]
    Ty = [T(k, y) for k in range(n + 1)]
    v = [Tx[i] * Ty[j] for i in range(n) for j in range(n - i)]
    for j in range((n + 1) // 2):
        v.append(Tx[n - j] * Ty[j] - sig * Tx[j] * Ty[n - j])
    return v


def Lcheb(n):
    return mp.fsum(mp.cot((2 * k - 1) * pi / (4 * n)) for k in range(1, n + 1)) / n


def dn(n, t):
    return (1 + 2 * mp.fsum(mp.cos(j * t) for j in range(1, n)) + mp.cos(n * t)) / (2 * n)


def setup(n):
    nd = nodes(n)
    z = [mp.cos(k * pi / n) for k in range(n + 1)]
    A = mp.matrix([basis_vals(n, z[r], z[s]) for (r, s) in nd])
    assert A.rows == A.cols, (A.rows, A.cols)
    C = mp.inverse(A)
    # residual check
    R = A * C
    res = max(abs(R[i, j] - (1 if i == j else 0)) for i in range(R.rows) for j in range(R.cols))
    return nd, z, C, res


def ells(n, C, x, y):
    phi = basis_vals(n, x, y)
    N = C.cols
    return [mp.fsum(phi[b] * C[b, k] for b in range(N)) for k in range(N)]


def main():
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    npts = int(sys.argv[2]) if len(sys.argv) > 2 else 500
    rng = random.Random(20261114)
    out = {}
    for n in range(2, nmax + 1):
        nd, z, C, res = setup(n)
        L2 = Lcheb(n) ** 2
        verts = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        vres = {}
        for (vx, vy) in verts:
            lam = mp.fsum(abs(l) for l in ells(n, C, mp.mpf(vx), mp.mpf(vy)))
            vres[(vx, vy)] = lam
        # X1-03 (1) per node at non-node vertices
        worst03 = mp.mpf(0)
        for (vx, vy) in verts:
            av = 0 if vx == 1 else n
            bv = 0 if vy == 1 else n
            if (av + bv) % 2 == (n + 1) % 2:
                continue  # node vertex
            ls = ells(n, C, mp.mpf(vx), mp.mpf(vy))
            for k, (r, s) in enumerate(nd):
                rp, sp = abs(r - av), abs(s - bv)
                assert (rp + sp) % 2 == 1
                beta = (r in (0, n)) + (s in (0, n))
                w = mp.mpf(2) ** (1 - beta) / n ** 2
                val = w * (-1) ** rp * (2 + z[rp] + z[sp]) / (z[rp] - z[sp])
                worst03 = max(worst03, abs(val - ls[k]))
        # random points
        maxlam = mp.mpf(0)
        maxratio = mp.mpf(0)
        viol = 0
        for _ in range(npts):
            x = mp.mpf(rng.uniform(-1, 1)); y = mp.mpf(rng.uniform(-1, 1))
            lam = mp.fsum(abs(l) for l in ells(n, C, x, y))
            maxlam = max(maxlam, lam)
            if lam > L2:
                viol += 1
        # lift formula X1-01 (1) at 15 random (u,v), fiber sizes
        Cn = [p for p in range(4 * n) if p % 2 == (n + 1) % 2]
        fib = {}
        for p in Cn:
            for q in Cn:
                th1 = (p + q) * pi / (2 * n); th2 = (p - q) * pi / (2 * n)
                # identify node
                r = int(mp.nint(mp.acos(mp.cos(th1)) * n / pi)); s = int(mp.nint(mp.acos(mp.cos(th2)) * n / pi))
                fib.setdefault((r, s), []).append((p, q))
        assert set(fib) == set(nd), "fiber image != node set"
        sizes_ok = all(len(fib[(r, s)]) == 2 ** (3 - ((r in (0, n)) + (s in (0, n)))) for (r, s) in nd)
        worst01 = mp.mpf(0)
        omega_bound_viol = 0
        for _ in range(15):
            u = mp.mpf(rng.uniform(-4, 4)); v = mp.mpf(rng.uniform(-4, 4))
            ls = ells(n, C, mp.cos(u + v), mp.cos(u - v))
            du = {p: dn(n, u - p * pi / (2 * n)) for p in Cn}
            dv = {q: dn(n, v - q * pi / (2 * n)) for q in Cn}
            for k, key in enumerate(nd):
                rhs = mp.fsum(du[p] * dv[q] for (p, q) in fib[key])
                worst01 = max(worst01, abs(rhs - ls[k]))
            lam = mp.fsum(abs(l) for l in ls)
            om = mp.fsum(abs(du[p]) for p in Cn) * mp.fsum(abs(dv[q]) for q in Cn)
            if lam > om * (1 + mp.mpf(10) ** -40) or om > L2 * (1 + mp.mpf(10) ** -40):
                omega_bound_viol += 1
        nv = [k for k in verts if True]
        line = dict(n=n, N=len(nd), inv_res=mp.nstr(res, 3), L2=mp.nstr(L2, 20),
                    vertex_dev={str(k): mp.nstr(vres[k] - (L2 if ((0 if k[0] == 1 else n) + (0 if k[1] == 1 else n)) % 2 == n % 2 else 1), 3) for k in verts},
                    worst_X1_03_formula=mp.nstr(worst03, 3), rand_max_lam=mp.nstr(maxlam, 12),
                    rand_max_ratio=mp.nstr(maxlam / L2, 6), rand_viol=viol,
                    fiber_sizes_ok=sizes_ok, worst_lift=mp.nstr(worst01, 3), omega_bound_viol=omega_bound_viol)
        print(json.dumps(line), flush=True)
        out[n] = line
    json.dump(out, open('/tmp/ic-x1/a_out.json', 'w'), indent=1)


if __name__ == '__main__':
    main()
