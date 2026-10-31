"""The 'quadratic' Padua set of F_q, q = 2n+1 an odd prime (smallest admissible field for degree n).

For q = 2n+1:  2n = q-1 (x-axis split, zeta generates F_q^*) and 2(n+1) = q+1 (y-axis non-split,
eta generates the norm-1 torus mu_{q+1} in F_{q^2}).  Claim (verified below):
   X = {x in F_q : chi(x^2-1) != -1}   (n+1 elements),   Y = {y in F_q : chi(y^2-1) != +1}  (n+2 elements),
   X u Y = F_q,  X n Y = {+1,-1},
   Pad_n(F_q) = {(x,y) in X x Y : eps(x) = del(y)},
        eps(x) = chi(2(x+1)) (x != -1), eps(-1) = chi(-1);   del(y) = chi(2(y+1)) (y != -1), del(-1) = -chi(-1),
   i.e. for x, y != -1 the parity condition j+k even is  chi((x+1)(y+1)) = 1.
   |Pad_n(F_q)| = (q+1)(q+3)/8 = dim P_{(q-1)/2}, unisolvent, with the cubature/fast transform of padua_ff.py.
Run: python3 -I quadratic_padua.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ffield import is_prime, legendre as chi
from padua_ff import PaduaFF

ok_all = True
for q in [p for p in range(5, 48) if is_prime(p)]:
    n = (q - 1) // 2
    P = PaduaFF(n, q); R = P.check_all()
    assert R['type'] == (1, -1)
    X = {x for x in range(q) if chi(x * x - 1, q) != -1}
    Y = {y for y in range(q) if chi(y * y - 1, q) != 1}
    eps = lambda x: chi(-1, q) if x == q - 1 else chi(2 * (x + 1), q)
    dl = lambda y: -chi(-1, q) if y == q - 1 else chi(2 * (y + 1), q)
    S = {(x, y) for x in X for y in Y if eps(x) == dl(y)}
    par_x = all((j % 2 == 0) == (eps(x) == 1) for j, x in enumerate(P.xs))
    par_y = all((k % 2 == 0) == (dl(y) == 1) for k, y in enumerate(P.ys))
    good = (set(P.xs) == X and set(P.ys) == Y and X | Y == set(range(q)) and X & Y == {1, q - 1}
            and par_x and par_y and S == set(P.pts) and R['rank_cheb'] == len(S) == (q + 1) * (q + 3) // 8
            and R['gram_is_D'])
    ok_all &= good
    print(f"q={q:3d} n={n:2d} |Pad|={len(S):4d} = (q+1)(q+3)/8: {len(S)==(q+1)*(q+3)//8}; character description "
          f"matches: {S == set(P.pts)}; unisolvent: {R['rank_cheb'] == len(S)}; fraction of plane {len(S)/q**2:.3f}")
print("ALL OK" if ok_all else "FAIL")
