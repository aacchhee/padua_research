"""Adversarial probe 2 for gen3-draft-1: entry point 3 (Fourier-basis commutation of truncated sections).
Model: claude-fable-5-1, effort xhigh (as requested by the orchestrator). 2026-11-01.

Claim under test (draft entry point 3): on M equispaced time samples of a trig curve, X = x(S), Y = y(S)
with S the cyclic shift, so H_x, H_y "should commute at rounding level even for the truncated
sections of the full M x M problem, unlike generic nodes"; kill criterion M = 64, 128, n <= 6.

Facts checked here (MEASURED, double precision):
  (1) [H_x^{(n)}, H_y^{(n)}] = Q_n^T (X P_n Y - Y P_n X) Q_n = -(B_x^T B_y - B_y^T B_x) placed in the
      degree-n diagonal block, where B_x, B_y are the degree-n -> degree-(n+1) coupling blocks
      (exact identity for commuting X, Y; verified numerically);
  (2) the commutator norm is invariant under any unitary change of basis of C^M (Fourier basis
      included), so "transformation to the Fourier basis" cannot reduce it;
  (3) the Krylov space of degree n of the pair (x(S), y(S)) started at the DC vector lives in
      Fourier modes |k| <= m n, and all Fourier coefficients of p(x(t), y(t)) beyond m n vanish.
Scope: rhodonea k = 7 (m = 8, D = 8), generic trig curve m = 4, and the Lissajous (5,6) control;
M = 64, 128, 512; n <= 8; graded Gram-Schmidt with two passes, tolerance 1e-10 on pivots.
"""
import numpy as np
from numpy.polynomial import chebyshev as C

def curve(name, t):
    if name == "lissajous_5_6": return np.cos(5*t), np.cos(6*t)
    if name == "rhodonea_7":    return np.cos(7*t)*np.cos(t), np.cos(7*t)*np.sin(t)
    if name == "generic_4":
        x = 0.7*np.cos(t)+0.25*np.cos(3*t+0.4); y = 0.7*np.sin(2*t)+0.2*np.sin(4*t+1.1); return x, y
    raise ValueError

def graded_idx(n): return [(d-j, j) for d in range(n+1) for j in range(d+1)]

def sections(x, y, nmax, tol=1e-10):
    """graded discrete OPs (vectors on the nodes) up to degree nmax; returns Q, degrees"""
    M = len(x)
    Tx, Ty = C.chebvander(x, nmax), C.chebvander(y, nmax)
    Q, deg = [], []
    for (i, j) in graded_idx(nmax):
        v = Tx[:, i]*Ty[:, j]/np.sqrt(M)
        for _ in range(2):
            for q in Q: v = v - q*(q@v)
        nv = np.linalg.norm(v)
        if nv > tol:
            Q.append(v/nv); deg.append(i+j)
    return np.column_stack(Q), np.array(deg)

def run(name, M, nmax):
    t = 2*np.pi*np.arange(M)/M
    x, y = curve(name, t)
    Q, deg = sections(x, y, nmax+1)        # one extra degree to form the coupling blocks
    X, Y = np.diag(x), np.diag(y)
    print(f"\n== {name}, M={M}: kept {Q.shape[1]} OP vectors up to degree {nmax+1}")
    print("  n   N_n   ||[Hx,Hy]||_2   ||Bx^T By - By^T Bx||_2   max|diff|   ||[Hx,Hy]||/||Hx||")
    for n in range(1, nmax+1):
        In = deg <= n; Ib = deg == n; Ic = deg == n+1
        Qn = Q[:, In]
        Hx, Hy = Qn.T@X@Qn, Qn.T@Y@Qn
        comm = Hx@Hy - Hy@Hx
        Bx, By = Q[:, Ic].T@X@Q[:, Ib], Q[:, Ic].T@Y@Q[:, Ib]   # degree n -> n+1 coupling
        pred = -(Bx.T@By - By.T@Bx)
        # predicted commutator: zero except the degree-n diagonal block
        P = np.zeros_like(comm); idx = np.flatnonzero(Ib[In]); P[np.ix_(idx, idx)] = pred
        print(f"  {n:>2} {Qn.shape[1]:>5}   {np.linalg.norm(comm,2):.3e}        {np.linalg.norm(pred,2):.3e}"
              f"            {np.abs(comm-P).max():.1e}     {np.linalg.norm(comm,2)/np.linalg.norm(Hx,2):.2e}")
    # (2) unitary invariance: same numbers after mapping everything to the Fourier basis
    F = np.fft.fft(np.eye(M))/np.sqrt(M)
    n = min(4, nmax); In = deg <= n; Qn = Q[:, In]
    Xf, Yf, Qf = F@X@F.conj().T, F@Y@F.conj().T, F@Qn
    Hxf, Hyf = Qf.conj().T@Xf@Qf, Qf.conj().T@Yf@Qf
    m = {"lissajous_5_6": 6, "rhodonea_7": 8, "generic_4": 4}[name]
    kk = np.arange(M); cyc = np.minimum(np.abs(kk[:, None]-kk[None, :]), M-np.abs(kk[:, None]-kk[None, :]))
    print(f"  Fourier basis, n={n}: ||[Hx,Hy]|| = {np.linalg.norm(Hxf@Hyf-Hyf@Hxf,2):.3e}  (same as above, unitary invariance);"
          f" Xf is a Laurent polynomial of the shift: max |entry| at cyclic distance > m: {np.abs(Xf[cyc > m]).max():.1e}")
    # (3) Fourier support of the Krylov space
    m = {"lissajous_5_6": 6, "rhodonea_7": 8, "generic_4": 4}[name]
    for n in (2, 4, 6):
        if n > nmax: break
        In = deg <= n; Qf = F@Q[:, In]
        k = np.minimum(np.arange(M), M-np.arange(M))          # |frequency|
        beyond = np.abs(Qf[k > m*n, :]).max() if (k > m*n).any() else 0.0
        print(f"  Krylov space degree {n}: max |Fourier coefficient| beyond mode m*n={m*n}: {beyond:.1e}  (dimension {In.sum()} inside 2mn+1={2*m*n+1} modes)")

if __name__ == "__main__":
    for name in ("rhodonea_7", "generic_4", "lissajous_5_6"):
        for M in (64, 128, 512):
            run(name, M, nmax=6 if M == 64 else 8)
