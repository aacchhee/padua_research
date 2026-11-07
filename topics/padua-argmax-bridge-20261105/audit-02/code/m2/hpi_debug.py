import mpmath as mp
mp.mp.dps = 30
pi = mp.pi
def f(x):
    x = abs(mp.mpf(x))
    if x == pi: return mp.mpf(1)
    u = x/(2*pi)
    return mp.cos(x/2)/pi*(-mp.digamma(mp.mpf(1)/2+u)-mp.digamma(mp.mpf(1)/2-u)-2*mp.log(pi))
lam0 = (2/pi)*mp.log(4/pi)
ig = lambda v: (f(pi-v)-1)/mp.sin(v/2)
for pts in ([0, pi], [0, pi/2, pi], [0, pi/8, pi/4, pi/2, 3*pi/4, pi]):
    print(len(pts), mp.nstr(lam0 + mp.quad(ig, pts)/pi, 20), mp.nstr(lam0 + mp.quad(ig, pts, method='gauss-legendre')/pi, 20))
print("target", mp.nstr((2/pi)*mp.log(2/pi), 20))
print("integrand samples", [mp.nstr(ig(mp.mpf(v)), 10) for v in ['1e-10', '0.5', '1.5', '3.0', '3.14159']])
