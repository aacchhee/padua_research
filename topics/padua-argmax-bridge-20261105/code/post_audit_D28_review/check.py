import ast, copy, hashlib, json, math, resource, time, types
from fractions import Fraction as F
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(1,2));start=time.process_time()
HERE=Path(__file__).resolve().parent;TOPIC=HERE.parent.parent;ROOT=TOPIC.parents[1]
SRC=HERE.parent/'post_audit_D28_static'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(SRC/'FREEZE.json')=='4769e50fbedcdfc54ce771a60f2870e725db71a04ea8933c9c0d6bd1655cf150'
assert sha(SRC/'SPEC.md')=='da0bce3a45248f2ecc825eb564e45c626d8763e3f14c3c24a5944566236e6e84'
assert sha(SRC/'SOURCE.md')=='d76247be408a85f7c524f0e80f1eb68f190e77c1bb5665ae6af7096d9108b0be'
frozen=json.loads((SRC/'FREEZE.json').read_text())
for row in frozen['code_data']:
 p=ROOT/row['path'];assert len(p.read_bytes())==row['bytes'] and sha(p)==row['sha256']
for p in SRC.glob('*.py'):ast.parse(p.read_text())
assert (SRC/'checker.py').read_bytes()==(HERE.parent/'post_audit_D21_static/checker.py').read_bytes().replace(b'D21 generic',b'D28 generic')
assert (HERE.parent/'post_audit_D23_backend/point.cpp').read_bytes()==(HERE.parent/'cheap_rows_C11/point.cpp').read_bytes()
old=json.loads((TOPIC/'evidence/d21-static6912.json').read_text())
final=json.loads((TOPIC/'evidence/d21-static6912-final-accounting.json').read_text())
obs=json.loads((TOPIC/'evidence/d21-static6912-primary-observation.json').read_text())
assert len(old['rows'])==41 and old['n']==6912 and final['complete'] is True and final['first_failure'] is None
assert final['result']=='EXACT_STATIC_COVER_ACCEPTED_PENDING_INDEPENDENT_REPLAY'
assert type(obs['observed_exit_code']) is int and obs['observed_exit_code']==0 and obs['final_accounting_complete'] is True
for item in obs['artifacts']:
 p=ROOT/item['path'];assert sha(p)==item['sha256'] and len(p.read_bytes())==item['bytes']
def functions(path,names,ns):
 tree=ast.parse(path.read_text());body=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in names]
 assert len(body)==len(names)
 exec(compile(ast.Module(body=body,type_ignores=[]),str(path),'exec'),ns)
ns={'F':F,'math':math,'WIDTH':F(1,50000)}
functions(SRC/'baseline.py',{'binary','compare'},ns)
raw={'api':'S','n':6912,'key':['0','0'],'native':{'returncode':0,'counts':[0]*6,'raw_hex':[float(0).hex(),float(2**-16).hex(),float(0).hex()]}}
reference={'lower':F(0),'upper':F(1,16384),'counts':[0]*6}
assert ns['compare']((F(0),F(0)),raw,reference)[0]==F(1,65536)
rejects=0
def reject(fn):
 global rejects
 try:fn()
 except (ValueError,RuntimeError):rejects+=1
 else:raise AssertionError('synthetic failure accepted')
for field,value in [('n',2048),('key',['1','0']),('api','lambda')]:
 bad=copy.deepcopy(raw);bad[field]=value;reject(lambda:ns['compare']((F(0),F(0)),bad,reference))
for field,value in [('counts',[1]*6),('returncode',1),('raw_hex',[float(0).hex(),float(2**-15).hex(),float(0).hex()])]:
 bad=copy.deepcopy(raw);bad['native'][field]=value;reject(lambda:ns['compare']((F(0),F(0)),bad,reference))
reject(lambda:ns['compare']((F(0),F(0)),raw,{**reference,'lower':F(1),'upper':F(2)}))
# Narrow interval overlaps old but upper-old lower exceeds cap: overhead independently fails.
bad=copy.deepcopy(raw);bad['native']['raw_hex']=[float(2**-14).hex(),float(2**-14).hex(),float(0).hex()]
reject(lambda:ns['compare']((F(0),F(0)),bad,reference))
class Fake:
 RUSAGE_CHILDREN=1;RUSAGE_SELF=2;RLIMIT_CPU=0
 def __init__(self,c=180.25,s=2):self.c=c;self.s=s;self.limit=None
 def getrusage(self,k):return types.SimpleNamespace(ru_utime=self.c if k==1 else self.s,ru_stime=0)
 def getrlimit(self,k):return (199,200)
 def setrlimit(self,k,v):self.limit=v
class Wait:
 WNOHANG=1
 def __init__(self,live=False):self.live=live
 def wait4(self,*args):
  if self.live:return (0,0,None)
  raise ChildProcessError
r=Fake();env={'resource':r,'os':Wait(),'math':math,'TOTAL':200}
functions(SRC/'controller.py',{'final_cpu_limit'},env)
result=env['final_cpu_limit']([{'accounting_complete':True}]);assert r.limit==(18,18) and r.c+18<=199
for r,w,stages in ((Fake(),Wait(True),[]),(Fake(),Wait(),[{'accounting_complete':False}]),(Fake(198,1),Wait(),[])):
 env['resource']=r;env['os']=w;reject(lambda:env['final_cpu_limit'](stages))
receipt={'status':'PASS_METADATA_SYNTHETIC_ONLY','freeze_sha256':sha(SRC/'FREEZE.json'),'frozen_files':len(frozen['code_data']),'baseline_rows_metadata':len(old['rows']),'synthetic_rejections':rejects,'cpu_through_receipt':time.process_time()-start,'check_sha256':sha(Path(__file__)),'native_calls':0,'author_controls':0,'controller_invocations':0,'limit':'soft1/hard2CPU; no children; receipt serialization/return remain inside hard limit'}
(HERE/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt))
