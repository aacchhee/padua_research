#!/usr/bin/env python3
"""Bounded fixed-work ratio controls, no candidate or box traversal."""
import ctypes, json, math, pathlib, resource, time
import mpmath as mp
import build_prototype as build

def main():
    resource.setrlimit(resource.RLIMIT_CPU,(90,95));start=time.process_time();wall=time.monotonic();ch=resource.getrusage(resource.RUSAGE_CHILDREN)
    outdir=build.ROOT/'local-output/argmax-bridge-20261105/cheap-C01/prototype';outdir.mkdir(parents=True,exist_ok=True);target=outdir/'unit-controls.json'
    if target.exists():raise RuntimeError('refuse controls overwrite')
    records=[];failure=None;manifest=None;assertions=0
    def test(ok,label):
        nonlocal assertions
        assertions+=1
        if not ok:raise AssertionError(label)
    try:
        binary,manifest,loaded=build.build();lib=ctypes.CDLL(str(binary));manifest['loaded_dependency_closure']=loaded(manifest)
        ptr=ctypes.POINTER(ctypes.c_double);ratio=lib.phase_ratio;ratio.argtypes=[ctypes.c_int,ctypes.c_int,ctypes.c_double,ctypes.c_double,ptr,ctypes.POINTER(ctypes.c_int)];ratio.restype=ctypes.c_int
        mp.mp.dps=85
        cases=[]
        for k in (1,2,17,32,128,512,513):
            for turn in (-3,0,2):
                cases.extend((k,turn,l,h) for l,h in ((0.,0.),(-.00001,.00002),(.125,.125),(-5.,5.)))
        cases.extend([(32,0,math.pi/32,math.pi/32),(513,1,-.01,.01),(2,0,-1.5,1.5),(2,0,-1.5001,1.5001)])
        for k,turn,l,h in cases:
            out=(ctypes.c_double*8)();used=ctypes.c_int();rc=ratio(k,turn,l,h,out,ctypes.byref(used));record=dict(k=k,turn=turn,lo=l,hi=h,status=rc,chart=used.value,bounds=list(out));records.append(record)
            test(rc==0,'finite valid ratio status');test(all(math.isfinite(v) for v in out),'finite ratio pair')
            for offset in (mp.mpf(l),(mp.mpf(l)+mp.mpf(h))/2,mp.mpf(h)):
                z=mp.pi*turn+offset
                value=mp.fsum(mp.cos((k-1-2*j)*z) for j in range(k));deriv=mp.fsum(-(k-1-2*j)*mp.sin((k-1-2*j)*z) for j in range(k))
                # Exact mathematical pole values avoid finite mp pi residue noise.
                if not offset:value=mp.mpf((-1 if turn%2 and k%2==0 else 1)*k);deriv=mp.mpf(0)
                test(mp.mpf(out[0])<=value<=mp.mpf(out[1]),'direct harmonic value sample enclosed')
                test(mp.mpf(out[2])<=deriv<=mp.mpf(out[3]),'direct harmonic derivative sample enclosed')
            if k==1:test(list(out[:4])==[1.,1.,0.,0.],'R1 exact')
        for k,turn,l,h in ((1,0,math.nan,0.),(1,0,0.,math.inf),(1,0,1.,0.),(0,0,0.,0.),(514,0,0.,0.)):
            o=(ctypes.c_double*8)();u=ctypes.c_int();rc=ratio(k,turn,l,h,o,ctypes.byref(u));records.append(dict(invalid=[k,turn,str(l),str(h)],status=rc));test(rc!=0,'invalid ratio rejected before R1 shortcut')
        fallback=lib.phase_nonfinite_refinement_control;fallback.argtypes=[ctypes.c_int,ptr];fallback.restype=ctypes.c_int
        for which in (0,1):
            o=(ctypes.c_double*4)();test(fallback(which,o)==0 and list(o)==[1.,1.,0.,0.],'nonfinite pair staging unchanged')
        test(fallback(2,(ctypes.c_double*4)())==3,'finite pair contradiction errors')
        test(lib.phase_disjoint_intersection_control()==3,'disjoint finite intersection errors')
        counts=(ctypes.c_double*8)();lib.c01_counts.argtypes=[ptr];lib.c01_counts(counts)
        for key in ('toolchain','toolchain_dependency_closure','headers','dependency_inputs','linked_dependency_closure','loaded_dependency_closure'):
            test(all(build.pinned.identity(e['path'])==e for e in manifest[key]),'closure stable '+key)
    except Exception as exc:failure=repr(exc)
    endch=resource.getrusage(resource.RUSAGE_CHILDREN)
    report=dict(status='FAIL' if failure else 'PASS',failure=failure,assertions=assertions,records=records,build=manifest,source=build.pinned.identity(build.HERE/'prototype.cpp'),control=build.pinned.identity(pathlib.Path(__file__)),builder=build.pinned.identity(build.HERE/'build_prototype.py'),own_cpu=time.process_time()-start,child_cpu=(endch.ru_utime+endch.ru_stime)-(ch.ru_utime+ch.ru_stime),wall=time.monotonic()-wall,counts=list(counts) if 'counts' in locals() else None,whole_candidate_replayed=False)
    target.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:report[k] for k in ('status','failure','assertions','own_cpu','child_cpu','wall')}));return int(failure is not None)
if __name__=='__main__':raise SystemExit(main())
