# Auditor's independent constant chain (MEASURED quadrature/series): from H01's structure,
#   C_M = int_0^1 R + a*gamma_1 + a*c0*gamma   (C_K = Stieltjes gamma_1, auditor derivation)
#   C_H = 2a*C_M + 2a^2*S_e - a^2*d^2,   kappa_chain = -1 + C_H + C_B.
# Compare with kappa from PD-T271's enclosure: tests that the H constant is kappa without PD-T269.
import mpmath as mp
mp.mp.dps = 40
pi=mp.pi; a=2/pi; g=mp.euler; c0=g+2*mp.log(2); d=g+mp.log(8/pi)
w=lambda x: mp.cot(pi*x/2)
def R(x):
    F=mp.log(x)+mp.log(1-x)-mp.psi(0,(1-x)/2)
    return w(x)*F - a*(mp.log(x)+c0)/x
with mp.workdps(80):
    IR=mp.quad(R,[0,mp.mpf(1)/2,1],method='tanh-sinh')
    IR2=mp.quad(R,[0,mp.mpf(1)/4,mp.mpf(1)/2,mp.mpf(3)/4,1],method='gauss-legendre')
print("int R (tanh-sinh)", mp.nstr(IR,30), " GL diff", mp.nstr(IR-IR2,3))
g1=mp.stieltjes(1)
# C_K check: sum_{r<m} log r/r - log^2 m/2 + log m/(2m) at m=10^6 via EM-free direct formula
Se=mp.nsum(lambda r: (mp.psi(0,r+mp.mpf(1)/2)-mp.log(r))/r,[1,mp.inf])
CM=IR+a*g1+a*c0*g
CH=2*a*CM+2*a**2*Se-a**2*d**2
CB=mp.mpf('0.3378987116946137090474372026405455')
kap_chain=-1+CH+CB
kap=(mp.mpf('0.919710118388492535099518225790')+mp.mpf('0.919710118388492535099518225791'))/2
print("gamma_1",mp.nstr(g1,25)," S_e",mp.nstr(Se,25))
print("C_M",mp.nstr(CM,25)," C_H",mp.nstr(CH,25))
print("kappa_chain=-1+C_H+C_B", mp.nstr(kap_chain,30), "  kappa(PD-T271)", mp.nstr(kap,30), " diff", mp.nstr(kap_chain-kap,3))
