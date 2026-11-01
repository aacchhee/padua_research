"""Read-only source inspection; writes DRAFT protocol receipts only."""
import pathlib,subprocess,json,hashlib,re,datetime
root=pathlib.Path('.');out=root/'topics/padua-mz-2d-20261101/protocol';topic=root/'topics/padua-mz-2d-20261101'
main='806cc7b4509fd93bae652f9545d32d95529f8281';old_a2='12e9cf4539d0977773cad75fc74f93d1664cb429'
refresh=json.loads((out/'final-github-refresh-frozen.json').read_text())
def git(*args):return subprocess.check_output(['git',*args])
def blob(b):return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def desc(p,b):return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':blob(b)}
def pin(ref,p):return dict(commit=ref,**desc(p,git('show',ref+':'+p)))
heads=[('main',main)]+[('PR'+str(x['number']),x['head_sha']) for x in refresh['open_prs']]
regs=['PROOF_STATUS.md','state/IDEAS.md','literature/INDEX.md','ID_CROSSWALK.md'];scan=[]
for label,sha in heads:
 paths=git('ls-tree','-r','--name-only',sha).decode().splitlines()
 ledger=[p for p in paths if re.search(r'allocat|reserv|ledger',p,re.I) and p.endswith('.md')]
 records=[]
 for p in regs+ledger:
  b=git('show',sha+':'+p);rec=desc(p,b);rec['complete_read']=True;records.append(rec)
 scan.append({'label':label,'commit':sha,'files':records})
res={'date':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'Point-in-time reservation recheck before proposed assignment; assignment NOT performed','rules_read_sha':'cf89b140530d5838bdb208a8c28f3e7aa676ace3','heads':scan,'closed_unmerged':refresh['closed_unmerged_search'],'campaign_priority_commit':'9f0c7710abd19ee5a0d61bce6384e7a399e838d2','campaign_ranges':{'PD-T':[106,135],'PD-N':[44,61],'IDEA':[210,245],'LIT':[427,444]},'PR15_disjoint_ranges':{'PD-T':[136,155],'PD-N':[62,71],'IDEA':[246,285],'LIT':[445,459]},'union_reserved_maxima':{'PD-T':155,'PD-N':71,'IDEA':285,'LIT':459},'verdict':'PASS: PR15 imports exact campaign ranges and reserves only higher disjoint ranges; PR12 remains no-range. No closed-unmerged PR returned. Existing campaign ranges remain valid.','notes':['PR12 ledger and registries lag merged PR9 but do not allocate a conflicting range. Do not import its stale shared state.','Current working campaign ledger does not yet include PR15; root should preserve its ranges during final preparation without allocating them again.','Historical NEXT-unreserved labels and external bttb-research LIT1729/1750 are not allocated Padua identifiers.','This does not refresh the frozen mathematical source pin to PR12; see final-input-manifest.json.']}
(out/'final-reservation-recheck.json').write_text(json.dumps(res,indent=2)+'\n')
# Preserve the explicitly reviewed frozen map; generic rescans cannot silently renumber it.
frozen_proposal=json.loads((out/'final-id-map-draft.json').read_text())
paths=list(topic.rglob('*.md'))+list(root.glob('tracks/mz-constants/theory/mz2d*.md'))
paths=[p for p in paths if 'protocol' not in p.parts and 'handoffs' not in p.parts]
counts=frozen_proposal['counts_declared'];proposal=frozen_proposal
if frozen_proposal.get('unfrozen',True):
 # Inventory is provisional while workers finish. Only declarations receive map proposals.
 paths=list(topic.rglob('*.md'))+list(root.glob('tracks/mz-constants/theory/mz2d*.md'))
 paths=[p for p in paths if 'protocol' not in p.parts and 'handoffs' not in p.parts]
 pat=re.compile(r'(?:PD-[TN]|IDEA|LIT)\?mz2d-codex-\d+')
 occ={};decl={}
 for p in sorted(paths):
  text=p.read_text()
  for num,line in enumerate(text.splitlines(),1):
   for ident in pat.findall(line):
    occ.setdefault(ident,[]).append({'path':str(p),'line':num})
    if re.match(r'^#{1,4}\s+'+re.escape(ident)+r'\b',line):decl.setdefault(ident,[]).append({'path':str(p),'line':num,'heading':line})
 starts={'PD-T':106,'PD-N':44,'IDEA':210};maps={};counts={}
 for ns,start in starts.items():
  ids=sorted([i for i in decl if i.startswith(ns+'?')],key=lambda i:int(i.rsplit('-',1)[1]))
  for n,ident in enumerate(ids,start):maps[ident]=ns+('-' if ns=='IDEA' else '')+f'{n:03}'
  counts[ns]=len(ids)
 lit={'LIT?mz2d-codex-01':{'proposed':'LIT-312','kind':'reuse same generating-curve2006 source'},'LIT?mz2d-codex-02':{'proposed':'LIT-427','kind':'new SVZ2008 source, no same-source row in complete INDEX'},'LIT?mz2d-codex-03':{'proposed':'LIT-428','kind':'new CDMV2007 Hyperinterpolation on the square, not existing CDMV2008 Computational aspects'},'LIT?mz2d-codex-04':{'proposed':'LIT-014','kind':'reuse earliest same Dencker-Erb2017 source; existing duplicates304/319/380 remain intact'},'LIT?mz2d-codex-05':{'proposed':'LIT-379','kind':'reuse same KL2021 source; add new direct reading coverage separately'},'LIT?mz2d-codex-06':{'proposed':'LIT-314','kind':'reuse same Xu1996 source'},'LIT?mz2d-codex-07':{'proposed':'LIT-045','kind':'reuse same ASV source;415 is retained historic duplicate'}}
 for k,v in lit.items():maps[k]=v['proposed']
 proposal={'status':'DRAFT ONLY. Root approval and worker freeze required before any assignment or shared write.','captured_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'working_head':git('rev-parse','HEAD').decode().strip(),'counts_declared':counts,'new_LIT_count':2,'reuse_LIT_count':5,'mapping':maps,'literature_decisions':lit,'declarations':decl,'occurrences':occ,'referenced_without_declaration':sorted(set(occ)-set(decl)),'unfrozen':True,'literature_index_identity':pin(main,'literature/INDEX.md'),'source_coverage_policy':'Reuse source ID only; retain all topic primary reading scopes/normalization warnings and dated attribution. Do not replace historical UNVERIFIED records or silently promote source claims to local PROVED.'}
 (out/'final-id-map-draft.json').write_text(json.dumps(proposal,indent=2)+'\n')
# Preserve every frozen A1/A2 identity, and compare to moved PR12 WITHOUT changing pin.
original=json.loads((out/'input-manifest.json').read_text());newa2=next(x['head_sha'] for x in refresh['open_prs'] if x['number']==12)
compare=[]
for f in original['A2']['files']:
 newer=pin(newa2,f['path']);compare.append({'path':f['path'],'frozen_commit':f['commit'],'frozen_blob':f['git_blob'],'current_PR12_commit':newa2,'current_PR12_blob':newer['git_blob'],'same_blob':f['git_blob']==newer['git_blob']})
# All preexisting and new MZ theory, code, manuscript/source inputs; actual bytes captured.
selected=[]
for base in [root/'tracks/mz-constants',root/'topics/mz-constants/sources']:
 for p in base.rglob('*'):
  if p.is_file() and '__pycache__' not in p.parts and p.suffix not in ['.pyc']:
   selected.append(p)
for p in paths:
 if p not in selected:selected.append(p)
files=[]
for p in sorted(set(selected)):
 b=p.read_bytes();rec=desc(p,b)
 try:rec['base_blob']=git('rev-parse',main+':'+str(p)).decode().strip();rec['unchanged_from_base']=rec['base_blob']==rec['git_blob']
 except subprocess.CalledProcessError:rec['base_blob']=None
 files.append(rec)
manifest={'status':'Frozen scientific source snapshot before ID-only replacement. Root-owned reports may receive final metadata later; content inspection is not an executed verification/audit of every object.','captured_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'working_head':git('rev-parse','HEAD').decode().strip(),'frozen_input_manifest':'input-manifest.json','original_A1_A2_pins_preserved':original,'PR12_advance_comparison':compare,'policy':'A2 mathematical input remains12e9cf45; newer PR12 objects recorded only for impact review, not adopted silently.','local_MZ_objects':files}
(out/'final-input-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({'scanned_heads':heads,'inventory_counts':counts,'literature_new':2,'literature_reuse':5,'pending_declarations':proposal.get('pending_declarations',proposal.get('referenced_without_declaration',[])),'local_objects':len(files),'A2_frozen_files_changed_at_new_PR12':[x['path'] for x in compare if not x['same_blob']]}))
