"""Read-only registry-preservation check; run from repository root, prints JSON.

Checks only the authorized integration against pinned main and accepted PR9
input. Does not regenerate historical evidence or mutate scientific files.
"""
from pathlib import Path
import collections, hashlib, json, re, subprocess, urllib.parse
BASE='cf89b140530d5838bdb208a8c28f3e7aa676ace3'
INPUT='93da3be26dbddf9ec2446af578fe8015bb4eeada'
TOPIC=Path('topics/padua-proof-attempts-20261101')
def git(*args):return subprocess.check_output(['git',*args])
def old(path,ref=BASE):return git('show',f'{ref}:{path}')
def digest(b):return hashlib.sha256(b).hexdigest()
report={'base':BASE,'accepted_response_input':INPUT,'rules_read_at':git('rev-parse','2c192c7').decode().strip(),'checks':{}}
# Every previously tracked file outside topic stays byte-identical except the
# explicit source/registry integration list. Detect accidental loss anywhere.
allowed={'PROOF_STATUS.md','ID_CROSSWALK.md','state/IDEAS.md','state/CURRENT.md','PAPER_MAP.md','topics/padua-batch-20261031/ALLOCATIONS.md','topics/programme-ideas-20261031/OPEN_TARGETS.md'}
allowed.update(x['path'] for x in json.loads((TOPIC/'finalization/applied-replacements.json').read_text())['replacements'])
unchanged=[]
for name in git('ls-tree','-r','--name-only',BASE).decode().splitlines():
 if name in allowed:continue
 assert Path(name).is_file(),('missing existing file',name)
 assert Path(name).read_bytes()==old(name),('unrelated change',name)
 unchanged.append(name)
report['checks']['unrelated_main_files_byte_identical']=len(unchanged)
# All historical rows survive; only three explicitly named rows per registry
# may gain current evidence. Their ID, claim and epistemic status are retained.
rowsets={
 'PROOF_STATUS.md':(3,{'PD-T098','PD-T100','PD-N042'}),
 'ID_CROSSWALK.md':(4,{'PD-T?programme-ideas-claude-04','PD-T?programme-ideas-claude-06','PD-N?programme-ideas-claude-04'}),
 'state/IDEAS.md':(2,{'IDEA-197','IDEA-206','[PD-N042]'}),
}
rowreport={}
for name,(prefixcells,changed) in rowsets.items():
 before=old(name).decode().splitlines();after=Path(name).read_text().splitlines();seen=[];preserved=0
 for line in before:
  if not line.startswith('|'):continue
  key=next((x for x in changed if line.startswith('| '+x)),None)
  if key:
   matches=[x for x in after if x.startswith('| '+key)]
   assert len(matches)==1,(name,key)
   assert line.split('|')[1:prefixcells+1]==matches[0].split('|')[1:prefixcells+1],(name,key,'changed identity/claim/status')
   seen.append(key)
  else:assert line in after,(name,'lost row',line);preserved+=1
 assert set(seen)==changed,(name,seen)
 # No deletion of non-table prose: existing prefixes and history stay intact.
 before_prose=[x for x in before if not x.startswith('|')]
 it=iter(x for x in after if not x.startswith('|'))
 assert all(any(y==x for y in it) for x in before_prose),(name,'lost prose')
 rowreport[name]={'untouched_rows':preserved,'updated_rows':sorted(seen)}
report['checks']['registry_rows']=rowreport
prooftext=Path('PROOF_STATUS.md').read_text()
ids=re.findall(r'^\| (PD-[TN]\d{3})\b',prooftext,re.M)
assert len(ids)==len(set(ids))==146
priorids=re.findall(r'^\| (PD-[TN]\d{3})\b',old('PROOF_STATUS.md').decode(),re.M)
assert set(priorids)<=set(ids)
assert set(ids)-set(priorids)=={'PD-T101','PD-T102','PD-T103'}
report['checks']['primary_proof_ids']={'count':len(ids),'duplicates':0,'prior_ids_preserved':len(priorids),'new':['PD-T101','PD-T102','PD-T103']}
# Existing mappings retain original key/final-ID/record; new mappings unique.
for provisional,final in json.loads((TOPIC/'finalization/id-map.json').read_text())['mappings'].items():
 assert Path('ID_CROSSWALK.md').read_text().count('| '+provisional+' | '+final+' |')==1
 assert len(re.findall(r'^\| '+re.escape(final)+r' \(',prooftext,re.M))==1
# Ledger is append/insert only: all prior bytes after unchanged title contiguous.
ledger=Path('topics/padua-batch-20261031/ALLOCATIONS.md').read_bytes()
assert old('topics/padua-batch-20261031/ALLOCATIONS.md').split(b'\n',1)[1] in ledger
for name in ('PAPER_MAP.md','state/CURRENT.md'):
 assert Path(name).read_bytes().startswith(old(name)),name
# Replay exact audited replacements from main; only dated history added after.
applied=json.loads((TOPIC/'finalization/applied-replacements.json').read_text())['replacements']
byfile=collections.defaultdict(list)
for item in applied:byfile[item['path']].append(item)
for name,items in byfile.items():
 s=old(name).decode()
 for x in items:
  assert s.count(x['old'])==1,(name,'old match')
  if name.endswith('OPEN_TARGETS.md'):assert x['new'].startswith(x['old']+'\n\nStatus update after audit:')
  s=s.replace(x['old'],x['new'])
 current=Path(name).read_text()
 assert current.startswith(s),(name,'extra source change')
 if name.endswith('OPEN_TARGETS.md'):assert current==s
 else:assert current[len(s):].startswith('\n- 2026-11-01, Codex PR #9 finalization')
report['checks']['audited_replacements_applied']=len(applied)
report['checks']['original_target_routes_preserved']=3
# No scientific/auditor mutation. New final-ID metadata is outside Statement;
# B5 Open items has one bookkeeping update, which cannot change a proof.
science=[]
for name in git('ls-tree','-r','--name-only',INPUT,str(TOPIC)).decode().splitlines():
 b=old(name,INPUT);p=Path(name)
 if '/code/' in name or '/outputs/' in name or '/audit-support/' in name or '/audit-' in name or name.endswith('/audit-01.md'):
  assert p.read_bytes()==b,('changed science/audit',name);science.append(name)
 if '/theory/proof-attempts-codex-0' in name and not name.endswith('-04-krylov-prefix-route.md'):
  current=p.read_text();before=b.decode()
  if '## Proof or evidence\n' in before:
   def proof(s):return s.split('## Proof or evidence\n',1)[1].split('\n## Scope',1)[0]
   assert proof(current)==proof(before),('proof changed',name)
  if '## Statement\n' in before:
   def statement(s):return s.split('## Statement\n',1)[1].split('\n## Definitions',1)[0]
   assert statement(current)==statement(before),('statement changed',name)
report['checks']['scientific_and_auditor_files_byte_identical']=len(science)
links=0;missing=[]
for name in ['PROOF_STATUS.md','ID_CROSSWALK.md','state/IDEAS.md','state/CURRENT.md','PAPER_MAP.md','literature/INDEX.md','literature/CORPUS.md']:
 p=Path(name)
 for target in re.findall(r'\]\(([^\s)]+)\)',p.read_text()):
  if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',target) or target.startswith('#'):continue
  target=urllib.parse.unquote(target.split('#',1)[0]);links+=1
  if not (p.parent/target).exists():missing.append([name,target])
assert not missing,missing
report['checks']['local_registry_links']={'checked':links,'missing':missing}
report['checks']['current_hashes']=[{'path':name,'sha256':digest(Path(name).read_bytes()),'bytes':Path(name).stat().st_size} for name in sorted(allowed)]
subprocess.run(['git','merge-base','--is-ancestor',BASE,'HEAD'],check=True)
subprocess.run(['git','diff','--check'],check=True)
report['pass']=True
print(json.dumps(report,indent=2,ensure_ascii=False))
