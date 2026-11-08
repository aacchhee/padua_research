"""C4A follow-up: the three tolerance-limited checks of check_c4a.py, with explicit reasoning."""
import mpmath as mp
mp.mp.dps = 40
pi = mp.pi; a = 2/pi; gam = mp.euler; d = gam + mp.log(8/pi)
w_ = lambda x: mp.cot(pi*x/2)
B_ = lambda x: mp.cot(pi*x) - 1/(pi*x) + 1/(pi*(1-x))
for x in ('1e-8', '1e-12'):
    x = mp.mpf(x)
    print("B(%s)-1/pi = %s ; B(1-%s)+1/pi = %s" % (mp.nstr(x,3), mp.nstr(B_(x)-1/pi,5), mp.nstr(x,3), mp.nstr(B_(1-x)+1/pi,5)))
# (8)=(12) at dps 40
def eps_(j, n): return mp.mpf(1)/2 if j in (0, n) else mp.mpf(1)
def lam8(n):
    m = n+1; s = 0
    for j in range(n+1):
        for k in range(n+1):
            if (j+k) % 2:
                th, ph = j*pi/n, k*pi/m
                s += eps_(j, n)*eps_(k, m)*(1+mp.cos(ph))/abs(mp.cos(th)-mp.cos(ph))
    return 4*s/(n*m) + mp.mpf(1)/m
def lam12b(n):
    m = n+1; H = 0; V = 0
    for r in range(1, m):
        x = mp.mpf(r)/m; s_ = m-r; al = (1-x)/2
        H += w_(x)*(mp.digamma(r+al)+mp.digamma(s_-al)-mp.digamma(m-al)-mp.digamma(al))
        V += w_(x)*mp.fsum(B_((l+al)/n) for l in range(r))
    return -1 + mp.mpf(2)/m + 4*H/(pi*m) + 4*V/(n*m)
print("max |(8)-(12b)| n=2..12 at dps40:", mp.nstr(max(abs(lam8(n)-lam12b(n)) for n in range(2,13)),3))
# C_H Richardson with remainder model log m/m^2
I1 = mp.quad(lambda x: w_(x)/(1-x) - a/x, [0, 1]); I2 = mp.quad(lambda x: x*w_(x), [0, 1])
bH = -2 - a**2*(gam + 2*mp.log(2)) - a*(I1 + I2)
def CH(m):
    s = 0
    for r in range(1, m):
        x = mp.mpf(r)/m; s_ = m-r; al = (1-x)/2
        s += w_(x)*(mp.digamma(r+al)+mp.digamma(s_-al)-mp.digamma(m-al)-mp.digamma(al))
    return 4*s/(pi*m) - a**2*(mp.log(m)+d)**2 - (-a**2*mp.log(m)+bH)/m
m1, m2 = 400, 800
c1_, c2_ = CH(m1), CH(m2)
g1, g2 = mp.log(m1)/m1**2, mp.log(m2)/m2**2
CHx = c2_ - (c1_-c2_)*g2/(g1-g2)
CB = 4*mp.quad(lambda t: w_(t)*mp.quad(B_, [0, t]) if t > 0 else 0, [0, 1])
kap = mp.quad(lambda t: (8/pi)*t**2*mp.cot(pi*t/2)*mp.nsum(lambda j: 1/((2*j+1)*((2*j+1)**2-t**2)), [0, mp.inf]) if t > 0 else 0, [0, 0.5, 1])
print("C_H(400)=%s C_H(800)=%s extrapolated %s" % (mp.nstr(c1_,12), mp.nstr(c2_,12), mp.nstr(CHx,12)))
print("-1+C_H+C_B (extrap) = %s ; kappa = %s ; diff %s" % (mp.nstr(-1+CHx+CB,12), mp.nstr(kap,12), mp.nstr(-1+CHx+CB-kap,3)))
