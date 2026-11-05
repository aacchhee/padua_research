"""Fresh, isolated checker build with a pinned preprocessed translation unit.
No existing checker .so is loaded. Artifacts remain local for receipt replay.
"""
import hashlib, os, pathlib, re, shutil, subprocess, tempfile

ROOT=pathlib.Path(__file__).resolve().parents[4]
LOCAL=ROOT/'local-output/argmax-bridge-20261105/phase-checker'
INC=LOCAL/'runtime/extracted/usr/include'
FLINT=LOCAL/'runtime/extracted/usr/lib/x86_64-linux-gnu/libflint.so.19'
FLAGS=['-std=c++17','-O3','-Wall','-Wextra','-fPIC']

def digest(data):return hashlib.sha256(data).hexdigest()
def identity(path):
 p=pathlib.Path(path).resolve();data=p.read_bytes()
 return {'path':str(p),'bytes':len(data),'sha256':digest(data)}
def run(cmd):
 r=subprocess.run(list(map(str,cmd)),cwd=ROOT,text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 if r.returncode:raise RuntimeError('build failed: '+str(cmd)+'\n'+r.stderr)
 return r.stdout

def closure(path):
 text=run(['ldd',path]);paths=[]
 if 'not found' in text:raise RuntimeError('unresolved runtime dependency')
 for line in text.splitlines():
  m=re.search(r'(?:=>\s+)?(/\S+)\s+\(',line)
  if m:paths.append(pathlib.Path(m.group(1)).resolve())
 return sorted(set(paths))

def preprocess_deps(cxx,src,include):
 text=run([cxx,*FLAGS,*include,'-M',src]).replace('\\\n',' ')
 return sorted(set(pathlib.Path(p).resolve() for p in text.split(':',1)[1].split()))

def build():
 LOCAL.mkdir(parents=True,exist_ok=True)
 work=pathlib.Path(tempfile.mkdtemp(prefix='check-',dir=LOCAL))
 src=work/'arb_kernel.cpp';source=(pathlib.Path(__file__).with_name('arb_kernel.cpp')).read_bytes();src.write_bytes(source)
 cxx=pathlib.Path(shutil.which('c++')).resolve()
 tools=[cxx]
 for flag in ['-print-prog-name=cc1plus','-print-prog-name=as','-print-prog-name=ld']:
  name=run([cxx,flag]).strip();tool=pathlib.Path(name) if '/' in name else pathlib.Path(shutil.which(name))
  tools.append(tool.resolve())
 tools=sorted(set(tools));toolids=[identity(p) for p in tools]
 tooldeps=sorted(set(p for tool in tools for p in closure(tool)));tooldepids=[identity(p) for p in tooldeps]
 include=['-I'+str(INC)]
 headers=preprocess_deps(cxx,src,include);headerids=[identity(p) for p in headers]
 dependency_paths=sorted(set([FLINT.resolve(),*closure(FLINT)]))
 depids=[identity(p) for p in dependency_paths]
 # Snapshot the non-Python arithmetic dependencies. The other system runtime
 # libraries are hashed before/after and checked against actual loaded maps.
 depdir=work/'deps';depdir.mkdir()
 for p in dependency_paths:
  if p.name.startswith(('libflint.so','libgmp.so','libmpfr.so')):
   target=depdir/p.name;target.write_bytes(p.read_bytes())
   # Link by SONAME (the unversioned development links are not trusted).
   soname=run(['readelf','-d',target]);m=re.search(r'\(SONAME\).*?\[(.*?)\]',soname)
   if not m:raise RuntimeError('library lacks SONAME')
   alias=depdir/m.group(1)
   if alias!=target:alias.symlink_to(target.name)
 ii=work/'kernel.ii';pre=[str(cxx),*FLAGS,*include,'-E',str(src),'-o',str(ii)]
 run(pre)
 iiid=identity(ii)
 if headerids!=[identity(p) for p in headers]:raise RuntimeError('header changed during preprocessing')
 binary=work/'libphase_checker.so'
 command=[str(cxx),*FLAGS,'-shared','-x','c++-cpp-output',str(ii),'-L'+str(depdir),
  '-Wl,-rpath,'+str(depdir),'-Wl,--disable-new-dtags','-l:libflint.so.19','-l:libgmp.so.10','-o',str(binary)]
 run(command)
 if iiid!=identity(ii):raise RuntimeError('preprocessed translation unit changed during compilation')
 if tooldepids!=[identity(p) for p in tooldeps]:raise RuntimeError('toolchain runtime dependency changed during build')
 if toolids!=[identity(p) for p in tools] or depids!=[identity(p) for p in dependency_paths]:raise RuntimeError('toolchain/dependency changed during build')
 linked=closure(binary)
 linkedids=[identity(p) for p in linked]
 return binary,{'workdir':str(work),'source_snapshot':identity(src),'preprocessed_translation_unit':iiid,
  'checker_binary':identity(binary),'flags':FLAGS,'preprocess_command':pre,'compile_command':command,
  'compiler_version':run([cxx,'--version']).splitlines()[0],'toolchain':toolids,'toolchain_dependency_closure':tooldepids,'headers':headerids,
  'dependency_inputs':depids,'linked_dependency_closure':linkedids,
  'build_policy':'fresh unique directory; no preexisting checker binary accepted'}

def loaded_closure(manifest):
 # Resolve the actual mappings, which can differ from ldd if a SONAME was
 # already loaded in this Python process. Such reuse must match pinned bytes.
 paths=set()
 for line in pathlib.Path('/proc/self/maps').read_text().splitlines():
  fields=line.split(maxsplit=5)
  if len(fields)==6 and fields[5].startswith('/') and not fields[5].endswith(' (deleted)'):
   paths.add(pathlib.Path(fields[5]).resolve())
 found=[]
 for expected in manifest['linked_dependency_closure']:
  matches=[p for p in paths if p.name==pathlib.Path(expected['path']).name]
  # Some loader names differ by a symlink; resolved paths normally agree.
  if not matches:raise RuntimeError('linked dependency not mapped: '+expected['path'])
  actual=[identity(p) for p in matches]
  if any(p['sha256']!=expected['sha256'] for p in actual):raise RuntimeError('mapped dependency differs from build manifest')
  found.extend(actual)
 return found
