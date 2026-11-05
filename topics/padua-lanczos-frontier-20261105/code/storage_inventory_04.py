#!/usr/bin/env python3
"""Index handoff04 temporary outputs; hash verification only, no scientific runs."""
import argparse,hashlib,json
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args()
topic=Path(__file__).resolve().parents[1]
index=topic/'cold-storage-04.json'
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
 'g1_flint':{'path':'/tmp/padua-lanczos-frontier-g1-fast','commands_and_checks':'g1-optimization.md; evidence/g1-fast*.json; independent-checks-g1-04.md'},
 'g1_native':{'path':'/tmp/padua-lanczos-frontier-g1-fast-independent','commands_and_checks':'independent-checks-g1-04.md; evidence/g1-fast-independent*.json'},
 'g4':{'path':'/tmp/padua-lanczos-frontier-l7','commands_and_checks':'g4-methods.md; evidence/g4-*.json; independent-checks-frontier-04.md'},
 'g3_independent':{'path':'/tmp/padua-lanczos-frontier-g3-independent','commands_and_checks':'independent-checks-g3-04.md; evidence/g3-independent.json'},
 'g3':{'path':'/tmp/padua-lanczos-frontier-g3','commands_and_checks':'g3-methods.md; independent-checks-g3-04.md; evidence/g3-*.json'} }
rows=[]
for group,r in roots.items():
 base=Path(r['path'])
 for f in sorted(base.rglob('*')):
  if f.is_file() and '__pycache__' not in f.parts:rows.append({'group':group,'path':str(f.relative_to(base)),**identity(f)})
out=Path('/tmp/padua-lanczos-frontier-storage/handoff04-inventory.json');out.parent.mkdir(exist_ok=True)
out.write_text(json.dumps({'roots':roots,'files':rows},separators=(',',':'))+'\n')
index.write_text(json.dumps({'state':'LOCAL_ONLY_NOT_DELIVERED','inventory':{'path':str(out),**identity(out),'entries':len(rows)},'roots':roots,'builder':{'path':str(Path(__file__).relative_to(topic)),**identity(Path(__file__))},'command':'python -B topics/padua-lanczos-frontier-20261105/code/storage_inventory_04.py','check_command':'python -B topics/padua-lanczos-frontier-20261105/code/storage_inventory_04.py --check','prior_inventory':'cold-storage.json (unchanged historical index)','retention':'Temporary local files; no Windows delivery or retention guarantee. Scientific regeneration commands/source and input pins in the linked methods and per-run receipts. Full raw inventory stays outside Git; rebuilding after regeneration records new bytes.'},indent=2)+'\n')
print('Indexed',len(rows),'files')
