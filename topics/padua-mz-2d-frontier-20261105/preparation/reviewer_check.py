#!/usr/bin/env python3
"""Independent pinned-blob protocol checks; read-only Git, no science execution."""
import hashlib,json,re,subprocess,posixpath
from pathlib import Path
C='05ccb20da1058cade31abc3615264bd4881fa8bf'; B='7a8d8dd313b5370589810f4efd910ed65744f865'; M='d9b7cb89460d4e46e44bbaa66ff766aa499b95ee'
T='topics/padua-mz-2d-frontier-20261105/'
def git(*a): return subprocess.check_output(['git',*a])
def blob(ref,p): return git('show',ref+':'+p)
def txt(ref,p): return blob(ref,p).decode()
def sha(b): return hashlib.sha256(b).hexdigest()
def files(ref): return git('ls-tree','-r','--name-only',ref).decode().splitlines()
cf=set(files(C)); bf=set(files(B)); mf=set(files(M))
m=json.loads(blob(C,T+'preparation/final-id-map.json')); mp={x['provisional']:x['final'] for x in m['records']+m['ideas']}
assert len(mp)==len(set(mp.values()))==25
# Full proof sections independently normalized, without the developer verifier.
proofs={}
for x in m['records']:
 p=T+x['path']; s=txt(C,p); assert x['provisional'] in s
 if x['final']=='PD-T300': assert p not in bf; continue
 old=txt(B,p)
 for a,b in sorted(mp.items(),key=lambda z:-len(z[0])): old=old.replace(a,b)
 def proof(s):
  sections=re.split(r'(?m)^## ',s)
  return next(z for z in sections if z.startswith(('Proof\n','Proof or evidence\n')))
 assert proof(old)==proof(s),p
 proofs[x['final']]=sha(proof(s).encode())
protected=[]
for p in bf:
 if not p.startswith(T): continue
 r=p[len(T):]
 if r=='code/evidence_manifest.py':continue
 if r.startswith(('code/','evidence/','audit-01-support/','independent-checks')) or r in ['audit-01.md','response-01.md']:
  assert blob(B,p)==blob(C,p),p; protected.append(p)
def rows(s):
 pairs=[(re.match(r'^\| (PD-[TN]\d{3})\b',l).group(1),l) for l in s.splitlines() if re.match(r'^\| (PD-[TN]\d{3})\b',l)]
 return dict(pairs)
a,z=rows(txt(M,'PROOF_STATUS.md')),rows(txt(C,'PROOF_STATUS.md'))
changed={'PD-T028','PD-T110','PD-T114','PD-T116'}
# PD-T140 deliberately has two separately labelled inherited claim rows.
for line in txt(M,'PROOF_STATUS.md').splitlines():
 match=re.match(r'^\| (PD-[TN]\d{3})\b',line)
 if match and match.group(1) not in changed: assert line in txt(C,'PROOF_STATUS.md').splitlines()
assert set(a)<=set(z)
assert all(z[k]==v for k,v in a.items() if k not in changed)
assert set(z)-set(a)=={x['final'] for x in m['records']}
for k,ns in [('PD-T028',['PD-N105','PD-N106']),('PD-T110',['PD-N106']),('PD-T116',['PD-N107'])]:
 assert z[k].split('|')[3].strip()=='OPEN' and 'REJECTED: refuted' in z[k]
 assert all(n in z[k] for n in ns)
assert z['PD-T114'].split('|')[3].strip()=='PROVED'
for x in m['records']: assert z[x['final']].split('|')[3].strip()==x['status']
for p in ['RESULTS.md','ID_CROSSWALK.md']:
 assert txt(C,p).startswith(txt(M,p)),p
# All old IDEA IDs remain present; only intended target-related old rows change.
old=txt(M,'state/IDEAS.md');new=txt(C,'state/IDEAS.md')
assert set(re.findall(r'IDEA-\d{3}',old))<=set(re.findall(r'IDEA-\d{3}',new))
for x in m['ideas']: assert x['final'] in new and x['provisional'] in new
cross=txt(C,'ID_CROSSWALK.md')
for x in m['records']+m['ideas']: assert f"| {x['provisional']} | {x['final']} |" in cross
for p in ['open-padua-target.md','mz2d-upper-open.md','mz2d-fixed-ratio.md','mz2d-hyperinterpolation-uniform-open.md']:
 path='tracks/mz-constants/theory/'+p; old=txt(M,path);new=txt(C,path)
 assert new.splitlines()[0]==old.splitlines()[0] and new.endswith(old.split('\n',1)[1])
# Inventory exact bytes and complete declared coverage, evaluated on pinned blobs.
inv=json.loads(blob(C,T+'evidence-manifest.json')); actual=[]
for p in sorted(cf):
 if p.startswith(T):
  r=p[len(T):]
  if r=='evidence-manifest.json' or Path(r).name=='LOG.md' or 'handoffs' in Path(r).parts or '__pycache__' in Path(r).parts or r.endswith('.pyc'):continue
  actual.append((r,p))
actual.append(('../../results/padua-mz-2d-frontier-20261105.md','results/padua-mz-2d-frontier-20261105.md'))
expected={r:[r,len(blob(C,p)),sha(blob(C,p))] for r,p in actual}
assert {x[0]:x for x in inv['files']}==expected
assert len(blob(C,T+'evidence-manifest.json'))<16384
# Independently validate all 43 source identities in the live scan receipt.
scan=json.loads(blob(C,T+'preparation/allocation-scan.json'))
for source,path,digest,_ in scan['files']: assert sha(blob(scan['heads'][source],path))==digest
for x in m['records']+m['ideas']:
 namespace='IDEA' if x['final'].startswith('IDEA') else x['final'][:4]
 n=int(re.search(r'\d+$',x['final']).group());lo,hi=scan['topic_reservation'][namespace];assert lo<=n<=hi
# Original theory files only ID replacements + preserved aliases, checked separately above.
assert set(p for p in cf-bf if p.startswith(T+'theory/'))=={T+'theory/frontier-measurements.md'}
assert blob(C,'AGENTS.md')==blob(B,'AGENTS.md') and blob(C,'agents/WORKFLOW.md')==blob(B,'agents/WORKFLOW.md')
assert not git('diff','--check',M,C)
out={'candidate':C,'response_input':B,'main':M,'verdict':'PASS','protected_files':len(protected),'unchanged_unrelated_registry_ids':len(a)-4,'registered_results':11,'retained_ideas':14,'allocation_source_hashes':len(scan['files']),'inventory_entries':len(expected),'inventory_bytes':len(blob(C,T+'evidence-manifest.json')),'proof_section_sha256':proofs,'measurement_sha256':sha(blob(C,T+'theory/frontier-measurements.md')),'limits':'Pinned mechanical scope only; no new mathematical audit or scientific execution; later integration and readiness records excluded.'}
print(json.dumps(out,indent=2))
