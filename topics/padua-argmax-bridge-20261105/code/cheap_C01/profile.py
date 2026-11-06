#!/usr/bin/env python3
"""Frozen C01 diagnostic: separate instrumented v3, selected boxes only."""
import ctypes, hashlib, importlib.util, json, pathlib, resource, sys, time
ROOT=pathlib.Path(__file__).resolve().parents[4]
HERE=pathlib.Path(__file__).resolve().parent
OLD=HERE.parent/'phase_checker'
OUT=ROOT/'local-output/argmax-bridge-20261105/cheap-C01'
sys.path.insert(0,str(OLD))
import build_snapshot_r9 as build
import check_r8 as acceptance

def ident(p):return build.identity(p)
def main():
    resource.setrlimit(resource.RLIMIT_CPU,(150,155))
    start=time.process_time();wall=time.monotonic();ch=resource.getrusage(resource.RUSAGE_CHILDREN)
    OUT.mkdir(parents=True,exist_ok=True)
    target=OUT/'profile.json'
    if target.exists():raise RuntimeError('refusing existing profile output')
    original=OLD/'hybrid_kernel_v3.cpp';src=original.read_text()
    prefix='''\n#include <ctime>
static double cp(){timespec t;clock_gettime(CLOCK_PROCESS_CPUTIME_ID,&t);return t.tv_sec+1e-9*t.tv_nsec;}
static double stats[12]={};
struct Scope{int i;double t;Scope(int j):i(j),t(cp()){}~Scope(){stats[i]+=cp()-t;}};
extern "C" void c01_stats(double*out){for(int i=0;i<12;i++){out[i]=stats[i];stats[i]=0;}}
'''
    src=src.replace('static constexpr slong P=160;',prefix+'\nstatic constexpr slong P=160;')
    replacements=[
    (' r0=B((n%2)?1:0);',' Scope timer(0);stats[4]++;stats[5]+=n;\n r0=B((n%2)?1:0);'),
    (' r=intersect(r,range(-k,k));',' Scope timer(1);stats[6]++;\n r=intersect(r,range(-k,k));'),
    (' B sk,ck,kz=z*B(k);',' stats[7]++;\n B sk,ck,kz=z*B(k);'),
    (' B pi;arb_const_pi(pi.x,P);int m=n+1;',' Scope timer(2);stats[8]++;stats[9]+=2*n*(n+1);\n B pi;arb_const_pi(pi.x,P);int m=n+1;'),
    (' const std::vector<Jet>&h,const std::vector<Jet>&c,const std::vector<Jet>&z,double*out){',' const std::vector<Jet>&h,const std::vector<Jet>&c,const std::vector<Jet>&z,double*out){\n Scope timer(3);stats[10]++;stats[11]+=2*n*(n+1)*(2*n+3);')]
    for a,b in replacements:
        if src.count(a)!=1:raise RuntimeError('unexpected source anchor count')
        src=src.replace(a,b)
    generated=OUT/'instrumented.cpp';generated.write_text(src)
    # Reuse pinned snapshot/closure builder, with new explicit source/destination.
    builder=pathlib.Path(build.__file__).read_text().replace("LOCAL=ROOT/'local-output/argmax-bridge-20261105/phase-r9'","LOCAL=ROOT/'local-output/argmax-bridge-20261105/cheap-C01'")
    builder=builder.replace("source_path=pathlib.Path(__file__).with_name(KERNEL_SOURCES[kernel_variant])","source_path=LOCAL/'instrumented.cpp'")
    namespace={'__file__':str(OLD/'build_snapshot_r9.py')};exec(compile(builder,'<c01-build-snapshot>','exec'),namespace)
    binary,manifest=namespace['build']();lib=ctypes.CDLL(str(binary));manifest['loaded_dependency_closure']=namespace['loaded_closure'](manifest)
    ptr=ctypes.POINTER(ctypes.c_double);fn=lib.phase_bounds;fn.argtypes=[ctypes.c_int]+[ctypes.c_double]*4+[ptr];fn.restype=ctypes.c_int
    stats=lib.c01_stats;stats.argtypes=[ptr];stats.restype=None
    cases=[];inputs=[]
    paths=[(17,'N3/outward-full-n17-r3/n17-phase-compact.json'),(24,'N3/outward-r6/n24/n24-phase-compact.json'),(32,'bootstrap-r8/n32/n32-phase-compact.json')]
    base=ROOT/'local-output/argmax-bridge-20261105'
    for n,p in paths:
        path=base/p;data=json.loads(path.read_bytes());inputs.append(ident(path))
        leaf=next(x for x in data['leaves'] if x['kind'] != 'outside')
        cases.append((n,acceptance.box_for(data['roots'],leaf['root'],leaf['path']),'first saved nonlocal leaf'))
    cases.extend((n,[.125,.1328125,.25,.2578125],'synthetic fixed box') for n in (64,128))
    results=[]
    for n,b,label in cases:
        if time.process_time()-start>120:break
        t=time.process_time();w=time.monotonic();out=(ctypes.c_double*7)();rc=fn(n,*b,out);s=(ctypes.c_double*12)();stats(s)
        record=dict(n=n,box=b,scope=label,status=rc,bounds=list(out),cpu=time.process_time()-t,wall=time.monotonic()-w,stats=list(s));results.append(record);print(json.dumps(record),flush=True)
        if rc:break
    for group in ('toolchain','toolchain_dependency_closure','headers','dependency_inputs','linked_dependency_closure','loaded_dependency_closure'):
        if any(ident(e['path'])!=e for e in manifest[group]):raise RuntimeError('closure mutation')
    children=resource.getrusage(resource.RUSAGE_CHILDREN)
    report=dict(status='MEASURED',source=ident(original),instrumentation=ident(pathlib.Path(__file__)),generated_source=ident(generated),builder=ident(pathlib.Path(build.__file__)),inputs=inputs,build=manifest,results=results,stats_order=['harmonic_cpu','refine_cpu','board_cpu','collect_cpu','ratio_calls','harmonic_iterations','refine_calls','quotient_attempts','board_calls','primitive_calls','collect_calls','pair_visits'],own_cpu=time.process_time()-start,child_cpu=(children.ru_utime+children.ru_stime)-(ch.ru_utime+ch.ru_stime),wall=time.monotonic()-wall,exit_status=0)
    target.write_text(json.dumps(report,indent=2)+'\n');print('receipt '+str(target),flush=True)
if __name__=='__main__':main()
