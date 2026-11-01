"""L2 reconstruction 01, item 1: numerical stress test of Theorem A of PD-T?bivariate-lanczos-claude-201,
  max|S - T| <= 2 eps_c + 2(mu1 + eta^2) tau1 + eta*gamma + 2 eta^2 (||T|| + ||G||)/(1 - eta) + 4 eps,
with every quantity evaluated in x87 long double from the computed data (own Cholesky, own triangular solves).
Since (H1) only *defines* f_k, the theorem must hold for any full-rank Q-hat and any coefficients: we also run the
recurrence in float32 and with injected structured perturbations (counterexample search).
Usage: python3 -I rl2_thmA.py > logs_L2/thmA.log"""
import sys, os, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import rl2_lib as R

LD = R.LD


def chol_ld(A):
    A = np.array(A, dtype=LD)
    n = A.shape[0]
    Lm = np.zeros_like(A)
    for j in range(n):
        s = A[j, j] - Lm[j, :j] @ Lm[j, :j]
        if s <= 0:
            raise np.linalg.LinAlgError('not PD')
        Lm[j, j] = np.sqrt(s)
        Lm[j + 1:, j] = (A[j + 1:, j] - Lm[j + 1:, :j] @ Lm[j, :j]) / Lm[j, j]
    return Lm            # lower, A = L L^T  (R = L^T)


def fsub(Lm, B):
    """solve Lm Z = B, Lm lower triangular"""
    Z = np.zeros_like(B)
    for i in range(Lm.shape[0]):
        Z[i] = (B[i] - Lm[i, :i] @ Z[:i]) / Lm[i, i]
    return Z


def recur_inject(x, y, w, nmax, orth, dtype, inject=None, seed=0):
    """BJ recurrence (own code), optional injections:
       ('coef', s): subtract the window coefficients h but RECORD h - z, z ~ s*N(0,1) on the window, and add Q_W z
                    to r (so f_k stays at rounding level while local orthogonality and coefficient consistency fail)
       ('vec', s) : add s*N(0,1)/sqrt(M) to r before normalisation (an out-of-span local error f_k)"""
    rng = np.random.default_rng(seed)
    N = R.Nof(nmax)
    x = np.asarray(x, dtype=dtype); y = np.asarray(y, dtype=dtype)
    M = len(x)
    Q = np.zeros((M, N), dtype=dtype)
    v = np.sqrt(np.asarray(w, dtype=dtype)); Q[:, 0] = v / np.sqrt(v @ v)
    recs = [None] * N
    for t in range(1, nmax + 1):
        for j in range(t + 1):
            k = R.start_of(t) + j
            op, pj = R.parent('bj', t, j)
            p = R.start_of(t - 1) + pj
            a = (x if op == 'X' else y) * Q[:, p]
            S = np.arange(k) if orth == 'cgs2all' else np.arange(R.start_of(max(t - 2, 0)), k)
            QS = Q[:, S]
            c = QS.T @ a; r = a - QS @ c
            if orth in ('cgs2all', 'cgs2win'):
                c2 = QS.T @ r; r = r - QS @ c2; c = c + c2
            if inject is not None:
                kind, s = inject
                if kind == 'coef':
                    Wl = np.arange(R.start_of(max(t - 2, 0)), k)
                    z = (s * rng.standard_normal(len(Wl)) * np.sqrt(r @ r)).astype(dtype)
                    r = r + Q[:, Wl] @ z
                    pos = np.searchsorted(S, Wl)
                    c = c.copy(); c[pos] -= z
                elif kind == 'vec':
                    r = r + (s * np.sqrt(r @ r) / np.sqrt(M) * rng.standard_normal(M)).astype(dtype)
            beta = np.sqrt(r @ r)
            Q[:, k] = r / beta
            recs[k] = (op, p, S, c, beta)
    return Q, recs


def theorem_A(Q, recs, x, y, n):
    """evaluate both sides of Theorem A at degree n for the F = Y section of the BJ run"""
    N, Nc = R.Nof(n), R.Nof(n - 1)
    deg = R.degrees(N)
    Ql = Q[:, :N].astype(LD)
    F = np.asarray(y, dtype=LD)
    T = np.zeros((N, Nc), dtype=LD); G = np.zeros((N, Nc), dtype=LD)
    epsc = LD(0)
    for k in range(1, N):
        op, p, S, c, beta = recs[k]
        if op != 'Y':
            continue
        Wk = S[deg[S] >= deg[k] - 2]
        Lk = S[deg[S] < deg[k] - 2]
        cS = np.asarray(c, dtype=LD)
        h = cS[np.isin(S, Wk)]; g = cS[np.isin(S, Lk)]
        T[Wk, p] = h; T[k, p] = LD(beta)
        if len(Lk):
            G[Lk, p] = g
        Fq = F * Ql[:, p]
        cons = np.abs(h - Ql[:, Wk].T @ Fq).max() if len(Wk) else LD(0)
        cons = max(cons, abs(LD(beta) - Ql[:, k] @ Fq))
        epsc = max(epsc, cons)
    E = F[:, None] * Ql[:, :Nc] - Ql @ (T + G)
    eps = float(np.linalg.norm(E.astype(np.float64), 2))
    Om = Ql.T @ Ql - np.eye(N, dtype=LD)
    eta = float(np.sqrt(np.sum(Om * Om)))
    loc = (np.abs(deg[:, None] - deg[None, :]) <= 2) & ~np.eye(N, dtype=bool)
    mu = float(np.abs(Om[loc]).max()) if loc.any() else 0.0
    mud = float(np.abs(np.diag(Om)).max())
    mu1 = max(mu, mud / 2)
    Tf, Gf = T.astype(np.float64), G.astype(np.float64)
    tau1 = float(max(np.abs(Tf).sum(axis=0).max(), np.abs(Tf).sum(axis=1).max()))
    gam = float(np.sqrt((Gf ** 2).sum(axis=0)).max())
    nT, nG = float(np.linalg.norm(Tf, 2)), float(np.linalg.norm(Gf, 2))
    rec = dict(n=n, eta=eta, mu=mu, mud=mud, epsc=float(epsc), eps=eps, tau1=tau1, gamma=gam, nT=nT, nG=nG,
               loss=float(np.abs(Om).max()))
    if eta > 0.25:
        rec['skip'] = 'eta > 1/4'
        return rec
    Lc = chol_ld(np.eye(N, dtype=LD) + Om)       # R = Lc^T
    A = Ql.T @ (F[:, None] * Ql[:, :Nc])
    Z = fsub(Lc, A)                               # R^-T A
    Sm = fsub(Lc[:Nc, :Nc], Z.T).T                # (R'^-T Z^T)^T = Z R'^-1
    lhs = float(np.abs(Sm - T).max())
    terms = dict(t_epsc=2 * float(epsc), t_loc=2 * (mu1 + eta ** 2) * tau1, t_gam=eta * gam,
                 t_rho=2 * eta ** 2 * (nT + nG) / (1 - eta), t_eps=4 * eps)
    rhs = sum(terms.values())
    rec.update(lhs=lhs, rhs=rhs, ratio=lhs / rhs, **terms)
    return rec


def main():
    print(f"# rl2_thmA.py numpy={np.__version__}; all quantities in long double", flush=True)
    sq, dk, tr = R.rng11_sets()
    sets = dict(rotpi4=R.rotate(sq, np.pi / 4), triangle=tr, rot03=R.rotate(sq, 0.3))
    cases = [
        ('triangle', 'cgs1win', np.float64, None, [6, 8, 10, 12]),
        ('triangle', 'cgs2win', np.float64, None, [8, 12, 16]),
        ('rot03', 'cgs1win', np.float64, None, [16, 20, 24]),
        ('rotpi4', 'cgs1win', np.float64, None, [16, 20, 22]),
        ('rotpi4', 'cgs2all', np.float64, None, [16, 24]),
        ('rotpi4', 'cgs1win', np.float32, None, [4, 6, 8, 10, 12]),
        ('triangle', 'cgs1win', np.float32, None, [4, 6, 8]),
        ('rotpi4', 'cgs2win', np.float64, ('coef', 1e-6), [4, 8, 12]),
        ('rotpi4', 'cgs2win', np.float64, ('coef', 1e-3), [4, 8]),
        ('triangle', 'cgs1win', np.float64, ('coef', 1e-8), [4, 8, 10]),
        ('rotpi4', 'cgs2win', np.float64, ('vec', 1e-8), [4, 8, 12]),
        ('rotpi4', 'cgs2all', np.float64, ('vec', 1e-5), [4, 8]),
    ]
    worst = 0.0
    for name, orth, dt, inj, ns in cases:
        P = sets[name]
        x, y = P[:, 0].copy(), P[:, 1].copy()
        w = np.ones(len(x))
        t0 = time.time()
        Q, recs = recur_inject(x, y, w, max(ns), orth, dt, inject=inj)
        for n in ns:
            r = theorem_A(Q, recs, x, y, n)
            r.update(set=name, orth=orth, dtype=np.dtype(dt).name, inject=str(inj))
            if 'skip' in r:
                print(f"  {name:8s} {orth:7s} {np.dtype(dt).name:7s} inj={str(inj):14s} n={n:2d}: loss={r['loss']:.1e} "
                      f"eta={r['eta']:.2e} -> skipped (eta > 1/4)", flush=True)
            else:
                worst = max(worst, r['ratio'])
                big = max(('t_epsc', 't_loc', 't_gam', 't_rho', 't_eps'), key=lambda kk: r[kk])
                print(f"  {name:8s} {orth:7s} {np.dtype(dt).name:7s} inj={str(inj):14s} n={n:2d}: loss={r['loss']:.1e} "
                      f"eta={r['eta']:.1e} mu={r['mu']:.1e} epsc={r['epsc']:.1e} eps={r['eps']:.1e} | "
                      f"LHS={r['lhs']:.2e} RHS={r['rhs']:.2e} ratio={r['ratio']:.2e} (largest term {big})", flush=True)
            print('JSON ' + json.dumps(r), flush=True)
        print(f"    ({time.time() - t0:.0f}s)", flush=True)
    print(f"# worst LHS/RHS = {worst:.3e} ({'NO violation' if worst <= 1 else 'VIOLATION'})", flush=True)


if __name__ == '__main__':
    main()
