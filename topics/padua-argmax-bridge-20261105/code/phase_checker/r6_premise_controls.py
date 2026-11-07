#!/usr/bin/env python3
"""Focused range-premise tests; no unchanged arithmetic campaign or full cover."""
import ast,copy,hashlib,json,math,pathlib,time
import check_r6 as r6
ROOT=r6.ROOT;OUT=ROOT/'local-output/argmax-bridge-20261105/phase-checker/round6'

def main():
 OUT.mkdir(parents=True,exist_ok=True);start=time.process_time()
 path=ROOT/r6.RANGE_RECEIPT_PATH;raw=path.read_bytes();receipt=r6.strict_json(raw)
 seen=[]
 def reader(path):
  assert path in r6.CODE_DATA_PINS and not path.endswith('.md');seen.append(path)
  return (ROOT/path).read_bytes()
 pins=r6._validate_range_snapshot(raw,reader)
 assert set(seen)==set(r6.CODE_DATA_PINS)
 production=r6.published_corner_premise();assert production['receipt_sha256']==r6.RANGE_RECEIPT_SHA
 negative=[]
 def bad_contents(name,mutate,read=None):
  obj=copy.deepcopy(receipt);mutate(obj)
  try:r6._validate_range_contents(obj,reader if read is None else read)
  except r6.Invalid as e:negative.append({'name':name,'reason':str(e)})
  else:raise AssertionError(name)
 try:r6._validate_range_snapshot(raw+b' ',reader)
 except r6.Invalid as e:negative.append({'name':'changed receipt bytes','reason':str(e)})
 else:raise AssertionError('tampered receipt accepted')
 bad_contents('status',lambda d:d.update(status='FAIL'))
 bad_contents('schema',lambda d:d.update(schema='caller-schema'))
 bad_contents('missing degree',lambda d:d['input_degrees'].remove(24))
 bad_contents('out of order range',lambda d:d['input_degrees'].reverse())
 bad_contents('bool degree alias',lambda d:d['input_degrees'].__setitem__(0,True))
 bad_contents('float degree alias',lambda d:d['input_degrees'].__setitem__(0,2.))
 for name,value in [('requested',126),('attempted',126),('completed',126),('passed',126),('failed',1),('unrun',1)]:
  bad_contents('counter '+name,lambda d,name=name,value=value:d['counters'].__setitem__(name,value))
 bad_contents('float counter alias',lambda d:d['counters'].__setitem__('passed',127.))
 bad_contents('all integer inputs flag false',lambda d:d.update(all_integer_inputs_ran_and_passed=False))
 bad_contents('integer truth alias',lambda d:d.update(all_integer_inputs_ran_and_passed=1))
 bad_contents('failure present',lambda d:d.update(failure='unrun degree'))
 bad_contents('kappa',lambda d:d.update(common_kappa='1/12500'))
 bad_contents('phase radius',lambda d:d.update(scaled_phase_square_radius='1/64'))
 bad_contents('source declared SHA',lambda d:d['source'].__setitem__('sha256','0'*64))
 bad_contents('wrapper path',lambda d:d['wrapper'].__setitem__('path','caller-code.py'))
 bad_contents('source size bool',lambda d:d['source'].__setitem__('bytes',True))
 bad_contents('missing data identity',lambda d:d['frozen_reference_identities'].pop(2))
 def corrupted_source(path):
  value=(ROOT/path).read_bytes()
  return value+b' ' if path.endswith('check_corner_exact.cpp') else value
 bad_contents('changed actual source bytes',lambda d:None,corrupted_source)
 def corrupted_data(path):
  value=(ROOT/path).read_bytes()
  return value+b' ' if path.endswith('n3-corner-batch.json') else value
 bad_contents('changed actual data bytes',lambda d:None,corrupted_data)
 # No current prose record is opened or hash-validated by the premise guard.
 # Changing a legacy prose-reference metadata SHA has no semantic effect here;
 # production still requires the fixed original evidence bytes above.
 prose=copy.deepcopy(receipt)
 for row in prose['frozen_reference_identities']:
  if row['path'].endswith('.md'):row['sha256']='not-a-new-prose-guard'
 assert r6._validate_range_contents(prose,reader)==pins
 geometry=[];square=[-1/128,1/128,-1/128,1/128]
 for n in [2,17,24,32,128]:
  assert r6.local_range(n,square)
  assert r6.F(1,128)**2*(1+r6.F(n*n,(n+1)**2))/2<r6.F(1,16384)<r6.F(1,16000)
  geometry.append({'n':n,'exact_square_accepted':True})
 for n in [1,129,True,24.]:assert not r6.local_range(n,square)
 for n in [2,17,24,32,128]:
  assert not r6.local_range(n,[0.,math.nextafter(1/128,math.inf),0.,1/128])
  assert not r6.local_range(n,[-math.nextafter(1/128,math.inf),0.,-1/128,0.])
 # The unchanged parser/geometry/build classes have exact AST equivalence.
 oldpath=pathlib.Path(__file__).with_name('check.py');old=ast.parse(oldpath.read_bytes());new=ast.parse(pathlib.Path(r6.__file__).read_bytes())
 unchanged=['rational','Kernel','tree_partition','box_for','minabs','maxabs','local_inherited','strict_json']
 def definitions(tree):return {x.name:ast.dump(x,include_attributes=False) for x in tree.body if isinstance(x,(ast.FunctionDef,ast.ClassDef))}
 od,nd=definitions(old),definitions(new)
 assert all(od[name]==nd[name] for name in unchanged)
 for bad in [b'{"n":24,"n":32}',b'{"x":NaN}',b'{"x":1e400}']:
  try:r6.strict_json(bad)
  except r6.Invalid:pass
  else:raise AssertionError('strict JSON regressed')
 try:r6.tree_partition([{'root':r,'path':''} for r in range(3)])
 except r6.Invalid:pass
 else:raise AssertionError('missing root accepted')
 # One existing positive partial sample checks the whole wrapper wiring;
 # this is bounded n17, not a complete n24/n32 replay or an arithmetic rerun.
 sample=ROOT/'local-output/argmax-bridge-20261105/N3/outward-calibration-v1/n17-sample-far.json'
 k=r6.Kernel('round5');partial=r6.check(r6.strict_json(sample.read_bytes()),k)
 assert not partial['accepted'] and not partial['failed_leaves'] and partial['checked_leaves']==1 and partial['pending']>0
 source_names=['check_r6.py','r6_premise_controls.py','check.py','hybrid_kernel_v2.cpp','build_snapshot.py']
 sources=[r6.build_snapshot.identity(pathlib.Path(__file__).with_name(name)) for name in source_names]
 assert sources[2]['sha256']=='88dde644a77a286e547679b0547c4d35814a4dda7373575208246882d9a26820'
 assert sources[3]['sha256']=='17fea91d4fa02e4183823e5d70b44705e96da7acfd26b04a0f3ed1cac443d9a2'
 assert sources[4]['sha256']=='19a5a7c2296768853b94672b9b5dc4cf16c9ae87c37abbcde073ffaf89246bfb'
 report={'status':'PASS focused guard controls; independent focused review required before full checks',
  'rules_input':'fc8c2885f47b08cecc7f65328db0e740cbc205ea','range_receipt_sha256':hashlib.sha256(raw).hexdigest(),
  'code_data_pins':pins,'negative_controls':negative,'geometry_controls':geometry,'degrees_rejected':[1,129,'bool True','float 24.0'],
  'outside_square_endpoints_rejected':True,'no_current_prose_read_or_guard':True,'unchanged_AST_definitions':unchanged,
  'partial_sample':{'candidate_sha256':hashlib.sha256(sample.read_bytes()).hexdigest(),'checked_leaves':partial['checked_leaves'],
    'pending':partial['pending'],'accepted':partial['accepted'],'failed_leaves':len(partial['failed_leaves'])},
  'sources':sources,'checker_cpu_seconds':time.process_time()-start,'full_runs_executed':0}
 full={'compact':report,'partial_replay':partial,'build_provenance':k.provenance}
 fullpath=OUT/'premise-controls-full.json';fullpath.write_text(json.dumps(full,indent=2)+'\n')
 report['full_receipt']={'path':str(fullpath.relative_to(ROOT)),'bytes':fullpath.stat().st_size,'sha256':hashlib.sha256(fullpath.read_bytes()).hexdigest()}
 evidence=ROOT/'topics/padua-argmax-bridge-20261105/evidence/phase-r6-premise-controls.json';evidence.write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps({'status':report['status'],'negative_controls':len(negative),'source_SHA':sources[0]['sha256'],'controls_SHA':sources[1]['sha256'],'full_runs_executed':0},indent=2))
if __name__=='__main__':main()
