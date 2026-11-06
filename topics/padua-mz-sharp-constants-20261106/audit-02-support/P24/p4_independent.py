"""Auditor's independent evaluation of the P4 J512 trial Rayleigh quotient.
(A) mpmath 60-digit closed-form evaluation (own special functions: mpmath si/ci/euler).
(B) Canonical integral int_0^inf t g(t)^2 dt by float64 Gauss-Legendre on pole-centred
    panels (closed-form-free), with explicit analytic tail bound beyond T.
No repository code is imported."""
import json, sys, time
from fractions import Fraction
import mpmath as mp
import numpy as np
t0=time.time()
trial=json.load(open(sys.argv[1])); out=sys.argv[2]
u=[Fraction(float.fromhex(x)) for x in trial['u']]; J=len(u)
mp.mp.dps=60
U=[mp.mpf(x.numerator)/x.denominator for x in u]
pi=mp.pi
s=[(-1)**j for j in range(1,J+1)]
num=4*mp.fsum(s[k]*U[k] for k in range(J))**2
om=[2*(s[j-1]+j*pi*mp.si(j*pi)) for j in range(1,J+1)]
num+=mp.fsum(om[k]*U[k]**2 for k in range(J))
d=[mp.euler+mp.log(2*j*pi)-mp.ci(2*j*pi) for j in range(1,J+1)]
diag=mp.fsum(2*(j*pi*mp.si(2*j*pi)+d[j-1])*U[j-1]**2 for j in range(1,J+1))
off=mp.mpf(0)
for j in range(2,J+1):
    dj=d[j-1]; Uj=U[j-1]
    acc=mp.fsum(s[i-1]*(i*i*dj-j*j*d[i-1])/(i*i-j*j)*U[i-1] for i in range(1,j))
    off+=4*s[j-1]*Uj*acc
den=diag+off
q=num/den
# spot check: d_j against its integral representation 2*int_0^a sin^2 v/v dv
spot={j:float(d[j-1]-2*mp.quad(lambda v: mp.sin(v)**2/v,mp.linspace(0,j*pi,4*j+1))) for j in (1,7,8,40)}
# (B) closed-form-free quadrature of the denominator
u64=np.array([float(x) for x in u]); jj=np.arange(1,J+1); a=np.pi*jj
c=2*np.array(s)*a**2*u64
def g_panel(k,z):
    t=k*np.pi+z
    if k==0:
        S=(c[None,:]/((t[:,None]-a[None,:])*(t[:,None]+a[None,:]))).sum(1)
        return np.sinc(t/np.pi)*S, t
    mask=np.ones(J,bool)
    if k<=J: mask[k-1]=False
    dm=((k-jj[mask])*np.pi+z[:,None])*((k+jj[mask])*np.pi+z[:,None])
    S=(c[mask][None,:]/dm).sum(1)
    sint=((-1)**k)*np.sin(z)
    g=sint/t*S
    if k<=J:
        g+=c[k-1]*((-1)**k)*np.sinc(z/np.pi)/(t*(2*a[k-1]+z))
    return g,t
def integrate(K,n):
    x,w=np.polynomial.legendre.leggauss(n)
    tot=0.0
    z=(x+1)*np.pi/4; g,t=g_panel(0,z); tot+=np.sum(w*t*g*g)*np.pi/4
    z=x*np.pi/2
    for k in range(1,K+1):
        g,t=g_panel(k,z); tot+=np.sum(w*t*g*g)*np.pi/2
    return tot
K=1<<15
T=(K+0.5)*np.pi
I40=integrate(K,40); I24=integrate(K,24)
M0=abs(c.sum()); R=np.sum(np.abs(c)*a**2)/(1-(a[-1]/T)**2)
tail=M0**2/(4*T**4)+2*M0*R/(6*T**6)+R**2/(8*T**8)
num_f=float(num)
res=dict(J=J,mp_dps=60,closed_form_numerator=mp.nstr(num,40),closed_form_denominator=mp.nstr(den,40),
 closed_form_quotient=mp.nstr(q,40),target='1.0044369',margin=mp.nstr(q-mp.mpf(10044369)/10**7,20),
 d_integral_spotcheck_diff=spot,
 quadrature=dict(T=T,panels=K,gl40=I40,gl24=I24,gl40_minus_gl24=I40-I24,tail_upper_bound=tail,
   den_closed_minus_quad=float(den)-I40,
   quotient_lower_from_quad=num_f/(I40+tail+abs(I40-I24)+1e-12)),
 seconds=time.time()-t0)
json.dump(res,open(out,'w'),indent=1); print(json.dumps(res,indent=1))
