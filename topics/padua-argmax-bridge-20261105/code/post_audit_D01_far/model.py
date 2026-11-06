"""New read-only evaluator of frozen M_far: stable quadrature and EM tail.
All floating results are MEASURED, including quadrature error estimates.
"""
import importlib.util,math,pathlib,warnings
import numpy as np
from scipy.integrate import quad,IntegrationWarning
from scipy.special import digamma
from fractions import Fraction
PI=math.pi;R=64;DELTA=.01
OLD=pathlib.Path(__file__).resolve().parent.parent/'c06_far_profile_diagnostic.py'
spec=importlib.util.spec_from_file_location('frozen_far_model',OLD)
old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)

def phi(t):
 t=t%1.;t=min(t,1-t)
 if t==0:return 1.
 return math.sin(PI*t)/PI*(-digamma(t)-digamma(1-t)-2*math.log(PI))

def g_R(t):
 x=R+t;bs=[Fraction(x) for x in ['1','-1/2','1/6','0','-1/30','0','1/42','0','-1/30','0','5/66','0','-691/2730']];logx=math.log(x);harm=0.;ans=-.5*logx**2+.5*logx/x
 for k in range(1,13):
  if k%2==0:ans+=float(bs[k])/k*(logx-harm)/x**k
  harm+=1/k
 C=float(sum(math.comb(12,k)*abs(bs[k]) for k in range(13)))
 bound=C*x**-12*((logx+harm)/12+1/144)
 return ans,bound

def params(alpha,beta,edge=False):
 a=0. if edge else (math.cos(alpha)+math.cos(beta))/2
 ce=0. if edge else math.cos((alpha+beta)/2)
 cd=math.cos((alpha-beta)/2);p=math.sin(alpha);q=math.sin(beta)
 U=ce*phi(.5+(alpha-beta)/(2*PI))+cd*phi(.5+(alpha+beta)/(2*PI))
 B0=4*a/PI**2
 b=2*U/PI+(8*a*math.log(2)+(4*a*math.log(a) if a else 0)+2*(alpha*p+beta*q))/PI**2
 return dict(a=a,ce=ce,cd=cd,p=p,q=q,U=U,B0=B0,b=b)

def A(v,pr):
 # Full-domain max identity avoids subtraction of trigonometric near zeros.
 return max(pr['p'],abs(pr['q']+2*pr['a']/math.tan(v/2)))/PI

def B(v,alpha,beta,pr):
 V=(pr['ce']*phi(.5+(alpha-beta+v)/(2*PI))+pr['cd']*phi(.5+(alpha+beta-v)/(2*PI)))/(2*math.sin(v/2))
 eps=min(v,abs(v-PI),2*PI-v)
 return V+old.J(pr['p']/2,abs(pr['q']/2+pr['a']/math.tan(v/2)),eps)/PI

def marks(alpha,beta,delta):
 # Include coefficient kinks and I branch switches. Split fine dyadic
 # neighborhoods of pi, where equal-phase cancellation can be delicate.
 xs=[delta,PI/2,PI,3*PI/2,2*PI-delta]
 xs +=[PI-alpha+beta,PI+alpha+beta,PI+alpha-beta]
 xs += [PI+s*2.**(-j) for j in range(1,18) for s in [-1,1]]
 return sorted(set(x for x in xs if delta<=x<=2*PI-delta))

def integral(f,alpha,beta,delta,eps=2e-11):
 total=error=0.;messages=[]
 with warnings.catch_warnings(record=True) as ws:
  warnings.simplefilter('always',IntegrationWarning)
  xs=marks(alpha,beta,delta)
  for lo,hi in zip(xs,xs[1:]):
   value,estimate=quad(f,lo,hi,epsabs=eps,epsrel=eps,limit=400)
   total+=value;error+=estimate
  messages=[str(x.message) for x in ws]
 return total/PI,error/PI,messages

def profile(alpha,beta,L,edge=False,delta=DELTA,eps=2e-11):
 pr=params(alpha,beta,edge);D0=pr['U']/PI+pr['B0']*math.log(PI);kap=math.log(delta/PI)
 tails=[g_R(beta/PI),g_R(1-beta/PI)]
 cm=pr['B0']*kap**2+2*D0*kap-D0*(digamma(R+beta/PI)+digamma(R+1-beta/PI))+pr['B0']*sum(x[0] for x in tails)
 cr=math.sin(beta)/beta if beta else 1.
 cr+=sum(old.ell(alpha,beta,r) for r in range(1,R))+sum(old.ell(alpha,-beta,r) for r in range(1,R+1))
 integ,err,msg=integral(lambda v:B(v,alpha,beta,pr),alpha,beta,delta,eps)
 ia,iae,_=integral(lambda v:A(v,pr),alpha,beta,delta,eps)
 return dict(**pr,constant=cr+cm+integ,value=pr['B0']*L**2+pr['b']*L+cr+cm+integ,
   endpoint_rows=cr,mesh_constant=cm,integral=integ,integral_A=ia,b_end=pr['b']-ia,
   integration_error_estimate=err,integral_A_error_estimate=iae,warnings=msg,
   g_tail_error_bound=abs(pr['B0'])*sum(x[1] for x in tails),
   old_g_weighted_difference=pr['B0']*sum(tails[i][0]-old.g_R(t) for i,t in enumerate([beta/PI,1-beta/PI])),
   old_g_weighted_tail_bound=abs(pr['B0'])*sum((math.log(4096+t+.5)+2)/(8*(4096+t+.5)**2) for t in [beta/PI,1-beta/PI]),delta=delta)
