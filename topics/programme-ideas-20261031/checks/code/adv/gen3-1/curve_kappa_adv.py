"""Adversarial probe for gen3-draft-1 (discrete OPs of sampled trajectory measures).
Model: claude-fable-5-1, effort xhigh (as requested by the orchestrator). 2026-11-01.

Derived from checks/code/gen3/curve_measure_probe.py (same quantities, more families,
two reference measures, growth-rate fits, diagonal n/m scaling, exact Gram cross-check).

Quantities (all MEASURED in the recorded scope, double precision unless stated):
  * D_pred  = implicit degree predicted by the tracing-index rule D = 2m/tau
              (m = trig degree, tau = tracing index of the parametrisation);
  * Hilbert increments h(d)-h(d-1) of the sampled measure (rank of the Chebyshev-
    Vandermonde on M equispaced time samples, tol 1e-10);
  * kappa_n(gamma; w) = sigma_max/sigma_min of the restriction Pi_n -> L^2(gamma, dt)
    in a basis orthonormal for the reference measure w (w = product Chebyshev on the
    square, or Lebesgue on the unit disk); computed from the SVD of V_curve R^{-1}
    where V_ref = Q R on a dense exact reference quadrature;
  * growth rate c = slope of log kappa_n in n (least squares over 2 <= n <= nmax);
  * Dubiner covering radius rho of the curve in the square (or disk) metric, which
    gives the known sup-norm norming bound ||p||_K <= sec(n rho) ||p||_gamma, n rho < pi/2.
Scope: M = 4096 equispaced time samples (exact trapezoidal integration of all trig
polynomials of degree < 4096, i.e. of all products p q with deg p, deg q <= n for
2 m n < 2048), degrees n <= 9, kappa resolved only while kappa < ~1e9 (double).
"""
import numpy as np, sys, math
from numpy.polynomial import chebyshev as C

M = 4096
T = 2*np.pi*np.arange(M)/M
rng = np.random.default_rng(20261101)

# ---------------------------------------------------------------- curve families
def rhodonea(k):
    return (lambda t: (np.cos(k*t)*np.cos(t), np.cos(k*t)*np.sin(t))), k+1, (2 if k % 2 else 1)

def lissajous(n1, n2, phi=0.0):
    # (cos n1 t, cos(n2 t + phi)); phi = 0 degenerate (traced twice), generic phi traced once
    tau = 2 if abs(math.sin(phi)) < 1e-14 else 1
    return (lambda t: (np.cos(n1*t), np.cos(n2*t+phi))), max(n1, n2), tau

def generic_trig(m, decay=0.6, seed=None):
    r = np.random.default_rng(seed)
    ax = r.normal(size=(m, 2))*decay**np.arange(m)[:, None]
    ay = r.normal(size=(m, 2))*decay**np.arange(m)[:, None]
    def f(t):
        x = sum(ax[k, 0]*np.cos((k+1)*t)+ax[k, 1]*np.sin((k+1)*t) for k in range(m))
        y = sum(ay[k, 0]*np.cos((k+1)*t)+ay[k, 1]*np.sin((k+1)*t) for k in range(m))
        return x, y
    x, y = f(T); s = 0.98/max(np.abs(x).max(), np.abs(y).max())
    return (lambda t: tuple(s*np.asarray(f(t)))), m, 1

def epitrochoid(k, d):
    # x = cos t - d cos k t, y = sin t - d sin k t ; trig degree k, traced once
    s = 1/(1+d)
    return (lambda t: (s*(np.cos(t)-d*np.cos(k*t)), s*(np.sin(t)-d*np.sin(k*t)))), k, 1

def modulated_rose(k, a=0.6, b=0.4):
    # closed "spiral-like" rosette r = a + b cos t, angle k t ; trig degree k+1, traced once
    return (lambda t: ((a+b*np.cos(t))*np.cos(k*t), (a+b*np.cos(t))*np.sin(k*t))), k+1, 1

def distorted_lissajous(n1, n2, eps):
    # Lissajous (cos n1 t, cos n2 t) plus a non-Chebyshev harmonic distortion of size eps
    def f(t):
        return (np.cos(n1*t)+eps*np.cos(2*t+0.3))/(1+eps), (np.cos(n2*t)+eps*np.sin(3*t+0.7))/(1+eps)
    return f, max(n1, n2), 1

# ---------------------------------------------------------------- bases and references
def graded_idx(n):
    return [(d-j, j) for d in range(n+1) for j in range(d+1)]

def cheb_prod(x, y, n):
    Tx, Ty = C.chebvander(x, n), C.chebvander(y, n)
    return np.column_stack([Tx[:, i]*Ty[:, j] for (i, j) in graded_idx(n)])

def reference(kind, n):
    """dense exact quadrature (nodes, sqrt-weights) for the reference measure, exact on Pi_{2n}"""
    if kind == "square":        # product Chebyshev (arcsine) measure, Gauss-Chebyshev tensor rule
        g = 2*n+2; th = (2*np.arange(g)+1)*np.pi/(2*g); xs = np.cos(th)
        X, Y = np.meshgrid(xs, xs, indexing="ij")
        w = np.full(X.size, (np.pi/g)**2)
        return X.ravel(), Y.ravel(), np.sqrt(w)
    if kind == "disk":          # Lebesgue measure on the unit disk, Gauss-Legendre in r^2 x equispaced angle
        gr = n+2; ga = 4*n+5
        u, wu = np.polynomial.legendre.leggauss(gr); r = np.sqrt((u+1)/2); wr = wu/2
        th = 2*np.pi*np.arange(ga)/ga
        R, TH = np.meshgrid(r, th, indexing="ij"); W = np.outer(wr, np.full(ga, np.pi/ga))
        return (R*np.cos(TH)).ravel(), (R*np.sin(TH)).ravel(), np.sqrt(W.ravel())
    raise ValueError(kind)

def kappa_table(curve, nmax, ref):
    xc, yc = curve(T)
    xr, yr, sw = reference(ref, nmax)
    Vr = cheb_prod(xr, yr, nmax)*sw[:, None]
    Vc = cheb_prod(xc, yc, nmax)/np.sqrt(M)
    Q, R = np.linalg.qr(Vr)            # reference-orthonormal basis coefficients R^{-1}
    out = []
    for n in range(nmax+1):
        N = (n+1)*(n+2)//2
        Rn = R[:N, :N]
        B = np.linalg.solve(Rn.T, Vc[:, :N].T).T      # Vc R^{-1}
        s = np.linalg.svd(B, compute_uv=False)
        rank = int(np.sum(s > 1e-10*s[0]))
        out.append((n, N, rank, s[0], s[-1], (s[0]/s[-1] if rank == N else np.inf)))
    return out

def hilbert_increments(curve, nmax, tol=1e-10):
    xc, yc = curve(T)
    V = cheb_prod(xc, yc, nmax)/np.sqrt(M)
    ranks = []
    for d in range(nmax+1):
        N = (d+1)*(d+2)//2
        s = np.linalg.svd(V[:, :N], compute_uv=False)
        ranks.append(int(np.sum(s > tol*s[0])))
    return [ranks[0]]+[ranks[d]-ranks[d-1] for d in range(1, nmax+1)]

def dubiner_radius(curve, ref, grid=161):
    """covering radius of the curve in the Dubiner metric of the square or the disk"""
    xc, yc = curve(T[::8])             # 512 curve samples suffice (metric is Lipschitz-ish)
    if ref == "square":
        g = np.cos(np.linspace(0, np.pi, grid)); X, Y = np.meshgrid(g, g); P = np.column_stack([X.ravel(), Y.ravel()])
        ax, ay = np.arccos(np.clip(xc, -1, 1)), np.arccos(np.clip(yc, -1, 1))
        dmin = np.full(len(P), np.inf)
        for i in range(0, len(P), 2000):
            p = P[i:i+2000]
            d = np.maximum(np.abs(np.arccos(p[:, :1])-ax[None, :]), np.abs(np.arccos(p[:, 1:2])-ay[None, :]))
            dmin[i:i+2000] = d.min(axis=1)
        return dmin.max()
    if ref == "disk":
        r = np.sqrt(np.linspace(0, 1, grid)); th = np.linspace(0, 2*np.pi, 2*grid, endpoint=False)
        R, TH = np.meshgrid(r, th); P = np.column_stack([(R*np.cos(TH)).ravel(), (R*np.sin(TH)).ravel()])
        cz = np.sqrt(np.clip(1-xc**2-yc**2, 0, None))
        dmin = np.full(len(P), np.inf)
        for i in range(0, len(P), 2000):
            p = P[i:i+2000]; pz = np.sqrt(np.clip(1-(p**2).sum(1), 0, None))
            cosd = p[:, :1]*xc[None, :]+p[:, 1:2]*yc[None, :]+pz[:, None]*cz[None, :]
            dmin[i:i+2000] = np.arccos(np.clip(cosd, -1, 1)).min(axis=1)
        return dmin.max()

def fit_slope(ns, ks):
    ns, ks = np.array(ns, float), np.log(np.array(ks, float))
    A = np.column_stack([ns, np.ones_like(ns)])
    return np.linalg.lstsq(A, ks, rcond=None)[0][0]

def report(name, fam, nmax=9, refs=("square",)):
    curve, m, tau = fam
    D = 2*m//tau
    print(f"\n== {name}: trig degree m={m}, tracing index tau={tau}, predicted implicit degree D={D}")
    inc = hilbert_increments(curve, min(nmax, D+1))
    if D+1 <= nmax:
        verdict = "yes" if inc[D-1:D+2] == [D, D, D] else "NO (numerical rank loss or wrong D_pred)"
    else:
        verdict = "n/a (D+1 > nmax; increments full so far)" if inc == list(range(1, len(inc)+1)) else "NO (rank loss below D)"
    print("  Hilbert increments d=0..:", inc, " (stabilise at D?)", verdict)
    for ref in refs:
        tab = kappa_table(curve, min(nmax, D-1), ref)
        ks = ["%.2e" % r[5] for r in tab]
        print(f"  kappa_n (ref={ref}), n=0..{min(nmax, D-1)}:", ks)
        fin = [(r[0], r[5]) for r in tab if 2 <= r[0] <= 8 and np.isfinite(r[5])]
        if len(fin) >= 3:
            c = fit_slope([f[0] for f in fin], [f[1] for f in fin])
            last = fin[-1]; step = np.log(fin[-1][1]/fin[-2][1])
            print(f"    log-slope c (n=2..{last[0]}) = {c:.2f} per degree; last-step ratio ln(k_n/k_(n-1)) = {step:.2f}")
        rho = dubiner_radius(curve, ref)
        print(f"    Dubiner covering radius in the {ref} metric rho = {rho:.3f}; sup-norm norming bound sec(n rho) valid for n < {np.pi/(2*rho):.1f}")
    return tab

if __name__ == "__main__":
    np.set_printoptions(linewidth=150)
    print("# Controls (Chebyshev / Lissajous--Chebyshev)")
    report("Lissajous (cos5t, cos6t) [degenerate, Padua-type]", lissajous(5, 6), nmax=9)
    report("Lissajous (cos5t, sin6t) = phase pi/2 [non-degenerate, Erb 2016 class]", lissajous(5, 6, np.pi/2), nmax=9)
    print("\n# Rhodonea family r = cos(k theta) (Erb 2021 nodes live on these), square and disk references")
    for k in (3, 5, 7, 9, 11):
        report(f"rhodonea k={k}", rhodonea(k), nmax=9, refs=("square", "disk"))
    for k in (2, 4):
        report(f"rhodonea k={k} (even: traced once)", rhodonea(k), nmax=9, refs=("square", "disk"))
    print("\n# Lissajous with generic phase (distortion of the Chebyshev case by phase only)")
    for phi in (0.05, 0.2, 0.5, 1.0):
        report(f"Lissajous (cos5t, cos(6t+{phi}))", lissajous(5, 6, phi), nmax=9)
    print("\n# Lissajous with harmonic distortion")
    for eps in (0.01, 0.05, 0.2):
        report(f"Lissajous(5,6) + eps={eps} harmonics", distorted_lissajous(5, 6, eps), nmax=9)
    print("\n# Epitrochoids / spirograph and closed rosettes")
    for k, d in ((4, 0.5), (6, 0.5), (8, 0.5)):
        report(f"epitrochoid k={k}, d={d}", epitrochoid(k, d), nmax=9, refs=("square", "disk"))
    for k in (4, 6, 8):
        report(f"modulated rose k={k} (r=0.6+0.4cos t)", modulated_rose(k), nmax=9, refs=("square", "disk"))
    print("\n# Generic trigonometric curves")
    for m, seed in ((3, 1), (4, 2), (5, 3), (6, 4), (8, 5)):
        report(f"generic trig m={m} seed={seed}", generic_trig(m, seed=seed), nmax=9)
