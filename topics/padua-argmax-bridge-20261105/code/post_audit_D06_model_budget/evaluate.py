"""D06 scalar-only preregistered bound evaluation; no kernel imports."""
import time
START = time.process_time()
import resource
resource.setrlimit(resource.RLIMIT_CPU, (9, 10))
import csv
import json
from decimal import Decimal as D, localcontext, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction as Q
from pathlib import Path
import mpmath as mp
mp.mp.dps = 80
PREC = 50

def directed(fn, rounding):
    with localcontext() as ctx:
        ctx.prec = PREC
        ctx.rounding = rounding
        return fn()

class I:
    def __init__(self, a, b=None):
        self.a = D(a)
        self.b = self.a if b is None else D(b)
    @staticmethod
    def cast(x):
        return x if isinstance(x, I) else I(x)
    def __add__(self, other):
        o = I.cast(other)
        return I(directed(lambda:self.a+o.a, ROUND_FLOOR),
                 directed(lambda:self.b+o.b, ROUND_CEILING))
    __radd__ = __add__
    def __neg__(self):
        return I(self.b.copy_negate(), self.a.copy_negate())
    def __sub__(self, other): return self + -I.cast(other)
    def __rsub__(self, other): return I.cast(other) + -self
    def __mul__(self, other):
        o = I.cast(other)
        pairs = [(x,y) for x in (self.a,self.b) for y in (o.a,o.b)]
        return I(min(directed(lambda:x*y,ROUND_FLOOR) for x,y in pairs),
                 max(directed(lambda:x*y,ROUND_CEILING) for x,y in pairs))
    __rmul__ = __mul__
    def __truediv__(self, other):
        o = I.cast(other)
        assert not o.a <= 0 <= o.b
        pairs = [(x,y) for x in (self.a,self.b) for y in (o.a,o.b)]
        return I(min(directed(lambda:x/y,ROUND_FLOOR) for x,y in pairs),
                 max(directed(lambda:x/y,ROUND_CEILING) for x,y in pairs))
    def __rtruediv__(self, other): return I.cast(other)/self
    def __pow__(self, exponent):
        assert exponent in (2,)
        return self*self

def ilog(x):
    x=I.cast(x)
    assert x.a > 0
    with localcontext() as ctx:
        ctx.prec=PREC
        lo=x.a.ln().next_minus()
        hi=x.b.ln().next_plus()
    return I(lo,hi)

def imax(*xs):
    xs=[I.cast(x) for x in xs]
    return I(max(x.a for x in xs),max(x.b for x in xs))

def atan_bounds(q, count):
    s=sum((Q((-1)**k,(2*k+1)*q**(2*k+1)) for k in range(count)),Q(0))
    nxt=Q((-1)**count,(2*count+1)*q**(2*count+1))
    return min(s,s+nxt),max(s,s+nxt)

a,b=atan_bounds(5,70)
c,d=atan_bounds(239,20)
pl,pu=16*a-4*d,16*b-4*c
PI=I(directed(lambda:D(pl.numerator)/D(pl.denominator),ROUND_FLOOR),
     directed(lambda:D(pu.numerator)/D(pu.denominator),ROUND_CEILING))

def components(n,a,p,P,d,U,H,pi,log,maxi):
    m=n+1; L=log(n); R=2; delta=pi/8; unit=pi/pi
    half=pi/pi/2
    x=delta*m/pi
    hr=log(R+half)+1/(8*(R-half)**2)
    cx=(5+half*log(x+half))/(2*(x-half))+(6+half*log(x+half))/(8*(x-half)**2)
    mesh=(2*R+3)*L/(2*m)+2*cx+(8+hr)/n+half/(n*n)
    row=(10*R+39+6*L)/n+unit*200*(R+2)*(R+1)**2/(n*n)
    rows=(4+L)/n+(2*R-1)*row
    collision=(unit*2/m)*(7+(2/pi)*(3+2*log(unit*4*m/R)))+5/(unit*n*n*m)+1/(unit*n*m)
    e4=mesh+rows+collision
    ed04=((52*a/(pi*pi)+352*P/(3*pi))*H+7*a+2*P/pi)/n+10/(pi/pi*n*n)+20*a*H/(pi*n*n)
    dpole=10/(pi/pi*n*n)+20*a*(1+L)/(pi*n*n)
    u=p/2; sb=half+4*a/delta; f=log(pi/delta)
    iszero=(u.a==u.b==0) if isinstance(u,I) else (u==0)
    entropy=pi*0 if iszero else 2*u*(1+log((sb+u)/u))
    astar=(1+8*a/delta)/pi; va=16*a/(pi*delta)
    vstar=2*U/delta+6; vv=4*U/delta+23
    jstar=maxi(5,2*sb*f+maxi(2*u,sb+u)*log(2))
    vj=(16*a/delta+4*sb)*f+3*entropy+2*(sb+u)*log(2)+20
    wstar=vstar+jstar/pi; vw=vv+vj/pi
    interior=((va/2+9*astar)*L+vw/2+5*wstar+4*vstar+(d/pi)*(4+5*log(m)))/m
    h=pi/m; eps=h*(R-half); lam=h*(R+half)
    def W(z): return 7+(P/pi)*(3+2*log(4*pi/z))
    tz_bv=(32+6*log(6/eps))/(2*m)
    tz_init=(2*lam/pi)*(7+(P/pi)*(5+2*log(4*pi/lam)))
    tz_upper=W(delta-h/2)/m; tz_holes=2*W(h*R)/m
    tz=tz_bv+tz_init+tz_upper+tz_holes
    total=ed04+e4+interior+dpole+tz
    return [ed04,mesh,rows,collision,e4,interior,dpole,tz_bv,tz_init,tz_upper,tz_holes,tz,total]

def phi0(t):
    t=t-mp.floor(t)
    if t==0: return mp.mpf(1)
    return mp.sin(mp.pi*t)*(-mp.digamma(t)-mp.digamma(1-t)-2*mp.log(mp.pi))/mp.pi

def phase_inputs(label,alpha,beta):
    if label=='midpoint':
        return mp.mpf(0),mp.mpf(1),mp.mpf(2),mp.mpf(0),mp.mpf(1)
    a=(mp.cos(alpha)+mp.cos(beta))/2
    p=mp.sin(alpha); q=mp.sin(beta)
    ce=mp.cos((alpha+beta)/2); cd=mp.cos((alpha-beta)/2)
    U=abs(ce*phi0(mp.mpf('0.5')+(alpha-beta)/(2*mp.pi))
          +cd*phi0(mp.mpf('0.5')+(alpha+beta)/(2*mp.pi)))
    return a,p,p+q,max(q-p,mp.mpf(0)),U

NS=[512,1000,2048,4096,10000,20000,50000,100000]
PHASES=[('zero',mp.mpf(0),mp.mpf(0)),('quarter',mp.mpf(1)/4,mp.mpf(1)/4),
        ('axis',mp.mpf(69)/50,mp.mpf(0)),('diag145',mp.mpf(29)/20,mp.mpf(29)/20),
        ('midpoint',mp.pi/2,mp.pi/2)]
out=Path(__file__).resolve().parent/'evidence.csv'
metadata={}
with out.open('w',newline='') as handle:
    writer=csv.writer(handle)
    writer.writerow(['kind','phase','n','E_D04','e_mesh','e_rows','e_collision','e4','I_n','D_pole','TZ_BV','TZ_initial','TZ_upper','TZ_holes','T_Z','total'])
    for label,alpha,beta in PHASES:
        vals=phase_inputs(label,alpha,beta)
        metadata[label]=dict(zip(['a','p','P','d','absU0'],[mp.nstr(v,25) for v in vals]))
        for n in NS:
            data=components(n,*vals,mp.harmonic(n),mp.pi,mp.log,max)
            writer.writerow(['MEASURED',label,n]+[mp.nstr(v,12) for v in data])
    for n in NS:
        data=components(n,I(1),I(1),I(2),I(1),I(8),1+ilog(n),PI,ilog,imax)
        def upper(x):
            with localcontext() as ctx:
                ctx.prec=PREC
                return str(x.b.quantize(D('1e-12'),rounding=ROUND_CEILING))
        writer.writerow(['UPPER_DECIMAL','uniform',n]+[upper(v) for v in data])
print(json.dumps({'cpu_seconds':time.process_time()-START,'output_bytes':out.stat().st_size,
                  'output':str(out),'actual_inputs':metadata,'uniform_inputs':
                  {'a':1,'p':1,'P':2,'d':1,'absU0':8,'H':'1+log n'},
                  'pi_interval':[str(PI.a),str(PI.b)]},sort_keys=True))
