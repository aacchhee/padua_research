#!/usr/bin/env python3
"""Auditor's operator-norm sanity values (MEASURED floats; enumeration exact up to rounding)."""
import math, time, sys
import numpy as np
sys.path.insert(0, '.')
from f4_numeric import nodes, rho_of, d_formula_nodes, weights_legendre_solve, legn, tot, PI, a_floor, kappa, Cstar

def basis(m, n, j, k):
    x = np.cos(PI*j/m); y = np.cos(PI*k/(m+1))
    lx = legn(x, n); ly = legn(y, n)
    return np.column_stack([lx[:, a]*ly[:, b] for a, b in tot(n)])

def enum_norm(w, B):
    s = len(w)
    M = (w[:, None]*B)  # rows: w_z b_z
    best = 0.0; arg = None
    total = 2**(s-1)
    step = 1 << 18
    bitsel = np.arange(s-1)
    for start in range(0, total, step):
        idx = np.arange(start, min(start+step, total), dtype=np.int64)
        S = np.empty((len(idx), s))
        S[:, 0] = 1.0
        S[:, 1:] = 2*((idx[:, None] >> bitsel) & 1) - 1
        out = S @ M
        val = np.einsum('ij,ij->i', out, out)
        i = int(np.argmax(val))
        if val[i] > best:
            best = float(val[i]); arg = S[i].copy()
    return math.sqrt(best), arg

def ascent(w, B, starts, rng, iters=500):
    best = 0.0
    M = w[:, None]*B
    for st in starts:
        s = st.copy()
        prev = -1
        for _ in range(iters):
            g = s @ M
            nv = np.linalg.norm(g)
            if nv <= prev*(1+1e-14):
                break
            prev = nv
            a = g/nv
            s_new = np.sign(w*(B @ a)); s_new[s_new == 0] = 1
            if np.array_equal(s_new, s):
                break
            s = s_new
        best = max(best, prev)
    return best

def main():
    rng = np.random.default_rng(20261105)
    t0 = time.time()
    print("C* = %.10f" % Cstar)
    print("== exact sign-vertex enumeration (n=m-1), plus all n<m ==")
    for m in [2, 3, 4, 5, 6]:
        j, k = nodes(m)
        w, _, _ = weights_legendre_solve(m)
        rho = rho_of(m, j, k)
        d = d_formula_nodes(m, j, k)
        assert np.max(np.abs(w-rho*d)) < 1e-13
        res = []
        for n in range(0, m):
            B = basis(m, n, j, k)
            nrm, s = enum_norm(w, B)
            res.append(nrm)
        tau = np.abs(w).sum()
        print(f"m={m} nodes={len(w)} tau={tau:.10f} tau/2={tau/2:.10f} norms n=0..m-1: " + ", ".join(f"{r:.10f}" for r in res), f"[{time.time()-t0:.1f}s]")
        assert abs(res[0]-tau/2) < 1e-12
        assert all(2-1e-12 <= r <= Cstar for r in res)
    print("== ascent lower bounds (n=m-1), proof-derived per-m upper bound, sqrt(tau*beta_abs) ==")
    for m in [7, 8, 9, 10, 11, 12, 15, 16, 20, 21, 25, 30, 31, 40, 41, 50, 60]:
        j, k = nodes(m)
        if m <= 45:
            w, _, _ = weights_legendre_solve(m)
            rho = rho_of(m, j, k)
            assert np.max(np.abs(w - rho*d_formula_nodes(m, j, k))) < 1e-12
        else:
            rho = rho_of(m, j, k)
            w = rho*d_formula_nodes(m, j, k)
        B = basis(m, m-1, j, k)
        starts = [np.ones(len(w)), np.sign(w)+(w == 0)]
        # sign of reproducing kernel at a few points
        for (px, py) in [(1, 1), (-1, 1), (1, -1), (-1, -1), (0, 0), (1, 0), (0, 1), (-1, 0), (0, -1)]:
            kv = basis_point(m, px, py) @ B.T
            st = np.sign(w*kv); st[st == 0] = 1
            starts.append(st)
        for _ in range(24):
            starts.append(rng.choice([-1.0, 1.0], size=len(w)))
        lb = ascent(w, B, starts, rng)
        absw = np.abs(w)
        tau = absw.sum()
        beta_abs = np.linalg.eigvalsh(B.T @ (absw[:, None]*B))[-1]
        g = PI**2*np.sin(PI*j/m)*np.sin(PI*k/(m+1))
        v = rho*g
        lam_main = np.linalg.eigvalsh(B.T @ (v[:, None]*B))[-1]
        lam_raw = np.linalg.eigvalsh(B.T @ (rho[:, None]*B))[-1]
        e_nodes = np.max(np.abs(w/rho - g))
        # pointwise inequality used in Section 4
        assert np.all(absw <= v + 68/(3*m)*rho + 1e-15)
        per_m = math.sqrt(v.sum()*lam_main) + e_nodes*math.sqrt(lam_raw)
        print(f"m={m:3d} lower(ascent)={lb:.6f} per-m proof bound={per_m:.4f} sqrt(tau*beta_abs)={math.sqrt(tau*beta_abs):.4f} tau={tau:.8f} C*={Cstar:.4f} [{time.time()-t0:.1f}s]")
        assert 2-1e-12 <= lb <= per_m + 1e-9 and per_m <= Cstar
    print("elapsed", time.time()-t0)

def basis_point(m, px, py):
    lx = legn(np.array([float(px)]), m-1); ly = legn(np.array([float(py)]), m-1)
    return np.array([lx[0, a]*ly[0, b] for a, b in tot(m-1)])

if __name__ == '__main__':
    main()
