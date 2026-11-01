"""Synthetic structural join controls only; no mathematical acceptance."""
import argparse,copy,gzip,json,tempfile
from pathlib import Path
import a5_n8_join_axis as m

def fixtures():
 source=next(iter(m.INTERIOR_SOURCES))
 interior={'format':'a5-n8-spatial-v1','n':8,'precision':160,'pattern_order':'compatible-mask','field_embedding':{},
  'metadata':{'source_sha256':source},'node_cones':[{'index':i}for i in range(45)],'interior_roots':[],
  'leaves':[{'path':'','all_gradient':0}],'pending_paths':[],'unresolved':[],
  'summary':{'interior_complete':True,'complete':False,'interior':0,'node_leaves':0,'all_gradient_leaves':1,'leaf_counts':{'all_gradient':1},'leaf_pattern_records':0}}
 boundary={'edges':[{'axis':axis,'side':side,'patterns':[]}for axis,side in((0,-1),(0,1),(1,-1),(1,1))],
  'corners':[{'point':[u,v],'kind':'node'}for u,v in((-1,-1),(-1,1),(1,-1),(1,1))],
  'summary':{'complete':True,'unresolved':0,'edge':0,'corner':0,'counts':{},'seconds':0},'unresolved':[]}
 return interior,boundary
def run():
 paths=[Path(m.__file__),Path(__file__)];before={str(p):m.sha(p.read_bytes())for p in paths}
 interior,boundary=fixtures();original_i,original_b=copy.deepcopy(interior),copy.deepcopy(boundary)
 joined,receipt=m.join_data(interior,boundary,{'synthetic_fixture':True})
 assert interior==original_i and boundary==original_b and joined['edges']==boundary['edges']and joined['corners']==boundary['corners']and joined['boundary_summary']==boundary['summary']
 assert receipt['schema_complete']is True and receipt['count_certified']is False and receipt['independent_checker_required']is True
 negative=[]
 def reject(name,change_i=None,change_b=None):
  a,b=copy.deepcopy(interior),copy.deepcopy(boundary)
  if change_i:change_i(a)
  if change_b:change_b(b)
  try:m.join_data(a,b,{'synthetic_fixture':True})
  except (ValueError,KeyError,TypeError):negative.append(name);return
  raise AssertionError('bad structural join accepted: '+name)
 reject('incomplete-interior-flag',lambda d:d['summary'].update(interior_complete=False))
 reject('already-complete-interior',lambda d:d['summary'].update(complete=True))
 reject('pending-interior',lambda d:d['pending_paths'].append('0'))
 reject('unresolved-interior',lambda d:d['unresolved'].append({'path':'0'}))
 reject('existing-boundary-fields',lambda d:d.update(edges=[]))
 reject('wrong-source',lambda d:d['metadata'].update(source_sha256='0'*64))
 reject('incomplete-prefix',lambda d:d['leaves'][0].update(path='0'))
 reject('mixed-leaf-keys',lambda d:d['leaves'][0].update(patterns=[]))
 reject('wrong-leaf-accounting',lambda d:d['summary'].update(leaf_counts={'all_gradient':2}))
 reject('wrong-root-count',lambda d:d['summary'].update(interior=1))
 reject('missing-node-record',lambda d:d['node_cones'].pop())
 reject('partial-edge-set',change_b=lambda d:d['edges'].pop())
 reject('duplicate-edge',change_b=lambda d:d['edges'][1].update(side=-1))
 reject('boolean-edge-coordinate',change_b=lambda d:d['edges'][1].update(side=True))
 reject('missing-corner',change_b=lambda d:d['corners'].pop())
 reject('unresolved-corner',change_b=lambda d:d['corners'][0].update(kind='unresolved'))
 reject('unresolved-boundary-list',change_b=lambda d:d['unresolved'].append({'axis':0}))
 reject('incomplete-boundary-flag',change_b=lambda d:d['summary'].update(complete=False))
 reject('wrong-boundary-count',change_b=lambda d:d['summary'].update(edge=1))
 reject('wrong-disposition-count',change_b=lambda d:d['summary'].update(counts={'root':1}))
 positive=copy.deepcopy(boundary);positive['edges'][0]['patterns']=[{'kind':'roots','mask':0,'points':[{'code':'root','id':0,'interval':['-1/2','0']}]}]
 positive['summary'].update(edge=1,counts={'root':1});positive['corners'][0].update(kind='max',id=0);positive['summary']['corner']=1
 combined,_=m.join_data(interior,positive,{'synthetic_fixture':True});assert combined['summary']['total']==2 and m.canonical({'edges':combined['edges'],'corners':combined['corners'],'summary':combined['boundary_summary']})==m.canonical(m.components(positive))
 with tempfile.TemporaryDirectory(prefix='a5-n8-synthetic-join-')as directory:
  root=Path(directory);ip=root/'synthetic-interior.gz';bp=root/'synthetic-boundary.json';out=root/'synthetic-output.gz'
  ip.write_bytes(gzip.compress(m.canonical(interior),mtime=0));bp.write_bytes(m.canonical(boundary))
  iraw,braw=ip.read_bytes(),bp.read_bytes();actual=m.run(ip,bp,m.sha(iraw),m.sha(braw),out)
  repeated=m.run(ip,bp,m.sha(iraw),m.sha(braw),out);assert actual==repeated and m.decode(out.read_bytes())['edges']==boundary['edges']
  try:m.run(ip,bp,'0'*64,m.sha(braw),root/'bad.gz')
  except ValueError:negative.append('wrong-raw-input-sha')
  else:raise AssertionError('wrong raw identity accepted')
  other=root/'different-output';other.write_bytes(b'preserve-existing')
  try:m.write_atomic(other,b'different')
  except ValueError:negative.append('different-existing-output-preserved')
  else:raise AssertionError('different existing bytes overwritten')
  assert other.read_bytes()==b'preserve-existing'
  try:m.decode(b'{"edges":[],"edges":[]}')
  except ValueError:negative.append('duplicate-json-key')
  else:raise AssertionError('duplicate JSON accepted')
 axis_source='f77056651bb1bbf8eb3b154190eadad47ce33cbb3b793b4f32ae31f0834497e5';m.guards(axis_source)
 synthetic_axis=copy.deepcopy(interior);synthetic_axis['metadata']['source_sha256']=axis_source
 axis_join,_=m.join_data(synthetic_axis,boundary,{'synthetic_fixture':True});assert axis_join['edges']==boundary['edges']
 saved=m.BASE_JOIN_SHA
 try:
  m.BASE_JOIN_SHA='0'*64
  try:m.guards(axis_source)
  except ValueError:negative.append('wrong-frozen-base-joiner-pin')
  else:raise AssertionError('wrong base joiner pin accepted')
 finally:m.BASE_JOIN_SHA=saved
 after={str(p):m.sha(p.read_bytes())for p in paths};assert before==after
 return {'format':'a5-n8-axis-join-structural-controls-v1','passed':True,'scope':'synthetic STRUCTURAL data only; fixtures intentionally do not satisfy mathematical predicates',
  'mathematical_search_executed':False,'mathematical_certificate_accepted':False,'negative_controls':negative,'negative_control_count':len(negative),
  'positive_controls':['literal-edge-corner-summary-copy','all-inputs-unmodified','root-disposition-count-accounting','deterministic-gzip-roundtrip','idempotence','source-pins-guarded'],
  'source_sha256_before':before,'source_sha256_after':after,'sources_unchanged':True}
if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--output',required=True);args=parser.parse_args();result=run();m.write_atomic(args.output,json.dumps(result,indent=2,sort_keys=True).encode()+b'\n');print(json.dumps({'passed':True,'negative_controls':result['negative_control_count'],'mathematical_certificate_accepted':False}),flush=True)
