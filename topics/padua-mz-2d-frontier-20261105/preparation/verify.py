#!/usr/bin/env python3
"""Read-only mechanical registration/impact checks; not a mathematical rerun."""
import hashlib,json,re,subprocess
from pathlib import Path
REPO=Path(__file__).resolve().parents[3]
R=Path(__file__).resolve().parents[1]
BASE='7a8d8dd313b5370589810f4efd910ed65744f865'
def git(*args):return subprocess.check_output(['git','-C',str(REPO),*args])
def previous(path,ref=BASE):return git('show',ref+':'+str(path.relative_to(REPO))).decode()
def digest(b):return hashlib.sha256(b).hexdigest()
def main():
 m=json.loads((R/'preparation/final-id-map.json').read_text())
 mapping={x['provisional']:x['final'] for x in m['records']+m['ideas']}
 mapping.update({'PD-N?...-13':'PD-N105','PD-N?...-14':'PD-N106','PD-T?...-12':'PD-T295','PD-T…12':'PD-T295','PD-N…13':'PD-N105','PD-N…14':'PD-N106','PD-N…f3-01':'PD-N107','PD-T…f3-01':'PD-T296','PD-T…f4-01':'PD-T297','PD-N…10':'PD-N104','PD-T…11':'PD-T294','PD-T…90/91':'PD-T298/299'})
 def canon(s):
  for a,b in sorted(mapping.items(),key=lambda x:-len(x[0])):s=s.replace(a,b)
  return s
 def proof(s):
  a=re.search(r'^## Proof(?: or evidence)?$',s,re.M)
  if not a:return None
  end=re.search(r'^## (?:Scope|Checks and sources)',s[a.end():],re.M)
  return s[a.end():a.end()+end.start()] if end else s[a.end():]
 proof_hashes={}
 for x in m['records']:
  p=R/x['path'];s=p.read_text();assert s.startswith('# '+x['final']+' '),x
  assert x['provisional'] in s,x
  if x['final']=='PD-T300':continue
  prior=previous(p);assert canon(proof(prior))==proof(s),x
  proof_hashes[x['final']]=digest(proof(s).encode())
 # Protect every existing scientific source, receipt, independent/auditor record.
 protected=[]
 for path in git('ls-tree','-r','--name-only',BASE).decode().splitlines():
  if not path.startswith(str(R.relative_to(REPO))+'/'):continue
  relative=path.split(R.name+'/',1)[1]
  check=relative.startswith(('code/','evidence/','audit-01-support/','independent-checks')) or relative=='audit-01.md'
  if relative=='code/evidence_manifest.py':check=False
  if check:
   assert (REPO/path).read_bytes()==git('show',BASE+':'+path),path
   protected.append(path)
 # Inherited canonical theory originals survive as exact suffix after dated addenda.
 for f in ['open-padua-target.md','mz2d-upper-open.md','mz2d-fixed-ratio.md','mz2d-hyperinterpolation-uniform-open.md']:
  p=REPO/'tracks/mz-constants/theory'/f;prior=previous(p,'origin/main');now=p.read_text();assert now.splitlines()[0]==prior.splitlines()[0];assert now.endswith(prior.split('\n',1)[1]),f
 # Registry changes only the four accepted existing targets, plus eleven new records.
 registry=(REPO/'PROOF_STATUS.md').read_text();old_registry=previous(REPO/'PROOF_STATUS.md','origin/main')
 def rows(s):return {re.match(r'^\| (PD-[TN]\d{3})(?:\s|\()',l).group(1):l for l in s.splitlines() if re.match(r'^\| (PD-[TN]\d{3})(?:\s|\()',l)}
 old,new=rows(old_registry),rows(registry);targets={'PD-T028','PD-T110','PD-T114','PD-T116'}
 for key,row in old.items():
  if key not in targets:assert new[key]==row,key
 assert set(new)-set(old)=={x['final'] for x in m['records']}
 for key in ['PD-T028','PD-T110','PD-T116']:
  assert new[key].split('|')[3].strip()=='OPEN' and 'REJECTED: refuted' in new[key],key
 assert new['PD-T114'].split('|')[3].strip()=='PROVED'
 for x in m['records']:assert new[x['final']].split('|')[3].strip()==x['status'],x
 # New IDs stay in own permanent reservation and do not alter any prior assignment.
 assert len({x['final'] for x in m['records']+m['ideas']})==25
 for x in m['records']+m['ideas']:
  ns='IDEA' if x['final'].startswith('IDEA') else x['final'][:4]
  n=int(re.search(r'(\d+)$',x['final']).group(1));low,high={'PD-T':(294,323),'PD-N':(104,115),'IDEA':(384,413)}[ns];assert low<=n<=high
 for x in m['ideas']:assert x['provisional'] in '\n'.join(p.read_text() for p in R.glob('ideas-*.md'))
 # Finite measurement transcription is constrained by the unchanged original receipts.
 screen=json.loads((R/'evidence/g1-screen.json').read_text());assert screen['completed_rows']==476 and not screen['threshold_hits']
 assert all(v['m_values']==list(range(2,240)) for v in screen['coverage_by_offset'].values())
 minima=json.loads((R/'evidence/g1-minimum-only.json').read_text())['results'];assert [x['m'] for x in minima]==[800,1000,1200,1600] and minima[-1]['minimum']<0
 assert 'MEASURED' in (R/'theory/frontier-measurements.md').read_text() and 'uncertified' in (R/'theory/frontier-measurements.md').read_text()
 # Only own RESULTS section may change; root/dedicated path conversion is explicit.
 source=(REPO/'results'/f'{R.name}.md').read_text();results=(REPO/'RESULTS.md').read_text();old_results=previous(REPO/'RESULTS.md','origin/main');assert results.startswith(old_results)
 own='## '+R.name+'\n\n'+'\n'.join(source.splitlines()[2:]).replace('../topics/','topics/')+'\n';assert results[len(old_results):].strip()==own.strip()
 # Check changed/new source links; retain historical preexisting broken links as a separate list.
 paths=set(git('diff','--name-only','origin/main').decode().splitlines())|{str(p.relative_to(REPO)) for p in R.rglob('*.md') if not any(x in p.parts for x in ['audit-01-support','handoffs'])}
 broken=[]
 for relative in paths:
  p=REPO/relative
  if not p.is_file() or p.suffix!='.md' or 'audit-01-support' in p.parts or 'handoffs' in p.parts:continue
  s=re.sub(r'```.*?```','',p.read_text(),flags=re.S)
  for t in re.findall(r'\]\(([^)]+)\)',s):
   if '://' in t or t.startswith('#') or '<' in t:continue
   target=t.split('#')[0]
   if target and not (p.parent/target).exists():broken.append((relative,t))
 assert not broken,broken
 for p in R.rglob('*.json'):json.loads(p.read_text());assert p.stat().st_size<=16384,p
 allowed=['PROOF_STATUS.md','state/IDEAS.md','state/CURRENT.md','PAPER_MAP.md','topics/README.md','ID_CROSSWALK.md','RESULTS.md','topics/padua-batch-20261031/ALLOCATIONS.md','tracks/mz-constants/README.md']
 allowed+=['tracks/mz-constants/theory/'+f for f in ['open-padua-target.md','mz2d-upper-open.md','mz2d-fixed-ratio.md','mz2d-hyperinterpolation-uniform-open.md']]
 for p in git('diff','--name-only','origin/main').decode().splitlines():assert p.startswith(str(R.relative_to(REPO))+'/') or p=='results/'+R.name+'.md' or p in allowed,p
 assert not git('diff','origin/main','--name-only','--','.github/','AGENTS.md','agents/')
 print(json.dumps({'protected_paths':len(protected),'unchanged_other_registry_rows':len(old)-4,'registered_results':len(m['records']),'ideas':len(m['ideas']),'normalized_proof_hashes':proof_hashes,'links':'PASS','finite_scope':'PASS','AC_status_cells':'PASS','scope':'PASS'},indent=1))
if __name__=='__main__':main()
