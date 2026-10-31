#!/usr/bin/env python3
"""Protocol identity/reference check; no mathematical validation or numerical rerun."""
import hashlib,json,re,subprocess
from pathlib import Path
R=Path(__file__).resolve().parents[3]
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def git(*args): return subprocess.check_output(['git',*args],cwd=R).decode()
m=json.loads((R/'topics/mz-constants/final-id-map.json').read_text()); mapping=m['mappings']; findings=[]
assert len(mapping)==len(set(mapping.values()))==65
counts={k:sum(v.startswith(k) for v in mapping.values()) for k in ['PD-T','PD-N','IDEA-','LIT-']}
assert counts=={'PD-T':16,'PD-N':5,'IDEA-':25,'LIT-':19}
files=set()
for old,new in mapping.items():
 p=R/m['canonical'][old]['path']; files.add(p)
 assert re.search(r'^#{1,6} '+re.escape(new)+r'\b',p.read_text(),re.M),(new,str(p))
 assert old in (R/'ID_CROSSWALK.md').read_text(),old
ideas=(R/'state/IDEAS.md').read_text()
assert len(re.findall(r'^### IDEA-\d+',ideas,re.M))==25
status={}
for p in (R/'tracks/mz-constants/theory').glob('*.md'):
 t=p.read_text(); id=t.splitlines()[0].split()[1]; st=re.search(r'Overall status:\s*(?:\*\*)?(PROVED|OPEN|MEASURED|PARTIAL|CONDITIONAL)',t).group(1)
 status[id]=st
 assert re.search(r'^\| '+id+r' \|[^\n]*?\| '+st+r' \|',(R/'PROOF_STATUS.md').read_text(),re.M),id
# Verify full input locally; fresh clone requires the uploaded archive for four ignored text sources.
src=R/'topics/mz-constants/sources/padua_mz_inputs'; source_count=0
for line in (src/'SHA256SUMS.txt').read_text().splitlines():
 h,n=line.split('  ',1); assert sha(src/n)==h,n; source_count+=1
assert source_count==21
for name in ['reproduction.json','astra-reproduction.json']:
 data=json.loads((R/'tracks/mz-constants/evidence'/name).read_text())
 assert data['runner_sha256']==sha(R/'tracks/mz-constants/code/reproduce.py')
 for name,h in data['source_sha256'].items(): assert sha(src/'code'/name)==h,name
impact=json.loads((R/'topics/mz-constants/allocation-impact.json').read_text()); changes={x['path']:x for x in impact['changes']}
manifest_results=[]
for name,keys in [('reproduction-manifest.json',['artifacts']),('astra-manifest.json',['audited_inputs','auditor_artifacts'])]:
 data=json.loads((R/'tracks/mz-constants/evidence'/name).read_text())
 for key in keys:
  for a in data[key]:
   p=R/a['path']; current=sha(p); result='current' if current==a['sha256'] and p.stat().st_size==a['bytes'] else 'historical'
   if result=='historical':
    c=changes.get(a['path']); bridged=bool(c and c['before_sha256']==a['sha256'] and c['after_sha256']==current)
    result='allocation-bridged' if bridged else 'changed-needs-impact-record'
   manifest_results.append({'manifest':name,'path':a['path'],'result':result})
tracked=[R/x for x in git('ls-files').splitlines() if (R/x).is_file()]
assert not [str(p) for p in tracked if p.suffix.lower()=='.pdf']
assert not [str(p) for p in tracked if '/sources/padua_mz_inputs/notes/' in str(p) or '/sources/padua_mz_inputs/reports/' in str(p)]
# Conservative bound: all tracked repository bytes plus untracked nonignored files, not merely generated outputs.
public=set(tracked)|{R/x for x in git('ls-files','--others','--exclude-standard').splitlines() if (R/x).is_file()}
assert max(p.stat().st_size for p in public)<1_000_000
assert sum(p.stat().st_size for p in public)<5_000_000
# Local Markdown links; remote URLs and anchors are excluded, not resolved or fetched.
scan=set(files)|{R/x for x in ['ID_CROSSWALK.md','PROOF_STATUS.md','state/CURRENT.md','state/IDEAS.md','literature/INDEX.md','PAPER_MAP.md']}
scan.update((R/'topics/mz-constants').glob('*.md')); scan.update((R/'tracks/mz-constants').glob('*.md'))
scan.update((R/'tracks/mz-constants/paper').glob('*'))
scan.update((R/'topics/padua-batch-20261031').glob('*.md'))
scan.discard(R/'topics/mz-constants/independent-protocol-01.md')
broken=[]
for p in scan:
 if not p.exists():continue
 for link in re.findall(r'\]\(([^)]+)\)',p.read_text()):
  link=link.split('#')[0]
  if not link or '://' in link or link.startswith('mailto:'):continue
  if not (p.parent/link).exists():broken.append({'file':str(p.relative_to(R)),'target':link})
result={'head':git('rev-parse','HEAD').strip(),'checker_sha256':sha(Path(__file__).resolve()),'counts':counts,'status_counts':{s:list(status.values()).count(s) for s in sorted(set(status.values()))},'source_manifest_sha256':sha(src/'SHA256SUMS.txt'),'source_entries_verified':source_count,'public_files':len(public),'public_bytes_conservative':sum(p.stat().st_size for p in public),'max_public_file_bytes':max(p.stat().st_size for p in public),'manifest_checks':manifest_results,'broken_local_links':broken,'pinned_inputs':[{'path':str(p.relative_to(R)),'sha256':sha(p),'bytes':p.stat().st_size} for p in sorted(public) if p.exists() and p.name not in ['protocol-check.json','independent-protocol-01.md']]}
print(json.dumps(result,indent=2))
