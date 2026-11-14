"""Path A for MP points (n even): Vandermonde solve in the basis U_i(x)U_j(y), i+j<=n, python-flint arb.

Independent of mp_kernel.py except for the (trivial) node/basis index lists, which are re-derived here.
All results are rigorous enclosures (arb balls).
"""
from flint import arb, arb_mat, ctx


def nodes_ints(n):
    """(m, k, p, q): w=p*pi/(n+2), v=q*pi/(n+3)."""
    return [(m, k, m, (2 * k if m % 2 else 2 * k - 1)) for m in range(1, n + 2) for k in range(1, n // 2 + 2)]


def basis_ij(n):
    return [(i, j) for i in range(n + 1) for j in range(n + 1 - i)]


def U_arb(x, n):
    u = [arb(1), 2 * x]
    for i in range(2, n + 1):
        u.append(2 * x * u[-1] - u[-2])
    return u[:n + 1]


def node_coords(n):
    pi = arb.pi()
    xs, ys = [], []
    for (m, k, p, q) in nodes_ints(n):
        xs.append((pi * p / (n + 2)).cos())
        ys.append((pi * q / (n + 3)).cos())
    return xs, ys


def phi_row(Ux, Uy, idx):
    return [Ux[i] * Uy[j] for (i, j) in idx]


def vandermonde(n):
    idx = basis_ij(n)
    xs, ys = node_coords(n)
    rows = [phi_row(U_arb(x, n), U_arb(y, n), idx) for x, y in zip(xs, ys)]
    return arb_mat(rows), idx, xs, ys


class ExactMP:
    """Lagrange basis enclosures.  l(P) solves V^T l = phi(P)  (V rows = nodes, cols = basis)."""

    def __init__(self, n, prec, want_inverse=False):
        self.n, self.prec = n, prec
        ctx.prec = prec
        self.V, self.idx, self.xs, self.ys = vandermonde(n)
        self.N = len(self.idx)
        self.det = self.V.det()
        self.det_nonzero = not self.det.contains(0)
        self.Vinv = self.V.inv() if want_inverse else None
        self.VT = self.V.transpose()

    def lagrange(self, x, y):
        """list of N arb enclosures of l_a(x,y) (x, y arb)."""
        ctx.prec = self.prec
        phi = phi_row(U_arb(x, self.n), U_arb(y, self.n), self.idx)
        if self.Vinv is not None:
            return [sum((self.Vinv[b, a] * phi[b] for b in range(self.N)), arb(0)) for a in range(self.N)]
        rhs = arb_mat([[t] for t in phi])
        sol = self.VT.solve(rhs)
        return [sol[a, 0] for a in range(self.N)]

    def lagrange_many(self, pts):
        """pts: list of (x,y) arb; one solve with several right-hand sides."""
        ctx.prec = self.prec
        cols = [phi_row(U_arb(x, self.n), U_arb(y, self.n), self.idx) for x, y in pts]
        rhs = arb_mat([[cols[c][b] for c in range(len(pts))] for b in range(self.N)])
        sol = self.VT.solve(rhs)
        return [[sol[a, c] for a in range(self.N)] for c in range(len(pts))]


def lam_from(ls):
    s = arb(0)
    for t in ls:
        s += abs(t)
    return s


def max_rad(vals):
    return max(float(abs(t).rad()) if False else float(t.rad()) for t in vals)


def adaptive_lambda(n, pts, precs=(256, 384, 512, 768, 1024, 1536, 2048, 3072), rad_target=1e-50):
    """Enclosures of lambda_n at pts (list of (x,y) arb built by caller with exact values at any prec: pass
    callables or fixed ints).  pts entries: (sx, sy) integers +-1 or arb-convertible exact values."""
    last = None
    for prec in precs:
        try:
            ctx.prec = prec
            ex = ExactMP(n, prec)
            if not ex.det_nonzero:
                continue
            P = [(arb(a), arb(b)) for a, b in pts]
            L = ex.lagrange_many(P)
            lams = [lam_from(l) for l in L]
            if all(l.is_finite() and float(l.rad()) < rad_target for l in lams):
                return prec, lams, ex
            last = (prec, lams, ex)
        except (ValueError, ZeroDivisionError, RuntimeError):
            continue
    return last
