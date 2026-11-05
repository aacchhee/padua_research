#!/usr/bin/env python3
"""Root-only disposable squash rehearsals; never checkout/push main or a topic."""
import argparse,json,re,subprocess,tempfile
from pathlib import Path
REPO=Path(__file__).resolve().parents[3]
R=Path(__file__).resolve().parents[1]
def command(cwd,*args,check=True):
 p=subprocess.run(['git','-C',str(cwd),*args],capture_output=True,text=True)
 if check and p.returncode:raise RuntimeError(p.stderr+p.stdout)
 return p
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--candidate',required=True);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args()
 scan=json.loads((R/'preparation/allocation-scan.json').read_text());heads=scan['heads'];main_sha=heads['main'];heads['PR23']=a.candidate
 sequences=[['PR23'],['PR21','PR23'],['PR22','PR23'],['PR24','PR23'],['PR23','PR21'],['PR23','PR22'],['PR23','PR24'],['PR23','PR21','PR22','PR24'],['PR21','PR22','PR23','PR24']]
 old_rows=command(REPO,'show',main_sha+':PROOF_STATUS.md').stdout
 ids=set(re.findall(r'^\| (PD-[TN]\d{3})(?:\s|\()',old_rows,re.M))
 old_sections=set(re.findall(r'^## (.+)$',command(REPO,'show',main_sha+':RESULTS.md').stdout,re.M))
 records=json.loads((R/'preparation/final-id-map.json').read_text())['records']
 out={'main':main_sha,'candidate':a.candidate,'foreign_heads':{k:v for k,v in heads.items() if k not in ('main','PR23')},'scope':'Actual local sequential squash rehearsals in unique disposable detached worktrees. Alternative orders are compatibility screens, not an AC merge-order instruction. Foreign PRs are draft/unprepared; no readiness is inferred for them. No live merge, main/topic mutation, force-push or tag.','scenarios':[]}
 for seq in sequences:
  parent=Path(tempfile.mkdtemp(prefix='padua-mz-rehearsal-'));tree=parent/'tree';scenario={'order':seq,'steps':[]}
  command(REPO,'worktree','add','--detach',str(tree),main_sha)
  try:
   for label in seq:
    p=command(tree,'merge','--squash','--no-commit',heads[label],check=False)
    conflicts=command(tree,'diff','--name-only','--diff-filter=U').stdout.splitlines()
    step={'source':label,'head':heads[label],'exit_code':p.returncode,'conflicts':conflicts};scenario['steps'].append(step)
    if p.returncode:scenario['result']='CONFLICT';break
    t=command(tree,'write-tree').stdout.strip();step['tree']=t
    if label=='PR23':
     after=(tree/'PROOF_STATUS.md').read_text();assert ids<=set(re.findall(r'^\| (PD-[TN]\d{3})(?:\s|\()',after,re.M))
     assert old_sections<=set(re.findall(r'^## (.+)$',(tree/'RESULTS.md').read_text(),re.M))
     for rec in records:
      path='topics/'+R.name+'/'+rec['path'];assert (tree/path).read_bytes()==subprocess.check_output(['git','-C',str(REPO),'show',a.candidate+':'+path])
     step['preserves_main_ids_and_sections']=True;step['registered_record_bytes_match_candidate']=True
     if len(seq)==1:step['equals_candidate_tree']=t==command(REPO,'rev-parse',a.candidate+'^{tree}').stdout.strip();assert step['equals_candidate_tree']
    command(tree,'-c','user.name=Andrey Chesnokov','-c','user.email=aacchhee@gmail.com','commit','--allow-empty','-m','test: disposable squash compatibility rehearsal')
   else:scenario['result']='CLEAN'
  finally:
   command(REPO,'worktree','remove','--force',str(tree));parent.rmdir()
  out['scenarios'].append(scenario)
 a.output.write_text(json.dumps(out,separators=(',',':'))+'\n')
 print(json.dumps([{'order':x['order'],'result':x['result'],'conflicts':[p for s in x['steps'] for p in s['conflicts']]} for x in out['scenarios']],indent=1))
if __name__=='__main__':main()
