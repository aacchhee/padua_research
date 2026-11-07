"""D23 isolated paired old/new S-only runtime. Import performs no native work."""
import ctypes, hashlib, importlib.util, json, math, os, pathlib, sys
from fractions import Fraction as F
HERE=pathlib.Path(__file__).resolve().parent
ROOT=HERE.parents[3]

def module(name,path):
 s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
D09=module('d23_d09_helpers',HERE.parent/'post_audit_D09_threepoint/controller.py')
BUILD=module('d23_builder',HERE/'build.py')
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
 def __init__(self,out,state,checkpoint):
  self.out,self.state,self.checkpoint=out,state,checkpoint
  if ctypes.sizeof(ctypes.c_long)!=8 or ctypes.sizeof(ctypes.c_double)!=8:raise RuntimeError('LP64 binary64 required')
  if not BUILD.INC.is_dir() or not BUILD.FLINT.exists():
   BUILD.run([sys.executable,HERE.parent/'phase_checker/setup.py'])
  BUILD.LOCAL=out;self.libs={};self.manifests={}
  for which in ('baseline','candidate'):
   before=cpu();binary,manifest=BUILD.build(which)
   manifest['inclusive_build_CPU']=cpu()-before;save(out/(which+'-build.json'),manifest)
   self.manifests[which]=manifest;self.libs[which]=ctypes.CDLL(str(binary))
  ptr=ctypes.POINTER(ctypes.c_double);iptr=ctypes.POINTER(ctypes.c_long)
  old=self.libs['baseline'];new=self.libs['candidate']
  for lib in (old,new):
   lib.c07_point.argtypes=[ctypes.c_long,ctypes.c_char_p,ctypes.c_char_p,ptr,iptr];lib.c07_point.restype=ctypes.c_int
  new.c23_point_audit.argtypes=old.c07_point.argtypes;new.c23_point_audit.restype=ctypes.c_int
  for name in ('c23_partial_control','c06_partial'):
   fn=getattr(new,name);fn.argtypes=[ctypes.c_long,ctypes.c_long,ctypes.c_char_p,ptr];fn.restype=ctypes.c_int
  new.c23_reference.argtypes=[ctypes.c_long,ctypes.c_char_p,ctypes.c_char_p,ptr];new.c23_reference.restype=ctypes.c_int
  new.c23_moment_control.argtypes=[];new.c23_moment_control.restype=ctypes.c_int
  self.before={k:BUILD.loaded_closure(m) for k,m in self.manifests.items()}
  self.python_before=identity(sys.executable);self.mapped_before=mapped_files()
  save(out/'runtime-before.json',{'loaded':self.before,'all_file_mappings':self.mapped_before,'python':sys.version})
  (out/'loaded-before.maps').write_text(pathlib.Path('/proc/self/maps').read_text())
 def call(self,label,invoke):
  if cpu()+D09.parent_cpu()>=54 or cpu()>=43:raise RuntimeError('pre-call CPU reserve exhausted')
  s=self.state;start=cpu();s['active_call']={'label':label,'cpu_start':start};self.checkpoint()
  raw=invoke();duration=cpu()-start
  entry={'label':label,'raw':raw,'inclusive_CPU':duration}
  s['completed_calls'].append(entry);s['active_call']=None;self.checkpoint()
  if duration>5:raise RuntimeError('completed call exceeded5CPU; no retry')
  return raw
 def point(self,which,n,a,b):
  fn=self.libs[which].c07_point if which=='baseline' else self.libs[which].c23_point_audit
  out=(ctypes.c_double*(3 if which=='baseline' else 4))();ct=(ctypes.c_long*6)()
  rc=fn(n,a.encode(),b.encode(),out,ct)
  return {'returncode':rc,'hex':[float(x).hex() for x in out],'counts':list(ct)}
 def partial(self,n,q,y,invalid=False):
  out=(ctypes.c_double*(3 if invalid else 2))();fn=self.libs['candidate'].c06_partial if invalid else self.libs['candidate'].c23_partial_control
  rc=fn(n,q,y.encode(),out);return {'returncode':rc,'hex':[float(x).hex() for x in out]}
 def invalid_point(self,n,a,b):
  out=(ctypes.c_double*3)();ct=(ctypes.c_long*6)();rc=self.libs['candidate'].c07_point(n,a.encode(),b.encode(),out,ct)
  return {'returncode':rc,'hex':[float(x).hex() for x in out],'counts':list(ct)}
 def reference(self,n,a,b):
  out=(ctypes.c_double*3)();rc=self.libs['candidate'].c23_reference(n,a.encode(),b.encode(),out)
  return {'returncode':rc,'hex':[float(x).hex() for x in out]}
 def close(self):
  after={k:BUILD.loaded_closure(m) for k,m in self.manifests.items()};mapped_after=mapped_files()
  if mapped_after!=self.mapped_before or self.before!=after or identity(sys.executable)!=self.python_before:raise RuntimeError('runtime closure changed')
  for manifest in self.manifests.values():recheck_build(manifest)
  save(self.out/'runtime-after.json',{'loaded':after,'all_file_mappings':mapped_after})
  (self.out/'loaded-after.maps').write_text(pathlib.Path('/proc/self/maps').read_text())
