# C2A audit: scalar profile f, Lemma uc:scalar-maximum, and the companion's added
# derivations (Q bounds, derivative table, sine inequality, f-integral, f''' sign, H finite part).
import mpmath as mp
from fractions import Fraction as Fr
mp.mp.dps = 25
pi = mp.pi; g_ = mp.euler
def Cc(t): return -mp.digamma(t)-mp.digamma(1-t)
def Phi(t):
    t = t - mp.floor(t)
    if t == 0: return mp.mpf(1)
    return mp.sin(pi*t)/pi*(Cc(t)-2*mp.log(pi))
def f(w): return Phi(mp.mpf(1)/2 + w/(2*pi))
k0 = 2*g_+4*mp.log(2)-2*mp.log(pi)
print('C0 check', mp.nstr(Cc(mp.mpf(1)/2), 15), mp.nstr(2*g_+4*mp.log(2), 15))
print('k0 =', mp.nstr(k0, 12), ' f(0)=', mp.nstr(f(0), 12), ' k0/pi=', mp.nstr(k0/pi, 12))
# f-series
def fser(w):
    return mp.cos(w/2)/pi*(k0 + 4*w**2*mp.nsum(lambda j: 1/((2*j+1)*((2*j+1)**2*pi**2-w**2)), [0, mp.inf]))
for w in [0.3, 1.7, 3.0]:
    print('f-series', w, mp.nstr(f(w)-fser(w), 5))
# grid bounds on (-pi,pi): f, f', f'', f'''
N = 400
ws = [-pi + 2*pi*(k+0.5)/N for k in range(N)]
fv = [f(w) for w in ws]
d1 = [mp.diff(f, w, 1) for w in ws]
d2 = [mp.diff(f, w, 2) for w in ws]
d3 = [mp.diff(f, w, 3) for w in ws]
print('min f', mp.nstr(min(fv), 10), 'max f', mp.nstr(max(fv), 10), 'f(pi)=', mp.nstr(f(pi), 10))
print('max|f\'|', mp.nstr(max(abs(z) for z in d1), 8), ' 6/pi=', mp.nstr(6/pi, 6))
print('max|g|', mp.nstr(max(abs(z) for z in d2), 8), ' max g', mp.nstr(max(d2), 8), ' 3/pi^2=', mp.nstr(3/pi**2, 6))
print('max|f\'\'\'|', mp.nstr(max(abs(z) for z in d3), 8), ' 13/20=0.65')
print('f\'\'\' sign on (0,pi): max f\'\'\'/sin(w/2) for w>0 =', mp.nstr(max(d3[k]/mp.sin(ws[k]/2) for k in range(N) if ws[k] > 0), 8), ' claimed bound -311/71680=', mp.nstr(mp.mpf(-311)/71680, 6))
# jump J0 of f' at pi
eps = mp.mpf('1e-12')
jl = mp.diff(f, pi-mp.mpf('1e-6')); jr = mp.diff(f, -pi+mp.mpf('1e-6'))
J0 = 2*(mp.log(pi)-g_)/pi
print('f\'(pi-)=', mp.nstr(jl, 8), ' f\'(pi+)=f\'(-pi+)=', mp.nstr(jr, 8), ' jump=', mp.nstr(jr-jl, 8), ' -J0=', mp.nstr(-J0, 8), ' J0>1/pi', J0 > 1/pi)
# variation of f' on circle: int |g| + J0
var = mp.quad(lambda w: abs(mp.diff(f, w, 2)), [-pi, 0, pi]) + J0
print('Var_per f\' =', mp.nstr(var, 8), ' (<4 claimed; 12/pi=', mp.nstr(12/pi, 6), ')')
# f-integral formula
def fint(w):
    return f(0)*mp.cos(w/2) + 2*mp.quad(lambda t: (mp.cos(w*t)-mp.cos(w/2))/mp.cos(pi*t), [0, 0.5])
for w in [0.5, 2.0, pi]:
    print('f-integral', mp.nstr(w, 4), mp.nstr(f(w)-fint(w), 5))
# cosine moment formula
for j in [0, 1, 3]:
    for w in [0.7, 2.5]:
        w = mp.mpf(w)
        lhs = mp.quad(lambda t: (mp.cos(w*t)-mp.cos(w/2))*mp.cos((2*j+1)*pi*t), [0, 0.5])
        rhs = (-1)**j*mp.cos(w/2)*w**2/((2*j+1)*pi*((2*j+1)**2*pi**2-w**2))
        print('moment j=%d w=%s' % (j, w), mp.nstr(lhs-rhs, 5))
# Abel kernel
for r in [0.3, 0.9]:
    for t in [0.1, 0.4]:
        r = mp.mpf(r); t = mp.mpf(t)
        s = mp.nsum(lambda j: (-1)**int(j)*r**(2*j+1)*mp.cos((2*j+1)*pi*t), [0, mp.inf])
        cf = r*(1+r**2)*mp.cos(pi*t)/((1-r**2)**2+4*r**2*mp.cos(pi*t)**2)
        print('Abel', mp.nstr(s-cf, 5), ' bound 5/(8cos) holds (r>=1/2):', (r < 0.5) or abs(cf) <= 5/(8*mp.cos(pi*t)))
# f''' formula
def f3int(w):
    return f(0)/8*mp.sin(w/2) + 2*mp.quad(lambda t: (t**3*mp.sin(t*w)-mp.sin(w/2)/8)/mp.cos(pi*t), [0, 0.5])
for w in [0.4, 1.9, 3.0]:
    print('f\'\'\' formula', w, mp.nstr(f3int(mp.mpf(w)) - mp.diff(f, mp.mpf(w), 3), 5))
# Q bounds on (0,1/2]
def Q(t): return Cc(t)-1/t-2*g_
ts = [mp.mpf(k)/400 for k in range(1, 201)]
print('Q<=4t^2:', all(Q(t) <= 4*t**2 for t in ts), " Q'<=5t/(1-t^2)^2:", all(mp.diff(Q, t) <= 5*t/(1-t**2)**2 for t in ts))
print("max Q''", mp.nstr(max(mp.diff(Q, t, 2) for t in ts), 10), ' 28zeta3-16=', mp.nstr(28*mp.zeta(3)-16, 10))
# T'' bounds
T = lambda t: mp.sinc(pi*t)
print("max T'' on (0,1/2]", mp.nstr(max(mp.diff(T, t, 2) for t in ts), 8), ' claimed <= -pi^2(1/3-pi^2/40)=', mp.nstr(-pi**2*(mp.mpf(1)/3-pi**2/40), 8), ' -pi^2/12=', mp.nstr(-pi**2/12, 6))
print("max |T''|", mp.nstr(max(abs(mp.diff(T, t, 2)) for t in ts), 8), " max|T'|", mp.nstr(max(abs(mp.diff(T, t, 1)) for t in ts), 8))
# Phi'' max on (0,1/2]
print("max Phi'' on (0,1/2]", mp.nstr(max(mp.diff(Phi, t, 2) for t in ts[:-1]), 8), ' (<12 claimed)', "  max|Phi''|", mp.nstr(max(abs(mp.diff(Phi, t, 2)) for t in ts[:-1]), 8), ' (<35)')
print("max|Phi'|", mp.nstr(max(abs(mp.diff(Phi, t, 1)) for t in ts[:-1]), 8), ' (<11)')
# sine inequality c_s >= (3/4)(1-s^2)
print('cos(pi s/2) >= 3/4(1-s^2):', all(mp.cos(pi*s/2) >= mp.mpf(3)/4*(1-s**2) for s in [mp.mpf(k)/1000 for k in range(1001)]), " h'(0)=pi/2-3/2=", mp.nstr(pi/2-1.5, 5))
# polynomial inequalities
print('t(1/2-t)/(1-t^2)^2 max on [0,1/2]', mp.nstr(max(t*(0.5-t)/(1-t**2)**2 for t in ts), 8), ' 3/40=0.075')
# rational checks
print('2822/81', Fr(10, 3)+10+Fr(608, 81)+Fr(32, 3)+Fr(10, 3), float(Fr(2822, 81)))
print('608/27', Fr(64, 9)*Fr(3, 2)+Fr(256, 27)*Fr(5, 4))
print('-311/71680', Fr(3, 40)+Fr(44, 35*1024)-Fr(1, 16)-Fr(37, 2048))
print('Phi\'\' upper', mp.nstr(-pi**2/12+2*pi+19/pi, 8))
# lambda0, H finite part
lam0 = 2/pi*mp.log(4/pi)
print('lambda0', mp.nstr(lam0, 8), ' 1/(2pi)=', mp.nstr(1/(2*pi), 8))
def H(w):
    w = mp.mpf(w)
    return lam0*f(w) + mp.quad(lambda t: (f(w+t)+f(w-t)-2*f(w))/(2*mp.sin(t/2)), [0, pi/2, pi])/pi
def H_def(w, eps):
    w = mp.mpf(w)
    return (mp.quad(lambda t: f(w+t)/(2*mp.sin(t/2)), [eps, pi, 2*pi-eps]) + 2*f(w)*mp.log(eps/pi))/pi
H0 = H(0)
print('H0 =', mp.nstr(H0, 12), ' H_def(0,1e-6)=', mp.nstr(H_def(0, mp.mpf('1e-6')), 12))
mx = -1
for k in range(1, 41):
    w = pi*k/40
    d = H(w)-H0
    bnd = -(pi-3)*w**2/(4*pi**3)
    if d > bnd + 1e-15: print('H bound violated', w, d, bnd)
    mx = max(mx, d)
print('max H(w)-H0 over grid', mp.nstr(mx, 8))
# W representation at w=1
def W(t): t = abs(t); return mp.quad(lambda s: mp.log(mp.cot(s/4)), [t, pi])
def g(w): return mp.diff(f, w, 2)
w = mp.mpf(1)
Hrep = lam0*f(w) + mp.quad(lambda t: W(t)*g(w+t), [-pi, -pi+0, pi-w, pi])/pi - J0/pi*W(pi-abs(w))
print('W-representation at w=1:', mp.nstr(Hrep, 10), ' direct', mp.nstr(H(w), 10))
print('W(pi-w)>=w^2/4:', all(W(pi-w) >= w**2/4 for w in [pi*k/20 for k in range(21)]))
