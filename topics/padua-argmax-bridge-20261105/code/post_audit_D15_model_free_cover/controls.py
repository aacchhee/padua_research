"""Once-only synthetic Python controls: no runtime/producer/native imports.
One CPU author share of the shared2CPU reserve. No numerical phase values.
"""
import argparse,ast,hashlib,json,pathlib,resource
from fractions import Fraction as F
import checker as C
HERE=pathlib.Path(__file__).resolve().parent;ROOT=HERE.parents[3]
OUT=ROOT/'local-output/argmax-bridge-20261105/post-audit-D15/model-free-cover-pure-controls'

def identity(path):
 data=path.read_bytes();return {'path':str(path),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
def reject(fn):
 try:fn()
 except (ValueError,RuntimeError,TypeError,KeyError,ZeroDivisionError):return
 raise AssertionError('malformed synthetic input admitted')
def cpu():
 r=resource.getrusage(resource.RUSAGE_SELF);return r.ru_utime+r.ru_stime
def frozen():
 f=json.loads((HERE/'FREEZE.json').read_text());s=json.loads((HERE/'SOURCES.json').read_text())
 for row in f['code_data']+s['immutable_code_data_dependencies']:
  got=identity(ROOT/row['path'])
  if any(got[k]!=row[k] for k in ('bytes','sha256')):raise RuntimeError('frozen bytes changed')
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--run-once',action='store_true');args=ap.parse_args()
 if not args.run_once:raise RuntimeError('explicit --run-once required')
 resource.setrlimit(resource.RLIMIT_CPU,(1,1));OUT.mkdir(parents=True,exist_ok=False)
 with (OUT/'preregistration.json').open('x') as out:json.dump({'source':identity(HERE/'controls.py'),'freeze':identity(HERE/'FREEZE.json'),'hard_CPU':1,'shared_author_auditor_reserved':2,'native_calls':0},out)
 frozen();cases=[]
 try:
  # Parse source syntax only; no compile, load or execution of stage modules.
  for path in sorted(HERE.glob('*.py')):ast.parse(path.read_text(),filename=str(path))
  cases.append('all local Python source syntax parsed without stage imports')
  for s in ('01','1.0','1/0','nan','1/2/3','1/'+'9'*300):reject(lambda s=s:C.rational(s))
  good={'format':'D15-midpoint-v1','n':2048,'preorder':'.'}
  for k,v in (('n',True),('n',512),('preorder','a.'),('preorder','..'),('preorder','?'),('preorder','a'*66+'.'*67)):
   reject(lambda k=k,v=v:C.decode_certificate(dict(good,**{k:v})))
  cases.append('canonical rationals, degree and complete preorder rejection')
  assert len(C.grid())==15 and len(set(C.grid()))==15
  raw={(F(i+d,4),F(j+e,4)) for i in range(4) for j in range(4-i) for d in (0,1) for e in (0,1)}
  assert len(raw)==19 and {C.canonical(*x) for x in raw}=={C.canonical(*x) for x in C.grid()}
  M,norm=C.norm_from_grid([F(1)]*15);theta=F(norm['theta']);assert M>=1/(1-theta) and M-1<1/(1-theta)
  reject(lambda:C.norm_from_grid([F(0)]*15));reject(lambda:C.norm_from_grid([F(1)]*14));reject(lambda:C.norm_from_grid([1.0]*15))
  cases.append('quarter-square19raw-to15triangle norm absorption and exact ceiling')
  assert C.canonical(F(1),F(0))==C.canonical(F(0),F(1))
  assert C.canonical(F(3,4),F(3,4))==C.canonical(F(1,4),F(1,4))
  assert C.corner_witness(F(100),[F(0)]*3,F(1))['gap']
  reject(lambda:C.corner_witness(F(1),[F(1)]*3,F(1)))
  threshold=F(22,7)**4*F(1,32)/6;u,v=F(1,32),F(9,512)
  reject(lambda:C.corner_witness(F(100),[F(100)-threshold*u,F(100)-threshold*v,F(100)-threshold*(u+v)],F(1)))
  cases.append('closed-edge fold and primary pi-fourth strict corner criterion')
  calls=[];C.verify_certificate({'format':'D15-midpoint-v1','n':2048,'preorder':'a..'},F(100),lambda key:(calls.append(key) or F(0)),F(1))
  assert calls
  tangent=(F(1,2),F(1),F(1,2),F(1));reject(lambda:C.leaf_predicate(tangent,[F(100)]*4,F(1),F(1)))
  assert C.leaf_predicate((F(3,4),F(1),F(3,4),F(1)),[],F(1),F(1))=='OUTSIDE'
  for bad in (F(-1),float('nan'),F(100)):reject(lambda bad=bad:C.verify_certificate(good,F(1),lambda key:bad,F(1)))
  node={'leaf':True};alias={'format':'D15-tree-v1','n':2048,'tree':{'axis':0,'at':'1/2','left':node,'right':node}}
  reject(lambda:C.verify_tree_skeleton(alias,F(100),lambda key:F(0),F(1)))
  reject(lambda:C.verify_certificate(good,F(100),lambda key:F(0),F(1),'test',{('test',2048,F(0),F(0)):float('nan')}))
  cases.append('closed complete union, tangencies, oracle and internal cache failures')
  frozen();status={'result':'PASS synthetic controls only','cases':cases,'CPU_before_summary':cpu(),'hard_CPU':1,'native_calls':0,'limitations':'No enclosure, throughput or mathematical instance established.'}
 except BaseException as error:
  status={'result':'FIRST_FAILURE','first_failure':repr(error),'cases':cases,'CPU_before_summary':cpu(),'native_calls':0}
  with (OUT/'summary.json').open('x') as out:json.dump(status,out)
  raise
 with (OUT/'summary.json').open('x') as out:json.dump(status,out)
 print(json.dumps(status))
if __name__=='__main__':main()
