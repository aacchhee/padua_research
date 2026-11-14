"""D21 isolated unchanged C11 S-only runtime. Import performs no native work."""
import ctypes, hashlib, importlib.util, json, math, os, pathlib, sys
from fractions import Fraction as F
HERE=pathlib.Path(__file__).resolve().parent
ROOT=HERE.parents[3]

def module(name,path):
 s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
D09=module('d21_d09_helpers',HERE.parent/'post_audit_D09_threepoint/controller.py')
BUILD=module('d21_builder',HERE/'build.py')
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
  if type(n) is not int or n!=6912:raise ValueError("sole registered degree6912")
  self.out,self.state,self.checkpoint,self.n=out,state,checkpoint,n
  if ctypes.sizeof(ctypes.c_long)!=8 or ctypes.sizeof(ctypes.c_double)!=8:raise RuntimeError('LP64 binary64 required')
  if not BUILD.INC.is_dir() or not BUILD.FLINT.exists():
   BUILD.run([sys.executable,HERE.parent/'phase_checker/setup.py'])
  BUILD.LOCAL=out;binary,self.manifest=BUILD.build()
  save(out/'checker-build.json',self.manifest)
  self.lib=ctypes.CDLL(str(binary));self.fn=self.lib.c07_point
  self.fn.argtypes=[ctypes.c_long,ctypes.c_char_p,ctypes.c_char_p,ctypes.POINTER(ctypes.c_double),ctypes.POINTER(ctypes.c_long)];self.fn.restype=ctypes.c_int
  self.before=BUILD.loaded_closure(self.manifest);self.python_before=identity(sys.executable);self.mapped_before=mapped_files()
  save(out/'checker-runtime-before.json',{'loaded':self.before,'all_file_mappings':self.mapped_before,'python':sys.version})
  (out/'checker-loaded-before.maps').write_text(pathlib.Path('/proc/self/maps').read_text())
 def call(self,a,b):
  if cpu()+D09.parent_cpu()>=590 or cpu()>=573:raise RuntimeError('pre-call CPU reserve exhausted')
  if not isinstance(a,F) or not isinstance(b,F) or max(len(str(a)),len(str(b)))>256:raise ValueError('exact rational input guard')
  if not (0<=a and 0<=b and a+b<=1):raise ValueError('C11 phase domain')
  s=self.state;start=cpu();s['active_call']={'api':'S','n':self.n,'key':[str(a),str(b)],'cpu_start':start};self.checkpoint()
  out=(ctypes.c_double*3)();ct=(ctypes.c_long*6)()
  rc=self.fn(self.n,str(a).encode(),str(b).encode(),out,ct)
  duration=cpu()-start
  entry={'api':'S','n':self.n,'key':[str(a),str(b)],'native':{'returncode':rc,'raw_hex':[float(x).hex() for x in out],'counts':list(ct)},'cpu_seconds':duration}
  s['completed_calls'].append(entry);s['active_call']=None;self.checkpoint()
  if duration>25:raise RuntimeError('completed call exceeded25CPU; no retry')
  if rc:raise RuntimeError('C11 returncode '+str(rc))
  point=D09.endpoint_record(list(out))
  counts=list(ct)
  if any(type(x) is not int or x<0 for x in counts):raise RuntimeError('invalid counters')
  retained,direct,blocks,maxdirect,maxblocks,ordinary=counts
  if a==1 or b==1:
   if counts!=[0]*6:raise RuntimeError('endpoint counters')
  elif retained!=4*self.n or ordinary!=2*(self.n+1)-4 or maxdirect>5 or maxblocks>24 or direct>5*ordinary or blocks>24*ordinary:
   raise RuntimeError('C11 counter closure')
  if F(point['lower'])<0:raise RuntimeError('negative S lower')
  entry['point']=point;self.checkpoint()
  return F(point['lower']),F(point['upper'])
 def close(self):
  after=BUILD.loaded_closure(self.manifest);mapped_after=mapped_files()
  if mapped_after!=self.mapped_before or self.before!=after or identity(sys.executable)!=self.python_before:raise RuntimeError('runtime closure changed')
  recheck_build(self.manifest)
  save(self.out/'checker-runtime-after.json',{'loaded':after,'all_file_mappings':mapped_after})
  (self.out/'checker-loaded-after.maps').write_text(pathlib.Path('/proc/self/maps').read_text())
