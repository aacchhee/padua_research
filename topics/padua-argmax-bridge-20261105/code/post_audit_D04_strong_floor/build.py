"""Fresh C08 producer build and full runtime/toolchain identity capture."""
import hashlib, pathlib, re, shutil, subprocess, tempfile
ROOT=pathlib.Path(__file__).resolve().parents[4]
HERE=pathlib.Path(__file__).resolve().parent
OUT=ROOT/'local-output/argmax-bridge-20261105/post-audit-D04/strong-floor'
INC=ROOT/'local-output/argmax-bridge-20261105/N3/runtime/extracted/usr/include'
FLAGS=['-O3','-std=c11','-Wall','-Wextra','-Wpedantic','-fmax-errors=5','-fPIC']
def identity(path):
 p=pathlib.Path(path).resolve();b=p.read_bytes();return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def run(cmd):
 result=subprocess.run(list(map(str,cmd)),cwd=ROOT,capture_output=True,text=True,errors='replace',timeout=20)
 if result.returncode:raise RuntimeError(str(cmd)+'\n'+result.stderr[:4000])
 return result.stdout

def closure(p):
 text=run(['ldd',p]);
 if 'not found' in text:raise RuntimeError('unresolved runtime')
 return sorted(set(pathlib.Path(p).resolve() for p in re.findall(r'(?:=>\s+)?(/\S+)\s+\(',text)))
def verify(entries):
 for e in entries:
  if identity(e['path'])!=e:raise RuntimeError('identity mutation '+e['path'])
def loaded(manifest):
 paths=set()
 for line in pathlib.Path('/proc/self/maps').read_text().splitlines():
  f=line.split(maxsplit=5)
  if len(f)==6 and f[5].startswith('/') and not f[5].endswith(' (deleted)'):paths.add(pathlib.Path(f[5]).resolve())
 actual=[identity(p) for p in sorted(paths)]
 for expected in manifest['linked_runtime_closure']:
  matches=[e for e in actual if pathlib.Path(e['path']).name==pathlib.Path(expected['path']).name]
  if not matches or any(e['sha256']!=expected['sha256'] for e in matches):raise RuntimeError('actual runtime mismatch '+expected['path'])
 return actual

def build():
 OUT.mkdir(parents=True,exist_ok=True);work=pathlib.Path(tempfile.mkdtemp(prefix='build-',dir=OUT))
 src=work/'producer.c';header=work/'c08_interval.h';src.write_bytes((HERE/src.name).read_bytes());header.write_bytes((HERE/header.name).read_bytes())
 cc=pathlib.Path(shutil.which('cc')).resolve();tools=[cc]
 for flag in ('-print-prog-name=cc1','-print-prog-name=as','-print-prog-name=ld'):
  p=run([cc,flag]).strip();tools.append(pathlib.Path(p).resolve() if '/' in p else pathlib.Path(shutil.which(p)).resolve())
 tools=sorted(set(tools));tool_ids=[identity(p) for p in tools];tooldeps=[identity(p) for p in sorted(set(q for p in tools for q in closure(p)))]
 command=[str(cc),*FLAGS,'-I'+str(INC),'-I'+str(work)]
 deps=run([*command,'-M',src]).replace('\\\n',' ').split(':',1)[1].split();headers=[identity(p) for p in sorted(set(deps))]
 pp=work/'producer.i';preprocess=[*command,'-E',src,'-o',pp];run(preprocess);ppid=identity(pp)
 binary=work/'producer.so';compile=[str(cc),*FLAGS,'-shared','-x','cpp-output',str(pp),'-x','none','/lib/x86_64-linux-gnu/libmpfr.so.6','-lm','-o',str(binary)];run(compile)
 manifest=dict(source=identity(src),header=identity(header),original_sources=[identity(HERE/'producer.c'),identity(HERE/'c08_interval.h'),identity(pathlib.Path(__file__))],preprocessed=ppid,binary=identity(binary),preprocess_command=list(map(str,preprocess)),compile_command=compile,compiler_version=run([cc,'--version']).splitlines()[0],tools=tool_ids,tool_runtime_closure=tooldeps,headers=headers,linked_runtime_closure=[identity(p) for p in closure(binary)])
 for key in ('tools','tool_runtime_closure','headers','linked_runtime_closure'):verify(manifest[key])
 verify([ppid]);return binary,manifest
