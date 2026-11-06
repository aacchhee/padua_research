#!/usr/bin/env python3
"""Exact pre-registered K1 SVD fit; no alternate fitting model or extension."""
import argparse,datetime,hashlib,json,platform,sys
from pathlib import Path
import numpy as np
from S4_fit_inputs import load as load_fit_input
PIN_RAW='7ce16e5c61fb82fe1fc4125bbd9570fdc7579db7aa139cd116b4807322f500f2'
HERE=Path(__file__).resolve().parent
PROPOSAL=HERE.parent/'S4-scan-proposal.json'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--raw',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
 raw,input_receipt=load_fit_input(args.raw);assert not raw['fits_executed'];grid=json.loads(PROPOSAL.read_text());lookup={r['N']:r for r in raw['results']};out={}
 for parity,offset in [('even',0),('odd',1)]:
  windows={}
  for key,base in grid['K1_windows'].items():
   Ns=np.array([x+offset for x in base],dtype=int);values=np.array([lookup[int(n)]['results']['minimum']['eigenvalue'] for n in Ns]);ell=np.log(Ns);X=np.column_stack([np.ones(len(Ns)),np.log(ell)/ell,1/ell]);y=ell*ell*values;beta,resids,rank,singular=np.linalg.lstsq(X,y,rcond=None);error=y-X@beta
   windows[key]=dict(Ns=Ns.tolist(),coefficient_names=['c','a','b'],coefficients=beta.tolist(),singular_values=singular.tolist(),design_condition_2=float(singular[0]/singular[-1]),rank=int(rank),residual_rms=float(np.sqrt(np.mean(error*error))),residual_max_abs=float(np.max(abs(error))),observed_y=y.tolist(),fit_residuals=error.tolist())
  cs=[x['coefficients'][0] for x in windows.values()];difference=abs(cs[0]-cs[1])/max(abs(cs[0]),abs(cs[1]));out[parity]=dict(windows=windows,c_relative_disagreement=difference,positive_intercepts=all(c>0 for c in cs),K1_pass=bool(all(c>0 for c in cs) and difference<=.02))
 passed=all(v['K1_pass'] for v in out.values());report=dict(status='MEASURED',fit_authorization='coordinator after S1 prediction commit977c07ae193f981b8d151fa766fdcfa3f19ee8ff',preregistration_commit='e2652c344819ba47621d3e19912dc0c376abd9ca',started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),command=sys.argv,python=sys.version,numpy=np.__version__,platform=platform.platform(),script_sha256=sha(__file__),proposal_sha256=sha(PROPOSAL),fit_input_receipt=input_receipt,raw_receipt={'sha256':PIN_RAW,'bytes':55192},fit_model=grid['fit'],results=out,K1_verdict='PASS' if passed else 'INCONCLUSIVE',extension_executed=False,K2_comparison='not evaluated because K1 did not pass')
 if passed:
  model=float(np.pi**4/8);cs={p:v['windows']['B_j15_to20']['coefficients'][0] for p,v in out.items()};delta={p:abs(c-model)/model for p,c in cs.items()};report['K2_comparison']=dict(model='pi^4/8, both N parities',model_value_float=model,measured_final_window_intercepts=cs,relative_model_disagreements=delta,verdict='PASS' if all(d<=.05 for d in delta.values()) else 'KILL_MODEL')
 args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':main()
