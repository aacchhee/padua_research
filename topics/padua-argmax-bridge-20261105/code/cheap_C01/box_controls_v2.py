#!/usr/bin/env python3
"""Selected saved failures plus four synthetic boxes; never a cover/checker."""
import ctypes, json, pathlib, resource, time
from fractions import Fraction as F
import build_prototype as build

def main():
    resource.setrlimit(resource.RLIMIT_CPU,(100,105));start=time.process_time();wall=time.monotonic();ch=resource.getrusage(resource.RUSAGE_CHILDREN)
    base=build.ROOT/'local-output/argmax-bridge-20261105';outdir=base/'cheap-C01/prototype';target=outdir/'box-controls-v2.json'
    if target.exists():raise RuntimeError('refuse existing box controls')
    unitpath=outdir/'unit-controls-v2.json';unit=json.loads(unitpath.read_text())
    if unit['status']!='PASS':raise RuntimeError('units not passed')
    manifest=unit['build']
    for key in ('source_snapshot','preprocessed_translation_unit','checker_binary'):
        if build.pinned.identity(manifest[key]['path'])!=manifest[key]:raise RuntimeError('frozen build mutation')
    if build.pinned.identity(build.HERE/'prototype.cpp')!=unit['source']:raise RuntimeError('source mutation')
    lib=ctypes.CDLL(manifest['checker_binary']['path']);ptr=ctypes.POINTER(ctypes.c_double)
    fn=lib.phase_bounds;fn.argtypes=[ctypes.c_int]+[ctypes.c_double]*4+[ptr];fn.restype=ctypes.c_int
    counts=lib.c01_counts;counts.argtypes=[ptr];counts.restype=None
    oldpath=base/'phase-r9/bounded-report.json';saved=json.loads(oldpath.read_text())
    cases=[dict(n=32,box=x['box'],reference=x['new_bounds'],kind='saved n32 former failure',root=x['root'],path=x['path']) for x in saved['selected_failed_leaves']]
    profilepath=base/'cheap-C01/profile.json';baseline=json.loads(profilepath.read_text())
    for n in (64,128):
        old=next(x for x in baseline['results'] if x['n']==n)
        cases.append(dict(n=n,box=old['box'],reference=old['bounds'],kind='same synthetic narrow box',baseline_cpu=old['cpu']))
        cases.append(dict(n=n,box=[0.,.25,0.,.25],kind='synthetic full half-radius square'))
    results=[];failure=None
    try:
        for case in cases:
            if time.process_time()-start>80:raise RuntimeError('prospective stop before next box')
            t=time.process_time();w=time.monotonic();out=(ctypes.c_double*7)();rc=fn(case['n'],*case['box'],out);c=(ctypes.c_double*8)();counts(c)
            record=dict(case,status=rc,bounds=list(out),counts=list(c),cpu=time.process_time()-t,wall=time.monotonic()-w)
            if not rc:
                record['S_strict_corner']=F(out[0])<F(out[3]);record['S_minus_defect_strict_corner']=F(out[0])-F(out[2])<F(out[3])
                if 'reference' in case:
                    ref=case['reference'];record['upper_changes']={str(i):out[i]-ref[i] for i in (0,1,4,6)};record['lower_changes']={str(i):out[i]-ref[i] for i in (2,3,5)}
            results.append(record);print(json.dumps(record),flush=True)
            if rc:raise RuntimeError('native case status '+str(rc))
        for group in ('toolchain','toolchain_dependency_closure','headers','dependency_inputs','linked_dependency_closure'):
            if any(build.pinned.identity(e['path'])!=e for e in manifest[group]):raise RuntimeError('closure mutation')
    except Exception as exc:failure=repr(exc)
    endch=resource.getrusage(resource.RUSAGE_CHILDREN)
    report=dict(status='FAIL' if failure else 'MEASURED',failure=failure,results=results,source=unit['source'],control=build.pinned.identity(pathlib.Path(__file__)),unit_receipt=build.pinned.identity(unitpath),saved_receipt=build.pinned.identity(oldpath),baseline_receipt=build.pinned.identity(profilepath),own_cpu=time.process_time()-start,child_cpu=(endch.ru_utime+endch.ru_stime)-(ch.ru_utime+ch.ru_stime),wall=time.monotonic()-wall,whole_candidate_replayed=False,exit_status=int(failure is not None))
    target.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:report[k] for k in ('status','failure','own_cpu','child_cpu','wall')}));return int(failure is not None)
if __name__=='__main__':raise SystemExit(main())
