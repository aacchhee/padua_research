"""Cross-check of E06 identity H0=kappa/2+(2k0/pi^2)log(2/pi) against PD-T271's kappa enclosure,
using direct high-precision quadrature of H(0) (numerical, not interval-certified)."""
import mpmath as mp
mp.mp.dps = 40
pi = mp.pi; g = mp.euler
def f(x):
    x = abs(mp.mpf(x))
    if x == pi: return mp.mpf(1)
    u = x/(2*pi)
    return mp.cos(x/2)/pi*(-mp.digamma(mp.mpf(1)/2+u)-mp.digamma(mp.mpf(1)/2-u)-2*mp.log(pi))
lam0 = (2/pi)*mp.log(4/pi); f0 = f(0)
H0 = lam0*f0 + mp.quad(lambda v: (f(v)-f0)/mp.sin(v/2), [0, pi/2, pi])/pi
k0 = 2*g+4*mp.log(2)-2*mp.log(pi)
kap = 2*(H0-(2*k0/pi**2)*mp.log(2/pi))
cst = (4/pi**2)*(g+mp.log(8/pi))**2 + kap
print("H0 =", mp.nstr(H0, 32))
print("kappa implied by E06(11) =", mp.nstr(kap, 32))
print("PD-T271 kappa enclosure  = (0.919710118388492535099518225790, ...791)")
print("inside:", mp.mpf('0.919710118388492535099518225790') < kap < mp.mpf('0.919710118388492535099518225791'))
print("Cstar implied =", mp.nstr(cst, 32), " inside PD-T271 c enclosure:", mp.mpf('1.846160310423926079759838737947') < cst < mp.mpf('1.846160310423926079759838737948'))
print("H(pi) direct vs (2/pi)log(2/pi):", mp.nstr(lam0*1 + mp.quad(lambda v: (2*f(pi-v)-2)/(2*mp.sin(v/2)), [0, pi/2, pi])/pi, 25), mp.nstr((2/pi)*mp.log(2/pi), 25))
