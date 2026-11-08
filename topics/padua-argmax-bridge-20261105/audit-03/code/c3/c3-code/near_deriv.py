import mpmath as mp
mp.mp.dps=30
def T(n): L=mp.log(n); return (4*L**2-3*L)/mp.pi**2
def A4(n): H=1+mp.log(n); return 4/n+40*H/(mp.pi*n**2)
def JN(n): H=1+mp.log(n); return (mp.mpf(3)/2*H+mp.mpf(16)/5)/n+78/n**2
worst=mp.inf
for e in [mp.mpf(i)/50 for i in range(0,351)]:
    n=320*mp.e**e  # n from 320 to ~320*e^7
    for rho in (0,mp.mpf(1)/2):
        d=mp.diff(lambda t: T(t)+A4(t)+rho*JN(t), n)
        rhs=mp.mpf(45)/(16*n)-mp.mpf(184)/(15*n**2)-78/n**3
        worst=min(worst,(d-rhs)*n)
print("min over n in [320, 320e^7], rho in {0,1/2} of n*[(T+A4+rho J_N)' - (45/(16n)-184/(15n^2)-78/n^3)] =",mp.nstr(worst,6))
