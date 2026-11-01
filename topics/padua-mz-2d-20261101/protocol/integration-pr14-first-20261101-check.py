"""Claude integration check for AC's order 'PR14 first' (2026-11-01).
Run from the PR14 checkout root. Read-only on the repo; writes JSON to argv[1]."""
import hashlib,json,re,subprocess,sys,pathlib,collections,datetime
def git(*a): return subprocess.check_output(['git',*a]).decode()
def sha(b): return hashlib.sha256(b).hexdigest()
R=pathlib.Path('.')
MAIN='806cc7b4509fd93bae652f9545d32d95529f8281'; CAND='e847601c6c1f1261d4862d63360fdfdb0df8a15b'
HEAD=git('rev-parse','HEAD').strip()
PRS={'PR12':'6c6e484818b8b949ab0a6b2a4b9086b6a46528c3','PR15':'fa5835f6fd2c1f62cd9e34e14e90d492ac387242'}
out={'executed_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'head':HEAD,'main':MAIN,'other_open_prs':PRS,'audited_candidate':CAND}
# 1. main is an ancestor of head (no main merge needed)
out['main_is_ancestor']=subprocess.call(['git','merge-base','--is-ancestor',MAIN,HEAD])==0
assert out['main_is_ancestor']
# 2. scientific objects unchanged since the audited candidate: code, evidence, theory proofs other than F1/F2 edits
changed=git('diff','--name-only',CAND,HEAD).split()
sci=[p for p in changed if p.startswith(('tracks/mz-constants/code/','topics/padua-mz-2d-20261101/evidence/','tracks/mz-constants/paper/'))]
out['code_evidence_paper_changed_since_candidate']=sci; assert not sci
theory=[p for p in changed if p.startswith('tracks/mz-constants/theory/')]
out['theory_files_changed_since_candidate']=theory
assert set(theory)<= {'tracks/mz-constants/theory/mz2d-upper-sign-obstruction.md','tracks/mz-constants/theory/mz2d-fixed-ratio.md','tracks/mz-constants/theory/mz2d-fixed-ratio-diamond-reconstruction.md'}
# F1 proof body identical to audited candidate
f1='tracks/mz-constants/theory/mz2d-upper-sign-obstruction.md'
a=git('show',CAND+':'+f1).encode(); b=R.joinpath(f1).read_bytes(); m=b'## Proof or evidence'
out['F1_proof_to_EOF_identical_to_candidate']=a[a.index(m):]==b[b.index(m):]; assert out['F1_proof_to_EOF_identical_to_candidate']
# 3. status cells of the 22 rows unchanged vs candidate
def rows(t): return {mm.group(1):mm.group(0).split('|')[3].strip() for mm in re.finditer(r'^\| (PD-[TN]\d+)\b.*$',t,re.M)}
o=rows(git('show',CAND+':PROOF_STATUS.md')); n=rows(R.joinpath('PROOF_STATUS.md').read_text())
out['proof_status_cells_unchanged']=all(o[k]==n[k] for k in o) and o.keys()==n.keys(); assert out['proof_status_cells_unchanged']
cnt=collections.Counter(n[k] for k in n if re.match(r'PD-T1(0[6-9]|1[0-7])$|PD-N0(4[4-9]|5[0-3])$',k)); out['campaign_status_counts']=dict(cnt)
assert cnt=={'PROVED':17,'MEASURED':2,'OPEN':3},cnt
# 4. audit record: candidate audit-01 text is an exact prefix of current (addendum only)
a1=git('show','0d48727f13bf8afcf8c21568ed71572c305552a5:topics/padua-mz-2d-20261101/audit-01.md'); cur=R.joinpath('topics/padua-mz-2d-20261101/audit-01.md').read_text()
out['audit01_original_is_prefix']=cur.startswith(a1); assert out['audit01_original_is_prefix']
# 5. registry uniqueness
for f,pat in [('PROOF_STATUS.md',r'^\| (PD-[TN]\d+)\b'),('literature/INDEX.md',r'^\| (LIT-\d+)\b')]:
    c=collections.Counter(re.findall(pat,R.joinpath(f).read_text(),re.M)); assert all(v==1 for v in c.values()),f
# 6. other open PRs: no primary rows in our ranges; PR15 ledger still has both reservation sets; A2 pins
rng={'PD-T':(106,135),'PD-N':(44,61),'IDEA':(210,245),'LIT':(427,444)}
coll=[]
for lab,h in PRS.items():
    for f in ['PROOF_STATUS.md','state/IDEAS.md','literature/INDEX.md']:
        t=git('show',h+':'+f)
        for ident in re.findall(r'^\| ((?:PD-[TN]|IDEA-|LIT-)\d+)\b',t,re.M):
            ns=re.sub(r'-?\d+$','',ident); k=int(re.search(r'\d+$',ident).group())
            if ns in rng and rng[ns][0]<=k<=rng[ns][1]: coll.append((lab,f,ident))
out['collisions']=coll; assert not coll
led=git('show',PRS['PR15']+':topics/padua-batch-20261031/ALLOCATIONS.md')
out['PR15_ledger_tokens']=all(t in led for t in ['PD-T106–PD-T135','PD-T136–PD-T155','PD-N062–PD-N071','IDEA-246–IDEA-285','LIT-445–LIT-459']); assert out['PR15_ledger_tokens']
man=json.loads(R.joinpath('topics/padua-mz-2d-20261101/protocol/final-input-manifest.json').read_text())
ok=sum(subprocess.check_output(['git','rev-parse',PRS['PR12']+':'+it['path']]).decode().strip()==it['frozen_blob'] for it in man['PR12_advance_comparison'])
out['A2_pins_unchanged_at_PR12']=f'{ok}/13'; assert ok==13
# 7. local markdown links in topic + new theory + shared registries
bad=[];links=0
files=list(R.joinpath('topics/padua-mz-2d-20261101').rglob('*.md'))+list(R.joinpath('tracks/mz-constants/theory').glob('mz2d*.md'))+[R/'PROOF_STATUS.md',R/'state/IDEAS.md',R/'ID_CROSSWALK.md',R/'literature/INDEX.md']
for p in files:
    txt=[];fen=False
    for line in p.read_text().splitlines():
        if re.match(r'^\s*(```|~~~)',line): fen=not fen; continue
        if not fen: txt.append(line)
    for raw in re.findall(r'\[[^\]]*\]\(([^)]+)\)',re.sub(r'`[^`]*`','','\n'.join(txt))):
        t=raw.split('#',1)[0].split(' ',1)[0].strip('<>')
        if not t or re.match(r'[a-z]+:',t): continue
        links+=1
        if not (p.parent/t).exists(): bad.append((str(p),t))
out['links_checked']=links; out['broken_links']=bad; assert not bad
# 8. sizes
js=[p for p in R.joinpath('topics/padua-mz-2d-20261101').rglob('*') if p.is_file() and p.suffix in ('.json','.gz')]
out['generated_json_total_bytes']=sum(p.stat().st_size for p in js); out['largest_json_bytes']=max(p.stat().st_size for p in js)
assert out['largest_json_bytes']<=1_000_000 and out['generated_json_total_bytes']<5_000_000
# 9. open handoffs
hs=sorted(R.joinpath('topics/padua-mz-2d-20261101/handoffs').glob('*.md'))
out['open_handoffs']=[h.name for h in hs if '- Status: open' in h.read_text()]
out['status']='PASS'
pathlib.Path(sys.argv[1]).write_text(json.dumps(out,indent=1,ensure_ascii=False)+'\n'); print(json.dumps({k:out[k] for k in ['status','campaign_status_counts','links_checked','generated_json_total_bytes','largest_json_bytes','open_handoffs','theory_files_changed_since_candidate']},ensure_ascii=False))
