import mpmath as mp
mp.mp.dps = 30
pi = mp.pi; g_ = mp.euler
bad = [s for s in [mp.mpf(k)/1000 for k in range(1001)] if not mp.cos(pi*s/2) >= mp.mpf(3)/4*(1-s**2)]
print('failures of cos(pi s/2)>=3/4(1-s^2):', [(mp.nstr(s,5), mp.nstr(mp.cos(pi*s/2)-mp.mpf(3)/4*(1-s**2),5)) for s in bad])
def Cc(t): return -mp.digamma(t)-mp.digamma(1-t)
k0 = 2*g_+4*mp.log(2)-2*mp.log(pi)
f0 = k0/pi
def f(w):
    w = mp.mpf(w); w = (w+pi) % (2*pi) - pi
    return f0*mp.cos(w/2) + 2*mp.quad(lambda t: (mp.cos(w*t)-mp.cos(w/2))/mp.cos(pi*t), [0, 0.5])
def g(w):
    w = mp.mpf(w); w = (w+pi) % (2*pi) - pi
    return -f0/4*mp.cos(w/2) + 2*mp.quad(lambda t: (-t**2*mp.cos(w*t)+mp.cos(w/2)/4)/mp.cos(pi*t), [0, 0.5])
lam0 = 2/pi*mp.log(4/pi); J0 = 2*(mp.log(pi)-g_)/pi
def W(t): t = abs(t); return mp.quad(lambda s: mp.log(mp.cot(s/4)), [t, pi])
def H(w):
    w = mp.mpf(w)
    return lam0*f(w) + mp.quad(lambda t: (f(w+t)+f(w-t)-2*f(w))/(2*mp.sin(t/2)), [0, pi-w, pi])/pi
mp.mp.dps = 20
w = mp.mpf(1)
Hrep = lam0*f(w) + mp.quad(lambda t: W(t)*g(w+t), [-pi, 0, pi-w, pi])/pi - J0/pi*W(pi-w)
print('W-rep', mp.nstr(Hrep, 12), ' direct', mp.nstr(H(w), 12))
