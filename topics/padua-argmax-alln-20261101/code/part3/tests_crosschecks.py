"""Supplemental developer normalization checks, not independent proof checks."""
import json, sys
from pathlib import Path
import numpy as np
from tests_common import Primitive, Eval

root=Path(sys.argv[1])
out={'status':'MEASURED','kind':'developer supplemental crosscheck','primitive':[],'T2_center':[]}
for n in (8,16,64):
    p,e=Primitive(n),Eval(n)
    q=round((n+1)/2)
    if q%2==0:q+=1
    for s in (0,.1,.4,1.,2.9):
        a=e.one(0,(q*np.pi+s)/(n+1))[1];b=p.one(s)
        out['primitive'].append({'n':n,'s':s,'difference':a-b})
d=json.loads((root/'tests_T2.json').read_text())
for n in (32,64,128):
    r=next(r for r in d['rows'] if r['n']==n and r['a']==5 and r['b']==5)
    out['T2_center'].append({'n':n,'antinode_gap':r['antinode_gap'],'cell_max_gap':r['gap'],'indices':[r['j'],r['k']]})
assert max(abs(r['difference']) for r in out['primitive'])<1e-10
(root/'tests_crosschecks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
