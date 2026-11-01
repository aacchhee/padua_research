"""Independent general-constructor certificate mutation controls."""
from pathlib import Path
import sys,gzip,json,copy,time
p=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(p/'code/part3'))
import finite_bernstein as b
import finite_general as g
import finite_general_check as checker
start=time.monotonic()
paths=[p/'code/part3'/x for x in ['finite_bernstein.py','finite_general.py','finite_general_check.py','finite_general_run.py','finite_n2_exact.py']]+[g.DEPENDENCY,p/'outputs/part3/finite_n12_pilot.json.gz']
hashes={str(x):b.digest(x) for x in paths}
data=json.loads(gzip.decompress(paths[-1].read_bytes()))
setup=g.setup(12)
g.setup=lambda n:setup if n==12 else (_ for _ in ()).throw(AssertionError('unexpected degree'))
out={'positive':checker.check(data),'source_sha256':hashes,'controls':[]}
assert out['positive']['accepted']
cases={}
a=copy.deepcopy(data);a['leaves'].pop();cases['missing_leaf']=a
a=copy.deepcopy(data);r=next(r for r in a['leaves'] if r['kind']=='corner');r['corner'][1]=1;cases['wrong_corner']=a
a=copy.deepcopy(data);a['threshold_interval'][0]+=1;cases['altered_threshold']=a
a=copy.deepcopy(data);a['x_cosine_seed'][0]+=1;cases['altered_cosine_seed']=a
for name,a in cases.items():
 try:checker.check(a)
 except AssertionError as e:out['controls'].append({'mutation':name,'rejected':True,'assertion':str(e)})
 else:raise AssertionError('mutation accepted: '+name)
assert all(b.digest(x)==hashes[str(x)] for x in paths)
out['source_unchanged']=True;out['seconds']=time.monotonic()-start
(p/'outputs/part3/independent_general_controls.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
