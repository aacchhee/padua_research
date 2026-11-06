"""Verified input loading for exact K1/K3 fits, full or compact essential data."""
import hashlib,json
from pathlib import Path
RAW_HASH='7ce16e5c61fb82fe1fc4125bbd9570fdc7579db7aa139cd116b4807322f500f2'
ESSENTIAL_HASH='7e18253a25fb8ab3b78389ef444c8014313b0d4231b6fb0c2467aaa062edacfb'
def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(path):
 h=digest(path);r=json.loads(path.read_text());assert h in [RAW_HASH,ESSENTIAL_HASH],'Unrecognized input receipt hash.'
 if h==ESSENTIAL_HASH:
  assert r['format']=='S4-essential-CC-v1' and r['raw_receipt_sha256']==RAW_HASH
  rows=[]
  for row in r['rows']:
   x=dict(zip(r['columns'],row));v={k:{'eigenvalue':x[k],'inverse_residual_2_float':x[k+'_inverse_residual_2_float'],'constraint_residual_float':x[k+'_constraint_residual_float']} for k in ['minimum','maximum']};guard=all(y['eigenvalue']>0 and y['inverse_residual_2_float']<=1e-9 and y['constraint_residual_float']<=1e-9 for y in v.values());rows.append(dict(N=x['N'],results=v,guards_pass=guard,inverse_extrema_order_pass=x['minimum']<=x['maximum']))
  r=dict(completed=True,fits_executed=False,results=rows)
 assert r['completed'] and len(r['results'])==42 and all(x['guards_pass'] and x['inverse_extrema_order_pass'] for x in r['results'])
 return r,dict(path=str(path),sha256=h,bytes=path.stat().st_size,loader_sha256=digest(__file__),original_full_raw_sha256=RAW_HASH)
