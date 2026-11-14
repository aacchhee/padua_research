"""Path A for Xu interpolation: rigorous interval (python-flint arb) Vandermonde solve.

Interpolation space V_n (literature-xu-mp.md section 1):
  Pi_{n-1} basis T_i(x)T_j(y) (i+j<=n-1, unscaled Chebyshev) plus the extra functions
  T_{n-j}(x)T_j(y) - sigma T_j(x)T_{n-j}(y), 0<=j<ceil(n/2), sigma=+1 (n even), -1 (n odd).
Nodes X_n = {(cos(r pi/n), cos(s pi/n)) : r+s = n+1 mod 2}.
All Lagrange values are arb enclosures (>= 256 bits by default); l_xi(x) = (b(x) . V^{-1})_xi.
Points are given as angles (arb) th=(th1,th2): x=(cos th1, cos th2); T_i(cos t) = cos(i t).
"""
from flint import arb, arb_mat, ctx
import math


def sigma(n):
    return 1 if n % 2 == 0 else -1


def node_list(n):
    return [(r, s) for r in range(n + 1) for s in range(n + 1) if (r + s) % 2 == (n + 1) % 2]


def basis_index(n):
    """List of ('p', i, j) for T_i T_j and ('e', j) for extra functions."""
    b = [("p", i, j) for i in range(n) for j in range(n - i)]
    b += [("e", j) for j in range((n + 1) // 2)]  # j < ceil(n/2)
    return b


class XuExact:
    def __init__(self, n, prec=256):
        self.n = n
        self.prec = prec
        ctx.prec = prec
        self.sig = sigma(n)
        self.nodes = node_list(n)
        self.basis = basis_index(n)
        self.N = len(self.nodes)
        self.dim = len(self.basis)
        self.square = self.N == self.dim
        self.pi = arb.pi()
        V = arb_mat(self.N, self.dim)
        for a, (r, s) in enumerate(self.nodes):
            row = self.basis_row((self.pi * r / n, self.pi * s / n))
            for m, val in enumerate(row):
                V[a, m] = val
        self.V = V
        self.det = V.det() if self.square else None
        self.det_nonzero = (not self.det.contains(0)) if self.square else False
        self.Vinv = V.inv() if self.det_nonzero else None

    def basis_row(self, th):
        n = self.n
        c1 = [arb(0) for _ in range(n + 1)]
        c2 = [arb(0) for _ in range(n + 1)]
        for i in range(n + 1):
            c1[i] = (th[0] * i).cos()
            c2[i] = (th[1] * i).cos()
        row = []
        for b in self.basis:
            if b[0] == "p":
                row.append(c1[b[1]] * c2[b[2]])
            else:
                j = b[1]
                row.append(c1[n - j] * c2[j] - self.sig * c1[j] * c2[n - j])
        return row

    def ell(self, th):
        """Enclosures of l_xi(x) for all nodes (list in node order)."""
        row = self.basis_row(th)
        out = []
        for a in range(self.N):
            acc = arb(0)
            for m in range(self.dim):
                acc += row[m] * self.Vinv[m, a]
            out.append(acc)
        return out

    def lam(self, th):
        return sum((abs(v) for v in self.ell(th)), arb(0))

    def interpolation_check(self):
        """V * Vinv encloses identity; returns (all_contain_delta, max_radius)."""
        P = self.V * self.Vinv
        ok = True
        mr = 0.0
        for i in range(self.N):
            for j in range(self.N):
                e = P[i, j]
                ok &= bool(e.contains(1 if i == j else 0))
                mr = max(mr, float(e.rad()))
        return ok, mr

    def inverse_max_width(self):
        return max(float(self.Vinv[i, j].rad()) for i in range(self.N) for j in range(self.N))
