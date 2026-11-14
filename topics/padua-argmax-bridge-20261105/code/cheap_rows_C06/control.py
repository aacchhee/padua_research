"""Bounded frozen C06 partial controls; raw closure manifest stays local."""
import ctypes, hashlib, importlib.util, json, pathlib, resource, time
ROOT=pathlib.Path(__file__).resolve().parents[4]
HERE=pathlib.Path(__file__).resolve().parent
OLD=HERE.parent/'phase_checker'/'build_snapshot_r9.py'
text=OLD.read_text().replace("LOCAL=ROOT/'local-output/argmax-bridge-20261105/phase-r9'", "LOCAL=ROOT/'local-output/argmax-bridge-20261105/c06-rows'")
text=text.replace("source_path=pathlib.Path(__file__).with_name(KERNEL_SOURCES[kernel_variant])", "source_path=ROOT/'topics/padua-argmax-bridge-20261105/code/cheap_rows_C06/partial.cpp'")
ns={'__file__':str(OLD)}
exec(compile(text,str(OLD), 'exec'),ns)
def cpu():
 return sum(resource.getrusage(k).ru_utime+resource.getrusage(k).ru_stime for k in (resource.RUSAGE_SELF,resource.RUSAGE_CHILDREN))
start=cpu()
# Hard total CPU cap (parent plus compiler children via explicit elapsed checks).
resource.setrlimit(resource.RLIMIT_CPU,(180,180))
binary,manifest=ns['build']();lib=ctypes.CDLL(str(binary))
for name in ('c06_partial','c06_compare'):
 f=getattr(lib,name);f.argtypes=[ctypes.c_long,ctypes.c_long,ctypes.c_char_p,ctypes.POINTER(ctypes.c_double)];f.restype=ctypes.c_int
before=ns['loaded_closure'](manifest)
lib.c06_budget.argtypes=[ctypes.c_long,ctypes.c_long,ctypes.POINTER(ctypes.c_double)]
import mpmath as mp
mp.mp.dps=100
cases=[]
for n in (2,3,4,8,16,32,64):
 for q,y in [(0,'0'),(1,'0.5'),(n,'0.5'),(n-1,'1'),(1,'1e-30'),(n-1,'1e-30'),(1,str(n-1)+'.999999999999999999999999999999'),(min(5,n-1),'0.25')]:
  a=(ctypes.c_double*3)();rc=lib.c06_compare(n,q,y.encode(),a)
  bounds=(ctypes.c_double*3)(); assert lib.c06_partial(n,q,y.encode(),bounds)==0
  refmp=sum(mp.cot(mp.pi*(mp.mpf(y)+i)/n) for i in range(q))
  assert mp.mpf(bounds[0])<=refmp<=mp.mpf(bounds[1])
  budget=(ctypes.c_double*3)();lib.c06_budget(n,q,budget)
  cases.append(dict(n=n,q=q,y=y,rc=rc,overlap=bool(a[0]),contains_reference=bool(a[1]),radius=a[2],budget=list(budget),mpmath_enclosed=True))
  if rc or not a[0] or not a[1]:raise RuntimeError(cases[-1])
  if cpu()-start>180:raise RuntimeError('CPU budget exceeded')
a=(ctypes.c_double*3)()
invalid=[lib.c06_partial(1,1,b'.5',a),lib.c06_partial(2,1,b'0',a),lib.c06_partial(2,1,b'2',a)]
assert all(invalid)
after=ns['loaded_closure'](manifest);assert before==after
manifest.update(api_header=ns['identity'](HERE/'partial.h'),builder=ns['identity'](OLD),mpmath_version=mp.__version__,actual_loaded_closure=after,driver=ns['identity'](__file__),cases=cases,cpu_seconds=cpu()-start,invalid_rejections=invalid)
raw=pathlib.Path(manifest['workdir'])/'controls.json';raw.write_text(json.dumps(manifest,indent=2)+'\n')
receipt={'scope':'C02 partial-cotangent backend only; no point S / arcs / boxes','precision':160,'reference_precision':512,'coefficient_precision':640,'J':48,'K':32,'Lh':16,'wp_degree':96,'cases':len(cases),'overlaps':sum(c['overlap'] for c in cases),'contains_reference':sum(c['contains_reference'] for c in cases),'max_radius':max(c['radius'] for c in cases),'regular_max_radius':max(c['radius'] for c in cases if '999999' not in c['y'] and c['y']!='1e-30'),'max_analytic_budgets':[max(c['budget'][i] for c in cases) for i in range(3)],'mpmath_enclosed':sum(c['mpmath_enclosed'] for c in cases),'cpu_seconds':manifest['cpu_seconds'],'source':ns['identity'](HERE/'partial.cpp'),'driver':ns['identity'](__file__),'builder':ns['identity'](OLD),'api_header':ns['identity'](HERE/'partial.h'),'raw_manifest':ns['identity'](raw),'binary':manifest['checker_binary'],'closure_entries':{k:len(manifest[k]) for k in ('headers','toolchain','toolchain_dependency_closure','linked_dependency_closure','actual_loaded_closure')},'invalid_rejections':invalid,'analytic_errors':'C02 smooth bound plus both harmonic EM radii; wprime series derivative geometric tail; all arithmetic outward Arb'}
out=HERE.parents[1]/'evidence/c06-rows-partial.json';out.write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt,indent=2))
