"""Independent check (b): grid + local search for the maximizer set, n = 2..16 (float64).
Lagrange basis from a direct Vandermonde solve (Chebyshev tensor basis + E_j), no kernel formula."""
import sys, json
import numpy as np
from scipy.optimize import minimize


def basis(n, x, y):
    sig = 1 if n % 2 == 0 else -1
    tx = np.arccos(np.clip(x, -1, 1)); ty = np.arccos(np.clip(y, -1, 1))
    Tx = [np.cos(k * tx) for k in range(n + 1)]; Ty = [np.cos(k * ty) for k in range(n + 1)]
    cols = [Tx[i] * Ty[j] for i in range(n) for j in range(n - i)]
    cols += [Tx[n - j] * Ty[j] - sig * Tx[j] * Ty[n - j] for j in range((n + 1) // 2)]
    return np.stack(cols, axis=-1)


def lag(n):
    nd = [(r, s) for r in range(n + 1) for s in range(n + 1) if (r + s) % 2 == (n + 1) % 2]
    z = np.cos(np.arange(n + 1) * np.pi / n)
    A = basis(n, np.array([z[r] for r, s in nd]), np.array([z[s] for r, s in nd]))
    return np.linalg.inv(A)


def Lc(n):
    k = np.arange(1, n + 1)
    return np.sum(1 / np.tan((2 * k - 1) * np.pi / (4 * n))) / n


def main():
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 16
    rng = np.random.default_rng(7)
    for n in range(2, nmax + 1):
        C = lag(n)
        lam = lambda x, y: np.abs(basis(n, x, y) @ C).sum(axis=-1)
        L2 = Lc(n) ** 2
        M = 12 * n
        th = np.arange(M + 1) * np.pi / M
        T1, T2 = np.meshgrid(th, th, indexing='ij')
        X, Y = np.cos(T1), np.cos(T2)
        V = lam(X.ravel(), Y.ravel()).reshape(X.shape)
        gmax = V.max()
        idx = np.argwhere(V >= gmax - 1e-9)
        argset = sorted({(round(float(X[i, j]), 12), round(float(Y[i, j]), 12)) for i, j in idx})
        if n % 2 == 0:
            Vstar = sorted({(1.0, 1.0), (1.0, -1.0), (-1.0, 1.0), (-1.0, -1.0)})
        else:
            Vstar = sorted({(1.0, -1.0), (-1.0, 1.0)})
        # best non-vertex on grid: exclude a neighbourhood of radius 1 grid cell? no: exclude exact vertices only
        isvert = (np.abs(np.abs(X) - 1) < 1e-14) & (np.abs(np.abs(Y) - 1) < 1e-14)
        Vn = np.where(isvert, -np.inf, V)
        second = Vn.max()
        # local refinement from top 30 non-vertex grid points + 200 random starts (angle variables)
        f = lambda t: -lam(np.array([np.cos(t[0])]), np.array([np.cos(t[1])]))[0]
        order = np.argsort(Vn.ravel())[::-1][:30]
        starts = [(T1.ravel()[k], T2.ravel()[k]) for k in order] + [tuple(rng.uniform(0, np.pi, 2)) for _ in range(200)]
        best_loc = -np.inf; best_pt = None
        for s in starts:
            r = minimize(f, np.array(s), method='Nelder-Mead', options=dict(xatol=1e-10, fatol=1e-13, maxiter=4000))
            x, y = np.cos(r.x[0]), np.cos(r.x[1])
            dv = min(np.hypot(x - a, y - b) for a, b in Vstar)
            if dv > 1e-6 and -r.fun > best_loc:
                best_loc = -r.fun; best_pt = (float(x), float(y))
        print(json.dumps(dict(n=n, L2=L2, gridmax_minus_L2=float(gmax - L2), argmax_eq_Vstar=(argset == Vstar),
                              grid_second_ratio=float(second / L2), local_best_nonvertex_ratio=float(best_loc / L2),
                              local_best_pt=best_pt)), flush=True)


if __name__ == '__main__':
    main()
