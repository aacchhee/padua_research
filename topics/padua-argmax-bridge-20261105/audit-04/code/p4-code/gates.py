# P4 audit: independent evaluation of Section 4 gate constants from the
# paper's displayed formulas (uc:constants, uc:uniform-allowance,
# uc:analytic-norm, Corollaries 4.6/4.7, Lemma 4.8, Lemma 4.9).
# High-precision floating evaluation (mpmath, 50 digits): MEASURED, not a proof.
import mpmath as mp
mp.mp.dps = 50
pi = mp.pi; log = mp.log
EG = mp.euler

def consts():
    C0 = 2*EG + 4*log(2)
    k0 = C0 - 2*log(pi)
    # kappa integral (eq:main-kappa)
    def integrand(t):
        s = mp.nsum(lambda j: 1/((2*j+1)*((2*j+1)**2 - t**2)), [0, mp.inf])
        return t**2*mp.cot(pi*t/2)*s
    kappa = 8/pi*mp.quad(integrand, [0, 1])
    Cstar = 4*(EG+log(8/pi))**2/pi**2 + kappa
    H0 = kappa/2 + (2*k0/pi**2)*log(2/pi)
    bstar = C0 - mp.mpf(7)/2
    dstar = C0*bstar/pi**2
    g0 = 4*(log(pi)**2 - log(2)**2)/pi**2
    jj = H0 + dstar - g0
    t0 = 2*log(2)/pi
    return dict(C0=C0, k0=k0, kappa=kappa, Cstar=Cstar, H0=H0, bstar=bstar,
                dstar=dstar, g0=g0, j=jj, t0=t0)

def allow(n):
    n = mp.mpf(n); m = n+1; L = log(n); Lb = 1+L; b0 = 4/pi**2
    r0 = log(mp.mpf(5)/2)+mp.mpf(1)/18
    T = (4*L**2-3*L)/pi**2
    D = ((52/pi**2)*Lb+7)/n + 10/n**2 + 20*Lb/(pi*n**2)
    Mesh = (b0*(2*L+2*r0)/n + (4+b0*(L+1/n))/(4*n**2-1) + b0/(2*n-1)**2
            + (5+b0*(log(n+mp.mpf(1)/2)+2))/(4*(n-mp.mpf(1)/2)**2))
    ebar = D+Mesh+1/n
    KD = ((6+16/(3*pi))*Lb+2/pi)/n
    A4 = 4/n+40*Lb/(pi*n**2); C4 = A4+20/n**2
    dbeta = (17*L+27)/n**2
    JW = ((mp.mpf(3)/2)*Lb+6)/n+148/n**2
    kWx = ((mp.mpf(19)/2)*Lb+(mp.mpf(23)/3)*L+mp.mpf(155)/2)/n+152/n**2
    kWy = kWx+dbeta
    Wn = (3*log(m)+log(2)+2*log(pi)+2)/(pi*m)
    gn = 1+log(2+8*m/(3*pi)); MA = 1/pi+4/pi**2
    Gg = (7*MA*L+mp.mpf(111)/2+(63+log(2)+4*log(pi)+7*log(m)+16*log(2*m)
          +(mp.mpf(3)/2)*gn)/pi)/m
    CE = D+Gg+(64+16*L)/n+318/n**2+Mesh+Wn
    Mn = (4*L**2+(mp.mpf(79)/5)*L)/pi**2+mp.mpf(9)/4+CE+2*KD
    return dict(L=L, Lb=Lb, T=T, D=D, Mesh=Mesh, ebar=ebar, KD=KD, A4=A4,
                C4=C4, dbeta=dbeta, JW=JW, kWx=kWx, kWy=kWy, Wn=Wn, Gg=Gg,
                CE=CE, M=Mn)

jst = mp.mpf(23)/250; tst = mp.mpf(221)/500

def G(n, rho1):
    a = allow(n); Th = a['T']+jst; h = mp.mpf(rho1)/2
    C = tst+2*a['KD']
    return (Th*(1-mp.cos(h)) - C*mp.sin(h) - tst**2*mp.cos(h)/(2*Th)
            - a['CE'] - a['ebar']), C/Th, mp.tan(h)

def Psq(n):
    a = allow(n)
    U = a['T']-a['ebar']+a['A4']+jst
    lx = a['kWx']+mp.mpf(5)/48; ly = a['kWy']
    dx = 11*U/48-mp.mpf(5)/12; dy = 11*U/48
    S0 = dx+dy
    e = dx*dy/S0; f = (dy*lx+dx*ly)/S0; g = (lx-ly)**2/(4*S0)
    P = lambda r: a['C4']+g+f*r-e*r**2
    mx = a['C4']+g+f**2/(4*e)
    mx2 = a['C4']+lx**2/(4*dx)+ly**2/(4*dy)
    vert = f/(2*e); vert2 = lx/(2*dx)+ly/(2*dy)
    xs = (dy/2+(lx-ly)/2)/S0; ys = (dx/2-(lx-ly)/2)/S0
    return dict(dx=dx, dy=dy, lx=lx, ly=ly, max=mx, max_id=mx2, vert=vert,
                vert_id=vert2, Phalf=P(mp.mpf(1)/2), P1=P(1), xs=xs, ys=ys,
                dbeta=a['dbeta'], C4=a['C4'])

def Fh(n):
    n = mp.mpf(n)
    As = mp.mpf(97)/100*mp.mpf(15)/16-mp.mpf(1)/4
    Is = mp.mpf(2303)/5000*mp.mpf(15)/16-mp.mpf(471)/2500
    Rs = mp.mpf(4837)/1875*mp.mpf(15)/16-mp.mpf(5)/6
    return 539*Is/1936-(140*As+400*Rs)/(157*n)-800*As/(3*n**2)

def Fh_true(n):
    # band formula with exact transcendental quantities (c=2, [pi/100,pi/4], rho=1/2)
    a = mp.mpf(15)/16; rb = mp.mpf(1)/2; bm = pi/100; bp = pi/4
    A0 = a-rb/2; Abm = A0-a*mp.sin(bm)
    I = A0*(bp-bm)+a*(mp.cos(bp)-mp.cos(bm))
    R = A0*log(mp.tan(bp/2)/mp.tan(bm/2))-a*(bp-bm)
    Tc = 4*log(2); c = 2
    return Tc*I/pi**2-Tc*Abm/(pi*n)-4*c*R/(pi*n)-4*c*Abm/(n**2*mp.sin(bm))

def corner(n):
    a = allow(n); K = consts()
    h = pi/4; qh = mp.mpf(7)/48; rU = mp.mpf(2)/125
    dA = qh*(a['T']-a['ebar']+K['j'])-mp.mpf(1)/4-a['C4']-h*a['kWy']
    dD = 2*qh*(a['T']+K['j'])-mp.mpf(4)/15-a['CE']-mp.mpf(3)/2*a['KD']-a['ebar']
    delta = min(dA, dD/2)
    return dict(dA_rUM=dA-rU*a['M'], dD_2rUM=dD-2*rU*a['M'],
                gap=delta-a['M']*pi**4/6144, coeff=(16/pi**2)*(delta-a['M']*pi**4/6144),
                **{k: a[k] for k in ['T', 'ebar', 'KD', 'CE', 'C4', 'kWy', 'M', 'L', 'Lb']})

if __name__ == '__main__':
    K = consts()
    print('constants:')
    for k, v in K.items():
        print(f'  {k:6s} {mp.nstr(v, 15)}')
    print('  kappa>9/10', K['kappa'] > mp.mpf(9)/10, ' Cstar<4629/2500', K['Cstar'] < mp.mpf(4629)/2500)
    print('  H0>7/25', K['H0'] > mp.mpf(7)/25, ' dstar>39/250', K['dstar'] > mp.mpf(39)/250,
          ' g0<43/125', K['g0'] < mp.mpf(43)/125, ' j>23/250', K['j'] > jst, ' t0<221/500', K['t0'] < tst)
    Cinf_max = K['Cstar']-K['j']/2+mp.sqrt(K['j']**2/4+K['t0']**2)
    print('  Cinf upper (true consts)', mp.nstr(Cinf_max, 12), '< 9/4', Cinf_max < mp.mpf(9)/4)
    print('absolute gate:')
    for n, r in [(512, 1), (192, pi/2), (160, pi/2), (191, pi/2), (511, 1), (300, 1), (400, 1)]:
        g, ratio, tn = G(n, r)
        print(f'  n={n} rho1={mp.nstr(r,6)} G={mp.nstr(g,12)} ratio={mp.nstr(ratio,8)} tan={mp.nstr(tn,8)}')
    # monotonic samples (illustrative only; proof is analytic)
    prev = None; ok = True
    for n in list(range(160, 4000, 7))+[10**4, 10**5, 10**6, 10**8, 10**12]:
        g, _, _ = G(n, pi/2)
        if prev is not None and g <= prev: ok = False
        prev = g
    print('  G(n,pi/2) increasing on sample 160..1e12:', ok)
    print('relative polynomial at 512:')
    R = Psq(512)
    for k, v in R.items():
        print(f'  {k:8s} {mp.nstr(v, 12)}')
    print('  checks: dx>1', R['dx'] > 1, ' 0<dbeta<5/48', 0 < R['dbeta'] < mp.mpf(5)/48,
          ' vert<3/20', R['vert'] < mp.mpf(3)/20, ' max<40786e-6', R['max'] < mp.mpf(40786)/10**6,
          ' P(1/2)<-143069e-6', R['Phalf'] < -mp.mpf(143069)/10**6)
    prev = None; ok = True
    for n in list(range(512, 5000, 11))+[10**5, 10**7, 10**10]:
        R2 = Psq(n)
        if prev is not None and not (R2['max'] < prev[0] and R2['Phalf'] < prev[1] and R2['vert'] < prev[2]):
            ok = False
        prev = (R2['max'], R2['Phalf'], R2['vert'])
    print('  max,P(1/2),vertex decreasing on sample:', ok)
    print('  smallest n where max P_n<1/20 (illustrative scan):',
          next(n for n in range(160, 2000) if Psq(n)['dx'] > 0 and Psq(n)['max'] < mp.mpf(1)/20))
    print('uniform floor:')
    for n in [64, 160, 295, 294, 512]:
        print(f'  n={n} Fh={mp.nstr(Fh(n),10)} Fh_true={mp.nstr(Fh_true(n),10)}')
    print('  Fh(295)>50064e-6', Fh(295) > mp.mpf(50064)/10**6, 'Fh(295)>1/20', Fh(295) > mp.mpf(1)/20)
    print('corner descent at 256:')
    C = corner(256)
    for k, v in C.items():
        print(f'  {k:8s} {mp.nstr(v, 12)}')
    print('  checks: T>107/10', C['T'] > mp.mpf(107)/10, ' ebar<1/5', C['ebar'] < mp.mpf(1)/5,
          ' KD<1/5', C['KD'] < mp.mpf(1)/5, ' CE<3/2', C['CE'] < mp.mpf(3)/2, ' C4<9/500', C['C4'] < mp.mpf(9)/500,
          ' kWy<93/100', C['kWy'] < mp.mpf(93)/100, ' M<26', C['M'] < 26,
          ' dA-rUM>2729/21000', C['dA_rUM'] > mp.mpf(2729)/21000, ' dD-2rUM>49/1000', C['dD_2rUM'] > mp.mpf(49)/1000,
          ' gap>49/2000', C['gap'] > mp.mpf(49)/2000, ' coeff>1/30', C['coeff'] > mp.mpf(1)/30)
    print('  rU>pi^4/6144', mp.mpf(2)/125 > pi**4/6144, ' (1-cos(pi/4))/2>7/48', (1-mp.cos(pi/4))/2 > mp.mpf(7)/48)
    print('  log256 in (277/50,111/20):', mp.mpf(277)/50 < log(256) < mp.mpf(111)/20, ' Lbar<131/20', 1+log(256) < mp.mpf(131)/20)
    # first-class / second-class floors
    print('selected-pair class bounds:')
    print('  37/(224(pi+1/2))', mp.nstr(mp.mpf(37)/(224*(pi+mp.mpf(1)/2)), 10), '>1/32')
    print('  225/(1040(pi+1/2))', mp.nstr(mp.mpf(225)/(1040*(pi+mp.mpf(1)/2)), 10), '>1/20')
    print('  33/(16pi sqrt3)(1/6-1/41)', mp.nstr(33/(16*pi*mp.sqrt(3))*(mp.mpf(1)/6-mp.mpf(1)/41), 10), '35/656=', mp.nstr(mp.mpf(35)/656, 10))
    print('  (7/8)(29/492)^2', mp.nstr(mp.mpf(7)/8*(mp.mpf(29)/492)**2, 10), '1/512=', mp.nstr(mp.mpf(1)/512, 10))
    print('  log(tan(pi/8)/tan(pi/200))', mp.nstr(log(mp.tan(pi/8)/mp.tan(pi/200)), 10), '<10/3')
    print('  (17pi-21)/41', mp.nstr((17*pi-21)/41, 6))
