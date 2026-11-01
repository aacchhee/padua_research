"""R01 (a): online 2D omega-estimates vs measured loss on the L1 benchmark set (IDEA?bivariate-lanczos-claude-201,
-202; kill rule in directions/L2/candidates.md, written before this script was run), plus the one-step source
audit (long double).  Plain BJ run (block window, CGS); the estimators are replayed causally on its coefficients.
MEASURED only.  Usage: python3 -I l2_r01_omega.py [bench ...] > logs/r01_omega.log"""
import sys, os, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import l2_core as C

U = C.U
TAU = 1e3 * U


x_g = y_g = None


def replay(Q, coef, nmax, **kw):
    est = C.OmegaEst(nmax, **kw)
    for k in range(1, Q.shape[1]):
        W, h, beta, Lset, g, opk, p, na = coef[k]
        meas = Q[:, :k].T @ Q[:, k] if (kw.get('jmeasure') and opk == 'J') else None
        absw = None
        if kw.get('inscale') == 'abs' and len(W):
            a = (x_g if opk == 'J' else y_g) * Q[:, p]
            absw = np.abs(Q[:, W]).T @ np.abs(a)
        est.add(k, opk, p, W, h, beta, meas_row=meas, absw=absw)
    return est.by_degree()


def verdict(L, E):
    D = [n for n in range(len(L)) if L[n] >= TAU or E[n] >= TAU]
    if not D:
        return dict(D=[], U=None, O=None)
    Uf = max(L[n] / E[n] for n in D)
    Of = max(E[n] / L[n] for n in D)
    return dict(D=[min(D), max(D)], U=float(Uf), O=float(Of))


def source_audit(Q, coef, tab, x, y, nmax):
    """actual one-step sources (long double) vs the model scale; per step type: max and median of |s|/sigma."""
    LD = np.longdouble
    idx, pos, parent, op, start = tab
    N = Q.shape[1]
    Ql = Q.astype(LD)
    Om = Ql.T @ Ql
    TF = np.zeros((N, N), dtype=LD); HJ = np.zeros((N, N), dtype=LD)
    for k in range(1, N):
        W, h, beta, Lset, g, opk, p, na = coef[k]
        col = np.zeros(N, dtype=LD); col[W] = np.asarray(h, dtype=LD); col[k] = LD(beta)
        if opk == 'F': TF[:, p] = col
        else: HJ[:, p] = col
    for m in range(N):
        t, j = idx[m]
        if j == 0 or Nof(t + 1) > N:
            continue
        W, h, beta, Lset, g, opk, p, na = coef[m]
        Ns = Nof(t)
        HJ[:, m] = (TF[:, :Ns] @ HJ[:Ns, p] - HJ[:, W] @ np.asarray(h, dtype=LD)) / LD(beta)
    TFn = np.sqrt(np.sum(TF.astype(float) ** 2, axis=0)); HJn = np.sqrt(np.sum(HJ.astype(float) ** 2, axis=0))
    res = {}
    for k in range(1, N):
        t, j = idx[k]
        W, h, beta, Lset, g, opk, p, na = coef[k]
        hl = np.asarray(h, dtype=LD); bl = LD(beta)
        nrm = float(np.sqrt(h @ h + beta * beta))
        lo = W[0] if len(W) else k
        T = TF if opk == 'F' else HJ; Tn = TFn if opk == 'F' else HJn
        r = res.setdefault(t, {'F': [], 'J': [], 'in': []})
        if lo > 0:
            s = bl * Om[:lo, k] - T[:p, :lo].T @ Om[:p, p] + Om[:lo, W] @ hl
            sig = U * (nrm + Tn[:lo])
            r[opk].append(np.abs(s.astype(float)) / sig)
        if len(W):
            OW = Om[np.ix_(W, W)].copy(); np.fill_diagonal(OW, 0)
            s = bl * Om[W, k] + OW @ hl
            r['in'].append(np.abs(s.astype(float)) / (U * nrm))
    out = {}
    for t in sorted(res):
        d = {}
        for key in ('F', 'J', 'in'):
            if res[t][key]:
                v = np.concatenate(res[t][key])
                d[key] = (float(v.max()), float(np.median(v)))
        out[t] = d
    return out


def Nof(n):
    return (n + 1) * (n + 2) // 2


def main(names):
    print(f"# l2_r01_omega.py numpy={np.__version__} u=2^-53 tau=1e3u; benches={names}", flush=True)
    for name in names:
        t0 = time.time()
        P, w, nmax = C.benchmark(name)
        x, y = P[:, 0].copy(), P[:, 1].copy()
        Q, coef, tab, st = C.run(x, y, w, nmax)
        global x_g, y_g
        x_g, y_g = x, y
        L = C.loss_by_degree(Q, nmax)
        ests = {}
        if E3ONLY:
            ests['E3'] = np.median(np.array([replay(Q, coef, nmax, mode='rand', seed=s, inscale='abs')
                                             for s in range(5)]), axis=0)
            ests['E1'] = np.median(np.array([replay(Q, coef, nmax, mode='rand', seed=s) for s in range(5)]), axis=0)
            report(name, x, nmax, Q, L, ests)
            continue
        E1 = np.median(np.array([replay(Q, coef, nmax, mode='rand', seed=s) for s in range(5)]), axis=0)
        ests['E1'] = E1
        ests['E1D'] = replay(Q, coef, nmax, mode='sign')
        ests['E2'] = np.median(np.array([replay(Q, coef, nmax, mode='rand', seed=s, jmeasure=True)
                                         for s in range(5)]), axis=0)
        ests['E2D'] = replay(Q, coef, nmax, mode='sign', jmeasure=True)
        report(name, x, nmax, Q, L, ests)
        if Q.shape[1] <= 820:
            aud = source_audit(Q, coef, tab, x, y, nmax)
            for t in sorted(aud):
                if t % 4 == 0 or t == nmax:
                    d = aud[t]
                    print(f"   audit deg {t:2d}: " + "  ".join(f"{key}: max {d[key][0]:.1e} med {d[key][1]:.1e}"
                                                         for key in ('F', 'J', 'in') if key in d), flush=True)
        print(f"# {name} done in {time.time() - t0:.1f}s", flush=True)


def report(name, x, nmax, Q, L, ests):
    if True:
        print(f"== {name}: M={len(x)} nmax={nmax} N={Q.shape[1]}", flush=True)
        step = 2 if nmax <= 32 else 4
        ns = list(range(4, nmax + 1, step))
        if nmax not in ns: ns.append(nmax)
        print("   n    : " + " ".join(f"{n:8d}" for n in ns))
        print("   L(n) : " + " ".join(f"{L[n]:8.1e}" for n in ns))
        for key, E in ests.items():
            print(f"   {key:5s}: " + " ".join(f"{E[n]:8.1e}" for n in ns))
        for key, E in ests.items():
            v = verdict(L, E)
            kill = (v['U'] is not None and v['U'] > 10)
            us = 'None' if v['U'] is None else f"{v['U']:.3g}"
            os_ = 'None' if v['O'] is None else f"{v['O']:.2e}"
            print(f"   verdict {key}: D={v['D']} U(max L/E)={us} O(max E/L)={os_} -> {'KILL' if kill else 'ok'}",
                  flush=True)
            print('JSON ' + json.dumps(dict(bench=name, est=key, L=L.tolist(), E=E.tolist(), **v)), flush=True)


E3ONLY = False
if __name__ == '__main__':
    args = sys.argv[1:]
    if args and args[0] == '--e3':
        E3ONLY = True; args = args[1:]
    main(args if args else C.BENCH)
