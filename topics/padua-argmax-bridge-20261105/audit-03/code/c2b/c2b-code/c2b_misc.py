import numpy as np
PI=np.pi; rng=np.random.default_rng(11)
sinc=lambda t: np.sinc(t/PI)
W={}
def upd(k,v): W[k]=max(W.get(k,-np.inf),v)
# f_j closed form 4a/(w^2-z^2) for ALL j (L2559-2560)
for _ in range(2000):
    x=rng.uniform(0,PI); y=rng.uniform(0,PI-x)
    for r,b in ((1,y),(1,-y),(2,-y)):
        ce,cd=np.cos((x+b)/2),np.cos((x-b)/2); a=ce*cd; w=r*PI+b
        for j in range(-10+((1-r)%2),11,2):
            z=j*PI+x
            if abs(abs(z)-w)<1e-6 or w<1e-6: continue
            sm=(-1)**((r-j-1)//2); sp=(-1)**((j+r-1)//2)
            fj=(ce*sm*sinc((z-w)/2)+cd*sp*sinc((z+w)/2))/w
            upd("f_j - 4a/(w^2-z^2) all j", abs(fj-4*a/(w*w-z*z)))
# c_e+c_d <= w (L2585) on full triangle
for _ in range(20000):
    x=rng.uniform(0,PI); y=rng.uniform(0,PI-x)
    for r,b in ((1,y),(1,-y),(2,-y)):
        upd("(c_e+c_d)/w", (np.cos((x+b)/2)+np.cos((x-b)/2))/(r*PI+b))
# h_2 bound r0 (L2764), via truncated series + tail
r0=np.log(2.5)+1/18
for t in np.linspace(0,1,101):
    k=np.arange(2,200000); s=-np.log(2+t-0.5)+np.sum(1/(k+t)-np.log((k+t+0.5)/(k+t-0.5)))
    upd("|h_2(t)|/r0", abs(s)/r0)
# far K>1/6, |H_h-1|<=u^2 (L2620-2621)
for n in (32,64,320):
    m=n+1
    for w in np.linspace(0.01,2*PI,40):
        v=w/m
        for u in np.linspace(2*w/n,PI,400):
            K=sinc((u+v)/2)*sinc((u-v)/2); Hh=(1+np.cos(v))/(2*K)
            upd("far 1/(6K)",1/(6*K)); upd("far |H_h-1|/u^2",abs(Hh-1)/u**2)
# elementary inequalities
z=np.linspace(1e-6,PI/2,100001)
upd("(1/z-cot z)/(pi z/6)", ((1/z-1/np.tan(z))/(PI*z/6)).max())
upd("-log(sin z/z)/(z^2/3)", (-np.log(np.sin(z)/z)/(z**2/3)).max())
fa=2/np.tan(z/2)-4/z
upd("|f_a'|/a", np.abs(np.gradient(fa,z)).max()); upd("|f_a|/(a z)",(np.abs(fa)/z).max())
for m in (33,100):
    w=np.linspace(1e-3,2*PI,1000); d=1/(2*m*np.sin(w/(2*m)))-1/w
    upd("prefactor err/(w/(20m^2))",(d/(w/(20*m*m))).max()); upd("prefactor err >=0 viol", (-d).max())
t=np.linspace(1e-6,1,10001); upd("(1-tau)/(2t^2/5) |t|<1", ((1-t/np.tan(t))/(2*t*t/5)).max())
u=np.linspace(1e-6,PI/4,10001); upd("(1-u cot u)/u^2",((1-u/np.tan(u))/u**2).max())
upd("|(u cot u)'|/(2u)",(np.abs(1/np.tan(u)-u/np.sin(u)**2)/(2*u)).max())
# L_n' norm (L3486-3489)
for n in (32,33,64):
    Hn=sum(1/k for k in range(1,n+1))
    for th in np.linspace(-0.55,0.55,23):
        ks=np.arange(-(n//2),n-(n//2))
        targ=(ks*PI+th)/n
        Lp=np.cos(th)/np.tan(targ)-np.sin(th)/n/np.sin(targ)**2
        k0=ks==0
        if abs(th)>1e-9:
            pass
        else:
            Lp[k0]=0.0
        upd("||L_n'||_1/((9/8) n H_n)", np.abs(Lp).sum()/(9/8*n*Hn))
# relative half-line inputs (L3279-3282)
for n in (32,100,320):
    m=n+1
    for j in range(2,n//2+1):
        v0=PI*j/m
        for y in np.linspace(0,1,21):
            for sgn in (1,-1):
                v=v0+sgn*y/m
                upd("cot(v/2)/(8/(3v0))", (1/np.tan(v/2))/(8/(3*v0)))
                upd("|cot diff|/(8pi^2 y/(9 m v0^2))", 0 if y==0 else abs(1/np.tan(v/2)-1/np.tan(v0/2))/(8*PI**2*y/(9*m*v0**2)))
for k_,v_ in W.items(): print(f"{k_:42s} worst={v_:.4g}")
