# Independent rigorous re-evaluation (mpmath interval arithmetic, 200 bits) of the gate quantities
# consumed by companion Sections 4.3/4.4 at n=512 (relative polynomial, absolute gate), 192 (far), 256 (corner).
# Definitions transcribed from companion comparison-unified.tex (uc:constants, uc:uniform-allowance,
# uc:analytic-norm, uc:absolute-gate, uc:relative-gate) and localization (corner lemma).
from mpmath import iv, mp
iv.prec = 200
pi = iv.pi; log = iv.log
jstar = iv.mpf(23)/250; tstar = iv.mpf(221)/500
def consts(n):
    n = iv.mpf(n); m = n + 1; L = log(n); Lb = 1 + L
    T = (4*L**2 - 3*L)/pi**2; b0 = 4/pi**2; r0 = log(iv.mpf(5)/2) + iv.mpf(1)/18
    D = ((52/pi**2)*Lb + 7)/n + 10/n**2 + 20*Lb/(pi*n**2)
    Mm = (b0*(2*L+2*r0)/n + (4 + b0*(L+1/n))/(4*n**2-1) + b0/(2*n-1)**2
          + (5 + b0*(log(n+iv.mpf(1)/2)+2))/(4*(n-iv.mpf(1)/2)**2))
    ebar = D + Mm + 1/n
    KD = ((6 + 16/(3*pi))*Lb + 2/pi)/n
    A4 = 4/n + 40*Lb/(pi*n**2); C4 = A4 + 20/n**2; db = (17*L+27)/n**2
    kWx = ((iv.mpf(19)/2)*Lb + (iv.mpf(23)/3)*L + iv.mpf(155)/2)/n + 152/n**2; kWy = kWx + db
    Wn = (3*log(m) + log(2) + 2*log(pi) + 2)/(pi*m)
    gn = 1 + log(2 + 8*m/(3*pi)); MA = 1/pi + 4/pi**2
    Gg = (7*MA*L + iv.mpf(111)/2 + (63 + log(2) + 4*log(pi) + 7*log(m) + 16*log(2*m) + iv.mpf(3)/2*gn)/pi)/m
    CE = D + Gg + (64+16*L)/n + 318/n**2 + Mm + Wn
    Mn = (4*L**2 + iv.mpf(79)/5*L)/pi**2 + iv.mpf(9)/4 + CE + 2*KD
    return dict(L=L, Lb=Lb, T=T, ebar=ebar, KD=KD, A4=A4, C4=C4, db=db, kWx=kWx, kWy=kWy, CE=CE, M=Mn)
def hi(x): return float(x.b)
def lo(x): return float(x.a)
# --- n = 512 relative polynomial
c = consts(512)
U = c['T'] - c['ebar'] + c['A4'] + jstar
lx = c['kWx'] + iv.mpf(5)/48; ly = c['kWy']; dx = 11*U/48 - iv.mpf(5)/12; dy = 11*U/48
maxP = c['C4'] + lx**2/(4*dx) + ly**2/(4*dy)
vert = lx/(2*dx) + ly/(2*dy)
# P(1/2) via the explicit line maximiser (positive coordinates) -- evaluate quadratic at x*,y*
x_ = (dy/2 + (lx-ly)/2)/(dx+dy); y_ = (dx/2 - (lx-ly)/2)/(dx+dy)
# use e,f,g form as well
e = dx*dy/(dx+dy); f = (dy*lx + dx*ly)/(dx+dy); g = (lx-ly)**2/(4*(dx+dy))
P12 = c['C4'] + g + f/2 - e/4
print("n=512: L in", lo(c['L']), hi(c['L']), " dx>", lo(dx), " db in", lo(c['db']), hi(c['db']), "(5/48=%.6f)" % (5/48))
print("  maxP <", hi(maxP), "(claim <0.040786 and <41/1000)")
print("  vertex <", hi(vert), "(claim <3/20)")
print("  P(1/2) <", hi(P12), "(claim < -0.143069 and < -1/7=%.6f)" % (-1/7), " x*,y* lower:", lo(x_), lo(y_))
# --- absolute gate G(n, rho1)
def G(n, rho1):
    c = consts(n); Th = c['T'] + jstar; h = iv.mpf(rho1)/2 if not isinstance(rho1, type(pi)) else rho1/2
    Cc = tstar + 2*c['KD']
    val = Th*(1-iv.cos(h)) - Cc*iv.sin(h) - tstar**2*iv.cos(h)/(2*Th) - c['CE'] - c['ebar']
    return val, Cc/Th, iv.tan(h)
v, ratio_, tn = G(512, 1)
print("G(512,1) >", lo(v), "(claim >0.534264, >1/2);  (t*+2KD)/Theta <", hi(ratio_), "(claim <3/50); tan(1/2)=", lo(tn))
v, ratio_, tn = G(192, pi/2)
print("G(192,pi/2) >", lo(v), "(claim lin. >0.098316, >3/100); ratio <", hi(ratio_), "(claim <1/10); tan(pi/4)=", lo(tn))
# --- corner 256
c = consts(256); qh = iv.mpf(7)/48; h = pi/4; rU = iv.mpf(2)/125
print("n=256: L in", lo(c['L']), hi(c['L']), "(277/50,111/20)", " Lbar <", hi(c['Lb']), "(131/20=6.55)")
for k, claim in [('T', '>107/10'), ('ebar', '<1/5'), ('KD', '<1/5'), ('CE', '<3/2'), ('C4', '<9/500'), ('kWy', '<93/100'), ('M', '<26')]:
    print("  %-5s in [%.6f, %.6f]  claim %s" % (k, lo(c[k]), hi(c[k]), claim))
dA = qh*(c['T'] - c['ebar'] + jstar) - iv.mpf(1)/4 - c['C4'] - h*c['kWy']
dD = 2*qh*(c['T'] + jstar) - iv.mpf(4)/15 - c['CE'] - iv.mpf(3)/2*c['KD'] - c['ebar']
print("  deltaA - rU*M >", lo(dA - rU*c['M']), "(claim >2729/21000=%.6f)" % (2729/21000))
print("  deltaD - 2rU*M >", lo(dD - 2*rU*c['M']), "(claim >49/1000)")
print("  with exact pi^4/6144:", lo(dA - pi**4/6144*c['M']), lo(dD/2 - pi**4/6144*c['M']), "(min claim >49/2000)")
print("  (1-cos(pi/4))/2 =", lo((1-iv.cos(h))/2), "> 7/48 =", 7/48, "; pi^4/6144 <", hi(pi**4/6144), "< 2/125")
# monotonic sanity (measurement): gates at a few larger n
for n in [300, 400, 1000, 10**4, 10**6]:
    c = consts(n)
    dA = qh*(c['T'] - c['ebar'] + jstar) - iv.mpf(1)/4 - c['C4'] - h*c['kWy']
    dD = 2*qh*(c['T'] + jstar) - iv.mpf(4)/15 - c['CE'] - iv.mpf(3)/2*c['KD'] - c['ebar']
    print("  [MEASURED] n=%d: dA-rU M=%.5f  dD-2rU M=%.5f" % (n, lo(dA - rU*c['M']), lo(dD - 2*rU*c['M'])))
