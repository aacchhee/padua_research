"""Root-approved one-shot ID-only assignment and append-only registration.
No Git operations. Dry run default; --apply-approved records execution.
"""
import argparse,collections,datetime,hashlib,json,pathlib,re,subprocess
R=pathlib.Path('.');T=R/'topics/padua-mz-2d-20261101';P=T/'protocol'
M=json.loads((P/'final-id-map-draft.json').read_text());mapping=M['mapping'];decl=M['declarations']
PAT=re.compile('|'.join(re.escape(x) for x in sorted(mapping,key=len,reverse=True)))
def replace(s):
 s=s.replace('LIT?mz2d-codex-01/02','LIT?mz2d-codex-01/LIT?mz2d-codex-02')
 return PAT.sub(lambda m:mapping[m.group()],s)
def sha(b):return hashlib.sha256(b).hexdigest()
def cell(s):return re.sub(r'\s+',' ',s).replace('|','\\|')
def git(*args):return subprocess.check_output(['git',*args])
def section(s,pat):
 m=re.search(r'^## '+pat+r'[^\n]*\n(.*?)(?=^## |\Z)',s,re.M|re.S);return m.group(1).strip() if m else ''
def excerpt(s,n=280):return cell(s)[:n]

def main(apply):
 assert M['counts_declared']=={'PD-T':12,'PD-N':10,'IDEA':18}
 assert mapping['PD-N?mz2d-codex-41']=='PD-N045'
 before={};writes={}
 def read(p):
  p=pathlib.Path(p)
  if p not in before:before[p]=p.read_bytes() if p.exists() else None
  return (before[p] or b'').decode()
 def write(p,s):read(p);writes[pathlib.Path(p)]=s.encode()
 def append(p,s):
  old=read(p);assert '## Padua MZ 2D campaign — PR14 final registration' not in old
  write(p,old.rstrip()+'\n\n'+s.strip()+'\n')
 marker='## Padua MZ 2D campaign — PR14 final registration'
 # Whitelist developer mathematical texts. Frozen reports, archives, code,
 # evidence, root-owned report/log/plan and handoff01 never enter this list.
 source_paths=[R/x['path'] for k,x in decl.items() if k.startswith('PD-')]
 source_paths+=sorted({R/x['path'] for k,x in decl.items() if k.startswith('IDEA')})
 source_paths += [T/'definitions.md',T/'literature.md']
 source_paths += sorted((T/'directions').glob('D[0-9]*.md'))
 source_paths=list(dict.fromkeys(source_paths))
 assert not any('verification' in p.name or 'independent' in p.name or 'audit' in p.name for p in source_paths)
 primary=[]
 for ident,x in decl.items():
  if not ident.startswith('PD-'):continue
  s=read(x['path']);assert s.splitlines()[0].startswith('# '+ident+' ')
  st=re.search(r'Overall status:\s*\*\*(PROVED|PARTIAL|CONDITIONAL|MEASURED|OPEN)\*\*',s,re.S)
  assert st,(ident,'missing explicit overall status')
  dependencies=replace(section(s,r'Depends on'))
  deps=sorted(set(re.findall(r'PD-[TN]\d{3}',dependencies)))
  deps={'PD-T106': ['PD-T101'], 'PD-N044': ['PD-T106'], 'PD-T115': [], 'PD-N053': [], 'PD-T112': [], 'PD-T113': ['PD-T106', 'PD-T112'], 'PD-N045': ['PD-T106'], 'PD-N046': [], 'PD-N049': ['PD-T018'], 'PD-T108': ['PD-T106'], 'PD-T117': ['PD-T013', 'PD-T017', 'PD-T018', 'PD-T022', 'PD-T023']}.get(mapping[ident],deps) # Exclude explicitly nondependent predecessor/context references.
  scope=section(s,r'Statement')
  primary.append({'provisional':ident,'final':mapping[ident],'title':x['title'],'path':x['path'],'status':st.group(1),'depends_on':deps,'statement_sha256':sha(scope.encode())})
 for p in source_paths:
  old=read(p);new=replace(old)
  # Canonical alias metadata preserves original identifiers, not scientific text.
  if str(p).startswith('tracks/mz-constants/theory/mz2d'):
   ident=next(k for k,x in decl.items() if x['path']==str(p))
   lines=new.splitlines(keepends=True);lines.insert(1,'\nProvisional alias: `'+ident+'`. Final ID assigned at PR preparation, 2026-11-01; required Claude audit PENDING.\n');new=''.join(lines)
  write(p,new)
 # Shared registries: append current bytes, never regenerate previous entries.
 proof=marker+'\n\nStage **AUDIT**, required Claude Opus 5.5 xhigh audit **PENDING**; draft not ready. Development statuses below are separate from acceptance. Exact scopes and limitations are in each linked durable record. No universal endpoint positivity or upper bound is claimed.\n\n| ID | Claim | Status | Evidence | Disposition / reason | Depends on | Record | Audit |\n|---|---|---|---|---|---|---|---|\n'
 for d in sorted(primary,key=lambda d:(d['final'][:4],d['final'])):
  disposition='Scoped mechanism statement only; candidate disposition and tested limits in record' if d['final'].startswith('PD-N') else 'Retained at exact stated scope; no novelty claim'
  proof+='| '+ ' | '.join([d['final']+' ('+d['provisional']+')',cell(d['title']),d['status'],'Written proof or finite evidence as explicitly distinguished in record',disposition,', '.join(d['depends_on']) or 'Explicit elementary/frozen inputs in record','[record]('+d['path']+')','Claude PENDING; supplementary checks in topic'])+' |\n'
 append('PROOF_STATUS.md',proof)
 idea=marker+'\n\nAll candidates, including failed, equivalent and deferred routes, are retained in full at the linked canonical files. Stage AUDIT; Claude audit PENDING. The disposition summaries below do not broaden their exact stated scopes.\n\n| ID | Provisional alias | Candidate | Disposition / scope | Full record |\n|---|---|---|---|---|\n'
 idea_rows=[]
 for ident,x in sorted(decl.items(),key=lambda v:mapping[v[0]]):
  if not ident.startswith('IDEA'):continue
  s=read(x['path']);start=s.index(ident);tail=s[start:];block=re.split(r'\n#{1,3} IDEA\?',tail,maxsplit=1)[0]
  m=re.search(r'(?:^|\n)-?\s*(?:Candidate )?[Dd]isposition[^:]*:\s*(.*?)(?=\n- |\n#{1,3} |\Z)',block,re.S)
  disp=replace(cell(m.group(1))) if m else 'Exact disposition, separation criterion and kill-test outcome in linked full candidate'
  # Keep full scoped paragraph rather than truncate off qualifications.
  idea+='| '+' | '.join([mapping[ident],ident,cell(x['title']),disp,'[full candidate](../'+x['path']+')'])+' |\n';idea_rows.append(ident)
 append('state/IDEAS.md',idea)
 cross=marker+'\n\nReservation priority: `9f0c7710abd19ee5a0d61bce6384e7a399e838d2`; [map](topics/padua-mz-2d-20261101/protocol/final-id-map.json), [fresh union scan](topics/padua-mz-2d-20261101/protocol/final-reservation-recheck.json). No accepted ID is renumbered.\n\n| Provisional ID | Final ID | Origin | Durable record / source coverage | Audit / provenance |\n|---|---|---|---|---|\n'
 for ident,final in mapping.items():
  path=decl[ident]['path'] if ident in decl else ('tracks/mz-constants/theory/mz2d-upper-sign-obstruction.md' if ident.startswith('PD-N') else 'topics/padua-mz-2d-20261101/literature.md')
  note='Historical duplicate consolidated into existing N10; no second PD-N allocation' if ident.endswith('-41') and ident.startswith('PD-N') else ('Same-source reuse; new reading coverage remains separately dated' if ident.startswith('LIT') and final not in ['LIT-427','LIT-428'] else 'Claude audit PENDING; see exact source scope')
  cross+='| '+' | '.join([ident,final,'codex/padua-mz-2d-20261101','[record]('+path+')',note])+' |\n'
 cross+='\nOriginal-to-split relations: PD-T106 exact aliases and pencil → PD-T109 separately substantive masked-tensor architecture; exact finite spectra PD-T107 → scoped threshold refutation PD-N044. PD-T028 remains the original OPEN signed-Padua spectral target, supported by PD-T106/109/111/115/117 and finite PD-T107/108; endpoint upper target PD-T110 and fixed-ratio target PD-T116 remain OPEN. D5 uniform operator target PD-T114 remains OPEN; proved general tools PD-T112/113 and scoped failures PD-N050–052 are separate dependencies, not solved target conjuncts. Historical provisional PD-N?mz2d-codex-41 consolidates into PD-N045, with complete original proof bytes retained in the verification-only archive.\n'
 append('ID_CROSSWALK.md',cross)
 append('state/CURRENT.md',marker+'\n\nSigned Lebesgue Padua campaign: stage **AUDIT**, required Claude Opus 5.5 xhigh audit **PENDING**; draft PR14 not ready. Registered exact aliases/defect structure, four independently executed finite spectral cases, the exact m30 eta>3/4 witness, scoped upper/lower/operator/filter obstructions, signed hyperinterpolation tools, corner weights and tensor-control extrema. Universal endpoint positivity/eta<1, endpoint upper bounds, fixed-ratio signed coercivity and the actual uniform hyperinterpolation norm remain OPEN. [Report](../topics/padua-mz-2d-20261101/report.md), [durable records](../PROOF_STATUS.md), [checks](../topics/padua-mz-2d-20261101/independent-checks.md). No manuscript or novelty claim; existing accepted MZ results remain intact.')
 append('PAPER_MAP.md',marker+'\n\n| Brief | Question | Support | Remaining gaps | Readiness |\n|---|---|---|---|---|\n| [Signed Padua MZ campaign](topics/padua-mz-2d-20261101/report.md) | Beyond-half-exactness signed Lebesgue Padua spectra and reconstruction | PD-T106–117; PD-N044–053 at their individual written statuses | Universal endpoint/fixed-ratio spectral targets and uniform signed operator norm OPEN; historical attribution limits retained | AUDIT, Claude PENDING; draft PR14 not ready, no manuscript/submission claim |')
 append('topics/README.md',marker+'\n\n[padua-mz-2d-20261101](padua-mz-2d-20261101/LOG.md): signed Lebesgue Padua MZ campaign; PD-T106–117, PD-N044–053, IDEA-210–227, LIT-427–428 plus five source-ID reuses. Stage AUDIT, required Claude audit PENDING, draft PR14 not ready.')
 append('tracks/mz-constants/README.md',marker+'\n\n[Two-dimensional signed Padua development](../../topics/padua-mz-2d-20261101/report.md) is registered in PD-T106–117/PD-N044–053 with their individual statuses; IDEA-210–227 retains all candidates. Exact four-size certificates and the m30 eta>3/4 witness have separate actual execution receipts. Universal signed Padua spectral bounds remain OPEN. Stage AUDIT, Claude PENDING; this draft does not change acceptance of the earlier MZ manuscript/results.')
 # Two genuinely new source records use the repository literature template;
 # source-identical prior IDs receive only separately dated coverage notes.
 lit=read(T/'literature.md');blocks={}
 for ident in M['literature_decisions']:
  hit=re.search(r'^### '+re.escape(ident)+r'[^\n]*\n(.*?)(?=^### |^## |\Z)',lit,re.M|re.S);assert hit,ident;blocks[ident]=hit.group(1).strip()
 recordpaths={'LIT?mz2d-codex-02':'literature/records/mz2d-sommariva-vianello-zanovello-2008.md','LIT?mz2d-codex-03':'literature/records/mz2d-caliari-demarchi-vianello-2007.md'}
 coverage_notes=[]
 index=marker+'\n\nAll entries below are **LITERATURE**, not inherited local proofs. Historical rows and reading limitations above remain unchanged.\n\n| ID | Status / claim type | Source statement | Source | Locator | Record | Coverage / limits |\n|---|---|---|---|---|---|---|\n'
 for ident,item in M['literature_decisions'].items():
  final=item['proposed'];title=item['authoritative_source_title'];block=replace(blocks[ident])
  if ident in recordpaths:
   path=recordpaths[ident]
   text='# '+pathlib.Path(path).stem+' — '+title+'\n\n- DOI / URL / supplied location: see primary links in the extracted source record below.\n- Access and reading date: 2026-11-01.\n- Reading coverage: selected primary author-text sections; exact pages/equations below.\n- Reader, model and effort: Codex campaign literature worker, allocated gpt-6.1-sol xhigh; runtime metadata unexposed.\n- Named gaps requiring future re-reading: final journal body/comparison limits below.\n\n## Extracted published statements\n\n### '+final+' — coverage-qualified primary source reading\n\n'+block+'\n\n- Statement in faithful paraphrase: the source statements above retain their attributed scope.\n- Hypotheses and notation: positive Chebyshev/Xu or signed Lebesgue conventions exactly as distinguished above.\n- Page / theorem / equation: exact primary locators above.\n- Reading evidence and limitations: selected reading only; no blanket fulltext or proof-audit claim.\n- Relation to campaign claims (no inherited proof status): see [campaign comparison](../../topics/padua-mz-2d-20261101/literature.md).\n\n## Search and attribution notes\n\nComplete base literature INDEX inspected before source-ID choice; same-source prior rows were reused where present. These two sources have no same-source row in that index. Coverage-qualified attribution, no novelty clearance.\n\n## History\n\n2026-11-01: final source-ID registration during PR14 preparation; no source theorem is promoted to a locally proved claim. Provisional alias `'+ident+'`.\n'
   assert not pathlib.Path(path).exists();write(path,text)
   index+='| '+' | '.join([final,'LITERATURE / selected primary reading',cell(title),'Campaign primary record','Exact equations/pages in source record','[record]('+path.removeprefix('literature/')+')','Selected author-text reading; named final-version gaps remain'])+' |\n'
  else:
   # Separate dated notes avoid creating duplicate primary-ID rows.
   coverage_notes.append('- **'+final+' — 2026-11-01 reading addendum:** '+title+'. Same-source ID reused; exact new primary reading, locators and version gaps are preserved in [campaign literature](../topics/padua-mz-2d-20261101/literature.md). The historical row and its original coverage qualifications remain intact. Provisional source alias `'+ident+'`.')
 index+='\n### Reused-source coverage addenda (2026-11-01)\n\n'+'\n\n'.join(coverage_notes)+'\n'
 append('literature/INDEX.md',index)
 # Preserve the remote PR15 reservation exactly and with published priority.
 ledger='topics/padua-batch-20261031/ALLOCATIONS.md';old=read(ledger)
 remote=git('show','2d20672f62e0130d2adbe104af6e5ee9d05d20af:'+ledger).decode()
 start=remote.index('## Padua Lanczos drift reservation');end=remote.index('## Padua MZ 2D reservation')
 imported=remote[start:end].strip()
 imported=imported.replace('../padua-lanczos-drift-20261101/allocation-scan.json','https://github.com/aacchhee/padua_research/blob/2d20672f62e0130d2adbe104af6e5ee9d05d20af/topics/padua-lanczos-drift-20261101/allocation-scan.json')
 if '## Padua Lanczos drift reservation' not in old:
  line=old.index('\n');old=old[:line+1]+'\n'+imported+'\n\n'+old[line+1:].lstrip()
 ledger_note=marker+'\n\nOwn reservation unchanged, first published `9f0c7710abd19ee5a0d61bce6384e7a399e838d2`: assigned PD-T106–117 (12), PD-N044–053 (10), IDEA-210–227 (18), LIT-427–428 (2). Same-source LIT IDs reused: 312,014,379,314,045. Permanent unused headroom: **PD-T118–135, PD-N054–061, IDEA-228–245, LIT-429–444**. No ranges shift or shrink. [Map](../padua-mz-2d-20261101/protocol/final-id-map.json); [fresh scan](../padua-mz-2d-20261101/protocol/final-reservation-recheck.json).\n\nPR15 reservation data above is imported unchanged (its unavailable local evidence link is made a pinned remote link) from `2d20672f62e0130d2adbe104af6e5ee9d05d20af`; first published commit **6920ba632843597c37e1493d077c1df2e89f54cb**, [PR15](https://github.com/aacchhee/padua_research/pull/15). Its PD-T136–155, PD-N062–071, IDEA-246–285 and LIT-445–459 remain reserved to its branch. This campaign assigns none of them. Stage AUDIT, Claude PENDING.\n'
 write(ledger,old.rstrip()+'\n\n'+ledger_note)
 approved=dict(M);approved['status']='ASSIGNED after explicit root approval; scientific statuses unchanged; Claude audit PENDING';approved['root_approval']='Explicit mapping approval in parent instruction, 2026-11-01';approved['input_head']=git('rev-parse','HEAD').decode().strip();approved['assigned_at']=datetime.datetime.now(datetime.timezone.utc).isoformat();write(P/'final-id-map.json',json.dumps(approved,indent=2)+'\n')
 # Capture every protected input before writes; preserve archive WHOLE FILE.
 protected=[]
 for p in list(T.rglob('*'))+list((R/'tracks/mz-constants/code').rglob('*')):
  if p.is_file() and ('__pycache__' not in p.parts) and ('protocol' not in p.parts) and (('evidence' in p.parts) or 'independent' in p.name or 'audit' in p.name or 'verification' in p.name or p.suffix=='.py' or 'handoffs' in p.parts):protected.append(p)
 protection=[{'path':str(p),'sha256':sha(p.read_bytes()),'bytes':p.stat().st_size} for p in sorted(set(protected))]
 assert not set(writes)&set(protected)
 changes=[{'path':str(p),'before_sha256':sha(before[p]) if before[p] is not None else None,'after_sha256':sha(b),'bytes':len(b)} for p,b in writes.items() if before[p]!=b]
 # Source impact: every source equals prescribed ID substitution and optional
 # canonical alias metadata; scientific statement transformation is recorded.
 impact=[]
 for p in source_paths:
  base=before[p].decode();expected=replace(base)
  if str(p).startswith('tracks/mz-constants/theory/mz2d'):
   ident=next(k for k,x in decl.items() if x['path']==str(p));ls=expected.splitlines(keepends=True);ls.insert(1,'\nProvisional alias: `'+ident+'`. Final ID assigned at PR preparation, 2026-11-01; required Claude audit PENDING.\n');expected=''.join(ls)
  assert writes[p].decode()==expected
  impact.append({'path':str(p),'before_sha256':sha(before[p]),'after_sha256':sha(writes[p]),'normalized_ID_only_plus_alias_metadata':True})
 report={'apply_requested':apply,'root_approved_counts':M['counts_declared'],'new_LIT':2,'reused_LIT':5,'canonical_records':primary,'source_ID_only_impact':impact,'protected_inputs':protection,'changed_files':changes,'shared_append_preservation':True,'stage':'AUDIT','Claude_audit':'PENDING'}
 if apply:
  for p,b in writes.items():
   current=p.read_bytes() if p.exists() else None
   assert current==before[p],('concurrent modification',str(p))
  for p,b in writes.items():p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b)
  for x in protection:assert sha(pathlib.Path(x['path']).read_bytes())==x['sha256']
  # Old shared bytes are a prefix except ledger's explicitly imported section.
  for p in ['PROOF_STATUS.md','state/IDEAS.md','ID_CROSSWALK.md','state/CURRENT.md','PAPER_MAP.md','topics/README.md','tracks/mz-constants/README.md','literature/INDEX.md']:
   assert pathlib.Path(p).read_bytes().startswith(before[pathlib.Path(p)].rstrip())
  (P/'final-assignment-checks.json').write_text(json.dumps(report,indent=2)+'\n')
 else:(P/'final-assignment-dry-run.json').write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps({'applied':apply,'changed_files':len(changes),'protected_files':len(protection),'statuses':dict(collections.Counter(d['status'] for d in primary)),'counts':M['counts_declared']}))

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--apply-approved',action='store_true');args=ap.parse_args();main(args.apply_approved)
