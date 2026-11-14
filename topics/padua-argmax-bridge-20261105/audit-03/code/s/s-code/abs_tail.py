# Planning scan [MEASURED, mpmath 30 digits, phase grids]: an "absolute-only" analytic tail.
# Uses ONLY these statements already proved in the paper (sections/comparison-unified.tex):
#   (G) |S_n - M_inf| <= Cbar_E + K_D*P          (uc:global-error), n>=32
#   (O) E_n(0) > -ebar                             (uc:origin-lower), n>=160   [variant: replace by Cbar_E]
#   (M) M_inf(phi)-M_inf(0) <= -u(T+j) + t0*p      (uc:model-loss),  j>23/250, t0<221/500
#   (F) noncorner floors on rho<=1/2: uniform 1/32 (n>=160)  [variant: tail floors F_near,F_small,F_h]
#   (P) squared-Peano corner descent with norm M(n) (ul:squared-peano, uc:analytic-norm)
# Gabs(phi) = u(T+j) - t0 p - Cbar_E - K_D P - e0,  e0 = ebar (or Cbar_E).
import mpmath as mp, sys, json
mp.mp.dps = 30
pi = mp.pi
j, t0 = mp.mpf(23)/250, mp.mpf(221)/500
def consts(n):
    n = mp.mpf(n); m = n + 1; L = mp.log(n); H = 1 + L
    T = (4*L**2 - 3*L)/pi**2; b0 = 4/pi**2; r0 = mp.log(mp.mpf(5)/2) + mp.mpf(1)/18
    D = ((52/pi**2)*H + 7)/n + 10/n**2 + 20*H/(pi*n**2)
    Mm = b0*(2*L + 2*r0)/n + (4 + b0*(L + 1/n))/(4*n**2 - 1) + b0/(2*n - 1)**2 \
         + (5 + b0*(mp.log(n + mp.mpf(1)/2) + 2))/(4*(n - mp.mpf(1)/2)**2)
    ebar = D + Mm + 1/n
    KD = ((6 + 16/(3*pi))*H + 2/pi)/n
    gn = 1 + mp.log(2 + 8*m/(3*pi)); MA = 1/pi + 4/pi**2
    Gg = (7*MA*L + mp.mpf(111)/2 + (63 + mp.log(2) + 4*mp.log(pi) + 7*mp.log(m) + 16*mp.log(2*m) + mp.mpf(3)/2*gn)/pi)/m
    Wn = (3*mp.log(m) + mp.log(2) + 2*mp.log(pi) + 2)/(pi*m)
    CE = D + Gg + (64 + 16*L)/n + 318/n**2 + Mm + Wn
    Mnorm = (4*L**2 + mp.mpf(79)/5*L)/pi**2 + mp.mpf(9)/4 + CE + 2*KD
    return dict(L=L, T=T, ebar=ebar, KD=KD, CE=CE, M=Mnorm, n=n)
def tail_floor(c, r):
    # min(F_near, F_small, F_h) from (ul:tail-floors), valid n>=64, r<=21/40
    n = c['n']; ar = 1 - r**2/4; pp = mp.mpf(22)/7
    eta = ar*(1 - (4*pp + r)/n) - r/2
    Fn = 2*eta/(pp + r)*n/(n + 1)*(mp.mpf(1)/4 - 1/n)
    Fs = mp.mpf(35)/286*(1 - 6/n)**2*(ar - r/2)
    Ar = mp.mpf(97)/100*ar - r/2
    Ih = mp.mpf(2303)/5000*ar - mp.mpf(471)/1250*r; Rh = mp.mpf(4837)/1875*ar - mp.mpf(5)/3*r
    Fh = mp.mpf(539)/1936*Ih - (140*Ar + 400*Rh)/(157*n) - 800*Ar/(3*n**2)
    return min(Fn, Fs, Fh)
def gabs(c, x, y, e0):
    u = 1 - (mp.cos(x) + mp.cos(y))/2; p = mp.sin(x); P = mp.sin(x) + mp.sin(y)
    return u*(c['T'] + j) - t0*p - c['CE'] - c['KD']*P - e0
def gates(n, origin='ebar', floor='uniform', N=40):
    c = consts(n); e0 = c['ebar'] if origin == 'ebar' else c['CE']
    # near noncorner rho<=1/2: min over grid of floor(rho)+Gabs ; floor(rho) uses radius r=rho rounded up
    worst_near = mp.inf
    for i in range(N + 1):
        rho = mp.mpf(i)/(2*N)
        fl = mp.mpf(1)/32 if floor == 'uniform' else tail_floor(c, max(rho, mp.mpf(1)/(2*N)))
        for k in range(N + 1):
            x = rho*k/N; y = rho - x
            worst_near = min(worst_near, fl + gabs(c, x, y, e0))
    worst_far = mp.inf
    for i in range(N + 1):
        rho = mp.mpf(1)/2 + (pi - mp.mpf(1)/2)*i/N
        for k in range(N + 1):
            x = rho*k/N; y = rho - x
            if x > pi or y > pi: continue
            worst_far = min(worst_far, gabs(c, x, y, e0))
    h = pi/4
    dA = min(gabs(c, h, 0, e0), gabs(c, 0, h, e0)); dD = gabs(c, h, h, e0)
    corner = min(dA, dD/2) - c['M']*pi**4/6144
    return dict(n=int(n), near=float(worst_near), far=float(worst_far), corner=float(corner),
                CE=float(c['CE']), ebar=float(c['ebar']), T=float(c['T']), M=float(c['M']))
if __name__ == '__main__':
    out = {}
    for origin in ('ebar', 'CE'):
        for floor in ('uniform', 'tail'):
            rows = [gates(n, origin, floor, N=24) for n in (320, 512, 1024, 2048, 3000, 4096, 6000, 8192, 16384, 32768)]
            out[f'{origin}/{floor}'] = rows
            print(f'== origin={origin} floor={floor}')
            for r in rows:
                print(f"n={r['n']:6d} CE={r['CE']:.4f} ebar={r['ebar']:.4f} T={r['T']:.2f} M={r['M']:.2f} "
                      f"near={r['near']:+.4f} far={r['far']:+.4f} corner={r['corner']:+.4f}")
    json.dump(out, open('abs_tail_out.json', 'w'), indent=1)
