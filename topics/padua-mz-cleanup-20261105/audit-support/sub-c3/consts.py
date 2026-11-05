from mpmath import mp, mpf, log, quad, sin, cos, inf, pi, quadosc, nsum
mp.dps = 40
def xlog(x):
    x = abs(x)
    return mpf(0) if x == 0 else x**2*log(x)
def C(q):
    q = mpf(q)
    return 3*xlog(q) - 2*xlog(q+1) - 2*xlog(q-1) + (xlog(q+2)+xlog(q-2))/2
A = 4*log(2)
def Jm(a):
    q = 1/mpf(a); return (A + C(q))/2
def Jp(a):
    q = 1/mpf(a); return (A - C(q) - C(2) + (C(q+2)+C(q-2))/2)/4
cm = 1/(9*A*Jm(mpf(1)/4)); cp = 1/(36*A*Jp(mpf(1)/8))
print('A', A); print('C(0)', C(0))
print('Jm(1/4)', Jm(mpf(1)/4)); print('Jp(1/8)', Jp(mpf(1)/8))
print('A*Jm', A*Jm(mpf(1)/4)); print('A*Jp', A*Jp(mpf(1)/8))
print('c_-', cm); print('c_+', cp)
# direct quadrature of the integrals (7), independent of the cosine transform
def ug(u):
    if u == 0: return mpf(0)
    return u*(sin(u/2)/(u/2))**4
def direct(f):
    # integrate on [0, 2000] piecewise + tail via asymptotic (|ug|<=16/u^3, tail < 8/2000^2 ~ 2e-6)
    # use many pieces of length pi for accuracy; tail handled by quadosc
    return quad(lambda u: ug(u)*f(u), [0]+[k*pi for k in range(1,400)]) + quadosc(lambda u: ug(u)*f(u), [399*pi, inf], omega=1)
mp.dps = 20
print('direct A', direct(lambda u: 1))
print('direct Jm(1/4)', direct(lambda u: cos(2*u)**2))
print('direct Jp(1/8)', direct(lambda u: sin(4*u)**2*sin(u)**2))
for q in [0, 0.5, 1, 2, 3.7]:
    print('C(%s)'%q, C(q), direct(lambda u: cos(q*u)))
