"""Independent Python-only synthetic source checks; never loads native code."""
import sys
sys.dont_write_bytecode = True
import importlib.util, json, pathlib, resource
from fractions import Fraction as F
resource.setrlimit(resource.RLIMIT_CPU, (1, 1))
p = pathlib.Path(__file__).resolve().parent.parent/'post_audit_D09_threepoint/controller.py'
spec = importlib.util.spec_from_file_location('reviewed_d09', p)
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)
checks = []
def ok(name, value):
    assert value, name
    checks.append(name)
def rejects(name, fn):
    try: fn()
    except (RuntimeError, ValueError): checks.append(name)
    else: raise AssertionError(name)
r = c.endpoint_record([0.1, 0.2, 0.0])
ok('exact binary endpoints differ from decimal shorthand', F(r['lower']) == F.from_float(0.1) != F('0.1'))
for name, values in [('NaN', [float('nan'),1.,0.]), ('infinity',[0.,float('inf'),0.]), ('reverse',[2.,1.,0.]), ('negative radius',[0.,1.,-1.]), ('arity',[])]:
    rejects(name, lambda values=values: c.endpoint_record(values))
n,a,b,M = 512,F(1,4),F(3,16),F(34)
u,v = a*a/2,b*b/2
threshold = F(22,7)**4*M*max(u,F(n,n+1)**4*v)/6
for delta in [F(-1,100),F(0),F(1,100)]:
    q = threshold+delta
    r = c.criterion(n,a,b,F(100),[100-q*u,100-q*v,100-q*(u+v)],M)
    ok('strict threshold '+str(delta), r['passes'] == (delta>0) and F(r['gap']) == delta)
    if delta>0: ok('epsilon rational',F(r['epsilon_lower']) == delta/F(22,7)**2)
rejects('three losses required',lambda:c.criterion(n,a,b,F(100),[F(99)],M))
state = dict(pending_points=['primary-x','primary-y'],completed_calls=[],active_call={'label':'primary-x'},rectangles={'primary':{'vertices':{}}})
record = dict(label='primary-x',result={'synthetic':True},cpu_seconds=21)
c.finish_call(state,record,dict(kind='vertex',rectangle='primary',vertex='x'))
ok('retain completed costly vertex',state['pending_points']==['primary-y'] and state['completed_calls']==[record] and state['active_call'] is None and state['rectangles']['primary']['vertices']['x']==record['result'])
rejects('ledger rejects wrong order',lambda:c.finish_call(state,record,dict(kind='vertex',rectangle='primary',vertex='x')))
sources=json.loads((p.parent/'SOURCES.json').read_text())
ok('exact norm selection',c.norm_upper(32,sources)[0]==46 and c.norm_upper(512,sources)[0]==34)
ok('fixed fallback positive sides',F(sources['fallback']['a_turn'])*F(sources['pi_lower'])>F(1,2) and F(sources['fallback']['b_turn'])*F(sources['pi_lower'])>F(1,2))
c.check_freeze()
checks.append('all runtime freeze identities')
print(json.dumps(dict(status='PASS',checks=checks,total_process_cpu_before_output=c.cpu(),controller=c.identity(p)),indent=2))
