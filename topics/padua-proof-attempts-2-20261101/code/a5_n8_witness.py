"""Standalone strict-interior-maxima lower-bound witnesses; no completeness claim."""
import argparse,hashlib,json,os,tempfile,time,platform
from pathlib import Path

MAIN_SHA='a9cff5748d6c40ee41ac76e4e8a0035e0d5dab95f4de1233dfcc26902cb085a2'
CONTROL_SHA='7f57ed9ba5ad864391aa2e309834d9b61c33f673a6854247d44594cb10ec71d2'
def sha(raw):return hashlib.sha256(raw).hexdigest()
def canonical(data):return json.dumps(data,separators=(',',':'),sort_keys=True).encode()
def atomic(path,raw):
 path=Path(path)
 if path.exists():
  if path.read_bytes()!=raw:raise ValueError('refusing to replace different witness output')
  return
 temporary=None
 try:
  with tempfile.NamedTemporaryFile(mode='wb',dir=path.resolve().parent,prefix=path.name+'.',delete=False)as f:
   temporary=f.name;f.write(raw);f.flush();os.fsync(f.fileno())
  os.replace(temporary,path);temporary=None
 finally:
  if temporary is not None:os.unlink(temporary)
def run(path,input_sha,driver_sha):
 started=time.monotonic();folder=Path(__file__).resolve().parent;main=folder/'a5_checker_n8.py';control=folder/'a5_checker_n8_controls.py'
 own=sha(Path(__file__).read_bytes())
 if own!=driver_sha or sha(main.read_bytes())!=MAIN_SHA or sha(control.read_bytes())!=CONTROL_SHA:raise ValueError('wrong driver/frozen checker hash')
 import a5_checker_n8 as check
 check.require(check.SOURCE_SHA_AT_IMPORT==MAIN_SHA,'imported main source identity mismatch')
 raw=Path(path).read_bytes();check.require(sha(raw)==input_sha,'raw input hash mismatch')
 data=json.loads(check.decode_payload(raw),object_pairs_hook=check.unique_object)
 check.require(data.get('format')in('a5-n8-spatial-v1','a5-n8-interior-witnesses-v1')and type(data.get('n'))is int and data['n']==8 and type(data.get('precision'))is int and data['precision']==160,'unsupported witness input')
 records=data['interior_roots'];check.require(type(records)is list and records,'nonempty root witness list required')
 proof={'field_embedding':data['field_embedding'],'interior_roots':records};proof_bytes=canonical(proof)
 verifier=check.Verifier(data['field_embedding'])
 for record in records:verifier.root(record)
 bound=len(verifier.roots);check.require(bound==len(records),'witness count mismatch')
 if data['format']=='a5-n8-interior-witnesses-v1':check.require(type(data.get('observed_lower_bound'))is int and data['observed_lower_bound']==bound,'standalone witness bound mismatch')
 check.require(canonical(proof)==proof_bytes,'input witness data mutated')
 check.require(sha(Path(__file__).read_bytes())==own and sha(main.read_bytes())==MAIN_SHA and sha(control.read_bytes())==CONTROL_SHA,'source changed during witness replay')
 return {'format':'a5-n8-interior-witnesses-v1','n':8,'precision':160,**proof,
  'observed_lower_bound':bound,'lower_bound_certified':True,'completeness_certified':False,'global_maximum_certified':False,
  'scope':'at least the observed number of distinct strict local maxima in the OPEN physical square; no completeness, edge/corner or global claim',
  'metadata':{'input_path':str(path),'input_sha256':input_sha,'input_bytes':len(raw),'driver_sha256':own,'checker_sha256':MAIN_SHA,'controls_sha256':CONTROL_SHA,'sources_unchanged':True,
   'mathematical_witness_payload_sha256':sha(proof_bytes),'field_checks':verifier.embedding_result,'python':platform.python_version(),'sympy':check.sp.__version__,'python_flint':check.flint.__version__,'FLINT':check.flint.__FLINT_VERSION__,'seconds':time.monotonic()-started}}
if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('input');parser.add_argument('--input-sha256',required=True);parser.add_argument('--driver-sha256',required=True);parser.add_argument('--output',required=True);args=parser.parse_args()
 result=run(args.input,args.input_sha256,args.driver_sha256);atomic(args.output,json.dumps(result,indent=2,sort_keys=True).encode()+b'\n')
 print(json.dumps({'observed_lower_bound':result['observed_lower_bound'],'lower_bound_certified':True,'completeness_certified':False,'output_sha256':sha(Path(args.output).read_bytes()),'seconds':result['metadata']['seconds']}),flush=True)
