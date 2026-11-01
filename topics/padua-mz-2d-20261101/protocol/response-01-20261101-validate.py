"""Documentation response integrity/reservation check; never runs scientific producers.
Run from repository root. Writes only new response-01-20261101-* receipts.
"""
import collections, datetime, hashlib, json, pathlib, platform, re, subprocess, sys, urllib.parse
R=pathlib.Path('.'); T=R/'topics/padua-mz-2d-20261101'; P=T/'protocol'
BASE='d04a39bb8481fa3320ea98b9d70cfb3bbf4b3878'
PREFIX='response-01-20261101-'
def sha(b): return hashlib.sha256(b).hexdigest()
def git(*a): return subprocess.check_output(['git',*a])
def blob(h,p): return git('show',h+':'+str(p))
def info(p,b): return {'path':str(p),'bytes':len(b),'sha256':sha(b)}
def save(n,d): (P/(PREFIX+n+'.json')).write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
def require(v,msg):
 if not v: raise AssertionError(msg)
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
connector=json.loads((P/(PREFIX+'connector.json')).read_text())
heads=[{'label':'main','sha':connector['main']}]+[{'label':'PR'+str(x['number']),'sha':x['sha']} for x in connector['open_prs']]
closed=[x for x in connector['closed_prs'] if not x['merged_at']]
heads += [{'label':'closed-unmerged PR'+str(x['number']),'sha':x['head']} for x in closed]
registries=['PROOF_STATUS.md','state/IDEAS.md','literature/INDEX.md','ID_CROSSWALK.md']
ranges={'PD-T':[106,135],'PD-N':[44,61],'IDEA':[210,245],'LIT':[427,444]}
scan=[]
for head in heads:
 names=git('ls-tree','-r','--name-only',head['sha']).decode().splitlines()
 paths=registries+[n for n in names if n.endswith('/ALLOCATIONS.md')]
 entry={**head,'files':[],'namespace_maximum_mentions':{},'retired_reservation_lines':[]}
 alltext=[]
 for path in paths:
  b=blob(head['sha'],path); text=b.decode(); alltext.append(text)
  item=info(path,b);item.update(git_blob=git('rev-parse',head['sha']+':'+path).decode().strip(),complete_byte_read=True)
  entry['files'].append(item)
  if path.endswith('ALLOCATIONS.md'):
   entry['retired_reservation_lines'] += [{'path':path,'line':i+1,'text':l} for i,l in enumerate(text.splitlines()) if 'retir' in l.lower()]
 for ns in ranges:
  nums=[int(n) for n in re.findall(r'(?<![A-Za-z0-9])'+re.escape(ns)+('-' if ns in ['IDEA','LIT'] else '')+r'(\d+)\b','\n'.join(alltext))]
  entry['namespace_maximum_mentions'][ns]=max(nums,default=0)
 # Primary registry rows cannot consume this campaign's namespace on other branches.
 if head['label'] not in ['PR14']:
  for path in registries[:3]:
   text=blob(head['sha'],path).decode()
   for ident in re.findall(r'^\| ((?:PD-[TN]|IDEA-|LIT-)\d+)\b',text,re.M):
    ns=re.sub(r'\d+$','',ident).rstrip('-'); n=int(re.search(r'\d+$',ident).group())
    if ns in ranges: require(not ranges[ns][0]<=n<=ranges[ns][1],(head['label'],path,ident,'collision'))
 scan.append(entry)
# Existing reservation prose is retained exactly, including historic retired-reservation statements.
ledger='topics/padua-batch-20261031/ALLOCATIONS.md'
oldledger=blob(BASE,ledger); currentledger=R.joinpath(ledger).read_bytes()
require(currentledger==oldledger,'Response unexpectedly changes ledger reservations')
for token in ['PD-T118–135','PD-N054–061','IDEA-228–245','LIT-429–444','6920ba632843597c37e1493d077c1df2e89f54cb']:
 require(token in currentledger.decode(),token)
for h in heads:
 if h['label']=='PR15':
  txt=blob(h['sha'],ledger).decode()
  for token in ['PD-T106–PD-T135','PD-N044–PD-N061','IDEA-210–IDEA-245','LIT-427–LIT-444','PD-T136–PD-T155','PD-N062–PD-N071','IDEA-246–IDEA-285','LIT-445–LIT-459']:
   require(token in txt,(h['label'],token))
pr12=next(h['sha'] for h in heads if h['label']=='PR12')
pins=[]
for item in json.loads((P/'input-manifest.json').read_text())['A2']['files']:
 b=blob(pr12,item['path']); require(sha(b)==item['sha256'],('A2 changed',item['path']))
 pins.append({**info(item['path'],b),'frozen_commit':item['commit'],'latest_commit':pr12,'latest_git_blob':git('rev-parse',pr12+':'+item['path']).decode().strip(),'unchanged':True})
require(len(pins)==13,'A2 pin count')
reservation={'status':'PASS','executed_at_utc':now,'rules_sha':BASE,'source':info(P/(PREFIX+'connector.json'),(P/(PREFIX+'connector.json')).read_bytes()),'heads':scan,'closed_unmerged_prs':closed,'closed_prs_examined':len(connector['closed_prs']),'campaign_ranges_unchanged':ranges,'union_reserved_maxima':{'PD-T':155,'PD-N':71,'IDEA':285,'LIT':459},'mention_maxima_note':'Raw mention maxima include historical NEXT labels and are not allocation boundaries. No allocation occurs.','retired_reservations':'No closed-unmerged PR returned; all ledger retired-reservation references read completely; existing ledger unchanged byte for byte, including historical reservation/headroom records.','allocation_performed':False,'A2_pins':pins,'verdict':'Own permanent reservations unchanged and disjoint; PR12 no-range; PR15 higher ranges unchanged. No new ID or range.'}
save('reservation-recheck',reservation)
# Permit exactly the listed response files; all other tracked baseline files immutable.
allowed={
 'PROOF_STATUS.md','state/IDEAS.md','ID_CROSSWALK.md','state/CURRENT.md','PAPER_MAP.md','topics/README.md','tracks/mz-constants/README.md',
 str(T/'ideas-d4.md'),str(T/'ideas-d5.md'),str(T/'directions/D4.md'),
 'tracks/mz-constants/theory/mz2d-fixed-ratio.md',
 'tracks/mz-constants/theory/mz2d-fixed-ratio-diamond-reconstruction.md',
 'tracks/mz-constants/theory/mz2d-upper-sign-obstruction.md',
 str(T/'LOG.md'),str(T/'report.md'),str(T/'plan.md')}
tracked=git('ls-tree','-r','--name-only',BASE).decode().splitlines(); protected=[]; changes=[]
for path in tracked:
 before=blob(BASE,path); require(R.joinpath(path).exists(),('deleted',path)); after=R.joinpath(path).read_bytes()
 if before!=after:
  require(path in allowed,('unlisted modification',path)); changes.append({'path':path,'before_sha256':sha(before),'after_sha256':sha(after),'before_bytes':len(before),'after_bytes':len(after)})
 else: protected.append(info(path,after))
# Shared summaries change only this campaign's appended PR14 section.
for path in ['state/CURRENT.md','topics/README.md','tracks/mz-constants/README.md']:
 title='## Padua MZ 2D campaign — PR14 final registration'
 require(blob(BASE,path).decode().split(title)[0]==R.joinpath(path).read_text().split(title)[0],('unrelated summary content changed',path))
# PAPER_MAP changes only the named campaign row.
def unrelated_paper_rows(s): return '\n'.join(l for l in s.splitlines() if not l.startswith('| [Signed Padua MZ campaign]'))
require(unrelated_paper_rows(blob(BASE,'PAPER_MAP.md').decode())==unrelated_paper_rows(R.joinpath('PAPER_MAP.md').read_text()),'unrelated PAPER_MAP content changed')
# Preserve entire old MZ input set, including PD-T028; no selective scientific exemptions.
oldobjects=[]
for item in json.loads((P/'final-input-manifest.json').read_text())['local_MZ_objects']:
 if item.get('base_blob') and item.get('unchanged_from_base') and ('code' in pathlib.Path(item['path']).parts or 'evidence' in pathlib.Path(item['path']).parts or 'paper' in pathlib.Path(item['path']).parts or 'sources' in pathlib.Path(item['path']).parts or (pathlib.Path(item['path']).parent.name=='theory' and not pathlib.Path(item['path']).name.startswith('mz2d'))):
  b=R.joinpath(item['path']).read_bytes(); require(sha(b)==item['sha256'],('old MZ input',item['path']));oldobjects.append(info(item['path'],b))
require(len(oldobjects)==73,('old input count',len(oldobjects)))
f1='tracks/mz-constants/theory/mz2d-upper-sign-obstruction.md'; before=blob(BASE,f1); after=R.joinpath(f1).read_bytes()
require(sha(after)=='df527d30b462dc34f2e7a14fa62a19a129b08aa2e165ebc0d731a7fb5c9d4b6a','F1 exact transcribed file identity')
marker=b'## Proof or evidence'; require(before[before.index(marker):]==after[after.index(marker):],'F1 proof-to-EOF changed')
proof=after.split(marker+b'\n\n',1)[1].split(b'\n## Scope',1)[0]
require(sha(proof)=='077f0c1f31e5f25c787553f9caa11e0b980a408c1d7b0eeb3f047b5fe3c5d26c','F1 proof hash')
# F2 changes are literal identifier normalization only, checked against baseline.
f2={
 str(T/'ideas-d4.md'):[('Historical provisional `PD-N045` is an alias mapped to N10,','Historical provisional `PD-N?mz2d-codex-41` is an alias mapped to PD-N045,'),('candidate 40','IDEA-224'),('Existing N10','Existing PD-N045'),('its old N41 alias mapped to canonical N10','its old PD-N?mz2d-codex-41 alias mapped to canonical PD-N045')],
 str(T/'ideas-d5.md'):[('candidate 31','IDEA-220')],
 str(T/'directions/D4.md'):[('N10','PD-N045'),('historical N41','historical PD-N?mz2d-codex-41')],
 'tracks/mz-constants/theory/mz2d-fixed-ratio.md':[('N41','PD-N?mz2d-codex-41'),('N10','PD-N045')],
 'tracks/mz-constants/theory/mz2d-fixed-ratio-diamond-reconstruction.md':[('candidate 42','IDEA-226')]
}
for path,replacements in f2.items():
 expected=blob(BASE,path).decode()
 for old,new in replacements: expected=expected.replace(old,new)
 require(expected==R.joinpath(path).read_text(),('F2 changes beyond ID normalization',path))
# Every unaffected section in F1 remains byte-identical.
for title in ['Definitions','Assumptions','Status by part','Depends on','Checks','Sources']:
 def section(b): return b.split(('## '+title+'\n').encode(),1)[1].split(b'\n## ',1)[0]
 require(section(before)==section(after),('F1 section',title))
def rows(text):
 return {m.group(1):m.group(0) for m in re.finditer(r'^\| (PD-[TN]\d+)\b.*$',text,re.M)}
oldrows=rows(blob(BASE,'PROOF_STATUS.md').decode());newrows=rows(R.joinpath('PROOF_STATUS.md').read_text())
require(oldrows.keys()==newrows.keys(),'proof IDs changed')
campaign={f'PD-T{n:03}' for n in range(106,118)}|{f'PD-N{n:03}' for n in range(44,54)}
proofrows=[]
for ident,old in oldrows.items():
 new=newrows[ident]
 if ident not in campaign: require(old==new,('other proof row changed',ident));continue
 a=[x.strip() for x in re.split(r'(?<!\\)\|',old)[1:-1]];b=[x.strip() for x in re.split(r'(?<!\\)\|',new)[1:-1]]
 require(len(a)==len(b)==8,(ident,'column count'))
 for col in [0,1,2,6]:require(a[col]==b[col],(ident,'fixed column',col))
 require('Written proof or finite evidence as explicitly distinguished in record' not in new,(ident,'boilerplate'))
 proofrows.append({'id':ident,'status':b[2],'evidence':b[3],'disposition':b[4],'depends_on':b[5],'audit':b[7]})
require(collections.Counter(x['status'] for x in proofrows)=={'PROVED':17,'MEASURED':2,'OPEN':3},'status tally')
for ident,tokens in {'PD-T110':['PD-T106, PD-T109','PD-T021 marginal support only','PD-T014/022 background only'],'PD-T114':['PD-T112, PD-T113'],'PD-T116':['PD-T106/109','PD-T115','PD-N045/053 obstruction context only']}.items():
 row=next(x for x in proofrows if x['id']==ident)
 for token in tokens: require(token in row['depends_on'],('F4 dependencies',ident,token))
# Registry non-row content is unchanged apart from the PR14 acceptance paragraph.
def without_rows(text): return re.sub(r'^\| PD-[TN]\d+\b.*$','',text,flags=re.M)
a=without_rows(blob(BASE,'PROOF_STATUS.md').decode());b=without_rows(R.joinpath('PROOF_STATUS.md').read_text())
a=re.sub(r'^Stage \*\*AUDIT\*\*, required Claude.*$','ADMIN_ACCEPTANCE_PARAGRAPH',a,flags=re.M)
b=re.sub(r'^Stage \*\*PR\*\*, pending AC.*$','ADMIN_ACCEPTANCE_PARAGRAPH',b,flags=re.M)
require(a==b,'PROOF_STATUS content outside rows/admin paragraph changed')
# No registry row IDs are added/deleted/duplicated by F1–F6; obstruction rows use links.
for path,pat in [('PROOF_STATUS.md',r'^\| (PD-[TN]\d+)\b'),('state/IDEAS.md',r'^\| (IDEA-\d+)\b'),('literature/INDEX.md',r'^\| (LIT-\d+)\b')]:
 a=collections.Counter(re.findall(pat,blob(BASE,path).decode(),re.M));b=collections.Counter(re.findall(pat,R.joinpath(path).read_text(),re.M));require(a==b,(path,'ID counts changed'))
 if path!='state/IDEAS.md': require(max(b.values())==1,(path,'duplicate IDs'))
ideasbefore=blob(BASE,'state/IDEAS.md').decode();ideasafter=R.joinpath('state/IDEAS.md').read_text()
require(ideasafter.startswith(ideasbefore),'F5 must append only')
appended=ideasafter[len(ideasbefore):]
require('Padua MZ 2D obstruction and disposition table' in appended,'F5 heading')
for n in range(44,54):require(len(re.findall(r'^\| \[?PD-N'+f'{n:03}',appended,re.M))==1,('F5 row',n))
# Local Markdown links outside fenced and inline code; literal examples excluded.
links=[]
paths=set(T.rglob('*.md'))|set((R/'tracks/mz-constants/theory').glob('mz2d*.md'))|{R/x for x in ['PROOF_STATUS.md','state/IDEAS.md','ID_CROSSWALK.md']}
for path in sorted(paths):
 lines=[];fence=None
 for line in path.read_text().splitlines():
  m=re.match(r'^\s*(`{3,}|~{3,})',line)
  if m:
   if fence is None:fence=m.group(1)[0]
   elif m.group(1)[0]==fence:fence=None
   continue
  if fence is None:lines.append(line)
 content=re.sub(r'(`+).*?\1','', '\n'.join(lines),flags=re.S)
 for raw in re.findall(r'\[[^\]]*\]\(([^)]+)\)',content):
  target=raw.split('#',1)[0].split(' ',1)[0].strip('<>')
  if not target or re.match(r'[A-Za-z][A-Za-z0-9+.-]*:',target):continue
  require((path.parent/urllib.parse.unquote(target)).exists(),('broken link',str(path),target));links.append({'path':str(path),'target':target})
# Conservative generated-output check: all JSON/compressed output plus audit logs.
files=[]
for p in T.rglob('*'):
 if p.is_file() and '__pycache__' not in p.parts and (p.suffix in ['.json','.gz','.xz','.zip','.log']): files.append(info(p,p.read_bytes()))
require(max(x['bytes'] for x in files)<=1000000,'1MB generated file limit')
require(sum(x['bytes'] for x in files)<5000000,'5MB generated total limit')
newpaths=git('ls-files','--others','--exclude-standard').decode().splitlines()
for p in newpaths:
 require(p.startswith(str(P/PREFIX)) or p.startswith(str(T/'response-work/') ) or p in [str(T/'response-01.md'),str(T/'readiness-plan-01.md')],('unlisted new path',p))
result={'status':'PASS','executed_at_utc':now,'command':'python3 '+str(P/(PREFIX+'validate.py')),'script':info(P/(PREFIX+'validate.py'),(P/(PREFIX+'validate.py')).read_bytes()),'environment':{'python':sys.version,'platform':platform.platform()},'response_baseline':BASE,'rules_sha':BASE,'reservation_receipt':PREFIX+'reservation-recheck.json','scientific_reruns':[],'scientific_scope':'No scientific rerun performed for this documentation response. Scientific checkers/evidence and accepted audit unchanged; this script checks bytes/registration only.','F1_proof_sections_1_to_3':{'bytes':len(proof),'sha256':sha(proof),'entire_proof_to_EOF_unchanged':True},'F3':'KEEP prior PD-T028 frozen; all 73 old MZ inputs unchanged','old_MZ_inputs':oldobjects,'immutable_baseline_files':protected,'allowed_response_differences':changes,'proof_rows':proofrows,'F5_appended_obstruction_rows':10,'local_markdown_links_checked':len(links),'generated_plus_logs_size':{'file_count':len(files),'total_bytes':sum(x['bytes'] for x in files),'largest_bytes':max(x['bytes'] for x in files)},'new_paths':newpaths,'new_document_inputs':[info(x,R.joinpath(x).read_bytes()) for x in newpaths if pathlib.Path(x).suffix=='.md'],'limitations':'Point-in-time pinned-head check; no primary-source network reread and no scientific rerun. Root handles publication/handoff transition separately.'}
# Include this receipt itself at its final serialized size (not a prior run's bytes).
receipt_path=P/(PREFIX+'validation.json')
other_generated=[x for x in files if x['path']!=str(receipt_path)]
for _ in range(10):
 size=len((json.dumps(result,indent=2,ensure_ascii=False)+'\n').encode())
 sizes={'file_count':len(other_generated)+1,'total_bytes':sum(x['bytes'] for x in other_generated)+size,'largest_bytes':max([size]+[x['bytes'] for x in other_generated])}
 if result['generated_plus_logs_size']==sizes: break
 result['generated_plus_logs_size']=sizes
else: raise AssertionError('Receipt size did not stabilize')
require(sizes['largest_bytes']<=1000000 and sizes['total_bytes']<5000000,'Final receipt size limit')
save('validation',result)
print(json.dumps({'status':result['status'],'links':len(links),'protected_baseline_files':len(protected),'old_MZ_inputs':len(oldobjects),'changed_files':[x['path'] for x in changes],'generated_bytes':result['generated_plus_logs_size']['total_bytes']}))
