# MEASURED diagnostics: R(n)=Lambda_c-[A(N)^2+kappa-1/N], N=n+1/2, A(z)=(2/pi)(log z+gamma+log(8/pi)).
# kappa = midpoint of PD-T271's open enclosure (half-width 5e-31). No fitting.
import sys, re
import mpmath as mp
mp.mp.dps = 40
pi = mp.pi; a = 2/pi; g = mp.euler; d = g + mp.log(8/pi)
kap = (mp.mpf('0.919710118388492535099518225790') + mp.mpf('0.919710118388492535099518225791'))/2
# H04 / H01 constants (MEASURED quadrature, constants.py)
CB = mp.mpf('0.3378987116946137090474372026405455')
betaB = mp.mpf('-0.0614858468583960839702868946412')
betaH = mp.mpf('-3.55127521601260996301315760499')
CH = kap + 1 - CB
A = lambda z: a*(mp.log(z) + d)

def parse(fn):
    out = {}
    for line in open(fn):
        if line.startswith('exit'):
            continue
        toks = line.split()
        if not toks:
            continue
        n = int(toks[0])
        balls = re.findall(r'\[([-0-9.e+]+) \+/- ([0-9.e+-]+)\]', line)
        vals = [mp.mpf(b[0]) for b in balls]
        rads = [mp.mpf(b[1]) for b in balls]
        out[n] = (vals, rads)
    return out

data = {}
for fn in sys.argv[1:]:
    for n, v in parse(fn).items():
        data.setdefault(n, v)
print("# n parity  Lambda_c  R=Lam-A(N)^2-kappa+1/N   N*R   N^2*R/logN   N^2*R   [radius]")
for n in sorted(data):
    vals, rads = data[n]
    L = vals[0]; N = mp.mpf(n) + mp.mpf(1)/2
    R = L - A(N)**2 - kap + 1/N
    print(n, 'even' if n % 2 == 0 else 'odd ', mp.nstr(L, 22), mp.nstr(R, 8), mp.nstr(N*R, 8),
          mp.nstr(N**2*R/mp.log(N), 8), mp.nstr(N**2*R, 8), mp.nstr(rads[0], 2))
print()
print("# component checks (fast runs only): H01 (1) and H04 (2)")
print("# n  m^2*[Hcal-A_m^2-C_H-(-a^2 log m+betaH)/m]/log m   n^2*|4V/(nm)-C_B-betaB/n| (H04 claims <=17)")
for n in sorted(data):
    vals, rads = data[n]
    if len(vals) < 3:
        continue
    m = n + 1
    H, V = vals[1], vals[2]
    eH = H - A(m)**2 - CH - (-a**2*mp.log(m) + betaH)/m
    eV = V - CB - betaB/n
    print(n, mp.nstr(m**2*eH/mp.log(m), 8), mp.nstr(n**2*eV, 8))
