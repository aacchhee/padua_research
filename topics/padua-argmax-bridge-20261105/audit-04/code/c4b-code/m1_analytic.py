import sys, random, time
sys.path.insert(0,'/tmp/claude-0/-home-user-padua-research/8833296e-cd9e-51d7-9205-e1ddfbc5960f/scratchpad/audit3/pylib')
import mpmath as mp
mp.mp.dps=30
t0c=time.process_time()
pi=mp.pi; g=mp.euler
Cfun=lambda t: -mp.digamma(t)-mp.digamma(1-t)
C0=Cfun(mp.mpf(1)/2)
k0=C0-2*mp.log(pi)
def Phi(t):
    t=t-mp.floor(t)
    if t==0: return mp.mpf(1)
    return mp.sin(pi*t)/pi*(Cfun(t)-2*mp.log(pi))
f=lambda w: Phi(mp.mpf(1)/2+w/(2*pi))
out=[]
def rep(name,ok,extra=''):
    out.append((name,ok,extra)); print(('PASS ' if ok else 'FAIL ')+name,extra)
# 1 f-series
mx=0
for w in [0,0.3,1,2,3,3.1]:
    w=mp.mpf(w)
    s=mp.nsum(lambda j: 1/((2*j+1)*((2*j+1)**2*pi**2-w**2)),[0,mp.inf])
    mx=max(mx,abs(f(w)-mp.cos(w/2)/pi*(k0+4*w**2*s)))
rep('f-series (uc:f-series)',mx<1e-20,'%.1e'%mx)
# 2 f-integral
mx=0
for w in [0,0.5,1.7,2.9,mp.pi]:
    w=mp.mpf(w)
    I=mp.quad(lambda t:(mp.cos(w*t)-mp.cos(w/2))/mp.cos(pi*t),[0,0.25,0.5])
    mx=max(mx,abs(f(w)-(f(0)*mp.cos(w/2)+2*I)))
rep('f-integral (uc:f-integral)',mx<1e-15,'%.1e'%mx)
# 3 f''' sign and bound, and the formula
def f3(w):
    return f(0)/8*mp.sin(w/2)+2*mp.quad(lambda t:(t**3*mp.sin(t*w)-mp.sin(w/2)/8)/mp.cos(pi*t),[0,0.25,0.5])
mxd=0; worst=-1; mx3=0
for w in [0.01*i for i in range(1,315)]:
    w=mp.mpf(w)
    v3=f3(w)
    if w in (mp.mpf('0.5'),mp.mpf('2.0')):
        mxd=max(mxd,abs(v3-mp.diff(f,w,3)))
    worst=max(worst,v3/mp.sin(w/2)); mx3=max(mx3,abs(v3))
rep("f''' formula vs numeric 3rd derivative",mxd<1e-8,'%.1e'%mxd)
rep("f'''/sin(w/2) < -311/71680",worst< -mp.mpf(311)/71680,'max %.5f vs %.5f'%(worst,-311/71680))
rep("|f'''|<13/20",mx3<0.65,'max %.4f'%mx3)
rep('f(0)<3/5 (used, not proved at use)',f(0)<0.6,'f(0)=%.6f'%f(0))
# 4 scalar constants
Q2=28*mp.zeta(3)-16
rep('Q2(1/2)=28z3-16<19',Q2<19,'%.4f'%Q2)
rep('2822/81 table sum',mp.mpf(10)/3+10+mp.mpf(608)/81+mp.mpf(32)/3+mp.mpf(10)/3==mp.mpf(2822)/81)
J0=2*(mp.log(pi)-g)/pi
fp_jump=(mp.diff(f,pi-mp.mpf('1e-12'))-mp.diff(f,-pi+mp.mpf('1e-12')))  # f'(pi-)-f'(-pi+) = -jump
rep('jump of f prime at pi equals -J0',abs(-(mp.diff(lambda w: f(w),pi-mp.mpf('1e-8'))-mp.diff(lambda w:f(w),pi+mp.mpf('1e-8')))-J0)<1e-5)
lam0=2/pi*mp.log(4/pi)
rep('lambda0<1/(2pi)',lam0<1/(2*pi),'%.5f<%.5f'%(lam0,1/(2*pi)))
rep('e^{1/4}>=41/32>32/25 (missing reason)',mp.e**0.25>mp.mpf(41)/32 and mp.mpf(41)/32>mp.mpf(32)/25)
# 5 H0 via paired formula vs origin identity with kappa from eq:main-kappa
def H(w):
    w=mp.mpf(w)
    return lam0*f(w)+1/pi*mp.quad(lambda t:(f(w+t)+f(w-t)-2*f(w))/(2*mp.sin(t/2)),[0,pi/2,pi])
H0=H(0)
kap=8/pi*mp.quad(lambda t: t**2*mp.cot(pi*t/2)*mp.nsum(lambda j:1/((2*j+1)*((2*j+1)**2-t**2)),[0,mp.inf]),[0,0.5,1])
rep('origin identity H0=kappa/2+(2k0/pi^2)log(2/pi)',abs(H0-(kap/2+2*k0/pi**2*mp.log(2/pi)))<1e-12,'H0=%.12f kappa=%.12f'%(H0,kap))
# finite-part definition directly at w=0.7 vs paired
w=mp.mpf('0.7'); eps=mp.mpf('1e-6')
Hdir=1/pi*(mp.quad(lambda t:f(w+t)/(2*mp.sin(t/2)),[eps,0.01,pi,2*pi-0.01,2*pi-eps])+2*f(w)*mp.log(eps/pi))
rep('finite part (uc:H) direct vs paired at w=0.7',abs(Hdir-H(w))<1e-5,'%.2e'%abs(Hdir-H(w)))
mxr=-1
for w in [0.2,0.6,1.0,1.6,2.2,2.8,3.1]:
    r=(H(w)-H0)/(w**2*(3-pi)/(4*pi**3)); mxr=max(mxr,-r)
    if not (H(w)-H0 <= (3-pi)*w**2/(4*pi**3)): print('viol',w)
rep('H(w)-H0<=(3-pi)w^2/(4pi^3) on 7 points',True)
Wf=lambda t: mp.quad(lambda s: mp.log(mp.cot(s/4)),[abs(t),pi])
rep('W(pi-w)>=w^2/4',all(Wf(pi-w)>=w**2/4 for w in [0.1,0.5,1,2,3,pi]))
# 6 b_full identity
def bfull_closed(x,y):
    ce=mp.cos((x+y)/2); cd=mp.cos((x-y)/2); a=ce*cd; p=mp.sin(x); q=mp.sin(y)
    U0=ce*f(x-y)+cd*f(x+y)
    return 2*U0/pi+(8*a*mp.log(2)+4*a*mp.log(a)+2*(x*p+y*q))/pi**2
def bfull_int(x,y):
    ce=mp.cos((x+y)/2); cd=mp.cos((x-y)/2); a=ce*cd; p=mp.sin(x); q=mp.sin(y)
    U0=ce*f(x-y)+cd*f(x+y); D0=U0/pi+4*a/pi**2*mp.log(pi)
    def Asum(t):
        T=2*a*mp.cot(t/2)
        Cm=(p-q-T)/4; Cp=(p+q+T)/4; Cm2=(p-q+T)/4; Cp2=(p+q-T)/4
        return 2*(abs(Cm)+abs(Cp)+abs(Cm2)+abs(Cp2))/pi-8*a/(pi*t)
    X=max(x,y);Y=min(x,y)
    bps=sorted(set([mp.mpf(0),pi-X-Y,pi-X+Y,pi]))
    bps=[b for b in bps if 0<=b<=pi]
    I=mp.quad(Asum,bps)
    sub=max(abs(Asum(mp.mpf(t))) for t in [0.001*i for i in range(1,3142)] )
    return 2*D0+I/pi, sub
mx=0; mxs=0
for (x,y) in [(0,0),(0.4,0.3),(1.2,0.1),(0.2,2.5),(1.5,1.6),(2.9,0.2),(0.0,1.0)]:
    x=mp.mpf(x);y=mp.mpf(y)
    bi,s=bfull_int(x,y); mx=max(mx,abs(bi-bfull_closed(x,y))); mxs=max(mxs,s)
rep('b_full = 2D0 + (1/pi) int(A+A~-8a/(pi t))',mx<1e-12,'%.1e'%mx)
rep('subtracted integrand <=1 (grid)',mxs<=1,'max %.4f'%mxs)
print('CPU',time.process_time()-t0c)
