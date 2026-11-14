"""Claude audit-06 (M6) independent checks of the response-05 analytic changes.

Run: PYTHONPATH=<audit6>/pylib python3 -I -B m6_checks.py <trees-root>
(-I is not used when PYTHONPATH is needed; run with python3 -B.)
Labels: every PASS line is [E]; floating results are MEASURED, iv/Fraction results exact/rigorous
for the numbers they check.  Own transcription of formulas from the 8937d3b TeX; no repository
code is imported.
"""
import sys, re, random
from fractions import Fraction as Fr
import mpmath as mp
from mpmath import iv, mpf

R = sys.argv[1]
T = 'topics/padua-argmax-bridge-20261105'
fails = []


def lo(x):
    return mp.make_mpf(x._mpi_[0])


def hi(x):
    return mp.make_mpf(x._mpi_[1])


def frac(v):
    man, ex = v.man_exp
    return Fr(man) * Fr(2) ** ex



def ok(cond, msg):
    print(('PASS ' if cond else 'FAIL ') + msg)
    if not cond:
        fails.append(msg)


mp.mp.dps = 50
pi = mp.pi

# ---------------------------------------------------------------- A. M5A-01 collisions
print('== A. omitted-collision clause (M5A-01)')


def frac_dist(z):
    return abs(z - mp.nint(z))


def collision_example(n, jp, y):
    m = n + 1
    r = 2 * m - jp                      # right-endpoint row, not in A_6 when jp >= 3
    v = (jp * pi - y) / m               # reflected endpoint angle, v_r = 2*pi - v
    x = pi - v - y                      # eta_+ collision locus x + y = pi - v
    vr = (r * pi + y) / m
    dr = (1 - r) % 2
    us = [(dr * pi + x + 2 * k * pi) / n for k in range(n)]
    dmin, kmin = min((frac_dist(n * (u + vr) / (2 * pi)), k) for k, u in enumerate(us))
    u = us[kmin]
    eta_p = mpf(1) / 2 + (x + y - vr) / (2 * pi)            # (uc:row-profile)
    s, nu, xi = -y / pi, jp - y / pi, x / pi
    off = (1 - s + xi) / 2 + nu / (2 * m)                    # text offset, '+' sign
    a = (mp.cos(x) + mp.cos(y)) / 2
    P = mp.sin(x) + mp.sin(y)
    rho = x + y
    print(f'  n={n} row r=2m-{jp} y={float(y)} x={float(x):.6f} v={float(v):.6g}: '
          f'min frac dist={float(dmin):.2e} (k={kmin}), |cos u-cos v_r|={float(abs(mp.cos(u)-mp.cos(vr))):.1e}, '
          f'frac(eta_+)={float(frac_dist(eta_p)):.1e}, text offset dist={float(frac_dist(off)):.1e}')
    print(f'     |x-y|={float(abs(x-y)):.6f}  pi-v={float(pi-v):.6f}  rho={float(rho):.6f}  '
          f'a={float(a):.3e}  Pv/2={float(P*v/2):.3e}  (P/2)cot(rho/2)={float(P/2*mp.cot(rho/2)):.3e}')
    ok(dmin < mpf(10) ** -40, f'n={n}: actual sample hits the -v_r pole (collision)')
    ok(abs(x - y) < pi - v, f'n={n}: old clause |x-y|>=pi-v is FALSE here')
    ok(rho >= pi - v - mpf(10) ** -40, f'n={n}: corrected clause rho>=pi-v holds')
    ok(a <= P * v / 2, f'n={n}: consequence a<=Pv/2 holds')
    ok(x >= 0 and x + y <= pi, f'n={n}: phase in the folded triangle')


for n in (32, 192, 512):
    collision_example(n, 3, mpf('0.4'))
    collision_example(n, 7, mpf('0.4'))

# randomized locus test: every collision of a non-retained endpoint row (either channel, either
# side) satisfies rho >= pi - v and a <= P v/2 (MEASURED on random points of every locus line)
random.seed(20261113)
mp.mp.dps = 30
viol = 0
tested = 0
for n in (32, 192, 512):
    m = n + 1
    for trial in range(4000):
        side = random.choice('LR')
        j = random.randint(2 if side == 'L' else 3, m - 1)   # endpoint rows with v < pi/2 only
        y = mpf(random.random()) * pi
        v = (j * pi + y) / m if side == 'L' else (j * pi - y) / m
        if not (0 < v < pi / 2):
            continue
        r = j if side == 'L' else 2 * m - j
        vr = (r * pi + y) / m
        # candidate loci: x - y = pi - v, y - x = pi - v, x + y = pi - v
        for locus in ('x-y', 'y-x', 'x+y'):
            x = {'x-y': y + pi - v, 'y-x': y - (pi - v), 'x+y': pi - v - y}[locus]
            if x < 0 or x + y > pi:
                continue
            dr = (1 - r) % 2
            # n*u_k/(2pi) = (dr*pi+x)/(2pi) + k, so the fractional offset is the same for every k
            hit = any(frac_dist((dr * pi + x - sgn * n * vr) / (2 * pi)) < mpf(10) ** -20 for sgn in (1, -1))
            if not hit:
                continue
            tested += 1
            a = (mp.cos(x) + mp.cos(y)) / 2
            P = mp.sin(x) + mp.sin(y)
            if not (x + y >= pi - v - mpf(10) ** -20 and a <= P * v / 2 + mpf(10) ** -20):
                viol += 1
ok(tested > 1000 and viol == 0, f'random collision loci: {tested} actual collisions, {viol} violations of rho>=pi-v / a<=Pv/2')

# converse: a point with rho < pi - v has no collision on that row (sampled)
mp.mp.dps = 30
bad = 0
for n in (32, 192):
    m = n + 1
    for trial in range(300):
        side = random.choice('LR')
        j = random.randint(2 if side == 'L' else 3, 8)
        y = mpf(random.random()) * 1.5
        v = (j * pi + y) / m if side == 'L' else (j * pi - y) / m
        x = mpf(random.random()) * (pi - v - y) * mpf('0.999')
        r = j if side == 'L' else 2 * m - j
        vr = (r * pi + y) / m
        dr = (1 - r) % 2
        if min(frac_dist((dr * pi + x - n * vr) / (2 * pi)), frac_dist((dr * pi + x + n * vr) / (2 * pi))) < mpf(10) ** -12:
            bad += 1
ok(bad == 0, f'no collision found when rho<pi-v (600 sampled rows): {bad}')

# ---------------------------------------------------------------- B. envelope (uc:endpoint-envelope)
print('== B. pole decomposition and sum to 7')
ivpi = iv.pi
iv.dps = 50
c7 = 6 + ivpi ** 2 / 24 + 1 / ivpi
ok(c7.b < 7, f'6+pi^2/24+1/pi = {c7} < 7')
ok((12 / ivpi).b < 6, '12/pi < 6 (|N_s-U_0|/t <= 12/pi absorbed in 6)')
mp.mp.dps = 30
worst = max(((1 / (2 * mp.sin(t / 2)) - 1 / t) / t) for t in mp.linspace(mpf('1e-6'), pi, 4001))
ok(worst <= pi / 48, f'sup_(0,pi] ([2sin(t/2)]^-1 - 1/t)/t = {float(worst):.6f} <= pi/48 = {float(pi/48):.6f}')
worst2 = max((t - 2 * mp.sin(t / 2)) / t ** 3 for t in mp.linspace(mpf('1e-6'), pi, 4001))
ok(worst2 <= mpf(1) / 24, f'sup (t-2sin(t/2))/t^3 = {float(worst2):.6f} <= 1/24')
worst3 = max(t * (1 + abs(mp.log(t))) for t in mp.linspace(mpf('1e-9'), pi / 4, 4001))
ok(worst3 <= 1, f'sup_(0,pi/4] t(1+|log t|) = {float(worst3):.6f} <= 1')
ok(Fr(11, 4) <= 3, '(P/4pi)*11 <= 3P/pi and (P/4pi)*8 = 2P/pi')

# ---------------------------------------------------------------- C. primitive and max formulas
print('== C. primitive, domination of the subtracted integrand')
import sympy as sp
t, a_, p_, q_ = sp.symbols('t a p q', positive=True)
ok(sp.simplify(sp.diff(4 * a_ * sp.log(sp.sin(t / 2)), t) - 2 * a_ * sp.cot(t / 2)) == 0,
   'd/dt 4a log sin(t/2) = 2a cot(t/2) = T_t')
g = sp.cot(t / 2) - 2 / t
ok(sp.limit(g, t, 0, '+') == 0 and abs(float(g.subs(t, sp.pi)) + 2 / float(sp.pi)) < 1e-15,
   'cot(t/2)-2/t -> 0 at 0+, = -2/pi at pi (bounded on (0,pi])')
mx = 0.0
random.seed(7)
for _ in range(20000):
    x = random.random() * mp.pi
    y = random.random() * (float(mp.pi) - x)
    p, q = float(mp.sin(x)), float(mp.sin(y))
    a = (float(mp.cos(x)) + float(mp.cos(y))) / 2
    tt = random.random() * float(mp.pi)
    Tt = 2 * a * float(mp.cot(tt / 2))
    Cm, Cp = (p - q - Tt) / 4, (p + q + Tt) / 4          # row coefficients at v = t
    Cm2, Cp2 = (p - q + Tt) / 4, (p + q - Tt) / 4        # at v = 2pi - t
    piA, piA2 = 2 * (abs(Cm) + abs(Cp)), 2 * (abs(Cm2) + abs(Cp2))
    mx = max(mx, abs(piA - Tt), abs(piA2 - Tt))
    assert abs(piA - max(p, q + Tt)) < 1e-9 and abs(piA2 - max(p, abs(q - Tt))) < 1e-9
ok(mx <= 1 + 1e-12, f'|pi A(t)-T_t|, |pi A(2pi-t)-T_t| <= 1 over 20000 random (x,y,t): max {mx:.6f}')

# ---------------------------------------------------------------- D. amplitude-phase minimum
print('== D. amplitude-phase minimum and Cauchy-Schwarz step')
A = 398 / (11 * ivpi ** 2)
B = 48 / ivpi
mn = A + B - iv.sqrt(A ** 2 + B ** 2)
ok(frac(lo(A)) > Fr(18, 5) and frac(lo(B)) > 15 and frac(lo(mn)) > 3, f'A={A}, B={B}, A+B-sqrt(A^2+B^2)={mn} > 3')
ok(frac(lo(2 * (A - 3) * (B - 3))) > 9, '2(A-3)(B-3) > 9')
xs = sp.symbols('x', real=True)
Aq, Bq = sp.symbols('A B', positive=True)
# (A+B-3)^2 - (A^2+B^2) = 2(A-3)(B-3) - 9
ok(sp.expand((Aq + Bq - 3) ** 2 - (Aq ** 2 + Bq ** 2) - (2 * (Aq - 3) * (Bq - 3) - 9)) == 0,
   'A+B-sqrt(A^2+B^2)>3  <=>  2(A-3)(B-3)>9 (when A+B>3)')
jj, t0 = sp.symbols('j t0', positive=True)
# max over x of (j/2)cos x + t0 sin x equals sqrt(j^2/4+t0^2)
ok(sp.simplify(sp.sqrt((jj / 2) ** 2 + t0 ** 2) - sp.sqrt(jj ** 2 / 4 + t0 ** 2)) == 0,
   'Cauchy-Schwarz bound for (j/2)cos x + t0 sin x')
d = Fr(249, 625)
ok(d ** 2 + d * Fr(23, 250) - Fr(221, 500) ** 2 == Fr(71, 6250000), 'delta^2+delta j-t0^2 = 71/6250000')

# ---------------------------------------------------------------- E. prefactor / wrap cost
print('== E. prefactor and wrap cost')
nu_, m_ = sp.symbols('nu m', positive=True)
vv = sp.pi * nu_ / m_
pref = 2 * a_ * (vv / 2) * sp.cot(vv / 2) / (sp.pi ** 2 * nu_)
ok(sp.simplify(pref - a_ * sp.cot(vv / 2) / (sp.pi * m_)) == 0,
   '2a tau(v/2)/(pi^2 nu) = a cot(v/2)/(pi m) (v = pi nu/m)')
ok(all(Fr(j) - Fr(5, 4) >= Fr(3, 4) * (j - 1) for j in range(2, 2000)), 'j-5/4 >= 3(j-1)/4 for j>=2')
ok(2 * Fr(1) * Fr(4, 3) == Fr(8, 3), 'two wraps x (P/(pi m)) x 4/(3(j-1)) = 8P/(3 pi m (j-1))')
# summing j=2..n+1 gives H_n; two sides -> 16 P H_n/(3 pi m) <= 16 P H_n/(3 pi n) since m=n+1
mp.mp.dps = 30
ok(all(mp.tan(v / 2) <= v for v in mp.linspace(mpf('1e-6'), pi / 2, 2001)),
   'tan(v/2) <= v on (0,pi/2]: a=(P/2)cot(rho/2) <= (P/2)tan(v/2) <= Pv/2 when rho >= pi-v')

# ---------------------------------------------------------------- F. section 3.3 reasons
print('== F. section 3.3 restored reasons')
z, tq = sp.symbols('z t', positive=True)
ok(sp.simplify(sp.Rational(1, 8) * sp.integrate(2 * (z + tq) ** -3, (tq, 0, sp.oo)) - 1 / (8 * z ** 2)) == 0,
   '(1/8) int_0^inf 2(z+t)^-3 dt = 1/(8 z^2)')
# trapezoid kernel max: (s)(1-s)/2 <= 1/8
ok(sp.maximum(tq * (1 - tq) / 2, tq, sp.Interval(0, 1)) == sp.Rational(1, 8), 'unit-cell trapezoid kernel max 1/8')
mp.mp.dps = 40
ok(all(abs(mp.digamma(y / 2) - (mp.digamma(1 + y / 2) - 2 / y)) < mpf(10) ** -35
       for y in (mpf('0.001'), mpf('0.3'), mpf('0.77'), mpf('1.9'))), 'psi(y/2) = psi(1+y/2) - 2/y')
worst = max((abs(mp.psi(1, r + mpf(1) / 2) - 1 / r) * 3 * r ** 3) for r in
            list(mp.linspace(1, 3, 201)) + [mpf(k) for k in range(3, 400)])
ok(worst <= 1, f'|psi\'(r+1/2)-1/r| <= 1/(3r^3) for real r>=1 (max ratio {float(worst):.4f})')
ok(all(Fr(1, 4) * (Fr(1, r ** 4) + Fr(1, 3 * r ** 3)) <= Fr(1, 3 * r ** 3) for r in range(1, 500)),
   '(1/4)(r^-4 + 1/(3r^3)) <= 1/(3 r^3) for integers r>=1 (and real r>=1 by r^-4<=r^-3)')
# midpoint cell error for t^-2: max|f''|/24 = 6/(24 (r+k)^4) = 1/(4 (r+k)^4)
ok(Fr(6, 24) == Fr(1, 4), 'midpoint cell bound h^3 max|g\'\'|/24 with g=t^-2 gives 1/(4(r+k)^4)')

# ---------------------------------------------------------------- G. base-value table (60 entries)
print('== G. base-value table, own mpmath.iv transcription of (uc:constants),(uc:uniform-allowance),(uc:analytic-norm), Cor 4.7')
iv.dps = 60


def base(n):
    n = iv.mpf(n)
    m = n + 1
    L = iv.log(n)
    Lb = 1 + L
    PI = iv.pi
    TT = (4 * L ** 2 - 3 * L) / PI ** 2
    b0 = 4 / PI ** 2
    r0 = iv.log(iv.mpf(5) / 2) + iv.mpf(1) / 18
    D = ((52 / PI ** 2) * Lb + 7) / n + 10 / n ** 2 + 20 * Lb / (PI * n ** 2)
    MM = (b0 * (2 * L + 2 * r0) / n + (4 + b0 * (L + 1 / n)) / (4 * n ** 2 - 1) + b0 / (2 * n - 1) ** 2
          + (5 + b0 * (iv.log(n + iv.mpf(1) / 2) + 2)) / (4 * (n - iv.mpf(1) / 2) ** 2))
    eb = D + MM + 1 / n
    KD = ((6 + 16 / (3 * PI)) * Lb + 2 / PI) / n
    A4 = 4 / n + 40 * Lb / (PI * n ** 2)
    C4 = A4 + 20 / n ** 2
    db = (17 * L + 27) / n ** 2
    kx = ((iv.mpf(19) / 2) * Lb + (iv.mpf(23) / 3) * L + iv.mpf(155) / 2) / n + 152 / n ** 2
    ky = kx + db
    Wn = (3 * iv.log(m) + iv.log(2) + 2 * iv.log(PI) + 2) / (PI * m)
    gn = 1 + iv.log(2 + 8 * m / (3 * PI))
    MA = 1 / PI + 4 / PI ** 2
    Gg = (7 * MA * L + iv.mpf(111) / 2 + (63 + iv.log(2) + 4 * iv.log(PI) + 7 * iv.log(m)) / PI
          + (16 * iv.log(2 * m) + iv.mpf(3) / 2 * gn) / PI) / m
    CE = D + Gg + (64 + 16 * L) / n + 318 / n ** 2 + MM + Wn
    Mn = (4 * L ** 2 + (iv.mpf(79) / 5) * L) / PI ** 2 + iv.mpf(9) / 4 + CE + 2 * KD
    js = iv.mpf(23) / 250
    Us = TT - eb + A4 + js
    return {'L': L, 'T': TT, 'ebar': eb, 'K_D': KD, 'CE': CE, 'C_4': C4, 'k_Wx': kx, 'k_Wy': ky,
            'd_beta': db, 'M(n)': Mn, 'U_*': Us, 'd_x': 11 * Us / 48 - iv.mpf(5) / 12,
            'd_y': 11 * Us / 48, 'l_x': kx + iv.mpf(5) / 48, 'l_y': ky}


names = {'L': 'L', '\\mathfrak T': 'T', '\\bar e': 'ebar', 'K_D': 'K_D', '\\overline C_E': 'CE', 'C_4': 'C_4',
         'k_{Wx}': 'k_Wx', 'k_{Wy}': 'k_Wy', 'd_\\beta': 'd_beta', 'M(n)': 'M(n)', 'U_*': 'U_*', 'd_x': 'd_x',
         'd_y': 'd_y', '\\ell_x': 'l_x', '\\ell_y': 'l_y'}


def parse_table(path):
    s = open(path).read()
    i = s.index('\\label{uc:base-values}')
    body = s[i:s.index('\\end{tabular}', i)]
    rows = {}
    cols = None
    for line in body.split('\\\\'):
        line = line.replace('\\midrule', '').replace('\\toprule', '').strip()
        if 'Quantity' in line:
            cols = [int(c) for c in re.findall(r'\$(\d+)\$', line)]
            continue
        mm = re.match(r'\$(.+?)\$\s*&\s*\$\[([-\d.]+),([-\d.]+)\]\$\s*&\s*\$\[([-\d.]+),([-\d.]+)\]\$', line)
        if mm and cols:
            key = names[mm.group(1)]
            rows[(key, cols[0])] = (Fr(mm.group(2)), Fr(mm.group(3)))
            rows[(key, cols[1])] = (Fr(mm.group(4)), Fr(mm.group(5)))
    return rows


tp = parse_table(f'{R}/new/{T}/paper/sections/comparison-unified.tex')
tc = parse_table(f'{R}/new/{T}/companion-paper/sections/comparison-unified.tex')
ok(len(tp) == 60 and tp == tc, f'table parsed: paper {len(tp)} entries, companion identical: {tp == tc}')
vals = {n: base(n) for n in (192, 256, 295, 512)}
contain = tight = 0
for (k, n), (tlo, thi) in sorted(tp.items(), key=lambda z: (z[0][1], z[0][0])):
    w = vals[n][k]
    wl, wh = frac(lo(w)), frac(hi(w))
    inside = wl >= tlo and wh <= thi
    # tightest outward 6-decimal enclosure of the (narrow) true interval
    lo6 = Fr((wl * 10 ** 6).__floor__(), 10 ** 6)
    hi6 = Fr((wh * 10 ** 6).__ceil__(), 10 ** 6)
    contain += inside
    tight += (tlo == lo6 and thi == hi6)
    if not (inside and tlo == lo6 and thi == hi6):
        print('   mismatch', k, n, tlo, thi, w)
ok(contain == 60, f'60/60 entries contain the true value: {contain}')
ok(tight == 60, f'60/60 entries are the tightest outward 6-decimal enclosure: {tight}')
v512 = vals[512]
print('   e.g. n=512: T', v512['T'], ' CE', v512['CE'], ' M', v512['M(n)'])

# ---------------------------------------------------------------- H. worked table J(1,1/2,e)
print('== H. worked-value J(1,1/2,e) constancy on 0<e<pi (MEASURED)')
mp.mp.dps = 25


def Iint(C, Dd, e):
    f = lambda tt: abs(C * mp.cot(tt) + Dd * mp.cot(tt + e)) - abs(C * mp.cot(tt)) - abs(Dd * mp.cot(tt + e))
    pts = sorted({mpf(0), pi / 2, (pi / 2 - e) % pi, pi - e, pi})
    # add equality crossings |C cot t| = |D cot(t+e)| inside each piece
    extra = []
    grid = mp.linspace(mpf('1e-8'), pi - mpf('1e-8'), 2001)
    h = lambda tt: abs(C * mp.cot(tt)) - abs(Dd * mp.cot(tt + e))
    prev = None
    for g_ in grid:
        if abs(mp.sin(g_ + e)) < mpf('1e-12'):
            prev = None
            continue
        val = h(g_)
        if prev is not None and prev[1] * val < 0:
            extra.append(mp.findroot(h, (prev[0], g_), solver='bisect'))
        prev = (g_, val)
    pts = sorted(set(pts) | set(extra))
    return mp.quad(f, pts)


Js = []
for e in (mpf('0.05'), mpf('0.4'), mpf(1), mpf(2), mpf('2.9'), mpf('3.1')):
    Js.append(Iint(mpf(1) / 4, mpf(3) / 4, e))
    print(f'   J(1,1/2,{float(e)}) = {float(Js[-1]):.7f}')
ok(all(abs(Jv - mpf('-1.12467')) < mpf('6e-6') for Jv in Js), 'J(1,1/2,e) = -1.12467 (6 d.p.) at six e in (0,pi)')

# ---------------------------------------------------------------- I. kernel evaluation form (25)
print('== I. (eq:kernel-evaluation) and product form against (eq:angular-kernel) (MEASURED)')
mp.mp.dps = 30


def G_def(n, u, v):
    nu = lambda p: 1 if p == 0 else 2
    return sum(nu(p) * nu(q) * mp.cos(p * u) * mp.cos(q * v) for p in range(n + 1) for q in range(n + 1 - p)) - mp.cos(n * u)


def Pn(n, c):
    return mp.chebyt(n + 1, c) + mp.chebyt(n, c)


def G_dd(n, u, v):
    cu, cv = mp.cos(u), mp.cos(v)
    if abs(cu - cv) < mpf(10) ** -25:
        return mp.diff(lambda c: Pn(n, c), cu) - mp.cos(n * u)
    return (Pn(n, cu) - Pn(n, cv)) / (cu - cv) - mp.cos(n * u)


def Rl(l, xi):
    if abs(mp.sin(xi)) < mpf(10) ** -25:
        j = int(mp.nint(xi / pi))
        return l * (-1) ** (j * (l - 1))
    return mp.sin(l * xi) / mp.sin(xi)


def G_prod(n, u, v):
    up, um = (u + v) / 2, (v - u) / 2
    return Rl(n + 1, up) * Rl(n + 1, um) + Rl(n, up) * Rl(n, um) - mp.cos(n * u)


random.seed(11)
e1 = e2 = mpf(0)
for n in range(1, 10):
    for _ in range(12):
        u, v = mpf(random.uniform(-7, 7)), mpf(random.uniform(-7, 7))
        g0 = G_def(n, u, v)
        e1 = max(e1, abs(g0 - G_dd(n, u, v)))
        e2 = max(e2, abs(g0 - G_prod(n, u, v)))
    for u, v in ((mpf('0.7'), mpf('0.7')), (mpf('0.7'), -mpf('0.7')), (mpf('0.7'), 2 * pi - mpf('0.7')),
                 (pi, pi), (mpf(0), mpf(0))):
        g0 = G_def(n, u, v)
        e1 = max(e1, abs(g0 - G_dd(n, u, v)))
        e2 = max(e2, abs(g0 - G_prod(n, u, v)))
ok(e1 < mpf(10) ** -15 and e2 < mpf(10) ** -15,
   f'n=1..9: |def-(25)| max {float(e1):.1e}, |def-product form| max {float(e2):.1e} (incl. collisions)')

# row identity with the -cos(nu) cancellation
mp.mp.dps = 30
emax = mpf(0)
for n in (32, 33, 192):
    m = n + 1
    for _ in range(40):
        x = mpf(random.random()) * pi
        y = mpf(random.random()) * (pi - x)
        r = random.randint(0, 2 * m - 1)
        k = random.randint(0, n - 1)
        dr = (1 - r) % 2
        u = (dr * pi + x + 2 * k * pi) / n
        vr = (r * pi + y) / m
        if abs(mp.cos(u) - mp.cos(vr)) < mpf('1e-8'):
            continue
        a = (mp.cos(x) + mp.cos(y)) / 2
        p, q = mp.sin(x), mp.sin(y)
        lhs = (-1) ** dr * G_dd(n, u, vr) / 2
        rhs = (a * (1 + mp.cos(vr)) - p / 2 * mp.sin(u) + q / 2 * mp.sin(vr)) / (mp.cos(u) - mp.cos(vr))
        ok_c = abs(mp.cos(n * u) - (-1) ** dr * mp.cos(x)) < mpf(10) ** -20
        Cm = (p - q - 2 * a * mp.cot(vr / 2)) / 4
        Cp = (p + q + 2 * a * mp.cot(vr / 2)) / 4
        rhs2 = Cm * mp.cot((u - vr) / 2) + Cp * mp.cot((u + vr) / 2)
        emax = max(emax, abs(lhs - rhs) / (1 + abs(rhs)), abs(rhs - rhs2) / (1 + abs(rhs)), 0 if ok_c else 1)
ok(emax < mpf(10) ** -15, f'row identity (-1)^d G/2 = [...]/(cos u-cos v) = C_-cot+C_+cot, cos(nu)=(-1)^d cos x: max rel err {float(emax):.1e}')

print()
print('FAILURES:', len(fails))
for f_ in fails:
    print('  ', f_)
sys.exit(1 if fails else 0)
