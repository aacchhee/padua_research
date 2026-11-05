#!/usr/bin/env python3
"""Post hoc exact Rayleigh diagnostic of envelope plus fixed-old-BJ-lower route.
This does not lower-bound the actual scalar capacity or kill the L4 target.
"""
import argparse,gzip,hashlib,json,pathlib,platform,sys,time
import flint
from flint import fmpq as Q,fmpq_mat as Mat
ENVELOPE_CODE='0da27e69ddd3cff5ca23e3fcac764f53891ad164ffab20324540fd67d2faf901'
LOWER_PIN='fae9c8743c78230ef0aa82c185d1efe0eee37be066982a37d39d920af95719f0'
def sha(p):
 h=hashlib.sha256()
 with open(p,'rb') as f:
  for x in iter(lambda:f.read(1048576),b''):h.update(x)
 return h.hexdigest()
def ident(p):return {'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)}
def checked_artifact(info):
 p=pathlib.Path(info['path']);assert p.stat().st_size==info['bytes'] and sha(p)==info['sha256'];return p
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--upper-receipt',required=True);ap.add_argument('--frozen-evidence',required=True);ap.add_argument('--output-dir',required=True);ap.add_argument('--receipt',required=True);a=ap.parse_args()
 start=time.monotonic();out=pathlib.Path(a.output_dir);out.mkdir(parents=True,exist_ok=False)
 upath=pathlib.Path(a.upper_receipt);upper=json.loads(upath.read_text());assert upper['code_sha256']==ENVELOPE_CODE and upper['old_frobenius_exactly_reproduced'] and upper['scope']['all_source_columns']==90
 ep=checked_artifact(upper['envelope'])
 with gzip.open(ep,'rt') as f:
  h=json.loads(next(f));rows=[json.loads(line) for line in f]
 assert h['schema']=='full-envelope-v1' and h['rows']==91 and h['nodes']==625 and h['sources']==list(range(1,91))
 assert [r['k'] for r in rows]==list(range(91)) and all(len(r['values'])==625 for r in rows)
 d=[Q(x) for x in h['d']];values=[[Q(x) for x in r['values']] for r in rows]
 assert len(d)==91 and min(d)>0 and all(x>=0 for row in values for x in row) and values[0]==[Q(0)]*625
 S=Mat(values)
 lp=pathlib.Path(a.frozen_evidence)/'e1-multinode-certificates.json';assert sha(lp)==LOWER_PIN
 lower=json.loads(lp.read_text());old=next(x for x in lower['witnesses'] if x['set']=='rotated' and x['rule']=='bj')
 assert old['degree']==12 and old['target_column']==90;G=Q(old['explicit_greedy_sign_lower_squared']['exact'])
 res=[]
 for step in [3,8]:
  summary=next(x for x in upper['candidates'] if x['step']==step);cp=checked_artifact(summary['candidate']);c=json.loads(cp.read_text());v=c['v']
  assert len(v)==625 and min(v)>0 and all(isinstance(x,int) for x in v)
  w=S*Mat([[x] for x in v]);R=sum((w[k,0]**2/d[k] for k in range(91)),Q(0))/sum(x*x for x in v)
  L=int(R.numerator)//int(R.denominator);assert L<=R<L+1
  exact=out/('rayleigh-%02d-exact.txt'%step);exact.write_text(str(R)+'\n')
  res.append({'candidate':step,'candidate_input':ident(cp),'rayleigh_float_display':float(R),'rayleigh_integer_lower':L,'integer_lower_exactly_checked':True,'exact_100lower_ge_frozen_G':bool(100*L>=G),'exact_rayleigh':ident(exact)})
 receipt={'result':'FIXED_OLD_LOWER_ENVELOPE_ROUTE_CANNOT_PASS' if all(x['exact_100lower_ge_frozen_G'] for x in res) else 'NO_ROUTE_OBSTRUCTION_CERTIFIED','label':'POST_HOC_ENVELOPE_DIAGNOSTIC_ONLY','rules_head':'684849d7d19ac2604213ae3d4f499d3436f58b3d','code_sha256':sha(__file__),'envelope_producer_source_sha256':ENVELOPE_CODE,'upper_receipt':ident(upath),'envelope_input':ident(ep),'frozen_BJ_lower_input':ident(lp),'checks':res,'command':[sys.executable,'-B',str(pathlib.Path(__file__).resolve()),*sys.argv[1:]],'runtime':{'python':platform.python_version(),'python_flint':flint.__version__,'elapsed_seconds':time.monotonic()-start},'limits':['This lower-bounds the nonnegative envelope eigenvalue, not the actual formal scalar capacity.','Obstruction applies only to a valid upper on this same envelope combined with the fixed old BJlower.','True factor-ten capacity target remains undecided; stronger lower witnesses or sharper non-envelope uppers remain possible.','Post hoc diagnostic executed after all nine preregistered vector uppers failed.','Developer execution; distinct independent verification remains separate.'],'retention':'Exact Rayleigh rationals remain temporary outsideGit with hashes; archive/delivery pending prescribed cold-storage process.'}
 pathlib.Path(a.receipt).write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt['checks'],indent=2),flush=True)
if __name__=='__main__':main()
