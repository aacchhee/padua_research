"""Check the missing beta factors in T201's F8 remark, not Theorem A.

Exact formula: with Gram(Qw)=I+[[0,t],[t,0]], a=q1+t^2*e3,
three exact CGS passes leave r3=-t^3*q2+t^2*e3. Thus beta~t^2,
local overlap~t and full Gram Frobenius error~2t. Set t=sqrt(u)/4.
This demonstrates why an O(u) remainder before normalization cannot be
relabelled O(u) after normalization without retaining the beta factor.
The formulas are derived on paper; 100-digit evaluation is verification.
"""
import json
import mpmath as mp

mp.mp.dps = 100
for exponent in [40, 60, 80]:
    u = mp.mpf(2) ** (-exponent)
    t = mp.sqrt(u) / 4
    Q = mp.matrix([[1, t], [0, mp.sqrt(1-t*t)], [0, 0]])
    a = mp.matrix([1, 0, t*t])
    r = a.copy()
    hs = []
    for _ in range(3):
        h = Q.T * r
        hs.append(h)
        r -= Q * h
    expected = -t**3 * Q[:, 1] + mp.matrix([0, 0, t*t])
    beta = mp.norm(r)
    new = r / beta
    Qall = mp.matrix([[Q[i, 0], Q[i, 1], new[i]] for i in range(3)])
    Omega = Qall.T * Qall - mp.eye(3)
    eta = mp.norm(Omega)
    local = mp.norm(Q.T * new)
    print(json.dumps(dict(exponent=exponent, eta_over_sqrtu=float(eta/mp.sqrt(u)),
                          beta=float(beta), local=float(local),
                          local_over_eta_cubed_plus_u=float(local/(eta**3+u)),
                          normalized_eta_cubed_h1_bound=float(eta**3*mp.norm(hs[0])/beta),
                          exact_formula_residual=float(mp.norm(r-expected)))), flush=True)
    assert eta <= mp.sqrt(u)
    assert mp.norm(r-expected) < mp.mpf('1e-90')
