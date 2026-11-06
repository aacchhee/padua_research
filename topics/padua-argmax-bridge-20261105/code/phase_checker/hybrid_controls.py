#!/usr/bin/env python3
"""Round4 preregistered bounded controls; never executes the whole tree."""
import ctypes,hashlib,json,math,pathlib,resource,time
import mpmath as mp
import check as ck
ROOT=ck.ROOT;OUT=ROOT/'local-output/argmax-bridge-20261105/phase-checker/round4'
CANDIDATE=ROOT/'local-output/argmax-bridge-20261105/N3/outward-full-n17-r3/n17-phase-compact.json'
OLD=ROOT/'local-output/argmax-bridge-20261105/phase-checker/n17-full-r3-replay.json'
TARGETS=[(0,'01010'),(0,'1100111'),(0,'11011111'),(3,'0011000'),(0,'1111111111101111')]

def main():
 OUT.mkdir(parents=True,exist_ok=True);start=time.process_time();children=resource.getrusage(resource.RUSAGE_CHILDREN)
 raw=CANDIDATE.read_bytes();assert hashlib.sha256(raw).hexdigest()=='64f7befd86658c8d9f29b05c1cb5a0162e611b726b161e737610547bed218c4b'
 data=ck.strict_json(raw)
 oldraw=OLD.read_bytes();assert hashlib.sha256(oldraw).hexdigest()=='021ded297f360245fb30a884efe7a3670321e4a736c22873abaa6079cc0257d7'
 old=ck.strict_json(oldraw);oldrows={(r['root'],r['path']):r for r in old['replay']}
 k=ck.Kernel();assert k.provenance['source_origin'].endswith('/hybrid_kernel.cpp')
 assert k.provenance['source_snapshot']['sha256']==ck.build_snapshot.identity(pathlib.Path(__file__).with_name('hybrid_kernel.cpp'))['sha256']
 ratio=k.lib.phase_ratio;ratio.argtypes=[ctypes.c_int,ctypes.c_int,ctypes.c_double,ctypes.c_double,ctypes.POINTER(ctypes.c_double),ctypes.POINTER(ctypes.c_int)];ratio.restype=ctypes.c_int
 mp.mp.dps=90;ratio_tests=[]
 for degree in [1,2,3,17,18]:
  frequencies=list(range(-(degree-1),degree,2));assert sum(abs(j) for j in frequencies)==degree*degree//2
  for turn,lo,hi,expect in [(0,0.,0.,0),(1,0.,0.,0),(-1,-.001,.001,0),(2,-.001,.001,0),(0,.125,.25,1),(1,.125,.25,1),(0,2**-30,2**-29,1),(0,-4.,4.,0)]:
   out=(ctypes.c_double*8)();used=ctypes.c_int(-1);assert ratio(degree,turn,lo,hi,out,ctypes.byref(used))==0;assert used.value==expect
   for t in [0,mp.mpf(1)/4,mp.mpf(1)/2,mp.mpf(3)/4,1]:
    z=turn*mp.pi+mp.mpf(lo)+(mp.mpf(hi)-mp.mpf(lo))*t
    val=sum(mp.cos(j*z) for j in frequencies);der=-sum(j*mp.sin(j*z) for j in frequencies)
    tolerance=mp.mpf('1e-70')
    assert mp.mpf(out[4])-tolerance<=val<=mp.mpf(out[5])+tolerance
    assert mp.mpf(out[6])-tolerance<=der<=mp.mpf(out[7])+tolerance
   ratio_tests.append({'k':degree,'turn':turn,'offsets':[lo,hi],'used_quotient':bool(used.value),'bounds':list(out)})
 disjoint=k.lib.phase_disjoint_intersection_control;disjoint.restype=ctypes.c_int;assert disjoint()==3
 # Different primitive formula: triangular D_n, including exceptional (n,0).
 primitive=k.lib.phase_term;primitive.argtypes=[ctypes.c_int,ctypes.c_int,ctypes.c_int,ctypes.c_double,ctypes.c_double,ctypes.POINTER(ctypes.c_double)];primitive.restype=ctypes.c_int
 primitive_tests=[]
 for n,r,s,a,b in [(3,0,0,0.,0.),(3,3,4,0.,0.),(3,0,4,0.,0.),(17,5,8,.2,.3)]:
  u=(r*mp.pi+mp.mpf(a))/n;v=(s*mp.pi+mp.mpf(b))/(n+1)
  value=mp.mpf(0);da=mp.mpf(0);db=mp.mpf(0)
  for i in range(n+1):
   for j in range(n+1-i):
    coef=(1 if i==0 else 2)*(1 if j==0 else 2)-(1 if (i,j)==(n,0) else 0)
    value+=coef*mp.cos(i*u)*mp.cos(j*v)
    da-=coef*i*mp.sin(i*u)*mp.cos(j*v)/n;db-=coef*j*mp.cos(i*u)*mp.sin(j*v)/(n+1)
  out=(ctypes.c_double*6)();assert primitive(n,r,s,a,b,out)==0
  assert all(mp.mpf(out[2*i])-mp.mpf('1e-70')<=z<=mp.mpf(out[2*i+1])+mp.mpf('1e-70') for i,z in enumerate([value,da,db]))
  primitive_tests.append({'n':n,'r':r,'s':s,'phases':[a,b],'triangular_value_and_gradient_agree':True})
 rejected=[]
 for name,rawbad in [('duplicate',b'{"n":17,"n":33}'),('nested duplicate',b'{"x":{"a":0,"a":1}}'),('NaN',b'{"x":NaN}'),('overflow',b'{"x":1e400}')]:
  try:ck.strict_json(rawbad)
  except ck.Invalid:rejected.append(name)
  else:raise AssertionError(name)
 pair=k.lib.phase_bounds_pair;pair.argtypes=[ctypes.c_int]+[ctypes.c_double]*4+[ctypes.POINTER(ctypes.c_double)];pair.restype=ctypes.c_int
 leaves={(r['root'],r['path']):r for r in data['leaves']};leaf_tests=[]
 for target in TARGETS:
  leaf=leaves[target];box=ck.box_for(data['roots'],*target);t=time.process_time()
  final=k.bounds(17,box);both=(ctypes.c_double*14)();assert pair(17,*box,both)==0
  assert list(both[:7])==oldrows[target]['bounds']
  assert final[0]<=both[0] and final[1]<=both[1] and final[2]>=both[2]
  su,cu,dl,lc=map(ck.F,[final[0],final[1],final[2],final[3]])
  ok=su<lc if leaf['kind']=='far' else cu<lc and su-dl<lc
  leaf_tests.append({'root':target[0],'path':target[1],'kind':leaf['kind'],'valid':bool(ok),'box':box,'old_bounds':list(both[:7]),'hybrid_bounds':list(both[7:]),'combined_bounds':final,'cpu_seconds_two_calls':time.process_time()-t})
 # Uneven dyadic endpoint regression: exact midpoint and radii are handled by
 # the unchanged Arb arithmetic; check a tiny asymmetric physical box.
 midpoint_box=[.1,math.nextafter(.1,math.inf),.3,math.nextafter(.3,math.inf)]
 midpoint_bounds=k.bounds(3,midpoint_box);assert all(math.isfinite(v) for v in midpoint_bounds)
 finishchildren=resource.getrusage(resource.RUSAGE_CHILDREN)
 childcpu=(finishchildren.ru_utime+finishchildren.ru_stime)-(children.ru_utime+children.ru_stime)
 sources=[ck.build_snapshot.identity(p) for p in sorted(pathlib.Path(__file__).parent.glob('*')) if p.is_file()]
 report={'status':'bounded gate PASS' if all(r['valid'] for r in leaf_tests) else 'bounded gate FAILED; no whole replay authorized',
  'input_head':'bda45a4c1392bea87de0841b6b23e5c35b2a694b','candidate_sha256':hashlib.sha256(raw).hexdigest(),
  'candidate_bytes':len(raw),'baseline_receipt_sha256':hashlib.sha256(oldraw).hexdigest(),
  'ratio_controls':ratio_tests,'primitive_controls':primitive_tests,'disjoint_intersection_rejected':True,
  'strict_json_rejections':rejected,'leaf_gate':leaf_tests,'midpoint_box':midpoint_box,'midpoint_bounds':midpoint_bounds,
  'build_provenance':k.provenance,'sources':sources,'checker_cpu_seconds':time.process_time()-start,'compiler_child_cpu_seconds':childcpu,
  'scope':'bounded controls only; numerical reference comparisons are diagnostic, separate source/math review required before full original-tree replay'}
 out=OUT/'hybrid-bounded-full.json';out.write_text(json.dumps(report,indent=2)+'\n')
 compact={key:report[key] for key in ['status','input_head','candidate_sha256','candidate_bytes','baseline_receipt_sha256','disjoint_intersection_rejected','strict_json_rejections','leaf_gate','sources','checker_cpu_seconds','compiler_child_cpu_seconds','scope']}
 compact['ratio_controls_count']=len(ratio_tests);compact['primitive_controls_count']=len(primitive_tests)
 compact['full_receipt']={'path':str(out.relative_to(ROOT)),'bytes':out.stat().st_size,'sha256':hashlib.sha256(out.read_bytes()).hexdigest()}
 compact['binary_sha256']=k.provenance['checker_binary']['sha256']
 evidence=ROOT/'topics/padua-argmax-bridge-20261105/evidence/phase-checker-round4-bounded.json';evidence.write_text(json.dumps(compact,indent=2)+'\n')
 print(json.dumps({'status':report['status'],'leaf_gate':leaf_tests,'checker_cpu_seconds':report['checker_cpu_seconds'],'compiler_child_cpu_seconds':childcpu},indent=2))
if __name__=='__main__':main()
