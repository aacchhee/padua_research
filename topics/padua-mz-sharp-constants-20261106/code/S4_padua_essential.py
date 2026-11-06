#!/usr/bin/env python3
"""Compact signed-Padua measurement receipt from actual guarded run files."""
import argparse,hashlib,json
from pathlib import Path
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--inputs',type=Path,nargs='+',required=True);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args();cases={};sources=[];meta=[]
 for p in a.inputs:
  r=json.loads(p.read_text());sources.append(dict(path=str(p),sha256=sha(p),bytes=p.stat().st_size,completed=r.get('completed',False),running_degree=r.get('running_degree')))
  env={k:r[k] for k in ['script_sha256','operator_sha256','frozen_code_sha256','proposal_sha256','python','numpy','scipy','platform','threads','preregistration_commit']}
  if env not in meta:meta.append(env)
  for x in r['results']:
   assert x['extreme'] in ['minimum','maximum'];key=str(x['m']);row=cases.setdefault(key,dict(m=x['m'],n=x['n'],dimension=x.get('dimension'),weight_sum=x.get('weight_sum'),negative_weight_count=x.get('negative_weight_count'),negative_weight_mass=x.get('negative_weight_mass')));assert x['extreme'] not in row,'Duplicate case/extreme input, do not silently replace.'
   row[x['extreme']]={k:x[k] for k in ['status','seed','ncv','tol','matvec_cap','wall_cap_seconds','matvecs','seconds','cpu_seconds','peak_rss_kib']};row[x['extreme']].update({k:x[k] for k in ['value','residual_2_float','residual_guard_pass','error_type','error'] if k in x})
 out=dict(status='MEASURED',format='S4-essential-Padua-v1',generator_sha256=sha(__file__),source_receipts=sources,run_environments=meta,rows=[cases[k] for k in sorted(cases,key=int)],total_completed_cpu_seconds=sum(v.get('cpu_seconds',0) for row in cases.values() for k,v in row.items() if k in ['minimum','maximum']),limitation='Finite float spectra and residuals only, no enclosures or asymptotic theorem. Incomplete upper pilot is never an accepted extremum.')
 content=json.dumps(out,separators=(',',':'),allow_nan=False)+'\n';assert len(content.encode())<16384,'Keep full raw offGit; do not split output to evade limits.';a.output.write_text(content);print('essential rows',len(cases),'bytes',len(content.encode()),'cpu',out['total_completed_cpu_seconds'])
if __name__=='__main__':main()
