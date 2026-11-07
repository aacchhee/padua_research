"""D36 isolated exact S/actual-lambda runtime runtime. Import performs no native work."""
import ctypes, hashlib, importlib.util, json, math, os, pathlib, sys
from fractions import Fraction as F
HERE=pathlib.Path(__file__).resolve().parent
ROOT=HERE.parents[3]

def module(name,path):
 s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
D09=module('d36_d09_helpers',HERE.parent/'post_audit_D09_threepoint/controller.py')
BUILD=module('d36_builder',HERE/'build.py')
identity=D09.identity
cpu=D09.cpu
save=D09.save

def strict_json(path,limit=4194304):
 data=pathlib.Path(path).read_bytes()
 if len(data)>limit:raise ValueError('JSON byte cap')
 def pairs(rows):
  out={}
  for k,v in rows:
   if k in out:raise ValueError('duplicate JSON key')
   out[k]=v
  return out
 def invalid(x):raise ValueError('nonfinite JSON '+x)
 def floating(x):
  value=float(x)
  if not math.isfinite(value):raise ValueError('nonfinite number')
  return value
 return json.loads(data.decode(),object_pairs_hook=pairs,parse_constant=invalid,parse_float=floating)

def check_freeze():
 f=strict_json(HERE/'FREEZE.json')
 for row in f['code_data']:
  got=identity(ROOT/row['path'])
  if (got['bytes'],got['sha256'])!=(row['bytes'],row['sha256']):raise RuntimeError('frozen bytes changed: '+row['path'])
 return f

def registration_check(out):
 reg=strict_json(out/'preregistration.json')
 if reg['freeze']!=identity(HERE/'FREEZE.json'):raise RuntimeError('registered freeze changed')
 check_freeze();return reg

def mapped_files():
 paths=set()
 for line in pathlib.Path('/proc/self/maps').read_text().splitlines():
  fields=line.split(maxsplit=5)
  if len(fields)==6 and fields[5].startswith('/'):
   if fields[5].endswith(' (deleted)'):raise RuntimeError('deleted mapping')
   paths.add(pathlib.Path(fields[5]).resolve())
 return [identity(p) for p in sorted(paths)]

def recheck_build(manifest):
 for k in ('source_snapshot','preprocessed_translation_unit','checker_binary'):
  if identity(manifest[k]['path'])!=manifest[k]:raise RuntimeError('compiled artifact changed')
 for k in ('toolchain','toolchain_dependency_closure','headers','linked_dependency_closure','dependency_inputs'):
  for row in manifest.get(k,[]):
   if identity(row['path'])!=row:raise RuntimeError('build closure changed')

class Native:
 def __init__(self,out,state,checkpoint,n):
  import checker as C
  self.n=C.degree(n);self.actual_keys=C.actual_keys(n) if n<1024 else ()
  self.out,self.state,self.checkpoint=out,state,checkpoint
  self.seen_S=set();self.seen_lambda=set()
  if ctypes.sizeof(ctypes.c_long)!=8 or ctypes.sizeof(ctypes.c_double)!=8:raise RuntimeError('LP64 binary64 required')
  if not BUILD.INC.is_dir() or not BUILD.FLINT.exists():BUILD.run([sys.executable,HERE.parent/'phase_checker/setup.py'])
  BUILD.LOCAL=out;self.libs={};self.manifests={}
  for api in (('S','lambda') if n<1024 else ('S',)):
   before=cpu();binary,manifest=BUILD.build(api);manifest['inclusive_build_CPU']=cpu()-before
   save(out/(api+'-build.json'),manifest);self.manifests[api]=manifest;self.libs[api]=ctypes.CDLL(str(binary))
  ptr=ctypes.POINTER(ctypes.c_double);iptr=ctypes.POINTER(ctypes.c_long)
  self.functions={'S':self.libs['S'].c07_point}
  if n<1024:self.functions['lambda']=self.libs['lambda'].d07_point
  for fn in self.functions.values():
   fn.argtypes=[ctypes.c_long,ctypes.c_char_p,ctypes.c_char_p,ptr,iptr];fn.restype=ctypes.c_int
  self.before={api:BUILD.loaded_closure(m) for api,m in self.manifests.items()}
  self.python_before=identity(sys.executable);self.mapped_before=mapped_files()
  save(out/'runtime-before.json',{'loaded':self.before,'all_file_mappings':self.mapped_before,'python':sys.version})
  (out/'loaded-before.maps').write_text(pathlib.Path('/proc/self/maps').read_text())
 def call(self,a,b,api='S'):
  from fractions import Fraction as F
  if cpu()+D09.parent_cpu()>=110 or cpu()>=93:raise RuntimeError('pre-call CPU reserve exhausted')
  if api not in self.functions or not isinstance(a,F) or not isinstance(b,F) or max(len(str(a)),len(str(b)))>256:raise ValueError('exact API/rational input guard')
  if api=='S':
   if not (a>=0 and b>=0 and a+b<=1):raise ValueError('S phase domain')
  elif self.n>=1024 or self.n>2048 or (a,b) not in self.actual_keys:raise ValueError('registered actual physical point required')
  if api=='S':
   if (a,b) in self.seen_S or len(self.seen_S)>=256:raise RuntimeError('native unique S/call cap or duplicate invocation')
   self.seen_S.add((a,b))
  else:
   if (a,b) in self.seen_lambda or len(self.seen_lambda)>=3:raise RuntimeError('native actual-call cap or duplicate invocation')
   self.seen_lambda.add((a,b))
  s=self.state;start=cpu();s['active_call']={'api':api,'n':self.n,'key':[str(a),str(b)],'cpu_start':start};self.checkpoint()
  out=(ctypes.c_double*3)();ct=(ctypes.c_long*(6 if api=='S' else 13))()
  rc=self.functions[api](self.n,str(a).encode(),str(b).encode(),out,ct);duration=cpu()-start
  entry={'api':api,'n':self.n,'key':[str(a),str(b)],'native':{'returncode':rc,'raw_hex':[float(x).hex() for x in out],'counts':list(ct)},'cpu_seconds':duration}
  s['completed_calls'].append(entry);s['active_call']=None;self.checkpoint()
  if duration>10:raise RuntimeError('completed native call exceeded10CPU; no retry')
  if rc:raise RuntimeError('native returncode '+str(rc))
  point=D09.endpoint_record(list(out));c=list(ct)
  if any(type(x) is not int or x<0 for x in c) or F(point['lower'])<0:raise RuntimeError('invalid native counters/lower')
  if api=='S':
   if a==1 or b==1:
    if c!=[0]*6:raise RuntimeError('S endpoint counters')
   elif c[0]!=4*self.n or c[5]!=2*(self.n+1)-4 or c[3]>5 or c[4]>24 or c[1]>5*c[5] or c[2]>24*c[5]:raise RuntimeError('S counter closure')
  elif c[0]!=self.n+2 or c[1]>self.n+2 or c[2]>self.n+2 or c[3]>c[2] or c[4]>c[2] or c[9]>self.n+2 or c[10]!=0 or c[11]!=0 or c[12]>40:raise RuntimeError('actual-point counter closure')
  entry['point']=point;self.checkpoint()
  return F(point['lower']),F(point['upper'])
 def close(self):
  after={api:BUILD.loaded_closure(m) for api,m in self.manifests.items()};mapped_after=mapped_files()
  if mapped_after!=self.mapped_before or self.before!=after or identity(sys.executable)!=self.python_before:raise RuntimeError('runtime closure changed')
  for m in self.manifests.values():recheck_build(m)
  save(self.out/'runtime-after.json',{'loaded':after,'all_file_mappings':mapped_after})
  (self.out/'loaded-after.maps').write_text(pathlib.Path('/proc/self/maps').read_text())
