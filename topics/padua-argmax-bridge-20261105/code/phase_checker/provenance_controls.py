#!/usr/bin/env python3
"""Focused R1/finite-instance regressions; preserves original math receipt."""
import concurrent.futures,hashlib,json,math,pathlib,subprocess,sys
import check as ck
BASE=ck.ROOT;OUT=BASE/'local-output/argmax-bridge-20261105/phase-checker'
def main():
 rejected=[]
 for name,raw in [('duplicate',b'{"n":17,"n":33}'),('nested duplicate',b'{"x":{"a":0,"a":1}}'),('NaN',b'{"x":NaN}'),('Infinity',b'{"x":Infinity}'),('overflow',b'{"x":1e400}')]:
  try:ck.strict_json(raw)
  except ck.Invalid:rejected.append(name)
  else:raise AssertionError(name)
 # The checked dict and digest remain bound to this byte snapshot when the
 # original path is replaced. No checker function rereads that path.
 path=OUT/'r1-mutable-input-control.json';raw=b'{"x":17}'
 path.write_bytes(raw);snapshot=path.read_bytes();path.write_bytes(b'{"x":33}')
 assert ck.strict_json(snapshot)=={'x':17} and hashlib.sha256(snapshot).hexdigest()==hashlib.sha256(raw).hexdigest()
 sample=BASE/'local-output/argmax-bridge-20261105/N3/outward-calibration-v1/n17-sample-far.json'
 def replay(i):
  out=OUT/f'r1-isolated-replay-{i}.json'
  result=subprocess.run([sys.executable,str(pathlib.Path(ck.__file__)),str(sample),'--output',str(out)],stdout=subprocess.DEVNULL,stderr=subprocess.PIPE,text=True)
  data=json.loads(out.read_bytes())
  assert result.returncode==1 and not data['accepted'] and not data.get('error') and not data['failed_leaves']
  return out,data
 with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:replays=list(pool.map(replay,[0,1]))
 dirs=[d['build_provenance']['workdir'] for _,d in replays];assert len(set(dirs))==2
 # The obsolete shared binary is not any loaded binary or dependency.
 fixed=str(OUT/'libphase_checker.so')
 for _,d in replays:
  assert d['build_provenance']['checker_binary']['path']!=fixed
  assert d['candidate_sha256']==hashlib.sha256(sample.read_bytes()).hexdigest()
  assert d['build_provenance']['loaded_dependency_closure']
 premise=ck.published_corner_premise()
 guards=[]
 for n in [17,32,33,64,128,129]:
  ok=ck.local_fixed_instance(n,[0.,1/128,0.,1/128]);assert ok==(n in (33,64,128))
  guards.append({'n':n,'phase_square_guard':ok})
 for n in (33,64,128):
  assert not ck.local_fixed_instance(n,[0.,math.nextafter(1/128,math.inf),0.,1/128])
  assert not ck.local_fixed_instance(n,[0.,.1,0.,.1])
 sources=[ck.build_snapshot.identity(p) for p in sorted(pathlib.Path(ck.__file__).parent.glob('*')) if p.is_file()]
 compact={'finding':'R1 build/input provenance','status':'focused regression PASS; mathematical review pending',
  'rules_sha':'c000899f3fb10d6ba0f1725341a045fe11ec943a','strict_json_rejections':rejected,
  'input_snapshot_replacement_control':True,'parallel_unique_workdirs':dirs,'obsolete_shared_binary_unused':True,
  'fixed_instance_guards':guards,'corner_receipt_sha256':premise['receipt_sha256'],
  'historical_source_pins':[p for p in premise['source_pins'] if p['snapshot']!='working source snapshot'],
  'fresh_replays':[{'path':str(p.relative_to(BASE)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
    'binary_sha256':d['build_provenance']['checker_binary']['sha256'],'candidate_sha256':d['candidate_sha256'],
    'preprocessed_sha256':d['build_provenance']['preprocessed_translation_unit']['sha256']} for p,d in replays],
  'sources':sources,'unchanged_campaign':'original phase-checker-calibration.json preserved; no full-cover claim'}
 evidence=BASE/'topics/padua-argmax-bridge-20261105/evidence/phase-checker-provenance.json'
 evidence.write_text(json.dumps(compact,indent=2)+'\n');print(json.dumps(compact,indent=2))
if __name__=='__main__':main()
