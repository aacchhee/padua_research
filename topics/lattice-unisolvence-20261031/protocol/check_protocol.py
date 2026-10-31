#!/usr/bin/env python3
"""Read-only campaign bookkeeping checks; not a mathematical checker."""
import hashlib,json,pathlib,re,subprocess
R=pathlib.Path(__file__).resolve().parents[3]
T=R/'topics/lattice-unisolvence-20261031'
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
paths=sorted(p for base in [T,R/'tracks/lattice-unisolvence',R/'literature/lattice-unisolvence'] for p in base.rglob('*') if p.is_file() and '__pycache__' not in p.parts and 'protocol' not in p.parts)
paths+= [R/p for p in ['topics/padua-batch-20261031/ALLOCATIONS.md','PROOF_STATUS.md','ID_CROSSWALK.md','state/IDEAS.md','state/CURRENT.md','PAPER_MAP.md','tracks/README.md','topics/README.md','literature/INDEX.md']]
result={'head':subprocess.check_output(['git','rev-parse','HEAD'],cwd=R,text=True).strip(),'files':[{'path':str(p.relative_to(R)),'sha256':digest(p),'bytes':p.stat().st_size} for p in paths]}
links=[]
for p in paths:
 if p.suffix!='.md':continue
 for s in re.findall(r'\]\(([^)]+)\)',p.read_text()):
  s=s.split('#')[0].split(' "')[0].strip('<>')
  if not s or re.match(r'^[\w+.-]+:',s):continue
  if not (p.parent/s).exists():links.append({'file':str(p.relative_to(R)),'link':s})
result['broken_local_markdown_links']=links
manifest=T/'audit-targets.json'
if manifest.exists():
 m=json.loads(manifest.read_text());bad=[]
 for item in m['files']:
  p=R/item['path']
  if not p.exists() or digest(p)!=item['sha256'] or p.stat().st_size!=item['bytes']:bad.append(item['path'])
 result['audit_target_hash_mismatches']=bad
 result['audit_targets_sha256']=digest(manifest)
# Every nested SHA-256 in campaign JSON must resolve to retained bytes or an explicitly external artifact.
by_hash={}
for p in paths:by_hash.setdefault(digest(p),[]).append(str(p.relative_to(R)))
# Historical integration bytes and the external staged ZIP are explicit retained targets.
integ=json.loads((T/'integration-result.json').read_text())
for row in integ['verified_repairs']:
 for field,rev in [('parent_sha256',integ['parent_source']),('source_sha256',integ['lattice_source'])]:
  data=subprocess.check_output(['git','show',rev+':'+row['path']],cwd=R)
  assert hashlib.sha256(data).hexdigest()==row[field]
  by_hash.setdefault(row[field],[]).append('git:'+rev+':'+row['path'])
cold=json.loads((T/'cold-manifest.json').read_text())['archive'];archive=pathlib.Path(cold['staging_path'])
assert digest(archive)==cold['sha256'] and archive.stat().st_size==cold['bytes']
by_hash.setdefault(cold['sha256'],[]).append(str(archive))
resolved=[];unresolved=[]
def hashwalk(x,where):
 if isinstance(x,dict):
  for k,v in x.items():
   if k=='point_sha256':
    expected=hashlib.sha256(json.dumps((x['n'],x['lengths'],x['points']),separators=(',',':')).encode()).hexdigest()
    assert v==expected,where
   elif isinstance(v,str) and 'sha256' in k.lower() and re.fullmatch('[0-9a-f]{64}',v):
    (resolved if v in by_hash else unresolved).append({'field':where+'.'+k,'sha256':v,'matches':by_hash.get(v,[])})
   elif isinstance(v,(dict,list)):hashwalk(v,where+'.'+k)
 elif isinstance(x,list):
  for i,v in enumerate(x):hashwalk(v,where+'['+str(i)+']')
for p in paths:
 if p.suffix=='.json' and p.name not in {'audit-targets.json','cold-manifest.json','manifest-check.json'}:hashwalk(json.loads(p.read_text()),str(p.relative_to(R)))
result['source_output_sha256_links']={'resolved_fields':len(resolved),'unresolved':unresolved}
tr=json.loads((T/'directions/C0/count-trials.json').read_text()); rows=[dict(zip(tr['columns'],v)) for v in tr['trials']]
cat=json.loads((T/'directions/C0/catalogue.json').read_text())['patterns']
def key(x):return (x['d'],x['n'],tuple(x['lengths']),x['k'],tuple(x['a']),x.get('c',x.get('residues',[None])[0]))
assert len(rows)==5061 and len({key(x) for x in rows})==5061
assert {key(x) for x in rows if x['count']==x['target']}=={key(x) for x in cat}
assert len({x['id'] for x in cat})==451
assert sum(x['orbit_size'] for x in rows)==77616
result['c0_schema_coverage']={'rows':5061,'admissible':451,'failures':4610,'raw_orbit_total':77616}
tracked=subprocess.check_output(['git','ls-files','-z'],cwd=R,text=True).split('\0')[:-1]
result['tracked_pdf_fulltext_named_files']=[p for p in tracked if p.lower().endswith(('.pdf','.html','.htm','.epub')) or 'fulltext' in p.lower() or 'extract' in p.lower()]
gen=[(p,(R/p).stat().st_size) for p in tracked if pathlib.Path(p).suffix in {'.json','.jsonl','.csv','.tsv','.out','.npz','.npy','.svg','.png','.zip'}]
result['tracked_generated_extension_inventory']={'total_bytes':sum(n for _,n in gen),'largest':max(gen,key=lambda x:x[1]),'over_1MB':[x for x in gen if x[1]>1000000]}
result['c0_hash_manifest_mismatches']=[s.split('  ',1)[1] for s in (T/'directions/C0/hashes.txt').read_text().splitlines() if digest(R/s.split('  ',1)[1])!=s.split('  ',1)[0]]
print(json.dumps(result,indent=2))
