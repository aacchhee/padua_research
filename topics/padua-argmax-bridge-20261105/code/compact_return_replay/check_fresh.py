import sys,json,hashlib
from pathlib import Path
ROOT=Path('/workspace/padua_research')
PKG=ROOT/'local-output/argmax-bridge-20261105/compact-release-aea62883/padua30'
OUT=ROOT/'local-output/argmax-bridge-20261105/actual-return-20261107'
sys.path.insert(0,str(PKG))
from evidence import Access,validate_pass,require
from common import manifest,digest
from plans import ENGINE
m=manifest(PKG)
assert digest((PKG/'runtime_manifest.json').read_bytes())=='5b89fa66e742952497f99a49110a965ada2828b1861917268d3074af0eb22a16'
class Local(Access):
 def identity(self,row):
  p=Path(row['path']);assert p.is_absolute() and '..' not in p.parts
  data=p.read_bytes();assert len(data)==row['bytes'] and digest(data)==row['sha256'],str(p)
  self.checked.add(str(p));return data
 def data(self,name):
  return ((PKG/name) if name in m['files'] else (ROOT/name)).read_bytes()
a=Local(PKG,str(ROOT));a.checked=set()
mm={'files':{str(PKG.relative_to(ROOT)/k):v for k,v in m['files'].items()}}
results=[]
for n in [199,238]:
 prefix=str((OUT/('verify-n'+str(n))).relative_to(ROOT))
 receipt=json.loads(validate_pass(a,prefix,n,'verify',mm))
 primary=json.loads((OUT/('primary-n'+str(n)+'.json')).read_bytes())
 fields=['n','tree','pi_bracket','S_upper_rows','origin_lower_hex','lambda_upper_rows','norm','floor','corner','analytic_far','verification']
 assert all(receipt[k]==primary[k] for k in fields)
 ex=json.loads((OUT/('verify-n'+str(n)+'-exit.json')).read_bytes())
 assert ex['observed_returncode']==0 and ex['ECHILD'] and not ex['cleanup_killed'] and ex['SIGCHLD']=='SIG_DFL'
 cp=a.json(prefix+'/checker-checkpoint.json')
 results.append({'n':n,'complete_validate_pass':True,'proof_fields_equal_primary':fields,'native_calls':len(cp['completed_calls']),'receipt_sha256':digest((ROOT/prefix/'essential-receipt.json').read_bytes()),'raw_sha256':digest((ROOT/prefix/'raw-evidence.json').read_bytes())})
print(json.dumps({'results':results,'distinct_identity_paths_rehashed':len(a.checked)},indent=2))
