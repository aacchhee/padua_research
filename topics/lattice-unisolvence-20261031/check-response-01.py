#!/usr/bin/env python3
"""Check registry union and unchanged mathematics after audit-01 metadata response."""
import argparse, hashlib, json, re, subprocess
from pathlib import Path

MAIN='07c5f5465d6de306aa81dbe8ca1f615295163864'
TOPIC='3f369611f364c8bab41b8a48f1414f88b21937ec'
SHARED={'ID_CROSSWALK.md','PAPER_MAP.md','PROOF_STATUS.md','literature/INDEX.md','state/CURRENT.md','state/IDEAS.md','topics/README.md','topics/padua-batch-20261031/ALLOCATIONS.md','tracks/README.md'}
MARKER='\n\n## Audit history addendum — 2026-11-01\n\n'

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[2]);p.add_argument('--output',type=Path);a=p.parse_args();root=a.root.resolve();fail=[]
 def git(*args):return subprocess.check_output(['git',*args],cwd=root)
 def old(ref,path):return git('show',ref+':'+path)
 def check(ok,message):
  if not ok:fail.append(message)
 def rows(data):
  out={}
  for line in data.decode().splitlines():
   if re.match(r'^\| PD-[TN](?:\d+|\?lattice-)',line):
    cells=[x.strip() for x in line.split('|')[1:-1]];check(len(cells)==8,'result-table shape '+line[:60]);check(cells[0] not in out,'duplicate result '+cells[0]);out[cells[0]]=cells
  return out
 def normalize(cell):return cell.replace(', focused re-audit pending',', accepted in Claude audit-02').replace('; specialization awaits focused re-audit','; specialization accepted in Claude audit-02')
 current=rows((root/'PROOF_STATUS.md').read_bytes());m=rows(old(MAIN,'PROOF_STATUS.md'));t=rows(old(TOPIC,'PROOF_STATUS.md'))
 expected=m|{k:v for k,v in t.items() if '?' in k};check(set(current)==set(expected),'result union differs')
 for ident,cells in expected.items():check([normalize(x) for x in cells[:7]]==current.get(ident,[])[:7],'scientific/status/disposition cells changed '+ident)
 # No main file outside the explicitly reconciled shared metadata may change.
 protected=0
 for path in git('ls-tree','-r','--name-only',MAIN).decode().splitlines():
  if path not in SHARED:
   protected+=1;check((root/path).is_file() and (root/path).read_bytes()==old(MAIN,path),'main protected bytes '+path)
 # Lattice scientific prefixes, producer code, numerical outputs and auditor records.
 histories=0;topic_exact=0
 for path in git('ls-tree','-r','--name-only',TOPIC).decode().splitlines():
  if path.startswith('tracks/lattice-unisolvence/theory/') and path.endswith('.md'):
   live=(root/path).read_text();check(MARKER in live,'history receipt absent '+path);check(live.split(MARKER,1)[0]==old(TOPIC,path).decode().rstrip(),'mathematical prefix changed '+path);histories+=1
  elif path.startswith(('tracks/lattice-unisolvence/code/','topics/lattice-unisolvence-20261031/directions/','topics/lattice-unisolvence-20261031/independent/','topics/lattice-unisolvence-20261031/claude-audit/','literature/lattice-unisolvence/')) or path=='topics/lattice-unisolvence-20261031/audit-01.md':
   topic_exact+=1;check((root/path).read_bytes()==old(TOPIC,path),'frozen science/auditor bytes '+path)
 # Historical developer hashes remain valid at the audited source.
 historic=0
 for path in ['C0/hashes.txt','C1/hashes.txt','C3/checkpoint.sha256']:
  name='topics/lattice-unisolvence-20261031/directions/'+path
  for line in old(TOPIC,name).decode().splitlines():
   digest,target=line.split(None,1);target=target.strip().lstrip('*');check(hashlib.sha256(old(TOPIC,target)).hexdigest()==digest,'historical developer hash '+target);historic+=1
 # Keep all accepted literal index rows; only lattice audit/prose fields are modernized.
 for path in ['ID_CROSSWALK.md','literature/INDEX.md','state/IDEAS.md']:
  live=(root/path).read_text()
  for line in old(MAIN,path).decode().splitlines():
   if line.startswith('|'):check(line in live,'accepted index row missing '+path+' '+line[:70])
 mapping=json.loads((root/'topics/lattice-unisolvence-20261031/provisional-id-map.json').read_text())['rows'];ids=[r['id'] for r in mapping];check(len(set(ids))==66,'provisional map uniqueness')
 ledger=(root/'topics/padua-batch-20261031/ALLOCATIONS.md').read_text();cross=(root/'ID_CROSSWALK.md').read_text()
 for ident in ids:check(ident in ledger and ident in cross,'provisional reservation lost '+ident)
 reservation=old(MAIN,'topics/padua-batch-20261031/ALLOCATIONS.md').decode().split('## Final reservations',1)[1].split('## Members and integration responsibilities',1)[0];check(reservation in ledger,'accepted final reservation table changed');check('**Allocation owner: the root Codex MZ orchestrator.**' in ledger,'allocation authority changed')
 ideas=[]
 for line in (root/'state/IDEAS.md').read_text().splitlines():
  if line.startswith('| IDEA?lattice-'):
   cells=[x.strip() for x in line.split('|')[1:-1]];check(len(cells)==3,'IDEA table shape');check('Kill' in cells[1] or 'kill' in cells[1],'IDEA kill test absent');ideas.append(cells)
 check(len(ideas)==13 and len({x[1] for x in ideas})==13,'distinct IDEA summaries')
 handoff=(root/'topics/lattice-unisolvence-20261031/AUDIT_HANDOFF.md').read_text();check('OPENBLAS_NUM_THREADS=2 OMP_NUM_THREADS=2 MKL_NUM_THREADS=2 python tracks/lattice-unisolvence/code/c1_stability.py' in handoff,'F3 thread count')
 # Link checking only metadata changed by the response; historical generic <placeholders> are excluded.
 links=0
 files=list(root.glob('tracks/lattice-unisolvence/theory/*.md'))+[root/x for x in SHARED if x.endswith('.md')]+[root/'topics/lattice-unisolvence-20261031/response-01.md',root/'topics/lattice-unisolvence-20261031/COLD_STORAGE.md']
 for path in files:
  for target in re.findall(r'\]\(([^)]+)\)',path.read_text()):
   target=target.split('#',1)[0]
   if not target or re.match(r'[a-zA-Z]+:',target) or '<' in target:continue
   links+=1;check((path.parent/target).resolve().exists(),'broken link '+str(path.relative_to(root))+' '+target)
 result={'scope':'unchanged mathematics; metadata/registry union','topic_source':TOPIC,'main_source':MAIN,'protected_main_files':protected,'result_rows':len(current),'accepted_final_results':len(m),'lattice_results':len(current)-len(m),'theory_history_prefixes':histories,'unchanged_science_auditor_files':topic_exact,'historical_developer_hashes':historic,'provisional_ids':len(ids),'distinct_idea_summaries':len(ideas),'links_checked':links,'failures':fail,'passed':not fail}
 if a.output:
  a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result,sort_keys=True));return bool(fail)
if __name__=='__main__':raise SystemExit(main())
