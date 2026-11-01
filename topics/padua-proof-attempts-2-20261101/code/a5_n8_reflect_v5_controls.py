"""Bounded exact reflection proposal pilot; count remains explicitly unverified."""
import argparse,copy,gzip,hashlib,json
from pathlib import Path
import a5_n8_reflect_v5 as m

def run(certificate,output_fixture):
 paths=[Path(m.__file__),Path(__file__)]
 before={str(p):hashlib.sha256(p.read_bytes()).hexdigest()for p in paths};m.guards()
 raw=Path(certificate).read_bytes();data=json.loads(gzip.decompress(raw))
 selected=[]
 for kind in('all_gradient','node_cone'):
  selected.append(next(copy.deepcopy(row)for row in data['leaves']if kind in row))
 for code in('root','hessian','gradient'):
  row=next(row for row in data['leaves']if'patterns'in row and any(v['code']==code for v in row['patterns']))
  if not any(row['path']==old['path']for old in selected):selected.append(copy.deepcopy(row))
 fixture=copy.deepcopy(data);fixture['leaves']=selected
 out,receipt=m.propose(fixture,True)
 require=m.require
 require(not out['summary']['complete']and not out['summary']['interior_complete'],'fixture became a count')
 require(receipt['exact_cardinal_identities']==45 and receipt['proposed_roots']==2*receipt['retained_left_roots'],'root-pair bookkeeping')
 permutation=out['metadata']['node_permutation']
 for mask in[0,(1<<45)-1,0x193A5C7E91D]+[1<<i for i in range(45)]:
  require(m.maskmap(m.maskmap(mask,permutation),permutation)==mask,'mask involution')
 for length in range(9):
  for number in range(1<<length):
   path=format(number,'0'+str(length)+'b')if length else''
   require(m.reflected_path(m.reflected_path(path))==path,'path involution')
   Q=m.pathbox(path);P=m.pathbox(m.reflected_path(path))
   require(P==[(-Q[0][1],-Q[0][0]),Q[1]],'dyadic reflected path geometry')
 for root in data['interior_roots']:
  require(m.reflected_box(m.reflected_box(root['R']))==root['R'],'box involution')
  require(m.reflected_C(m.reflected_C(root['C']))==root['C'],'preconditioner involution')
 negatives=[]
 def reject(name,case,fixture_only=True):
  try:m.propose(case,fixture_only)
  except ValueError:negatives.append(name);return
  raise AssertionError('unsupported proposal accepted: '+name)
 reject('actual-left-half-incomplete',data,False)
 bad=copy.deepcopy(fixture);bad['field_embedding']['a_interval']=['0','1'];reject('wrong-field',bad)
 bad=copy.deepcopy(fixture);bad['metadata']['source_sha256']='0'*64;reject('wrong-producer',bad)
 bad=copy.deepcopy(fixture);bad['interior_roots'][0]['R'][0]=['-1/1073741824','1/1073741824'];reject('axis-crossing-root',bad)
 bad=copy.deepcopy(fixture);ordinary=next(row for row in bad['leaves']if'patterns'in row);ordinary['patterns'].pop();reject('implicit-mask-count-mismatch',bad)
 bad=copy.deepcopy(fixture);node=next(row for row in bad['leaves']if'node_cone'in row);index=permutation[node['node_cone']];bad['node_cones'][index]['B']=[['0','0'],['0','0']];reject('reflected-node-cube-containment',bad)

 # Synthetic provenance only: no V5 search/output is represented by this fixture.
 provenance={'metadata':{'source_sha256':m.PRODUCER_V5_SHA,'continuation':{'prior_source_sha256':m.CONTINUATION_SHA,'source96_sha256':m.CONTINUATION_SHA,'frozen_sources':dict(m.FROZEN_SOURCES),'original_v3_sha256':hashlib.sha256(raw).hexdigest(),'original_v3_bytes':len(raw),'input_sha256':'1'*64},'left_focus':{'all_parked_paths_restored':True,'parked_right_paths':['1']}},'pending_paths':['1','00']}
 m.validate_new_provenance(provenance)
 for name,change in(
  ('wrong-new-parent-source',lambda d:d['metadata']['continuation'].update(prior_source_sha256='0'*64)),
  ('wrong-new-original-frozen-pin',lambda d:d['metadata']['continuation']['frozen_sources'].update(extra='bad')),
  ('missing-new-original-sha',lambda d:d['metadata']['continuation'].update(original_v3_sha256='')),
  ('parked-frontier-not-restored',lambda d:d['metadata']['left_focus'].update(all_parked_paths_restored=False)),
  ('missing-parked-right-word',lambda d:d.update(pending_paths=['00'])),
  ('non-right-parked-word',lambda d:d['metadata']['left_focus'].update(parked_right_paths=['0']))):
  changed=copy.deepcopy(provenance);change(changed)
  try:m.validate_new_provenance(changed)
  except ValueError:negatives.append(name)
  else:raise AssertionError('unsupported synthetic new provenance accepted: '+name)

 out['metadata']['input_sha256']=hashlib.sha256(raw).hexdigest();out['metadata']['fixture_selection']='first direct universal/node and ordinary root/hessian/gradient leaves; no search'
 m.write_artifact(out,output_fixture);fixture_raw=Path(output_fixture).read_bytes()
 after={str(p):hashlib.sha256(p.read_bytes()).hexdigest()for p in paths};require(before==after,'proposal/control source changed')
 return {'format':'a5-n8-versioned-reflection-controls-v1','passed':True,'scope':'exact identities and incomplete transformed witness fixture only; no count acceptance',
  'search_advanced':False,'count_certified':False,'input_sha256':hashlib.sha256(raw).hexdigest(),
  'fixture_path':output_fixture,'fixture_bytes':len(fixture_raw),'fixture_sha256':hashlib.sha256(fixture_raw).hexdigest(),
  'negative_controls':negatives,'negative_control_count':len(negatives),'proposal_receipt':receipt,
  'source_sha256_before':before,'source_sha256_after':after,'sources_unchanged':True,
  'fixture_summary':out['summary'],'independent_verification':'PENDING; unchanged checker must replay every proposed record'}

if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('certificate');parser.add_argument('--fixture',required=True);parser.add_argument('--output',required=True);args=parser.parse_args()
 result=run(args.certificate,args.fixture);Path(args.output).write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
 print(json.dumps({'passed':result['passed'],'negative_controls':result['negative_control_count'],'fixture_sha256':result['fixture_sha256'],'count_certified':False}),flush=True)
