#!/usr/bin/env python3
"""Index handoff05 temporary outputs; hash verification only, no scientific runs."""
import argparse,hashlib,json
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args()
topic=Path(__file__).resolve().parents[1]
index=topic/'cold-storage-05.json'
def identity(f):
 h=hashlib.sha256()
 with f.open('rb') as s:
  for b in iter(lambda:s.read(1048576),b''):h.update(b)
 return {'bytes':f.stat().st_size,'sha256':h.hexdigest()}
if a.check:
 d=json.loads(index.read_text());f=Path(d['inventory']['path']);assert identity(f)=={k:d['inventory'][k] for k in ('bytes','sha256')}
 raw=json.loads(f.read_text());missing=[]
 for r in raw['files']:
  f=Path(raw['roots'][r['group']]['path'])/r['path']
  if not f.exists():missing.append(str(f));continue
  assert identity(f)=={k:r[k] for k in ('bytes','sha256')},str(f)
 assert not missing,missing
 print('PASS',len(raw['files']),'retained raw identities');raise SystemExit
roots={
 'n4_diagnostic':{'path':'/tmp/padua-lanczos-frontier-g3-n4-diagnostic','commands_and_checks':'g3-n4-diagnostic-methods.md; evidence/g3-n4-diagnostic*.json'},
 'l6_n1':{'path':'/tmp/padua-lanczos-frontier-l6-n1','commands_and_checks':'l6-n1-methods.md; evidence/l6-n1*.json'},
 'l6_independent':{'path':'/tmp/padua-lanczos-frontier-l6-n1-independent','commands_and_checks':'independent-checks-frontier-05.md; evidence/l6-n1-independent.json'},
 'fit':{'path':'/tmp/padua-lanczos-frontier-g1-fit','commands_and_checks':'g1-fit-methods.md; synthetic controls and actual complete-scan report; executions separately labeled'},
 'fit_independent':{'path':'/tmp/padua-lanczos-frontier-g1-fit-independent','commands_and_checks':'independent-checks-g1-fit.md; synthetic controls and actual complete-scan report; executions separately labeled'},
 'g1_native_remaining':{'path':'/tmp/padua-lanczos-frontier-g1-native-remaining','commands_and_checks':'g1-remaining-scan.md; independent-checks-g1-05.md; evidence/g1-batch-independent-native*.json'},
 'n5_producer':{'path':'/tmp/padua-lanczos-frontier-g3-n5','commands_and_checks':'g3-n5-methods.md; evidence/g3-n5*.json'},
 'n5_independent':{'path':'/tmp/padua-lanczos-frontier-g3-n5-independent','commands_and_checks':'independent-checks-g3-06.md; evidence/g3-n5-independent*.json'},
 'g1_batch':{'path':'/tmp/padua-lanczos-frontier-g1-batch','commands_and_checks':'g1-batching.md; evidence/g1-batch*.json; independent-checks-g1-05.md'},
 'g1_check':{'path':'/tmp/padua-lanczos-frontier-g1-check05','commands_and_checks':'independent-checks-g1-05.md; evidence/g1-batch-independent*.json'},
 'l7_suite':{'path':'/tmp/padua-lanczos-frontier-l7-suite','commands_and_checks':'l7-suite-methods.md; evidence/l7-suite*.json'},
 'l7_independent':{'path':'/tmp/padua-lanczos-frontier-l7-independent','commands_and_checks':'independent-checks-frontier-05.md; evidence/l7-independent.json'},
 'n4_producer':{'path':'/tmp/padua-lanczos-frontier-g3-n4','commands_and_checks':'g3-n4-methods.md; evidence/g3-n4*.json'},
 'n4_independent':{'path':'/tmp/padua-lanczos-frontier-g3-n4-independent','commands_and_checks':'independent-checks-g3-05.md; evidence/g3-n4-independent*.json'} }
rows=[]
for group,r in roots.items():
 base=Path(r['path'])
 for f in sorted(base.rglob('*')):
  if f.is_file() and '__pycache__' not in f.parts:rows.append({'group':group,'path':str(f.relative_to(base)),**identity(f)})
out=Path('/tmp/padua-lanczos-frontier-storage/handoff05-inventory.json');out.parent.mkdir(exist_ok=True)
out.write_text(json.dumps({'roots':roots,'files':rows},separators=(',',':'))+'\n')
index.write_text(json.dumps({'state':'LOCAL_ONLY_NOT_DELIVERED','inventory':{'path':str(out),**identity(out),'entries':len(rows)},'roots':roots,'builder':{'path':str(Path(__file__).relative_to(topic)),**identity(Path(__file__))},'command':'python -B topics/padua-lanczos-frontier-20261105/code/storage_inventory_05.py','check_command':'python -B topics/padua-lanczos-frontier-20261105/code/storage_inventory_05.py --check','prior_inventory':'cold-storage.json and cold-storage-04.json (unchanged historical indices)','retention':'Temporary local files; no Windows delivery or retention guarantee. Scientific regeneration commands/source and input pins in the linked methods and per-run receipts. Full raw inventory stays outside Git; rebuilding after regeneration records new bytes.'},indent=2)+'\n')
print('Indexed',len(rows),'files')
