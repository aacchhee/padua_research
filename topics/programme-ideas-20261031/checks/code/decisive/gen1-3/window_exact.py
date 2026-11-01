"""Decisive test gen1-3, window diagnostics with EXACT blocks (found while implementing T3).

With W_t the exact degree blocks (from a double QR of the graded evaluated basis, twice), and the
candidate space C_t = (W_{t-1} + W_t + x W_t + y W_t) / l_{t+1}:
  (1) the largest singular value of the inner-product matrix W_s^H W C_t for every older block s <= t
      (nonzero => C_t has components in W_s);
  (2) the rank of the remainder of C_t after PROJECTING off the last k blocks (k = 1..t+1); a
      Lanczos step with a k-block projection window needs rank t+2 = dim W_{t+1};
  (3) the two CONSTRAINED schemes: project off the last two blocks and keep the subspace orthogonal
      to the third (B), or project three and constrain with the fourth (A): dimension of the
      remainder, rank of the constraint matrix, dimension kept, min singular value against W_{t+1}.
Classes: the adversary's generic real lines, Ppt, Pbhh, Ldiag, Mpt and the polynomial control.
Scope: M = 120 random nodes in [-1,1]^2 (seed 1), unit weights, n = 10, eps_min = 1e-2; seconds.
MEASURED within this scope only.
"""
import sys, os
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from orf2d import *

OUT = []


def say(s=""):
    print(s)
    OUT.append(s)


if __name__ == '__main__':
    x, y = random_nodes(120, 1); w = np.ones(120); sw = np.sqrt(w)
    n = 10
    rng = np.random.default_rng(5)
    generic = []
    for k in range(n):
        th = rng.uniform(0, 2 * np.pi); c = rng.choice([-1, 1]) * rng.uniform(1.6, 2.5)
        generic.append((np.cos(th), np.sin(th), c))
    classes = {'generic real lines': generic, 'Ppt': make_lines('Ppt', n, 1e-2), 'Pbhh': make_lines('Pbhh', n, 1e-2),
               'Ldiag': make_lines('Ldiag', n, 1e-2), 'Mpt': make_lines('Mpt', n, 1e-2), 'P (control)': make_lines('P', n, 1e-2)}
    for name, lines in classes.items():
        A = eval_basis_graded(x, y, lines, n)
        Qw, _ = np.linalg.qr(sw[:, None] * A); Qw, _ = np.linalg.qr(Qw); Q = Qw / sw[:, None]
        blocks = np.concatenate([[t] * (t + 1) for t in range(n + 1)])
        Wb = lambda t: Q[:, blocks == t]
        say(f"\n== {name} ==")
        for t in range(1, n):
            ell = line_vals(x, y, lines[t])
            Ct = np.column_stack([Wb(t - 1), Wb(t), x[:, None] * Wb(t), y[:, None] * Wb(t)]) / ell[:, None]
            U, S, _ = np.linalg.svd(sw[:, None] * Ct, full_matrices=False); rk = int(np.sum(S > 1e-10 * S[0])); R = U[:, :rk]
            Wn = sw[:, None] * Wb(t + 1)
            gen = np.linalg.norm(Wn - R @ (R.conj().T @ Wn), 2)
            comps = " ".join(f"W{s}:{np.linalg.svd((sw[:, None] * Wb(s)).conj().T @ R, compute_uv=False).max():.0e}" for s in range(t + 1))
            rem = []
            for k in range(1, t + 2):
                Wlow = sw[:, None] * np.column_stack([Wb(s) for s in range(t - k + 1, t + 1)])
                Rr = R - Wlow @ (Wlow.conj().T @ R); Rr = Rr - Wlow @ (Wlow.conj().T @ Rr)
                rem.append(int(np.sum(np.linalg.svd(Rr, compute_uv=False) > 1e-8)))

            def proj_off(R, ks):
                Wlow = sw[:, None] * np.column_stack([Wb(s) for s in ks])
                Rr = R - Wlow @ (Wlow.conj().T @ R); Rr = Rr - Wlow @ (Wlow.conj().T @ Rr)
                U, S, _ = np.linalg.svd(Rr, full_matrices=False); r = int(np.sum(S > 1e-8)); return U[:, :r]

            def constrain(R, ks):
                Wc = sw[:, None] * np.column_stack([Wb(s) for s in ks])
                N = Wc.conj().T @ R
                _, s, Vh = np.linalg.svd(N, full_matrices=True); r = int(np.sum(s > 1e-8))
                Y = R @ Vh[r:].conj().T
                sv = np.linalg.svd(Wn.conj().T @ Y, compute_uv=False).min() if Y.shape[1] else 0.0
                return Y.shape[1], r, sv
            schemes = ""
            if t >= 2:
                Rp = proj_off(R, [t - 1, t]); dB, rB, sB = constrain(Rp, [t - 2])
                schemes += f" | B(proj2,con1): rem {Rp.shape[1]}, con rank {rB}, kept {dB}, min sv vs W_t+1 {sB:.2f}"
            if t >= 3:
                Rp = proj_off(R, [t - 2, t - 1, t]); dA, rA, sA = constrain(Rp, [t - 3])
                schemes += f" | A(proj3,con1): rem {Rp.shape[1]}, con rank {rA}, kept {dA}, min sv {sA:.2f}"
            say(f" t={t} dimC={rk} W_t+1 in C_t: {gen:.0e} | comps {comps} | remainder rank after projecting k=1..{t+1} blocks: {rem} (need {t+2}){schemes}")
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'window_exact.out'), 'w') as fh:
        fh.write("\n".join(OUT) + "\n")
