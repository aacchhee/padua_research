"""M0a comparison against rounded historical table and fresh precision replay."""
import json,re,hashlib,sys
from pathlib import Path
import mpmath as mp
mp.mp.dps=320
root=Path(__file__).resolve().parents[3]
out=Path(sys.argv[1])
history=root/'topics/nn-mop-stability-20261105/attempts/D1.md'
tab={int(m[1]):[m[i].strip() for i in range(2,6)] for m in re.finditer(r'^\| (\d+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \|$',history.read_text(),re.M)}
receipt={'gate':'M0a','original_M0':'UNASSESSABLE: historical full precision absent','cases':[],'inputs':[]}
for family,ix in [('krawtchouk',0),('hahn',1)]:
 runs=[]
 for suffix in ['', '260']:
  p=out/f'm0-{family}{suffix}.json'; b=p.read_bytes();runs.append(json.loads(b))
  receipt['inputs'].append({'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
 a,b=runs
 assert [r['N'] for r in a['cases']]==[4,16,32]
 assert [r['N'] for r in b['cases']]==[4,16,32]
 assert a['code_sha256']==b['code_sha256'] and a['baseline_sha256']==b['baseline_sha256']
 for lo,hi in zip(a['cases'],b['cases']):
  assert lo['input_sha256']==hi['input_sha256']
  for target,col in [('NN',ix),('step_line',ix+2)]:
   x,y=[mp.mpf(r[target]['mixed']['kappa']) for r in [lo,hi]]
   rel=abs(x/y-1); rounded=mp.nstr(y,7)
   assert rel<mp.mpf('1e-10')
   assert mp.mpf(rounded)==mp.mpf(tab[lo['N']][col])
   receipt['cases'].append({'family':family,'N':lo['N'],'target':target,'kappa':mp.nstr(y,30),'relative_precision_difference':mp.nstr(rel,8),'historical_cell':tab[lo['N']][col]})
receipt['verdict']='PASS'
receipt['historical_table_sha256']=hashlib.sha256(history.read_bytes()).hexdigest()
print(json.dumps(receipt,indent=2))
