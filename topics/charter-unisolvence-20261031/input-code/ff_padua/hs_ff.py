"""Does Harris-Simanek (Proc. AMS 149 (2021), Thm 1: checkerboard subsets of X x Y with |X|=m+1,
|Y|=m+2 are unisolvent for P_m for ANY distinct *decreasing* real nodes) survive over F_p?

Findings checked here:
 (1) symbolic m=2: det of the monomial Vandermonde of the checkerboard set is, up to sign,
       prod(differences) * (g0 - g1 + g2 - g3)          [even family]
     so over any field it vanishes on the hyperplane g0+g2 = g1+g3 (which no strictly decreasing
     real sequence meets, since g0>g1, g2>g3).  -> HS is NOT a characteristic-free statement:
     the real proof uses the order (alternation / positivity).
 (2) m=3: the extra (non-difference) factor(s) of the determinant.
 (3) over F_p, random labelled distinct nodes: fraction of unisolvent checkerboard sets ~ 1 - O(m^2/p),
     while Chebyshev/Dickson-type labelled nodes (finite-field Padua) are always unisolvent.
 (4) the non-difference factor equals (up to a constant) a product of the 'alternation' Hankel
     determinants of X and Y (moments mu_k = sum_n (-1)^n h_n^k / omega'(h_n)): tested numerically
     over F_p by comparing zero sets.
Run: python3 -I hs_ff.py
"""
import sys, os, random, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ffield import rank_mod_p, det_mod_p, is_prime

def checker(X, Y, par=0):
    return [(x, y) for i, x in enumerate(X) for j, y in enumerate(Y) if (i + j) % 2 == par]

def monos(m): return [(a, d - a) for d in range(m + 1) for a in range(d, -1, -1)]

def vander(pts, m, p=None):
    if p is None: return [[x**a * y**b for a, b in monos(m)] for x, y in pts]
    return [[pow(x, a, p) * pow(y, b, p) % p for a, b in monos(m)] for x, y in pts]

def alt_hankel_dets(H, p):
    """leading principal minors 1..len(H)-1 of the alternation moment matrix on nodes H mod p."""
    L = len(H)
    w = []
    for n_, h in enumerate(H):
        d = 1
        for l, g in enumerate(H):
            if l != n_: d = d * (h - g) % p
        w.append((-1)**n_ * pow(d, p - 2, p) % p)
    mu = [sum(wi * pow(h, k, p) for wi, h in zip(w, H)) % p for k in range(2 * L)]
    return [det_mod_p([[mu[i + j] for j in range(r)] for i in range(r)], p) for r in range(1, L)]

def symbolic():
    import sympy as sp
    # m = 2: fully symbolic (Bareiss)
    h = sp.symbols('h0:3'); g = sp.symbols('g0:4')
    for par in (0, 1):
        d = sp.factor(sp.Matrix(vander(checker(h, g, par), 2)).det(method='bareiss'))
        print(f"m=2 parity={par}: det = {d}")
    # m = 3: everything numeric except the last y-node t; extra root is X-independent
    t = sp.symbols('t')
    for X in ([0, 1, 3, 7], [2, -5, 11, 4], [0, 1, 2, 3]):
        d = sp.factor(sp.Matrix(vander(checker(X, [0, 2, 5, 9, t], 0), 3)).det(method='bareiss'))
        print(f"m=3 X={X}, Y=[0,2,5,9,t]: det = {d}")
    print("   (t=8 is exactly where mu_0(Y) = sum_n (-1)^n/omega_Y'(g_n) vanishes, i.e. the first alternation Hankel minor of Y)")

def random_labelings(p, m, trials, rng):
    good = agree = 0
    for _ in range(trials):
        vals = rng.sample(range(p), 2 * m + 3)
        X, Y = vals[:m + 1], vals[m + 1:]
        qd = all(alt_hankel_dets(X, p)) and all(alt_hankel_dets(Y, p))
        for par in (0, 1):
            u = rank_mod_p(vander(checker(X, Y, par), m, p), p) == (m + 1) * (m + 2) // 2
            good += u; agree += (u == qd)
    return good / (2 * trials), agree / (2 * trials)

def mu0(H, p):
    s = 0
    for n_, h in enumerate(H):
        d = 1
        for l, g in enumerate(H):
            if l != n_: d = d * (h - g) % p
        s += (-1)**n_ * pow(d, p - 2, p)
    return s % p

if __name__ == '__main__':
    try:
        symbolic()
    except ImportError:
        print("(sympy not installed: skipping symbolic part)")
    p = 101
    print("F_101 counterexample m=2: X=(0,1,2), Y=(0,1,3,2) (g0+g2=g1+g3): rank",
          rank_mod_p(vander(checker([0, 1, 2], [0, 1, 3, 2]), 2, p), p), "of 6")
    print("Chebyshev/Dickson-labelled nodes: see padua_ff.py (always unisolvent when p does not divide 2n(n+1))")
    rng = random.Random(1)
    for p in (13, 31, 101):
        for m in (2, 3, 4, 5, 6):
            if 2 * m + 3 > p: continue
            fr, ag = random_labelings(p, m, 600, rng)
            print(f"p={p:4d} m={m}: unisolvent fraction {fr:.3f};  [unisolvent <=> alternation functionals on X and Y"
                  f" quasi-definite]: agreement {ag:.4f}")
