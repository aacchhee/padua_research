# (1) Riesz/trigonometric Bernstein identity as written in companion cert lines 818-918 (40 digits).
# (2) Reflection identities of Sec.4 (lambda=S-Delta, Delta>=max(Qh,Qv), S symmetries, S(0)=Lambda_c) for small n.
import mpmath as mp, random, itertools
mp.mp.dps = 40
worst = 0
for d in range(1, 9):
    tau = [(2*j-1)*mp.pi/(2*d) for j in range(1, 2*d+1)]
    c = [(-1)**(j-1)/(4*d*mp.sin(tau[j-1]/2)**2) for j in range(1, 2*d+1)]
    for p in range(-d, d+1):
        val = sum(cj*mp.e**(1j*p*tj) for cj, tj in zip(c, tau))
        worst = max(worst, abs(val - 1j*p))
    cf = [sum(1j*l*mp.e**(-1j*l*tj) for l in range(-d+1, d+1))/(2*d) for tj in tau]
    worst = max(worst, max(abs(a-b) for a, b in zip(c, cf)))
    assert abs(sum(abs(x) for x in c) - d) < mp.mpf(10)**-30
print("Riesz: max multiplier/coefficient error d=1..8:", mp.nstr(worst, 3), "; sum|c_j|=d exact to 1e-30")
# (2) kernel via divided difference (companion loc. line 68-71), cardinal via reflection (ul:cardinal-reflection)
import math
def Pn(n, X): return math.cos((n+1)*math.acos(max(-1,min(1,X)))) + math.cos(n*math.acos(max(-1,min(1,X))))
def G(n, u, v):
    cu, cv = math.cos(u), math.cos(v)
    if abs(cu-cv) < 1e-9:   # divided difference -> derivative P_n'(cos u); use symmetric difference
        h = 1e-6; return (Pn(n, cu+h)-Pn(n, cu-h))/(2*h) - math.cos(n*u)
    return (Pn(n, cu)-Pn(n, cv))/(cu-cv) - math.cos(n*u)
random.seed(1)
maxdef = maxsym = 0.0; minQgap = 1e9
for n in (3, 4, 5, 6):
    m = n+1; N = n*m
    def S(al, be): return sum(abs(G(n, (r*math.pi+al)/n, (s*math.pi+be)/m)) for r in range(2*n) for s in range(2*m) if (r+s)%2)/(2*N)
    def lam_parts(J, K, al, be):
        th, ph = (J*math.pi+al)/n, (K*math.pi+be)/m
        tot = 0.0; Delta = 0.0
        for j in range(n+1):
            for k in range(m+1):
                if (j+k)%2: continue
                w = (0.5 if j in (0, n) else 1)*(0.5 if k in (0, m) else 1)*2/N
                g = [G(n, th+sg*j*math.pi/n, ph+et*k*math.pi/m) for sg in (1,-1) for et in (1,-1)]
                tot += w/4*abs(sum(g)); Delta += w/4*(sum(map(abs, g)) - abs(sum(g)))
        return tot, Delta
    for trial in range(6):
        J = random.randrange(0, n+1); K = random.randrange(0, m+1)
        if (J+K)%2 == 0: K = K+1 if K < m else K-1
        al = random.uniform(-1, 1); be = random.uniform(-1, 1)*(math.pi-abs(al))/math.pi
        th, ph = (J*math.pi+al)/n, (K*math.pi+be)/m
        if not (0 <= th <= math.pi and 0 <= ph <= math.pi): continue
        lam, Delta = lam_parts(J, K, al, be)
        maxdef = max(maxdef, abs(lam - (S(al, be) - Delta)))
        def Qv():
            return sum(abs(G(n,(r*math.pi+al)/n,(s*math.pi+be)/m))+abs(G(n,(r*math.pi+al)/n,((2*K-s)*math.pi+be)/m))
                       -abs(G(n,(r*math.pi+al)/n,(s*math.pi+be)/m)+G(n,(r*math.pi+al)/n,((2*K-s)*math.pi+be)/m))
                       for r in range(2*n) for s in range(2*m) if (r+s)%2)/(4*N)
        def Qh():
            return sum(abs(G(n,(r*math.pi+al)/n,(s*math.pi+be)/m))+abs(G(n,((2*J-r)*math.pi+al)/n,(s*math.pi+be)/m))
                       -abs(G(n,(r*math.pi+al)/n,(s*math.pi+be)/m)+G(n,((2*J-r)*math.pi+al)/n,(s*math.pi+be)/m))
                       for r in range(2*n) for s in range(2*m) if (r+s)%2)/(4*N)
        minQgap = min(minQgap, Delta - max(Qv(), Qh()))
        x, y = abs(al), abs(be)
        maxsym = max(maxsym, abs(S(al, be)-S(-al, be)), abs(S(al, be)-S(al+2*math.pi, be)), abs(S(x, y)-S(math.pi-x, math.pi-y)))
    # corner identity S(0,0) = lambda at the nonnode corner (-1,-1)
    lamc, D0 = lam_parts(n, m, 0.0, 0.0)
    maxsym = max(maxsym, abs(S(0.0, 0.0)-lamc), abs(D0))
print("[MEASURED] |lambda-(S-Delta)| max:", f"{maxdef:.1e}", " min(Delta-max(Qh,Qv)):", f"{minQgap:.1e}", " symmetry/corner max dev:", f"{maxsym:.1e}")
