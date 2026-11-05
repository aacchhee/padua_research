#!/usr/bin/env python3
"""Prospective G2 R lower only: stage11/source6 allnodes, global90-source law."""
import argparse,hashlib,json,pathlib,platform,sys,time
import flint
from flint import fmpq as Q
SCREEN_PIN='2e8c87db119b407a884bc089a5a7e69addfc674b94ebc499236a18307ca1c57d'
def sha(p):return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def ident(p):return {'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--screen-receipt',required=True);ap.add_argument('--output-dir',required=True);ap.add_argument('--receipt',required=True);a=ap.parse_args();start=time.monotonic();out=pathlib.Path(a.output_dir);out.mkdir(parents=True,exist_ok=False)
 sp=pathlib.Path(a.screen_receipt);s=json.loads(sp.read_text());assert s['code_sha256']==SCREEN_PIN and s['scope']['degree']==12 and s['scope']['global_source_count']==90 and s['scope']['global_source_range']==[1,90]
 trial=next(x for x in s['screens'] if x['stage']==11 and x['source']==6);info=trial['artifact'];ip=pathlib.Path(info['path']);assert ip.stat().st_size==info['bytes'] and sha(ip)==info['sha256'];r=json.loads(ip.read_text())
 M=325 if s['scope']['set']=='triangle' else 625;X2=Q(1) if M==325 else Q(49,25)
 ell=[Q(v) for v in r['all_node_ell']];assert len(ell)==M and min(ell)>=0 and r['stage']==11 and r['source']==6 and Q(r['Xnorm_squared'])==X2 and r['direct_projected_pulse_exactly_agrees']
 denominator=90*M*X2;partial=sum(ell,Q(0))/denominator;L=int(partial.numerator)//int(partial.denominator);assert L<=partial<L+1
 raw=out/'partial-expectation-lower-exact.txt';raw.write_text(str(partial)+'\n')
 receipt={'result':'R_PARTIAL_LOWER_PASSES' if partial>=16 else 'R_PARTIAL_LOWER_INCONCLUSIVE','scope':{'set':s['scope']['set'],'degree':12,'stage':11,'source':6,'selected_node_count':M,'global_source_count':90,'global_source_law':'independent signs, u_hi=xi_hi/sqrt(90*M)','original_R_threshold':16,'role':'lower on full E12 only; not exact E12 or a subset-law expectation'},'source_screen':ident(sp),'source_impulse':ident(ip),'screen_code_sha256':SCREEN_PIN,'frozen_source_sha256':s['frozen_source_sha256'],'analytic_reduction_sha256':s['analytic_reduction_sha256'],'Xnorm_squared_exact':str(X2),'global_denominator_exact':str(denominator),'partial_lower_integer_floor':L,'partial_lower_display':float(partial),'exact_lower_ge_16':bool(partial>=16),'integer_floor_ge_16':bool(L>=16),'exact_partial_lower':ident(raw),'code_sha256':sha(__file__),'command':[sys.executable,'-B',str(pathlib.Path(__file__).resolve()),*sys.argv[1:]],'runtime':{'python':platform.python_version(),'python_flint':flint.__version__,'elapsed_seconds':time.monotonic()-start},'limits':['All omitted stage/source contributions are nonnegative under the full original law.','If this lower does not reach16, original R is inconclusive, not false.','No probability, actual IEEE, original PD-T055 or all-degree conclusion.','Developer arithmetic on screened exact data; independent reconstruction remains separate.','External artifacts are temporary working evidence; archive/delivery pending.']}
 pathlib.Path(a.receipt).write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps({'result':receipt['result'],'partial_lower_integer_floor':L}),flush=True)
if __name__=='__main__':main()
