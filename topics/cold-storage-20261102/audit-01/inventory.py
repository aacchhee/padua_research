import collections, hashlib, json, pathlib, re, subprocess
# Run from the repository root at the audited candidate (see audit-01.md).
R=pathlib.Path.cwd(); BASE='2b52b432fe59c9a50aef9deebe5152c5d6874465'
def git(*a): return subprocess.check_output(['git','-C',str(R),*a])
assert git('rev-parse','HEAD').decode().strip() == '1d90af5d58fca87f240a04c18c427e8f59e2d6b8', 'Use a checkout of the audited candidate'
manifests=sorted(R.glob('**/cold-storage.json')); entries=[]; reports=[]
for p in manifests:
 m=json.loads(p.read_text()); entries.extend(m['entries'])
 for e in m['entries']:
  b=git('show',BASE+':'+e['path'])
  assert hashlib.sha256(b).hexdigest()==e['sha256'] and len(b)==e['bytes']
  assert git('rev-parse',m['source_commit']+':'+e['path']).decode().strip()==e['git_blob']
 assert sum(e['bytes'] for e in m['entries'])==m['total_bytes']
 run=subprocess.run(['python','tools/cold_storage.py','verify',m['slug']],cwd=R,capture_output=True,text=True)
 assert run.returncode==0,run.stderr+run.stdout
 reports.append(json.loads(run.stdout))
deleted=git('diff','--diff-filter=D','--name-only',BASE,'HEAD').decode().splitlines()
c=collections.Counter(e['path'] for e in entries)
assert set(deleted)==set(c) and all(v==1 for v in c.values())
changed=git('diff','--diff-filter=M','--name-only',BASE,'HEAD').decode().splitlines()
md=[]; append=[]; other=[]; redirects=[]
pat=re.compile(r'(!?\[[^\]\n]*\])\(([^)\n]*)\)')
def normal(s): return pat.sub(lambda m:m[1]+'(TARGET)',s)
for p in changed:
 old=git('show',BASE+':'+p).decode(); new=(R/p).read_text()
 if p.endswith('COLD_STORAGE.md'):
  # Prior text may itself have link redirects.
  assert normal(new).startswith(normal(old)),p
  append.append(p)
 elif p.endswith('.md') and p!='agents/WORKFLOW.md':
  assert normal(old)==normal(new),p
  md.append(p)
 else: other.append(p)
 a=pat.findall(old); b=pat.findall(new)
 # only compare equal-position links for files with target-only edits
 if p in md:
  assert len(a)==len(b)
  for x,y in zip(a,b):
   if x!=y: redirects.append({'file':p,'old':x[1],'new':y[1]})
def tree(ref):
 ans={}
 for row in git('ls-tree','-rl','-z',ref).split(b'\0'):
  if not row: continue
  meta,path=row.split(b'\t',1); ans[path.decode()]=int(meta.split()[3])
 return ans
extensions={'md','py','sh','tex','bib','svg','gitignore'}
def generated(d): return {p:n for p,n in d.items() if p.rsplit('.',1)[-1] not in extensions}
before=generated(tree(BASE));after=generated(tree('HEAD'))
large={p:n for p,n in after.items() if n>=16384 and not pathlib.Path(p).name.lower().startswith('cold-storage')}
assert not large,large
result={'base':BASE,'audited_head':git('rev-parse','HEAD').decode().strip(),'deleted_files':len(deleted),'unique_entries':len(entries),'deleted_bytes':sum(e['bytes'] for e in entries),'all_source_blob_sha_size_checks':True,'generated_before':sum(before.values()),'generated_after':sum(after.values()),'remaining_large_nonmanifests':large,'target_only_modified_files':len(md),'target_changes_non_cold_docs':len(redirects),'prior_cold_docs_preserved_modulo_targets':append,'other_modified_files':other,'verify':reports}
pathlib.Path('/tmp/cold-audit-inventory.json').write_text(json.dumps(result,indent=2)+'\n')
pathlib.Path('/tmp/cold-audit-redirects.json').write_text(json.dumps(redirects,indent=2)+'\n')
print(json.dumps(result,indent=2))
