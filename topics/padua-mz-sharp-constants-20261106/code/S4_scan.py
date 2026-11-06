#!/usr/bin/env python3
"""Authorized raw CC scan, or selective high-precision validation. No fits."""
import argparse,datetime,hashlib,importlib.util,json,os,platform,resource,sys,time
from pathlib import Path
import numpy as np
import scipy
import mpmath as mp
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
spec=importlib.util.spec_from_file_location('structured_frozen',HERE/'S4_structured.py');structured=importlib.util.module_from_spec(spec);spec.loader.exec_module(structured)
SEED=20261106
THREADS=['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def high_precision(N):
 mp.mp.dps=75;extrema=[]
 def moment(k):return mp.mpf(0) if k%2 else mp.mpf(2)/(1-k*k)
 def qmoment(k):return moment(k if k<=N else 2*N-k)
 for parity in [0,1]:
  idx=list(range(parity,N,2));T=mp.matrix([[(moment(i+j)+moment(abs(i-j)))/2 for j in idx] for i in idx]);Q=mp.matrix([[(qmoment(i+j)+qmoment(abs(i-j)))/2 for j in idx] for i in idx]);L=mp.cholesky(T);Li=L**-1;B=Li*Q*Li.T;B=(B+B.T)/2
  vals=mp.eigsy(B,eigvals_only=True);extrema.append([vals[0],vals[len(idx)-1]])
 return min(x[0] for x in extrema),max(x[1] for x in extrema)
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--suite',choices=['high-precision','scan'],required=True);ap.add_argument('--output',type=Path,required=True);ap.add_argument('--selected-N',type=int,nargs='*');args=ap.parse_args()
 files=[Path(__file__),HERE/'S4_structured.py',HERE.parent/'S4-scan-proposal.json']
 code_hashes={str(p.relative_to(ROOT)):sha(p) for p in files}
 r=dict(status='MEASURED',fits_executed=False,pin='2143ad622fa98faf8fe7d5cb8ed2bb7e0062f861',preregistration_commit='e2652c344819ba47621d3e19912dc0c376abd9ca',command=sys.argv,started_utc=utc(),python=sys.version,numpy=np.__version__,scipy=scipy.__version__,mpmath=mp.__version__,platform=platform.platform(),threads={k:os.getenv(k) for k in THREADS},code_and_proposal_sha256=code_hashes,seed=SEED,tol=2e-12,ncv=40,maxiter=3000,inverse_residual_guard=1e-9,constraint_guard=1e-9,results=[])
 tick=time.monotonic()
 def save():
  r['elapsed_seconds']=time.monotonic()-tick;r['peak_rss_kib']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss;args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(r,indent=2,allow_nan=False)+'\n')
 grid=json.loads(files[-1].read_text());Ns=[20,40] if args.suite=='high-precision' else [N for pair in zip(grid['even_N'],grid['odd_N']) for N in pair]
 if args.selected_N:
  assert args.suite=='scan';Ns=args.selected_N
 for N in Ns:
  start=utc();row=structured.solve(N);row.update(started_utc=start,code_and_proposal_sha256=code_hashes,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
  checks=[np.isfinite(x['eigenvalue']) and x['eigenvalue']>0 and x['inverse_residual_2_float']<=1e-9 and x['constraint_residual_float']<=1e-9 for x in row['results'].values()]
  row['guards_pass']=bool(all(checks));row['inverse_extrema_order_pass']=row['results']['minimum']['eigenvalue']<=row['results']['maximum']['eigenvalue']
  if args.suite=='high-precision':
   before=time.monotonic();ref=high_precision(N);row['mpmath_dps']=75;row['high_precision_seconds']=time.monotonic()-before;row['reference_extrema_75digit']=[mp.nstr(x,70) for x in ref];row['high_precision_max_relative_error']=float(max(abs(mp.mpf(row['results'][k]['eigenvalue'])/v-1) for k,v in zip(['minimum','maximum'],ref)));row['high_precision_pass_1e10']=row['high_precision_max_relative_error']<=1e-10
  r['results'].append(row);save();print('completed N',N,'guards',row['guards_pass'],'seconds',row['seconds'],flush=True)
  if not row['guards_pass'] or not row['inverse_extrema_order_pass'] or not row.get('high_precision_pass_1e10',True):
   r['completed']=False;r['failure_N']=N;save();raise RuntimeError('Numerical guard failed; no acceptance or continuation.')
 r['completed']=True;save()
if __name__=='__main__':main()
