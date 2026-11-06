#!/usr/bin/env python3
"""Pre-registered K3 finite upper-spectrum fit. No model norm comparison."""
import argparse,datetime,hashlib,json,platform,sys
from pathlib import Path
import numpy as np
from S4_fit_inputs import load as load_fit_input
HERE=Path(__file__).resolve().parent
PROPOSAL=HERE.parent/'S4-scan-proposal.json'
RAW_HASH='7ce16e5c61fb82fe1fc4125bbd9570fdc7579db7aa139cd116b4807322f500f2'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--raw',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);args=ap.parse_args();raw,input_receipt=load_fit_input(args.raw);assert raw['completed'];assert all(r['guards_pass'] and r['inverse_extrema_order_pass'] for r in raw['results']);lookup={r['N']:r for r in raw['results']};grid=json.loads(PROPOSAL.read_text());out={}
 for parity,offset in [('even',0),('odd',1)]:
  windows={}
  for label,base in grid['K1_windows'].items():
   Ns=np.array([x+offset for x in base]);nref=int(Ns[0]);z=(nref/Ns)**2;X=np.column_stack([np.ones(len(Ns)),z,z*np.log(Ns/nref)]);scale=np.linalg.norm(X,axis=0);scaled=X/scale;y=np.array([lookup[int(n)]['results']['maximum']['eigenvalue']-1 for n in Ns]);gamma,resids,rank,singular=np.linalg.lstsq(scaled,y,rcond=None);beta=gamma/scale;error=y-X@beta;limit=1+beta[0];threshold=1e-7 if label.startswith('A') else 1e-8
   windows[label]=dict(Ns=Ns.tolist(),Nref=nref,coefficient_names=['c0','a','b'],coefficients=beta.tolist(),fitted_limit=float(limit),column_scales=scale.tolist(),scaled_singular_values=singular.tolist(),scaled_condition_2=float(singular[0]/singular[-1]),rank=int(rank),residual_rms=float(np.sqrt(np.mean(error*error))),max_absolute_residual=float(np.max(abs(error))),residual_threshold=threshold,window_usable=bool(rank==3 and np.max(abs(error))<=threshold),observed_lambda_max_minus1=y.tolist(),fit_residuals=error.tolist())
  limits=[x['fitted_limit'] for x in windows.values()];difference=abs(limits[0]-limits[1]);out[parity]=dict(windows=windows,absolute_intercept_window_difference=difference,window_agreement_pass=bool(difference<=1e-6))
 final=[v['windows']['B_j15_to20']['fitted_limit'] for v in out.values()];parity_difference=abs(final[0]-final[1]);usable=bool(parity_difference<=1e-6 and all(v['window_agreement_pass'] and all(w['window_usable'] for w in v['windows'].values()) for v in out.values()))
 report=dict(status='MEASURED',preregistration_commit='18992e1e159ff0f8af3b8b235e837e14ca9a6c2f',fit_model='lambda_max-1=c0+a(Nref/N)^2+b(Nref/N)^2 log(N/Nref); columns scaled to unit2norm, unweighted SVD',started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),command=sys.argv,python=sys.version,numpy=np.__version__,platform=platform.platform(),script_sha256=sha(__file__),proposal_sha256=sha(PROPOSAL),fit_input_receipt=input_receipt,raw_receipt={'sha256':RAW_HASH,'bytes':55192},results=out,final_window_absolute_parity_difference=parity_difference,parity_agreement_pass=bool(parity_difference<=1e-6),numerical_fit_usability='USABLE' if usable else 'INCONCLUSIVE',K3_model_comparison='PENDING S2 model norm estimate; no comparison executed',alternate_fits_executed=False)
 args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':main()
