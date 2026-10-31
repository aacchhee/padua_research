"""Probe: conditioning of the Husimi-Q sensing matrix for Fock cutoff N under
three phase-space designs with the SAME number of points (N+1)(2N+1):
  (a) Padua points of total degree 2N scaled to the square [-R,R]^2 (Landon-Cardinal et al. 2018 style),
  (b) multi-ring design: N+1 rings, 2N+1 equispaced angles, radii = sqrt(Gauss-Laguerre nodes),
  (c) equispaced (N+1)x(2N+1) grid on [-R,R]^2.
Sensing matrix A[i,(j,k)] = exp(-|a_i|^2) conj(a_i)^j a_i^k / sqrt(j! k!)  (pi dropped).
Also reports the angular decoupling check for the ring design.
"""
import numpy as np
from math import factorial

def padua(n):
    # Pad_n = {(cos(j pi/n), cos(k pi/(n+1))): j+k even}
    pts = []
    for j in range(n+1):
        for k in range(n+2):
            if (j+k) % 2 == 0:
                pts.append((np.cos(j*np.pi/n), np.cos(k*np.pi/(n+1))))
    return np.array(pts)

def sensing(alpha, N):
    J, K = np.meshgrid(np.arange(N+1), np.arange(N+1), indexing="ij")
    J, K = J.ravel(), K.ravel()
    fac = np.array([np.sqrt(factorial(j)*factorial(k)) for j, k in zip(J, K)])
    A = np.exp(-np.abs(alpha)[:, None]**2) * np.conj(alpha)[:, None]**J[None, :] * alpha[:, None]**K[None, :] / fac[None, :]
    return A

def kappa(A):
    s = np.linalg.svd(A, compute_uv=False)
    return s[0]/s[-1]

def ring_design(N, scale=1.0):
    s, _ = np.polynomial.laguerre.laggauss(N+1)      # nodes of weight e^{-s} on [0,inf)
    radii = np.sqrt(s)*scale
    ang = 2*np.pi*np.arange(2*N+1)/(2*N+1)
    return (radii[:, None]*np.exp(1j*ang[None, :])).ravel()

print(" N | #pts | kappa Padua(best R) R | kappa ring(best scale) sc | kappa grid(best R) R")
for N in range(1, 9):
    npts = (N+1)*(2*N+1)
    best_p = min(((kappa(sensing(P[:, 0]+1j*P[:, 1], N)), R) for R in np.linspace(1.0, 5.0, 41)
                   for P in [padua(2*N)*R]), key=lambda t: t[0])
    best_r = min(((kappa(sensing(ring_design(N, sc), N)), sc) for sc in np.linspace(0.6, 1.6, 41)), key=lambda t: t[0])
    def grid(R):
        xs = np.linspace(-R, R, N+1); ys = np.linspace(-R, R, 2*N+1)
        X, Y = np.meshgrid(xs, ys, indexing="ij")
        return (X+1j*Y).ravel()
    best_g = min(((kappa(sensing(grid(R), N)), R) for R in np.linspace(1.0, 5.0, 41)), key=lambda t: t[0])
    print(f"{N:2d} | {npts:4d} | {best_p[0]:9.2e} {best_p[1]:4.1f} | {best_r[0]:9.2e} {best_r[1]:4.2f} | {best_g[0]:9.2e} {best_g[1]:4.1f}")

# angular decoupling check: Gram A^H A of the ring design is block-diagonal in p = k - j
N = 5
A = sensing(ring_design(N), N)
G = A.conj().T @ A
J, K = np.meshgrid(np.arange(N+1), np.arange(N+1), indexing="ij")
p = (K-J).ravel()
mask = p[:, None] != p[None, :]
print("ring design N=5: max |Gram entry| across different angular frequencies p=k-j: %.1e (same-p block max %.1e)"
      % (np.max(np.abs(G[mask])), np.max(np.abs(G[~mask]))))
