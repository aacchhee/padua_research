"""D12 <=2CPU metadata-only postprocess; outside primary D11 freeze.
No compiler, Native, CDLL, producer, phase evaluation or native rerun.
Retained point enclosures are data, not independently recomputed arithmetic.
"""
import hashlib,json,math,pathlib,resource,sys
from fractions import Fraction as F
import checker as C
HERE=pathlib.Path(__file__).resolve().parent;ROOT=HERE.parents[3]
RAW=ROOT/'local-output/argmax-bridge-20261105/post-audit-D11/point-cover'
EVID=ROOT/'topics/padua-argmax-bridge-20261105/evidence'
ATT=ROOT/'topics/padua-argmax-bridge-20261105/attempts/D11-point-cover.md'
COMMAND='python3 topics/padua-argmax-bridge-20261105/code/post_audit_D11_point_cover/receipt_postprocess.py --run-once'
GEN='OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 topics/padua-argmax-bridge-20261105/code/post_audit_D11_point_cover/controller.py --run-once'

def identity(path):
 p=pathlib.Path(path).resolve();b=p.read_bytes()
 return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def load(p):return json.loads(pathlib.Path(p).read_text())
def check(row):
 got=identity(ROOT/row['path'])
 if got['sha256']!=row['sha256'] or got['bytes']!=row['bytes']:raise ValueError('identity mismatch '+row['path'])
def save_exclusive(p,obj):
 data=(json.dumps(obj,indent=2,allow_nan=False)+'\n').encode()
 if p.parent==EVID and len(data)>=16384:raise ValueError('essential evidence byte cap')
 with p.open('xb') as out:out.write(data)

def main():
 if sys.argv[1:]!=['--run-once']:raise RuntimeError('explicit metadata-only --run-once required')
 resource.setrlimit(resource.RLIMIT_CPU,(2,2))
 save_exclusive(RAW/'postprocess-registration.json',{'command':COMMAND,'helper':identity(__file__),'hard_CPU':2,'scope':'separately authorized metadata after primary; zero native calls'})
 freeze=load(HERE/'FREEZE.json');sources=load(HERE/'SOURCES.json')
 reg=load(RAW/'preregistration.json');assert reg['freeze']==identity(HERE/'FREEZE.json')
 for row in freeze['code_data']+sources['immutable_code_data_dependencies']:check(row)
 manifests={};verified=set()
 def check_once(row):
  key=(row['path'],row['sha256'])
  if key not in verified:check(row);verified.add(key)
 for stage in ('producer','checker'):
  m=load(RAW/(stage+'-build.json'));manifests[stage]=m
  for key in ('source_origin','source_snapshot','linkage_wrapper','preprocessed_translation_unit','checker_binary'):
   if isinstance(m.get(key),dict):check_once(m[key])
  for key in ('toolchain','toolchain_dependency_closure','headers','linked_dependency_closure','dependency_inputs'):
   for row in m.get(key,[]):check_once(row)
  before=load(RAW/(stage+'-runtime-before.json'));after=load(RAW/(stage+'-runtime-after.json'))
  assert before['loaded']==after['loaded'] and before['all_file_mappings']==after['all_file_mappings']
  for row in after['all_file_mappings']:check_once(row)
  supervisor=load(RAW/(stage+'-supervisor.json'));desc=load(RAW/(stage+'-descendants.json'))
  assert supervisor['complete'] and supervisor['accounting_complete'] and desc['complete'] and supervisor['returncode']==0 and supervisor['stop'] is None
  check_once(supervisor['checkpoint'])
 summary=load(RAW/'summary.json');account=load(RAW/'final-accounting.json')
 assert summary['result']=='EXACT_COVER_ACCEPTED_PENDING_INDEPENDENT_REPLAY' and summary['first_failure'] is None and account['complete']
 prod=load(RAW/'producer-checkpoint.json');exact=load(RAW/'checker-checkpoint.json')
 assert prod['status']==exact['status']=='COMPLETE' and exact['active_call'] is None and prod['active_call'] is None
 assert prod['certificate']==identity(RAW/'certificate.json')
 certbytes=(RAW/'certificate.json').read_bytes();document=load(RAW/'certificate.json')
 assert len(certbytes)<16384 and set(document)=={'format','n','preorder'} and document['format']=='D11-midpoint-v1' and document['n']==512
 # Retained endpoint binary64 replay only. No fresh point computation.
 points={};counts=[];times=[]
 for call in exact['completed_calls']:
  native=call['native'];assert native['returncode']==0
  xs=list(map(float.fromhex,native['raw_hex']))
  assert len(xs)==3 and all(map(math.isfinite,xs)) and xs[0]<=xs[1] and xs[2]>=0
  p=call['point'];assert p['binary64_hex']==native['raw_hex']
  assert [str(F.from_float(x)) for x in xs]==[p[k] for k in ('lower','upper','radius')]
  a,b=map(F,call['key'].split(','));assert (a,b)==C.canonical(a,b) and (a,b) not in points
  points[a,b]=F(p['upper']);ct=native['counts'];assert len(ct)==6 and all(type(x) is int and x>=0 for x in ct)
  counts.append(ct);times.append(call['cpu_seconds']);assert 0<=times[-1]<=20
 receipt=load(ROOT/'topics/padua-argmax-bridge-20261105/evidence/d09-threepoint.json')
 L,witness=C.corner_witness(receipt);assert witness==exact['corner_premise']
 tokens=document['preorder'];index=0;leaf_counts={};margins={};used=set();maxdepth=0
 def keep(mode,gap):
  assert gap>0
  margins[mode]=min(margins.get(mode,gap),gap)
 def walk(box,depth):
  nonlocal index,maxdepth
  assert index<len(tokens) and depth<=64
  maxdepth=max(maxdepth,depth);token=tokens[index];index+=1
  al,ah,bl,bh=box
  if token=='.':
   low=al+bl;high=min(ah+bh,F(1))
   if low>1:mode='OUTSIDE'
   else:
    keys=[C.canonical(a,b) for a in (al,ah) for b in (bl,bh)];used.update(keys)
    upper=max(points[k] for k in keys)+F(34)*F(22,7)**2*((ah-al)**2+F(512,513)**2*(bh-bl)**2)/8
    if upper<L:mode='FAR';keep(mode,L-upper)
    elif 2*F(22,7)*high<=1 and upper-F(1,32)<L:mode='NEAR';keep(mode,L-upper+F(1,32))
    else:
     mode='SPLIT'
     if low<=1/(2*F(157,50)):keep('SPLIT_NEAR',L-upper+F(1,32))
     if high>=1/(2*F(22,7)):keep('SPLIT_FAR',L-upper)
   leaf_counts[mode]=leaf_counts.get(mode,0)+1;return
  assert token in 'ab'
  if token=='a':
   t=(al+ah)/2;walk((al,t,bl,bh),depth+1);walk((t,ah,bl,bh),depth+1)
  else:
   t=(bl+bh)/2;walk((al,ah,bl,t),depth+1);walk((al,ah,t,bh),depth+1)
 walk((F(0),F(1),F(0),F(1)),0)
 assert index==len(tokens) and used==set(points) and index==exact['verification']['visited'] and len(points)==exact['verification']['vertices'] and leaf_counts==exact['verification']['leaf_counts']
 assert index<=2048 and len(points)<=384
 for row in freeze['code_data']+sources['immutable_code_data_dependencies']:check(row)
 treepath=EVID/'d12-point-cover-tree.json'
 with treepath.open('xb') as out:out.write(certbytes)
 rawmanifest=[identity(p) for p in sorted(RAW.iterdir()) if p.is_file() and p.name not in ('postprocess-registration.json',)]
 prefix=ATT.read_bytes()
 addition=('\n2026-11-06 D12 actual primary outcome (metadata postprocess only).\n'
 'Frozen release e13a538bda80e6cc785f4835937b2ca338bc1d6f executed once by root;\n'
 'producer COMPLETE, checker COMPLETE, no first failure or cap stop, full\n'
 'descendant accounting. Exact tree has83nodes/42leaves:8NEAR,31FAR,3OUTSIDE;\n'
 '53distinct canonical C11 vertices. Producer4.503105CPU, checker40.079552CPU;\n'
 'primary sample44.626053CPU, through-summary sample44.626205CPU, wall41.286455s.\n'
 'Every required exact strict margin is positive; finite values and source/build/\n'
 'all-loaded-file identities rechecked by separate <=2CPU metadata helper.\n'
 'No native repeat or historical-case speedup ratio is asserted. Essential\n'
 'evidence/d12-point-cover.json and exact d12-point-cover-tree.json retained;\n'
 'raw caches/builds remain local with hash manifest, archival retrieval pending.\n'
 'This is a successful primary finite adapter computation, pending distinct\n'
 'fresh fixed-certificate native replay and mathematical application review;\n'
 'no full global512 adoption is made here. Frozen primary sources unchanged.\n').encode()
 outreceipt={'status':'MEASURED primary exact finite-cover acceptance; independent fresh native replay and mathematical application pending','release_commit':'e13a538bda80e6cc785f4835937b2ca338bc1d6f','generating_command':GEN,'metadata_command':COMMAND,'freeze':identity(HERE/'FREEZE.json'),'sources':identity(HERE/'SOURCES.json'),'postprocessor':identity(__file__),'essential_certificate':identity(treepath),'corner_computational_premise':identity(ROOT/'topics/padua-argmax-bridge-20261105/evidence/d09-threepoint.json'),'verification':{'nodes':index,'internal_nodes':index-sum(leaf_counts.values()),'leaves':sum(leaf_counts.values()),'leaf_counts':leaf_counts,'distinct_canonical_vertices':len(points),'max_depth':maxdepth,'minimum_strict_margin_by_required_predicate':{k:str(v) for k,v in margins.items()},'minimum_strict_margin':str(min(margins.values())),'retained_endpoint_hex_replay':'PASS; no fresh point evaluation','native_count_columns':['retained','direct','blocks','maxdirect','maxblocks','ordinary'],'native_count_sums':[sum(c[k] for c in counts) for k in range(6)],'native_count_maxima':[max(c[k] for c in counts) for k in range(6)],'completed_native_calls':len(times),'maximum_completed_call_CPU':max(times),'source_build_mapped_identity_recheck':'PASS','distinct_identity_rows_checked':len(verified)},'CPU':{'producer_inclusive':summary['stages'][0]['inclusive_CPU_with_supervision'],'checker_inclusive':summary['stages'][1]['inclusive_CPU_with_supervision'],'primary_sample':summary['total_waited_descendant_CPU_before_summary'],'primary_through_summary_sample':account['total_CPU_through_summary'],'primary_final_write_note':'Final tiny accounting write/print outside last sample; bounded by supervisor RLIMIT_CPU398.','root_pure_preflight':0.05421,'shared_pure_reserved':2,'primary_gate':400,'metadata_separate_hard_cap':2,'metadata_before_receipt_serialization':sum(resource.getrusage(k).ru_utime+resource.getrusage(k).ru_stime for k in (resource.RUSAGE_SELF,resource.RUSAGE_CHILDREN))},'wall_seconds':summary['wall_seconds'],'accounting_complete':True,'raw_artifacts':rawmanifest,'retention_retrieval':{'location':str(RAW),'retention':'Keep full raw caches/builds/maps locally; AC-selected cold-storage export pending, no permanent retrieval claim.','essential_scope':'Clean-clone fresh checker needs repository code/freeze/dependencies, essential tree and accepted repository D09 receipt; old raw cache and old binaries are not proof premises.','fresh_checker_command':'Pending independent reviewer-owned fixed-certificate fresh-build command; primary command above is consumed and MUST NOT be rerun.','no_splitting':'Raw producer19038B/checker37857B caches remain whole off Git.'},'attempt_before_addendum':{'bytes':len(prefix),'sha256':hashlib.sha256(prefix).hexdigest()},'attempt_after_addendum':{'bytes':len(prefix+addition),'sha256':hashlib.sha256(prefix+addition).hexdigest()},'limitations':'No native rerun in postprocess; endpoints are retained data. No global theorem adoption, new degree or historical speedup comparison. Compiler/runtime identities are checked, no hermeticity claim.'}
 save_exclusive(EVID/'d12-point-cover.json',outreceipt)
 with ATT.open('ab') as out:out.write(addition)
 print(json.dumps({'receipt':identity(EVID/'d12-point-cover.json'),'certificate':identity(treepath),'verification':outreceipt['verification'],'metadata_CPU_before_final_print':sum(resource.getrusage(k).ru_utime+resource.getrusage(k).ru_stime for k in (resource.RUSAGE_SELF,resource.RUSAGE_CHILDREN))}))
if __name__=='__main__':main()
