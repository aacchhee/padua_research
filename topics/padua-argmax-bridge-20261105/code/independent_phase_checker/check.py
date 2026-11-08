"""Independent paper-formula interval evaluator and exact closed-cover checker.
No production imports. See theory/J03-independent-phase-checker.md for soundness.
"""
from fractions import Fraction as F
from math import factorial, lcm
import numpy as np

def need(ok, why):
    if not ok: raise ValueError(why)

def atan_bounds(q, count=80):
    s = sum((F((-1)**j, (2*j+1)*q**(2*j+1)) for j in range(count)), F(0))
    t = F((-1)**count, (2*count+1)*q**(2*count+1))
    return min(s, s+t), max(s, s+t)

A, B = atan_bounds(5), atan_bounds(239)
PL, PH = (16*A[0]-4*B[1])*2**100, (16*A[1]-4*B[0])*2**100
PLO, PHI = F(PL.numerator//PL.denominator,2**100),F(-(-PH.numerator//PH.denominator),2**100)
U = F(1, 2**53)
PREF = float(PLO)
need(F(3) < PLO < PHI < F(22,7), 'pi bracket')
need(1-2*U <= PLO/F(PREF) <= PHI/F(PREF) <= 1+2*U, 'pi conversion')
COEF = [float(F((-1)**j, factorial(2*j+1))) for j in range(13)]
need(all(abs(F(c)-F((-1)**j,factorial(2*j+1))) <= U/F(factorial(2*j+1))
         for j,c in enumerate(COEF)), 'coefficient conversion')
need(sum((F(4)**j/F(factorial(2*j+1)) for j in range(13))) < 2, 'Taylor majorant')
need(F(2)**26/F(factorial(27)) < U, 'Taylor remainder')
def dn(x): return np.nextafter(x, -np.inf)
def up(x): return np.nextafter(x, np.inf)
def finite(*xs): need(all(np.all(np.isfinite(x)) for x in xs), 'nonfinite arithmetic')
def add(a,b): return dn(a[0]+b[0]), up(a[1]+b[1])
def neg(a): return -a[1], -a[0]
def mul(a,b):
    v=np.array([a[0]*b[0],a[0]*b[1],a[1]*b[0],a[1]*b[1]])
    return dn(v.min(axis=0)),up(v.max(axis=0))
def div(a,b):
    need(np.all((b[0]>0)|(b[1]<0)), 'division through zero')
    v=np.array([a[0]/b[0],a[0]/b[1],a[1]/b[0],a[1]/b[1]])
    return dn(v.min(axis=0)),up(v.max(axis=0))
def absolute(a):
    return np.maximum(0,np.maximum(a[0],-a[1])),np.maximum(abs(a[0]),abs(a[1]))
def total(a):
    lo,hi=(np.asarray(x).ravel().copy() for x in a)
    while lo.size>1:
        z=lo.size//2
        ll,hh=dn(lo[:2*z:2]+lo[1:2*z:2]),up(hi[:2*z:2]+hi[1:2*z:2])
        lo=np.append(ll,lo[-1:]) if lo.size%2 else ll
        hi=np.append(hh,hi[-1:]) if hi.size%2 else hh
    finite(lo,hi)
    return F(float(lo[0])),F(float(hi[0]))

def sinpi(num,den):
    need(isinstance(den,int) and 0<den<2**52, 'argument denominator range')
    num=np.asarray(num,dtype=np.int64)
    r=num%(2*den); sign=np.where(r>=den,-1.,1.)
    r=np.where(r>=den,r-den,r); r=np.minimum(r,den-r)
    t=PREF*(r/den); z=t*t
    p=np.full(t.shape,COEF[-1])
    for c in reversed(COEF[:-1]): p=p*z+c
    s=t*p; err=t*2.**-46
    lo,hi=dn(s-err),up(s+err)
    lo,hi=np.maximum(lo,0.),np.minimum(hi,1.)
    lo=np.where(r==0,0.,lo); hi=np.where(r==0,0.,hi)
    finite(lo,hi)
    return np.where(sign>0,lo,-hi),np.where(sign>0,hi,-lo)

def ratio(k,num,den):
    need(np.max(np.abs(num),initial=0)<2**62//k, 'integer multiplication overflow')
    a,b=sinpi(k*num,den),sinpi(num,den)
    zero=num%den==0
    b=(np.where(zero,1.,b[0]),np.where(zero,1.,b[1]))
    v=div(a,b)
    exact=k*np.where(((num//den)*(k-1))%2==0,1.,-1.)
    return np.where(zero,exact,v[0]),np.where(zero,exact,v[1])

def kernel(n,Uv,Vv,den,cosnum,cosden,parity):
    x,y=Uv+Vv,Vv-Uv
    d=add(mul(ratio(n+1,x,den),ratio(n+1,y,den)),
          mul(ratio(n,x,den),ratio(n,y,den)))
    c=sinpi(np.array([2*cosnum+cosden],dtype=np.int64),2*cosden)
    c=(np.where(parity%2==0,c[0][0],-c[1][0]),np.where(parity%2==0,c[1][0],-c[0][0]))
    return add(d,neg(c))

def geometry(n,a,b,actual=False):
    a,b=F(a),F(b); m=n+1; Q=lcm(a.denominator,b.denominator)
    aq,bq=a.numerator*(Q//a.denominator),b.numerator*(Q//b.denominator)
    # This Python-integer bound precedes every numpy multiplication.
    need(4*(n+1)*n*m*(abs(aq)+abs(bq)+4*Q)<2**62, 'geometry overflow')
    need(2*n*m*Q<2**52, 'geometry denominator')
    r=np.arange(n+1 if actual else 2*n,dtype=np.int64)[:,None]
    s=np.arange(m+1 if actual else 2*m,dtype=np.int64)[None,:]
    mask=(r+s)%2==(0 if actual else 1)
    return aq,bq,Q,np.broadcast_to(r,mask.shape)[mask],np.broadcast_to(s,mask.shape)[mask]

def S(n,a,b):
    aq,bq,Q,r,s=geometry(n,a,b); m=n+1
    h=kernel(n,(r*Q+aq)*m,(s*Q+bq)*n,2*n*m*Q,aq,Q,r)
    lo,hi=total(absolute(h)); return lo/(2*n*m),hi/(2*n*m)

def actual_lambda(n,xi,zeta):
    aq,bq,Q,j,k=geometry(n,1-F(xi),1-F(zeta),True); m=n+1
    tot=(np.zeros(j.shape),np.zeros(j.shape))
    for sg in (-1,1):
        for et in (-1,1):
            h=kernel(n,aq*n*m+sg*j*Q*m,bq*n*m+et*k*Q*n,2*n*m*Q,aq*n,Q,j)
            tot=add(tot,h)
    # w/4 = e_j f_k/(2nm); widen even scalings of subnormal endpoints.
    weight=np.where((j==0)|(j==n),.5,1.)*np.where((k==0)|(k==m),.5,1.)
    v=absolute(tot); lo,hi=total(mul(v,(weight,weight)))
    return lo/(2*n*m),hi/(2*n*m)

def fold(a,b): return (1-a,1-b) if a+b>1 or (a+b==1 and a>b) else (a,b)
def vertices(r):
    a,b,c,d=r
    return [(a,c),(a,d),(b,c),(b,d)]
def parse(tree,n):
    need(tree['format']=='FINAL-HYBRID-midpoint-v1' and tree['n']==n,'tree identity')
    stream=tree['preorder']; need(isinstance(stream,str) and len(stream)<100000,'tree length')
    stack=[(F(0),F(1),F(0),F(1))]; leaves=[]
    for tok in stream:
        need(bool(stack),'trailing tree tokens'); a,b,c,d=stack.pop()
        if tok=='a':
            h=(a+b)/2; stack.extend([(h,b,c,d),(a,h,c,d)])
        elif tok=='b':
            h=(c+d)/2; stack.extend([(a,b,h,d),(a,b,c,h)])
        else:
            need(tok in '.f','unknown tree token'); leaves.append((tok,(a,b,c,d)))
    need(not stack,'incomplete tree'); return leaves

def maximum(r,w,M,k,side=None):
    a,b,c,d=r; h=b-a; v=d-c
    cross=(w[3]-w[2]-w[1]+w[0])/(h*v)
    bx=(w[2]-w[0])/h-cross*c; by=(w[1]-w[0])/v-cross*a
    c0=w[0]-bx*a-by*c-cross*a*c
    px=M*PHI**2/2; py=px*k*k
    bx+=px*(a+b); by+=py*(c+d); c0-=px*a*b+py*c*d
    def val(x,y): return c0+bx*x+by*y+cross*x*y-px*x*x-py*y*y
    # Ax+By<=C, including every closed edge and the near/far overlap.
    hp=[(-1,0,-a),(1,0,b),(0,-1,-c),(0,1,d),(1,1,F(1))]
    if side=='near': hp.append((1,1,1/(2*PLO)))
    if side=='far': hp.append((-1,-1,-1/(2*PHI)))
    def inside(x,y): return all(A*x+B*y<=C for A,B,C in hp)
    pts=set()
    for i,(A,B,C) in enumerate(hp):
        for D,E,G in hp[i+1:]:
            det=A*E-B*D
            if det:
                x,y=(C*E-B*G)/det,(A*G-C*D)/det
                if inside(x,y): pts.add((x,y))
    if not pts: return None
    candidates=list(pts)
    for x,y in pts:
        for u,vv in pts:
            dx,dy=u-x,vv-y
            q2=cross*dx*dy-px*dx*dx-py*dy*dy
            q1=(bx+cross*y-2*px*x)*dx+(by+cross*x-2*py*y)*dy
            if q2<0:
                t=-q1/(2*q2)
                if 0<t<1: candidates.append((x+t*dx,y+t*dy))
    det=4*px*py-cross*cross
    if det:
        x,y=(2*py*bx+cross*by)/det,(2*px*by+cross*bx)/det
        if inside(x,y): candidates.append((x,y))
    return max(val(x,y) for x,y in candidates)

def floor(n,r):
    a=1-r*r/4; u=F(347,1000)*a-F(157,500)*r
    v=F(17,20)*a-r/2; w=F(779,750)*a-F(5,6)*r
    B=F(11711,48400)*u-F(120,157*n)*v-F(250,157*n)*w-F(100,3*n*n)*v
    return max(F(1,512 if n<64 else 64 if n<160 else 32),min(F(1,32 if n<64 else 20),B))

def read_rows(rows):
    out={}
    for a,b,h in rows:
        a,b=F(a),F(b); x=float.fromhex(h); finite(x)
        need((a,b) not in out,'duplicate premise'); out[a,b]=F(x)
    return out

def check(data,cache=None):
    n=data['n']; need(type(n) is int and 41<=n<512,'degree range')
    need(data['format']=='FINAL-HYBRID-kept-proof-v1','certificate format')
    need(data['pi_bracket']==['157/50','22/7'],'declared pi bracket')
    leaves=parse(data['tree'],n); method=data['norm']['method']
    need(method in ('TREE','GRID'),'norm method')
    need(not any(t=='f' for t,r in leaves) or method=='GRID','analytic leaf needs GRID')
    tier=('D29-radius41: max(1/512,min(1/32,B_n(r_B)))' if n<64 else
          'accepted C02: max(1/64,min(1/20,B_n(r_B)))' if n<160 else
          'accepted C02: max(1/32,min(1/20,B_n(r_B)))')
    need(data['floor']=={'tier':tier,'domain':'actual noncorner signed rho<=r_B<=1/2 only'},'floor metadata')
    af=data['analytic_far']
    need(af=={'kind':'ANALYTIC_E15_192','minimum_degree':192,
         'closed_normalized_guard':'abs(alpha/pi)+abs(beta/pi)>=1/2','primitive_gap':'3/100',
         'comparison':'S_n<true Lambda_c-3/100; physical lambda<=S_n',
         'dependencies':['E15 general E09 u-majorant','E08 full-phase absolute and one-sided origin',
         'E07 Hmax/E06 map','computer-assisted PD-T271','D32 physical signed chart']},'far metadata')
    keys=set()
    for tok,r in leaves:
        if r[0]+r[2]<=1 and tok=='.': keys.update(fold(*p) for p in vertices(r))
        if tok=='f': need(n>=192 and r[0]+r[2]>=F(1,2),'analytic far guard')
    grid={fold(F(i,4),F(j,4)) for i in range(5) for j in range(5-i)}
    if method=='GRID': keys.update(grid)
    stored=read_rows(data['S_upper_rows']); need(keys<=set(stored),'missing required S keys')
    need(all(0<=a and 0<=b and a+b<=1 for a,b in stored),'retained S key domain')
    keys.update(stored)
    cache={} if cache is None else cache
    def ev(kind,a,b):
        key=(kind,n,a,b)
        if key not in cache: cache[key]=(S if kind=='S' else actual_lambda)(n,a,b)
        lo,hi=cache[key]; need(lo<=hi,'invalid interval'); return lo,hi
    values={p:ev('S',*p) for p in sorted(keys)}
    need(all(lo<=stored[p] for p,(lo,hi) in values.items()),'stored upper below independent lower')
    W={p:hi for p,(lo,hi) in values.items()}; L=values[0,0][0]
    oldL=float.fromhex(data['origin_lower_hex']); finite(oldL)
    need(F(oldL)<=values[0,0][1],'stored origin lower above independent upper')
    k=F(n,n+1); radii=[]
    for tok,r in leaves:
        if r[0]+r[2]>1 or tok=='f': continue
        theta=PHI**2*((r[1]-r[0])**2+k*k*(r[3]-r[2])**2)/8
        need(theta<1,'tree norm theta')
        radii.append(max(W[fold(*p)] for p in vertices(r))/(1-theta))
    bound=max(W[p] for p in grid)/(1-PHI**2/64) if method=='GRID' else max(radii)
    M=F(-(-bound.numerator//bound.denominator)); near=[]; far=[]; used=[]
    for tok,r in leaves:
        if r[0]+r[2]>1 or tok=='f': continue
        ws=[W[fold(*p)] for p in vertices(r)]
        rad=min(F(1,2),PHI*(r[1]+r[3])); delta=floor(n,rad)
        q=maximum(r,ws,M,k,'near')
        if q is not None: near.append(L+delta-q); used.append(delta)
        q=maximum(r,ws,M,k,'far')
        if q is not None: far.append(L-q)
    need(all(x>0 for x in near+far),'strict leaf comparison')
    corner=data['corner']; lam=read_rows(data['lambda_upper_rows']); gap=None
    if corner['kind']=='ANALYTIC_E12_256':
        need(n>=256 and corner=={'kind':'ANALYTIC_E12_256',
             'theorem':'accepted E12-corner256 for every integer n>=256',
             'closed_patch':'[0,pi/4]^2 at both parity-correct actual corners','radial_squared_loss':'1/30',
             'dependencies':['E12 global signed-cardinal norm and squared Peano',
             'E08 full-phase absolute and one-sided origin','E11 closed half-pi model',
             'E07 Hmax/E06 map','computer-assisted PD-T271','D32 physical cover and parity']} and not lam,'analytic corner metadata')
    else:
        need(corner=={'kind':'ACTUAL_THREE','theorem':'accepted D08/D32 pi/4 by3pi/16; exact pi^4 losses'},'corner metadata')
        xy=[(F(1,4*n),F(0)),(F(0),F(3,16*(n+1))),(F(1,4*n),F(3,16*(n+1)))]
        need(set(lam)==set(xy),'actual lambda keys')
        loss=[]
        for p,d in zip(xy,[F(1,32),F(9,512),F(25,512)]):
            lo,hi=ev('lambda',*p); need(lo<=lam[p],'stored lambda upper below independent lower')
            loss.append((L-hi)/d)
        gap=min(loss)-M*PHI**4/6*max(F(1,32),k**4*F(9,512))
        need(gap>0,'strict corner descent')
    return {'n':n,'S_keys':len(keys),'lambda_keys':len(lam),'M':str(M),'L':str(L),
            'near_min':str(min(near)) if near else None,'far_min':str(min(far)) if far else None,
            'corner_gap':str(gap),'floor_min':str(min(used)) if used else None,
            'native_S_upper_contained':sum(hi<=stored[p] for p,(lo,hi) in values.items()),
            'native_S_upper_total':len(keys),'native_lower_contained':F(oldL)<=L,
            'scope':'independent substituted-bound recertification; native endpoints not all validated'}
