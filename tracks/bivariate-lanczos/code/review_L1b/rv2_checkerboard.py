"""Independent rerun of the Harris-Simanek checkerboard claims of L1 R04/R06 (PD-T?...-111 numerics, -112 (a, b, d),
-114 part 5 / IDEA?...-117 table), written from the theory-file statements only (no developer code imported).
Uses the reconstructor's own recurrence code (review_L1/rv_core.py).

Checkerboard (PD-T?...-111 part 2): x_0 < ... < x_m, y_0 < ... < y_{m+1}; a_i = 1/|w_X'(x_i)|, b_j = 1/|w_Y'(y_j)|;
mu_e = sum_{i+j = e mod 2} a_i b_j delta_(x_i, y_j); here e = 0, m = 30 (M = 496).
Families: 'cubic' x_i = s_i^3 (s equispaced in [-1, 1]), 'equi' x_i = s_i, 'lobatto' x_i = -cos(pi i/m).
Usage: python3 -I -u rv2_checkerboard.py > logs_L1b/checkerboard.log
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'review_L1'))
import numpy as np
import rv_core as C

ld = np.longdouble


def abscissae(fam, npts):
    s = np.linspace(-1, 1, npts, dtype=ld)
    if fam == 'cubic':
        return s ** 3
    if fam == 'equi':
        return s
    if fam == 'lobatto':
        return -np.cos(np.pi * np.arange(npts, dtype=ld) / (npts - 1))
    raise ValueError(fam)


def inv_abs_wprime(x):
    n = len(x)
    out = np.empty(n, dtype=ld)
    for i in range(n):
        d = x[i] - np.delete(x, i)
        out[i] = 1 / np.prod(np.abs(d))
    return out


def checkerboard(fam, m, e=0):
    x = abscissae(fam, m + 1); y = abscissae(fam, m + 2)
    a = inv_abs_wprime(x); b = inv_abs_wprime(y)
    a = a / a.sum(); b = b / b.sum()
    P, w = [], []
    for i in range(m + 1):
        for j in range(m + 2):
            if (i + j) % 2 == e:
                P.append((x[i], y[j])); w.append(a[i] * b[j])
    P = np.array(P, dtype=ld); w = np.array(w, dtype=ld); w = w / w.sum()
    return P, w, (x, a), (y, b)


def jacobi(nodes, wts, nmax):
    """Jacobi coefficients (alpha_l, beta_{l+1}) of the probability measure, Lanczos with full double reorth in long double"""
    q = np.sqrt(wts); q = q / np.sqrt(q @ q)
    Q = [q]; al, be = [], [ld(0)]
    for l in range(nmax):
        v = nodes * Q[-1]
        al.append(Q[-1] @ v)
        for _ in range(2):
            for qq in Q:
                v = v - (qq @ v) * qq
        bb = np.sqrt(v @ v)
        be.append(bb); Q.append(v / bb)
    return np.array(al), np.array(be)     # x r_l = be[l+1] r_{l+1} + al[l] r_l + be[l] r_{l-1}


def univariate_lanczos_loss(nodes, wts, nsteps):
    """plain three-term Lanczos (no reorth) in double on diag(nodes) with start sqrt(w): loss after each step"""
    x = nodes.astype(float); q = np.sqrt(wts.astype(float)); q /= np.linalg.norm(q)
    Q = [q]; qprev = np.zeros_like(q); bprev = 0.0; out = []
    for l in range(nsteps):
        v = x * Q[-1] - bprev * qprev
        a = Q[-1] @ v; v = v - a * Q[-1]
        b = np.linalg.norm(v); qprev = Q[-1]; Q.append(v / b); bprev = b
        A = np.array(Q).T; out.append(float(np.max(np.abs(A.T @ A - np.eye(A.shape[1])))))
    return out


def on_pattern(k, l, idx):
    (t, j), (tl, jl) = idx[k], idx[l]
    if j == 0:
        return jl == 0 and tl in (t - 1, t - 2)
    return (tl, jl) in ((t - 1, j - 1), (t - 2, j - 2))


def product_coeffs(rec, idx, pos, ax, bx, ay, by):
    """c* in the recorded window layout: list of (h vector, beta)"""
    out = [None]
    for k in range(1, len(idx)):
        t, j = idx[k]
        op, p, W, h, beta = rec[k]
        hs = np.zeros(len(W), dtype=ld)
        for ii, l in enumerate(W):
            tl, jl = idx[l]
            if j == 0:
                if (tl, jl) == (t - 1, 0): hs[ii] = ax[t - 1]
                if (tl, jl) == (t - 2, 0): hs[ii] = bx[t - 1]
                bs = bx[t]
            else:
                if (tl, jl) == (t - 1, j - 1): hs[ii] = ay[j - 1]
                if (tl, jl) == (t - 2, j - 2): hs[ii] = by[j - 1]
                bs = by[j]
        out.append((hs, bs if j > 0 else bx[t]))
    return out


def xi_map(P, w, rec, coeffs, nmax):
    idx, pos = C.cols(nmax)
    x = P[:, 0].astype(ld); y = P[:, 1].astype(ld)
    Xi = np.zeros((len(x), len(idx)), dtype=ld)
    Xi[:, 0] = np.sqrt(w.astype(ld))
    for k in range(1, len(idx)):
        op, p, W, _, _ = rec[k]
        h, b = coeffs[k]
        a = x if op == 'X' else y
        Xi[:, k] = (a * Xi[:, p] - Xi[:, W] @ h.astype(ld)) / ld(b)
    return Xi


def gram_defect(Xi, n):
    Nn = C.N_of(n); G = Xi[:, :Nn].T @ Xi[:, :Nn]
    return float(np.max(np.abs(G - np.eye(Nn, dtype=ld))))


def main():
    m = 30; nmax = 24
    print(f'# rv2_checkerboard.py numpy {np.__version__}; Harris-Simanek checkerboards m={m}, e=0 (M = N_m = {C.N_of(m)})')
    degs = (8, 12, 16, 20, 24)
    for fam in ('lobatto', 'equi', 'cubic'):
        P, w, (xs, a), (ys, b) = checkerboard(fam, m)
        assert len(P) == C.N_of(m)
        x64, y64, w64 = P[:, 0].astype(float), P[:, 1].astype(float), w.astype(float)
        print(f'## {fam}: x-factor weights {float(a.min()):.1e}..{float(a.max()):.2f}; bivariate weights {float(w.min()):.1e}..{float(w.max()):.2f}')
        Q, rec = C.window_rec(x64, y64, w64, nmax, 'dev', 'block', 'cgs', record=True)
        L = C.loss_profile(Q, nmax)
        print('   BJ (dev, block, CGS) double loss n=8..24 step 4:  ' + ' '.join(f'{L[n]:.1e}' for n in degs))
        Qld, _ = C.window_rec(P[:, 0], P[:, 1], w, nmax, 'dev', 'block', 'cgs', dtype=ld)
        Lld = [gram_defect(Qld, n) for n in degs]
        print('   BJ long double loss:                              ' + ' '.join(f'{v:.1e}' for v in Lld))
        for ch in ('mirror', 'alt', 'adapt'):
            Qc, _ = C.window_rec(x64, y64, w64, nmax, ch, 'block', 'cgs'); Lc = C.loss_profile(Qc, nmax)
            print(f'   {ch:6s} rule double loss:                         ' + ' '.join(f'{Lc[n]:.1e}' for n in degs))
        Qt = C.two_relation(x64, y64, w64, nmax); Lt = C.loss_profile(Qt, nmax)
        print('   two-relation (1 CGS pass + SVD) loss:             ' + ' '.join(f'{Lt[n]:.1e}' for n in degs))
        ux = univariate_lanczos_loss(xs, a, m); uy = univariate_lanczos_loss(ys, b, m)
        print('   univariate Lanczos (no reorth) loss, x / y, steps 8..24: ' + ' '.join(f'{ux[n-1]:.0e}/{uy[n-1]:.0e}' for n in degs))
        # coefficient channel
        idx, pos = C.cols(nmax)
        ax, bx = jacobi(xs, a, m); ay, by = jacobi(ys, b, m + 1)
        cstar = product_coeffs(rec, idx, pos, ax, bx, ay, by)
        cbj = [None] + [(rec[k][3].astype(ld), ld(rec[k][4])) for k in range(1, len(idx))]
        on_only = [None]; mix = [None]; dev_on = 0.0; off_max = 0.0; cpl = 0.0
        for k in range(1, len(idx)):
            W = rec[k][2]
            mask = np.array([on_pattern(k, l, idx) for l in W], dtype=bool)
            hb, bb = cbj[k]; hs, bs = cstar[k]
            on_only.append((np.where(mask, hb, 0), bb))
            mix.append((np.where(mask, hs, hb), bs))
            if mask.any():
                dev_on = max(dev_on, float(np.max(np.abs((hb - hs)[mask]))))
            dev_on = max(dev_on, abs(float(bb - bs)))
            if (~mask).any():
                off_max = max(off_max, float(np.max(np.abs(hb[~mask]))))
        print(f'   max|c_BJ - c*| on pattern (incl. beta) = {dev_on:.1e}; max|c_BJ| off pattern = {off_max:.1e}  (degrees <= {nmax})')
        for lab, cc in (('D(c*)', cstar), ('D(c_BJ)  [exact split: Gram defect of Xi-bar]', cbj),
                        ('D(c_BJ on-pattern, off-pattern zeroed)', on_only), ('D(c* + c_BJ off-pattern values)', mix)):
            Xi = xi_map(P, w, rec, cc, nmax)
            print(f'   {lab:48s} ' + ' '.join(f'{gram_defect(Xi, n):.1e}' for n in degs))
            if lab.startswith('D(c_BJ)'):
                Phi = Xi.astype(float) - Q
                print(f'   |Phi~| = max|Xi-bar - Q| (propagated vector-operation error), cols of degree <= n: ' +
                      ' '.join(f'{float(np.max(np.abs(Phi[:, :C.N_of(n)]))):.1e}' for n in degs))
        sys.stdout.flush()


if __name__ == '__main__':
    main()
