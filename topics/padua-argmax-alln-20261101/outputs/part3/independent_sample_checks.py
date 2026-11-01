"""Supplementary independent bounded numerical replay; not a proof."""
from pathlib import Path
import sys,json,hashlib,platform
import numpy as np
import scipy
p=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(p/'code/part3'))
from tests_common import Edge, Eval, validate
from tests_T1 import cells,gbeta
sources=['code/part3/tests_common.py','code/part3/tests_T1.py','code/maj.py']
hashes={name:hashlib.sha256((p/name).read_bytes()).hexdigest() for name in sources}
out={'status':'MEASURED','scope':'bounded independent numerical check, not complete T1 rerun','python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,'source_sha256':hashes,'validation':validate(),'n12_cells':{},'crosschecks':[],'gbeta':[]}
e=Edge(12)
for edge in ['v+','v-','h+','h-']:out['n12_cells'][edge]=cells(e,edge)
for n in [3,8,101,400]:
 e,v=Edge(n),Eval(n)
 for edge in ['v+','v-','h+','h-']:
  for t in [0.,.173*np.pi,np.pi/2,np.pi]:
   theta=(0. if edge[1]=='+' else np.pi) if edge[0]=='v' else t
   phi=t if edge[0]=='v' else (0. if edge[1]=='+' else np.pi)
   error=abs(e.one(edge,t)-v.one(theta,phi)[0]);assert error<1e-7
   out['crosschecks'].append({'n':n,'edge':edge,'t':t,'error':error})
for b in [.1,.25,.5,.75,.9]:out['gbeta'].append({'beta_over_pi':b,'value':gbeta(b*np.pi)})
for name,h in hashes.items():assert hashlib.sha256((p/name).read_bytes()).hexdigest()==h
(p/'outputs/part3/independent_sample_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'accepted':True,'maximum_edge_error':max(r['error'] for r in out['crosschecks']),'gbeta':out['gbeta']}))
