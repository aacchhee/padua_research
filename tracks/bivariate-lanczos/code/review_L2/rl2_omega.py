"""L2 reconstruction 01, item 4: independent ω-estimate (E1 random median of 5, E1D sign-matched) for the plain
BJ run, and an independent PRO-2D-J (two-pass window + sign-matched estimate on F-steps, exact J-rows, trigger
sqrt(u), index set u^(3/4), next column forced).  Own code (rl2_lib, rl2_thmA); model as described in
directions/L2/candidates.md IDEA?...-201/-209.  MEASURED.  Usage: python3 -I rl2_omega.py > logs_L2/omega.log"""
import sys, os, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import rl2_lib as R
import rl2_thmA as TA

U = R.U
SQRTU = np.sqrt(U)
U34 = U ** 0.75
LD = R.LD


def alt_weights(h):
    lw = np.array([-np.sum(np.log(np.abs(h[i] - np.delete(h, i)))) for i in range(len(h))])
    w = np.exp(lw - lw.max()); return w / w.sum()


def checkerboard_cubic(m=30):
    s1, s2 = np.linspace(-1, 1, m + 1), np.linspace(-1, 1, m + 2)
    X, Y = s1 * np.abs(s1) ** 2, s2 * np.abs(s2) ** 2
    wx, wy = alt_weights(X), alt_weights(Y)
    pts, w = [], []
    for i in range(len(X)):
        for j in range(len(Y)):
            if (i + j) % 2 == 0:
                pts.append((X[i], Y[j])); w.append(wx[i] * wy[j])
    w = np.array(w)
    return np.array(pts), w / w.sum()


class Omega:
    """dense online ω-estimate for the BJ recurrence (block window)"""

    def __init__(self, nmax, mode='sign', seed=0):
        self.N = N = R.Nof(nmax)
        self.om = np.zeros((N, N))
        self.TF = np.zeros((N, N)); self.HJ = np.zeros((N, N))
        self.TFn = np.zeros(N); self.HJn = np.zeros(N)
        self.rec = [None] * N
        self.mode = mode
        self.rng = np.random.default_rng(seed)
        self.deg = R.degrees(N)

    def eps(self, base):
        if self.mode == 'rand':
            return self.rng.standard_normal(len(base))
        s = np.sign(base); s[s == 0] = 1.0
        return s

    def row(self, k, op, p, W, h, beta, consume=True):
        st = None if consume else self.rng.bit_generator.state
        out = np.zeros(k)
        lo = W[0] if len(W) else k
        nrm = np.sqrt(h @ h + beta * beta)
        T, Tn = (self.TF, self.TFn) if op == 'Y' else (self.HJ, self.HJn)
        if lo > 0:
            base = T[:p, :lo].T @ self.om[:p, p] - self.om[:lo][:, W] @ h
            out[:lo] = (base + self.eps(base) * U * (nrm + Tn[:lo])) / beta
        if len(W):
            OW = self.om[np.ix_(W, W)]
            OW = np.triu(OW, 1); OW = OW + OW.T
            base = -(OW @ h)
            out[W] = (base + self.eps(base) * U * nrm) / beta
        if st is not None:
            self.rng.bit_generator.state = st
        return out

    def commit(self, k, op, p, S, c, beta, rowvals):
        col = np.zeros(self.N); col[S] = c; col[k] = beta
        if op == 'Y':
            self.TF[:, p] = col; self.TFn[p] = np.linalg.norm(col)
        else:
            self.HJ[:, p] = col; self.HJn[p] = np.linalg.norm(col)
        self.om[:k, k] = rowvals
        self.rec[k] = (op, p, np.asarray(S), np.asarray(c), beta)
        t = self.deg[k]
        if k == R.Nof(t) - 1 and t >= 1:              # degree t complete: implicit H_J columns of degree t-1
            s = t - 1
            for j in range(1, s + 1):
                m = R.start_of(s) + j
                opm, pm, Sm, cm, bm = self.rec[m]
                Ns = R.Nof(s)
                v = self.TF[:, :Ns] @ self.HJ[:Ns, pm] - self.HJ[:, Sm] @ cm
                self.HJ[:, m] = v / bm; self.HJn[m] = np.linalg.norm(v / bm)

    def by_degree(self, nmax):
        A = np.abs(np.triu(self.om, 1)).max(axis=0)
        return np.array([max(U, A[:R.Nof(n)].max()) for n in range(nmax + 1)])


def replay(recs, nmax, mode, seed=0):
    est = Omega(nmax, mode, seed)
    for k in range(1, R.Nof(nmax)):
        op, p, S, c, beta = recs[k]
        rowv = est.row(k, op, p, S, c, beta)
        est.commit(k, op, p, S, c, beta, rowv)
    return est.by_degree(nmax)


def loss_by_degree(Q, nmax):
    G = Q.astype(LD).T @ Q.astype(LD) - np.eye(Q.shape[1], dtype=LD)
    A = np.abs(G).astype(np.float64)
    return np.array([A[:R.Nof(n), :R.Nof(n)].max() for n in range(nmax + 1)])


def verdict(L, E):
    D = [n for n in range(len(L)) if L[n] >= 1e3 * U or E[n] >= 1e3 * U]
    if not D:
        return None, None, D
    return max(L[n] / E[n] for n in D), max(E[n] / L[n] for n in D), D


def pro2dj(x, y, w, nmax):
    """independent PRO-2D-J"""
    N = R.Nof(nmax); M = len(x)
    Q = np.zeros((M, N)); v = np.sqrt(w); Q[:, 0] = v / np.linalg.norm(v)
    est = Omega(nmax, 'sign')
    recs = [None] * N
    force = False
    stats = dict(reorth_cols=0, dots_window=0, dots_reorth=0, dots_measure=0)
    for t in range(1, nmax + 1):
        for j in range(t + 1):
            k = R.start_of(t) + j
            op, pj = R.parent('bj', t, j)
            p = R.start_of(t - 1) + pj
            a = (x if op == 'X' else y) * Q[:, p]
            W = np.arange(R.start_of(max(t - 2, 0)), k)
            QW = Q[:, W]
            h = QW.T @ a; r = a - QW @ h
            h2 = QW.T @ r; r = r - QW @ h2; h = h + h2
            stats['dots_window'] += 2 * len(W)
            S, c = W, h
            lo = W[0]
            if lo > 0:
                b0 = np.linalg.norm(r)
                if op == 'X':
                    rowO = Q[:, :lo].T @ (r / b0); stats['dots_measure'] += lo
                else:
                    rowO = est.row(k, op, p, W, h, b0, consume=False)[:lo]
                trig = np.abs(rowO).max() > SQRTU
                sel = np.nonzero(np.abs(rowO) > U34)[0]
                if (trig or force) and len(sel):
                    QL = Q[:, sel]
                    g = QL.T @ r; r = r - QL @ g; g2 = QL.T @ r; r = r - QL @ g2; g = g + g2
                    h3 = QW.T @ r; r = r - QW @ h3; h = h + h3
                    stats['reorth_cols'] += 1; stats['dots_reorth'] += 2 * len(sel) + len(W)
                    S = np.concatenate([sel, W]); c = np.concatenate([g, h])
                    force = trig
                else:
                    force = False
            beta = np.linalg.norm(r)
            Q[:, k] = r / beta
            recs[k] = (op, p, S, c, beta)
            if op == 'X':
                rowv = Q[:, :k].T @ Q[:, k]; stats['dots_measure'] += k
            else:
                rowv = est.row(k, op, p, W, h, beta)
                if len(S) > len(W):
                    rowv[S[:len(S) - len(W)]] = U * est.rng.standard_normal(len(S) - len(W))
                    rowv[W] = U * est.rng.standard_normal(len(W))
            est.commit(k, op, p, S, c, beta, rowv)
    return Q, recs, stats


def main():
    print(f"# rl2_omega.py numpy={np.__version__}", flush=True)
    sq, dk, tr = R.rng11_sets()
    sets = [('rotpi4', R.rotate(sq, np.pi / 4), np.ones(1681), 24), ('triangle', tr, np.ones(1681), 20)]
    Pc, wc = checkerboard_cubic(30)
    sets.append(('cb_cubic', Pc, wc, 29))
    for name, P, w, nmax in sets:
        t0 = time.time()
        x, y = P[:, 0].copy(), P[:, 1].copy()
        Q, recs = R.recur(x, y, w, nmax, rule='bj', orth='cgs1win', record=True)
        L = loss_by_degree(Q, nmax)
        E1 = np.median(np.array([replay(recs, nmax, 'rand', s) for s in range(5)]), axis=0)
        E1D = replay(recs, nmax, 'sign')
        ns = [n for n in range(4, nmax + 1, 2)] + ([nmax] if nmax % 2 else [])
        print(f"== {name}: M={len(x)} nmax={nmax}", flush=True)
        print("   n   : " + " ".join(f"{n:8d}" for n in ns))
        print("   L   : " + " ".join(f"{L[n]:8.1e}" for n in ns))
        print("   E1  : " + " ".join(f"{E1[n]:8.1e}" for n in ns))
        print("   E1D : " + " ".join(f"{E1D[n]:8.1e}" for n in ns))
        for nm, E in (('E1', E1), ('E1D', E1D)):
            Uf, Of, D = verdict(L, E)
            print(f"   verdict {nm}: U = max L/E = {Uf:.3g}, O = max E/L = {Of:.3g} over D = [{min(D)}, {max(D)}] "
                  f"-> {'KILL' if Uf > 10 else 'not killed'}", flush=True)
            print('JSON ' + json.dumps(dict(set=name, est=nm, U=Uf, O=Of, L=L.tolist(), E=E.tolist())), flush=True)
        # PRO-2D-J
        Qp, recp, st = pro2dj(x, y, w, nmax)
        Lp = loss_by_degree(Qp, nmax)
        full = R.Nof(nmax) * (R.Nof(nmax) - 1)
        eF = {}
        for n in sorted(set(list(range(4, nmax + 1, 4)) + [nmax])):
            if Lp[n] <= SQRTU:
                r = TA.theorem_A(Qp, recp, x, y, n)
                eF[n] = r.get('lhs')
        killL = [n for n in range(nmax + 1) if Lp[n] > 10 * SQRTU]
        killF = [n for n, v in eF.items() if v is not None and v > U34]
        print(f"   PRO-2D-J (own): max L = {Lp.max():.1e} (L(nmax) = {Lp[nmax]:.1e}); e_F at SO degrees: " +
              " ".join(f"{n}:{v:.1e}" for n, v in eF.items()) +
              f"; kill L>10sqrt(u): {killL}; kill eF: {killF}; reorth columns {st['reorth_cols']}; "
              f"(window+reorth+measure)/fullcgs2 = {(st['dots_window'] + st['dots_reorth'] + st['dots_measure']) / full:.2f}"
              f"; (reorth+measure)/fullcgs2 = {(st['dots_reorth'] + st['dots_measure']) / full:.2f} "
              f"({time.time() - t0:.0f}s)", flush=True)
        print('JSON ' + json.dumps(dict(set=name, pro2dj_L=Lp.tolist(), eF=eF, stats={k_: int(v_) for k_, v_ in st.items()},
                                         full=full)), flush=True)


if __name__ == '__main__':
    main()
