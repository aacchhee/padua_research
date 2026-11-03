"""Independent certificate mutation controls; verified setup cached only in this harness."""
from pathlib import Path
import sys,gzip,json,copy,hashlib,platform,time
p=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(p/'code/part3'))
import finite_bernstein as b
import finite_bernstein_check as checker
start=time.monotonic()
paths=[p/'code/part3'/x for x in ['finite_bernstein.py','finite_bernstein_check.py','finite_bernstein_run.py']]+[b.PART2/'a5_n8_field.py',p/'outputs/part3/finite_n8_pilot.json.gz']
hashes={str(x.relative_to(p)) if x.is_relative_to(p) else str(x):b.digest(x) for x in paths}
data=json.loads(gzip.decompress(paths[-1].read_bytes()))
original_setup=b.setup_n8
verified_setup=original_setup()
b.setup_n8=lambda:verified_setup
out={'status':'independent executed controls','source_sha256':hashes,'python':platform.python_version(),'positive':checker.check(data),'controls':[]}
assert out['positive']['accepted']
cases={}
a=copy.deepcopy(data);a['leaves'].pop();cases['missing_leaf_hole']=a
a=copy.deepcopy(data);row=next(r for r in a['leaves'] if r['kind']=='corner');row['corner'][1]=1;cases['wrong_corner']=a
a=copy.deepcopy(data);a['threshold_interval'][0]+=1;cases['altered_threshold']=a
a=copy.deepcopy(data);a['leaves'].append(copy.deepcopy(a['leaves'][0]));cases['duplicate_leaf']=a
a=copy.deepcopy(data);a['accepted']=True;cases['producer_self_approval']=a
for name,a in cases.items():
 try:checker.check(a)
 except AssertionError as e:out['controls'].append({'mutation':name,'rejected':True,'assertion':str(e)})
 else:raise AssertionError('mutation accepted: '+name)
assert all(b.digest(x)==hashes[str(x.relative_to(p)) if x.is_relative_to(p) else str(x)] for x in paths)
out['seconds']=time.monotonic()-start
out['sympy']=__import__('sympy').__version__
out['source_unchanged']=True
(p/'outputs/part3/independent_n8_controls.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
