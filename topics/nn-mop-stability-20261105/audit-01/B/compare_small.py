import json, sys, importlib.util
from fractions import Fraction as Fr
import mpmath as mp
import os
B = os.environ.get('AUDIT_OUT', os.path.dirname(os.path.abspath(__file__)))  # auditor output directory
spec=importlib.util.spec_from_file_location('cond',os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../../')+'topics/nn-mop-stability-20261105/code/conditioning.py')
cond=importlib.util.module_from_spec(spec); spec.loader.exec_module(cond)
ex=json.load(open(B+'/exact3to8.json'))
worst=mp.mpf(0); rows=[]
mp.mp.dps=150
for r in ex:
    out=cond.conditioning_case(r['N'],r['family'],dps=120)
    for tgt,key in (('NN','NN'),('SL','step_line')):
        for model in ('mixed','componentwise','blocknorm'):
            e=Fr(r[tgt][model]['kappa']); e=mp.mpf(e.numerator)/e.denominator
            c=mp.mpf(out[key][model]['kappa'])
            rel=abs(c-e)/e; worst=max(worst,rel)
            # by field
            for f,v in r[tgt][model]['by_field'].items():
                cf=float(out[key][model]['by_field'][f])
                assert abs(cf-v)<=1e-12*max(abs(v),1e-300), (r['N'],r['family'],tgt,model,f,cf,v)
            rows.append((r['family'],r['N'],tgt,model,mp.nstr(e,12),mp.nstr(rel,3),r[tgt][model]['arg'],out[key][model]['maximizer']))
for x in rows: print(*x)
print('worst relative difference conditioning.py(120dps) vs exact:',mp.nstr(worst,5))
