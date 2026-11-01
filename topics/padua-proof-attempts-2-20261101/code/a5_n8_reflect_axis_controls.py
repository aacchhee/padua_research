"""Bounded actual-axis proposal controls; no complete count is accepted."""
import argparse,copy,gzip,hashlib,json,time
from fractions import Fraction
from pathlib import Path
import a5_n8_reflect_axis as m

def run(certificate,expected,fixture_path):
 start=time.monotonic();paths=[Path(m.__file__),Path(__file__)];before={str(p):hashlib.sha256(p.read_bytes()).hexdigest()for p in paths};m.guards()
 raw=Path(certificate).read_bytes();m.require(hashlib.sha256(raw).hexdigest()==expected,'actual capped input identity mismatch');data=json.loads(gzip.decompress(raw));selected=[]
 def add(row):
  if not any(v['path']==row['path']for v in selected):selected.append(copy.deepcopy(row))
 for kind in('all_gradient','node_cone'):add(next(r for r in data['leaves']if kind in r))
 for code in('root','hessian','gradient'):add(next(r for r in data['leaves']if'patterns'in r and any(p['code']==code for p in r['patterns'])))
 axis=[]
 for root in data['interior_roots']:
  lo,hi=map(Fraction,root['R'][0])
  if lo<=0<=hi:
   axis.append(root['id']);add(next(r for r in data['leaves']if any(p['code']=='root'and p['id']==root['id']for p in r.get('patterns',[]))))
 m.require(axis,'actual capped fixture must contain an axis-box case')
 fixture=copy.deepcopy(data);fixture['leaves']=selected
 out,receipt=m.propose(fixture,True)
 assert receipt['retained_axis_roots']==len(axis)and len(out['metadata']['axis_reuse'])==len(axis)
 assert all(row['same_mask']and row['full_stored_and_reflected_root_predicates']and Fraction(row['contraction_upper'])<1 for row in out['metadata']['axis_reuse'])
 assert not out['summary']['complete']and not out['summary']['interior_complete']
 negatives=[]
 def reject(name,case,fixture_only=True):
  try:m.propose(case,fixture_only)
  except ValueError:negatives.append(name);return
  raise AssertionError('unsupported axis proposal accepted: '+name)
 reject('actual-left-prefix-incomplete',data,False)
 bad=copy.deepcopy(fixture);bad['field_embedding']['a_interval']=['0','1'];reject('wrong-exact-field',bad)
 bad=copy.deepcopy(fixture);bad['metadata']['source_sha256']='0'*64;reject('wrong-input-source',bad)
 bad=copy.deepcopy(fixture);bad['interior_roots'][axis[0]]['C']=[['0','0'],['0','0']];reject('invalid-stored-preconditioner',bad)
 original=m.inject
 try:
  m.inject=lambda *args:(False,None)
  reject('failed-same-mask-hull-injectivity',fixture)
 finally:m.inject=original
 calls=[0]
 def fail_reflected_reference(*args):
  calls[0]+=1
  return(False,None)if calls[0]==len(axis)+2 else original(*args)
 try:
  m.inject=fail_reflected_reference
  reject('failed-enlarged-reflected-reference',fixture)
 finally:m.inject=original
 out['metadata']['input_sha256']=expected;out['metadata']['fixture_selection']='actual axis references plus first direct/root/hessian/gradient leaves; explicitly incomplete'
 m.write_artifact(out,fixture_path);fixture_raw=Path(fixture_path).read_bytes();after={str(p):hashlib.sha256(p.read_bytes()).hexdigest()for p in paths};assert before==after
 return {'format':'a5-n8-actual-axis-controls-v1','passed':True,'scope':'actual incomplete axis witness fixture; all original root/reference predicates; no count acceptance',
  'search_advanced':False,'count_certified':False,'input_sha256':expected,'actual_axis_box_ids':axis,
  'fixture_path':fixture_path,'fixture_bytes':len(fixture_raw),'fixture_sha256':hashlib.sha256(fixture_raw).hexdigest(),
  'proposal_receipt':receipt,'axis_checks':out['metadata']['axis_reuse'],'negative_controls':negatives,'negative_control_count':len(negatives),
  'source_sha256_before':before,'source_sha256_after':after,'sources_unchanged':True,'seconds':time.monotonic()-start}
if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('certificate');parser.add_argument('--input-sha256',required=True);parser.add_argument('--fixture',required=True);parser.add_argument('--output',required=True);args=parser.parse_args()
 result=run(args.certificate,args.input_sha256,args.fixture);Path(args.output).write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print(json.dumps({'passed':True,'negative_controls':result['negative_control_count'],'fixture_sha256':result['fixture_sha256'],'count_certified':False}),flush=True)
