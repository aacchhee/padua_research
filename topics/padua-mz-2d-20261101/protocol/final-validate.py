"""Mechanical verification of approved assignment; no scientific audit."""
import collections,hashlib,json,pathlib,re,subprocess,urllib.parse
R=pathlib.Path('.');P=R/'topics/padua-mz-2d-20261101/protocol';T=P.parent
D=json.loads((P/'final-assignment-checks.json').read_text());M=json.loads((P/'final-id-map.json').read_text())
def sha(b):return hashlib.sha256(b).hexdigest()
def git(*args):return subprocess.check_output(['git',*args])
base='806cc7b4509fd93bae652f9545d32d95529f8281'
results={};ids={}
for file,key,pat in [('PROOF_STATUS.md','proof',r'^\| (PD-[TN]\d+)\b'),('state/IDEAS.md','idea',r'^\| (IDEA-\d+)\b'),('literature/INDEX.md','literature',r'^\| (LIT-\d+)\b')]:
 now=collections.Counter(re.findall(pat,pathlib.Path(file).read_text(),re.M));old=collections.Counter(re.findall(pat,git('show',base+':'+file).decode(),re.M));added=now-old
 assert not old-now,(file,'lost old rows')
 assert all(v==1 for v in added.values()),(file,'new duplicate primary rows')
 if key!='idea':assert all(v==1 for v in now.values())
 results[key]={'rows':sum(now.values()),'distinct_ids':len(now),'new_primary_ids':sorted(added),'prior_historical_repeat_counts_unchanged':True};ids[key]=now
assert len(results['proof']['new_primary_ids'])==22
assert len(results['idea']['new_primary_ids'])==18
assert results['literature']['new_primary_ids']==['LIT-427','LIT-428']
for old,new in M['mapping'].items():
 if old.startswith('PD-T'):assert 106<=int(new[4:])<=117
 elif old.startswith('PD-N'):assert 44<=int(new[4:])<=53
 elif old.startswith('IDEA'):assert 210<=int(new[5:])<=227
 elif new not in ['LIT-312','LIT-014','LIT-379','LIT-314','LIT-045']:assert 427<=int(new[4:])<=428
for item in D['protected_inputs']:assert sha(pathlib.Path(item['path']).read_bytes())==item['sha256'],item['path']
archive=T/'directions/d4-positive-floor-verification.md';bodyhash=sha(archive.read_bytes()[2255:]);assert bodyhash=='bcecd47698bea9679f6b734a26f8afb0fd85874a51b414ad75cf9ac650e98903'
# Markdown links outside fenced code. Keep math prose; only fenced code is removed.
bad=[];links=0
for row in D['changed_files']:
 path=pathlib.Path(row['path'])
 if path.suffix!='.md':continue
 text=path.read_text();lines=[];fenced=False
 for line in text.splitlines():
  if re.match(r'^\s*(```|~~~)',line):fenced=not fenced;continue
  if not fenced:lines.append(line)
 for raw in re.findall(r'\[[^\]]*\]\(([^)]+)\)','\n'.join(lines)):
  target=raw.split('#',1)[0].split(' ',1)[0].strip('<>')
  if not target or re.match(r'[a-z]+:',target):continue
  links+=1
  if not (path.parent/urllib.parse.unquote(target)).exists():bad.append({'file':str(path),'target':target})
assert not bad,bad
# All earlier tracked MZ code/evidence/manuscript/source objects and A1 pins retained.
objects=json.loads((P/'final-input-manifest.json').read_text());protected_prior=[]
for item in objects['local_MZ_objects']:
 path=pathlib.Path(item['path'])
 if item['base_blob'] and item.get('unchanged_from_base') and ('code' in path.parts or 'evidence' in path.parts or 'paper' in path.parts or 'sources' in path.parts or (path.parent.name=='theory' and not path.name.startswith('mz2d'))):
  assert sha(path.read_bytes())==item['sha256'],str(path);protected_prior.append(str(path))
peer=[];pre={x['path']:x['before_sha256'] for x in D['source_ID_only_impact']}
for report in T.glob('independent-math*.md'):
 for line in report.read_text().splitlines():
  m=re.search(r'`(tracks/[^`]+)`.*`([a-f0-9]{64})`',line)
  if not m:continue
  path,h=m.groups()
  if path.endswith('mz2d-fixed-ratio-energy-conversion-obstruction.md'):
   peer.append({'report':str(report),'historical_path':path,'pinned_sha256':h,'disposition':'Original proof recovered exactly from verification-only archive byte offset2255','archive_body_matches':h==bodyhash});assert h==bodyhash
  elif h==pre.get(path):peer.append({'report':str(report),'path':path,'pinned_sha256':h,'pre_ID_pin_matches':True})
  else:
   assert path.endswith('mz2d-lower-corner-subtraction-obstruction.md') and h=='b7ebf2023118c2fbd2c492ff6318addee2802a3faad1244caed5db840705fcac'
   assert pre[path]=='282bc22de3a15056bef406ddc6a3aa4f268a62b4c54a2574b82208e8240a63a1'
   supplementary=(T/'supplementary-audit.md').read_text()
   assert '282bc22de3a15056bef406ddc6a3aa4f268a62b4c54a2574b82208e8240a63a1' in supplementary
   peer.append({'report':str(report),'path':path,'old_peer_sha256':h,'final_pre_ID_sha256':pre[path],'material_pre_ID_extension':'D3 added fixed-theta corollary using K_n~n^4/24 BEFORE assignment; old peers cover endpoint-only scope','separate_validation':'Final supplementary Astra late fixed-theta reconstruction checks exact282bc22 source and passes; old peer reports preserved. ID-only impact applies against final Astra pin, not original peer pin.'})
files=[]
for p in T.rglob('*'):
 if p.is_file() and p.suffix in ['.json','.gz'] and '__pycache__' not in p.parts:files.append({'path':str(p),'bytes':p.stat().st_size})
assert max(x['bytes'] for x in files)<=1000000
assert sum(x['bytes'] for x in files)<5000000
# These are conservative counts including manifests, not only generated evidence.
ledger=pathlib.Path('topics/padua-batch-20261031/ALLOCATIONS.md').read_text()
for a in ['PD-T136–PD-T155','PD-N062–PD-N071','IDEA-246–IDEA-285','LIT-445–LIT-459','6920ba632843597c37e1493d077c1df2e89f54cb','PD-T118–135','PD-N054–061','IDEA-228–245','LIT-429–444']:assert a in ledger,a
result={'status':'PASS','mechanical_scope':'ID-only assignment/registration checks; no new scientific audit','registry_counts':results,'mapping_membership':'All assignments in own reserved ranges; five reused LIT IDs already accepted; historicalN41 aliasesN045','local_markdown_links_checked':links,'broken_local_markdown_links':bad,'protected_frozen_files':len(D['protected_inputs']),'old_MZ_code_evidence_manuscript_sources_unchanged':len(protected_prior),'archive_body_start':2255,'archive_body_sha256':bodyhash,'peer_review_impact':peer,'source_ID_only_checks':D['source_ID_only_impact'],'generated_plus_manifest_size_check':{'file_count':len(files),'total_bytes':sum(x['bytes'] for x in files),'largest_bytes':max(x['bytes'] for x in files)},'stage':'AUDIT','Claude':'PENDING','limitations':'External links identified by pinned source provenance; no network fetch of every URL. Source status unchanged. Root-owned final summaries may be edited after this run.'}
(P/'final-validation.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k not in ['peer_review_impact','source_ID_only_checks']}))
