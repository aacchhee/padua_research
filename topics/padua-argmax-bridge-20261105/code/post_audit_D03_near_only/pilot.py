"""PROPOSED D03 pilot. No invocation has been authorized or executed.

Thin float-domain wrapper; unchanged C kernels. Never a rigorous certifier.
"""
import argparse,collections,ctypes,hashlib,json,math,os,pathlib,resource,shutil,signal,subprocess,sys,time
from fractions import Fraction as F
HERE=pathlib.Path(__file__).resolve().parent;ROOT=HERE.parents[3];TOPIC=HERE.parents[1]
OUT=ROOT/'local-output/argmax-bridge-20261105/post-audit-D03/near-only'
OLD=ROOT/'topics/padua-argmax-effective-2-20261105/code'
N=512;BOXES=128;CASE_CPU=720;TOTAL_CPU=1800
PINS={
 'topics/padua-argmax-bridge-20261105/code/n3_meanvalue.c':'4739e36d05d75ce4389118364a2e2a693d2b14d87a8b79e84aa5199d6bb6a86a',
 'topics/padua-argmax-effective-2-20261105/code/phase_probe.c':'692d4afd89d3bbda3bac3daaeef7c56aa4ecdde0f9cdd32b9fefa0e296adc365',
 'topics/padua-argmax-effective-2-20261105/code/box_pilot.c':'92f111e0c58c59de32490118a30d88b26de356a93e0ec7251928059e1f2f4d0b'}
def cpu():
 return sum(resource.getrusage(k).ru_utime+resource.getrusage(k).ru_stime for k in (resource.RUSAGE_SELF,resource.RUSAGE_CHILDREN))
def identity(p):
 p=pathlib.Path(p).resolve();return {'path':str(p),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
def save(p,x):
 temporary=p.with_name(p.name+'.tmp');temporary.write_text(json.dumps(x,indent=2,allow_nan=False)+'\n');temporary.replace(p)
def finite(*values):
 if not all(math.isfinite(x) for x in values):raise RuntimeError('nonfinite scalar reference or margin')
def minabs(a,b):return 0 if a<=0<=b else min(abs(a),abs(b))
def h3(n,b):
 # Exact rational sufficient guard for the inherited all-n physical radius.
 aa=max(abs(F(b[0])),abs(F(b[1])));bb=max(abs(F(b[2])),abs(F(b[3])))
 return aa*aa/(2*n*n)+bb*bb/(2*(n+1)**2)<=F(1,10**11*n*n)
def load(tag):
 lib=ctypes.CDLL(str(OUT/'pilot.so'));ptr=ctypes.POINTER(ctypes.c_double)
 lib.n3_box.argtypes=[ctypes.c_int,*([ctypes.c_double]*6),ctypes.c_int,ptr];lib.n3_box.restype=ctypes.c_int
 lib.n3_jet.argtypes=[ctypes.c_int,*([ctypes.c_double]*4),ptr]
 for name in ['phase_s','phase_lambda']:
  f=getattr(lib,name);f.argtypes=[ctypes.c_int,ctypes.c_double,ctypes.c_double];f.restype=ctypes.c_double
 paths={pathlib.Path(sys.executable).resolve()}
 for module in list(sys.modules.values()):
  p=getattr(module,'__file__',None)
  if p and pathlib.Path(p).is_file():paths.add(pathlib.Path(p).resolve())
 maps=pathlib.Path('/proc/self/maps').read_text();(OUT/(tag+'-loaded.maps')).write_text(maps)
 for line in maps.splitlines():
  p=line.split()[-1]
  if p.startswith('/') and pathlib.Path(p).is_file():paths.add(pathlib.Path(p).resolve())
 save(OUT/(tag+'-runtime.json'),{'loaded_files':[identity(p) for p in sorted(paths)],'python':sys.version,'double_bytes':ctypes.sizeof(ctypes.c_double),'python_float_mantissa_bits':sys.float_info.mant_dig,'python_float_radix':sys.float_info.radix})
 return lib
def bounds(lib,n,b,lc,eps,local):
 arr=(ctypes.c_double*6)();status=lib.n3_box(n,*b,lc,eps,int(local),arr)
 if status or not all(math.isfinite(x) for x in arr) or min(arr[:3])<0:raise RuntimeError('invalid native float result')
 return list(arr)
def control(lib):
 resource.setrlimit(resource.RLIMIT_CPU,(59,60));n=32;lc=lib.phase_lambda(n,math.pi,math.pi);cases=[]
 finite(lc)
 if lc<=0:raise RuntimeError('nonpositive corner reference')
 for a,b in [(0.,0.),(-1/32,0.),(0.,-1/32)]:
  box=[a,a,b,b];x=bounds(lib,n,box,lc,0.,h3(n,box));s=lib.phase_s(n,a,b)
  corner=lib.phase_lambda(n,math.pi+a/n,math.pi+b/(n+1));j,k=16,17
  noncorner=lib.phase_lambda(n,(j*math.pi+a)/n,(k*math.pi+b)/(n+1))
  finite(s,corner,noncorner)
  differences=[s-x[0],corner-x[1],x[2]-(s-noncorner)];finite(*differences)
  violation=max(*differences,0.)
  if violation>1e-10*(1+abs(s)):raise RuntimeError('n32 cross-formula control failed')
  cases.append({'phase':[a,b],'bounds':x,'S':s,'corner_lambda':corner,'noncorner_lambda':noncorner,'violation':violation})
 save(OUT/'controls.json',{'scope':'MEASURED separate point-sum formula controls, not interval validation','cases':cases,'cpu_seconds':cpu()})
def structural(leaves,pending,rho):
 start=time.process_time();groups=[set() for _ in range(4)]
 for row in leaves+pending:
  root,path=row['root'],row['path']
  if root not in range(4) or any(bit not in '01' for bit in path):raise RuntimeError('invalid partition address')
  r=F(rho);b=([-r,F(0)] if root<2 else [F(0),r])+([-r,F(0)] if root%2==0 else [F(0),r])
  for bit in path:
   i=0 if b[1]-b[0]>=b[3]-b[2] else 2;mid=(b[i]+b[i+1])/2
   b[i+1 if bit=='0' else i]=mid
  if list(map(F,row['box']))!=b:raise RuntimeError('box/path geometry mismatch')
  if path in groups[root]:raise RuntimeError('duplicate partition path')
  groups[root].add(path)
 for g in groups:
  if any(p[:i] in g for p in g for i in range(len(p))):raise RuntimeError('overlapping partition path')
  while g!={''}:
   if not g:raise RuntimeError('missing partition root')
   p=max(g,key=len);s=p[:-1]+('1' if p[-1]=='0' else '0')
   if s not in g:raise RuntimeError('partition gap')
   g.remove(p);g.remove(s);g.add(p[:-1])
 for row in leaves:
  if row['status']=='outside-near':
   b=list(map(F,row['box']))
   if minabs(*b[:2])+minabs(*b[2:])<=F(rho):raise RuntimeError('outside-near geometry failure')
 return time.process_time()-start
def case(lib,rho):
 resource.setrlimit(resource.RLIMIT_CPU,(739,740));start=cpu();tag='rho-'+('1-2' if rho==.5 else '1-8')
 lc=lib.phase_lambda(N,math.pi,math.pi);eps=1e-12*(1+lc)
 finite(lc,eps)
 if lc<=0 or eps<=0:raise RuntimeError('nonpositive corner reference or epsilon')
 q=collections.deque({'root':i,'path':'','box':[a,b,c,d]} for i,(a,b,c,d) in enumerate([(a,b,c,d) for a,b in [(-rho,0.),(0.,rho)] for c,d in [(-rho,0.),(0.,rho)]]))
 leaves=[];trace=[];stop='complete';native_calls=0;kernel_cpu=0.
 while q and len(trace)<BOXES and cpu()-start<CASE_CPU:
  # This checkpoint retains the current uncomputed box after any hard stop.
  save(OUT/(tag+'-checkpoint.json'),{'leaves':leaves,'pending':list(q),'trace':trace})
  row=q.popleft();b=row['box'];al,ah,bl,bh=b
  if minabs(al,ah)+minabs(bl,bh)>rho:row['status']='outside-near'
  else:
   local=h3(N,b);before=cpu();x=bounds(lib,N,b,lc,eps,local);spent=cpu()-before
   native_calls+=1;kernel_cpu+=spent;su,cu,dl,p=x[:4]
   status='far' if su<lc-eps else ('local-corner-plus-defect' if local and su-dl<lc-eps else ('corner-orbit-plus-defect' if cu<lc-eps and su-dl<lc-eps else 'split'))
   row.update(status=status,bounds=x,local_H3=local,native_cpu_seconds=spent,
    margins={'far':lc-eps-su,'corner':lc-eps-cu,'noncorner':lc-eps-(su-dl)})
   finite(*row['margins'].values())
  trace.append(row)
  if row['status']=='split':
   i=0 if ah-al>=bh-bl else 2;mid=b[i]+(b[i+1]-b[i])/2
   if not b[i]<mid<b[i+1]:raise RuntimeError('stagnant bisection')
   for bit in [0,1]:
    child=list(b);child[i+1 if bit==0 else i]=mid;q.append({'root':row['root'],'path':row['path']+str(bit),'box':child})
  else:leaves.append(row)
  if row.get('native_cpu_seconds',0)>60:
   stop='single-call-cost-stop';break
 if q and stop=='complete':stop='box-cap' if len(trace)>=BOXES else 'CPU-cap'
 pending=list(q);check_cpu=structural(leaves,pending,rho)
 detail={'n':N,'rho':rho,'Lambda_corner':lc,'eps':eps,'trace':trace,'leaves':leaves,'pending':pending}
 save(OUT/(tag+'-partition.json'),detail)
 summary={'n':N,'rho':rho,'visited':len(trace),'native_calls':native_calls,'leaf_counts':dict(collections.Counter(x['status'] for x in leaves)),'unresolved_frontier':len(pending),'complete_float_partition':not pending,'stop_reason':stop,'producer_process_cpu_seconds':cpu()-start-check_cpu,'native_calls_cpu_seconds':kernel_cpu,'structural_checker_cpu_seconds':check_cpu,'exact_checker_cpu_seconds':None,'detail':identity(OUT/(tag+'-partition.json'))}
 save(OUT/(tag+'-summary.json'),summary);print(json.dumps(summary),flush=True)
def launch(args,label,limit):
 before=cpu();started=time.monotonic();wall_limit=min(900,2*limit+30);stopped=None
 # Direct files avoid deadlock even when compiler helper output exceeds a pipe.
 with (OUT/(label+'.stdout')).open('wb') as stdout,(OUT/(label+'.stderr')).open('wb') as stderr:
  p=subprocess.Popen(args,stdin=subprocess.DEVNULL,stdout=stdout,stderr=stderr,start_new_session=True)
  while p.poll() is None:
   # One worker plus its compiler children. /proc child CPU is sampled only
   # as a safety stop; final totals use waited-child getrusage.
   live=0.
   for stat in pathlib.Path('/proc').glob('[0-9]*/stat'):
    try:
     text=stat.read_text();v=text[text.rfind(')')+2:].split()
     if int(v[2])==p.pid:live+=sum(int(v[k]) for k in (11,12,13,14))/os.sysconf('SC_CLK_TCK')
    except (OSError,ValueError,IndexError):pass
   if cpu()+live>1790:stopped='aggregate-CPU-cap'
   elif cpu()-before+live>limit:stopped='command-CPU-cap'
   elif time.monotonic()-started>wall_limit:stopped='command-wall-cap'
   if stopped:
    try:os.killpg(p.pid,signal.SIGKILL)
    except ProcessLookupError:pass
    break
   time.sleep(.1)
  p.wait()
 return {'argv':args,'exit':p.returncode,'stop_reason':stopped,'wall_limit_seconds':wall_limit,'wall_seconds':time.monotonic()-started,'cpu_seconds':cpu()-before,'stdout':identity(OUT/(label+'.stdout')),'stderr':identity(OUT/(label+'.stderr'))}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--run-once',action='store_true');ap.add_argument('--worker',choices=['controls','half','eighth']);args=ap.parse_args()
 if args.worker:
  lib=load(args.worker)
  if args.worker=='controls':control(lib)
  else:case(lib,.5 if args.worker=='half' else .125)
  return
 if not args.run_once:raise RuntimeError('preparation only; reviewed --run-once invocation required')
 resource.setrlimit(resource.RLIMIT_CPU,(1799,1800))
 OUT.mkdir(parents=True,exist_ok=True)
 if (OUT/'preregistration.json').exists():raise RuntimeError('refuse overwrite or rescue')
 for p,pin in PINS.items():
  if identity(ROOT/p)['sha256']!=pin:raise RuntimeError('frozen native source changed; new gate required')
 save(OUT/'preregistration.json',{'source':identity(__file__),'native_sources':[identity(ROOT/p) for p in PINS],'degrees':[512],'radii':[.5,.125],'box_cap_per_case':BOXES,'CPU_cap_total':TOTAL_CPU,'CPU_case_soft_stop':CASE_CPU,'single_call_cost_stop':60,'float_precision':'C double / Python binary64; ordinary libm, no directed rounding'})
 records=[];build=['cc','-O3','-std=c11','-shared','-fPIC','-MD','-MF',str(OUT/'build.d'),str(OLD/'phase_probe.c'),str(TOPIC/'code/n3_meanvalue.c'),'-lm','-o',str(OUT/'pilot.so')]
 records.append(launch(build,'build',60));save(OUT/'commands.json',records)
 if records[-1]['exit']:raise RuntimeError('first build failure; stop')
 deps=(OUT/'build.d').read_text().replace('\\\n',' ').split(': ',1)[1].split()
 # -MD with multiple translation units may retain only the last unit;
 # phase_probe.c's sole include is math.h, also included by that last unit.
 save(OUT/'build-inputs.json',{'compiler':identity(shutil.which('cc')),'binary':identity(OUT/'pilot.so'),'dependencies':[identity(p) for p in sorted(set(deps))]})
 records.append(launch(['cc','--version'],'compiler-version',10));save(OUT/'commands.json',records)
 if records[-1]['exit']:raise RuntimeError('first compiler-version helper failure; stop')
 records.append(launch(['cc','-dM','-E','-include','float.h','-'],'compiler-float-macros',10));save(OUT/'commands.json',records)
 if records[-1]['exit']:raise RuntimeError('first float-precision helper failure; stop')
 macro=(OUT/'compiler-float-macros.stdout').read_text().splitlines()
 save(OUT/'float-format.json',{'compiler_macros':[x for x in macro if any(k in x for k in ('__DBL_MANT_DIG__','__FLT_RADIX__','__FLT_EVAL_METHOD__'))]})
 for mode,limit in [('controls',60),('half',750),('eighth',750)]:
  records.append(launch([sys.executable,str(__file__),'--worker',mode],mode,limit));save(OUT/'commands.json',records)
  if records[-1]['exit']:raise RuntimeError('first worker failure; stop with checkpoint retained')
 save(OUT/'run-summary.json',{'status':'MEASURED float pilot only','commands':records,'total_process_CPU_seconds':cpu(),'binary':identity(OUT/'pilot.so'),'python':sys.version,'failures':[]})
if __name__=='__main__':main()
