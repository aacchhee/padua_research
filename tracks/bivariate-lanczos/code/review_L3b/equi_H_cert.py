"""Reviewer (L3 reconstruction 02): independent exact certificates for condition (H) on the ordered
equispaced checkerboards S_0(n) = {(-1 + 2i/n, -1 + 2j/(n+1)) : i + j even} (PD-T?...-310/311).

Independent of the developer's exact_checkerboard.py / exact_certificates.py (not imported):
 * basis of Pi_{2n+1}: Chebyshev products T_a(x) T_b(y), a + b <= 2n+1 (developer: monomials);
 * exact jet matrix, nullspace S_1, rank of the Hessian map: own Fraction RREF;
 * proposer: own primal-dual-free BARRIER method in mpmath high precision (no SDP package):
     maximise s  s.t.  B_i(theta) - s I > 0 (2x2 blocks, affine in theta),  normalisation eliminated;
   DUAL: theta = coordinates in an exact rational basis of null(G), G v = 0 the S_1-annihilation
         constraints, B_i = A_i, normalisation sum_i tr A_i = 1;
   PRIMAL (run if the dual optimum is <= 0): theta = coordinates of p in the exact S_1 basis,
         B_i = Hess p(z_i), normalisation sum_i tr Hess p(z_i) = 1;
 * acceptance: theta rounded to rationals; v = V theta (resp. p = sum theta_k s_k) lies EXACTLY in the
   constraint space by construction; exact PD test of every 2x2 block (a > 0, ad - b^2 > 0).
Prints dim S_1, rank of the Hessian map, the high-precision optimum t_D (dual, same normalisation as
the developer: sum tr A_i = 1, t = min lambda_min) and the exact certified min_i det/tr.
Usage: python3 -I equi_H_cert.py nmin nmax [dps] [equi|randrat] [seeds, e.g. 1,2,3]
(randrat = negative-control family: N_n random rational points in [-1,1]^2 with denominators 1000)
"""
import sys
import time
from fractions import Fraction as Fr
import mpmath as mp


# ------------------------------------------------------------------ exact linear algebra (own)
def rref(A):
    """A: list of rows of Fractions. Returns (R, pivots)."""
    R = [list(r) for r in A]
    m = len(R); ncol = len(R[0]) if m else 0
    piv = []; r = 0
    for c in range(ncol):
        p = next((i for i in range(r, m) if R[i][c] != 0), None)
        if p is None:
            continue
        R[r], R[p] = R[p], R[r]
        inv = 1 / R[r][c]
        R[r] = [v * inv for v in R[r]]
        for i in range(m):
            if i != r and R[i][c] != 0:
                f = R[i][c]
                R[i] = [a - f * b for a, b in zip(R[i], R[r])]
        piv.append(c); r += 1
        if r == m:
            break
    return R, piv


def nullspace(A, ncol):
    if not A:
        return [[Fr(int(i == j)) for i in range(ncol)] for j in range(ncol)]
    R, piv = rref(A)
    free = [c for c in range(ncol) if c not in piv]
    basis = []
    for f in free:
        v = [Fr(0)] * ncol; v[f] = Fr(1)
        for i, pc in enumerate(piv):
            v[pc] = -R[i][f]
        basis.append(v)
    return basis


def rank(A):
    return len(rref(A)[1]) if A else 0


# ------------------------------------------------------------------ Chebyshev jets at rational points
def cheb_vals(t, D):
    """T_k(t), T_k'(t), T_k''(t) for k = 0..D (exact; recurrences)."""
    T = [Fr(1), t]; dT = [Fr(0), Fr(1)]; ddT = [Fr(0), Fr(0)]
    for k in range(1, D):
        T.append(2 * t * T[k] - T[k - 1])
        dT.append(2 * T[k] + 2 * t * dT[k] - dT[k - 1])
        ddT.append(4 * dT[k] + 2 * t * ddT[k] - ddT[k - 1])
    return T[:D + 1], dT[:D + 1], ddT[:D + 1]


def nodes_equi(n):
    return [(Fr(-1) + Fr(2 * i, n), Fr(-1) + Fr(2 * j, n + 1)) for i in range(n + 1) for j in range(n + 2) if (i + j) % 2 == 0]


# ------------------------------------------------------------------ barrier proposer (own, mpmath)
def maximise_min_eig(blocks0, blocksL, norm_row, dps, tmax_exp, verbose=False):
    """Blocks B_i(theta) = blocks0[i] + sum_l theta_l blocksL[i][l], blocks as (a, b, d) mp tuples.
    Constraint: norm_row . theta = 1 - norm0 is eliminated beforehand by the caller (here we take the
    form theta = theta_p + W z). Maximises s subject to B_i - s I > 0 by a log-barrier method.
    Returns (theta, s)."""
    raise NotImplementedError


class Barrier:
    def __init__(self, base, lin, dps):
        """base[i] = (a, b, d) at z = 0; lin[i] = list over z-coordinates of (da, db, dd)."""
        mp.mp.dps = dps
        self.base = base; self.lin = lin
        self.M = len(base); self.r = len(lin[0]) if lin else 0

    def blocks(self, z, s):
        out = []
        for i in range(self.M):
            a, b, d = self.base[i]
            for l, zl in enumerate(z):
                if zl:
                    da, db, dd = self.lin[i][l]
                    a += zl * da; b += zl * db; d += zl * dd
            out.append((a - s, b, d - s))
        return out

    @staticmethod
    def feasible(bl):
        return all(a > 0 and a * d - b * b > 0 for (a, b, d) in bl)

    def phi(self, bl):
        return -mp.fsum(mp.log(a * d - b * b) for (a, b, d) in bl)

    def newton_step(self, z, s, t):
        r = self.r
        bl = self.blocks(z, s)
        g = mp.matrix(r + 1, 1); H = mp.matrix(r + 1, r + 1)
        g[r] = -t
        for i, (a, b, d) in enumerate(bl):
            Dt = a * d - b * b
            # gradient of -log det wrt (a, b, d)
            ga, gb, gd = -d / Dt, 2 * b / Dt, -a / Dt
            # Hessian of -log det wrt (a, b, d)
            Haa, Hab, Had = d * d / Dt ** 2, -2 * b * d / Dt ** 2, b * b / Dt ** 2
            Hbb, Hbd, Hdd = 2 * (a * d + b * b) / Dt ** 2, -2 * a * b / Dt ** 2, a * a / Dt ** 2
            # Jacobian of (a, b, d) wrt (z_1..z_r, s): columns lin[i][l], and (-1, 0, -1) for s
            cols = list(self.lin[i]) + [(mp.mpf(-1), mp.mpf(0), mp.mpf(-1))]
            v = []
            for (ja, jb, jd) in cols:
                v.append((Haa * ja + Hab * jb + Had * jd, Hab * ja + Hbb * jb + Hbd * jd, Had * ja + Hbd * jb + Hdd * jd))
            for p_, (ja, jb, jd) in enumerate(cols):
                g[p_] += ga * ja + gb * jb + gd * jd
                for q_ in range(p_, r + 1):
                    ka, kb, kd = cols[q_]
                    val = v[p_][0] * ka + v[p_][1] * kb + v[p_][2] * kd
                    H[p_, q_] += val
        for p_ in range(r + 1):
            for q_ in range(p_):
                H[p_, q_] = H[q_, p_]
        dx = mp.lu_solve(H, -g)
        lam2 = -mp.fsum(g[i] * dx[i] for i in range(r + 1))
        return dx, lam2, bl

    def run(self, z0, s0, tmax_exp=40, stop_when_positive=False, log=None, tmin=1):
        z = list(z0); s = s0; t = mp.mpf(tmin)
        m = 2 * self.M
        while True:
            for it in range(80):
                dx, lam2, bl = self.newton_step(z, s, t)
                if lam2 / 2 < mp.mpf(10) ** (-(mp.mp.dps // 2)):
                    break
                f0 = -t * s + self.phi(bl)
                step = mp.mpf(1)
                while True:
                    zn = [z[i] + step * dx[i] for i in range(self.r)]; sn = s + step * dx[self.r]
                    bn = self.blocks(zn, sn)
                    if self.feasible(bn) and (-t * sn + self.phi(bn)) <= f0 - step * lam2 / 4:
                        break
                    step /= 2
                    if step < mp.mpf(10) ** (-30):
                        break
                z, s = zn, sn
            if log:
                log(f"      barrier t=1e{int(mp.log10(t))}: s = {mp.nstr(s, 8)} (gap bound {mp.nstr(m / t, 3)})")
            if stop_when_positive and s > m / t:
                return z, s
            if m / t < abs(s) * mp.mpf(10) ** (-6) or t > mp.mpf(10) ** tmax_exp:
                return z, s
            t *= 100


def frac_of(x, den_exp):
    D = 10 ** den_exp
    return Fr(int(mp.nint(x * D)), D)


def nodes_randrat(n, seed):
    import random
    rnd = random.Random(seed)
    N = (n + 1) * (n + 2) // 2
    return [(Fr(rnd.randint(-1000, 1000), 1000), Fr(rnd.randint(-1000, 1000), 1000)) for _ in range(N)]


def run_n(n, dps, log, family='equi', seed=0):
    t0 = time.time()
    nodes = nodes_equi(n) if family == 'equi' else nodes_randrat(n, seed); M = len(nodes); Dg = 2 * n + 1
    E = [(a, b) for k in range(Dg + 1) for b in range(k + 1) for a in [k - b]]   # T_a(x) T_b(y), a + b <= 2n+1
    jets = []
    for (x, y) in nodes:
        Tx, dTx, ddTx = cheb_vals(x, Dg); Ty, dTy, ddTy = cheb_vals(y, Dg)
        jets.append((Tx, dTx, ddTx, Ty, dTy, ddTy))
    J = []
    for (Tx, dTx, ddTx, Ty, dTy, ddTy) in jets:
        J.append([Tx[a] * Ty[b] for (a, b) in E])
        J.append([dTx[a] * Ty[b] for (a, b) in E])
        J.append([Tx[a] * dTy[b] for (a, b) in E])
    rkJ = rank(J)
    S1 = nullspace(J, len(E)); K = len(S1)
    # Hessians of basis elements at nodes: (pxx, pxy, pyy)
    Hs = []
    for (Tx, dTx, ddTx, Ty, dTy, ddTy) in jets:
        row = []
        for s in S1:
            pxx = sum(c * ddTx[a] * Ty[b] for c, (a, b) in zip(s, E) if c)
            pxy = sum(c * dTx[a] * dTy[b] for c, (a, b) in zip(s, E) if c)
            pyy = sum(c * Tx[a] * ddTy[b] for c, (a, b) in zip(s, E) if c)
            row.append((pxx, pxy, pyy))
        Hs.append(row)
    Hmap = [[Hs[i][k][q] for k in range(K)] for i in range(M) for q in range(3)]
    rkH = rank(Hmap)
    log(f"{family}{'' if family == 'equi' else ' seed=' + str(seed)} n={n}: M={M} dim Pi_2n+1={len(E)} rank J={rkJ} (3M={3*M}) dim S1={K} (expected {n*(n+1)//2}) "
        f"rank Hess|S1={rkH} (injective {rkH == K})  [{time.time()-t0:.1f}s exact setup]")
    # ---- DUAL: v = (a_i, b_i, d_i)_i with sum_i a_i pxx + 2 b_i pxy + d_i pyy = 0 for all basis p
    G = [[x for i in range(M) for x in (Hs[i][k][0], 2 * Hs[i][k][1], Hs[i][k][2])] for k in range(K)]
    V = nullspace(G, 3 * M); r = len(V)
    # normalisation sum tr = 1: tr(v) = sum a_i + d_i ; coordinates theta in V; pick theta_p, W
    trV = [sum(v[3 * i] + v[3 * i + 2] for i in range(M)) for v in V]
    l0 = next(l for l in range(r) if trV[l] != 0)
    # theta = e_l0 / trV[l0] + sum_{l != l0} z_l (e_l - trV[l]/trV[l0] e_l0)
    mp.mp.dps = dps
    mpf = lambda q: mp.mpf(q.numerator) / q.denominator
    Vm = [[mpf(x) for x in v] for v in V]
    def vec_from_theta(theta):
        return [mp.fsum(theta[l] * Vm[l][c] for l in range(r)) for c in range(3 * M)]
    base_theta = [mp.mpf(0)] * r; base_theta[l0] = 1 / mpf(trV[l0])
    Wcols = []
    for l in range(r):
        if l == l0:
            continue
        w = [mp.mpf(0)] * r; w[l] = mp.mpf(1); w[l0] = -mpf(trV[l]) / mpf(trV[l0])
        Wcols.append(w)
    bv = vec_from_theta(base_theta)
    base = [(bv[3 * i], bv[3 * i + 1], bv[3 * i + 2]) for i in range(M)]
    lin = [[None] * len(Wcols) for _ in range(M)]
    for l, w in enumerate(Wcols):
        wv = vec_from_theta(w)
        for i in range(M):
            lin[i][l] = (wv[3 * i], wv[3 * i + 1], wv[3 * i + 2])
    bar = Barrier(base, lin, dps)
    z0 = [mp.mpf(0)] * len(Wcols)
    bl0 = bar.blocks(z0, 0)
    s0 = min((a + d) / 2 - mp.sqrt(((a - d) / 2) ** 2 + b * b) for (a, b, d) in bl0) - 1
    z, s = bar.run(z0, s0, tmax_exp=dps - 10, log=log)
    log(f"   DUAL high-precision optimum t_D = {mp.nstr(s, 10)}  (normalisation sum tr A_i = 1)  [{time.time()-t0:.1f}s]")
    verdict = 'UNRESOLVED'
    if s > 0:
        theta = [base_theta[l] for l in range(r)]
        for jz, w in enumerate(Wcols):
            for l in range(r):
                theta[l] += z[jz] * w[l]
        thq = [frac_of(th, dps - 5) for th in theta]
        v = [sum(thq[l] * V[l][c] for l in range(r) if thq[l]) for c in range(3 * M)]
        assert all(sum(G[k][c] * v[c] for c in range(3 * M)) == 0 for k in range(K))   # exact annihilation
        ok = all(v[3 * i] > 0 and v[3 * i] * v[3 * i + 2] - v[3 * i + 1] ** 2 > 0 for i in range(M))
        if ok and rkH == K:
            trs = sum(v[3 * i] + v[3 * i + 2] for i in range(M))
            marg = min((v[3 * i] * v[3 * i + 2] - v[3 * i + 1] ** 2) / (v[3 * i] + v[3 * i + 2]) for i in range(M)) / trs
            verdict = '(H) CERTIFIED'
            log(f"   DUAL exact check PASS: G v = 0 exactly, all {M} blocks PD exactly; exact min det/tr (normalised) = {float(marg):.4e} => {verdict}")
        else:
            log(f"   DUAL exact check FAILED (ok={ok}, injective={rkH == K})")
    if s <= 0:
        # ---- PRIMAL: p = sum theta_k S1_k, maximise min eig of Hess p(z_i), sum tr = 1
        trS = [sum(Hs[i][k][0] + Hs[i][k][2] for i in range(M)) for k in range(K)]
        k0 = next(k for k in range(K) if trS[k] != 0)
        baseP = [mp.mpf(0)] * K; baseP[k0] = 1 / mpf(trS[k0])
        Wp = []
        for k in range(K):
            if k == k0:
                continue
            w = [mp.mpf(0)] * K; w[k] = mp.mpf(1); w[k0] = -mpf(trS[k]) / mpf(trS[k0]); Wp.append(w)
        Hm = [[tuple(mpf(q) for q in Hs[i][k]) for k in range(K)] for i in range(M)]
        def blk(theta, i):
            return tuple(mp.fsum(theta[k] * Hm[i][k][q] for k in range(K)) for q in range(3))
        baseB = [blk(baseP, i) for i in range(M)]
        linB = [[blk(w, i) for w in Wp] for i in range(M)]
        barP = Barrier(baseB, linB, dps)
        zp0 = [mp.mpf(0)] * len(Wp)
        bl0 = barP.blocks(zp0, 0)
        sp0 = min((a + d) / 2 - mp.sqrt(((a - d) / 2) ** 2 + b * b) for (a, b, d) in bl0) - 1
        zp, sp_ = barP.run(zp0, sp0, tmax_exp=dps - 10, log=log)
        log(f"   PRIMAL high-precision optimum lambda_P = {mp.nstr(sp_, 10)}  (normalisation sum tr Hess p(z_i) = 1)")
        if sp_ > 0:
            theta = list(baseP)
            for jz, w in enumerate(Wp):
                for k in range(K):
                    theta[k] += zp[jz] * w[k]
            thq = [frac_of(th, dps - 5) for th in theta]
            ok = True
            for i in range(M):
                a = sum(thq[k] * Hs[i][k][0] for k in range(K)); b = sum(thq[k] * Hs[i][k][1] for k in range(K))
                d = sum(thq[k] * Hs[i][k][2] for k in range(K))
                ok &= (a > 0 and a * d - b * b > 0)
            if ok:
                verdict = 'ROBUST FAILURE OF (H) CERTIFIED (p in S_1 exactly, PD Hessians at all nodes)'
            log(f"   PRIMAL exact check {'PASS' if ok else 'FAILED'} => {verdict}")
    log(f"   verdict n={n}: {verdict}  [{time.time()-t0:.1f}s]")
    return verdict


def main():
    nmin, nmax = int(sys.argv[1]), int(sys.argv[2])
    dps = int(sys.argv[3]) if len(sys.argv) > 3 else 40
    log = lambda s_: print(s_, flush=True)
    log(f"equi_H_cert.py nmin={nmin} nmax={nmax} dps={dps} (mpmath {mp.__version__})")
    family = sys.argv[4] if len(sys.argv) > 4 else 'equi'
    seeds = [int(s_) for s_ in sys.argv[5].split(',')] if len(sys.argv) > 5 else [0]
    for n in range(nmin, nmax + 1):
        for sd in (seeds if family != 'equi' else [0]):
            run_n(n, dps, log, family, sd)


if __name__ == '__main__':
    main()
