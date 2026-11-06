#!/usr/bin/env python3
"""C10 prepare/one-shot known-n32 cheap producer. No checker execution.
Execution requires separate review, publication and coordinator release.
"""
import argparse,collections,ctypes,gzip,hashlib,json,math,os,pathlib,resource,secrets,signal,subprocess,sys,time
ROOT=pathlib.Path(__file__).resolve().parents[4]
TOPIC=ROOT/'topics/padua-argmax-bridge-20261105'
HERE=pathlib.Path(__file__).resolve().parent
WORK=ROOT/'local-output/argmax-bridge-20261105/cheap-C10-producer/n32'
LIMITS=dict(total_cpu=90,watchdog_cpu=86,worker_cpu=84,search_total_cpu=78,visits=2048,leaves=1024,pending=2052,depth=32,raw_bytes=262144,compact_bytes=131072,gzip_bytes=16383,trace_bytes=2097152,stream_bytes=65536,wall_seconds=180)

def identity(path):
 p=pathlib.Path(path).resolve();b=p.read_bytes();return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def require(ok,message):
 if not ok:raise RuntimeError(message)
def write_new(path,data):
 with pathlib.Path(path).open('x') as f:json.dump(data,f,indent=2,allow_nan=False);f.write('\n')
def verify(entries):
 for e in entries:require(identity(e['path'])==e,'identity changed: '+e['path'])
def child_cpu():
 r=resource.getrusage(resource.RUSAGE_CHILDREN);return r.ru_utime+r.ru_stime

def inputs():
 entries=[]
 for rel,sha in json.loads((HERE/'pins.json').read_bytes()).items():
  e=identity(ROOT/rel);require(e['sha256']==sha,'frozen input mismatch '+rel);entries.append(e)
 return entries

def publication(commit,entries):
 require(len(commit)==40 and not set(commit)-set('0123456789abcdef'),'full source commit required')
 for e in entries:
  rel=str(pathlib.Path(e['path']).relative_to(ROOT));r=subprocess.run(['git','cat-file','blob',commit+':'+rel],cwd=ROOT,capture_output=True,timeout=10)
  require(r.returncode==0 and len(r.stdout)==e['bytes'] and hashlib.sha256(r.stdout).hexdigest()==e['sha256'],'publication mismatch '+rel)

def group_cpu(pgid):
 ticks=0
 for p in pathlib.Path('/proc').iterdir():
  if not p.name.isdecimal():continue
  try:
   f=(p/'stat').read_text().rsplit(')',1)[1].split()
   if int(f[2])==pgid:ticks+=sum(int(f[i]) for i in (11,12,13,14))
  except (FileNotFoundError,ProcessLookupError):pass
 return ticks/os.sysconf('SC_CLK_TCK')

def imports():
 allowed={pathlib.Path(e['path']) for e in inputs() if e['path'].endswith('.py')}|{pathlib.Path(__file__).resolve()};paths=set()
 for m in tuple(sys.modules.values()):
  name=getattr(m,'__file__',None)
  if name:
   p=pathlib.Path(name).resolve()
   if p.is_relative_to(ROOT):paths.add(p)
 require(paths<=allowed,'unrecorded project import '+str(paths-allowed));return [identity(p) for p in sorted(paths)]

def load_builder():
 original=TOPIC/'code/cheap_C08_mpfr/build.py';text=original.read_text();old="OUT=ROOT/'local-output/argmax-bridge-20261105/cheap-C08-mpfr'";new="OUT=ROOT/'local-output/argmax-bridge-20261105/cheap-C10-producer/n32/build'"
 require(text.count(old)==1,'builder adaptation anchor');text=text.replace(old,new);snapshot=WORK/'builder_snapshot.py'
 with snapshot.open('x') as f:f.write(text)
 ns={'__file__':str(original)};exec(compile(text,str(snapshot),'exec'),ns)
 binary,manifest=ns['build']();manifest['executed_builder']=identity(snapshot);manifest['adaptation']='output directory only; C08 source/header and compiler arithmetic unchanged'
 return binary,manifest,ns

def full_closure(manifest):
 e=[manifest[k] for k in ('source','header','preprocessed','binary','executed_builder')]
 for key in ('original_sources','tools','tool_runtime_closure','headers','linked_runtime_closure','actual_loaded_mappings'):
  require(bool(manifest[key]),'missing closure '+key);e.extend(manifest[key])
 return e

def worker(token):
 resource.setrlimit(resource.RLIMIT_CPU,(84,85));start=time.process_time();before=child_cpu();launch=json.loads((WORK/'launch.json').read_bytes())
 require(token==launch['token'] and os.getppid()==launch['supervisor_pid'] and os.getpid()==os.getpgrp(),'worker must be supervised once')
 report=dict(status='FAIL',complete=False,accepted=False,n=32);trace=None;manifest=None
 try:
  pins=inputs();require(pins==launch['inputs'],'launch inputs changed');verify(pins+[launch['controller'],launch['pins_file']])
  sys.path.insert(0,str(TOPIC/'code'));import n3_bootstrap_r8 as legacy
  moduleids=imports();premise=legacy.range_premise();energy=legacy.published_bootstrap_premise()
  require(premise is not None and energy is not None,'fixed premise missing')
  binary,manifest,build=load_builder();lib=ctypes.CDLL(str(binary));manifest['actual_loaded_mappings']=build['loaded'](manifest);verify(full_closure(manifest))
  ptr=ctypes.POINTER(ctypes.c_double);lib.n3_box.argtypes=[ctypes.c_int]+[ctypes.c_double]*6+[ctypes.c_int,ptr];lib.n3_box.restype=ctypes.c_int
  lib.n3_geometry.argtypes=[ctypes.c_int]+[ctypes.c_double]*4;lib.n3_geometry.restype=ctypes.c_int;lib.n3_constants.argtypes=[ctypes.c_int,ptr]
  lib.n3_mpfr_version.restype=ctypes.c_char_p;lib.c08_counts.argtypes=[ptr]
  write_new(WORK/'build-manifest.json',manifest);constants=(ctypes.c_double*4)();lib.n3_constants(32,constants)
  require(all(math.isfinite(v) for v in constants) and 3<constants[0]<constants[1]<4 and 1<constants[2]<=constants[3],'invalid constants')
  counter_reset=(ctypes.c_double*10)();lib.c08_counts(counter_reset)
  n=32;pi=constants[1];lc=constants[2];roots=[(a,b,c,d) for a,b in [(-pi,0.),(0.,pi)] for c,d in [(-pi,0.),(0.,pi)]]
  q=collections.deque((r,'',b) for r,b in enumerate(roots));leaves=[];counts=collections.Counter();visited=splits=native=0;stop=None
  trace=(WORK/'native-calls.jsonl').open('x')
  while q:
   if time.process_time()-start+child_cpu()-before>=LIMITS['search_total_cpu']:stop='CPU';break
   if visited>=LIMITS['visits'] or len(leaves)>=LIMITS['leaves'] or len(q)>LIMITS['pending']:stop='tree cap';break
   root,path,box=q.popleft();visited+=1;geometry=lib.n3_geometry(n,*box);require(geometry in (0,1,2),'geometry guard rejected original root descendant')
   if geometry==1:leaves.append(dict(root=root,path=path,kind='outside'));counts['outside']+=1;continue
   local=geometry==2 or legacy.local_range(n,box);bootstrap=legacy.bootstrap_range(n,box);t=time.process_time()
   values=legacy.producer_bounds(lib,n,box,lc,always_compute_defect=local or bootstrap);native+=1;counter=(ctypes.c_double*10)();lib.c08_counts(counter)
   record=dict(call=native,root=root,path=path,box=box,bounds=values,counters=list(counter),cpu=time.process_time()-t);trace.write(json.dumps(record,allow_nan=False)+'\n');trace.flush();require(trace.tell()<=LIMITS['trace_bytes'],'trace cap')
   su,cu,dl=values[:3]
   # Original r8 priority and directed binary64 strict tests, unchanged.
   if su<lc:kind='far'
   elif bootstrap and math.nextafter(su-dl,math.inf)<lc:kind='maximum-exclusion-plus-defect'
   elif (local or cu<lc) and math.nextafter(su-dl,math.inf)<lc:kind='local-corner-plus-defect' if local else 'corner-orbit-plus-defect'
   else:
    require(len(path)<LIMITS['depth'],'depth cap')
    al,ah,bl,bh=box
    if ah-al>=bh-bl:
     mid=al+(ah-al)/2;require(al<mid<ah,'unbisectable alpha');children=[(al,mid,bl,bh),(mid,ah,bl,bh)]
    else:
     mid=bl+(bh-bl)/2;require(bl<mid<bh,'unbisectable beta');children=[(al,ah,bl,mid),(al,ah,mid,bh)]
    splits+=1;counts['split']+=1
    for bit,b in enumerate(children):q.append((root,path+str(bit),b))
    continue
   leaves.append(dict(root=root,path=path,kind=kind,S_upper=su,corner_upper=cu,defect_lower=dl));counts[kind]+=1
  trace.close();pending=[dict(root=r,path=p) for r,p,_ in q];legacy_bootstrap=sys.modules['check_r8'];legacy_bootstrap.tree_partition(leaves+pending)
  require(legacy.range_premise()==premise and legacy.published_bootstrap_premise()==energy,'premise changed')
  data=dict(format='n3-phase-maximum-bootstrap-v2',mode='global-maximum-bootstrap',bootstrap_premise=legacy.bootstrap_descriptor(),n=n,complete=not q,accepted=False,constants=list(constants),roots=roots,leaves=leaves,pending=pending,statistics=dict(visited=visited,splits=splits,counts=dict(counts),cpu_seconds=time.process_time()-start),sources=[manifest['source'],manifest['header'],manifest['binary'],launch['controller']],build_manifest=identity(WORK/'build-manifest.json'),python=sys.version,mpfr=lib.n3_mpfr_version().decode(),compile_command=manifest['compile_command'],limits=LIMITS,fixed_corner_range=premise,acceptance='PENDING separate independent checker')
  raw=(json.dumps(data,separators=(',',':'),allow_nan=False)+'\n').encode();require(len(raw)<=LIMITS['raw_bytes'],'raw output cap');path=WORK/'n32-phase.json'
  with path.open('xb') as f:f.write(raw)
  path.chmod(0o444);report.update(complete=not q,pending=len(q),stop_reason=stop,visited=visited,native_calls=native,leaf_count=len(leaves),raw_candidate=identity(path),statistics=data['statistics'])
  if not q:
   compact=WORK/'n32-phase-compact.json';projected=legacy.compact_candidate(path,compact);require(projected['candidate']['bytes']<=LIMITS['compact_bytes'] and projected['gzip']['bytes']<=LIMITS['gzip_bytes'],'compact/gzip output cap')
   report.update(projected)
  verify(full_closure(manifest)+pins+moduleids+[launch['controller'],launch['pins_file']]);require(imports()==moduleids,'project imports changed');require(build['loaded'](manifest)==manifest['actual_loaded_mappings'],'loaded closure changed')
  report.update(status='PRODUCED_UNCHECKED' if not q else 'INCOMPLETE_FROZEN',closure_unchanged=True,project_modules=moduleids,build_manifest=identity(WORK/'build-manifest.json'))
 except Exception as exc:report.update(error=repr(exc),status='FAIL_FROZEN')
 finally:
  if trace is not None and not trace.closed:trace.close()
  report.update(own_cpu_before_serialization=time.process_time()-start,helper_cpu=child_cpu()-before,source_commit=launch['source_commit'])
  write_new(WORK/'producer-receipt.json',report)
 return 0 if report['status']=='PRODUCED_UNCHECKED' else 1

def supervisor(commit):
 start=time.monotonic();own=time.process_time();before=child_cpu();require(not WORK.exists(),'one-shot output already exists')
 pins=inputs();controller=identity(__file__);pinsfile=identity(HERE/'pins.json');publication(commit,pins+[controller,pinsfile]);WORK.mkdir(parents=True)
 token=secrets.token_hex(16);launch=dict(source_commit=commit,controller=controller,pins_file=pinsfile,inputs=pins,supervisor_pid=os.getpid(),token=token);write_new(WORK/'launch.json',launch)
 command=[sys.executable,str(pathlib.Path(__file__).resolve()),'--worker-token',token];stopped=False;peak=0.;pre=child_cpu()-before
 with (WORK/'stdout.txt').open('x') as out,(WORK/'stderr.txt').open('x') as err:
  process=subprocess.Popen(command,stdout=out,stderr=err,start_new_session=True)
  try:
   while process.poll() is None:
    cpu=group_cpu(process.pid)+pre+time.process_time()-own;peak=max(peak,cpu)
    if cpu>=LIMITS['watchdog_cpu'] or time.monotonic()-start>=LIMITS['wall_seconds'] or out.tell()+err.tell()>LIMITS['stream_bytes']:
     os.killpg(process.pid,signal.SIGKILL);stopped=True;break
    time.sleep(.1)
   code=process.wait()
  except BaseException:
   try:os.killpg(process.pid,signal.SIGKILL)
   except ProcessLookupError:pass
   process.wait();raise
 reportpath=WORK/'producer-receipt.json';report=json.loads(reportpath.read_bytes()) if reportpath.exists() else {};errors=[]
 try:
  verify(pins+[controller,pinsfile]);require(inputs()==pins,'pins changed after worker')
  if report.get('closure_unchanged'):
   verify([report['build_manifest']]);manifest=json.loads(pathlib.Path(report['build_manifest']['path']).read_bytes());verify(full_closure(manifest))
  if report.get('status')=='PRODUCED_UNCHECKED':verify([report['candidate'],report['gzip'],report['raw_candidate']])
 except Exception as exc:errors.append(repr(exc))
 total=child_cpu()-before+time.process_time()-own
 passed=code==0 and not stopped and not errors and total<=LIMITS['total_cpu'] and report.get('status')=='PRODUCED_UNCHECKED' and report.get('complete') is True and report.get('pending')==0 and report.get('closure_unchanged') is True
 result=dict(format='C10-known-n32-cheap-producer-v1',status='PRODUCED_UNCHECKED' if passed else 'FAIL_FROZEN',independent_acceptance=False,source_commit=commit,controller=controller,exit_status=code,watchdog_stopped=stopped,errors=errors,total_cpu=total,wall=time.monotonic()-start,peak_group_and_supervisor_cpu=peak,limits=LIMITS,producer_receipt=identity(reportpath) if reportpath.exists() else None,first_result=report)
 write_new(WORK/'supervisor-receipt.json',result)
 if passed:
  # This freezes a request. It never starts, authorizes, or accepts a checker.
  candidate=report['candidate'];verify([candidate,report['gzip']]);write_new(WORK/'checker-gate-request.json',dict(stage='PENDING independent wrapper review, publication and explicit root release',candidate=candidate,gzip=report['gzip'],n=32,expected_leaves=report['leaf_count'],checker='unchanged check_r8.check with separate C03 mode0 Arb kernel',checker_total_cpu_cap=180,producer_accepted=False,required_result='complete tree, all generated leaves checked, zero pending/failed, exact candidate and full source/input/runtime closure stable; accepted true only in independent checker receipt'))
 print(json.dumps({k:result[k] for k in ('status','exit_status','total_cpu','wall')}));return 0 if passed else 1

def main():
 p=argparse.ArgumentParser();p.add_argument('--plan',action='store_true');p.add_argument('--run-once',action='store_true');p.add_argument('--source-commit');p.add_argument('--worker-token');a=p.parse_args()
 if a.worker_token:return worker(a.worker_token)
 if a.plan:
  require(not a.run_once and not a.source_commit,'plan excludes execution');print(json.dumps(dict(stage='PREPARATION ONLY; no execution authorization',degree=32,limits=LIMITS,input_count=len(inputs()),new_tree_from_scratch=True,checker_automatic=False),indent=2));return 0
 require(a.run_once and a.source_commit,'explicit --run-once --source-commit SHA required after release');return supervisor(a.source_commit)
if __name__=='__main__':raise SystemExit(main())
