"""X1 round 2 research helpers: the tensor (rotated-torus) lift of Xu interpolation.

Conventions (literature-xu-mp.md section 1): z_k = cos(k pi/n); X_n = {(z_r, z_s): r+s = n+1 mod 2}.
Rotated angles: x = (cos th1, cos th2), u = (th1+th2)/2, v = (th1-th2)/2.
Lift grid: u_p = p pi/(2n), p in the residue class C_n = {p mod 4n : p = n+1 mod 2} (2n residues).
1-D cardinal kernel of 2n equispaced nodes: d_n(t) = sin(n t) cot(t/2) / (2n), d_n(0) = 1.
Claim tested (theory/X1-01): l_xi(x) = sum over lifts (p,q) of xi of d_n(u-u_p) d_n(v-v_q).
All functions use mpmath (precision set by the caller).
"""
import mpmath as mp


def cls(n):
    """Residues p mod 4n with p = n+1 (mod 2)."""
    return [p for p in range(4 * n) if (p - n - 1) % 2 == 0]


def dker(n, t):
    """d_n(t) = sin(n t) cot(t/2)/(2n); removable singularity at t in 2 pi Z handled by the cosine sum."""
    s = mp.sin(t / 2)
    if abs(s) < mp.mpf(10) ** (-(mp.mp.dps // 2)):
        return (1 + 2 * mp.fsum(mp.cos(j * t) for j in range(1, n)) + mp.cos(n * t)) / (2 * n)
    return mp.sin(n * t) * mp.cos(t / 2) / s / (2 * n)


def fold(n, k):
    k %= 2 * n
    return k if k <= n else 2 * n - k


def node_of_lift(n, p, q):
    """Xu node (r,s) in [0,n]^2 below the lift (p,q): angles ((p+q) pi/(2n), (p-q) pi/(2n)) folded by evenness."""
    return fold(n, (p + q) // 2), fold(n, (p - q) // 2)


def fibers(n):
    """dict node -> list of lifts (p,q) in C_n x C_n."""
    C = cls(n)
    F = {}
    for p in C:
        for q in C:
            F.setdefault(node_of_lift(n, p, q), []).append((p, q))
    return F


def ell_lift(n, th, F=None):
    """dict node -> sum over its fiber of d(u-u_p) d(v-v_q)."""
    if F is None:
        F = fibers(n)
    u, v = (th[0] + th[1]) / 2, (th[0] - th[1]) / 2
    C = cls(n)
    du = {p: dker(n, u - mp.pi * p / (2 * n)) for p in C}
    dv = {q: dker(n, v - mp.pi * q / (2 * n)) for q in C}
    return {xi: mp.fsum(du[p] * dv[q] for (p, q) in lifts) for xi, lifts in F.items()}


def omega(n, u):
    """Lebesgue function of the 2n-point equispaced trigonometric interpolation on the class C_n."""
    return mp.fsum(abs(dker(n, u - mp.pi * p / (2 * n))) for p in cls(n))


def Lcheb(n):
    """L_n = (1/n) sum_{k=1}^n cot((2k-1) pi/(4n)): Lebesgue constant of interpolation at the n zeros of T_n."""
    return mp.fsum(mp.cot((2 * k - 1) * mp.pi / (4 * n)) for k in range(1, n + 1)) / n


def A(n):
    return 2 / mp.pi * (mp.log(n) + mp.euler + mp.log(8 / mp.pi))
