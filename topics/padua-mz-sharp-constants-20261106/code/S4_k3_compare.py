#!/usr/bin/env python3
"""Operational measured K3 comparison with finite Galerkin model estimate."""
import argparse,hashlib,json,sys
from pathlib import Path
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--model',type=Path,required=True);ap.add_argument('--fit',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args();m=json.loads(a.model.read_text());f=json.loads(a.fit.read_text());assert f['numerical_fit_usability']=='USABLE';row=next(x for x in m['galerkin'] if x['J']==512);norm=row['lambda_max'];values={p:x['windows']['B_j15_to20']['fitted_limit'] for p,x in f['results'].items()};errors={p:abs(v-norm) for p,v in values.items()};r=dict(status='MEASURED',command=sys.argv,script_sha256=sha(__file__),inputs={'model':{'path':str(a.model),'sha256':sha(a.model)},'fit':{'path':str(a.fit),'sha256':sha(a.fit)}},model_estimate_kind='finite J512 Galerkin norm; unbounded infinite tail',model_estimate=norm,finite_CC_fitted_limits=values,absolute_discrepancies=errors,absolute_kill_threshold=1e-3,K3_operational_verdict='PASS' if all(x<=1e-3 for x in errors.values()) else 'KILL_MODEL',limitation='Measured operational comparison only. No certified full infinite model norm, no finite-to-model convergence theorem, no proof of the actual upper limit.');a.output.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
if __name__=='__main__':main()
