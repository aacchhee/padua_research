#!/usr/bin/env python3
"""Pinned, read-only Git preservation checks. No mathematical execution or Git writes."""
import collections, difflib, hashlib, json, pathlib, re, subprocess
ROOT=pathlib.Path(__file__).resolve().parents[3]
SOURCE='37820a528c863e5cfe2dc2f1f8879b4fd40cf210'
BASE='f4e213390f66a8c9f0c6bd65131b97b78db873c8'
MAIN='21e620ba8b5f0e0706f3a8c6613517df04d9d469'
ALLOCATION='6954664fc0906b7e5c8ff0f1804b077bd3b5861f'
MERGE='3e0100f1a339c3f63dcb638785917400089a31a6'
T='topics/programme-ideas-20261031/'
def git(*args): return subprocess.check_output(['git',*args],cwd=ROOT).decode()
def old(rev,path): return git('show',rev+':'+path)
def files(rev): return git('ls-tree','-r','--name-only',rev).splitlines()
def diff(a,b,*paths): return git('diff','--name-only',a,b,'--',*paths).splitlines()
def identity(rev,path):
 s=old(rev,path).encode();return {'git_blob':git('rev-parse',rev+':'+path).strip(),'sha256':hashlib.sha256(s).hexdigest(),'bytes':len(s)}
fail=[]
def check(ok,msg):
 if not ok: fail.append(msg)
out={'scope':'Integration preservation only; accepted mathematics not reopened; no full mathematical tests executed. Novelty gate not applicable: no novelty-bearing content is proposed or assessed.','source':SOURCE,'rules_read':SOURCE,'baseline':BASE,'main':MAIN,'allocation':ALLOCATION,'merge':MERGE,'checks':{}}
checks=out['checks'];sourcefiles=files(SOURCE)
pat=r"Final ID: \*\*([^*]+)\*\* \(allocated 2026-11-01 under AC's authorisation; the provisional ID above and in the text is retained as provenance — see ID_CROSSWALK.md\).\n\n"
pd=[p for p in sourcefiles if p.startswith(('tracks/lattice-unisolvence/theory/',T+'theory/')) and p.endswith('.md')]
ideas=['topics/lattice-unisolvence-20261031/directions/'+x+'/candidates.md' for x in ('C0','C1','C3')]+[T+'ideas/candidates.md']
checks['canonical_allocation']=[]
for p in pd+ideas:
 after=old(ALLOCATION,p);before=old(ALLOCATION+'^',p);norm,n=re.subn(pat,'',after)
 ids=re.findall(pat,after);equal=norm==before and after==old(SOURCE,p)
 check(equal,'allocation adds more than Final ID provenance: '+p)
 checks['canonical_allocation'].append({'path':p,'final_ids':ids,'count':n,'existing_bytes_preserved':equal,'before':identity(ALLOCATION+'^',p),'after':identity(SOURCE,p)})
check(len(pd)==32,'PD count');check(sum(x['count'] for x in checks['canonical_allocation'] if x['path'] in ideas)==33,'IDEA count')
protected=[p for p in files(BASE) if p=='AGENTS.md' or p.startswith('agents/') or p in [T+'audit-01.md',T+'audit-02.md',T+'audit-03.md'] or p.startswith(tuple(T+x for x in ('audit-support/','audit-02-support/','audit-03-support/','checks/code/')))]
checks['baseline_protected']={'count':len(protected),'differences':[p for p in protected if old(BASE,p)!=old(SOURCE,p)],'paths':protected}
check(not checks['baseline_protected']['differences'],'protected baseline content changed')
checks['rules_diff_from_main']=diff(MAIN,SOURCE,'AGENTS.md','agents')
check(checks['rules_diff_from_main']==['agents/WORKFLOW.md','agents/claude/CLAUDE_ROLES.md'],'unexpected rules changes relative main')
checks['baseline_nonallocation_theory_diffs']=[]
for p in pd+ideas:
 norm=re.sub(pat,'',old(SOURCE,p));before=old(BASE,p)
 if before!=norm:
  checks['baseline_nonallocation_theory_diffs'].append({'path':p,'diff':''.join(difflib.unified_diff(before.splitlines(True),norm.splitlines(True)))})
check([x['path'] for x in checks['baseline_nonallocation_theory_diffs']]==[T+'theory/programme-ideas-claude-01-finite-favard-pattern-pairs.md'],'unexpected post-audit canonical edits beyond disclosed gauge wording')
regs=['ID_CROSSWALK.md','PROOF_STATUS.md','literature/CORPUS.md','literature/INDEX.md','state/IDEAS.md']
checks['main_merge_registry_preservation']={}
for p in regs:
 a=old(MAIN,p).splitlines();b=old(MERGE,p).splitlines();missing=list((collections.Counter(a)-collections.Counter(b)).elements())
 # Stricter than set containment: full original line sequence must remain a subsequence.
 it=iter(b);ordered=all(any(v==w for w in it) for v in a)
 checks['main_merge_registry_preservation'][p]={'original_lines':len(a),'missing_lines':missing,'original_order_preserved':ordered}
 check(not missing and ordered,'main registry lost/reordered lines: '+p)
p='literature/CORPUS.md';branch=old(MERGE+'^1',p).splitlines();merged=old(MERGE,p).splitlines();main=old(MAIN,p).splitlines();missing=[x for x in branch if x.startswith('|') and x not in merged]
def key(row):return row.split('|')[1].strip()
replacement={key(x):x for x in main if x.startswith('|')}
checks['corpus_removed_branch_rows']=[{'key':key(x),'old':x,'replacement_from_main':replacement.get(key(x))} for x in missing]
checks['corpus_removed_branch_nonrows']=[x for x in branch if x and not x.startswith('|') and x not in merged]
check(len(missing)==49,'expected 15 rewritten + 34 duplicate branch CORPUS rows')
check(all(key(x) in replacement for x in missing),'CORPUS row lacks main replacement')
checks['inherited_main_changes']={}
for prefix in ['topics/bivariate-lanczos-20261031/','tracks/bivariate-lanczos/']:
 checks['inherited_main_changes'][prefix]={'baseline_to_source_count':len(diff(BASE,SOURCE,prefix)),'main_to_source_changes':diff(MAIN,SOURCE,prefix)}
 check(not checks['inherited_main_changes'][prefix]['main_to_source_changes'],'inherited main Lanczos subtree mutated')
hist=['topics/lattice-unisolvence-20261031/'+p for p in ['check-response-01.py','response-review/check_response.py','response-01-checks.json','response-review/final-snapshot.json','response-review/report.md']]
checks['historical_checker_receipts']=[{'path':p,'unchanged_from_baseline':old(BASE,p)==old(SOURCE,p),'identity':identity(SOURCE,p)} for p in hist]
check(all(x['unchanged_from_baseline'] for x in checks['historical_checker_receipts']),'historical receipt changed')
checks['historical_checker_current_head_caveat']=next(l for l in old(SOURCE,T+'pr-prep.md').splitlines() if l.startswith('- **Expected effect:**'))
check('will not pass at this head' in checks['historical_checker_current_head_caveat'],'missing current-head caveat')
out['failures']=fail;out['passed']=not fail
print(json.dumps(out,indent=2,ensure_ascii=False))
raise SystemExit(bool(fail))
