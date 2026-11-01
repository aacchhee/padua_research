"""Structural continuation controls only; never accept a mathematical witness."""
import argparse,copy,hashlib,json,platform,tempfile
from pathlib import Path
import a5_n8_continue_v5 as m

def fixture():
 r=m.S>>30
 return {
  'format':'a5-n8-spatial-v1','n':8,'precision':m.PREC,
  'pattern_order':'compatible-mask','field_embedding':m.embedding_record(),
  'metadata':{'source_sha256':m.PREVIOUS_SOURCE_SHA},
  'node_cones':[{'index':i,'status':'accepted'}for i in range(45)],
  'interior_roots':[{'id':0,'mask':1,'R':m.encbox([(m.S//4-r,m.S//4+r),(-r,r)]),'C':[['1','0'],['0','1']]}],
  'leaves':[{'path':'0','all_gradient':0}],
  'pending_paths':['1'],'unresolved':[],
  'summary':{'complete':False,'interior_complete':False,'unresolved':0,
   'stats':{'visited':2,'discard':1,'all_gradient':1,'root':1},
   'pending':1,'depth':1,'interior':1,'leaf_counts':{'all_gradient':1},
   'leaf_pattern_records':0,'node_leaves':0,'all_gradient_leaves':1,
   'maximum_ambiguity':45,'seconds':0}}

def run():
 before={str(p):hashlib.sha256(p.read_bytes()).hexdigest()for p in(Path(m.__file__),Path(__file__))}
 pins=m.frozen_guards();valid=fixture();original=copy.deepcopy(valid)
 roots,counts=m.validate_partial(valid)
 assert valid==original and len(roots)==1 and roots[0]['_C']==[[m.F(1),m.F(0)],[m.F(0),m.F(1)]]
 assert roots[0]['_R']==[(m.dyadic(z[0]),m.dyadic(z[1]))for z in valid['interior_roots'][0]['R']]
 assert {k:v for k,v in roots[0].items()if not k.startswith('_')}==valid['interior_roots'][0]
 assert m.pathbox('')==[(-m.S,m.S),(-m.S,m.S)]
 assert m.pathbox('0')==[(-m.S,0),(-m.S,m.S)]
 assert m.pathbox('01')==[(-m.S,0),(0,m.S)]
 m.prefix_partition(['00','01','10','11'])
 cases=[]
 def bad(name,change):
  data=copy.deepcopy(valid);change(data)
  try:m.validate_partial(data)
  except (ValueError,KeyError,TypeError,ZeroDivisionError):cases.append(name);return
  raise AssertionError('malformed structural fixture accepted: '+name)
 bad('wrong-degree',lambda d:d.update(n=7))
 bad('boolean-degree',lambda d:d.update(n=True))
 bad('wrong-precision',lambda d:d.update(precision=159))
 bad('wrong-field',lambda d:d['field_embedding'].update(a_interval=['0','1']))
 bad('wrong-source',lambda d:d['metadata'].update(source_sha256='0'*64))
 bad('complete-input',lambda d:d['summary'].update(complete=True))
 bad('interior-complete-input',lambda d:d['summary'].update(interior_complete=True))
 bad('boundary-bearing-input',lambda d:d.update(edges=[]))
 bad('unresolved-input',lambda d:d['unresolved'].append({'path':'1'}))
 bad('empty-pending',lambda d:d.update(pending_paths=[]))
 bad('duplicate-terminal',lambda d:d.update(pending_paths=['0']))
 bad('overlapping-prefix',lambda d:d.update(pending_paths=['00','1']))
 bad('incomplete-partition',lambda d:d.update(pending_paths=['11']))
 bad('nonbinary-path',lambda d:d.update(pending_paths=['x']))
 bad('depth45-path',lambda d:d.update(pending_paths=['1'*45]))
 bad('boolean-visited',lambda d:d['summary']['stats'].update(visited=True))
 bad('wrong-visited',lambda d:d['summary']['stats'].update(visited=3))
 bad('wrong-discard',lambda d:d['summary']['stats'].update(discard=0))
 bad('wrong-pending-count',lambda d:d['summary'].update(pending=2))
 bad('boolean-pending-count',lambda d:d['summary'].update(pending=True))
 bad('wrong-leaf-counts',lambda d:d['summary'].update(leaf_counts={'all_gradient':2}))
 bad('boolean-leaf-count',lambda d:d['summary'].update(leaf_counts={'all_gradient':True}))
 bad('wrong-node-count',lambda d:d['summary'].update(node_leaves=1))
 bad('wrong-pattern-count',lambda d:d['summary'].update(leaf_pattern_records=1))
 bad('wrong-root-count',lambda d:d['summary'].update(interior=0))
 bad('depth-limit-input',lambda d:d['summary']['stats'].update(depth_limit=1))
 bad('root-id-boolean',lambda d:d['interior_roots'][0].update(id=False))
 bad('root-id-gap',lambda d:d['interior_roots'][0].update(id=1))
 bad('mask-overflow',lambda d:d['interior_roots'][0].update(mask=1<<45))
 bad('root-not-dyadic',lambda d:d['interior_roots'][0]['R'][0].__setitem__(0,'1/3'))
 bad('root-not-interior',lambda d:d['interior_roots'][0]['R'][0].__setitem__(0,'-1'))
 bad('floating-preconditioner',lambda d:d['interior_roots'][0]['C'][0].__setitem__(0,1.0))
 bad('singular-preconditioner',lambda d:d['interior_roots'][0].update(C=[['0','0'],['0','0']]))
 bad('missing-node',lambda d:d['node_cones'].pop())
 bad('wrong-node-index',lambda d:d['node_cones'][1].update(index=0))
 bad('boolean-axis',lambda d:d['leaves'][0].update(all_gradient=True))
 bad('mixed-leaf-keys',lambda d:d['leaves'][0].update(patterns=[]))
 ordinary=copy.deepcopy(valid);ordinary['leaves']=[{'path':'0','patterns':[{'code':'root','id':0}]}]
 ordinary['summary'].update(leaf_counts={'root':1},leaf_pattern_records=1,all_gradient_leaves=0)
 ordinary['summary']['stats']['all_gradient']=0;m.validate_partial(ordinary)
 for name,reference in(('absent-root-reference',1),('boolean-root-reference',False)):
  changed=copy.deepcopy(ordinary);changed['leaves'][0]['patterns'][0]['id']=reference
  try:m.validate_partial(changed)
  except ValueError:cases.append(name)
  else:raise AssertionError('malformed root reference accepted')
 with tempfile.TemporaryDirectory(prefix='a5-n8-continue-structural-')as folder:
  path=Path(folder)/'synthetic-structural-fixture.json.gz';m.write_artifact(valid,str(path))
  loaded,restored,recounts,digest,size=m.load_partial(path)
  assert loaded==valid and len(restored)==1 and dict(recounts)==dict(counts)
  assert digest==hashlib.sha256(path.read_bytes()).hexdigest()and size==path.stat().st_size
  badpath=Path(folder)/'duplicate-key.json';badpath.write_text('{"n":8,"n":8}')
  try:m.load_partial(badpath)
  except ValueError:cases.append('duplicate-JSON-key')
  else:raise AssertionError('duplicate JSON key accepted')

 # NEW final-stage protocol controls are synthetic structural fixtures only.
 from a5_n8_continue_controls import fixture as original_fixture
 original=original_fixture();current=copy.deepcopy(original)
 current['metadata']['source_sha256']=m.PREVIOUS_SOURCE_SHA
 def ancestry(digest,size):return {'input_sha256':digest,'input_bytes':size,'prior_source_sha256':m.FROZEN_SOURCES['a5_n8_boxes.py'],'prior_summary_seconds':original['summary']['seconds'],'frozen_sources':dict(m.FROZEN_SOURCES)}
 with tempfile.TemporaryDirectory(prefix='a5-n8-v5-lineage-')as folder:
  oldpath=Path(folder)/'synthetic-original-v3.json.gz';m.write_artifact(original,str(oldpath));oldraw=oldpath.read_bytes();oldsha=hashlib.sha256(oldraw).hexdigest()
  current['metadata']['continuation']=ancestry(oldsha,len(oldraw))
  newpath=Path(folder)/'synthetic-source96-v4.json.gz';m.write_artifact(current,str(newpath));newsha=hashlib.sha256(newpath.read_bytes()).hexdigest()
  loaded,_,_,actual,_,lineage=m.load_stage(newpath,oldpath,newsha)
  assert loaded==current and actual==newsha and lineage['original_v3_sha256']==oldsha
  try:m.load_stage(newpath,oldpath,'0'*64)
  except ValueError:cases.append('wrong-actual-v4-raw-sha')
  else:raise AssertionError('wrong expected raw digest accepted')
  other=Path(folder)/'different-original-v3.json.gz';altered=copy.deepcopy(original);altered['metadata']['synthetic_owner']='other';m.write_artifact(altered,str(other))
  try:m.load_stage(newpath,other,newsha)
  except ValueError:cases.append('different-original-file-lineage')
  else:raise AssertionError('different original bytes accepted')
 for name,change in(
  ('wrong-original-ancestor-source',lambda d:d['metadata']['continuation'].update(prior_source_sha256='0'*64)),
  ('wrong-frozen-ancestor-pin',lambda d:d['metadata']['continuation']['frozen_sources'].update(a5_n8_field='wrong')),
  ('wrong-original-timing',lambda d:d['metadata']['continuation'].update(prior_summary_seconds=1)),
  ('changed-original-node-record',lambda d:d['node_cones'][0].update(extra=True)),
  ('changed-original-root-prefix',lambda d:d['interior_roots'][0].update(mask=2)),
  ('changed-original-leaf-prefix',lambda d:d['leaves'][0].update(all_gradient=1)),
  ('decreased-traversal-count',lambda d:d['summary']['stats'].update(visited=1))):
  altered=copy.deepcopy(current);change(altered)
  try:m.validate_lineage(altered,original,oldsha,len(oldraw))
  except ValueError:cases.append(name)
  else:raise AssertionError('bad original lineage accepted: '+name)
 def frontier(paths):return [(*m.pathbox(p),len(p),p)for p in paths]
 full=frontier(['1','01','001','000']);active,parked=m.park_frontier(full)
 assert [v[-1]for v in active]==['01','001','000']and[v[-1]for v in parked]==['1']
 restored,complete=m.restore_frontier(parked,active,[],[],{'visited':3,'discard':0})
 assert restored==full and complete is False
 restored,complete=m.restore_frontier(frontier(['1']),[],[{'path':'0'}],[],{'visited':2,'discard':1})
 assert [v[-1]for v in restored]==['1']and complete is True and not(not restored)
 restored,complete=m.restore_frontier(frontier(['1']),[],[],[{'path':'0'}],{'visited':2,'discard':0})
 assert [v[-1]for v in restored]==['1']and complete is False
 for name,action in(
  ('empty-pending-root-cannot-be-parked',lambda:m.park_frontier(frontier(['']))),
  ('unordered-frontier-rejected',lambda:m.park_frontier(frontier(['0','1']))),
  ('missing-parked-right-detected',lambda:m.restore_frontier([],[],[{'path':'0'}],[],{'visited':2,'discard':1})),
  ('wrong-full-tree-accounting',lambda:m.restore_frontier(frontier(['1']),[],[{'path':'0'}],[],{'visited':3,'discard':1}))):
  try:action()
  except ValueError:cases.append(name)
  else:raise AssertionError('bad parking/restoration accepted: '+name)
 after={path:hashlib.sha256(Path(path).read_bytes()).hexdigest()for path in before}
 assert before==after
 return {'format':'a5-n8-final-left-stage-structural-controls-v1','passed':True,
  'scope':'synthetic structural fixtures only; no mathematical witness accepted and no search advanced',
  'mathematical_search_executed':False,'mathematical_certificate_accepted':False,
  'negative_controls':cases,'negative_control_count':len(cases),
  'positive_controls':['full-prefix-partition','widest-side-path-reconstruction','exact-root-R-C-ID-restoration','input-not-mutated','atomic-gzip-structural-roundtrip','all-original-mathematical-helpers-AST-identical','classification-subdivision-loop-AST-identical','actual-source96-lineage-sha-binding','original-node-root-leaf-prefix-preservation','parked-right-frontier-restored-exactly','left-complete-keeps-full-pending','unresolved-axis-side-retained'],
  'frozen_original_sources':pins,'source_sha256_before':before,'source_sha256_after':after,
  'sources_unchanged':True,'python':platform.python_version(),'sympy':m.s.__version__}

if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--output',required=True);args=parser.parse_args()
 result=run();Path(args.output).write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
 print(json.dumps({'passed':result['passed'],'negative_controls':result['negative_control_count'],'search_advanced':False}),flush=True)
