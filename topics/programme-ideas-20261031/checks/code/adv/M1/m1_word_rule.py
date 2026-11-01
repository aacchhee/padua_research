#!/usr/bin/env python3
"""Adversarial check M1 (gen1-draft-1 half): what the non-commuting section pair
(H_x^(k), H_y^(k)) of a bivariate discrete measure actually defines.

Scope: M = 30 random nodes in [-1,1]^2, random positive weights (sum 1),
exact (H_x, H_y) from a Householder QR of the graded Vandermonde up to degree 9,
sections k = 1..4 (sizes 3, 6, 10, 15).  Seconds.  numpy only.

Tests
 T1  words of length <= 2k+1 are exact (reproduces the generator; the proof is
     the one-line P_k-projection argument, see the adversarial note).
 T2  at length 2k+2 the value e1' w e1 depends on the ORDER of the letters:
     x..xy..y, (xy)^(k+1), x y..y x give different numbers, so "the error of the
     rule on the monomial x^a y^b" is not defined beyond Pi_{2k+1}.
 T3  the error at length 2k+2 for the split (m1, m2) equals
     +<(I-P_k) m1, (I-P_k) m2>: sign-definite only for palindromic words
     (m1 = m2); for m1 = x^{k+1}, m2 = y^{k+1} it changes sign across measures.
 T4  anti-Gauss by sqrt(2)-scaling of the degree k -> k+1 coupling blocks of the
     (k+1)-section: error = -(Gauss error) word by word at length 2k+2 (identity);
     at length 2k+3 the errors are also checked.
 T5  non-polynomial f: f(x,y) = 1/((x-a)^2+(y-b)^2) through the only
     order-free lift G_k = (A-a)^2 + (B-b)^2 (A, B the k-sections):
     value e1' G_k^{-1} e1, anti-Gauss value, exact value; bracketing rate over
     random instances (generator's own kill: brackets fail on > 10% of
     instances); comparison with m-step univariate Lanczos on g(X,Y) with
     m = ceil((k+1)/2), i.e. the same exactness degree in g.
"""
import itertools
import numpy as np

rng = np.random.default_rng(20261101)


def graded_monomials(deg):
    return [(a - b, b) for a in range(deg + 1) for b in range(a + 1)]  # (i,j): x^i y^j, i+j = a


def sections(x, y, w, deg):
    """Orthonormal graded basis via QR of sqrt(w)-weighted Vandermonde; returns
    full H_x, H_y (size dim Pi_deg) in the orthonormal basis."""
    mons = graded_monomials(deg)
    V = np.array([[xi ** i * yi ** j for (i, j) in mons] for xi, yi in zip(x, y)])
    W = np.sqrt(w)[:, None]
    Q, R = np.linalg.qr(W * V)
    # fix signs so that diag(R) > 0
    s = np.sign(np.diag(R))
    Q = Q * s
    Hx = Q.T @ (x[:, None] * Q)
    Hy = Q.T @ (y[:, None] * Q)
    return Hx, Hy, Q


def dimP(k):
    return (k + 1) * (k + 2) // 2


def word_value(A, B, word):
    v = np.zeros(A.shape[0]); v[0] = 1.0
    for c in reversed(word):
        v = (A if c == 'x' else B) @ v
    return v[0]


def moment(x, y, w, word):
    i = word.count('x'); j = word.count('y')
    return np.sum(w * x ** i * y ** j)


def anti_gauss_pair(Hx, Hy, k):
    """(k+1)-section with the coupling blocks between degree k and k+1 scaled by sqrt(2)."""
    n0, n1 = dimP(k), dimP(k + 1)
    A = Hx[:n1, :n1].copy(); B = Hy[:n1, :n1].copy()
    for M in (A, B):
        M[n0:, :n0] *= np.sqrt(2.0)
        M[:n0, n0:] *= np.sqrt(2.0)
    return A, B


def lanczos_gauss(G, u, m):
    """m steps of Lanczos on symmetric G with start u (unit): returns T_m and e1'f(T)e1 for f = 1/t."""
    n = len(u)
    Q = np.zeros((n, m + 1)); alpha = np.zeros(m); beta = np.zeros(m)
    Q[:, 0] = u / np.linalg.norm(u)
    for j in range(m):
        v = G @ Q[:, j]
        if j > 0:
            v -= beta[j - 1] * Q[:, j - 1]
        alpha[j] = Q[:, j] @ v
        v -= alpha[j] * Q[:, j]
        v -= Q[:, :j + 1] @ (Q[:, :j + 1].T @ v)  # full reorthogonalisation (tiny sizes)
        beta[j] = np.linalg.norm(v)
        if j < m - 1:
            Q[:, j + 1] = v / beta[j]
    T = np.diag(alpha) + np.diag(beta[:m - 1], 1) + np.diag(beta[:m - 1], -1)
    e1 = np.zeros(m); e1[0] = 1
    return e1 @ np.linalg.solve(T, e1)


def main():
    M, DEG = 30, 9
    print("# M1 adversarial script: word rules of non-commuting sections (M = %d random nodes)" % M)
    # ---------- T1-T4 on three random measures ----------
    for trial in range(3):
        x = rng.uniform(-1, 1, M); y = rng.uniform(-1, 1, M)
        w = rng.uniform(0.2, 1.0, M); w /= w.sum()
        Hx, Hy, Q = sections(x, y, w, DEG)
        print("\n== measure %d ==" % trial)
        for k in range(1, 5):
            n = dimP(k)
            A, B = Hx[:n, :n], Hy[:n, :n]
            # T1: all words of length <= 2k+1
            err1 = 0.0
            for L in range(1, 2 * k + 2):
                for word in itertools.product('xy', repeat=L):
                    err1 = max(err1, abs(word_value(A, B, word) - moment(x, y, w, word)))
            # T2/T3: length 2k+2, monomial x^{k+1} y^{k+1}
            w1 = 'x' * (k + 1) + 'y' * (k + 1)
            w2 = 'xy' * (k + 1)
            w3 = 'x' + 'y' * (k + 1) + 'x' * k
            vals = [word_value(A, B, wd) for wd in (w1, w2, w3)]
            mom = moment(x, y, w, w1)
            # projection check of the error for the split m1 = x^{k+1}, m2 = y^{k+1}
            mons = graded_monomials(DEG)
            def coeffs(i, j):  # coordinates of x^i y^j in the orthonormal basis
                vec = np.sqrt(w) * x ** i * y ** j
                return Q.T @ vec
            c1 = coeffs(k + 1, 0); c2 = coeffs(0, k + 1)
            tail = c1[n:] @ c2[n:]            # <(I-P_k) x^{k+1}, (I-P_k) y^{k+1}>
            pal = 'x' * (k + 1) + 'x' * (k + 1)  # palindromic word x^{2k+2}
            pal_err = moment(x, y, w, pal) - word_value(A, B, pal)
            # T4: anti-Gauss
            Aa, Ba = anti_gauss_pair(Hx, Hy, k)
            flip = 0.0
            for word in itertools.product('xy', repeat=2 * k + 2):
                eG = moment(x, y, w, word) - word_value(A, B, word)
                eA = moment(x, y, w, word) - word_value(Aa, Ba, word)
                flip = max(flip, abs(eG + eA))
            flip3 = 0.0; ratio3 = []
            for word in itertools.product('xy', repeat=2 * k + 3):
                eG = moment(x, y, w, word) - word_value(A, B, word)
                eA = moment(x, y, w, word) - word_value(Aa, Ba, word)
                flip3 = max(flip3, abs(eG + eA))
                if abs(eG) > 1e-10:
                    ratio3.append(eA / eG)
            print("k=%d n=%2d | T1 max err words<=2k+1: %.1e | T2 values of x^%dy^%d by order: %s (moment %.6f)"
                  % (k, n, err1, k + 1, k + 1, ", ".join("%.6f" % v for v in vals), mom))
            print("        | T3 error(x..xy..y)=%+.3e  <(I-P)m1,(I-P)m2>=%+.3e | palindrome x^%d error=%+.3e (= +|.|^2)"
                  % (mom - vals[0], tail, 2 * k + 2, pal_err))
            print("        | T4 max|eGauss+eAnti| len 2k+2: %.1e ; len 2k+3: %.1e (eA/eG range %s)"
                  % (flip, flip3, ("[%.3f, %.3f]" % (min(ratio3), max(ratio3))) if ratio3 else "n/a"))
    # ---------- T5: non-polynomial f through the order-free lift ----------
    print("\n== T5: f = 1/((x-a)^2+(y-b)^2), pole outside [-1,1]^2 ; 200 random instances per k ==")
    for k in range(1, 5):
        n = dimP(k)
        brack = 0; errG = []; errL = []; errA = []
        for inst in range(200):
            x = rng.uniform(-1, 1, M); y = rng.uniform(-1, 1, M)
            w = rng.uniform(0.2, 1.0, M); w /= w.sum()
            a = rng.choice([-1, 1]) * rng.uniform(1.3, 2.5); b = rng.choice([-1, 1]) * rng.uniform(1.3, 2.5)
            Hx, Hy, Q = sections(x, y, w, DEG)
            A, B = Hx[:n, :n], Hy[:n, :n]
            G = (A - a * np.eye(n)) @ (A - a * np.eye(n)) + (B - b * np.eye(n)) @ (B - b * np.eye(n))
            e1 = np.zeros(n); e1[0] = 1
            vG = e1 @ np.linalg.solve(G, e1)
            Aa, Ba = anti_gauss_pair(Hx, Hy, k); na = Aa.shape[0]
            Ga = (Aa - a * np.eye(na)) @ (Aa - a * np.eye(na)) + (Ba - b * np.eye(na)) @ (Ba - b * np.eye(na))
            ea = np.zeros(na); ea[0] = 1
            vA = ea @ np.linalg.solve(Ga, ea)
            exact = np.sum(w / ((x - a) ** 2 + (y - b) ** 2))
            if (vG - exact) * (vA - exact) < 0:
                brack += 1
            # univariate Lanczos on g(X,Y) = diag((x-a)^2+(y-b)^2) with sqrt(w) start:
            #   m = k+1 steps (size k+1 << dim Pi_k) -- same number of "degrees" in one variable
            g = (x - a) ** 2 + (y - b) ** 2
            vL = lanczos_gauss(np.diag(g), np.sqrt(w), k + 1)
            errG.append(abs(vG - exact) / exact); errA.append(abs(vA - exact) / exact); errL.append(abs(vL - exact) / exact)
        print("k=%d (section size %2d): Gauss/anti-Gauss bracket the exact value in %3d/200 instances; "
              "median rel.err: pair-Gauss %.1e, pair-anti %.1e, univariate Lanczos on g(X,Y) with m=%d steps (size %d) %.1e"
              % (k, n, brack, np.median(errG), np.median(errA), k + 1, k + 1, np.median(errL)))
    # ---------- T5b: equal-cost comparison (dim Pi_k products with X/Y vs ~2 per Lanczos step on g(X,Y)) ----------
    print("\n== T5b: equal X/Y-product count: pair k-section (dim Pi_k products) vs Lanczos on g(X,Y) with m = dim Pi_k // 2 steps ==")
    for k in range(1, 5):
        n = dimP(k); errG = []; errL = []
        for inst in range(100):
            x = rng.uniform(-1, 1, M); y = rng.uniform(-1, 1, M)
            w = rng.uniform(0.2, 1.0, M); w /= w.sum()
            a = rng.choice([-1, 1]) * rng.uniform(1.3, 2.5); b = rng.choice([-1, 1]) * rng.uniform(1.3, 2.5)
            Hx, Hy, Q = sections(x, y, w, DEG); A, B = Hx[:n, :n], Hy[:n, :n]
            G = (A - a * np.eye(n)) @ (A - a * np.eye(n)) + (B - b * np.eye(n)) @ (B - b * np.eye(n))
            e1 = np.zeros(n); e1[0] = 1
            vG = e1 @ np.linalg.solve(G, e1); exact = np.sum(w / ((x - a) ** 2 + (y - b) ** 2))
            g = (x - a) ** 2 + (y - b) ** 2; m = max(1, n // 2)
            vL = lanczos_gauss(np.diag(g), np.sqrt(w), m)
            errG.append(abs(vG - exact) / exact); errL.append(abs(vL - exact) / exact)
        print("k=%d size %2d: pair-Gauss median rel.err %.1e | Lanczos on g with m=%d steps %.1e (exact to g-degree %d vs %d for the pair)"
              % (k, n, np.median(errG), max(1, n // 2), np.median(errL), 2 * max(1, n // 2) - 1, k))
    # ---------- T6: a genuinely mixed f: lift dependence ----------
    print("\n== T6: f = 1/(c - x y), c = 1.5: three lifts of the SAME f give different 'rules' ; 200 instances per k ==")
    c = 1.5
    for k in range(1, 5):
        n = dimP(k)
        spread = []; br = [0, 0, 0]; errs = [[], [], []]
        for inst in range(200):
            x = rng.uniform(-1, 1, M); y = rng.uniform(-1, 1, M)
            w = rng.uniform(0.2, 1.0, M); w /= w.sum()
            Hx, Hy, Q = sections(x, y, w, DEG)
            A, B = Hx[:n, :n], Hy[:n, :n]
            Aa, Ba = anti_gauss_pair(Hx, Hy, k); na = Aa.shape[0]
            e1 = np.zeros(n); e1[0] = 1; ea = np.zeros(na); ea[0] = 1
            exact = np.sum(w / (c - x * y))
            lifts = [lambda P, R: P @ R, lambda P, R: R @ P, lambda P, R: 0.5 * (P @ R + R @ P)]
            vals = []
            for i, lift in enumerate(lifts):
                vG = e1 @ np.linalg.solve(c * np.eye(n) - lift(A, B), e1)
                vA = ea @ np.linalg.solve(c * np.eye(na) - lift(Aa, Ba), ea)
                vals.append(vG)
                errs[i].append(abs(vG - exact) / exact)
                if (vG - exact) * (vA - exact) < 0:
                    br[i] += 1
            spread.append((max(vals) - min(vals)) / exact)
        print("k=%d: median relative spread between lifts AB, BA, sym: %.1e | median rel.err per lift: %.1e %.1e %.1e | brackets: %d %d %d /200"
              % (k, np.median(spread), np.median(errs[0]), np.median(errs[1]), np.median(errs[2]), br[0], br[1], br[2]))


if __name__ == "__main__":
    main()
