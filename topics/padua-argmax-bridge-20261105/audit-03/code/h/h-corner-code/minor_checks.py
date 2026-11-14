# Auditor checks: H04 (9) second-derivative majorant coefficients; H01 (5) finite psi' identity.
import sympy as sp, mpmath as mp
t,k=sp.symbols('t k',positive=True)
g=t**2/(4*k**2-t**2)
print("g''(t) =", sp.factor(sp.diff(g,t,2)))
# majorant with 4k^2-t^2>=3k^2, t<=1:  (4/pi)*8k^2(4k^2+3)/(27k^6)
maj=sp.expand(sp.Rational(4,1)*8*k**2*(4*k**2+3)/(27*k**6))
print("(4)*8k^2(4k^2+3)/(27k^6) =", maj, " ; as (8)*[...]:", sp.expand(maj/8))
mp.mp.dps=40
for R in (1,2,5,17):
    lhs=mp.fsum(mp.psi(1,r+mp.mpf(1)/2) for r in range(1,R+1))
    rhs=(R+mp.mpf(1)/2)*mp.psi(1,R+mp.mpf(1)/2)+mp.psi(0,R+mp.mpf(1)/2)-mp.psi(0,mp.mpf(1)/2)-mp.psi(1,mp.mpf(1)/2)/2
    print("H01(5) R=",R," diff",mp.nstr(lhs-rhs,3))
