"""Mechanical PR12 finalization validation; no mathematical execution/audit.

Default writes a small receipt. --no-write preserves existing receipts;
--manifest additionally checks the staged-index evidence snapshot.
"""
import argparse, hashlib, json, re, subprocess
from pathlib import Path
from urllib.parse import unquote

R=Path(__file__).resolve().parents[3]
T='topics/padua-proof-attempts-2-20261101/'
P=R/T/'preparation'
BASE='67bd07c0867d8d49eb104942237d7f51a7d9f77d'
RESPONSE='e1581b3d697610be5eb647c594e7d66fcbc61352'
def git(*a):return subprocess.check_output(['git',*a],cwd=R)
def data(ref,path):return git('show',ref+':'+path)
def current(path):return (R/path).read_bytes()
def tree(ref):return git('ls-tree','-r','--name-only',ref).decode().splitlines()
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--no-write',action='store_true');ap.add_argument('--manifest',action='store_true');args=ap.parse_args()
    errors=[]
    def check(ok,msg):
        if not ok:errors.append(msg)
    m=json.loads(current(T+'preparation/final-id-map.json'))
    records=m['records'];mapping=m['mapping'];numbers={r['local_number']:r['final'] for r in records.values()}
    check(len(records)==44 and len(mapping)==70 and len(set(mapping.values()))==70,'mapping counts/uniqueness')
    check({r['final'] for r in records.values() if r['status']=='OPEN'}=={'PD-T180','PD-T181','PD-T184'},'OPEN split scope')
    frozen=[p for p in tree(RESPONSE) if p.startswith(T+'code/') or p.startswith(T+'outputs/') or p==T+'audit-01.md' or p.startswith(T+'audit-support/') or p==T+'response-01.md']
    for p in frozen:check(current(p)==data(RESPONSE,p),'frozen file changed: '+p)
    for local,r in records.items():
        s=current(r['path']).decode();before=data(RESPONSE,r['path']).decode()
        check(f"Final ID: **{r['final']}**" in s and local in s,'theory registration: '+r['final'])
        stripped=re.sub(r'\n\nFinal ID:.*?\n\nCanonical Split from \(registration\):[^\n]*\n','\n',s,count=1,flags=re.S)
        check(stripped==before,'non-metadata theory change: '+r['final'])
        source=re.search(r'^Canonical Split from \(registration\): (.*)$',s,re.M)
        check(source is not None,'missing reciprocal source: '+r['final'])
        if source:
            for source_id in re.findall(r'PD-[TN]\d{3}',source[1]):
                parents={'PD-T098':'04-padua-corner-expansion','PD-T099':'05-padua-corner-argmax','PD-T100':'06-padua-lebesgue-maxima-counts','PD-N039':'N01-symmetrised-product-inertia-count','PD-N040':'N02-windowed-rational-lanczos-instability'}
                check(source_id in parents,'unexpected canonical source')
                if source_id in parents:
                    pp='topics/programme-ideas-20261031/theory/programme-ideas-claude-'+parents[source_id]+'.md'
                    split=re.search(r'^Split into: (.*)$',current(pp).decode(),re.M)
                    check(split is not None and r['final'] in split[1],'nonreciprocal split '+source_id+' -> '+r['final'])

    ps=current('PROOF_STATUS.md').decode();ideas=current('state/IDEAS.md').decode();cross=current('ID_CROSSWALK.md').decode()
    for local,r in records.items():
        check(len(re.findall(r'^\| '+r['final']+r' \(',ps,re.M))==1,'theory registry definition '+r['final'])
        check(f"| {local} | {r['final']} |" in cross,'theory crosswalk '+r['final'])
    for r in m['ideas']:
        check(len(re.findall(r'^\| '+r['final']+r';',ideas,re.M))==1,'idea registry definition '+r['final'])
        check(f"| {r['local']} | {r['final']} |" in cross,'idea crosswalk '+r['final'])
    check(re.search(r'^\| PD-T100 .*?\| MEASURED \|',ps,re.M) is not None,'PD-T100 must remain MEASURED')
    for parent in ['PD-T098','PD-T099']:
        check(re.search(r'^\| '+parent+r' .*?\| OPEN \|',ps,re.M) is not None,parent+' must remain OPEN')

    # All inherited definitions remain exact except the specifically approved
    # parent/frontier pointers. Crosswalk/results/literature are append-only.
    allowed={'PROOF_STATUS.md':{'PD-T098','PD-T099','PD-T100','PD-N039','PD-N040'},'state/IDEAS.md':{'IDEA-048','IDEA-192','IDEA-198','IDEA-206'}}
    for path,ids in allowed.items():
        now=current(path).decode()
        for line in data(BASE,path).decode().splitlines():
            if not line.startswith('|'):continue
            k=re.match(r'^\| (PD-[TN]\d{3}|IDEA-\d{3})',line)
            if not k or k[1] not in ids:check(line in now,'inherited row lost/changed '+path+':'+line[:65])
    for path in ['RESULTS.md','ID_CROSSWALK.md','literature/INDEX.md','PAPER_MAP.md','state/CURRENT.md','topics/README.md','topics/padua-batch-20261031/ALLOCATIONS.md']:
        baseline=data('103ee71' if path.endswith('/ALLOCATIONS.md') else BASE,path).rstrip()
        check(current(path).startswith(baseline),'unrelated shared content changed: '+path)
    check(current('RESULTS.md').decode().count('## padua-proof-attempts-2-20261101\n')==1,'own RESULTS section count')

    def translate(s):
        for a,b in sorted(mapping.items(),key=lambda kv:-len(kv[0])):s=s.replace(a,b)
        return re.sub(r'(?<=[\s`,(/])-(\d{2})(?!\d|[./]\d)',lambda x:numbers.get(x[1],x[0]),s)
    blocks=re.findall(r'Target: `([^`]+)`\s+Pinned commit: `([a-f0-9]{40})`\s+Old:\s+```text\n(.*?)\n```\s+New:\s+```text\n(.*?)\n```',current(T+'proposed-record-changes.md').decode(),re.S)
    check(len(blocks)==10,'literal proposal count')
    for target,pin,o,n in blocks:
        now=current(target).decode()
        if not o:
            check(target not in tree(BASE),'new results target existed at base');continue
        check(data(pin,target).decode().count(o)==1 and data(BASE,target).decode().count(o)==1,'Old uniqueness '+target)
        addition=n[len(o):] if n.startswith(o) else n[:-len(o)]
        check(o in now and translate(addition) in now,'literal applied text/preservation '+target)
        check(re.search(r'(?<=[\s`,(/])-(\d{2})(?!\d|[./]\d)',translate(addition)) is None,'unresolved short local ID '+target)
    frontier=current('topics/programme-ideas-20261031/OPEN_TARGETS.md').decode()
    check(not any('A2/A3 asymptotics' in l and not l.startswith('Historical introduction') for l in frontier.splitlines()),'stale unqualified A2/A3 frontier')

    owned={r['path'] for r in records.values()}
    shared=set(json.loads(current(T+'preparation/prepare-receipt.json'))['shared_paths'])
    changed=git('diff','--name-only',BASE).decode().splitlines()
    untracked=git('ls-files','--others','--exclude-standard').decode().splitlines()
    for p in changed+untracked:
        check(p.startswith(T) or p in shared,'unauthorized preparation path '+p)
        check(not p.startswith('.github/') and p not in ['AGENTS.md','agents/WORKFLOW.md','agents/codex/CODEX.md'],'protected path '+p)
    for path in sorted(set(changed+untracked)):
        if not path.endswith('.md'):continue
        s=current(path).decode();s=re.sub(r'^```[^\n]*\n.*?^```\s*$','',s,flags=re.M|re.S)
        for link in re.findall(r'\[[^\]\n]*\]\(([^\s)]+)\)',s):
            link=unquote(link.split('#')[0])
            if not link or re.match(r'[a-zA-Z][\w+.-]*:',link):continue
            check(((R/path).parent/link).exists(),'broken link '+path+' -> '+link)

    files=[p for p in (R/T).rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix not in ['.md','.py','.sh']]
    total=sum(p.stat().st_size for p in files);largest=max(p.stat().st_size for p in files)
    check(total<=5_000_000 and largest<=1_000_000,'generated output budget')
    manifest_counts=None
    if args.manifest:
        doc=json.loads(data('',T+'evidence-manifest.json'))
        for row in doc['inputs']:
            d=data(row['commit'],row['path']);check(len(d)==row['bytes'] and hashlib.sha256(d).hexdigest()==row['sha256'],'manifest input '+row['path'])
            check(git('rev-parse',row['commit']+':'+row['path']).decode().strip()==row['git_blob'],'manifest blob '+row['path'])
        for row in doc['outputs']:
            d=data('',row['path']);check(len(d)==row['bytes'] and hashlib.sha256(d).hexdigest()==row['sha256'],'manifest output '+row['path'])
        expected={p for p in git('ls-files','--',T).decode().splitlines() if p!=T+'evidence-manifest.json' and not p.startswith(T+'handoffs/') and '__pycache__' not in p}
        check(expected=={r['path'] for r in doc['outputs']},'manifest coverage')
        manifest_counts={'inputs':len(doc['inputs']),'outputs':len(doc['outputs'])}
    shared_identities=[]
    for p in sorted(shared):
        d=current(p);prior=data(BASE,p) if p in tree(BASE) else b''
        shared_identities.append({'path':p,'base_blob':git('rev-parse',BASE+':'+p).decode().strip() if prior else None,'sha256':hashlib.sha256(d).hexdigest(),'bytes':len(d)})
    result={'purpose':'mechanical preparation verification, not mathematical audit','base':BASE,'response':RESPONSE,'mapping_count':len(mapping),'theory_count':44,'idea_count':26,'frozen_files_checked':len(frozen),'theory_files_metadata_only':44,'literal_blocks':len(blocks),'generated_bytes':total,'largest_generated':largest,'manifest':manifest_counts,'shared_outputs':shared_identities,'errors':errors,'passed':not errors}
    if not args.no_write:(P/'validation.json').write_text(json.dumps(result,indent=1)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='shared_outputs'}))
    return bool(errors)

if __name__=='__main__':raise SystemExit(main())
