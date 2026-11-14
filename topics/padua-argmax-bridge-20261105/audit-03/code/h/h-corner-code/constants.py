# Auditor numerical evaluation (MEASURED) of the H01/H04 constants and identities.
import mpmath as mp
mp.mp.dps = 45
pi = mp.pi; a = 2/pi; g = mp.euler; d = g + mp.log(8/pi)
w = lambda x: mp.cot(pi*x/2)
def B(x):
    return mp.cot(pi*x) - 1/(pi*x) + 1/(pi*(1-x))
def G(x):
    return mp.log(mp.sin(pi*x)/(pi*x*(1-x)))/pi
def Q(f):
    with mp.workdps(90):
        v1 = mp.quad(f, [0, mp.mpf(1)/4, mp.mpf(1)/2, mp.mpf(3)/4, 1], method='gauss-legendre')
    return v1
def Q2(f):
    with mp.workdps(90):
        v2 = mp.quad(f, [0, mp.mpf(1)/2, 1], method='tanh-sinh')
    return v2
I1 = Q(lambda x: w(x)/(1-x) - a/x)
I2 = Q(lambda x: x*w(x))
IB = Q(lambda x: x*w(x)*B(x))
CB = 4*Q(lambda x: w(x)*G(x))
print("I1 ", mp.nstr(I1, 35), " tanh-sinh diff", mp.nstr(I1-Q2(lambda x: w(x)/(1-x) - a/x), 3))
print("I2 ", mp.nstr(I2, 35))
print("IB ", mp.nstr(IB, 35), " tanh-sinh diff", mp.nstr(IB-Q2(lambda x: x*w(x)*B(x)), 3))
print("CB ", mp.nstr(CB, 35))
lhs = 2*IB - a*I1; rhs = a**2 - 1 + a**2*mp.log(pi/2)
print("identity(6): 2IB-a I1 =", mp.nstr(lhs, 35), " rhs", mp.nstr(rhs, 35), " diff", mp.nstr(lhs-rhs, 3))
betaB = -a**2 + 2*IB + a*I2
betaH = -2 - a**2*(g + 2*mp.log(2)) - a*(I1+I2)
print("betaB", mp.nstr(betaB, 30)); print("betaH", mp.nstr(betaH, 30))
print("2+betaH+betaB", mp.nstr(2+betaH+betaB, 30), " -1-a^2 d", mp.nstr(-1-a**2*d, 30))
Su = mp.nsum(lambda r: mp.psi(1, r+mp.mpf(1)/2) - 1/r, [1, mp.inf])
print("S_u", mp.nstr(Su, 30), " claimed", mp.nstr(1+2*mp.log(2)-pi**2/4, 30))
# kappa via PD-T269 integral, digamma form derived by auditor:
# sum_{l odd} t^2/(l(l^2-t^2)) = (1/4)[2psi(1/2)-psi((1-t)/2)-psi((1+t)/2)]
kap = Q(lambda t: (2/pi)*mp.cot(pi*t/2)*(2*mp.psi(0, mp.mpf(1)/2) - mp.psi(0, (1-t)/2) - mp.psi(0, (1+t)/2)))
print("kappa(integral)", mp.nstr(kap, 35))
lo = mp.mpf('0.919710118388492535099518225790'); hi = mp.mpf('0.919710118388492535099518225791')
print("  inside PD-T271 enclosure:", lo < kap < hi)
c1 = a*d; c = c1**2 + kap
print("c1", mp.nstr(c1, 30), " b=2ac1", mp.nstr(2*a*c1, 30), " c=c1^2+kappa", mp.nstr(c, 32))
print("C_H implied = kappa+1-C_B", mp.nstr(kap + 1 - CB, 30))
