"""Fast exact interpolation / evaluation on finite-field Padua points (Padua2DM over F_p).

values f on Pad_n(F_p)  <->  coefficients c_ab (a+b<=n) in the product Chebyshev basis T_a(x)T_b(y)

Interpolation (from discrete orthogonality V^T W V = D):
    c = D^{-1} C_x^T G C_y,   G_jk = w_jk f(x_j,y_k) on the checkerboard (0 elsewhere),
where C_x[j][a] = T_a(x_j) (size (n+1)^2) and C_y[k][b] = T_b(y_k) (size (n+2)^2) are DCT-I matrices.
Evaluation: f_jk = (C_x Cpad C_y^T)_jk on the checkerboard.
DCT-I of length m+1 over F_p is computed from one length-2m DFT over F_{p^2} (the root of unity
lives in F_p in the split case, in F_{p^2} in the non-split case):
    sum_{j=0}^m g_j T_a(x_j) = ( DFT_{2m}(even extension of g)_a + g_0 + (-1)^a g_m ) / 2.
Cost: (2n+3) DFTs of length ~2n per direction  ->  O(n^2 log n) for smooth 2n, 2n+2
(this mixed-radix code: O(n^2 * sum of prime factors)).
Run: python3 -I fast_transform.py
"""
import sys, os, time, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ffield import Fp2, is_prime, power_table, fft, factorize
from padua_ff import PaduaFF, axis_type, basis_index, rank_mod_p


class FastPadua:
    def __init__(self, n, p):
        self.n, self.p = n, p
        F = self.F = Fp2(p)
        assert axis_type(p, 2 * n) and axis_type(p, 2 * n + 2) and (n * (n + 1)) % p
        self.z = F.root_of_unity(2 * n); self.e = F.root_of_unity(2 * n + 2)
        self.pwz = power_table(F, self.z, 2 * n); self.pwe = power_table(F, self.e, 2 * n + 2)
        h = self.h = pow(2, p - 2, p)
        self.xs = [F.smul(h, F.add(self.pwz[j % (2*n)], self.pwz[(-j) % (2*n)]))[0] for j in range(n + 1)]
        self.ys = [F.smul(h, F.add(self.pwe[k % (2*n+2)], self.pwe[(-k) % (2*n+2)]))[0] for k in range(n + 2)]
        c = 2 * pow(n * (n + 1), p - 2, p) % p
        ee = lambda i, m: h if i in (0, m) else 1
        self.W = [[c * ee(j, n) * ee(k, n + 1) % p if (j + k) % 2 == 0 else 0 for k in range(n + 2)] for j in range(n + 1)]

    def dct1(self, g, axis):
        """out_a = sum_{j=0}^m g_j T_a(node_j), a = 0..m  (m = n for x-axis, n+1 for y-axis)."""
        F, p = self.F, self.p
        m = len(g) - 1
        pw = self.pwz if axis == 0 else self.pwe
        ext = [(v % p, 0) for v in g] + [(g[j] % p, 0) for j in range(m - 1, 0, -1)]
        Y = fft(F, ext, pw[1], pw)
        out = []
        for a in range(m + 1):
            v = F.add(Y[a], ((g[0] + (g[m] if a % 2 == 0 else -g[m])) % p, 0))
            assert v[1] == 0
            out.append(v[0] * self.h % p)
        return out

    def interpolate(self, fvals):
        """fvals: dict (j,k) -> value on Pad_n. Returns dict (a,b) -> c_ab."""
        n, p = self.n, self.p
        G = [[self.W[j][k] * fvals.get((j, k), 0) % p for k in range(n + 2)] for j in range(n + 1)]
        # x-direction: for each k, transform over j
        S1 = [self.dct1([G[j][k] for j in range(n + 1)], 0) for k in range(n + 2)]   # S1[k][a]
        # y-direction: for each a, transform over k
        S = [self.dct1([S1[k][a] for k in range(n + 2)], 1) for a in range(n + 1)]    # S[a][b]
        inv2 = 2  # 1/(1/2)
        out = {}
        for a, b in basis_index(n):
            if (a, b) == (n, 0): d_inv = 1
            else: d_inv = (1 if a == 0 else 2) * (1 if b == 0 else 2)
            out[(a, b)] = S[a][b] * d_inv % p
        return out

    def evaluate(self, coef):
        """coef: dict (a,b) -> c_ab, a+b <= n. Returns dict (j,k) -> f(x_j, y_k) on Pad_n."""
        n, p = self.n, self.p
        C = [[coef.get((a, b), 0) for b in range(n + 2)] for a in range(n + 1)]
        # over a (x-direction) for each b: E1[b][j] = sum_a C[a][b] T_a(x_j)  (DCT-I is symmetric)
        E1 = [self.dct1([C[a][b] for a in range(n + 1)], 0) for b in range(n + 2)]
        E = [self.dct1([E1[b][j] for b in range(n + 2)], 1) for j in range(n + 1)]   # E[j][k]
        return {(j, k): E[j][k] for j in range(n + 1) for k in range(n + 2) if (j + k) % 2 == 0}


def find_prime(n, lo=3, types=None, hi=None):
    p = lo | 1
    hi = hi or lo + 200 * n * (n + 1) + 1000
    while p < hi:
        if is_prime(p) and (n * (n + 1)) % p and axis_type(p, 2 * n) and axis_type(p, 2 * n + 2):
            if types is None or (axis_type(p, 2 * n), axis_type(p, 2 * n + 2)) in types: return p
        p += 2
    return None


def dense_check(n, p):
    """compare with dense evaluation through the Chebyshev Vandermonde."""
    P = PaduaFF(n, p); V = P.vandermonde_cheb(); fp = FastPadua(n, p)
    assert P.xs == fp.xs and P.ys == fp.ys
    rng = random.Random(n * 1000 + p)
    coef = {ab: rng.randrange(p) for ab in basis_index(n)}
    cv = [coef[ab] for ab in P.idx]
    vals_dense = {jk: sum(v * c for v, c in zip(V[i], cv)) % p for i, jk in enumerate(P.jk)}
    vals_fast = fp.evaluate(coef)
    back = fp.interpolate(vals_fast)
    return vals_dense == vals_fast and back == coef


if __name__ == '__main__':
    print("dense vs fast (evaluation) and round trip (interpolation o evaluation = id):")
    for n in range(1, 13):
        for t in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            p = find_prime(n, types=[t])
            if p is None: continue          # n = 1: 2n = 2 divides p-1 and p+1, only 'split' x-type
            ok = dense_check(n, p)
            print(f"  n={n:2d} p={p:6d} type={t}: {'OK' if ok else 'FAIL'}")
            assert ok
    print("\ntiming of fast transform (pure Python, mixed radix FFT):")
    print("   n      p     N=dim P_n   2n factors      2n+2 factors   eval[s]  interp[s]  roundtrip")
    for n in [8, 16, 24, 32, 48, 64, 80, 96, 128]:
        p = find_prime(n, lo=10**6)
        fp = FastPadua(n, p); rng = random.Random(n)
        coef = {ab: rng.randrange(p) for ab in basis_index(n)}
        t0 = time.time(); vals = fp.evaluate(coef); t1 = time.time(); back = fp.interpolate(vals); t2 = time.time()
        N = (n + 1) * (n + 2) // 2
        print(f"  {n:4d} {p:9d} {N:8d}   {str(factorize(2*n)):14s} {str(factorize(2*n+2)):16s} {t1-t0:7.2f}  {t2-t1:7.2f}   {back == coef}")
