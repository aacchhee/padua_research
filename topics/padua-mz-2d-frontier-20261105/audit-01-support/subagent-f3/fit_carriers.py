import numpy as np, math, importlib.util, sys
spec = importlib.util.spec_from_file_location('ct', 'check_threshold.py')
src = open('check_threshold.py').read()
# reuse only the function definitions (stop before the result-producing sections)
cut = src.index('res = {}')
ns = {}
exec(src[:cut], ns)
exec(src[src.index('# D carriers'):src.index('Drows = []')], ns)
fejer = ns['fejer']; tcoef = ns['tcoef']; PI = math.pi
def Q_only(m, theta, sign):
    d = theta-0.5; a = d/4; r = int(math.floor(a*m)); s = r; R = m//2
    th = np.arange(m+1)*PI/m; ph = np.arange(m+2)*PI/(m+1)
    px = np.cos(m*th/2)*fejer(r, th) if sign < 0 else np.sin(m*th/2)*np.sin(r*th)*fejer(r, th)
    py = fejer(s, ph); aa = np.arange(R+1); hm = 2.0/(1-m*m)
    eps = np.ones(m+1); eps[[0, m]] = .5; eta = np.ones(m+2); eta[[0, m+1]] = .5
    gx = eps*px**2; gy = eta*py**2
    sj = (-1.0)**np.arange(m+1); sk = (-1.0)**np.arange(m+2)
    def ct(g):
        G = g[:-1].copy(); G[0] += g[-1]; return np.real(np.fft.fft(G))[:R+1]
    X0 = tcoef(aa)*ct(gx); X1 = tcoef(aa)*ct(sj*gx); Y0 = tcoef(aa)*ct(gy); Y1 = tcoef(aa)*ct(sk*gy)
    S = 0.5*(np.sum(X0*np.cumsum(Y0)[R-aa])+np.sum(X1*np.cumsum(Y1)[R-aa]))
    ex = np.cos(m*th)
    E = 0.5*(np.sum(ex*gx)*np.sum(gy)+np.sum(sj*ex*gx)*np.sum(sk*gy))
    return 2/(m*(m+1))*(S-2*hm*E)
for theta in [0.6, 0.75, 0.95]:
    for sg in (-1, 1):
        ks = list(range(12, 24))
        Qs = [Q_only(2**k, theta, sg) for k in ks]
        lg = np.array([k*math.log(2) for k in ks])
        Lfit, cfit = np.polyfit(lg[-5:], Qs[-5:], 1)
        d = theta-.5; pred = -d*d/9 if sg < 0 else d*d/18
        print(f"theta={theta} sign={sg:+d} Q(2^12..2^23)={[round(q,4) for q in Qs[::3]]} fitted slope={Lfit:.5f} predicted={pred:.5f} intercept={cfit:.3f} est. log m at Q=0: {(-cfit/Lfit) if sg<0 else float('nan'):.0f}")
