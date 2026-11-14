"""Numeric check (MEASURED, mpmath 30 digits) of Delta_2 = E_inf - E_2 =
sum_{j>=2} {Xi_j(t)+Xi_{j+1}(-t)} and the partial-fraction formula for ell_j."""
import mpmath as mp
mp.mp.dps = 30
pi = mp.pi
def C(t): return -mp.digamma(t) - mp.digamma(1-t)
def Phi(t): return mp.sin(pi*t)/pi*(C(t) - 2*mp.log(pi))
def f(w): return Phi(mp.mpf(1)/2 + w/(2*pi))
def h(j,t): return -mp.log(j+t-mp.mpf(1)/2) + mp.nsum(lambda k: 1/(k+t) - mp.log((k+t+mp.mpf(1)/2)/(k+t-mp.mpf(1)/2)), [j, mp.inf])
def g(j,t): return -mp.log(j+t-mp.mpf(1)/2)**2/2 + mp.nsum(lambda k: mp.log(k+t)/(k+t) - (mp.log(k+t+mp.mpf(1)/2)**2 - mp.log(k+t-mp.mpf(1)/2)**2)/2, [j, mp.inf])
worst = 0; worst_l = 0
for (x,y) in [(mp.mpf('0.3'),mp.mpf('0.2')),(mp.mpf('1.1'),mp.mpf('0.7')),(mp.mpf('0.05'),mp.mpf('1.9')),(mp.mpf('2.0'),mp.mpf('0.4'))]:
    ce, cd = mp.cos((x+y)/2), mp.cos((x-y)/2); a = ce*cd
    t = y/pi
    td = mp.mpf(1)/2 + (x-y)/(2*pi); te = mp.mpf(1)/2 + (x+y)/(2*pi)
    U0 = ce*f(x-y) + cd*f(x+y); B0 = 4*a/pi**2; D0 = U0/pi + B0*mp.log(pi)
    D0alt = a*(C(td)+C(te))/pi**2
    def ell(r,b):
        w = r*pi + b
        return mp.sin(b)/w + 8*a*mp.fsum(1/(w**2 - (j*pi+x)**2) for j in range(-r+1, r, 2))
    def ell_psi(r,b):
        s = b/pi; qp = (1+s+x/pi)/2; qm = (1+s-x/pi)/2
        return (D0 + 2*a/pi**2*(mp.digamma(r+qm)+mp.digamma(r+qp)))/(r+s)
    for r in (1,2,3,5,9):
        for b in (y,-y):
            worst_l = max(worst_l, abs(ell(r,b)-ell_psi(r,b)))
    C2 = mp.sinc(y) if y else 1
    C2 = mp.sin(y)/y + ell(1,y) + ell(1,-y) + ell(2,-y)
    H2 = h(2,t)+h(2,1-t); Q2 = g(2,t)+g(2,1-t)
    E2 = C2 + D0*H2 + B0*Q2
    Einf = a/3 + a/pi**2*C(td)*C(te)
    def Xi(j,s):
        qp = (1+s+x/pi)/2; qm = (1+s-x/pi)/2; nu = j+s
        return 2*a/(pi**2*nu)*(mp.digamma(j+qp)+mp.digamma(j+qm)-2*mp.log(nu))
    D2 = mp.nsum(lambda j: Xi(j,t)+Xi(j+1,-t), [2, mp.inf])
    print(f"x={float(x)}, y={float(y)}: D0-D0alt={float(D0-D0alt):.2e}  Einf-E2={float(Einf-E2):.12f}  sumXi={float(D2):.12f}  diff={float(Einf-E2-D2):.2e}")
    worst = max(worst, abs(Einf-E2-D2))
print("max |E_inf-E_2-Delta_2| =", float(worst), "; max |ell_j finite - psi formula| =", float(worst_l))
