"""Identity checks and compact summaries for the focused L2 audit."""
from pathlib import Path
import hashlib, json, platform, subprocess, sys
import numpy as np
import scipy

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
BASE = '5f523313b7b388cb114103734028f0a850dfeaad'
CAND = '075d4074017445a0fd4d7443ffac97cd7f8c106b'
HEAD = '50b0d304001b48607527e5086a67045f534d9472'
TOP = 'topics/bivariate-lanczos-20261031'

def git(*args):
    return subprocess.check_output(['git',*args],cwd=ROOT)

def digest(data):
    return hashlib.sha256(data).hexdigest()

def ident(rel):
    b=(ROOT/rel).read_bytes()
    return dict(path=rel,size=len(b),sha256=digest(b))

frozen=git('ls-tree','-r','--name-only',BASE,'--',f'{TOP}/audit-01.md',f'{TOP}/audit-01',f'{TOP}/audit-handoff.md').decode().splitlines()
unchanged=['state/IDEAS.md','literature/INDEX.md']
unchanged+=git('ls-tree','-r','--name-only',BASE,'--','tracks/bivariate-lanczos/code/L2','tracks/bivariate-lanczos/code/review_L2').decode().splitlines()
unchanged+=['tracks/bivariate-lanczos/code/L1/l1_recurrence.py','tracks/bivariate-lanczos/code/L1/l1_r04_checkerboard.py']
identity=[]
for rel in sorted(set(frozen+unchanged)):
    old=git('show',f'{BASE}:{rel}')
    now=(ROOT/rel).read_bytes()
    assert old==now, rel
    identity.append(ident(rel)|dict(baseline_sha256=digest(old)))

source=['AGENTS.md','agents/WORKFLOW.md','agents/codex/CODEX.md','state/IDEAS.md','literature/INDEX.md']
source += [f'{TOP}/{f}' for f in ['response-01.md','SPLITS.md','report.md','plan.md']]
source += [str(p.relative_to(ROOT)) for p in (ROOT/TOP/'directions/L2').glob('*.md')]
source += [str(p.relative_to(ROOT)) for p in (ROOT/TOP/'directions/L2/logs').glob('audit01_*')]
source += [str(p.relative_to(ROOT)) for p in (ROOT/'tracks/bivariate-lanczos/code/L2').glob('*.py')]
for p in (ROOT/'tracks/bivariate-lanczos/theory').glob('*.md'):
    first=p.read_text().splitlines()[0]
    if any(f'bivariate-lanczos-claude-{n} ' in first for n in range(201,211)):
        source.append(str(p.relative_to(ROOT)))
source=sorted(set(source))
source_ids=[]
for rel in source:
    cand=git('show',f'{CAND}:{rel}')
    now=(ROOT/rel).read_bytes()
    same=cand==now
    if not same:
        assert rel == f'{TOP}/response-01.md', rel
        assert now==git('show',f'{HEAD}:{rel}')
    source_ids.append(ident(rel)|dict(candidate_git_blob=git('rev-parse',f'{CAND}:{rel}').decode().strip(),
                                     candidate_sha256=digest(cand),identical_to_candidate=same))

def rows(filename):
    return [json.loads(s[5:]) for s in (HERE/filename).read_text().splitlines() if s.startswith('JSON ')]

ld=rows('ldnorm-rerun.log')
assert len(ld)==24
assert all(r['control_bitwise'] for r in ld)
bench={}
for r in ld:
    bench.setdefault(r['bench'],{})[r['variant']]=r
ldsummary={}
for name, variants in bench.items():
    degrees=[16,20] if name=='triangle' else [20,24]
    ldsummary[name]=dict(ratios_double_over_ldn={n:variants['double']['L'][n]/variants['ldn']['L'][n] for n in degrees},
                         final_lb={v:r['thetaLB'][-1] for v,r in variants.items()},
                         max_ldn_loss=max(variants['ldn']['L']))
chi=rows('chi-rerun.log')
assert len(chi)==24
chisummary=[dict(bench=r['bench'],run=r['run'],max_chi=max(p['chi'] for p in r['prof']),
                 max_L_over_sqrtu=max(p['L'] for p in r['prof'])/np.sqrt(2.**-53),
                 final_eta=r['prof'][-1]['eta']) for r in chi]
pro=[r for r in chisummary if r['run']=='proJ']
summary=dict(ldnorm=ldsummary,chi=chisummary,max_chi=max(r['max_chi'] for r in chisummary),
             proJ_strict_pass=int(sum(r['max_L_over_sqrtu']<=1 for r in pro)),
             proJ_registered_pass=int(sum(r['max_L_over_sqrtu']<=10 for r in pro)),
             prior_audit_files_unchanged=len(frozen),old_producer_and_catalog_files_unchanged=len(set(unchanged)))
(HERE/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
manifest=dict(audit_baseline=BASE,scientific_candidate=CAND,rules_execution_head=HEAD,
              model='gpt-6-astra',effort='xhigh',model_metadata='prior explicit launch; no independent runtime metadata exposed',
              environment=dict(python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__,machine=platform.machine(),
                               unit_roundoff=float(np.finfo(float).epsneg),longdouble_unit_roundoff=float(np.finfo(np.longdouble).epsneg),
                               OMP_NUM_THREADS=1,OPENBLAS_NUM_THREADS=1),
              unchanged_against_audit_baseline=identity,source_inputs=source_ids,
              outputs=[ident(str(p.relative_to(ROOT))) for p in sorted(HERE.iterdir()) if p.is_file() and p.name!='manifest.json'],
              retention='Small necessary local audit evidence; no external archive; root owns Git and retention.')
(HERE/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps(dict(inputs=len(source_ids),frozen_unchanged=len(frozen),old_sources_unchanged=len(set(unchanged)),
                      max_chi=summary['max_chi'],strict_pass=summary['proJ_strict_pass'],registered_pass=summary['proJ_registered_pass'],
                      artifact_bytes=sum(p.stat().st_size for p in HERE.iterdir() if p.is_file()))))
