"""One-shot D21 metadata/synthetic controls; no author execution slot."""
import resource
resource.setrlimit(resource.RLIMIT_CPU,(1,2))
import ast, hashlib, json, math, sys, time, types
from fractions import Fraction as F
from pathlib import Path
assert sys.argv[1:]==['--run-once']
here=Path(__file__).resolve().parent; base=here.parents[1]; root=base.parents[1]
out=here/'receipt.json'
assert not out.exists(),'no retry'
src=base/'code/post_audit_D21_static'
fr=(src/'FREEZE.json').read_bytes()
assert hashlib.sha256(fr).hexdigest()=='c25384c68de1691de2342d1d012c3f0d08e99458dfffa3652dfe36befed607bc'
freeze=json.loads(fr)
for row in freeze['code_data']:
    raw=(root/row['path']).read_bytes()
    assert len(raw)==row['bytes'] and hashlib.sha256(raw).hexdigest()==row['sha256']
raw=(src/'checker.py').read_bytes(); ns={}
exec(compile(raw,str(src/'checker.py'),'exec'),ns)
tree_raw=(base/'evidence/d19-pruned-tree.json').read_bytes()
assert hashlib.sha256(tree_raw).hexdigest()==ns['TREE_SHA']
doc=json.loads(tree_raw); tokens=doc['preorder']; pos=0; leaves=[]
def walk(box):
    global pos
    ident=pos; token=tokens[pos]; pos+=1
    if token=='.': leaves.append((ident,box)); return
    lo,hi,blo,bhi=box
    if token=='a':
        mid=(lo+hi)/2; children=((lo,mid,blo,bhi),(mid,hi,blo,bhi))
    elif token=='b':
        mid=(blo+bhi)/2; children=((lo,hi,blo,mid),(lo,hi,mid,bhi))
    else: raise AssertionError('token')
    for child in children: walk(child)
walk((F(0),F(1),F(0),F(1)))
assert pos==len(tokens)==61 and leaves==ns['decode'](doc)
def orbit(a,b):
    return min((ea*a+p,eb*b+q) for ea in (-1,1) for eb in (-1,1) for p in range(-2,3) for q in range(-2,3) if (p+q)%2==0 and 0<=ea*a+p and 0<=eb*b+q and ea*a+p+eb*b+q<=1)
points=set();retained=0;tangent=0;outside=0;orbit_cache={}
for _,(al,ah,bl,bh) in leaves:
    if al+bl>1: outside+=1;continue
    retained+=1;tangent+=al+bl==1
    for a in (al,ah):
        for b in (bl,bh):
            if (a,b) not in orbit_cache:orbit_cache[(a,b)]=orbit(a,b)
            assert orbit_cache[(a,b)]==ns['canonical'](a,b)
            points.add(orbit_cache[(a,b)])
assert sorted(points)==ns['keys'](leaves) and len(points)==41 and (F(0),F(0)) in points
assert all(0<=ns['theta'](box)<1 for _,box in leaves if box[0]+box[2]<=1)
def rejects(fn):
    try:fn()
    except (ValueError,RuntimeError,TypeError,KeyError,ZeroDivisionError):return
    raise AssertionError('invalid synthetic case accepted')
uppers={k:F(1) for k in points}; M,details=ns['adaptive_norm'](leaves,uppers)
ratio=F(details['R']); assert M-1<ratio<=M
rejects(lambda:ns['adaptive_norm'](leaves,{}))
rejects(lambda:ns['adaptive_norm'](leaves,{k:1.0 for k in points}))
rejects(lambda:ns['theta']((F(0),F(1),F(0),F(1))))
box=(F(0),F(1,16),F(0),F(1,16));bound=ns['theta'](box)
assert ns['leaf'](box,[F(0)]*4,bound-F(1,16)+F(1,1000),F(1))[0]=='NEAR'
rejects(lambda:ns['leaf'](box,[F(0)]*4,bound-F(1,16),F(1)))
tbox=(F(1,2),F(1),F(1,2),F(1))
rejects(lambda:ns['leaf'](tbox,[F(10)]*4,F(1),F(1)))
assert ns['leaf']((F(3,4),F(1),F(3,4),F(1)),[],F(1),F(1))[0]=='OUTSIDE'
rejects(lambda:ns['decode'](dict(doc,preorder='.'*61)))
rejects(lambda:ns['decode'](dict(doc,n=True)))
controller=(src/'controller.py').read_bytes()
fn=[x for x in ast.parse(controller).body if isinstance(x,ast.FunctionDef) and x.name=='final_cpu_limit']
assert len(fn)==1
class FakeResource:
    RUSAGE_CHILDREN=0;RUSAGE_SELF=1;RLIMIT_CPU=2
    def __init__(self,child,own):self.child=child;self.own=own;self.limit=None
    def getrusage(self,k):return types.SimpleNamespace(ru_utime=self.child if k==0 else self.own,ru_stime=0)
    def getrlimit(self,k):return (599,600)
    def setrlimit(self,k,v):self.limit=v
class FakeOS:
    WNOHANG=1
    def __init__(self,live=False):self.live=live
    def wait4(self,pid,flags):
        if self.live:return (0,0,None)
        raise ChildProcessError
def final_test(child=12.75,own=1.25,live=False,complete=True):
    rr=FakeResource(child,own);env={'resource':rr,'os':FakeOS(live),'math':math,'TOTAL':600}
    exec(compile(ast.Module(body=fn,type_ignores=[]),'<frozen-finalizer>','exec'),env)
    value=env['final_cpu_limit']([{'accounting_complete':complete}])
    assert rr.limit[1]+child<=599 and value['no_live_children']
    return value
final=final_test()
rejects(lambda:final_test(live=True))
rejects(lambda:final_test(complete=False))
rejects(lambda:final_test(child=598,own=1))
usage=resource.getrusage(resource.RUSAGE_SELF)
result={'status':'PASS_METADATA_SYNTHETIC_ONLY','nodes':len(tokens),'leaves':len(leaves),'retained_leaves':retained,'tangent_leaves':tangent,'outside_leaves':outside,'canonical_required_keys':len(points),'origin_present':True,'full_orbit_keys_match':True,'all_retained_theta_valid':True,'synthetic_final_limit':final,'native_calls':0,'author_controls_calls':0,'primary_lock_consumed':False,'cpu_through_pre_serialization':usage.ru_utime+usage.ru_stime,'whole_process_CPU_cap':2,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'SPEC_sha256':hashlib.sha256((here/'SPEC.md').read_bytes()).hexdigest(),'frozen_author_manifest_sha256':hashlib.sha256(fr).hexdigest(),'utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())}
data=json.dumps(result,indent=2,sort_keys=True)+'\n';assert len(data.encode())<16384
with out.open('x') as h:h.write(data)
print(json.dumps({'status':result['status'],'cpu':result['cpu_through_pre_serialization'],'receipt_sha256':hashlib.sha256(data.encode()).hexdigest(),'bytes':len(data.encode())}))
