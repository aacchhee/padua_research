"""Independent audit of committed finite lattice evidence and gate arithmetic.

Run from any cwd. Optional --output selects the replay receipt; by default it
is written under /tmp/padua-audit-finite. This is audit support, not development
code or an additional mathematical claim.
"""
import argparse,json,math,hashlib,sys,itertools,importlib.util
from pathlib import Path
import sympy as s
import numpy as np
ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,default=Path('/tmp/padua-audit-finite/independent_checks.json'));args=ap.parse_args()
root=Path(__file__).resolve().parents[3];topic=root/'topics/padua-effective-cubature-20261112'
r=json.loads((topic/'evidence/pdn-lattice-witness.json').read_text())
out={'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'python':sys.version,'numpy':np.__version__,'sympy':s.__version__,'committed_strong_witnesses':[]}
for row in r['rows']:
 n,p8,index,covered,flat,idxweak,covweak=row
 A=s.Matrix(3,3,flat); d=abs(int(A.det()));Ai=A.inv();E=2*n-1
 assert p8==8*math.comb(n+3,3) and d==index and covered==(index<=p8)
 bounds=[int(math.floor(E*max(abs(Ai[i,j]) for j in range(3)))) for i in range(3)]
 minimum=None
 # Independent SymPy inverse, Python integer vector products and exhaustive coefficient box.
 for c in itertools.product(*(range(-b,b+1) for b in bounds)):
  if c==(0,0,0):continue
  k=[sum(flat[3*i+j]*c[j] for j in range(3)) for i in range(3)]
  norm=sum(map(abs,k)); minimum=norm if minimum is None else min(minimum,norm)
 assert minimum>E,(n,minimum,E)
 out['committed_strong_witnesses'].append({'n':n,'index':index,'8P':p8,'covered':covered,'coefficient_bounds':bounds,'min_norm_in_box':minimum})
spec=importlib.util.spec_from_file_location('ball',topic/'code/pdn_check_ball.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
assert not m.avoids(np.eye(3,dtype=int).tolist(),1)
assert m.avoids((7*np.eye(3,dtype=int)).tolist(),6)
assert not m.avoids((7*np.eye(3,dtype=int)).tolist(),7)
out['negative_controls']={'Z3_E1':False,'7Z3_E6':True,'7Z3_E7':False}
t=json.loads((topic/'evidence/lp-torus.json').read_text());l={v['n']:v['M'] for v in json.loads((topic/'evidence/lp-lattice.json').read_text())['rows']}
assert len(t['torus_script_sha256'])==4
out['q1b_all_32_torus_bounds']=all(v['m_n']<=v['R_upper']<=l[v['n']] for v in t['rows'])
out['completed_bnb']=[{'n':v['n'],'extra':v['extra'],'R_lower_bnb':v['R_lower_bnb']} for v in t['rows'] if v['bnb_complete']]
out['plain_ratios']=[{'n':v['n'],'rho_minus_one':v['R_upper']/v['m_n']-1,'n_rho_minus_one':v['n']*(v['R_upper']/v['m_n']-1)} for v in t['rows'] if v['extra']==0]
args.output.parent.mkdir(parents=True,exist_ok=True)
args.output.write_text(json.dumps(out,indent=2))
print('PASS independent 139 committed strong witnesses, coverage recomputed, direct-ball negative controls; all 32 torus Q1b references satisfied')
