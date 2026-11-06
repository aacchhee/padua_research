#!/usr/bin/env python3
"""Small pinned replay manifest for all completed T9 round06 mechanisms."""
import argparse,hashlib,json,platform,sys
from pathlib import Path
import numpy as np
import scipy,sympy
TOP=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args();rows=[]
 for name in ('qr','localdet','weights','unbalanced','exact','snapshots','t10-owner','controls','complement'):
  f=TOP/f'evidence/t9-r06-{name}.json';d=json.loads(f.read_text());assert f.stat().st_size<16384
  if name in ('qr','localdet'):
   argv=['python','-I',str((TOP/'code/t9_r06_maxima.py').relative_to(TOP.parents[1])),'--family',name,'--scratch',d['scratch'],'--output',str(f.relative_to(TOP.parents[1]))]
  else:argv=['python','-I']+d['command']
  source=TOP/'code'/({'qr':'t9_r06_maxima.py','localdet':'t9_r06_maxima.py','weights':'t9_r06_weights.py','unbalanced':'t9_r06_unbalanced.py','exact':'t9_r06_exact.py','snapshots':'t9_r06_snapshots.py','t10-owner':'t9_r06_t10_owner.py','controls':'t9_r06_controls.py','complement':'t9_r06_complement.py'}[name]);assert sha(source)==d['code_sha256']
  for helper,value in d.get('helpers',{}).items():assert sha(TOP/'code'/helper)==value
  rows.append({'receipt':str(f.relative_to(TOP)),'sha256':sha(f),'bytes':f.stat().st_size,'argv':argv,'source_code_matches':True,'helper_hashes_match':True})
 sources=list((TOP/'literature-round06').glob('t9-*.md'));theory=list((TOP/'theory').glob('t9-r06-*.md'));owned=[TOP/'attempts/T9-round06.md',TOP/'literature-T9-round06.md',TOP/'novelty-gate-T9-round06.md',TOP/'preregistration-T9-round06.md']+sources+theory
 out={'schema':'t9-r06-manifest-v1','status':'replay receipt; mathematical and measured statuses remain in individual records','rules_sha':'7afa6a54a4db4652267e38cd48658ba435d20481','command':sys.argv,'code_sha256':sha(__file__),'seed':0,'versions':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,'sympy':sympy.__version__},'cwd':'/workspace/padua_research','environment':{'OPENBLAS_NUM_THREADS':'1','OMP_NUM_THREADS':'1'},'receipts':rows,'record_sha256':{str(f.relative_to(TOP)):sha(f) for f in owned},'raw_policy':'regenerate-only; pass a fresh unique --scratch directory to replay commands, never reuse a concurrent worker directory; raw optimizer initials/finals and NPY nodes are not theorem evidence','primary_source_policy':'source record hashes pin statements/coverage/URLs; PDFs accessed through WEB and no local PDF byte hash is claimed','replay_policy':'numeric timings may differ; compare scientific values/guards/node hashes, not elapsed time. T8/T10 input owners must remain frozen at the hashes in snapshots.'}
 text=json.dumps(out,separators=(',',':'))+'\n';assert len(text.encode())<16384;a.output.write_text(text)
if __name__=='__main__':main()
