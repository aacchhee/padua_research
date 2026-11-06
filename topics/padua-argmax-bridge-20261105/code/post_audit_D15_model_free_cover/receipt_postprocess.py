"""D15 separately authorized <=2CPU metadata preservation, OUTSIDE FREEZE.
Reads retained data only. No runtime/producer/Native/ctypes import or native job.
The primary no-retry command is consumed; this helper cannot repeat it.
"""
import argparse,hashlib,json,math,os,pathlib,resource
from fractions import Fraction as F
import checker as C
HERE=pathlib.Path(__file__).resolve().parent;ROOT=HERE.parents[3]
RAW=ROOT/'local-output/argmax-bridge-20261105/post-audit-D15/model-free-cover'
EVID=ROOT/'topics/padua-argmax-bridge-20261105/evidence'
ATT=ROOT/'topics/padua-argmax-bridge-20261105/attempts/D15-model-free-cover.md'
LOG=ROOT/'topics/padua-argmax-bridge-20261105/LOG.md'
COMMAND='python3 topics/padua-argmax-bridge-20261105/code/post_audit_D15_model_free_cover/receipt_postprocess.py --run-once'
GEN='OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 topics/padua-argmax-bridge-20261105/code/post_audit_D15_model_free_cover/controller.py --run-once'
RECEIPT_SHA='6be2926071f43d2a619784c16b15c980e6952eaa3cfe4bab0703c14dcc6b3481'

def cpu():
 return sum(resource.getrusage(k).ru_utime+resource.getrusage(k).ru_stime for k in (resource.RUSAGE_SELF,resource.RUSAGE_CHILDREN))
def identity(path):
 p=pathlib.Path(path).resolve();data=p.read_bytes()
 return {'path':str(p),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
def load(path):
 def pairs(rows):
  out={}
  for k,v in rows:
   if k in out:raise ValueError('duplicate JSON key')
   out[k]=v
  return out
 def invalid(x):raise ValueError('nonfinite JSON constant')
 return json.loads(path.read_text(),object_pairs_hook=pairs,parse_constant=invalid)
def exclusive(path,obj):
 data=(json.dumps(obj,indent=2,allow_nan=False)+'\n').encode()
 with path.open('xb') as stream:stream.write(data)
 return identity(path)
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--run-once',action='store_true');args=ap.parse_args()
 if not args.run_once:raise RuntimeError('explicit metadata-only --run-once required')
 resource.setrlimit(resource.RLIMIT_CPU,(2,2))
 exclusive(RAW/'preservation-registration.json',{'command':COMMAND,'source':identity(__file__),'hard_CPU':2,'separate_metadata_allocation':True,'native_calls':0})
 freeze=load(HERE/'FREEZE.json');sources=load(HERE/'SOURCES.json');reg=load(RAW/'preregistration.json')
 assert reg['freeze']==identity(HERE/'FREEZE.json')
 verified=set()
 def check(row):
  key=(row['path'],row['sha256'])
  if key in verified:return
  path=pathlib.Path(row['path']);path=path if path.is_absolute() else ROOT/path
  got=identity(path)
  assert (got['bytes'],got['sha256'])==(row['bytes'],row['sha256']),str(path)
  verified.add(key)
 for row in freeze['code_data']+sources['immutable_code_data_dependencies']:check(row)
 for stage in ('producer','checker'):
  build=load(RAW/(stage+'-build.json'))
  for key in ('source_origin','source_snapshot','linkage_wrapper','preprocessed_translation_unit','checker_binary'):
   if isinstance(build.get(key),dict):check(build[key])
  for key in ('toolchain','toolchain_dependency_closure','headers','linked_dependency_closure','dependency_inputs'):
   for row in build.get(key,[]):check(row)
  before=load(RAW/(stage+'-runtime-before.json'));after=load(RAW/(stage+'-runtime-after.json'))
  assert before['loaded']==after['loaded'] and before['all_file_mappings']==after['all_file_mappings']
  for row in after['loaded']+after['all_file_mappings']:check(row)
  supervisor=load(RAW/(stage+'-supervisor.json'));desc=load(RAW/(stage+'-descendants.json'))
  assert supervisor['complete'] and supervisor['returncode']==0 and supervisor['stop'] is None
  assert supervisor['accounting_complete'] and desc['complete'];check(supervisor['checkpoint'])
 final=load(RAW/'final-accounting.json');summary=load(RAW/'summary.json')
 assert final['result']=='EXACT_COVER_ACCEPTED_PENDING_INDEPENDENT_REPLAY' and final['complete'] and final['first_failure'] is None
 assert summary['result']=='PROVISIONAL_COVER_PENDING_FINAL_ACCOUNTING' and summary['first_failure'] is None
 limit=final['final_self_limit'];assert limit['no_live_children'] and not limit['additional_reaped']
 assert limit['waited_child_CPU']+limit['absolute_self_CPU_hard']<=397 and final['total_CPU_through_summary']<398
 rawreceipt=RAW/'essential-receipt.json';rawtree=RAW/'certificate.json'
 assert identity(rawreceipt)['sha256']==RECEIPT_SHA
 assert rawreceipt.stat().st_size+rawtree.stat().st_size<16384
 receipt=load(rawreceipt);document=load(rawtree);exact=load(RAW/'checker-checkpoint.json')
 assert receipt['n']==document['n']==2048 and exact['status']=='COMPLETE' and exact['active_call'] is None
 assert receipt['freeze']==identity(HERE/'FREEZE.json');check(receipt['certificate']);check(receipt['raw_checkpoint'])
 points={};lower={};actual={};countrows={'S':[],'lambda':[]}
 assert len(receipt['rows'])==len(exact['completed_calls'])
 for row,call in zip(receipt['rows'],exact['completed_calls']):
  api,a,b,lh,uh,rh,counts,cost=row;key=(F(a),F(b));xs=list(map(float.fromhex,(lh,uh,rh)))
  assert call['api']==api and call['key']==a+','+b and call['n']==2048
  assert call['native']=={'returncode':0,'raw_hex':[lh,uh,rh],'counts':counts} and call['cpu_seconds']==cost
  assert all(map(math.isfinite,xs)) and xs[0]<=xs[1] and xs[2]>=0 and 0<=cost<=20
  assert call['point']['binary64_hex']==[lh,uh,rh]
  assert [call['point'][k] for k in ('lower','upper','radius')]==list(map(lambda x:str(F.from_float(x)),xs))
  assert all(type(x) is int and x>=0 for x in counts)
  if api=='S':
   assert len(counts)==6 and key==C.canonical(*key) and key not in points
   points[key]=F.from_float(xs[1]);lower[key]=F.from_float(xs[0])
  else:
   assert api=='lambda' and len(counts)==13 and key not in actual
   actual[key]=F.from_float(xs[1])
  countrows[api].append(counts)
 assert set(actual)=={(F(1,8192),F(0)),(F(0),F(1,10928)),(F(1,8192),F(1,10928))}
 grid=[]
 for a,b in C.grid():
  key=C.canonical(a,b);grid.append({'raw':list(map(str,(a,b))),'canonical':list(map(str,key)),'upper':str(points[key])})
 M,norm=C.norm_from_grid([F(row['upper']) for row in grid]);assert receipt['norm']=={'grid':grid,**norm}
 L=lower[(F(0),F(0))];assert receipt['L']==str(L)
 witness=C.corner_witness(L,[actual[k] for k in ((F(1,8192),F(0)),(F(0),F(1,10928)),(F(1,8192),F(1,10928)))],M)
 assert receipt['corner']==exact['corner_premise']==witness
 used=set()
 def oracle(key):
  n,a,b=key;assert n==2048;used.add((a,b));return points[a,b]
 metadata_identity='retained-metadata-only'
 normkeys={C.canonical(a,b) for a,b in C.grid()}
 cache={(metadata_identity,2048,*key):points[key] for key in normkeys}
 cover=C.verify_certificate(document,L,oracle,M,metadata_identity,cache)
 assert cover==receipt['cover']==exact['verification'] and used|{C.canonical(a,b) for a,b in C.grid()}==set(points)
 tokens=document['preorder'];index=0;depthmax=0
 def depth(d):
  nonlocal index,depthmax
  token=tokens[index];index+=1;depthmax=max(depthmax,d)
  if token!='.':depth(d+1);depth(d+1)
 depth(0);assert index==len(tokens)
 for row in freeze['code_data']+sources['immutable_code_data_dependencies']:check(row)
 # Whole raw manifest stays off Git; no output splitting to evade16KiB.
 rawmanifest=[]
 for path in sorted(RAW.rglob('*')):
  if path.is_file():
   row=identity(path);row['entry']=str(path.relative_to(RAW))
   if path.is_symlink():row['symlink_target']=os.readlink(path)
   rawmanifest.append(row)
 manifestid=exclusive(RAW/'preservation-raw-manifest.json',{'root':str(RAW),'files':rawmanifest,'scope':'All raw files before this manifest/output completion; whole caches/builds retained. Content-addressed cold archive pending root selection.'})
 for raw,dest in ((rawreceipt,EVID/'d15-model-free-cover.json'),(rawtree,EVID/'d15-model-free-cover-tree.json')):
  with dest.open('xb') as out:out.write(raw.read_bytes())
 assert '### D15 primary2048 execution observed by root' in LOG.read_text()
 assert 'exec session97483' in LOG.read_text() and 'directly observed process EXIT0' in LOG.read_text()
 observed='Root directly observed process EXIT0 in exec session97483 and separately read successful final accounting; helper did not infer exit from provisional summary.'
 finalreceipt={'status':'MEASURED complete primary; independent fresh native replay and global2048 adoption pending','release_commit':'0768cb93c4f829faf5f38d47cdd7e33faad8bf64','generating_command':GEN,'metadata_command':COMMAND,'metadata_helper':identity(__file__),'primary_process_exit':{'returncode':0,'attribution':observed,'canonical_root_record':'topics/padua-argmax-bridge-20261105/LOG.md#d15-primary2048-execution-observed-by-root'},'final_accounting':final,'raw_final_accounting':identity(RAW/'final-accounting.json'),'essential_receipt':identity(EVID/'d15-model-free-cover.json'),'essential_tree':identity(EVID/'d15-model-free-cover-tree.json'),'raw_manifest':manifestid,'raw_location':str(RAW),'recheck':{'distinct_identity_records':len(verified),'compiler_headers_preprocessed_binary_loaded_mappings':'PASS metadata identity recheck','retained_hex_fraction_norm_corner_tree':'PASS; retained data only, no fresh enclosure','max_depth':depthmax,'S_points':len(points),'actual_lambda_points':len(actual),'counts_sum':{api:[sum(row[i] for row in rows) for i in range(len(rows[0]))] for api,rows in countrows.items()}},'pure_preflight_CPU':{'author_sample':0.061098,'independent_whole_process':0.084,'shared_reserved':2},'separate_metadata_CPU':{'hard_cap':2,'before_final_receipt_serialization':cpu()},'retention':'Full raw manifest/caches/builds/maps remain whole off Git; cold archive endpoint/retrieval pending root. Clean fresh native replay uses repository sources and essential exact rows/tree; no old binary prerequisite.','limitations':'Receipt status remains provisional internally; successful final accounting AND root-observed return0 establish primary completion only. No independent native rerun here, no speedup ratio or general solver guarantee.'}
 exclusive(EVID/'d15-model-free-cover-final-accounting.json',finalreceipt)
 prefix=ATT.read_bytes()
 addition=('\n## D15 primary metadata preservation — 2026-11-06\n\nRoot executed frozen0768cb9 once and explicitly observed exit0 plus successful\nfinal-accounting; provisional summary is not acceptance. Primary complete only,\nindependent fresh native replay/theorem application and root global2048 adoption\npending. Exact raw11491B receipt and142B tree copied unchanged to evidence.\nPostprocessor outside FREEZE ran once under separate2CPU RLIMIT: identity,\nretained hex/Fraction norm/corner/tree checks only; no native/phase/compiler job.\nMceil42;77nodes/39leaves(5NEAR,32FAR,2OUTSIDE),51canonicalSpoints+3actuallambda.\nProducer54.263514CPU/checker175.307516CPU, through-summary229.616251CPU;\nfinal hard self186 after waited-child210.482649CPU, no failure/retry/coststop.\nExact endpoints/counters, full raw manifest, source/build/mapped closure and\nfinal-accounting linkage preserved. Cold archive remains pending; no raw splitting\nor unmatched-case speedup comparison. FLOAT producer54CPU remains a potential\nfuture optimization target, not a changed source in this run.\n').encode()
 with ATT.open('ab') as out:out.write(addition)
 completion=exclusive(RAW/'preservation-completion.json',{'result':'PASS metadata preservation only','CPU_before_completion':cpu(),'hard_CPU':2,'native_calls':0,'attempt_prefix':{'bytes':len(prefix),'sha256':hashlib.sha256(prefix).hexdigest()},'essential':[identity(EVID/name) for name in ('d15-model-free-cover.json','d15-model-free-cover-tree.json','d15-model-free-cover-final-accounting.json')],'norm':norm,'corner':witness,'cover':cover,'max_depth':depthmax,'lambda_counts':countrows['lambda'],'distinct_identity_records':len(verified)})
 print(json.dumps({'completion':completion,'CPU_before_final_print':cpu(),'norm':norm,'corner':witness,'cover':cover,'max_depth':depthmax,'lambda_counts':countrows['lambda']}))
if __name__=='__main__':main()
