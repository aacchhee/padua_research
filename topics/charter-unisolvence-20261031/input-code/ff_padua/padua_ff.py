"""Padua points over finite fields F_p (exact arithmetic, pure Python).

Definition (finite-field Padua set).  Let n >= 1, p an odd prime with p not dividing n(n+1),
zeta a primitive 2n-th and eta a primitive 2(n+1)-th root of unity in F_{p^2}. Put
    x_j = (zeta^j + zeta^-j)/2   (0 <= j <= n),     y_k = (eta^k + eta^-k)/2   (0 <= k <= n+1),
    Pad_n(F) = {(x_j, y_k) : j + k even}.
Equivalently Pad_n = {((u+1/u)/2, (v+1/v)/2) : u in mu_{2n}, v in mu_{2n+2}, u^n = v^{n+1}}
(independent of the choice of zeta, eta).  All coordinates lie in F_p iff
    p = +-1 mod 2n   and   p = +-1 mod 2(n+1)          (four 'types': split/nonsplit per axis).
This script checks, for many (n, p):
  1. cardinality (n+1)(n+2)/2 and distinctness of the nodes, F_p-rationality;
  2. unisolvence for P_n (rank of Chebyshev and monomial Vandermonde mod p);
  3. discrete orthogonality V^T W V = D exactly (D diagonal, only T_n(x) 'norm^2 2'),
     with W = 2 e_j e_k/(n(n+1)), e = 1/2 at the ends;
  4. cubature exactness set: sum_A w_A T_a(x_A)T_b(y_A) = delta_{a0}delta_{b0} for all a+b <= 2n+1
     except exactly (a,b) = (2n,0) and (n,n+1);
  5. the Padua discriminant  det V_mon(2x,2y)^2 = 2^{(n^2+3n+6)/2} (n(n+1))^{(n+1)(n+2)/2}  (mod p);
  6. the two-term ideal generators T_{n+1}(x)-T_{n-1}(x), T_{n+1-r}(x)T_r(y)-T_{r-1}(x)T_{n+1-r}(y)
     (1<=r<=n+1) vanish on Pad_n(F_p);
  7. multiplication ('recurrence') matrices M_x, M_y in the Chebyshev product basis:
     diag(x) V = V M_x, <= 2 nonzeros/column, D M_x symmetric (self-adjoint for the cubature form);
  8. the set does not depend on the choice of primitive roots.
Run:  python3 -I padua_ff.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ffield import Fp2, is_prime, rank_mod_p, det_mod_p, matmul_mod, transpose


def axis_type(p, L):
    """+1 if L | p-1 (split torus), -1 if L | p+1 (non-split), None otherwise."""
    if (p - 1) % L == 0: return +1
    if (p + 1) % L == 0: return -1
    return None


def cheb_table(vals, deg, p):
    """T[a][i] = T_a(vals[i]) mod p, a = 0..deg."""
    T = [[1] * len(vals), [v % p for v in vals]]
    for a in range(1, deg):
        T.append([(2 * v * t1 - t0) % p for v, t1, t0 in zip(vals, T[a], T[a - 1])])
    return T[:deg + 1]


def basis_index(n):
    return [(a, d - a) for d in range(n + 1) for a in range(d, -1, -1)]


class PaduaFF:
    def __init__(self, n, p, zeta_pow=1, eta_pow=1):
        assert is_prime(p) and p > 2 and (n * (n + 1)) % p != 0
        self.n, self.p = n, p
        F = self.F = Fp2(p)
        self.tx, self.ty = axis_type(p, 2 * n), axis_type(p, 2 * n + 2)
        z = F.pow(F.root_of_unity(2 * n), zeta_pow)
        e = F.pow(F.root_of_unity(2 * n + 2), eta_pow)
        self.zeta, self.eta = z, e
        h = pow(2, p - 2, p)
        xs2 = [F.smul(h, F.add(F.pow(z, j), F.pow(z, -j))) for j in range(n + 1)]
        ys2 = [F.smul(h, F.add(F.pow(e, k), F.pow(e, -k))) for k in range(n + 2)]
        self.rational = all(F.in_base(v) for v in xs2 + ys2)
        self.xs2, self.ys2 = xs2, ys2
        if not self.rational: return
        self.xs = [v[0] for v in xs2]; self.ys = [v[0] for v in ys2]
        self.jk = [(j, k) for j in range(n + 1) for k in range(n + 2) if (j + k) % 2 == 0]
        self.pts = [(self.xs[j], self.ys[k]) for j, k in self.jk]
        inv = lambda a: pow(a % p, p - 2, p)
        c = 2 * inv(n * (n + 1)) % p
        ee = lambda i, m: h if i in (0, m) else 1
        self.w = [c * ee(j, n) * ee(k, n + 1) % p for j, k in self.jk]
        self.idx = basis_index(n)

    # ---------- matrices ----------
    def vandermonde_cheb(self, deg=None):
        n, p = self.n, self.p; deg = n if deg is None else deg
        X = [x for x, _ in self.pts]; Y = [y for _, y in self.pts]
        TX, TY = cheb_table(X, deg + 1, p), cheb_table(Y, deg + 1, p)
        self.TX, self.TY = TX, TY
        return [[TX[a][i] * TY[b][i] % p for (a, b) in self.idx] for i in range(len(self.pts))]

    def vandermonde_mon(self, scale=1):
        p = self.p
        return [[pow(scale * x, a, p) * pow(scale * y, b, p) % p for (a, b) in self.idx] for x, y in self.pts]

    def D_expected(self):
        n, p = self.n, self.p; h = pow(2, p - 2, p)
        ca = lambda a: 1 if a == 0 else h
        return [1 if (a, b) == (n, 0) else ca(a) * ca(b) % p for (a, b) in self.idx]

    # ---------- checks ----------
    def check_all(self, verbose=False):
        n, p = self.n, self.p
        R = {'n': n, 'p': p, 'type': (self.tx, self.ty), 'rational': self.rational}
        if not self.rational: return R
        N = (n + 1) * (n + 2) // 2
        R['card_ok'] = (len(self.pts) == N == len(set(self.pts)))
        R['nodes_distinct'] = (len(set(self.xs)) == n + 1 and len(set(self.ys)) == n + 2)
        V = self.vandermonde_cheb()
        R['rank_cheb'] = rank_mod_p(V, p)
        R['rank_mon'] = rank_mod_p(self.vandermonde_mon(), p)
        # discrete orthogonality
        WV = [[self.w[i] * v % p for v in row] for i, row in enumerate(V)]
        G = matmul_mod(transpose(V), WV, p)
        D = self.D_expected()
        R['gram_is_D'] = all(G[r][s] == (D[r] if r == s else 0) for r in range(N) for s in range(N))
        # cubature exactness set for a+b <= 2n+1
        TX, TY = cheb_table([x for x, _ in self.pts], 2 * n + 1, p), cheb_table([y for _, y in self.pts], 2 * n + 1, p)
        fails = []
        for a in range(2 * n + 2):
            for b in range(2 * n + 2 - a):
                s = sum(wi * TX[a][i] * TY[b][i] for i, wi in enumerate(self.w)) % p
                if s != (1 if a == b == 0 else 0): fails.append((a, b))
        R['cubature_fails'] = fails
        # Padua discriminant (Dickson coordinates X = 2x, Y = 2y)
        e2 = (n * n + 3 * n + 6) // 2
        disc = pow(2, e2, p) * pow(n * (n + 1), N, p) % p
        dm = det_mod_p(self.vandermonde_mon(scale=2), p)
        R['discriminant_ok'] = (dm * dm % p == disc)
        # ideal generators
        gens_ok = all((TX[n + 1][i] - TX[n - 1][i]) % p == 0 for i in range(N))
        for r in range(1, n + 2):
            gens_ok &= all((TX[n + 1 - r][i] * TY[r][i] - TX[r - 1][i] * TY[n + 1 - r][i]) % p == 0 for i in range(N))
        R['ideal_gens_vanish'] = gens_ok
        # multiplication matrices
        Mx, My = self.mult_matrices()
        X = [x for x, _ in self.pts]; Y = [y for _, y in self.pts]
        ok = True; nnz = 0; sym = True
        for M, C in ((Mx, X), (My, Y)):
            VM = matmul_mod(V, M, p)
            ok &= all(VM[i][s] == C[i] * V[i][s] % p for i in range(N) for s in range(N))
            nnz = max(nnz, max(sum(1 for r in range(N) if M[r][s]) for s in range(N)))
            DM = [[D[r] * M[r][s] % p for s in range(N)] for r in range(N)]
            sym &= all(DM[r][s] == DM[s][r] for r in range(N) for s in range(N))
        R['mult_ok'], R['mult_max_nnz_col'], R['DM_symmetric'] = ok, nnz, sym
        return R

    def mult_matrices(self):
        """M_x, M_y with diag(x) V = V M_x, in the Chebyshev product basis, using only
        T_a T_b = (T_{a+b}+T_{|a-b|})/2 and the ideal relations on Pad_n."""
        n, p = self.n, self.p; h = pow(2, p - 2, p)
        pos = {ab: i for i, ab in enumerate(self.idx)}; N = len(self.idx)
        def reduce(a, b):           # T_a(x)T_b(y), a+b <= n+1  ->  basis index
            if a + b <= n: return (a, b)
            if b == 0: return (n - 1, 0)            # T_{n+1}(x) = T_{n-1}(x)
            return (b - 1, a)                        # T_{n+1-r}(x)T_r(y) = T_{r-1}(x)T_{n+1-r}(y), r=b
        Ms = []
        for var in (0, 1):
            M = [[0] * N for _ in range(N)]
            for s, (a, b) in enumerate(self.idx):
                if var == 0: terms = [(1, (1, b))] if a == 0 else [(h, (a + 1, b)), (h, (a - 1, b))]
                else:        terms = [(1, (a, 1))] if b == 0 else [(h, (a, b + 1)), (h, (a, b - 1))]
                for c, ab in terms:
                    r = pos[reduce(*ab)]; M[r][s] = (M[r][s] + c) % p
            Ms.append(M)
        return Ms


def admissible_primes(n, pmax, per_type=2):
    out = {}
    for p in range(3, pmax, 2):
        if not is_prime(p) or (n * (n + 1)) % p == 0: continue
        t = (axis_type(p, 2 * n), axis_type(p, 2 * n + 2))
        if None in t: continue
        out.setdefault(t, [])
        if len(out[t]) < per_type: out[t].append(p)
    return out


def canonical_check(n, p):
    """Pad_n(F_p) is independent of the chosen primitive roots."""
    from math import gcd
    base = set(PaduaFF(n, p).pts)
    for r in range(1, 2 * n):
        if gcd(r, 2 * n) != 1: continue
        for s in range(1, 2 * n + 2):
            if gcd(s, 2 * n + 2) != 1: continue
            if set(PaduaFF(n, p, r, s).pts) != base: return False
    return True


if __name__ == '__main__':
    names = {1: 'split', -1: 'nonsplit'}
    allok = True
    for n in range(1, 11):
        adm = admissible_primes(n, 6000, per_type=2)
        for t in sorted(adm):
            for p in adm[t]:
                P = PaduaFF(n, p); R = P.check_all()
                N = (n + 1) * (n + 2) // 2
                good = (R['rational'] and R['card_ok'] and R['nodes_distinct'] and R['rank_cheb'] == N
                        and R['rank_mon'] == N and R['gram_is_D'] and R['discriminant_ok']
                        and R['ideal_gens_vanish'] and R['mult_ok'] and R['mult_max_nnz_col'] <= 2
                        and R['DM_symmetric'] and set(R['cubature_fails']) == {(2 * n, 0), (n, n + 1)})
                if n == 1: good = good and True
                allok &= good
                print(f"n={n:2d} p={p:5d} x:{names[t[0]]:8s} y:{names[t[1]]:8s} N={N:3d} rank={R['rank_cheb']:3d}"
                      f" gram=D:{R['gram_is_D']} disc:{R['discriminant_ok']} gens:{R['ideal_gens_vanish']}"
                      f" Mx/My ok:{R['mult_ok']} nnz/col<={R['mult_max_nnz_col']} DM sym:{R['DM_symmetric']}"
                      f" cub-fails(a+b<=2n+1):{R['cubature_fails']}  {'OK' if good else 'FAIL'}")
    print("canonical (root-independent) for (n,p) in [(3,7),(4,31),(5,11),(6,13)]:",
          [canonical_check(n, p) for n, p in [(3, 7), (4, 31), (5, 11), (6, 13)]])
    # rationality is necessary: a prime with p != +-1 mod 2n gives nodes outside F_p
    P = PaduaFF(3, 13)
    print("n=3, p=13 (13 = 1 mod 6 but 13 = 5 mod 8): nodes rational?", P.rational,
          "| y-nodes in F_p:", [P.F.in_base(v) for v in P.ys2])
    print("ALL CHECKS PASSED" if allok else "SOME CHECK FAILED")
