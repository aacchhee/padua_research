"""Response to Codex audit-01, finding L2-F2 (supplementary measurement, no kill rule): size of the near-breakdown /
normalisation factor chi of PD-T?bivariate-lanczos-claude-201 Corollary A' in the runs that PD-T?...-204/-207 report,
   chi_k := ||B_k q_{p(k)}||_2 / beta_k   (B_k in {X, Y} the operator of column k's relation, p(k) its parent),
   chi(n) := max over columns k = 1..N_n - 1 of chi_k,
together with the Frobenius loss eta(n) = ||Q_n^T Q_n - I||_F and the local level mu(n) (max |Omega_ab| over
a != b, |deg a - deg b| <= 2), all in double.  ||B_k q_p|| is the norm of the computed product a = fl(B q_p)
(l2_core.run stores it as a_norm); beta_k the computed normalisation.  Runs: BJ block window with a two-pass window
and no reorthogonalisation ('w2_none', as PD-T?...-204) and PRO-2D-J ('proJ', as PD-T?...-207).  MEASURED only.
Usage (from this directory):
    python3 -I l2_audit01_chi.py > ../../../../topics/bivariate-lanczos-20261031/directions/L2/logs/audit01_chi.raw
"""
import sys, os, json, time, platform
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import l2_core as C

U, SQRTU = C.U, C.SQRTU


def chi_profile(Q, coef, nmax):
    N = Q.shape[1]
    deg = C.degree_of(N)
    chik = np.zeros(N)
    for k in range(1, N):
        W, h, beta, Lset, g, opk, p, na = coef[k]
        chik[k] = na / beta
    G = Q.T @ Q
    Om = G - np.eye(N)
    A = np.abs(Om)
    loc = np.abs(deg[:, None] - deg[None, :]) <= 2
    out = []
    for n in range(nmax + 1):
        Nn = C.Nof(n)
        B = np.where(loc[:Nn, :Nn], A[:Nn, :Nn], 0.0); np.fill_diagonal(B, 0.0)
        out.append(dict(n=n, chi=float(chik[1:Nn].max()) if Nn > 1 else 0.0,
                        argmax=int(np.argmax(chik[:Nn])), eta=float(np.linalg.norm(Om[:Nn, :Nn])),
                        L=float(A[:Nn, :Nn].max()), mu=float(B.max())))
    return out, chik


def main(names):
    print(f"# l2_audit01_chi.py python={platform.python_version()} numpy={np.__version__} u=2^-53", flush=True)
    for name in names:
        t0 = time.time()
        P, w, nmax = C.benchmark(name)
        x, y = P[:, 0].copy(), P[:, 1].copy()
        for lab in ('w2_none', 'proJ'):
            if lab == 'w2_none':
                Q, coef, tab, st = C.run(x, y, w, nmax, orth='cgs2w', reorth='none')
            else:
                est = C.OmegaEst(nmax, mode='sign', jmeasure=True)
                Q, coef, tab, st = C.run(x, y, w, nmax, orth='cgs2w', reorth='est', est=est)
            prof, chik = chi_profile(Q, coef, nmax)
            so = [r for r in prof if r['L'] <= SQRTU]
            chi_so = max(r['chi'] for r in so) if so else float('nan')
            last_so = so[-1]['n'] if so else None
            r = prof[nmax]
            print(f"== {name} {lab}: M={len(x)} nmax={nmax}: chi(nmax)={r['chi']:.3e} (column {r['argmax']}); "
                  f"max chi over strictly SO degrees (L<=sqrt u, up to n={last_so}) = {chi_so:.3e}; "
                  f"u*chi(SO)={U * chi_so:.2e}; eta(nmax)={r['eta']:.2e} L(nmax)={r['L']:.2e} mu(nmax)={r['mu']:.2e}",
                  flush=True)
            print("   chi(n): " + " ".join(f"{q['n']}:{q['chi']:.2e}" for q in prof if q['n'] % 4 == 0 or q['n'] == nmax),
                  flush=True)
            print('JSON ' + json.dumps(dict(bench=name, run=lab, prof=prof, chik=chik.tolist())), flush=True)
        print(f"# {name} done in {time.time() - t0:.1f}s", flush=True)


if __name__ == '__main__':
    main(sys.argv[1:] if len(sys.argv) > 1 else C.BENCH)
