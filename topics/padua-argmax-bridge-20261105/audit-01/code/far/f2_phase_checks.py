import random, time
from mpmath import mp, mpf, pi, psi, cos, sin, log, euler, stieltjes, diff, iv, findroot
mp.dps = 30
t0 = time.process_time()
def Cfun(t): return -psi(0,t)-psi(0,1-t)
def Phi0(t):
    t = t - int(mp.floor(t))
    if t == 0: return mpf(1)
    return sin(pi*t)/pi*(Cfun(t)-2*log(pi))
k = euler + log(8/pi)
bc = 8*k/pi**2
def coeffs(al, be):
    a = (cos(al)+cos(be))/2
    ce, cd = cos((al+be)/2), cos((al-be)/2)
    U0 = ce*Phi0(mpf(1)/2+(al-be)/(2*pi)) + cd*Phi0(mpf(1)/2+(al+be)/(2*pi))
    return a, ce, cd, U0
def bfull(al, be):
    a, ce, cd, U0 = coeffs(al, be)
    alog = a*log(a) if a > 0 else mpf(0)
    return 2*U0/pi + (8*a*log(2)+4*alog+2*(al*sin(al)+be*sin(be)))/pi**2, a
# 1. b_full - b_c <= 3(1-a)/pi^2 on a grid of the closed triangle
worst = -1e9; wpt = None
N = 60
for i in range(N+1):
    for j in range(N+1-i):
        al = pi*i/N; be = pi*j/N
        b, a = bfull(al, be)
        r = (b-bc) - 3*(1-a)/pi**2
        if r > worst: worst, wpt = r, (float(al), float(be), float(b-bc), float(3*(1-a)/pi**2))
print("max[(b_full-b_c)-3(1-a)/pi^2] on grid:", float(worst), wpt)
# ratio (b_full-b_c)/((1-a)/pi^2) on far region
mx = -1e9
for i in range(N+1):
    for j in range(N+1-i):
        al = pi*i/N; be = pi*j/N
        if al+be < 0.5: continue
        b, a = bfull(al, be)
        mx = max(mx, (b-bc)/((1-a)/pi**2))
print("max (b_full-b_c)*pi^2/(1-a) on far grid:", float(mx))
# 2. E_R vs E_inf at random interior phases
def ell(r, al, b, a):
    w = r*pi + b
    s = sin(b)/w
    acc = mpf(0)
    for j in range(-r+1, r, 2):
        acc += 1/(w**2-(j*pi+al)**2)
    return s + 8*a*acc
def E_R(R, al, be):
    a, ce, cd, U0 = coeffs(al, be)
    B0 = 4*a/pi**2; D0 = U0/pi + B0*log(pi)
    CR = sin(be)/be if be != 0 else mpf(1)
    for r in range(1, R): CR += ell(r, al, be, a)
    for r in range(1, R+1): CR += ell(r, al, -be, a)
    t = be/pi
    h = -psi(0, R+t) - psi(0, R+1-t)
    g = stieltjes(1, R+t) + stieltjes(1, R+1-t)
    return CR + D0*h + B0*g, CR, a
def E_inf(al, be):
    a = (cos(al)+cos(be))/2
    td = mpf(1)/2+(al-be)/(2*pi); te = mpf(1)/2+(al+be)/(2*pi)
    return a/3 + a*Cfun(td)*Cfun(te)/pi**2
# check g_R via direct partial sum for one t
R=64; t=mpf('0.3'); K=20000
direct = sum(log(k+t)/(k+t) for k in range(R, K+1)) - log(K+t+mpf(1)/2)**2/2
print("g_R direct(K=2e4) vs stieltjes:", float(direct), float(stieltjes(1,R+t)), "tail bound", float((log(K+t+0.5)+2)/(8*(K+t+0.5)**2)))
random.seed(1)
pts = [(mpf('0.25'),mpf('0.25')),(mpf('1.0'),mpf('0.7')),(mpf('0.1'),mpf('2.9')),(mpf('2.0'),mpf('1.1')),(mpf('1.5'),mpf('1.5')-mpf('1e-6'))]
for _ in range(4):
    x=random.uniform(0,3.14); y=random.uniform(0,3.14-x); pts.append((mpf(x),mpf(y)))
mxE = -1
for al,be in pts:
    e64, CR, a = E_R(64, al, be)
    e128, _, _ = E_R(128, al, be)
    ei = E_inf(al, be)
    mxE = max(mxE, e64)
    print("al=%.4f be=%.4f a=%.4f E64=%.10f E128=%.10f Einf=%.10f |E64-Einf|=%.3e (bound %.3e) |E128-Einf|=%.3e (bound %.3e)" % (al,be,a,e64,e128,ei,abs(e64-ei),1/63**2,abs(e128-ei),1/127**2))
print("max E64 at sampled points", float(mxE), "bound 49/25+1/3000 =", 49/25+1/3000)
print("C0=",float(Cfun(mpf(1)/2)), "C0^2/pi^2+1/3=", float(Cfun(mpf(1)/2)**2/pi**2+mpf(1)/3))
# 3. Phi0'' on (0,1): max of smooth part; derivative jump at integers
mxd2 = -1e9; arg=None
for i in range(1, 400):
    t = mpf(i)/400
    v = diff(Phi0, t, 2)
    if v > mxd2: mxd2, arg = v, t
print("max Phi0'' on (0,1) grid:", float(mxd2), "at", float(arg))
dp = diff(Phi0, mpf('1e-12'), 1); dm = diff(Phi0, 1-mpf('1e-12'), 1)
print("Phi0'(0+)=",float(dp)," Phi0'(1-)=",float(dm)," jump at integer (right-left)=",float(dp-dm))
# 4. f(x)=Phi0(1/2+x/2pi) range
vals=[Phi0(mpf(1)/2+mpf(i)/200) for i in range(0,201)]
print("min/max Phi0 on [1/2,3/2]:", float(min(vals)), float(max(vals)), "k0/pi=", float((Cfun(mpf(1)/2)-2*log(pi))/pi))
# 5. interval check 1-cos(1/4) >= 191/6144 and k>3/2
x = iv.mpf(1)/4
lo = 1-iv.cos(x)
print("iv 1-cos(1/4) =", lo, " 191/6144 =", 191/6144, " lower>=191/6144:", lo.a >= iv.mpf(191)/6144)
kiv = iv.euler + iv.log(iv.mpf(8)/iv.pi)
print("iv k =", kiv, " (2k/pi)^2 =", (2*kiv/iv.pi)**2)
print("cpu", time.process_time()-t0)
