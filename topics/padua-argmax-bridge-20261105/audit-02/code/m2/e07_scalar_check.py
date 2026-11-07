"""Independent numerical cross-check of E07 scalar claims (Claude audit2, m2).
NUMERICAL (mpmath, sampled) -- not a proof. Exact rational arithmetic via Fraction.
f(x)=cos(x/2)/pi*[-psi(1/2+x/2pi)-psi(1/2-x/2pi)-2log pi], |x|<pi, f(pi)=1 (derived [D]).
"""
import sys
from fractions import Fraction as F
import mpmath as mp

mp.mp.dps = 30
pi = mp.pi
g_ = mp.euler

def f(x):
    x = mp.mpf(x)
    # reduce to principal period, even
    x = mp.fmod(x, 2*pi)
    if x > pi: x = 2*pi - x
    if x < -pi: x = x + 2*pi
    x = abs(x)
    if x == pi:
        return mp.mpf(1)
    u = x/(2*pi)
    return mp.cos(x/2)/pi*(-mp.digamma(mp.mpf(1)/2+u) - mp.digamma(mp.mpf(1)/2-u) - 2*mp.log(pi))

f0 = f(0)
C0 = 2*g_ + 4*mp.log(2)
lam0 = (2/pi)*mp.log(4/pi)

def f_int(x):  # eq (9)
    x = mp.mpf(x)
    I = mp.quad(lambda t: (mp.cos(x*t)-mp.cos(x/2))/mp.cos(pi*t), [0, mp.mpf(1)/4, mp.mpf(1)/2])
    return f0*mp.cos(x/2) + 2*I

def f3_int(x):  # eq (10)
    x = mp.mpf(x)
    I = mp.quad(lambda t: (t**3*mp.sin(t*x)-mp.sin(x/2)/8)/mp.cos(pi*t), [0, mp.mpf(1)/4, mp.mpf(1)/2])
    return f0/8*mp.sin(x/2) + 2*I

def f2_int(x):
    x = mp.mpf(x)
    I = mp.quad(lambda t: (-t**2*mp.cos(t*x)+mp.cos(x/2)/4)/mp.cos(pi*t), [0, mp.mpf(1)/4, mp.mpf(1)/2])
    return -f0/4*mp.cos(x/2) + 2*I

def f1_int(x):
    x = mp.mpf(x)
    I = mp.quad(lambda t: (-t*mp.sin(t*x)+mp.sin(x/2)/2)/mp.cos(pi*t), [0, mp.mpf(1)/4, mp.mpf(1)/2])
    return -f0/2*mp.sin(x/2) + 2*I

out = []
def rep(*a):
    s = " ".join(str(z) for z in a); print(s); out.append(s)

rep("f0", mp.nstr(f0, 20), "C0", mp.nstr(C0, 20), "lam0", mp.nstr(lam0, 20), "1/(2pi)", mp.nstr(1/(2*pi), 20))
# 1. representation (9) vs closed form
mx = 0
for x in [0, 0.1, 0.5, 1, 2, 3, 3.1, mp.pi - mp.mpf('1e-8'), mp.pi]:
    d = abs(f(x) - f_int(x)); mx = max(mx, d)
rep("max|f_closed - f_(9)| on 9 pts:", mp.nstr(mx, 5))
# 2. third derivative sign: integral (10) vs mp.diff of closed form; sup ratio
d3 = max(abs(f3_int(x) - mp.diff(f, x, 3)) for x in [0.3, 1.0, 2.0, 2.9])
rep("max|f'''_(10) - diff^3 closed| at 4 pts:", mp.nstr(d3, 5))
N = 400
ratios = []
for k in range(1, N+1):
    x = pi*k/(N+1)
    ratios.append((f3_int(x)/mp.sin(x/2), x))
for xs in [mp.mpf('1e-6'), mp.mpf('1e-3'), pi - mp.mpf('1e-3'), pi - mp.mpf('1e-6')]:
    ratios.append((f3_int(xs)/mp.sin(xs/2), xs))
rmax = max(ratios)
rep("sup sampled f'''/sin(x/2) =", mp.nstr(rmax[0], 12), "at x=", mp.nstr(rmax[1], 8), "; claimed bound -311/71680 =", mp.nstr(mp.mpf(-311)/71680, 12))
rep("all sampled ratios < -311/71680:", all(r < mp.mpf(-311)/71680 for r, _ in ratios))
B = f0/8 + 2*mp.quad(lambda t: (t**3*mp.sin(pi*t)-mp.mpf(1)/8)/mp.cos(pi*t), [0, mp.mpf(1)/4, mp.mpf(1)/2])
rep("B numeric =", mp.nstr(B, 15), " (limit of ratio at x->pi should equal B)")
# exact rational
s = F(3, 40) + F(44, 35840) - F(1, 16) - F(37, 2048)
rep("exact 3/40+44/35840-1/16-37/2048 =", s)
rep("exact pieces: 2*int_0^1/4 (22/7 t^4 - 1/8) =", F(2)*(F(22, 7)*F(1, 4)**5/5 - F(1, 8)*F(1, 4)), "; 2*(1/8)*(27/512-1/8) =", F(2)*F(1, 8)*(F(27, 512)-F(1, 8)))
# 3. jump J
J = 2*(mp.log(pi)-g_)/pi
fpl = f1_int(pi)
rep("f'(pi-) via (9) =", mp.nstr(fpl, 15), " (log pi-gamma)/pi =", mp.nstr((mp.log(pi)-g_)/pi, 15), " J=", mp.nstr(J, 15), " 1/pi=", mp.nstr(1/pi, 15))
# 4. g(0)<=3/pi^2 and g monotone
g0 = f2_int(0); gpi = f2_int(pi)
rep("g(0)=f''(0)=", mp.nstr(g0, 15), " 3/pi^2=", mp.nstr(3/pi**2, 15), " g(pi-)=", mp.nstr(gpi, 15))
# 5. H direct (1) and via (20)
def H(x):
    x = mp.mpf(x)
    fx = f(x)
    brk = [0]
    for b in [pi - x, x]:
        if 0 < b < pi: brk.append(b)
    brk = sorted(set(brk)) + [pi]
    I = mp.quad(lambda v: (f(x+v)+f(x-v)-2*fx)/(2*mp.sin(v/2)) if v != 0 else mp.mpf(0), brk)
    return lam0*fx + I/pi
def W(t):
    t = abs(mp.mpf(t))
    if t >= pi: return mp.mpf(0)
    return mp.quad(lambda s: mp.log(mp.cot(s/4)), [t, pi])
def H20(x):
    x = mp.mpf(x)
    brk = sorted(set([-pi, 0, -x, pi - x if pi - x <= pi else pi, pi]))
    brk = [b for b in brk if -pi <= b <= pi]
    def gg(y):
        y = mp.fmod(y, 2*pi)
        if y > pi: y -= 2*pi
        if y < -pi: y += 2*pi
        return f2_int(abs(y))
    I = mp.quad(lambda t: W(t)*gg(x+t), brk)
    return lam0*f(x) + I/pi - (J/pi)*W(pi-abs(x))
H0 = H(0)
rep("H(0) direct =", mp.nstr(H0, 15))
mp.mp.dps = 20
h20_0 = H20(0); h20_2 = H20(2)
mp.mp.dps = 30
rep("H(0) via (20) =", mp.nstr(h20_0, 12), "; H(2) direct =", mp.nstr(H(2), 12), " via (20) =", mp.nstr(h20_2, 12))
c = (pi-3)/(4*pi**3)
worst = None
xs = [mp.mpf(k)/1000 for k in (1, 2, 5, 10, 20, 50)] + [pi*k/64 for k in range(1, 65)]
for x in xs:
    val = H(x) - H0 + c*x**2
    rat = (H(x) - H0)/x**2
    if worst is None or val > worst[0]: worst = (val, x, rat)
rep("max over", len(xs), "sampled x of [H(x)-H(0)+(pi-3)x^2/(4pi^3)] =", mp.nstr(worst[0], 10), "at x=", mp.nstr(worst[1], 8), "(should be <0)")
small = [(H(x)-H0)/x**2 for x in [mp.mpf('0.001'), mp.mpf('0.01')]]
rep("(H(x)-H(0))/x^2 at x=1e-3,1e-2:", [mp.nstr(z, 10) for z in small], " -c =", mp.nstr(-c, 10))
rep("H(pi)-H(0) =", mp.nstr(H(pi)-H0, 12), " bound -(pi-3)/(4pi) =", mp.nstr(-c*pi**2, 12))
# monotone decrease sample of H on [0,pi]
vals = [H(pi*k/64) for k in range(0, 65)]
rep("H sampled strictly decreasing on [0,pi] (65 pts):", all(vals[i+1] < vals[i] for i in range(64)))
# W(pi-x)>=x^2/4
rep("W(0)=", mp.nstr(W(0), 12), ">= pi^2/4=", mp.nstr(pi**2/4, 12))
# rational elementary constants
rep("log pi>11/10:", mp.log(pi) > mp.mpf(11)/10, "gamma<3/5:", g_ < mp.mpf(3)/5, "C0<4:", C0 < 4, "lam0<1/(2pi):", lam0 < 1/(2*pi))
rep("e^(1/4) lower Taylor 1+1/4+1/32+1/384 =", F(1)+F(1, 4)+F(1, 32)+F(1, 384), "> 32/25 =", F(32, 25), (F(1)+F(1, 4)+F(1, 32)+F(1, 384)) > F(32, 25))
