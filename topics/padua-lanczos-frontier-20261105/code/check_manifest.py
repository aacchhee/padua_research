#!/usr/bin/env python3
"""Verify/rebuild a content-addressed file inventory; no scientific computation."""
import argparse,hashlib,json,subprocess
from pathlib import Path
root=Path(__file__).resolve().parents[3]
topic=Path(__file__).resolve().parents[1]
mp=topic/'evidence-manifest.json'
ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');ap.add_argument('--cached',action='store_true');ap.add_argument('--rules');opts=ap.parse_args()
def inventory():
    files={}
    for name in sorted(subprocess.check_output(['git','ls-files'],cwd=root,text=True).splitlines()):
        p=root/name
        if not(p.is_relative_to(topic) or name=='results/padua-lanczos-frontier-20261105.md'):continue
        if p==mp or p==topic/'LOG.md' or 'handoffs' in p.parts or '__pycache__' in p.parts:continue
        b=subprocess.check_output(['git','show',':'+name],cwd=root) if opts.cached else p.read_bytes()
        key=str(p.relative_to(topic)) if p.is_relative_to(topic) else '@'+name
        files[key]=[len(b),hashlib.sha256(b).hexdigest()]
    return files
def encoded(files):return (json.dumps({'files':files},sort_keys=True,separators=(',',':'))+'\n').encode()
if opts.write:
    files=inventory();b=encoded(files);digest=hashlib.sha256(b).hexdigest()
    out=Path('/tmp/padua-lanczos-frontier-storage')/('files-'+digest+'.json');out.parent.mkdir(exist_ok=True);out.write_bytes(b)
    mp.write_text(json.dumps({'format':'regenerable-file-inventory-v1','source_rules_commit':opts.rules,'scope':'All tracked topic/results files except LOG, handoffs and this manifest; identities only, not scientific acceptance.','inventory':{'path':str(out),'bytes':len(b),'sha256':digest,'files':len(files)},'verification':'Recompute the entire canonical file inventory from repository bytes; external inventory is not an acceptance dependency. Individual rows remain in the external content-addressed inventory and can be regenerated with this committed helper.','build_command':'python -B topics/padua-lanczos-frontier-20261105/code/check_manifest.py --write --rules '+str(opts.rules),'retention':'Local temporary inventory only; no archival delivery or retention promised.'},indent=2)+'\n')
    print('WROTE',len(files),'file identities; external bytes',len(b));raise SystemExit
m=json.loads(mp.read_text())
if m.get('format')=='regenerable-file-inventory-v1':
    files=inventory();b=encoded(files);e=m['inventory']
    assert len(files)==e['files'] and len(b)==e['bytes'] and hashlib.sha256(b).hexdigest()==e['sha256'],'Inventory differs; inspect Git changes or regenerate expected rows from their pinned source commit'
    print('PASS:',len(files),'pinned checkpoint files (repository-only reconstruction)');raise SystemExit
# Historic schemas remain verifiable.
files=m['files']
if isinstance(files,dict):
    rows=[{'path':p,'bytes':v[0],'sha256':v[1]} for p,v in files.items()]
    for r in rows:
        p=r['path'];r['path']=str((root/p[1:]) if p.startswith('@') else topic/p)
else:
    rows=files
    for r in rows:r['path']=str(root/m.get('path_roots',{}).get(r.get('root'),'')/r['path'])
for r in rows:
    b=Path(r['path']).read_bytes();assert len(b)==r['bytes'] and hashlib.sha256(b).hexdigest()==r['sha256'],r['path']
print('PASS:',len(rows),'pinned historic checkpoint files')
