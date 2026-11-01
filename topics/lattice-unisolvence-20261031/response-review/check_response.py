#!/usr/bin/env python3
"""Independent read-only registry preservation check; no mathematical reruns."""
import collections,hashlib,json,pathlib,re,subprocess
R=pathlib.Path(__file__).resolve().parents[3]
MAIN='07c5f5465d6de306aa81dbe8ca1f615295163864'
TOPIC='3f369611f364c8bab41b8a48f1414f88b21937ec'
def git(*args):return subprocess.check_output(['git',*args],cwd=R,text=True)
def old(rev,p):return git('show',rev+':'+p)
def sha(p):return hashlib.sha256((R/p).read_bytes()).hexdigest()
result={'main':MAIN,'topic_before_response':TOPIC,'head':git('rev-parse','HEAD').strip(),'checks':{}}
checks=result['checks']
for prefix in ['tracks/unisolvence','topics/charter-unisolvence-20261031','tracks/mz-constants','topics/mz-constants']:
 checks[prefix+'_changed_from_main']=git('diff','--name-only',MAIN,'--',prefix).splitlines()
def status_rows(s):
 out={}
 for l in s.splitlines():
  if re.match(r'^\| PD-[TN](?:\d|\?lattice)',l):
   c=[x.strip() for x in l.split('|')];key=c[1]
   if key in out:raise AssertionError('duplicate '+key)
   out[key]={'status':c[3],'row':l,'disposition':c[5]}
 return out
cur=status_rows((R/'PROOF_STATUS.md').read_text())
expected={**status_rows(old(MAIN,'PROOF_STATUS.md')),**{k:v for k,v in status_rows(old(TOPIC,'PROOF_STATUS.md')).items() if '?lattice' in k}}
checks['result_rows_expected']=len(expected)
checks['result_status_missing_or_changed']=[k for k,v in expected.items() if k not in cur or cur[k]['status']!=v['status']]
checks['accepted_final_result_row_changes']=[k for k,v in expected.items() if '?lattice' not in k and (k not in cur or cur[k]['row']!=v['row'])]
for p in ['ID_CROSSWALK.md','state/IDEAS.md','literature/INDEX.md']:
 before=old(MAIN,p).splitlines();now=(R/p).read_text().splitlines()
 rows=[l for l in before if l.startswith('|') and re.search(r'(PD-[TN]\d{3}|IDEA-\d{3}|LIT-\d{3})',l)]
 checks[p+'_accepted_rows_missing_or_changed']=[l for l in rows if l not in now]
mp=json.loads((R/'topics/lattice-unisolvence-20261031/provisional-id-map.json').read_text())['rows']
checks['provisional_count']=len(mp)
for p in ['ID_CROSSWALK.md','topics/padua-batch-20261031/ALLOCATIONS.md']:
 checks[p+'_missing_provisionals']=[x['id'] for x in mp if x['id'] not in (R/p).read_text()]
ideas=[l for l in (R/'state/IDEAS.md').read_text().splitlines() if l.startswith('| IDEA?lattice')]
summaries=[l.split('|')[2].strip() for l in ideas]
checks['idea_family_count']=len(ideas);checks['distinct_idea_summaries']=len(set(summaries));checks['idea_rows_without_kill']=[l for l in ideas if 'kill' not in l.lower()]
paths=git('diff','--name-only',TOPIC).splitlines()
result['target_hashes']=[{'path':p,'sha256':sha(p),'bytes':(R/p).stat().st_size} for p in paths if (R/p).is_file() and '/response-review/' not in p]
print(json.dumps(result,indent=2))
