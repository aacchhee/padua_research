"""One pure control execution; no imports of a builder or native controller."""
import ast,hashlib,json,math,pathlib,resource,time
from fractions import Fraction as Q
from arithmetic import endpoints,check_endpoint_record,loss_test,covers_half_diamond
resource.setrlimit(resource.RLIMIT_CPU,(1,1))
HERE=pathlib.Path(__file__).resolve().parent;ROOT=HERE.parents[3]
OUT=ROOT/'local-output/argmax-bridge-20261105/post-audit-D09/result-review'
OUT.mkdir(parents=True,exist_ok=True)
with (OUT/'pure-registration.json').open('x') as f:json.dump(dict(scope='pure synthetic arithmetic and AST only',hard_CPU=1),f)
def rejects(fn):
    try:fn()
    except ValueError:return
    raise AssertionError('negative control admitted')
for p in HERE.glob('*.py'):ast.parse(p.read_text(),filename=str(p))
row=endpoints([1.,math.nextafter(1.,math.inf),0.])
assert Q(row['upper'])==Q(2**52+1,2**52)
assert Q(row['upper'])!=Q(str(math.nextafter(1.,math.inf)))
check_endpoint_record(row)
for values in ([math.nan,1.,0.],[0.,math.inf,0.],[2.,1.,0.],[0.,1.,-1.],[0.,1.]):
    rejects(lambda values=values:endpoints(values))
bad=dict(row,upper='1');rejects(lambda:check_endpoint_record(bad))
a,b=Q(1,4),Q(3,16)
corner=endpoints([10.,10.,0.]);points=[endpoints([9.,9.,0.])]*3
good=loss_test(512,a,b,corner,points)
assert good['q']=='512/25' and good['passes']
assert Q(good['threshold'])==Q(22,7)**4*34/192
assert Q(good['epsilon_lower'])==Q(good['gap'])/Q(22,7)**2
badpoints=[endpoints([11.,11.,0.]),*points[1:]]
assert not loss_test(512,a,b,corner,badpoints)['passes']
assert covers_half_diamond(a,b) and covers_half_diamond(Q(1,6),Q(5,31))
assert not covers_half_diamond(Q(25,157),b)
rejects(lambda:loss_test(512,a,b,corner,points[:2]))
record=dict(status='PASS',checks='AST; binary64 dyadic reconstruction; invalid endpoint rejection; positive/negative exact loss; geometry',
    self_CPU_before_final_output=time.process_time(),hard_CPU=1,no_native_import_or_execution=True)
with (OUT/'pure-result.json').open('x') as f:json.dump(record,f,indent=2)
print(json.dumps(record))
