#!/usr/bin/env python3
"""Focused review of the author geometry guard; no ratio or box calls."""
import ctypes, importlib.util, json, math, resource, tempfile, time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];TOPIC=ROOT/'topics/padua-argmax-bridge-20261105'
HERE=TOPIC/'code/cheap_C08_mpfr'
spec=importlib.util.spec_from_file_location('c08_geometry_builder',HERE/'build.py')
build=importlib.util.module_from_spec(spec);spec.loader.exec_module(build)

def main():
    resource.setrlimit(resource.RLIMIT_CPU,(10,12));start=time.process_time();before=resource.getrusage(resource.RUSAGE_CHILDREN)
    target=TOPIC/'evidence/c08-review-mpfr-geometry.json'
    if target.exists():raise RuntimeError('refuse geometry review overwrite')
    assertions=0;records=[];failure=None;manifest=None
    def test(ok,label):
        nonlocal assertions
        assertions+=1
        if not ok:raise AssertionError(label)
    try:
        previous=json.loads((TOPIC/'evidence/c08-review-mpfr.json').read_text())
        oldraw=json.loads(Path(previous['raw']['path']).read_text());oldsrc=Path(oldraw['build']['source']['path']).read_text()
        source=build.identity(HERE/'producer.c');header=build.identity(HERE/'c08_interval.h')
        test(source['sha256']=='270eb7b0f073efcb996c7c832f6e946d37b0e6f780fdac63fc66591332560a5e','new source pin')
        test(header['sha256']=='275936b502180f2d92af94eb2138815114ba75afb9c258cadffa44e580be0a03','unchanged header')
        new=(HERE/'producer.c').read_text()
        oldgeometry=oldsrc[oldsrc.index('int n3_geometry('):oldsrc.index('const char *n3_mpfr_version')]
        newgeometry=new[new.index('int n3_geometry('):new.index('const char *n3_mpfr_version')]
        test(oldsrc.replace(oldgeometry,newgeometry)==new,'only geometry function differs')
        # Inspectable literal deletion/reinsertion proves old arithmetic is intact.
        declaration='double aa=fmax(fabs(al),fabs(ah)),bb=fmax(fabs(bl),fabs(bh));'
        guard='if(aa>4||bb>4)return 3;'
        compact=lambda s:''.join(s.split())
        test(compact(newgeometry).replace(compact(guard),'').replace(compact(declaration),'')==
             compact(oldgeometry).replace(compact(declaration),''),'only exact endpoint-domain guard added')
        ids=[source,header,build.identity(HERE/'build.py'),build.identity(__file__),build.identity(TOPIC/'evidence/c08-review-mpfr.json')]
        binary,manifest=build.build();lib=ctypes.CDLL(str(binary));manifest['actual_loaded_mappings']=build.loaded(manifest)
        geometry=lib.n3_geometry;geometry.argtypes=[ctypes.c_int]+[ctypes.c_double]*4;geometry.restype=ctypes.c_int
        oldlib=ctypes.CDLL(oldraw['build']['binary']['path']);old=oldlib.n3_geometry;old.argtypes=geometry.argtypes;old.restype=ctypes.c_int
        # Capture both loaded libraries after the second load, then freeze that map.
        manifest['actual_loaded_mappings']=build.loaded(manifest)
        p=math.nextafter(math.pi,math.inf);u=math.nextafter(4.,math.inf)
        cases=[(2,[-8*math.pi,8*math.pi,0.,0.],3,'original-counterexample'),
               (2,[-4.,4.,0.,0.],0,'closed-alpha-boundary'),(2,[0.,0.,-4.,4.],0,'closed-beta-boundary'),
               (2,[-u,u,0.,0.],3,'alpha-one-ulp-beyond'),(2,[0.,0.,-u,u],3,'beta-one-ulp-beyond'),
               (2,[3.5,3.5,0.,0.],1,'outside'),(2,[0.,0.,0.,0.],2,'local-zero'),
               (2,[-1e-8,1e-8,-1e-8,1e-8],2,'local-small'),
               (1,[0.,0.,0.,0.],3,'invalid-degree'),(513,[0.,0.,0.,0.],3,'invalid-degree'),
               (2,[1.,0.,0.,0.],3,'reversed'),(2,[math.nan,0.,0.,0.],3,'nan'),
               (2,[0.,math.inf,0.,0.],3,'infinite')]
        for n in (2,32,512):
            for a in ((-p,0.),(0.,p)):
                for b in ((-p,0.),(0.,p)):cases.append((n,[*a,*b],0,'original-root'))
        for n,b,expected,label in cases:
            got=geometry(n,*b);prior=old(n,*b)
            records.append(dict(n=n,box=[v if math.isfinite(v) else str(v) for v in b],label=label,old=prior,new=got,expected=expected))
            test(got==expected,label)
            if all(math.isfinite(v) and abs(v)<=4 for v in b):test(got==prior,'in-domain behavior unchanged')
        for group in ('tools','tool_runtime_closure','headers','linked_runtime_closure','actual_loaded_mappings'):build.verify(manifest[group])
        build.verify(ids+[manifest[k] for k in ('source','header','preprocessed','binary')]+[oldraw['build']['binary']])
        test(build.loaded(manifest)==manifest['actual_loaded_mappings'],'actual mappings stable')
    except Exception as exc:failure=repr(exc)
    after=resource.getrusage(resource.RUSAGE_CHILDREN)
    full=dict(status='FAIL' if failure else 'PASS',failure=failure,assertions=assertions,records=records,
              build=manifest,own_cpu=time.process_time()-start,child_cpu=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime)
    raw=Path(tempfile.mkstemp(prefix='c08-geometry-review-',suffix='.json')[1]);raw.write_text(json.dumps(full,indent=2)+'\n')
    summary={k:full[k] for k in ('status','failure','assertions','own_cpu','child_cpu')}
    summary.update(raw=build.identity(raw),source=build.identity(HERE/'producer.c'),header=build.identity(HERE/'c08_interval.h'),control=build.identity(__file__),geometry_cases=len(records),ratio_calls=0,box_calls=0,full_producer_run=False)
    with target.open('x') as f:json.dump(summary,f,indent=2);f.write('\n')
    print(json.dumps(summary,indent=2));return int(failure is not None)

if __name__=='__main__':raise SystemExit(main())
