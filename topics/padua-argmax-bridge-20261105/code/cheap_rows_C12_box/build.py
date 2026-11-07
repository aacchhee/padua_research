"""Fresh C12/J16 build with pinned transitive source and actual mapped closure."""
import pathlib,sys
ROOT=pathlib.Path(__file__).resolve().parents[4];HERE=pathlib.Path(__file__).resolve().parent
OLD=HERE.parent/'phase_checker';PARTIAL=HERE.parent/'cheap_rows_C11/partial.cpp';PARTIAL_SHA='bde1ce4850849dd402acc91eb3cee7d40883bbd51d5f7cff13334abc0f4ee23c'
sys.path.insert(0,str(OLD));import build_snapshot_r9 as pinned
OUT=ROOT/'local-output/argmax-bridge-20261105/c12-row-box'
def build():
 if pinned.identity(PARTIAL)['sha256']!=PARTIAL_SHA:raise RuntimeError('reviewed J16 partial mismatch')
 text=pathlib.Path(pinned.__file__).read_text();changes={"LOCAL=ROOT/'local-output/argmax-bridge-20261105/phase-r9'":"LOCAL=ROOT/'local-output/argmax-bridge-20261105/c12-row-box'","source_path=pathlib.Path(__file__).with_name(KERNEL_SOURCES[kernel_variant])":"source_path=ROOT/'topics/padua-argmax-bridge-20261105/code/cheap_rows_C12_box/reference.cpp'","include=['-I'+str(INC)]":"include=['-I'+str(INC),'-I'+str(ROOT/'topics/padua-argmax-bridge-20261105/code/cheap_rows_C12_box'),'-I'+str(ROOT/'topics/padua-argmax-bridge-20261105/code/cheap_rows_C11')]","'-Wall','-Wextra'":"'-Wall','-Wextra','-fmax-errors=3'"}
 for a,b in changes.items():
  if text.count(a)!=1:raise RuntimeError('builder anchor changed')
  text=text.replace(a,b)
 ns={'__file__':str(OLD/'build_snapshot_r9.py')};exec(compile(text,'<c12-builder>','exec'),ns);binary,manifest=ns['build']();manifest['partial_source']=pinned.identity(PARTIAL);manifest['adapted_builder_sha256']=pinned.digest(text.encode());return binary,manifest,ns['loaded_closure']
def actual_maps():
 paths=set()
 for line in pathlib.Path('/proc/self/maps').read_text().splitlines():
  f=line.split(maxsplit=5)
  if len(f)==6 and f[5].startswith('/') and not f[5].endswith(' (deleted)'):paths.add(pathlib.Path(f[5]).resolve())
 return [pinned.identity(p) for p in sorted(paths)]
def verify(entries):
 for e in entries:
  if pinned.identity(e['path'])!=e:raise RuntimeError('identity mutation '+e['path'])
