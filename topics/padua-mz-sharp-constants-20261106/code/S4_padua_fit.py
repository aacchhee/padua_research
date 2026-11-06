#!/usr/bin/env python3
"""Only registered signed-Padua two-window slope/K4/K5 measurements."""
import argparse,hashlib,json,sys
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent;PROPOSAL=HERE.parent/'S4-padua-proposal.json'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--essential',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args();data=json.loads(a.essential.read_text());p=json.loads(PROPOSAL.read_text());assert data['format']=='S4-essential-Padua-v1';assert all(x['proposal_sha256']==sha(PROPOSAL) for x in data['run_environments']);rows={r['m']:r for r in data['rows']};out={}
 for sign,proxy in [('minimum',-.1336),('maximum',.0456)]:
  parity_results={};needed=[m+off for key in ['window_A_even_m','window_B_even_m'] for m in p['grids'][key] for off in [0,1]];complete=all(m in rows and sign in rows[m] and rows[m][sign]['status']=='COMPLETED' and rows[m][sign]['residual_guard_pass'] for m in needed)
  if not complete:
   out[sign]=dict(status='INCONCLUSIVE',reason='Registered required rows incomplete or failed; no fit attempted.',K4='INCONCLUSIVE',K5='INCONCLUSIVE');continue
  for parity,off in [('even',0),('odd',1)]:
   fits={}
   for key in ['window_A_even_m','window_B_even_m']:
    Ms=np.array([m+off for m in p['grids'][key]]);vals=np.array([rows[int(m)][sign]['value'] for m in Ms]);assert all(rows[int(m)][sign]['seed']==20261106 for m in Ms);z=np.log(Ms/Ms[0]);X=np.column_stack([np.ones(len(Ms)),z]);scales=np.linalg.norm(X,axis=0);b,_,rank,s=np.linalg.lstsq(X/scales,vals,rcond=None);beta=b/scales;err=vals-X@beta;slope=float(beta[1]);span=float(np.log(Ms[-1]/Ms[0]));threshold=.01*abs(slope)*span+1e-7;expected_sign=slope<0 if sign=='minimum' else slope>0;condition=float(s[0]/s[-1]);valid=bool(rank==2 and condition<=100 and expected_sign and abs(slope)>=1e-4 and np.all(np.isfinite(beta)) and np.max(abs(err))<=threshold)
    fits[key]=dict(Ms=Ms.tolist(),mref=int(Ms[0]),intercept=float(beta[0]),slope=slope,rank=int(rank),column_scales=scales.tolist(),scaled_singular_values=s.tolist(),scaled_condition_2=condition,unscaled_condition_2=float(np.linalg.cond(X)),residual_rms=float(np.sqrt(np.mean(err*err))),max_absolute_residual=float(np.max(abs(err))),residual_threshold=threshold,fit_residuals=err.tolist(),observed_extrema=vals.tolist(),endpoint_contrast=float(vals[-1]-vals[0]),fitted_endpoint_contrast=slope*span,window_checks_pass=valid)
   slopes=[x['slope'] for x in fits.values()];drift=abs(slopes[0]-slopes[1])/max(abs(slopes[0]),abs(slopes[1]));parity_results[parity]=dict(windows=fits,relative_window_slope_drift=drift,stable=bool(drift<=.05 and all(x['window_checks_pass'] for x in fits.values())))
  stable=all(v['stable'] for v in parity_results.values());final={k:v['windows']['window_B_even_m']['slope'] for k,v in parity_results.items()};delta={k:abs(s-proxy)/abs(proxy) for k,s in final.items()};paritygap=abs(final['even']-final['odd'])/max(abs(final['even']),abs(final['odd']));out[sign]=dict(status='STABLE_REGISTERED_WINDOWS' if stable else 'INCONCLUSIVE',results=parity_results,finite_K128_heuristic_proxy=proxy,relative_proxy_discrepancies=delta if stable else None,K4=('KILL_HEURISTIC_PROXY' if any(x>.10 for x in delta.values()) else 'PASS_HEURISTIC_PROXY') if stable else 'INCONCLUSIVE',final_window_relative_parity_slope_difference=paritygap,K5=('MEASURED_WINDOW_PARITY_AGREEMENT' if paritygap<=.05 else 'MEASURED_WINDOW_PARITY_DISAGREEMENT') if stable else 'INCONCLUSIVE')
 r=dict(status='MEASURED',command=sys.argv,script_sha256=sha(__file__),essential_input=dict(path=str(a.essential),sha256=sha(a.essential)),proposal_sha256=sha(PROPOSAL),preregistration_commit='ec52c16569ea959dfe682fcd7985378a2ef1cd42',numpy=np.__version__,results=out,limitation='Registered finite-window slope stability only. Model proxies are uncertified finiteK128 approximants; no full operator-norm identification, actual spectral limit or true parity equality follows. No alternate fit executed.');text=json.dumps(r,indent=2,allow_nan=False)+'\n';assert len(text.encode())<16384;a.output.write_text(text);print(text)
if __name__=='__main__':main()
