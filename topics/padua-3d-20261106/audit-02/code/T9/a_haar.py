# Audit checks for T9-03 Haar/dual reduction and T9-PACK threshold.
import numpy as np, itertools as it, math, sympy as sp
rng=np.random.default_rng(11)
def group(gens,q,d):
    H={tuple([0]*d)}; frontier=list(H)
    while frontier:
        new=[]
        for h in frontier:
            for g in gens:
                x=tuple((h[i]+g[i])%q for i in range(d))
                if x not in H: H.add(x); new.append(x)
        frontier=new
    return np.array(sorted(H))
def dual(Hm,q,d):  # H^perp in (Z/q)^d
    K=np.array(list(it.product(range(q),repeat=d)))
    return K[np.all((K@Hm.T)%q==0,axis=1)]
def lattice_vectors(Hm,q,d,R):
    K=np.array([k for k in it.product(range(-R,R+1),repeat=d) if 0<sum(map(abs,k))<=R])
    return K[np.all((K@Hm.T)%q==0,axis=1)]
def moments_ok(Hm,q,d,a,D):
    th=2*np.pi*Hm/q+a  # angles
    worst=0
    for al in it.product(range(D+1),repeat=d):
        if sum(al)>D: continue
        mom=np.mean(np.prod(np.cos(np.array(al)*th),axis=1))
        # formula: 2^-d sum_eps e^{i eps al . a} [eps al in L]
        s=0
        for e in it.product([1,-1],repeat=d):
            k=np.array(e)*np.array(al)
            if np.all((Hm@k)%q==0): s+=np.exp(1j*k@a)
        worst=max(worst,abs(mom-s/2**d))
    return worst
d=3; bad=0; cnt=0; detok=True; foldok=True
for trial in range(60):
    q=int(rng.integers(2,13)); ng=int(rng.integers(1,3))
    gens=[tuple(int(x) for x in rng.integers(0,q,d)) for _ in range(ng)]
    Hm=group(gens,q,d); Hp=dual(Hm,q,d)
    detok&= len(Hm)*len(Hp)==q**d
    # det L via sympy HNF of generators of L: L = {k: Hm k = 0 mod q}; index [Z^d:L]=q^d/|Hp|
    a=np.zeros(d) if trial%2==0 else 2*np.pi*rng.integers(0,24,d)/24
    w=moments_ok(Hm,q,d,a,4); bad+= w>1e-12; cnt+=1
    if trial%2==0:
        # exactness degree vs shortest l1 dual vector
        L=lattice_vectors(Hm,q,d,9); sh=min(np.abs(L).sum(1)) if len(L) else 99
        exact=0
        for D in range(0,10):
            ok=all(abs(np.mean(np.prod(np.cos(np.array(al)*2*np.pi*Hm/q),axis=1)))<1e-12 for al in it.product(range(D+1),repeat=d) if sum(al)==D and D>0)
            if not ok: break
            exact=D
        if sh<99 and exact!=sh-1: print('MISMATCH exactness',q,gens,exact,sh)
        # folded nodes distinct count >= |H|/8 (exact residues)
        X={tuple(min(h[i]%q,(-h[i])%q) for i in range(d)) for h in map(tuple,Hm)}
        foldok&= len(X)*8>=len(Hm)
print('moment formula max err over',cnt,'random (H,a) cases: failures',bad,' |H||H^perp|=q^d:',detok,' fold bound:',foldok)
# 2-D Padua consistency n=1..12
for n in range(1,13):
    q=2*n*(n+1); g=(n+1, n)  # (pi/n, pi/(n+1)) = 2pi*(n+1)/q, 2pi*n/q
    Hm=group([g],q,2); assert len(Hm)==q
    L=lattice_vectors(Hm,q,2,2*n+1); sh=min(np.abs(L).sum(1))
    X={tuple(min(h[i]%q,(-h[i])%q) for i in range(2)) for h in map(tuple,Hm)}
    pts=np.cos(2*np.pi*np.array(sorted(X))/q)
    pad={(round(math.cos(i*math.pi/n),12),round(math.cos(j*math.pi/(n+1)),12)) for i in range(n+1) for j in range(n+2) if (i+j)%2==0}
    same= {tuple(np.round(p,12)) for p in pts}=={tuple(np.round(p,12)) for p in pad}
    # exactness of pushed-forward Haar through 2n-1 and failure at 2n
    th=2*np.pi*Hm/q
    ex=max(abs(np.mean(np.cos(a*th[:,0])*np.cos(b*th[:,1]))-(a==0 and b==0)) for a in range(2*n) for b in range(2*n-a))
    fail=max(abs(np.mean(np.cos(a*th[:,0])*np.cos(b*th[:,1]))) for a in range(2*n+1) for b in [2*n-a])
    if n<=4 or n==12: print('2D n',n,'|H|',len(Hm),'shortest dual l1',sh,'folded',len(X),'(n+1)(n+2)/2',(n+1)*(n+2)//2,'equals Padua pts',same,'exact err',ex,'deg2n moment',fail)
    assert sh==2*n and len(X)==(n+1)*(n+2)//2 and same and ex<1e-12 and fail>0.1
print('2D Padua checks n=1..12 passed')
# phase counterexample
print('H={0}, a=pi/2: T1(0)=',math.cos(math.pi/2),' T2(0)=',math.cos(math.pi),' (arcsine moments 0,0)')
# threshold algebra
n=sp.symbols('n',positive=True)
N=(n+1)*(n+2)*(n+3)/6
print('19n^3/108 - N  *108 =',sp.expand(108*(sp.Rational(19,108)*n**3-N)),'; n^3/(6*18/19)=',sp.Rational(19,108))
f=lambda n:n**3-108*n*n-198*n-108
neg=[m for m in range(1,200001) if f(m)<=0]; print('f<=0 exactly for n in [1,%d]; f(109)=%d f(110)=%d'%(max(neg),f(109),f(110)), 'contiguous:',neg==list(range(1,max(neg)+1)))
print('octahedron |x|_1<1 volume in R^3 = 2^3/3! =',sp.Rational(8,6),' times n^3')
