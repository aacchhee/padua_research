"""E07 H sampling redone with Gauss-Legendre (avoids tanh-sinh endpoint cancellation at the cusp
found in hpi_debug). Sampled numerics; not a proof."""
import mpmath as mp
mp.mp.dps = 30
pi = mp.pi
def f(x):
    x = mp.mpf(x); x = mp.fmod(x, 2*pi)
    if x > pi: x = 2*pi - x
    if x < -pi: x = x + 2*pi
    x = abs(x)
    if x == pi: return mp.mpf(1)
    u = x/(2*pi)
    return mp.cos(x/2)/pi*(-mp.digamma(mp.mpf(1)/2+u)-mp.digamma(mp.mpf(1)/2-u)-2*mp.log(pi))
lam0 = (2/pi)*mp.log(4/pi)
def H(x):
    x = mp.mpf(x); fx = f(x)
    brk = sorted(set([mp.mpf(0)] + [b for b in [pi-x, x] if 0 < b < pi] + [pi]))
    return lam0*fx + mp.quad(lambda v: (f(x+v)+f(x-v)-2*fx)/(2*mp.sin(v/2)), brk, method='gauss-legendre')/pi
H0 = H(0); c = (pi-3)/(4*pi**3)
print("H(0) GL =", mp.nstr(H0, 25))
print("H(pi) GL =", mp.nstr(H(pi), 25), " (2/pi)log(2/pi) =", mp.nstr((2/pi)*mp.log(2/pi), 25))
xs = [mp.mpf(k)/10000 for k in (1, 3, 10, 30, 100, 300)] + [pi*k/128 for k in range(1, 129)]
vals = [(x, H(x)) for x in xs]
worst = max((h - H0 + c*x**2, x) for x, h in vals)
print("max sampled [H(x)-H(0)+(pi-3)x^2/(4pi^3)] over", len(xs), "pts:", mp.nstr(worst[0], 8), "at", mp.nstr(worst[1], 6), "(<0 expected)")
grid = [h for x, h in vals[6:]]
print("H strictly decreasing on the 128-pt grid (pi k/128):", all(grid[i+1] < grid[i] for i in range(len(grid)-1)) and grid[0] < H0)
print("(H(x)-H0)/x^2 at x=1e-4, 1e-3:", mp.nstr((vals[0][1]-H0)/vals[0][0]**2, 10), mp.nstr((vals[2][1]-H0)/vals[2][0]**2, 10))
# near-pi behaviour: H(pi-eps)-H(pi) ~ (J/pi) eps log(1/eps) > 0 (pi is a local min)
for eps in ['1e-2', '1e-3']:
    e = mp.mpf(eps); print("H(pi-eps)-H(pi) eps=", eps, mp.nstr(H(pi-e)-H(pi), 8))
