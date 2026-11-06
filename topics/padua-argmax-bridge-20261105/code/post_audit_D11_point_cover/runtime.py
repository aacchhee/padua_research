"""D11 metadata/build/native support. Imported definitions perform no native work."""
import ctypes,hashlib,importlib.util,json,math,os,pathlib,sys,time
from fractions import Fraction as F
HERE=pathlib.Path(__file__).resolve().parent
ROOT=HERE.parents[3]

def module(name,path):
 s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
D09=module('d11_frozen_d09_helpers',HERE.parent/'post_audit_D09_threepoint/controller.py')
BUILD=module('d11_frozen_d07_builder',HERE.parent/'post_audit_D07_fourcopy_point/build.py')
identity=D09.identity
cpu=D09.cpu
save=D09.save


def strict_json(path,limit=4194304):
 p=pathlib.Path(path)
 with p.open("rb") as stream:data=stream.read(limit+1)
 if len(data)>limit:raise ValueError('JSON byte cap')
 def pairs(rows):
  result={}
  for k,v in rows:
   if k in result:raise ValueError('duplicate JSON key')
   result[k]=v
  return result
 def invalid(x):raise ValueError('nonfinite JSON constant '+x)
 def floating(x):
  value=float(x)
  if not math.isfinite(value):raise ValueError('overflow/nonfinite JSON number')
  return value
 try:return json.loads(data.decode('utf-8'),object_pairs_hook=pairs,parse_constant=invalid,parse_float=floating)
 except (RecursionError,UnicodeError) as e:raise ValueError('malformed/too-deep JSON') from e


def check_freeze():
 f=strict_json(HERE/'FREEZE.json');s=strict_json(HERE/'SOURCES.json')
 for row in f['code_data']+s['immutable_code_data_dependencies']:
  got=identity(ROOT/row['path'])
  if got['bytes']!=row['bytes'] or got['sha256']!=row['sha256']:raise RuntimeError('frozen input changed: '+row['path'])
 return f


def registration_check(out):
 reg=strict_json(out/'preregistration.json')
 if reg['freeze']!=identity(HERE/'FREEZE.json'):raise RuntimeError('registered FREEZE changed')
 check_freeze();return reg


def build_float(out):
 """New linkage wrapper only; phase_probe.c bytes and arithmetic unchanged."""
 import tempfile,shutil
 origin=ROOT/'topics/padua-argmax-effective-2-20261105/code/phase_probe.c'
 work=pathlib.Path(tempfile.mkdtemp(prefix='float-',dir=out))
 snapshot=work/'phase_probe.c';snapshot.write_bytes(origin.read_bytes())
 src=work/'wrapper.cpp';src.write_text('extern "C" {\n#include "phase_probe.c"\n}\n')
 cxx=pathlib.Path(shutil.which('c++')).resolve();tools=[cxx]
 for flag in ('-print-prog-name=cc1plus','-print-prog-name=as','-print-prog-name=ld'):
  name=BUILD.run([cxx,flag]).strip();tools.append((pathlib.Path(name) if '/' in name else pathlib.Path(shutil.which(name))).resolve())
 tools=sorted(set(tools));toolids=[identity(p) for p in tools]
 tooldeps=sorted(set(p for tool in tools for p in BUILD.closure(tool)));td=[identity(p) for p in tooldeps]
 headers=BUILD.preprocess_deps(cxx,src,[]);hi=[identity(p) for p in headers]
 ii=work/'float.ii';pre=[cxx,*BUILD.FLAGS,'-E',src,'-o',ii];BUILD.run(pre);iiid=identity(ii)
 if hi!=[identity(p) for p in headers]:raise RuntimeError('FLOAT preprocessing input changed')
 binary=work/'libphase_float.so';cmd=[cxx,*BUILD.FLAGS,'-shared','-x','c++-cpp-output',ii,'-lm','-o',binary];BUILD.run(cmd)
 if iiid!=identity(ii) or toolids!=[identity(p) for p in tools] or td!=[identity(p) for p in tooldeps]:raise RuntimeError('FLOAT compiler inputs changed')
 linked=[identity(p) for p in BUILD.closure(binary)]
 return binary,dict(source_origin=identity(origin),source_snapshot=identity(snapshot),linkage_wrapper=identity(src),preprocessed_translation_unit=iiid,checker_binary=identity(binary),preprocess_command=list(map(str,pre)),compile_command=list(map(str,cmd)),toolchain=toolids,toolchain_dependency_closure=td,headers=hi,linked_dependency_closure=linked)


def mapped_files():
 paths=set()
 for line in pathlib.Path('/proc/self/maps').read_text().splitlines():
  fields=line.split(maxsplit=5)
  if len(fields)==6 and fields[5].startswith('/'):
   if fields[5].endswith(' (deleted)'):raise RuntimeError('deleted mapped file')
   paths.add(pathlib.Path(fields[5]).resolve())
 return [identity(p) for p in sorted(paths)]


def recheck_build(manifest):
 for key in ('source_snapshot','preprocessed_translation_unit','checker_binary'):
  row=manifest[key]
  if identity(row['path'])!=row:raise RuntimeError('compiled artifact changed')
 for k in ('toolchain','toolchain_dependency_closure','headers','linked_dependency_closure','dependency_inputs'):
  for row in manifest.get(k,[]):
   if identity(row['path'])!=row:raise RuntimeError('build closure changed')


class Native:
 def __init__(self,stage,out,state,checkpoint):
  self.stage,self.out,self.state,self.checkpoint=stage,out,state,checkpoint
  if ctypes.sizeof(ctypes.c_long)!=8 or ctypes.sizeof(ctypes.c_double)!=8:raise RuntimeError('LP64 binary64 required')
  if stage=='producer':binary,self.manifest=build_float(out)
  else:
   if not BUILD.INC.is_dir() or not BUILD.FLINT.exists():
    # Pinned official-package provisioning is inside checker CPU/wall budget.
    BUILD.run([sys.executable,HERE.parent/'phase_checker/setup.py'])
   BUILD.LOCAL=out;binary,self.manifest=BUILD.build()
  save(out/(stage+'-build.json'),self.manifest)
  self.lib=ctypes.CDLL(str(binary))
  if stage=='producer':
   self.fn=self.lib.phase_s;self.fn.argtypes=[ctypes.c_int,ctypes.c_double,ctypes.c_double];self.fn.restype=ctypes.c_double
  else:
   self.fn=self.lib.c07_point;self.fn.argtypes=[ctypes.c_long,ctypes.c_char_p,ctypes.c_char_p,ctypes.POINTER(ctypes.c_double),ctypes.POINTER(ctypes.c_long)];self.fn.restype=ctypes.c_int
  self.binary_before=identity(binary)
  self.before=BUILD.loaded_closure(self.manifest)
  self.python_before=identity(sys.executable)
  self.mapped_before=mapped_files()
  save(out/(stage+'-runtime-before.json'),{'loaded':self.before,'all_file_mappings':self.mapped_before,'python':sys.version})
  (out/(stage+'-loaded-before.maps')).write_text(pathlib.Path('/proc/self/maps').read_text())
 def call(self,a,b):
  s=self.state;budget=60 if self.stage=='producer' else 300
  if cpu()+D09.parent_cpu()>=390 or cpu()>=budget-7:raise RuntimeError('pre-call CPU reserve exhausted')
  start=cpu();label=str(a)+','+str(b)
  s['active_call']={'label':label,'cpu_start':start};self.checkpoint()
  # Save complete native outputs before validation or cost-stop decisions.
  if self.stage=='producer':
   raw=self.fn(512,a,b);record={'value_hex':float(raw).hex()}
  else:
   if not isinstance(a,F) or not isinstance(b,F) or not (0<=a and 0<=b and a+b<=1) or max(len(str(a)),len(str(b)))>256:raise ValueError('C11 exact point input guard')
   out=(ctypes.c_double*3)();ct=(ctypes.c_long*6)();rc=self.fn(512,str(a).encode(),str(b).encode(),out,ct)
   raw=list(out);record={'returncode':rc,'raw_hex':[float(x).hex() for x in out],'counts':list(ct)}
  duration=cpu()-start
  entry={'key':label,'native':record,'cpu_seconds':duration}
  s['completed_calls'].append(entry);s['active_call']=None;self.checkpoint()
  if duration>20:raise RuntimeError('completed native call exceeded20CPU; output retained')
  if self.stage=='producer':
   if not math.isfinite(raw) or raw<0:raise RuntimeError('invalid FLOAT output')
   return raw
  if rc:raise RuntimeError('C11 point returncode '+str(rc))
  point=D09.endpoint_record(raw);entry['point']=point;self.checkpoint()
  return F(point['lower']),F(point['upper'])
 def close(self):
  after=BUILD.loaded_closure(self.manifest)
  mapped_after=mapped_files()
  if mapped_after!=self.mapped_before:raise RuntimeError('all mapped file identities changed')
  if self.before!=after or identity(sys.executable)!=self.python_before:raise RuntimeError('loaded native/Python closure changed')
  recheck_build(self.manifest)
  save(self.out/(self.stage+'-runtime-after.json'),{'loaded':after,'all_file_mappings':mapped_after})
  (self.out/(self.stage+'-loaded-after.maps')).write_text(pathlib.Path('/proc/self/maps').read_text())


def validate_witness():
 """Frozen computational evidence plus fresh review authority resolved by root.
 No runtime pin of prose. Retained accepted D09 point endpoints are data.
 """
 p=ROOT/'topics/padua-argmax-bridge-20261105/evidence/d09-threepoint.json'
 receipt=strict_json(p)
 # Accepted immutable essential receipt is a compositional computational
 # premise. Old raw outputs/binary are not required in a fresh cloud clone.
 # Their pinned identities remain provenance inside that essential receipt.
 # Never load or execute a retained D09 binary here.
 expected='34553e6d91dc77285f1bbb277a0f519c5a8a5da5f27a8f43501c7caf13631509'
 if identity(p)['sha256']!=expected:raise RuntimeError('unaccepted D09 receipt')
 if receipt['result']!='PASS primary exact loss criterion; fallback not executed':raise RuntimeError('D09 receipt disposition')
 corner=receipt['corner']
 if (corner['api'],corner['n'],corner['xi_pi'],corner['zeta_pi'])!=('c07_point',512,'0','0'):raise RuntimeError('D09 corner scope')
 primary=receipt['rectangles']['primary']
 for key,turns in {'x':('1/2048','0'),'y':('0','1/2736'),'xy':('1/2048','1/2736')}.items():
  row=primary['vertices'][key]
  if (row['api'],row['n'],row['xi_pi'],row['zeta_pi'])!=('d07_point',512,*turns):raise RuntimeError('D09 actual lambda scope')
 for point in [receipt['corner']['point']]+[receipt['rectangles']['primary']['vertices'][key]['point'] for key in ('x','y','xy')]:
  values=[float.fromhex(x) for x in point['binary64_hex']]
  got=D09.endpoint_record(values)
  if got!=point:raise RuntimeError('D09 exact endpoint/hex disagreement')
 return receipt
