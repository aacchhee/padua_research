# Worked example: row decomposition R_r/n ~ V(L,v_r), and E_n=S_n-M_inf vs bound.
# Float64/scipy measurement only (MEASURED, not a proof).
import numpy as np, math, time
from scipy import integrate, special
t0=time.process_time()
pi=math.pi
def J(v,s,e):
    # Lemma uc:cancellation-lemma closed forms, v,s>=0, 0<e<=pi/2
    if v==0 and s==0: return 0.0
    if s<=v:
        c=(v-s)/2; b=(v+s)/2
        xl=lambda z: z*math.log(z/v) if z>0 else 0.0
        return 2*(xl(c)+xl(b))
    c=(s-v)/2; b=(s+v)/2
    if s*math.sin(e)>=v: return 2*s*math.log(math.sin(e))
    th=math.asin(s*math.sin(e)/v); t1=(th-e)/2
    val=2*s*math.log(math.sin(e))+2*(b*math.log(math.cos(t1)/math.sin(t1+e)) - (c*math.log(math.cos(t1+e)/math.sin(t1)) if c>0 else 0.0))
    return val
def I(C,D,e):
    e=e%pi
    if e>pi/2: e=pi-e
    return J(abs(C+D),abs(D-C),e)
def I_quad(C,D,e):
    g=lambda t: abs(C/math.tan(t)+D/math.tan(t+e))-abs(C/math.tan(t))-abs(D/math.tan(t+e))
    pts=sorted([x%pi for x in [pi/2,pi-e,pi/2-e]])
    return integrate.quad(g,0,pi,points=pts,limit=400,epsabs=1e-12)[0]
rng=np.random.default_rng(5)
mx=0
for _ in range(40):
    C,D=rng.normal(size=2); e=rng.uniform(0.05,3.0)
    mx=max(mx,abs(I(C,D,e)-I_quad(C,D,e)))
print('I closed-form vs quadrature max diff %.2e'%mx)
Cf=lambda t: -special.digamma(t)-special.digamma(1-t)
def Phi(t):
    t=t-math.floor(t)
    if t<1e-14: return 1.0
    return math.sin(pi*t)/pi*(Cf(t)-2*math.log(pi))
f=lambda w: Phi(0.5+w/(2*pi))
def model(x,y):
    ce=math.cos((x+y)/2); cd=math.cos((x-y)/2); a=ce*cd; p=math.sin(x); q=math.sin(y)
    U0=ce*f(x-y)+cd*f(x+y); B0=4*a/pi**2; D0=U0/pi+B0*math.log(pi)
    def coef(v):
        T=2*a/math.tan(v/2); return (p-q-T)/4,(p+q+T)/4
    def A(v):
        Cm,Cp=coef(v); return 2*(abs(Cm)+abs(Cp))/pi
    def B(v):
        Cm,Cp=coef(v)
        em=0.5+(x-y+v)/(2*pi); ep=0.5+(x+y-v)/(2*pi)
        return (ce*Phi(em)+cd*Phi(ep))/(2*math.sin(v/2))+I(Cm,Cp,v)/pi
    bfull=2*U0/pi+(8*a*math.log(2)+4*a*(math.log(a) if a>0 else 0)+2*(x*p+y*q))/pi**2
    Einf=a/3+a/pi**2*Cf(0.5+(x-y)/(2*pi))*Cf(0.5+(x+y)/(2*pi))
    integrand=lambda t: B(t)+B(2*pi-t)-2*U0/t-(8*a/pi)*math.log(t)/t
    val=integrate.quad(integrand,0,pi,points=[pi-x-y,pi-abs(x-y),pi/2],limit=500,epsabs=1e-11)[0]/pi
    Cinf=Einf+val
    return dict(a=a,p=p,q=q,A=A,B=B,coef=coef,bfull=bfull,Cinf=Cinf,Einf=Einf,U0=U0)
def Sn_rows(n,x,y,mod):
    m=n+1; L=math.log(n); res=[]
    k=np.arange(n)
    for r in range(2*m):
        d=(1-r)%2; v=(r*pi+y)/m
        u=(d*pi+x+2*k*pi)/n
        Cm,Cp=mod['coef'](v)
        Rr=np.sum(np.abs(Cm/np.tan((u-v)/2)+Cp/np.tan((u+v)/2)))
        res.append((r,v,Rr))
    return res
for (x,y) in [(0.4,0.3),(0.0,0.0)]:
    mod=model(x,y)
    print('phase',(x,y),'C_inf=%.6f E_inf=%.6f b_full=%.6f'%(mod['Cinf'],mod['Einf'],mod['bfull']))
    for n in [160,512]:
        L=math.log(n); m=n+1
        rows=Sn_rows(n,x,y,mod)
        Sn=sum(R for _,_,R in rows)/(n*m)
        Minf=4*mod['a']/pi**2*L**2+mod['bfull']*L+mod['Cinf']
        # row decomposition at a few ordinary rows
        dev=[]
        for (r,v,Rr) in rows:
            if r in (5,m//2-3,m+7,2*m-6):
                V=mod['A'](v)*L+mod['B'](v); dev.append((r,round(Rr/n,6),round(V,6),round(Rr/n-V,6)))
        print('  n=%d S_n=%.6f M_inf=%.6f E_n=%.6f'%(n,Sn,Minf,Sn-Minf))
        print('   rows (r, R_r/n, V(L,v_r), diff):',dev)
print('CPU',time.process_time()-t0)
