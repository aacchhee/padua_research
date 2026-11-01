"""Independent read-only registry audit; isolated allocator rerun uses temporary copies.
Run from repo root. No imports of the developer's checker or allocator functions.
"""
from pathlib import Path
from collections import Counter
import hashlib, json, re, shutil, subprocess, sys, tempfile

ROOT = Path.cwd()
T = Path('topics/bivariate-lanczos-20261031')
OUT = T / 'audit-04/registries'
MAIN = '9739a0c56b7a3976422ce60a8441bfbbfd6554df'
SCIENCE = 'cf01449fc96233c9074ce25efcb056535414aa1d'
P = 'bivariate-lanczos-claude'
def git_text(rev, path):
    return subprocess.check_output(['git','show',f'{rev}:{path}'], text=True)
def splitrow(line):
    return [x.strip() for x in re.split(r'(?<!\\)\|',line.strip())[1:-1]]
def table(text, pattern):
    return [splitrow(l) for l in text.splitlines() if re.match(pattern,l)]
def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()
rep = {'head':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),
       'main':MAIN, 'science':SCIENCE, 'python':sys.version, 'structural_failures':[]}
def check(name, actual, expected):
    if actual != expected:
        rep['structural_failures'].append({'check':name,'actual':actual,'expected':expected})
data=json.loads((T/'pr-prep/id-map.json').read_text()); M=data['map']
inventory={}; files={}
for f in sorted(Path('tracks/bivariate-lanczos/theory').glob('*.md')):
    prov=re.search(r'PD-[TN]\?'+P+r'-\d{3}', f.read_text().splitlines()[0]).group()
    check('one theory per provisional '+prov, prov in files, False)
    files[prov]=str(f); inventory[prov]='theory'
for f in sorted((T/'directions').glob('*/candidates.md')):
    for p in re.findall(r'^#{2,3} (IDEA\?'+P+r'-\d{3})\b',f.read_text(),re.M):
        inventory[p]='candidate'
for p in re.findall(r'^\| (IDEA\?'+P+r'-0\d\d)\b',(T/'baseline-candidates.md').read_text(),re.M):
    inventory[p]='seed'
science_lit=set(re.findall(r'^\| (LIT\?'+P+r'-\d{3})\b',git_text(SCIENCE,'literature/INDEX.md'),re.M))
current_lit=set(re.findall(r'^\| LIT-\d{3} \((LIT\?'+P+r'-\d{3})\)',Path('literature/INDEX.md').read_text(),re.M))
rep['literature_inventory_note']={'accepted_science':len(science_lit),'current':len(current_lit),
 'added_during_preparation':len(current_lit-science_lit),'removed':sorted(science_lit-current_lit),
 'limit':'Literature additions and reading coverage are audited by the other assigned agent.'}
for p in current_lit:
    inventory[p]='literature'
check('complete inventory',sorted(M),sorted(inventory))
check('unique final values',len(set(M.values())),len(M))
check('theory file map',data['theory_files'],files)
rep['inventory_counts']=dict(Counter(inventory.values()))
rep['map_count']=len(M)
expected={'PD-T':(29,80),'PD-N':(7,31),'IDEA':(77,176),'LIT':(66,292)}
rep['ranges']={}
for ns,(lo,hi) in expected.items():
    values=sorted(v for k,v in M.items() if k.startswith(ns+'?'))
    desired=[f'{ns}{"-" if ns in ("IDEA","LIT") else ""}{n:03}' for n in range(lo,hi+1)]
    check('contiguous range '+ns,values,desired)
    rep['ranges'][ns]={'count':len(values),'min':values[0],'max':values[-1]}
ps=table(Path('PROOF_STATUS.md').read_text(),r'^\| PD-[TN]\d{3} \|')
ideas=table(Path('state/IDEAS.md').read_text(),r'^\| IDEA-\d{3} \|')
idx=table(Path('literature/INDEX.md').read_text(),r'^\| LIT-\d{3}\b')
cw=table(Path('ID_CROSSWALK.md').read_text(),r'^\| (?:PD-[TN]|IDEA|LIT)\?'+P+r'-\d{3} \|')
check('crosswalk bijection',Counter((r[0],r[1]) for r in cw),Counter(M.items()))
check('IDEA membership',sorted(r[0] for r in ideas if int(r[0][5:])>=77),sorted(v for k,v in M.items() if k.startswith('IDEA?')))
check('theory registry membership',sorted(r[0] for r in ps if r[0] in M.values()),sorted(v for k,v in M.items() if k.startswith(('PD-T?','PD-N?'))))
check('literature registry membership',sorted(re.match(r'LIT-\d{3}',r[0]).group() for r in idx if int(r[0][4:7])>=66),sorted(v for k,v in M.items() if k.startswith('LIT?')))
rep['main_rows']={}
for path,pattern in [('PROOF_STATUS.md',r'^\| PD-[TN]'),('state/IDEAS.md',r'^\| IDEA'),('literature/INDEX.md',r'^\| LIT'),('ID_CROSSWALK.md',r'^\| (?:PD-[TN]|IDEA|LIT)')]:
    old=[l for l in git_text(MAIN,path).splitlines() if re.match(pattern,l)]
    now=Counter(Path(path).read_text().splitlines())
    missing=[l for l,c in Counter(old).items() if now[l]<c]
    rep['main_rows'][path]={'count':len(old),'missing_or_changed':missing}
    check('main accepted rows '+path,missing,[])
neg=table(Path('tracks/bivariate-lanczos/NEGATIVE_RESULTS.md').read_text(),r'^\| PD-N\d{3}')
check('negative membership',sorted(re.match(r'PD-N\d{3}',r[0]).group() for r in neg),sorted(v for k,v in M.items() if k.startswith('PD-N?')))
for prov,f in files.items():
    hdr=re.findall(r'^Final ID: \*\*(PD-[TN]\d{3})\*\*',Path(f).read_text(),re.M)
    check('header '+prov,hdr,[M[prov]])
    source_status=re.search(r'Overall status:\s*\**([A-Z]+)',Path(f).read_text()).group(1)
    check('status '+prov,[r[2] for r in ps if r[0]==M[prov]],[source_status])
    # Scientific bodies should be unchanged apart from one allocation line and its blank.
    stripped=re.sub(r'\n\nFinal ID:[^\n]*\n','\n',Path(f).read_text(),count=1)
    check('science body '+prov,stripped==git_text(SCIENCE,f),True)
source_splits=table((T/'SPLITS.md').read_text(),r'^\| (?:PD-|—)')
final_splits=table(Path('ID_CROSSWALK.md').read_text().split('### Bivariate Lanczos original-to-split mappings')[1],r'^\| (?:PD-|—)')
def convert(s):
    return re.sub(r'(PD-T|PD-N|IDEA|LIT)\?(?:'+P+r'|…)-(\d{3})',lambda m:M[m[1]+'?'+P+'-'+m[2]],s)
check('split row count',len(final_splits),11)
for i,(a,b) in enumerate(zip(source_splits,final_splits),1):
    check('split row exact content '+str(i),[b[0],b[1],b[2],b[4]],[convert(x) for x in a])
rep['split_rows']=len(final_splits)
# Exercise the advertised generator on an isolated copy of the current prepared inputs.
# Temporary copy and generated outputs disappear automatically; main workspace is never mutated.
with tempfile.TemporaryDirectory(prefix='allocator-',dir=OUT) as td:
    copyroot=Path(td)
    paths=[T/'pr-prep/allocate.py',T/'baseline-candidates.md',Path('literature/INDEX.md')]
    paths+=list((T/'directions').glob('*/candidates.md'))+list(Path('tracks/bivariate-lanczos/theory').glob('*.md'))
    for f in paths:
        dest=copyroot/f; dest.parent.mkdir(parents=True,exist_ok=True); shutil.copyfile(f,dest)
    run=subprocess.run([sys.executable,'-I',str(T/'pr-prep/allocate.py')],cwd=copyroot,text=True,capture_output=True)
    after=json.loads((copyroot/T/'pr-prep/id-map.json').read_text())
    apply=subprocess.run([sys.executable,'-I',str(T/'pr-prep/allocate.py'),'--apply'],cwd=copyroot,text=True,capture_output=True)
    duplicate_headers=sum(len(re.findall(r'^Final ID:',(copyroot/f).read_text(),re.M))!=1 for f in files.values())
    rep['isolated_generator_rerun']={'dry_run_exit':run.returncode,'dry_run_stdout':run.stdout,
       'dry_run_stderr':run.stderr,'before_map_count':len(M),'after_map_count':len(after['map']),
       'lost_map_entries':len(set(M)-set(after['map'])),'after_counts':after['counts'],
       'apply_exit':apply.returncode,'apply_stdout':apply.stdout,'apply_stderr':apply.stderr,
       'files_with_duplicate_final_headers_after_apply':duplicate_headers}
tracked=['AGENTS.md','agents/WORKFLOW.md','agents/codex/CODEX.md','PROOF_STATUS.md','ID_CROSSWALK.md','state/IDEAS.md','literature/INDEX.md','tracks/bivariate-lanczos/NEGATIVE_RESULTS.md','topics/padua-batch-20261031/ALLOCATIONS.md']
tracked += [str(p) for p in (T/'pr-prep').glob('*') if p.is_file()]
tracked += [str(p) for p in (T/'directions').glob('*/candidates.md')]
tracked += [str(T/'SPLITS.md')]+list(files.values())
rep['source_sha256']={p:sha(p) for p in sorted(tracked)}
print(json.dumps(rep,indent=2,ensure_ascii=False))
sys.exit(bool(rep['structural_failures']))
