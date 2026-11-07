#!/usr/bin/env python3
"""One frozen prospective D01-far attempt. Measurements are not proof."""
import ctypes,hashlib,json,math,pathlib,platform,resource,time
from fractions import Fraction
import numpy as np
import scipy
from scipy.special import gammaln,zeta,digamma
from scipy.integrate import quad
import build,model
HERE=pathlib.Path(__file__).resolve().parent;ROOT=HERE.parents[3]
RAW=ROOT/'local-output/argmax-bridge-20261105/post-audit-D01/far'
EVIDENCE=HERE.parents[1]/'evidence/d01-far.json'
def cpu():return sum(resource.getrusage(k).ru_utime+resource.getrusage(k).ru_stime for k in (resource.RUSAGE_SELF,resource.RUSAGE_CHILDREN))
def save(path,obj):path.write_text(json.dumps(obj,indent=2,allow_nan=False)+'\n')
def rat(x):return str(Fraction.from_float(x/math.pi))
def midpoint(a):return (a[:,0]+a[:,1])/2
start=cpu();wall=time.monotonic();resource.setrlimit(resource.RLIMIT_CPU,(570,570))
assert not EVIDENCE.exists(),'No overwrite of first receipt'
assert (HERE/'SPEC.md').exists(),'SPEC must precede native execution'
freeze=[build.identity(p) for p in sorted(HERE.glob('*')) if p.is_file() and p.suffix in ('.py','.cpp','.md')]
save(RAW/'prospective-freeze.json',dict(files=freeze,input_head='4cf68980fa0538b53e2aea7174ed6e5782a34908',cap=600,
 phases=[['.25','.25'],['1.38','0'],['1.45','1.45'],['pi/2','pi/2']],degrees=[512,2048,8192],
 success='all |component| sum <=2log(n)/n away a~0; O(1) components<=.02 at8192; T1c resolved',
 kill='O(1) components>.3 at8192; preserve first failures; no tuning/retries'))
binary,manifest,ns=build.build();lib=ctypes.CDLL(str(binary));before=ns['loaded_closure'](manifest)
rowsfun=lib.d01_rows;rowsfun.argtypes=[ctypes.c_long,ctypes.c_char_p,ctypes.c_char_p,ctypes.POINTER(ctypes.c_double),ctypes.POINTER(ctypes.c_double)];rowsfun.restype=ctypes.c_int
polesfun=lib.d01_poles;polesfun.argtypes=[ctypes.c_long,ctypes.c_char_p,ctypes.c_char_p,ctypes.POINTER(ctypes.c_double),ctypes.POINTER(ctypes.c_int)];polesfun.restype=ctypes.c_int
point=lib.c07_point;point.argtypes=[ctypes.c_long,ctypes.c_char_p,ctypes.c_char_p,ctypes.POINTER(ctypes.c_double),ctypes.POINTER(ctypes.c_long)];point.restype=ctypes.c_int
controls=[]
for n,lo,hi in [(32,10.837661142251891,10.837661142251893),(128,17.060896841022608,17.06089684102261)]:
 arr=np.zeros((2*(n+1),2));ans=np.zeros(2);assert rowsfun(n,b'1/12',b'1/16',arr.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),ans.ctypes.data_as(ctypes.POINTER(ctypes.c_double)))==0
 out=(ctypes.c_double*3)();counts=(ctypes.c_long*6)();assert point(n,b'1/12',b'1/16',out,counts)==0
 assert ans[0]==out[0] and ans[1]==out[1] and ans[0]<=hi and lo<=ans[1]
 discrepancy=abs(math.fsum(midpoint(arr))-sum(ans)/2);assert discrepancy<1e-12
 controls.append(dict(n=n,actual=list(ans),capture_sum_error=discrepancy))
# T1c first; degree-independent model reevaluation and exact boundary oracle.
t1c=[];profiles={}
phases=[(rat(.25),rat(.25)),(rat(1.38),'0'),(rat(1.45),rat(1.45)),('1/2','1/2')]
for index in [2,3]:
 af,bf=map(Fraction,phases[index]);alpha=float(af)*math.pi;beta=float(bf)*math.pi;edge=af+bf==1
 for delta in [.01,.005,.0025]:
  pr=model.profile(alpha,beta,math.log(8192),edge,delta)
  rec=dict(phase=index,delta=delta,model=pr)
  if delta==.01:
   profiles[index]=pr
   tighter=model.profile(alpha,beta,math.log(8192),edge,delta,eps=3e-12)
   rec['tighter_constant_difference']=tighter['constant']-pr['constant']
   rec['tighter_warnings']=tighter['warnings']
   assert abs(rec['tighter_constant_difference'])<2e-8,rec
   if not edge:
    def residue(z):
     s0=(pr['U']+4*pr['a']/math.pi*math.log(z))/z
     return model.B(z,alpha,beta,pr)+model.B(2*math.pi-z,alpha,beta,pr)-2*s0
    partial,estimate=quad(residue,1e-7,delta,epsabs=2e-9,limit=300)
    rec['strip_residual_partial_integral']=partial/math.pi
    rec['strip_residual_partial_estimate']=estimate/math.pi
    rec['strip_residual_coverage']='z in [1e-7,.01]; omitted z<1e-7 OPEN; not whole limiting bias'
  if edge:
   eps=delta/(2*math.pi)
   oracle=2/math.pi*(-digamma(.5)+math.log(delta/math.pi)+gammaln(eps)-gammaln(1-eps)-(1-2*eps)*math.log(math.pi))
   rec['constant_oracle']=oracle;rec['oracle_difference']=pr['constant']-oracle
   rec['limiting_S_minus_model']=4/math.pi*((float(np.euler_gamma)-math.log(math.pi))*eps+sum(zeta(2*k+1)*eps**(2*k+1)/(2*k+1) for k in range(1,5)))
   assert abs(rec['oracle_difference'])<2e-9,rec
  t1c.append(rec)
save(RAW/'t1c.json',t1c)
results=[]
for n in [512,2048,8192]:
 for index,(astr,bstr) in enumerate(phases):
  if cpu()-start>550:raise RuntimeError('prospective reserve before next fixed case')
  t=cpu();m=n+1;af,bf=Fraction(astr),Fraction(bstr);alpha=float(af)*math.pi;beta=float(bf)*math.pi;edge=af+bf==1
  actual=np.zeros((2*m,2));ans=np.zeros(2)
  rc=rowsfun(n,astr.encode(),bstr.encode(),actual.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),ans.ctypes.data_as(ctypes.POINTER(ctypes.c_double)));assert rc==0,('actual',n,index,rc)
  poles=np.zeros_like(actual);kinds=np.zeros(2*m,dtype=np.int32)
  rc=polesfun(n,astr.encode(),bstr.encode(),poles.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),kinds.ctypes.data_as(ctypes.POINTER(ctypes.c_int)));assert rc==0,('poles',n,index,rc)
  pr=profiles.get(index)
  if pr is None:pr=model.profile(alpha,beta,math.log(n),edge);profiles[index]=pr
  # Coefficients and constants independent of n; retain original Mfar.
  L=math.log(n);M=pr['B0']*L*L+pr['b']*L+pr['constant'];row=midpoint(actual);pole=midpoint(poles)
  v=(np.arange(2*m)+float(bf))*math.pi/m;z=np.minimum(v,2*math.pi-v)
  ordinary=np.where(kinds==0)[0];Z=ordinary[z[ordinary]<=.01];inside=ordinary[z[ordinary]>.01]
  assert len(Z)==0,'Fixed registered grid topology changed'
  aval=np.array([model.A(v[r],pr) for r in inside]);bval=np.array([model.B(v[r],alpha,beta,pr) for r in inside]);H=aval*L+bval
  # Exact signed definitions from SPEC; no component inferred from fit.
  cr=pr['endpoint_rows'];tend=pr['B0']*L*L+pr['b_end']*L+pr['mesh_constant']
  D=math.fsum(pole[inside])-math.fsum((aval*L+(bval-np.array([model.old.J(pr['p']/2,abs(pr['q']/2+pr['a']/math.tan(v[r]/2)),min(v[r],abs(v[r]-math.pi),2*math.pi-v[r]))/math.pi for r in inside])))/m)
  cancellation=np.array([model.old.J(pr['p']/2,abs(pr['q']/2+pr['a']/math.tan(v[r]/2)),min(v[r],abs(v[r]-math.pi),2*math.pi-v[r]))/math.pi for r in inside])
  E=math.fsum(row[inside]-pole[inside]-cancellation/m)
  components=dict(endpoint_actual_minus_sinc=math.fsum(row[kinds==1])-cr,mesh=-tend,
    collision=math.fsum(row[kinds==2]),central=math.fsum(row[kinds==3]),ordinary_interior_quadrature=math.fsum(H)/m-(pr['integral_A']*L+pr['integral']),E=E,D=D,Q=0.)
  diff=sum(ans)/2-M;closure=math.fsum(components.values())-diff
  assert abs(closure)<2e-10,(n,index,closure)
  rec=dict(n=n,phase=index,alpha_pi=astr,beta_pi=bstr,alpha=alpha,beta=beta,S=list(ans),M=M,S_minus_M=diff,components=components,
   sum_absolute_components=math.fsum(map(abs,components.values())),telescope_closure_error=closure,
   counts={str(k):int(np.sum(kinds==k)) for k in range(4)},endpoint_ordinary_rows=len(Z),
   coarse_bound_formulas=dict(E=2*(pr['p']+pr['q'])*float(digamma(n+1)+np.euler_gamma)/n+2*pr['a']*m/(n*63),
    D=10/n**2+20*pr['a']*float(digamma(n+1)+np.euler_gamma)/(math.pi*n**2),
    Q=.02/math.pi*(7+(pr['p']+pr['q'])/math.pi*(5+2*math.log(4*math.pi/.01))),
    endpoint_block_admissible=False),
   actual_radius_max=float(np.max(actual[:,1]-actual[:,0])/2),pole_radius_max=float(np.max(poles[:,1]-poles[:,0])/2),cpu_seconds=cpu()-t)
  if edge:
   oracle=next(x for x in t1c if x['phase']==3 and x['delta']==.01)['limiting_S_minus_model']+2/math.pi*math.log1p(1/n)
   rec['boundary_oracle_S_minus_M']=oracle;rec['boundary_oracle_discrepancy']=diff-oracle
   assert abs(diff-oracle)<2e-9,rec
  np.savez(RAW/('rows-n%d-p%d.npz'%(n,index)),actual=actual,poles=poles,kinds=kinds)
  results.append(rec);save(RAW/'results.json',results);print(json.dumps(rec),flush=True)
after=ns['loaded_closure'](manifest);assert before==after
manifest.update(actual_loaded_before=before,actual_loaded_after=after,controls=controls,freeze=freeze,results=results,t1c=t1c,total_cpu_seconds=cpu()-start,wall_seconds=time.monotonic()-wall)
save(RAW/'full-manifest.json',manifest)
receipt=dict(status='MEASURED',input_head='4cf68980fa0538b53e2aea7174ed6e5782a34908',scope='12 fixed cases; full signed telescope; no uniform theorem',
 versions=dict(python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__),
 raw_manifest=build.identity(RAW/'full-manifest.json'),raw_t1c=build.identity(RAW/'t1c.json'),raw_freeze=build.identity(RAW/'prospective-freeze.json'),
 sources=freeze,binary=manifest['checker_binary'],controls=controls,results=results,
 T1c='RESOLVED: original fixed-delta model has nonzero endpoint residual bias; boundary closed-form oracle agrees. No missing correction inserted.',
 gate='OPEN: original coarse e4 topology fails at all target n; signed terms exhibit explicit geometry cancellation. No B3 authorization.',
 total_driver_and_children_cpu_seconds=cpu()-start,limitation='Binary64 quadrature estimates are not rigorous. Supervisor total CPU reported separately; full runtime closure in raw manifest.')
EVIDENCE.write_text(json.dumps(receipt,separators=(',',':'),allow_nan=False)+'\n');assert EVIDENCE.stat().st_size<16384,EVIDENCE.stat().st_size
print(json.dumps(dict(receipt=build.identity(EVIDENCE),cpu_seconds=cpu()-start)))
