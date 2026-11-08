import sys, random, time
sys.path.insert(0,'/tmp/claude-0/-home-user-padua-research/8833296e-cd9e-51d7-9205-e1ddfbc5960f/scratchpad/audit3/pylib')
import mpmath as mp
mp.mp.dps=30
t0c=time.process_time()
pi=mp.pi
random.seed(20261108)
def rep(name,ok,extra=''): print(('PASS ' if ok else 'FAIL ')+name,extra)
nu=lambda p: 1 if p==0 else 2
def Gsum(n,u,v):
    s=0
    for p in range(n+1):
        cp=mp.cos(p*u)
        for q in range(n+1-p):
            s+=nu(p)*nu(q)*cp*mp.cos(q*v)
    return s-mp.cos(n*u)
def Gdd(n,u,v):
    P=lambda c: mp.chebyt(n+1,c)+mp.chebyt(n,c)
    return (P(mp.cos(u))-P(mp.cos(v)))/(mp.cos(u)-mp.cos(v))-mp.cos(n*u)
# (a) divided-difference form = eq:angular-kernel sum
mx=0
for n in [3,7,10]:
    for _ in range(5):
        u=mp.mpf(random.uniform(0,2*3.14159)); v=mp.mpf(random.uniform(0,2*3.14159))
        mx=max(mx,abs(Gsum(n,u,v)-Gdd(n,u,v)))
rep('divided-difference form equals eq:angular-kernel sum',mx<1e-20,'%.1e'%mx)
# (b) row identity and offsets
mx=0; mxo=0; mxw=0
for n in [7,12,33]:
    m=n+1
    for _ in range(6):
        x=mp.mpf(random.uniform(0,1.5)); y=mp.mpf(random.uniform(0,1.5))
        ce=mp.cos((x+y)/2); cd=mp.cos((x-y)/2); a=ce*cd; p=mp.sin(x); q=mp.sin(y)
        for r in [random.randrange(2*m) for _ in range(3)]:
            d=(1-r)%2; v=(r*pi+y)/m
            Cm=(p-q-2*a*mp.cot(v/2))/4; Cp=(p+q+2*a*mp.cot(v/2))/4
            em=mp.mpf(1)/2+(x-y+v)/(2*pi); ep=mp.mpf(1)/2+(x+y-v)/(2*pi)
            # weight identity
            mxw=max(mxw,abs(Cm+ce*mp.sin(pi*em)/(2*mp.sin(v/2))),abs(Cp-cd*mp.sin(pi*ep)/(2*mp.sin(v/2))))
            for k in [random.randrange(n) for _ in range(3)]:
                u=(d*pi+x+2*k*pi)/n
                lhs=(-1)**d*Gdd(n,u,v)/2
                rhs=Cm*mp.cot((u-v)/2)+Cp*mp.cot((u+v)/2)
                mid=(a*(1+mp.cos(v))-(p/2)*mp.sin(u)+(q/2)*mp.sin(v))/(mp.cos(u)-mp.cos(v))
                mx=max(mx,abs(lhs-rhs),abs(lhs-mid))
                o1=n*(u-v)/(2*pi)-em; o2=n*(u+v)/(2*pi)-ep
                mxo=max(mxo,abs(o1-mp.nint(o1)),abs(o2-mp.nint(o2)))
rep('row identity (both displayed forms)',mx<1e-18,'%.1e'%mx)
rep('fractional pole offsets eta_-/eta_+ mod 1',mxo<1e-20,'%.1e'%mxo)
rep('weight identity C_-=-c_e sin(pi eta_-)/(2sin(v/2)), C_+=c_d sin(pi eta_+)/(2 sin(v/2))',mxw<1e-20,'%.1e'%mxw)
# (c) pole estimate (uc:pole-error)
Cf=lambda t:-mp.digamma(t)-mp.digamma(1-t)
worst=0
for n in [2,3,5,8,13,32,33,100,101,512]:
    for t in [1e-6,0.01,0.1,0.3,0.5,0.77,0.999]:
        t=mp.mpf(t)
        N=mp.fsum(abs(mp.cot(pi*(k+t)/n)) for k in range(n))
        err=abs(N/n-(2*mp.log(n)+Cf(t)-2*mp.log(pi))/pi)*n**2
        worst=max(worst,err)
rep('pole estimate |N_n/n-(2L+C-2logpi)/pi|<=5/n^2',worst<=5,'max n^2*err=%.3f'%worst)
# (d) c''(pi/2) and pole-proof constants
cpp=lambda w: mp.diff(lambda s: mp.cot(s)-1/s, w, 2)
rep("-c''(pi/2)=16/pi^3",abs(-cpp(pi/2)-16/pi**3)<1e-15)
rep('pi^2/3+pi/4+1/(2pi)<5',pi**2/3+pi/4+1/(2*pi)<5,'%.4f'%(pi**2/3+pi/4+1/(2*pi)))
# (e) half-line defect
worst=0
for n in [8,32,100,400]:
    hs=pi/n
    for v in [0.001,0.05,0.3,0.9,1.5]:
        v=mp.mpf(v)
        if v>=pi/2: continue
        for t in [0.0,0.2,0.5,0.9]:
            t=mp.mpf(t); dd=v/hs
            S=mp.fsum(mp.cot(v+hs*(k+t)) for k in range(0,4*n) if v+hs*(k+t)<pi/2)
            val=abs(S+mp.log(mp.sin(v))/hs-(mp.log(dd)-mp.digamma(dd+t))/hs)
            worst=max(worst,val)
rep('half-line defect <=4/pi',worst<=4/pi,'max %.4f vs %.4f'%(worst,4/pi))
# (f) l_j partial fraction, constant pi*D0, cutoff recurrence
def ell(r,x,b,a):
    w=r*pi+b
    return mp.sin(b)/w+8*a*mp.fsum(1/(w**2-(j*pi+x)**2) for j in range(-r+1,r,2))
mx=0; mxc=0
f=lambda w: mp.sin(pi*(mp.mpf(1)/2+w/(2*pi)))/pi*(Cf(mp.mpf(1)/2+w/(2*pi)-mp.floor(mp.mpf(1)/2+w/(2*pi)))-2*mp.log(pi))
for (x,y) in [(0.3,0.2),(1.0,0.4),(0.05,1.2)]:
    x=mp.mpf(x);y=mp.mpf(y)
    ce=mp.cos((x+y)/2); cd=mp.cos((x-y)/2); a=ce*cd
    U0=ce*f(x-y)+cd*f(x+y); D0=U0/pi+4*a/pi**2*mp.log(pi)
    for b in [y,-y]:
        s=b/pi
        qp=(1+s+x/pi)/2; qm=(1+s-x/pi)/2
        for j in [2,3,5,9]:
            nuj=j+s
            lhs=ell(j,x,b,a)
            rhs=(D0+2*a/pi**2*(mp.digamma(j+qm)+mp.digamma(j+qp)))/nuj
            mx=max(mx,abs(lhs-rhs))
rep('l_j digamma form with constant D0',mx<1e-20,'%.1e'%mx)
# harmonic estimate
ok=all(0<=mp.log(w)-1/(2*w)-mp.digamma(w)<=1/(8*w**2) for w in [mp.mpf(z) for z in [1,1.3,2,5,40]])
rep('0<=log w-1/(2w)-psi(w)<=1/(8w^2)',ok)
# (g) mesh series telescoping
def hj(j,t):
    return -mp.log(j+t-mp.mpf(1)/2)+mp.nsum(lambda k:1/(k+t)-mp.log((k+t+mp.mpf(1)/2)/(k+t-mp.mpf(1)/2)),[j,mp.inf])
t=mp.mpf('0.37'); n=20
rep('h_2-h_n = sum_{k=2}^{n-1} 1/(k+t)',abs(hj(2,t)-hj(n,t)-mp.fsum(1/(k+t) for k in range(2,n)))<1e-20)
print('CPU',time.process_time()-t0c)
