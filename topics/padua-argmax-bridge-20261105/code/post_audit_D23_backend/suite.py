"""One frozen finite diagnostic suite; no numerical/native work on import."""
from fractions import Fraction as F
import math

INVALID_POINTS=((1,'1/12','1/16'),(2147483648,'1/12','1/16'),(16,'-1/12','0'),(16,'1','1'),(16,'nan','0'),(16,'1/0','0'))
INVALID_PARTIALS=((1,1,'.5'),(16,17,'.5'),(16,1,'0'),(16,9,'8'))
PARTIALS=((16,7,'0.5'),(16,8,'0.5'),(16,9,'0.5'),(16,9,'1e-30'),(16,9,'7.999999999999999999999999999999'),(16,9,'[0.5 +/- 0.01]'),(16,8,'8.5'))
REFERENCES=((8,'1/12','1/16'),(8,'0','0'),(16,'0','1/4'),(16,'1/4','3/4'))

def binary(s):
 x=float.fromhex(s)
 if not math.isfinite(x):raise ValueError('nonfinite native output')
 return F.from_float(x)

def point(raw,which):
 if raw['returncode']!=0 or len(raw['hex'])!=(3 if which=='baseline' else 4):raise ValueError('point returncode/schema')
 lo,hi,radius=map(binary,raw['hex'][:3])
 if not 0<=lo<=hi or radius<0:raise ValueError('point enclosure')
 c=raw['counts']
 if len(c)!=6 or any(type(x) is not int or x<0 for x in c):raise ValueError('point counters')
 if c[0]!=8192 or c[5]!=4094 or c[3]>5 or c[4]>24 or c[1]>5*c[5] or c[2]>24*c[5]:raise ValueError('counter closure')
 if which=='candidate' and binary(raw['hex'][3])!=1:raise ValueError('exact full Arb radius exceeds1/100000')
 return lo,hi,radius

def run(native,state,checkpoint,historical):
 checks=[]
 for i,(n,a,b) in enumerate(INVALID_POINTS):
  raw=native.call('invalid-point-'+str(i),lambda n=n,a=a,b=b:native.invalid_point(n,a,b))
  if raw['returncode']==0:raise ValueError('invalid point admitted')
 for i,(n,q,y) in enumerate(INVALID_PARTIALS):
  raw=native.call('invalid-partial-'+str(i),lambda n=n,q=q,y=y:native.partial(n,q,y,True))
  if raw['returncode']==0:raise ValueError('invalid partial admitted')
 checks.append('fixed invalid integer/domain/pole/rational API guards')
 # Invalid guards return before any coefficient table is initialized.
 old=native.call('baseline-cold-n2048',lambda:native.point('baseline',2048,'1/12','1/16'))
 oldlo,oldhi,_=point(old,'baseline')
 new=native.call('candidate-cold-n2048',lambda:native.point('candidate',2048,'1/12','1/16'))
 newlo,newhi,_=point(new,'candidate')
 hist=[p for p in historical['points'] if p['n']==2048]
 if len(hist)!=1 or hist[0]['alpha_pi']!='1/12' or hist[0]['beta_pi']!='1/16':raise ValueError('historical reference schema')
 hlo,hhi=F.from_float(hist[0]['lower']),F.from_float(hist[0]['upper'])
 if max(oldlo,hlo)>min(oldhi,hhi) or max(newlo,hlo)>min(newhi,hhi) or max(oldlo,newlo)>min(oldhi,newhi):raise ValueError('fresh/historical endpoint overlap')
 if newhi-oldlo>F(1,50000) or newhi-hlo>F(1,50000):raise ValueError('outward upper overhead exceeds2e-5')
 state['matched_pair']={'phase_pi':['1/12','1/16'],'n':2048,'old':old,'candidate':new,'upper_minus_fresh_old_lower':str(newhi-oldlo),'upper_minus_historical_lower':str(newhi-hlo),'both_coefficient_tables_cold':True,'timing_scope':'point call includes its initial checkpoint and native coefficient preparation; builds and valid controls reported separately'};checkpoint()
 checks.append('one fresh old/new cold-table matched point; exact full radius and outward upper gaps')
 for i,(n,q,y) in enumerate(PARTIALS):
  raw=native.call('partial-control-'+str(i),lambda n=n,q=q,y=y:native.partial(n,q,y))
  if raw['returncode'] or binary(raw['hex'][0])!=1 or binary(raw['hex'][1])<0:raise ValueError('full-image endpoint-hull containment failed')
 checks.append('fixed harmonic transition, both poles, removable endpoints and input-ball hull')
 moments=native.call('moments-degree0-through5',lambda:{'checks':native.libs['candidate'].c23_moment_control()})
 if moments['checks']!=18:raise ValueError('exact rational moments')
 checks.append('eighteen exact rational moment containments through degree5')
 for i,(n,a,b) in enumerate(REFERENCES):
  raw=native.call('finite-cosine-reference-'+str(i),lambda n=n,a=a,b=b:native.reference(n,a,b))
  if raw['returncode'] or not (binary(raw['hex'][0])==1 or binary(raw['hex'][1])==1) or binary(raw['hex'][2])<0:raise ValueError('complete finite cosine reference containment')
 checks.append('four complete512-bit original finite cosine references')
 return {'result':'PASS fixed paired benchmark and controls','checks':checks,'matched_pair':state['matched_pair'],'native_invocations':len(state['completed_calls']),'scope':'single fullS arithmetic trial only; no cover, actual lambda, degree or asymptotic throughput conclusion'}
