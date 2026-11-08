# C2A audit: verify cancellation lemma (uc:cancellation-lemma) and the companion's
# added derivations (integration intervals, root formula, R_s/R_e, endpoint value, E<=Z).
import mpmath as mp, random
mp.mp.dps = 30
pi = mp.pi

def I_direct(C, D, e):
    f = lambda t: abs(C*mp.cot(t)+D*mp.cot(t+e)) - abs(C*mp.cot(t)) - abs(D*mp.cot(t+e))
    pts = set([mp.mpf(0), pi/2-e, pi/2, pi-e, pi])
    # equality roots of |C cot t| = |D cot(t+e)| : C cot t = +-D cot(t+e)
    # sample-based root bracketing for breakpoints
    N = 4000
    ts = [pi*(k+0.5)/N for k in range(N)]
    def h(t): return abs(C*mp.cot(t)) - abs(D*mp.cot(t+e))
    prev = h(ts[0])
    for k in range(1, N):
        cur = h(ts[k])
        if prev*cur < 0:
            try:
                r = mp.findroot(h, (ts[k-1], ts[k]), solver='bisect')
                pts.add(r)
            except Exception:
                pts.add((ts[k-1]+ts[k])/2)
        prev = cur
    pts = sorted(p for p in pts if 0 <= p <= pi)
    return mp.quad(f, pts)

def J_direct(v, s, e):
    return I_direct((v-s)/2, (v+s)/2, e)

def J_closed(v, s, e):
    if s <= v:
        c = (v-s)/2; b = (v+s)/2
        xl = lambda z: 0 if z == 0 else z*mp.log(z/v)
        return 2*(xl(c)+xl(b))
    c = (s-v)/2; b = (s+v)/2
    if s*mp.sin(e) >= v:
        return 2*s*mp.log(mp.sin(e))
    th = mp.asin(s*mp.sin(e)/v)
    t1 = (th-e)/2
    return 2*s*mp.log(mp.sin(e)) + 2*(b*mp.log(mp.cos(t1)/mp.sin(t1+e)) - c*mp.log(mp.cos(t1+e)/mp.sin(t1)))

def R_closed(v, s, e):
    return J_closed(v, s, e) - 2*max(s-v, 0)*mp.log(mp.sin(e))

def Rs_formula(v, s, e):
    if s < v: return mp.log((v+s)/(v-s))
    D = mp.sqrt(max(v**2 - s**2*mp.sin(e)**2, 0))
    if s*mp.sin(e) >= v: return mp.mpf(0)
    return mp.log((s*mp.cos(e)-D)/(s*mp.cos(e)+D))

def Re_formula(v, s, e):
    if s <= v: return mp.mpf(0)
    D = mp.sqrt(max(v**2 - s**2*mp.sin(e)**2, 0))
    return 2*(v*mp.cos(e)-D)/mp.sin(e)

def Z(v, s, e):
    g = lambda t: mp.sqrt(max(v**2 - s**2*mp.sin(t)**2, 0))/mp.sin(t)
    pts = [e, pi/2]
    if s*mp.sin(e) < v < s:
        pts = [e, mp.asin(v/s), pi/2]
    return 2*mp.quad(g, pts)

random.seed(1)
maxerr = 0; worst = None
viol = []
cases = []
for _ in range(60):
    v = mp.mpf(random.uniform(0.05, 2)); s = mp.mpf(random.uniform(0, 3)); e = mp.mpf(random.uniform(0.02, float(pi/2)))
    cases.append((v, s, e))
# add special cases
cases += [(mp.mpf(1), mp.mpf(1), mp.mpf(0.3)), (mp.mpf(1), mp.mpf(0), mp.mpf(0.7)), (mp.mpf(0.5), mp.mpf(2), mp.mpf(0.1)), (mp.mpf(0.5), mp.mpf(2), mp.mpf(1.2))]
for (v, s, e) in cases:
    jd = J_direct(v, s, e); jc = J_closed(v, s, e)
    err = abs(jd-jc)
    if err > maxerr: maxerr = err; worst = (v, s, e, jd, jc)
    R = R_closed(v, s, e)
    if R > 1e-20: viol.append(('R>0', v, s, e, R))
    if abs(R) > max(2*v, s+v)*mp.log(2) + 1e-20: viol.append(('|R| bound', v, s, e, R))
    # derivative checks (skip near thresholds)
    hstep = mp.mpf('1e-8')
    if abs(s-v) > 1e-3 and abs(s*mp.sin(e)-v) > 1e-3 and s > 1e-3:
        Rs_num = (R_closed(v, s+hstep, e)-R_closed(v, s-hstep, e))/(2*hstep)
        Re_num = (R_closed(v, s, e+hstep)-R_closed(v, s, e-hstep))/(2*hstep)
        if abs(Rs_num-Rs_formula(v, s, e)) > 1e-6: viol.append(('R_s', v, s, e, Rs_num, Rs_formula(v, s, e)))
        if abs(Re_num-Re_formula(v, s, e)) > 1e-6: viol.append(('R_e', v, s, e, Re_num, Re_formula(v, s, e)))
        if abs(Rs_num) > mp.log((v+s)/abs(v-s)) + 1e-9: viol.append(('|R_s| bound', v, s, e))
        if s > v and not (0 <= Re_num <= 2*v*mp.cot(e) + 1e-9): viol.append(('R_e range', v, s, e, Re_num))
    # E <= Z, equality for s>=v
    E = jc - 2*s*mp.log(mp.sin(e)); z = Z(v, s, e)
    if E > z + 1e-15: viol.append(('E>Z', v, s, e, E, z))
    if s >= v and abs(E-z) > 1e-12: viol.append(('E!=Z for s>=v', v, s, e, E, z))
print('max |J_direct - J_closed| =', mp.nstr(maxerr, 5), 'worst', [mp.nstr(w, 6) for w in worst])
print('violations:', len(viol))
for vv in viol[:20]: print([mp.nstr(w, 8) if not isinstance(w, str) else w for w in vv])
# endpoint value R(v,s,0+) for s>v: 2(c log c + v log v - b log b)
for (v, s) in [(0.5, 2.0), (1.0, 1.5), (0.2, 3.0)]:
    v = mp.mpf(v); s = mp.mpf(s); c = (s-v)/2; b = (s+v)/2
    lim = 2*(c*mp.log(c)+v*mp.log(v)-b*mp.log(b))
    print('R(v,s,0+) check', v, s, mp.nstr(R_closed(v, s, mp.mpf('1e-12')), 12), mp.nstr(lim, 12), ' >= -(s+v)log2:', lim >= -(s+v)*mp.log(2))
# reference I(-w,w,t) = 4 w log sin t
for (w, t) in [(0.7, 0.3), (2.0, 0.05), (0.1, 1.0)]:
    w = mp.mpf(w); t = mp.mpf(t)
    print('I(-w,w,t) direct', mp.nstr(I_direct(-w, w, t), 12), ' 4w log sin t', mp.nstr(4*w*mp.log(mp.sin(t)), 12))
# symmetry claims: exchange channels, reversal, reflection e->pi-e
C, D, e = mp.mpf(0.3), mp.mpf(-1.1), mp.mpf(0.9)
print('I(C,D,e), I(D,C,e), I(-C,-D,e), I(C,D,pi-e):', [mp.nstr(z, 10) for z in (I_direct(C, D, e), I_direct(D, C, e), I_direct(-C, -D, e), I_direct(C, D, pi-e))])
