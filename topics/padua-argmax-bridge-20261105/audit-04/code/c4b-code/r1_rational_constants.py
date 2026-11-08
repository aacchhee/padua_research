# Independent exact-rational reconstruction of the companion's stated rules
# (comparison-unified.tex lines 1268-1319), written from the text only.
from fractions import Fraction as F
import time
t0=time.process_time()
DEN=10**80
def rd(x): # round down to grid
    return F((x.numerator*DEN)//x.denominator, DEN)
def ru(x):
    return F(-((-x.numerator*DEN)//x.denominator), DEN)
# pi via Machin, alternating partial sums through 40 terms bracket arctan
def atan_br(xinv, N=40):
    x=F(1,xinv); s=F(0); sums=[]
    for k in range(N):
        s+= (-1)**k * x**(2*k+1)/(2*k+1); sums.append(s)
    a,b=sums[-2],sums[-1]
    return (min(a,b),max(a,b))
a5=atan_br(5); a239=atan_br(239)
pi_lo=16*a5[0]-4*a239[1]; pi_hi=16*a5[1]-4*a239[0]
pi_lo,pi_hi=rd(pi_lo),ru(pi_hi)
# log via series with J=48, argument reduced to [1,2] by powers of two
def log_lo_hi(z,J=48):
    k=0
    while z>2: z/=2; k+=1
    assert 1<=z<=2
    w=(z-1)/(z+1); s=F(0); wp=w; w2=w*w
    for j in range(J):
        s+=wp/(2*j+1); wp*=w2
    lo=2*s; hi=2*s+2*wp/((2*J+1)*(1-w2))
    return lo,hi,k
def LOG(z):
    lo,hi,k=log_lo_hi(z)
    L2=log_lo_hi(F(2))
    return (rd(lo+k*L2[0]), ru(hi+k*L2[1]))
log2=LOG(F(2)); 
# log is increasing: log(pi) in [log(pi_lo), log(pi_hi)]
logpi=(LOG(pi_lo)[0], LOG(pi_hi)[1])
# zeta brackets
def zeta(s):
    Z=sum(F(1,k**s) for k in range(1,11))
    lo=Z+F(1,(s-1)*10**(s-1))-F(1,2*10**s)
    hi=Z+F(2**(s-1),(s-1)*21**(s-1))
    return (lo,hi)
Zs={s:zeta(s) for s in [2,3,4,5,6,7,9]}
# gamma bracket
H256=sum(F(1,k) for k in range(1,257))
g_lo=rd(H256-LOG(F(257))[1]); g_hi=ru(H256-LOG(F(513,2))[0])
# interval arithmetic helpers
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def sub(a,b): return (a[0]-b[1],a[1]-b[0])
def mul(a,b):
    c=[a[0]*b[0],a[0]*b[1],a[1]*b[0],a[1]*b[1]]; return (min(c),max(c))
def sc(k,a): return (k*a[0],k*a[1]) if k>=0 else (k*a[1],k*a[0])
def cst(x): return (x,x)
def rdI(a): return (rd(a[0]),ru(a[1]))
# a_p
ap=[cst(F(1))]
acc=cst(F(0))
for p in range(1,4):
    acc=add(acc, sc(F(2,4**p), Zs[2*p]))
    ap.append(sub(cst(F(1)),acc))
lam=lambda s:(Zs[s][0]*(1-F(1,2**s)), Zs[s][1]*(1-F(1,2**s)))
bq=[lam(3)]
for q in range(1,4):
    bq.append(sub(lam(2*q+3),lam(2*q+1)))
ck=[]
for k in range(4):
    acc=cst(F(0))
    for p in range(k+1): acc=add(acc,mul(ap[p],bq[k-p]))
    ck.append(rdI(acc))
S=cst(F(0))
for k in range(4): S=add(S,sc(F(1,k+1),ck[k]))
pi2=(pi_lo**2,pi_hi**2)
eight_over_pi2=(F(8)/pi2[1],F(8)/pi2[0])
kap=mul(eight_over_pi2,S)
tail=F(8,3*5*4**4)
kap=(rd(kap[0]-tail),ru(kap[1]+tail))
print('tail',tail,'=1/480?',tail==F(1,480))
print('kappa in [%.9f, %.9f]'%(float(kap[0]),float(kap[1])))
print('claimed 917166e-6 < kappa < 921489e-6:', kap[0]>F(917166,10**6), kap[1]<F(921489,10**6))
# C_* = 4(gamma+log(8/pi))^2/pi^2 + kappa
log8pi=sub(sc(3,log2),logpi)
gl=add((g_lo,g_hi),log8pi)
Cs=add(mul(sc(4,mul(gl,gl)),(1/pi2[1],1/pi2[0])),kap)
print('C* in [%.9f, %.9f]'%(float(Cs[0]),float(Cs[1])),' claimed C*<1847940e-6:',Cs[1]<F(1847940,10**6), ' <4629/2500:',Cs[1]<F(4629,2500))
C0=add(sc(2,(g_lo,g_hi)),sc(4,log2)); k0=sub(C0,sc(2,logpi))
logpi2=sub(logpi,log2)
chk={
 '161/100<k0':k0[0]>F(161,100),'k0<9/5':k0[1]<F(9,5),
 'log(pi/2)<23/50':logpi2[1]<F(23,50),
 '23/40<gamma':g_lo>F(23,40),'gamma<3/5':g_hi<F(3,5),
 '69/100<log2':log2[0]>F(69,100),'log2<6932/10000':log2[1]<F(6932,10000),
 'logpi<23/20':logpi[1]<F(23,20),'logpi>11/10 (used, not listed)':logpi[0]>F(11,10),
 '197/20<pi^2':pi2[0]>F(197,20),'pi^2<10':pi2[1]<10,
 'pi>25/8':pi_lo>F(25,8),'pi<22/7':pi_hi<F(22,7),'pi>157/50':pi_lo>F(157,50),
 'gamma+log(8/pi)>3/2':(g_lo+log8pi[0])>F(3,2),'gamma+log(8/pi)<8/5':(g_hi+log8pi[1])<F(8,5),
}
for k,v in chk.items(): print(k,v)
# consequences (uc:scalar-constants) using only the listed rational brackets
k0u=F(9,5); pi2l=F(197,20); lp2u=F(23,50)
H0lb=F(9,20)-2*k0u/pi2l*lp2u
print('828/4925 equals 2*(9/5)*(20/197)*(23/50):',2*k0u/pi2l*lp2u==F(828,4925),' H0lb',H0lb, float(H0lb),'>7/25',H0lb>F(7,25))
C0lb=2*F(23,40)+4*F(69,100); print('C0>39/10',C0lb,C0lb>F(39,10))
dstar=F(39,10)*F(2,5)/10; print('d*>=',dstar,dstar==F(39,250))
g0ub=F(80,197)*(F(23,20)**2-F(69,100)**2); print('g0<',g0ub,float(g0ub),'<43/125',g0ub<F(43,125))
j=F(7,25)+F(39,250)-F(43,125); print('j>',j,j==F(23,250))
t0ub=2*F(6932,10000)/pi_lo; print('t0<',float(t0ub),'<221/500',t0ub<F(221,500))
d=F(9,4)-F(4629,2500); print('delta',d,d==F(249,625))
val=d*d+d*F(23,250)-F(221,500)**2; print('delta^2+delta j - t0^2 =',val,val==F(71,6250000))
# actual values for reference
import math
print('elapsed CPU s',time.process_time()-t0)
